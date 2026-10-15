"""Targeted structural-inventory tests; not Excel F3 behavior tests."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import inspect_native_excel as scanner  # noqa: E402

REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def relationships(*items):
    parts = "".join(
        f'<Relationship Id="r{i}" Type="http://schemas.openxmlformats.org/'
        f'officeDocument/2006/relationships/{kind}" Target="{target}"/>'
        for i, (kind, target) in enumerate(items, 1)
    )
    return f'<Relationships xmlns="{REL_NS}">{parts}</Relationships>'


class NativeExcelInventoryTests(unittest.TestCase):
    def test_styled_summary_cannot_masquerade_as_pivot(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "summary.xlsx"
            with ZipFile(path, "w") as archive:
                archive.writestr("xl/worksheets/sheet1.xml", "<worksheet/>")
            result = scanner.inspect(path)
            self.assertEqual(result["objects"]["verified_pivot_structure_count"], 0)

    def test_pivot_needs_sheet_link_and_cache_link(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "linked.xlsx"
            with ZipFile(path, "w") as archive:
                archive.writestr(
                    "xl/worksheets/_rels/sheet1.xml.rels",
                    relationships(("pivotTable", "../pivotTables/pivotTable1.xml")),
                )
                archive.writestr("xl/pivotTables/pivotTable1.xml", "<pivotTableDefinition/>")
                archive.writestr(
                    "xl/pivotTables/_rels/pivotTable1.xml.rels",
                    relationships(("pivotCacheDefinition", "../pivotCache/pivotCacheDefinition1.xml")),
                )
                archive.writestr("xl/pivotCache/pivotCacheDefinition1.xml", "<pivotCacheDefinition/>")
                archive.writestr("xl/tables/table1.xml", "<table/>")
                archive.writestr(
                    "xl/worksheets/_rels/sheet2.xml.rels",
                    relationships(("table", "../tables/table1.xml")),
                )
            result = scanner.inspect(path)
            self.assertEqual(result["objects"]["verified_pivot_structure_count"], 1)
            self.assertEqual(result["objects"]["linked_excel_table_count"], 1)

    def test_unlinked_parts_do_not_count_as_verified_pivot(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "unlinked.xlsx"
            with ZipFile(path, "w") as archive:
                archive.writestr("xl/pivotTables/pivotTable1.xml", "<pivotTableDefinition/>")
                archive.writestr("xl/pivotCache/pivotCacheDefinition1.xml", "<pivotCacheDefinition/>")
            result = scanner.inspect(path)
            self.assertEqual(result["objects"]["pivot_table_parts"], 1)
            self.assertEqual(result["objects"]["verified_pivot_structure_count"], 0)


if __name__ == "__main__":
    unittest.main()
