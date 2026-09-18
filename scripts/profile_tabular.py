#!/usr/bin/env python3
"""Privacy-conscious first-pass profiler for CSV, Parquet, and Excel tables.

Requires pandas. Excel formats require the relevant pandas engine.
Outputs JSON and never modifies the source.

Safe defaults:
- CSV/Excel are read as text where practical.
- pandas default NA strings such as "NA" are NOT silently converted in safe mode.
- blank strings are counted separately from null values.
- raw/top values are not emitted unless --include-values is explicitly set.
- formula-like text is counted for review; this script does not sanitize it.
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


def numeric_summary(pd, s, include_values: bool) -> dict | None:
    parsed = pd.to_numeric(s, errors="coerce")
    nonnull_source = s.notna().sum()
    if nonnull_source == 0:
        return None

    valid = parsed.notna().sum()
    result = {"numeric_parse_rate": float(valid / nonnull_source)}
    if valid and include_values:
        result["numeric_min"] = safe_scalar(parsed.min())
        result["numeric_max"] = safe_scalar(parsed.max())
    return result


def text_risk_counts(s) -> dict[str, int]:
    values = s.dropna().astype(str)
    if values.empty:
        return {
            "formula_like_text_count": 0,
            "dash_prefixed_text_count": 0,
            "control_prefixed_text_count": 0,
        }

    return {
        # Stronger spreadsheet formula-entry signals.
        "formula_like_text_count": int(values.str.match(r"^[=+@]").sum()),
        # Separate because legitimate negative numbers are common.
        "dash_prefixed_text_count": int(values.str.startswith("-").sum()),
        # Tabs/CR can matter in CSV/spreadsheet injection contexts.
        "control_prefixed_text_count": int(values.str.match(r"^[\t\r]").sum()),
    }


def blank_count(s) -> int:
    nonnull = s.dropna()
    if nonnull.empty:
        return 0
    try:
        return int(nonnull.astype(str).str.strip().eq("").sum())
    except Exception:
        return 0


def profile_df(pd, df, top_n: int, include_values: bool) -> dict:
    out = {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "duplicate_rows": int(df.duplicated().sum()),
        "values_included": bool(include_values),
        "column_profiles": [],
    }

    for col in df.columns:
        s = df[col]
        p = {
            "name": str(col),
            "dtype": str(s.dtype),
            "null_count": int(s.isna().sum()),
            "null_rate": float(s.isna().mean()) if len(s) else 0.0,
            "blank_count": blank_count(s),
            "unique_count": int(s.nunique(dropna=True)),
            **text_risk_counts(s),
        }

        nonnull = s.dropna()
        if len(nonnull):
            try:
                vc = nonnull.astype(str).value_counts().head(top_n)
                if len(vc):
                    p["most_common_count"] = int(vc.iloc[0])
                    p["most_common_share"] = float(vc.iloc[0] / len(nonnull))
                if include_values:
                    p["top_values"] = [
                        {"value": str(idx), "count": int(cnt)}
                        for idx, cnt in vc.items()
                    ]
            except Exception:
                pass

            if include_values:
                try:
                    p["sample_min"] = safe_scalar(nonnull.min())
                    p["sample_max"] = safe_scalar(nonnull.max())
                except Exception:
                    pass

            try:
                summary = numeric_summary(pd, s, include_values=include_values)
                if summary:
                    p.update(summary)
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
        help="Allow pandas dtype/NA inference instead of safe text-preserving ingestion.",
    )
    parser.add_argument(
        "--include-values",
        action="store_true",
        help="Include top/raw summary values in JSON. Off by default to reduce sensitive-data exposure.",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="CSV text encoding. Default: utf-8. Set explicitly for legacy encodings.",
    )
    parser.add_argument(
        "--sep",
        default=",",
        help='CSV separator. Default ",". Use "auto" for pandas/Python delimiter inference.',
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
        kwargs = {
            "low_memory": False,
            "encoding": args.encoding,
        }

        if args.sep == "auto":
            kwargs["sep"] = None
            kwargs["engine"] = "python"
            kwargs.pop("low_memory", None)
        else:
            kwargs["sep"] = args.sep

        if preserve_text:
            # Preserve literal strings such as "NA", "NULL", and leading-zero IDs.
            # Empty fields remain empty strings and are reported via blank_count.
            kwargs.update({
                "dtype": str,
                "keep_default_na": False,
                "na_filter": False,
            })

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
            kwargs.update({
                "dtype": str,
                "keep_default_na": False,
                "na_filter": False,
            })

        df = pd.read_excel(path, **kwargs)

    else:
        raise SystemExit(f"Unsupported format: {ext}")

    result = {
        "path": str(path),
        "sheet": args.sheet,
        "read_mode": "pandas-inferred" if args.infer_types else "preserve-text-where-practical",
        "row_limit": args.nrows,
        "csv_encoding": args.encoding if ext == ".csv" else None,
        "csv_separator": args.sep if ext == ".csv" else None,
        **profile_df(pd, df, args.top, args.include_values),
        "limitations": [
            "Automated profiling is triage, not final analytical judgment.",
            "Safe CSV/Excel mode preserves literal text/blank strings instead of applying pandas default NA labels.",
            "Raw/top values are excluded unless --include-values is explicitly enabled.",
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
