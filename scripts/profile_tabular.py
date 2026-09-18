#!/usr/bin/env python3
"""First-pass profiler for CSV, Parquet, and Excel tables.

Requires pandas. Excel formats require the relevant pandas engine.
Outputs JSON and never modifies the source.

Safety default:
- CSV/Excel values are read as strings where practical to preserve identifiers
  such as 00123. Use --infer-types only when pandas inference is desired.
- Formula-like text is counted for review; this script does not sanitize it.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def safe_scalar(v):
    try:
        if hasattr(v, "item"):
            v = v.item()
    except Exception:
        pass
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    return str(v)


def numeric_summary(pd, s):
    parsed = pd.to_numeric(s, errors="coerce")
    nonnull_source = s.notna().sum()
    if nonnull_source == 0:
        return None
    valid = parsed.notna().sum()
    result = {"numeric_parse_rate": float(valid / nonnull_source)}
    if valid:
        result["numeric_min"] = safe_scalar(parsed.min())
        result["numeric_max"] = safe_scalar(parsed.max())
    return result


def spreadsheet_text_risk_counts(s) -> dict[str, int]:
    # =, +, and @ are stronger formula-like text signals.
    # Leading '-' is tracked separately because negative numbers are legitimate.
    values = s.dropna().astype(str)
    if values.empty:
        return {
            "formula_like_text_count": 0,
            "dash_prefixed_text_count": 0,
        }
    return {
        "formula_like_text_count": int(values.str.match(r"^[=+@]").sum()),
        "dash_prefixed_text_count": int(values.str.startswith("-").sum()),
    }


def profile_df(pd, df, top_n: int) -> dict:
    out = {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "duplicate_rows": int(df.duplicated().sum()),
        "column_profiles": [],
    }

    for col in df.columns:
        s = df[col]
        p = {
            "name": str(col),
            "dtype": str(s.dtype),
            "null_count": int(s.isna().sum()),
            "null_rate": float(s.isna().mean()) if len(s) else 0.0,
            "unique_count": int(s.nunique(dropna=True)),
            **spreadsheet_text_risk_counts(s),
        }

        nonnull = s.dropna()
        if len(nonnull):
            try:
                p["sample_min"] = safe_scalar(nonnull.min())
                p["sample_max"] = safe_scalar(nonnull.max())
            except Exception:
                pass
            try:
                vc = nonnull.astype(str).value_counts().head(top_n)
                p["top_values"] = [{"value": str(idx), "count": int(cnt)} for idx, cnt in vc.items()]
            except Exception:
                pass
            try:
                nsum = numeric_summary(pd, s)
                if nsum:
                    p.update(nsum)
            except Exception:
                pass

        out["column_profiles"].append(p)

    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--sheet")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument(
        "--nrows",
        type=int,
        default=None,
        help="Optional row limit for first-pass profiling of very large CSV/Excel files.",
    )
    parser.add_argument(
        "--infer-types",
        action="store_true",
        help="Allow pandas dtype inference instead of preserving CSV/Excel values as strings.",
    )
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    try:
        import pandas as pd
    except ImportError:
        raise SystemExit("pandas is required: pip install pandas")

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    ext = path.suffix.lower()
    preserve_text = not args.infer_types

    if ext == ".csv":
        kwargs = {"low_memory": False}
        if preserve_text:
            kwargs.update({"dtype": str, "keep_default_na": True})
        if args.nrows is not None:
            kwargs["nrows"] = args.nrows
        df = pd.read_csv(path, **kwargs)
    elif ext in {".parquet", ".pq"}:
        df = pd.read_parquet(path)
    elif ext in {".xlsx", ".xlsm", ".xls", ".xlsb"}:
        kwargs = {"sheet_name": args.sheet or 0}
        if args.nrows is not None:
            kwargs["nrows"] = args.nrows
        if preserve_text:
            kwargs["dtype"] = str
        df = pd.read_excel(path, **kwargs)
    else:
        raise SystemExit(f"Unsupported format: {ext}")

    result = {
        "path": str(path.resolve()),
        "sheet": args.sheet,
        "read_mode": "pandas-inferred" if args.infer_types else "preserve-text-where-practical",
        "row_limit": args.nrows,
        **profile_df(pd, df, args.top),
        "limitations": [
            "Automated profiling is triage, not final analytical judgment.",
            "CSV/Excel safe mode preserves text to reduce identifier loss; numeric_parse_rate is only a diagnostic.",
            "formula_like_text_count is a review signal, not proof of malicious content.",
            "dash_prefixed_text_count is separate because legitimate negative numbers are common.",
            "Excel cell storage/type semantics can still require workbook-aware inspection.",
            "Large files may require selective columns, chunks, Polars, or DuckDB.",
        ],
    }

    print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
