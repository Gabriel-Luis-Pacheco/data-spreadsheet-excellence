from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable


def run_json(script: str, *args: str) -> tuple[subprocess.CompletedProcess[str], dict]:
    proc = subprocess.run(
        [PY, str(ROOT / "scripts" / script), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode not in {0, 2}:
        raise AssertionError(f"{script} failed: {proc.stderr}\n{proc.stdout}")
    return proc, json.loads(proc.stdout)


class UtilityTests(unittest.TestCase):
    def test_profile_preserves_leading_zero_identifier(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "sample.csv"
            path.write_text("id,amount\n00123,10\n00456,20\n", encoding="utf-8")
            proc, payload = run_json("profile_tabular.py", str(path))
            self.assertEqual(proc.returncode, 0)
            self.assertEqual(payload["read_mode"], "preserve-text-where-practical")
            id_profile = next(x for x in payload["column_profiles"] if x["name"] == "id")
            top_values = {x["value"] for x in id_profile.get("top_values", [])}
            self.assertIn("00123", top_values)
            self.assertIn("00456", top_values)\n            note_profile = next(x for x in payload["column_profiles"] if x["name"] == "note")\n            self.assertEqual(note_profile["formula_like_text_count"], 1)

    def test_inspect_workbook_reports_formula_and_hidden_sheet(self) -> None:
        from openpyxl import Workbook

        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "book.xlsx"
            wb = Workbook()
            ws = wb.active
            ws.title = "Data"
            ws["A1"] = 1
            ws["A2"] = 2
            ws["A3"] = "=SUM(A1:A2)"
            hidden = wb.create_sheet("Hidden")
            hidden.sheet_state = "hidden"
            wb.save(path)

            proc, payload = run_json("inspect_workbook.py", str(path))
            self.assertEqual(proc.returncode, 0)
            self.assertEqual(payload["sheet_count"], 2)
            data = next(x for x in payload["sheets"] if x["title"] == "Data")
            hidden_info = next(x for x in payload["sheets"] if x["title"] == "Hidden")
            self.assertEqual(data["formula_cells"], 1)
            self.assertEqual(hidden_info["state"], "hidden")\n            self.assertEqual(data["comment_cells"], 1)\n            self.assertEqual(data["hyperlinks"], 1)\n            self.assertIn("hidden_or_very_hidden_sheets_present", payload["risk_hints"])\n            self.assertIn("cell_comments_present", payload["risk_hints"])

    def test_workbook_diff_detects_formula_change(self) -> None:
        from openpyxl import Workbook, load_workbook

        with tempfile.TemporaryDirectory() as td:
            before = Path(td) / "before.xlsx"
            after = Path(td) / "after.xlsx"

            wb = Workbook()
            ws = wb.active
            ws.title = "Data"
            ws["A1"] = 1
            ws["A2"] = 2
            ws["A3"] = "=SUM(A1:A2)"
            wb.save(before)

            wb2 = load_workbook(before)
            wb2["Data"]["A3"] = "=AVERAGE(A1:A2)"
            wb2.save(after)

            proc, payload = run_json("workbook_diff.py", str(before), str(after))
            self.assertEqual(proc.returncode, 0)
            self.assertIn("formula_structure_changed", payload["risk_flags"])
            self.assertGreater(payload["change_count"], 0)

            proc2, _ = run_json("workbook_diff.py", str(before), str(after), "--fail-on-risk")
            self.assertEqual(proc2.returncode, 2)

    def test_repository_validators_pass(self) -> None:
        for script, extra in [
            ("validate_skill.py", []),
            ("context_budget.py", ["--check"]),
        ]:
            proc = subprocess.run(
                [PY, str(ROOT / "scripts" / script), *extra],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, msg=proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
