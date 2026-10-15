#!/usr/bin/env python3
"""Read-only OOXML inventory of native Excel objects.

Detects native object parts/relationships, not actual Excel UI functionality.
Only a compatible Excel application can verify F3 interaction.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile

REL_NS = "{http://schemas.openxmlformats.org/package/2006/relationships}"
LIMIT = 2_000_000  # Relationship XML should be compact.
PATTERNS = {
    "pivot_table_parts": r"xl/pivotTables/pivotTable\d+\.xml",
    "pivot_cache_parts": r"xl/pivotCache/pivotCacheDefinition\d+\.xml",
    "excel_table_parts": r"xl/tables/table\d+\.xml",
    "chart_parts": r"xl/charts/chart\d+\.xml",
    "slicer_parts": r"xl/slicers/slicer\d+\.xml",
    "slicer_cache_parts": r"xl/slicerCaches/slicerCache\d+\.xml",
    "timeline_parts": r"xl/timelines/timeline\d+\.xml",
    "query_table_parts": r"xl/queryTables/queryTable\d+\.xml",
    "external_link_parts": r"xl/externalLinks/externalLink\d+\.xml",
}
REQUIRED = {
    "pivot_table": "verified_pivot_structure_count",
    "excel_table": "linked_excel_table_count",
    "chart": "chart_parts",
    "slicer": "slicer_parts",
    "connection": "connections_part",
}


def _targets(zip_file: ZipFile, rels: str, token: str) -> list[str]:
    """Return targets only when relationship type matches token."""
    info = zip_file.NameToInfo.get(rels)
    if info is None or info.file_size > LIMIT:
        return []
    try:
        root = ElementTree.fromstring(zip_file.read(rels))
    except (ElementTree.ParseError, UnicodeError):
        return []
    return [
        e.attrib.get("Target", "")
        for e in root.findall(f"{REL_NS}Relationship")
        if e.attrib.get("Type", "").rsplit("/", 1)[-1] == token
        and e.attrib.get("TargetMode", "Internal") != "External"
    ]


def _resolve(relfile: str, target: str) -> str:
    """Resolve an internal OOXML relationship target relative to its source."""
    if not target:
        return ""
    if target.startswith("/"):
        return target.lstrip("/")
    base = relfile.split("/_rels/", 1)[0]
    components = list(PurePosixPath(base).parts)
    for part in target.replace("\\", "/").split("/"):
        if part == "..":
            if components:
                components.pop()
        elif part and part != ".":
            components.append(part)
    return "/".join(components)


def inspect(path: Path) -> dict[str, object]:
    with ZipFile(path) as zf:
        names = set(zf.namelist())
        counts = {
            k: sum(bool(re.fullmatch(pattern, name)) for name in names)
            for k, pattern in PATTERNS.items()
        }
        sheet_rels = sorted(
            name
            for name in names
            if re.fullmatch(r"xl/worksheets/_rels/sheet\d+\.xml\.rels", name)
        )
        sheet_pivots = set()
        sheet_tables = set()
        for rel in sheet_rels:
            sheet_pivots.update(_resolve(rel, target) for target in _targets(zf, rel, "pivotTable"))
            sheet_tables.update(_resolve(rel, target) for target in _targets(zf, rel, "table"))
        linked_pivots = {
            name for name in sheet_pivots
            if name in names and re.fullmatch(PATTERNS["pivot_table_parts"], name)
        }
        linked_tables = {
            name for name in sheet_tables
            if name in names and re.fullmatch(PATTERNS["excel_table_parts"], name)
        }
        verified_pivot_count = 0
        for pivot in linked_pivots:
            parent, filename = pivot.rsplit("/", 1)
            relfile = parent + "/_rels/" + filename + ".rels"
            caches = [_resolve(relfile, target)
                      for target in _targets(zf, relfile, "pivotCacheDefinition")]
            if any(
                target in names and re.fullmatch(PATTERNS["pivot_cache_parts"], target)
                for target in caches
            ):
                verified_pivot_count += 1
        counts["linked_excel_table_count"] = len(linked_tables)
        counts["verified_pivot_structure_count"] = verified_pivot_count
        counts["connections_part"] = int("xl/connections.xml" in names)
        counts["vba_project_part"] = int("xl/vbaProject.bin" in names)
        return {
            "file": path.name,
            "objects": counts,
            "warning": (
                "Package-level presence only; cannot certify Excel UI, refresh, "
                "formula evaluation, source validity or complete F3 fidelity."
            ),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument(
        "--require", action="append", choices=sorted(REQUIRED), default=[],
        help="Fail if OOXML evidence of the native object is absent (repeatable).",
    )
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    try:
        data = inspect(args.file)
    except (FileNotFoundError, PermissionError, BadZipFile, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    missing = [name for name in args.require if not data["objects"][REQUIRED[name]]]
    data["missing_required_objects"] = missing
    print(json.dumps(data, indent=2 if args.pretty else None, ensure_ascii=False))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
