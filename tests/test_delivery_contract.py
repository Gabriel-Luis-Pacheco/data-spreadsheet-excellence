"""End-to-end synthetic workbook artifacts: explicit allowed edit vs realistic bad outputs."""
import tempfile
import unittest
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from sys import path as sys_path

sys_path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_delivery import evaluate


class DeliveryContractFixtureTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)
        self.src = self.root / "original.xlsx"
        self.out = self.root / "result.xlsx"
        self.wb = Workbook()
        ws = self.wb.active
        ws.title = "Base"
        ws.append(["ID", "Amount", "CLASSIFICADO"])
        ws.append(["EXP-001", 10.0, "SIM"])
        ws.append(["EXP-002", 11.0, "NÃO"])
        ws["A1"].fill = PatternFill("solid", fgColor="B4C6E7")
        self.wb.save(self.src)

    def tearDown(self):
        self.t.cleanup()

    def contract(self, **opts):
        return dict(mode="EDIT_EXISTING", original=str(self.src), output=str(self.out),
                    header_rows={"Base": 1}, authorized_changed_ranges={"Base":["C2:C3"]},
                    allowed_status_values={"Base":{"CLASSIFICADO":["SIM","NÃO"]}}, **opts)

    def test_approved_existing_field_only(self):
        self.wb.active["C2"] = "NÃO"
        self.wb.save(self.out)
        result = evaluate(self.contract())
        self.assertTrue(result["pass"], result["errors"])

    def test_unrequested_extra_concilia_column_is_blocked(self):
        self.wb.active["D1"] = "CONCILIA"
        self.wb.save(self.out)
        self.assertFalse(evaluate(self.contract())["pass"])

    def test_unrequested_qa_sheet_is_blocked(self):
        self.wb.create_sheet("QA")
        self.wb.save(self.out)
        self.assertFalse(evaluate(self.contract())["pass"])

    def test_unrequested_green_status_fill_is_blocked(self):
        self.wb.active["C2"].fill = PatternFill("solid", fgColor="00FF00")
        self.wb.save(self.out)
        self.assertTrue(any("formatting" in e for e in evaluate(self.contract())["errors"]))

    def test_unrequested_revisar_status_is_blocked(self):
        self.wb.active["C2"] = "REVISAR"
        self.wb.save(self.out)
        self.assertFalse(evaluate(self.contract())["pass"])

    def test_unrequested_tolerance_sidebar_is_blocked(self):
        self.wb.active["F1"] = "Tolerância"
        self.wb.active["G1"] = .05
        self.wb.save(self.out)
        self.assertFalse(evaluate(self.contract())["pass"])

    def test_same_name_wrong_business_meaning_cannot_be_auto_verified(self):
        self.wb.save(self.out)
        result = evaluate(self.contract())
        self.assertIn("semantic_field_meaning", result["not_verified"])

    def test_missing_input_cannot_claim_pass(self):
        self.wb.save(self.out)
        data = self.contract()
        data["original"] = str(self.root / "missing.xlsx")
        with self.assertRaises(ValueError):
            evaluate(data)

    def test_explicit_added_header_at_fixed_position(self):
        self.wb.active["D1"] = "CONCILIA"
        self.wb.save(self.out)
        data = self.contract(authorized_new_headers={"Base":[{"column":4,"name":"CONCILIA"}]})
        result = evaluate(data)
        self.assertTrue(result["pass"], result["errors"])
        self.assertTrue(result["warnings"])


    def test_authorized_new_column_does_not_bypass_unauthorized_other_cells(self):
        self.wb.active["D1"] = "CONCILIA"
        self.wb.active["B2"] = 99999  # Original protected data tampered with.
        self.wb.save(self.out)
        data = self.contract(authorized_new_headers={"Base":[{"column":4,"name":"CONCILIA"}]})
        result = evaluate(data)
        self.assertFalse(result["pass"])
        self.assertTrue(any("B2" in x for x in result["errors"]))

    def test_wrong_column_position_is_not_authorized(self):
        self.wb.active["D1"] = "CONCILIA"
        self.wb.save(self.out)
        data = self.contract(authorized_new_headers={"Base":[{"column":2,"name":"CONCILIA"}]})
        result = evaluate(data)
        self.assertFalse(result["pass"])

    def test_modified_existing_conditional_format_is_detected(self):
        from openpyxl.formatting.rule import CellIsRule
        self.wb.active.conditional_formatting.add("C2:C3",
            CellIsRule(operator="equal", formula=['"SIM"'], fill=PatternFill("solid",fgColor="00FF00")))
        self.wb.save(self.out)
        self.assertTrue(any("Excel object/layout" in x for x in evaluate(self.contract())["errors"]))

    def test_extra_style_without_value_is_detected(self):
        self.wb.active["F8"].fill = PatternFill("solid", fgColor="00FF00")
        self.wb.save(self.out)
        self.assertTrue(any("formatting" in x for x in evaluate(self.contract())["errors"]))

    def test_explicitly_permitted_inserted_column_with_other_cells_intact(self):
        ws = self.wb.active
        ws.insert_cols(2)
        ws["B1"] = "CONCILIA"
        self.wb.save(self.out)
        contract = self.contract(authorized_new_headers={"Base":[{"column":2,"name":"CONCILIA"}]})
        result = evaluate(contract)
        self.assertTrue(result["pass"], result["errors"])


if __name__ == "__main__":
    unittest.main()
