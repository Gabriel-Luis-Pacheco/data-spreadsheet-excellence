#!/usr/bin/env python3
"""Fail-closed, read-only EDIT_EXISTING workbook delivery gate.

The allowlist is supplied from a trusted task instruction. This gate does NOT
verify the allowlist's authority, business semantics, or Excel F3 UI behavior.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.utils.cell import column_index_from_string, range_boundaries


def _load(path):
    return load_workbook(path, data_only=False, read_only=False, keep_links=True,
                         keep_vba=path.suffix.lower() in {".xlsm", ".xltm"})


def _header(ws, row):
    return [(col, str(ws.cell(row, col).value))
            for col in range(1, ws.max_column + 1)
            if ws.cell(row, col).value is not None
            and str(ws.cell(row, col).value).strip()]


def _allowed_cell(row, col, ranges):
    for area in ranges:
        left, top, right, bottom = range_boundaries(area)
        if left <= col <= right and top <= row <= bottom:
            return True
    return False


def _style(cell):
    return (
        str(cell.font), str(cell.fill), str(cell.border), str(cell.alignment),
        cell.number_format, str(cell.protection),
    )


def _normalize(value):
    return " ".join(str(value).split()).upper() if value is not None else ""


def evaluate(contract, max_cells=400_000):
    if contract.get("mode") != "EDIT_EXISTING":
        raise ValueError("This gate supports EDIT_EXISTING only. Never claim other modes were verified.")
    original = Path(contract["original"])
    output = Path(contract["output"])
    if original.resolve() == output.resolve():
        raise ValueError("Original and output must be separate files")
    if not original.is_file() or not output.is_file():
        raise ValueError("Original/output file not found")
    header_rows = contract["header_rows"]
    if not isinstance(header_rows, dict) or not header_rows:
        raise ValueError("Specify source header_rows by sheet")
    allowed_sheets = set(contract.get("authorized_new_sheets", []))
    allowed_new = contract.get("authorized_new_headers", {})
    allowed_cells = contract.get("authorized_changed_ranges", {})
    status_rules = contract.get("allowed_status_values", {})
    errors = []
    warnings = []
    checked = 0
    before = _load(original)
    after = _load(output)
    try:
        a = set(after.sheetnames)
        b = set(before.sheetnames)
        for name in sorted(a - b - allowed_sheets):
            errors.append(f"Unapproved new sheet: {name}")
        for name in sorted(b - a):
            errors.append(f"Original sheet removed: {name}")
        if [x for x in after.sheetnames if x in b] != [x for x in before.sheetnames if x in a]:
            errors.append("Original sheet order changed")
        for sheet, row in header_rows.items():
            if not isinstance(row, int) or row < 1:
                raise ValueError(f"Bad header row for {sheet}")
            if sheet not in before.sheetnames:
                raise ValueError(f"Source header sheet missing: {sheet}")
        if set(before.sheetnames) - set(header_rows):
            raise ValueError("Must specify header row for EVERY original sheet; no partial comparison")
        if set(allowed_new) - set(header_rows) or set(allowed_cells) - set(header_rows):
            raise ValueError("Authorized changes refer to unknown source sheets")
        for sheet in before.sheetnames:
            if sheet not in after.sheetnames:
                continue
            ws, dst = before[sheet], after[sheet]
            row = header_rows[sheet]
            old = _header(ws, row)
            new = _header(dst, row)
            additions = allowed_new.get(sheet, [])
            if not isinstance(additions, list):
                raise ValueError(f"authorized_new_headers.{sheet} must be a list")
            approved = set()
            for item in additions:
                col = item.get("column")
                if isinstance(col, str):
                    col = column_index_from_string(col)
                if not isinstance(col, int) or col < 1:
                    raise ValueError("Authorized header needs exact Excel column index")
                if col in approved:
                    raise ValueError(f"Duplicated authorized header position {sheet}!{col}")
                approved.add(col)
                if (col, str(item.get("name", ""))) not in new:
                    errors.append(f"Authorized header absent/wrong position: {sheet}!{col}")
            expected = [name for _, name in old]
            actual = [name for col, name in new if col not in approved]
            if expected != actual:
                errors.append(f"Unexpected header/order changes in {sheet}: {expected!r} => {actual!r}")
            if len(old) + len(additions) != len(new):
                errors.append(f"Header count changed beyond permission on {sheet}")
            if any(col in {p for p, _ in old} for col in approved):
                # Insertion ahead of original fields is allowed only if explicitly configured
                # and the unchanged source field sequence remains intact.
                pass
            ranges = allowed_cells.get(sheet, [])
            if not isinstance(ranges, list):
                raise ValueError(f"authorized_changed_ranges.{sheet} must be list")
            for area in ranges:
                try:
                    range_boundaries(area)
                except (TypeError, ValueError) as exc:
                    raise ValueError(f"Bad authorized range {sheet}!{area}") from exc
            size = max(ws.max_row, dst.max_row) * max(ws.max_column, dst.max_column)
            if size > max_cells:
                raise ValueError(f"{sheet}: {size} cells exceeds scan cap {max_cells}; NOT VERIFIED")
            # Added columns shift existing fields; comparing coordinates would give false
            # positives. Require a separate scoped evaluator for such structural changes.
            if additions:
                warnings.append(f"{sheet}: new header authorized; cell/format comparisons need separate insertion-aware QA")
                continue
            for row_cells in ws.iter_rows():
                for src in row_cells:
                    dst_cell = dst[src.coordinate]
                    checked += 1
                    if src.value != dst_cell.value and not _allowed_cell(src.row, src.column, ranges):
                        errors.append(f"Unauthorized cell change: {sheet}!{src.coordinate}")
                    if _style(src) != _style(dst_cell) and not _allowed_cell(src.row, src.column, contract.get("authorized_style_ranges", {}).get(sheet, [])):
                        errors.append(f"Unapproved formatting change: {sheet}!{src.coordinate}")
                    if len(errors) >= 40:
                        break
                if len(errors) >= 40:
                    break
            # Prevent unapproved content beyond original range (including detached notes).
            for row_cells in dst.iter_rows():
                for cell in row_cells:
                    if cell.row <= ws.max_row and cell.column <= ws.max_column:
                        continue
                    if cell.value is not None and not _allowed_cell(cell.row, cell.column, ranges):
                        errors.append(f"Extra populated cell: {sheet}!{cell.coordinate}")
                        if len(errors) >= 40:
                            break
                if len(errors) >= 40:
                    break
            for header, permitted in status_rules.get(sheet, {}).items():
                hits = [col for col, name in new if name == header]
                if len(hits) != 1:
                    errors.append(f"Status field missing/ambiguous: {sheet}.{header}")
                    continue
                allowed = {_normalize(x) for x in permitted}
                for idx in range(row + 1, dst.max_row + 1):
                    cell = dst.cell(idx, hits[0])
                    if cell.data_type == "f":
                        warnings.append(f"Formula status not recalculated by Python: {sheet}!{cell.coordinate}")
                        continue
                    if _normalize(cell.value) and _normalize(cell.value) not in allowed:
                        errors.append(f"Unexpected status {sheet}!{cell.coordinate}: {cell.value!r}")
                        if len(errors) >= 40:
                            break
        return {
            "pass": not errors,
            "checked_cells": checked,
            "errors": errors[:40],
            "warnings": sorted(set(warnings)),
            "verified": ["source_sheet_inventory", "header_names_order", "value_scope",
                         "existing_cell_styles", "literal_closed_status_values"],
            "not_verified": ["semantic_field_meaning", "Excel_native_F3_interactivity",
                             "calculated_formula_results", "unauthorized_user_permission_claims"],
        }
    finally:
        before.close()
        after.close()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", required=True, type=Path)
    p.add_argument("--max-cells", type=int, default=400_000)
    p.add_argument("--pretty", action="store_true")
    a = p.parse_args()
    try:
        contract = json.loads(a.contract.read_text(encoding="utf-8"))
        result = evaluate(contract, max_cells=a.max_cells)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"pass": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2 if a.pretty else None))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
