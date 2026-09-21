#!/usr/bin/env python3
"""Privacy-conscious semantic diff for tabular files.

Supported: CSV, XLSX/XLSM/XLS/XLSB (via pandas engines), Parquet.
CSV/Excel values are preserved as text by default to avoid identifier loss.

Without --include-values, row-key samples are hashed and changed cell values are
not emitted. This utility is intended for QA/triage, not as a replacement for a
business-specific reconciliation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import pandas as pd

SUPPORTED = {".csv", ".xlsx", ".xlsm", ".xls", ".xlsb", ".parquet", ".pq"}


def read_table(path: Path, sheet: str | int | None, infer_types: bool) -> pd.DataFrame:
    ext = path.suffix.lower()

    if ext == ".csv":
        kwargs: dict[str, Any] = {"low_memory": False}
        if not infer_types:
            kwargs.update({"dtype": str, "keep_default_na": False, "na_filter": False})
        return pd.read_csv(path, **kwargs)

    if ext in {".xlsx", ".xlsm", ".xls", ".xlsb"}:
        kwargs = {"sheet_name": 0 if sheet is None else sheet}
        if not infer_types:
            kwargs.update({"dtype": str, "keep_default_na": False, "na_filter": False})
        return pd.read_excel(path, **kwargs)

    if ext in {".parquet", ".pq"}:
        return pd.read_parquet(path)

    raise ValueError(f"Unsupported format: {ext}")


def blank_mask(series: pd.Series) -> pd.Series:
    return series.isna() | series.astype("string").fillna("").str.strip().eq("")


def normalize_compare_value(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value)


def key_label(values: tuple[Any, ...], include_values: bool) -> str:
    raw = "".join(normalize_compare_value(v) for v in values)
    if include_values:
        return raw
    return "sha256:" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def dtype_map(df: pd.DataFrame) -> dict[str, str]:
    return {str(col): str(dtype) for col, dtype in df.dtypes.items()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("before")
    parser.add_argument("after")
    parser.add_argument("--key", action="append", default=[], help="Key column; repeat for composite keys.")
    parser.add_argument("--before-sheet")
    parser.add_argument("--after-sheet")
    parser.add_argument("--infer-types", action="store_true")
    parser.add_argument("--include-values", action="store_true", help="Include raw key/value samples. Off by default.")
    parser.add_argument("--sample", type=int, default=10)
    parser.add_argument("--fail-on-diff", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    before_path = Path(args.before)
    after_path = Path(args.after)
    for path in (before_path, after_path):
        if not path.exists():
            raise SystemExit(f"File not found: {path}")
        if path.suffix.lower() not in SUPPORTED:
            raise SystemExit(f"Unsupported format: {path.suffix}")

    before = read_table(before_path, args.before_sheet, args.infer_types)
    after = read_table(after_path, args.after_sheet, args.infer_types)

    before_cols = [str(c) for c in before.columns]
    after_cols = [str(c) for c in after.columns]
    before.columns = before_cols
    after.columns = after_cols

    added_cols = [c for c in after_cols if c not in before_cols]
    removed_cols = [c for c in before_cols if c not in after_cols]
    common_cols = [c for c in before_cols if c in after_cols]
    before_dtypes = dtype_map(before)
    after_dtypes = dtype_map(after)
    dtype_changes = {
        col: {"before": before_dtypes[col], "after": after_dtypes[col]}
        for col in common_cols
        if before_dtypes.get(col) != after_dtypes.get(col)
    }
    column_order_changed = before_cols != after_cols and not added_cols and not removed_cols
    schema_changed = bool(added_cols or removed_cols or dtype_changes or column_order_changed)

    result: dict[str, Any] = {
        "before": str(before_path),
        "after": str(after_path),
        "read_mode": "pandas-inferred" if args.infer_types else "preserve-text-where-practical",
        "rows": {"before": int(len(before)), "after": int(len(after)), "delta": int(len(after) - len(before))},
        "schema": {
            "added_columns": added_cols,
            "removed_columns": removed_cols,
            "common_columns": common_cols,
            "column_order_changed": column_order_changed,
            "dtype_changes": dtype_changes,
            "dtypes_before": before_dtypes,
            "dtypes_after": after_dtypes,
        },
        "key": None,
        "row_diff": {
            "status": "not_run",
            "message": "Provide one or more --key columns for row-level semantic comparison.",
        },
        "semantic_row_comparison_complete": False,
        "differences_detected": bool(schema_changed or len(before) != len(after)),
        "limitations": [
            "String-preserving comparison is intentional by default; use --infer-types only when typed comparison is desired.",
            "This utility compares tabular semantics, not business meaning.",
            "Duplicate or blank keys make row-level comparison ambiguous.",
            "Parquet retains native types unless --infer-types behavior is otherwise handled by pandas.",
        ],
    }

    keys = [str(k) for k in args.key]
    if keys:
        missing = [k for k in keys if k not in before.columns or k not in after.columns]
        if missing:
            raise SystemExit(f"Key columns missing from before/after: {missing}")

        before_blank = pd.Series(False, index=before.index)
        after_blank = pd.Series(False, index=after.index)
        for key in keys:
            before_blank |= blank_mask(before[key])
            after_blank |= blank_mask(after[key])

        before_dup = before.duplicated(keys, keep=False)
        after_dup = after.duplicated(keys, keep=False)

        key_info = {
            "columns": keys,
            "blank_rows_before": int(before_blank.sum()),
            "blank_rows_after": int(after_blank.sum()),
            "duplicate_rows_before": int(before_dup.sum()),
            "duplicate_rows_after": int(after_dup.sum()),
            "unique_before": int(before[keys].drop_duplicates().shape[0]),
            "unique_after": int(after[keys].drop_duplicates().shape[0]),
        }
        result["key"] = key_info

        ambiguous = bool(before_blank.any() or after_blank.any() or before_dup.any() or after_dup.any())
        if ambiguous:
            result["row_diff"] = {
                "status": "ambiguous_key",
                "message": "Row-level comparison skipped because key contains blanks or duplicates.",
            }
            result["differences_detected"] = True
            result["semantic_row_comparison_complete"] = False
        else:
            before_i = before.set_index(keys, drop=False)
            after_i = after.set_index(keys, drop=False)
            before_keys = set(before_i.index.tolist())
            after_keys = set(after_i.index.tolist())

            def as_tuple(value: Any) -> tuple[Any, ...]:
                return value if isinstance(value, tuple) else (value,)

            removed_keys = sorted(before_keys - after_keys, key=lambda x: str(x))
            added_keys = sorted(after_keys - before_keys, key=lambda x: str(x))
            common_keys = before_keys & after_keys

            compare_cols = [c for c in common_cols if c not in keys]
            changed_cells_by_column = {c: 0 for c in compare_cols}
            changed_rows: list[dict[str, Any]] = []

            for idx in sorted(common_keys, key=lambda x: str(x)):
                a = before_i.loc[idx]
                b = after_i.loc[idx]
                changed_cols: list[str] = []
                value_changes: dict[str, dict[str, str]] = {}
                for col in compare_cols:
                    av = normalize_compare_value(a[col])
                    bv = normalize_compare_value(b[col])
                    if av != bv:
                        changed_cells_by_column[col] += 1
                        changed_cols.append(col)
                        if args.include_values:
                            value_changes[col] = {"before": av, "after": bv}
                if changed_cols:
                    item: dict[str, Any] = {
                        "key": key_label(as_tuple(idx), args.include_values),
                        "columns": changed_cols,
                    }
                    if args.include_values:
                        item["values"] = value_changes
                    changed_rows.append(item)

            changed_cells_by_column = {k: v for k, v in changed_cells_by_column.items() if v}
            result["row_diff"] = {
                "status": "ok",
                "added_rows": len(added_keys),
                "removed_rows": len(removed_keys),
                "common_rows": len(common_keys),
                "changed_rows": len(changed_rows),
                "changed_cells_by_column": changed_cells_by_column,
                "sample_added_keys": [
                    key_label(as_tuple(x), args.include_values) for x in added_keys[: args.sample]
                ],
                "sample_removed_keys": [
                    key_label(as_tuple(x), args.include_values) for x in removed_keys[: args.sample]
                ],
                "sample_changed_rows": changed_rows[: args.sample],
            }

            result["semantic_row_comparison_complete"] = True
            if added_keys or removed_keys or changed_rows:
                result["differences_detected"] = True

    print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False, default=str))

    if args.fail_on_diff and result["differences_detected"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
