# Delivery Contract — One Source of Truth for Each Workbook Task

## Priority and task mode

Before editing, identify a single task mode: **EDIT_EXISTING**, **CREATE_NEW**, **DERIVED_REPORT**, or **EXPLICIT_REDESIGN**. An instruction to analyze an existing workbook does not automatically permit editing it. Creating an independent report is different from editing the original.

For EDIT_EXISTING, the **actual original file** defines its worksheets, header names and meanings, status vocabulary, formulas, object behavior, presentation and source values. Derive requested output *inside already appropriate destinations*. User-supplied examples override generic skill examples.

For DERIVED_REPORT, the analyst may design a *separate* artifact that meets the user-requested columns and native behavior, but must leave the original data untouched and not claim the new schema came from the source.

For CREATE_NEW and EXPLICIT_REDESIGN, use sensible editorial/design judgment within task scope. Do not overapply the preservation rules for existing files to a new workbook.

## Five universal invariants

1. **Source truth:** inspect the original; never anchor a diff to the preceding agent-generated version.
2. **Semantic truth:** reuse or modify a field only if its *actual business meaning* matches the requested output. Same values do not imply same meaning.
3. **Minimal authorized change:** every modified cell, added/removed/reordered field, new sheet or visible formatting change has a legitimate user/task rationale; temporary grouping and QA fields belong outside the reader-facing workbook.
4. **Native correctness:** user-requested functional Excel objects are real, not screenshots or imitations, and are tested in the intended application where possible.
5. **Proven outcome:** a finished workbook passes the applicable deterministic checks; material unknowns or non-executed functional tests are disclosed. Never mark a failed/unrun check passed or claim user sign-off.

The skill's earlier specific column/status examples illustrate these invariants but are **not** defaults for another dataset.

## Small internal change contract

For a substantive existing-workbook edit, map:
- original and intended output file paths;
- exact intended task mode and header rows;
- authorized existing-cell ranges (e.g. `Base!D2:D10000`);
- explicitly authorized new fields (name **and exact position**), sheets or style changes, if any;
- permitted values for any closed-domain status fields;
- any known semantic constraints that cannot be mechanically verified;
- high-risk native features that need real Excel inspection.

Do not place this contract as a visible worksheet. Store a compact manifest alongside internal execution evidence, if needed. User's trusted request and actual input determine permissions: **the agent must never grant itself permissions just to make its edited file pass**. A failing verification is a repair signal, not a reason to enlarge the allowlist.

`scripts/verify_delivery.py` provides a read-only deterministic *edit-mode* gate using JSON settings. It checks existing headers and their order, exact positions of approved new fields, cell-change scope, original-cell styles, unexpected sheets, and closed status vocabularies; it cannot infer business semantics, prove PivotTables refresh in Excel or decide whether a permission was genuinely granted by a human. See `assets/delivery-contract.example.json` and `tests/test_delivery_contract.py`.

## Execution that is both fast and safe

Use **one** initial targeted inventory, then focused source investigation, calculate in memory, write a temporary output, run the delivery gate and the minimum independent financial/semantic checks, and atomically hand over a reviewed artifact. Full-workbook diff/QA when assurance or blast radius requires; not ten repetitive tests.

For A2/A3, use a second independent control (row/value bridge, alternative calculation or manual Excel refresh where feasible). Agents can research independent workstreams in parallel but only one owner edits/publishes a given workbook. Fast workers should not invent new final columns or perform unreviewed concurrent writes.

## Hard stop conditions

- Existing workbook was mutated beyond authorized scope.
- A different business meaning was silently assigned to an existing field.
- Required native feature is an imitation.
- Status labels are fabricated or ignored inputs are reclassified as failures without a rule.
- The original is unavailable, while the agent claims to have verified original fidelity.
- A material computation or target Excel interaction is claimed complete without evidence.

Correct these issues or clearly scope down the claim. Do not solve them with extra 'QA', 'Critério', 'Tolerância' or 'Execução' worksheets.
