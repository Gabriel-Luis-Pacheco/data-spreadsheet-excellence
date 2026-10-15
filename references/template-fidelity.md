# Template Fidelity and No-Unsolicited-Design Contract

## Principle: the template is the design specification

If the user supplies an original workbook, reference screenshot, report, corporate template, or established working layout, **preserve it as the primary design specification**. A request to populate, reconcile, audit, fix, automate, add calculations, or create native Excel functionality is **NOT** a request to restyle.

Correctness and native Excel behavior can be improved without inventing a new look. "Professional", "human-made", "clear", "high-quality" and "anti-AI-slop" do **not** authorize cosmetic changes. No visual change needs to happen merely because the agent knows a popular design convention.

### Default for an existing workbook: visual minimal diff

- Preserve existing fills, font colors/types/sizes, number formats, borders, banding, row heights, column widths, alignment, merged ranges, themes, conditional-formatting rules, tab colors, sheet names, chart styles, existing table styles, filters, freeze panes, printing, and presentation order unless a requested functional change necessitates a bounded adjustment.
- Keep original header colors (for example, existing light-blue headers); do not replace or supplement the palette just to look "consistent" with an AI-generated theme.
- Never color `SIM` cells green or `NÃO` cells red merely because their meaning *could* be semantically colored. Native text/status is often enough. If the original used no highlights, keep no highlights.
- Do not add green background, colored type, bold statuses, data bars, icons, traffic lights, conditional formatting, borders, alternating-row fills, callouts, legends, cards or dashboards absent from the supplied model. Do not assume the absence of color is a design deficiency.
- **Do not add new columns/rows** unless specifically authorized; if an authorized new column is required, inherit the nearest relevant style without inventing a new color scheme.
- Preserve original recipient-facing layout and avoid unsolicited parameter/criterion notes elsewhere (see `references/human-deliverables.md`).
- A native Excel Table or PivotTable may introduce application-defined presentation. Use the least disruptive compatible style and keep the workbook's existing visual conventions; preserve real native interactivity. If an unavoidable visible change is material, explain it in a short handoff (not as an execution report inside the sheet).

### Evidence hierarchy

1. Explicit user request **for this task** (including explicit restyling).
2. Original workbook and relevant sheets: exact style/structure and functioning objects.
3. Provided screenshot/sample: visible styling and layout clues only; do not infer invisible behavior.
4. Established company conventions and previous user examples when demonstrably applicable.
5. Conservative, unobtrusive defaults **only when creating from scratch or where references are silent**.

A generic aesthetic preference must not override an actual supplied template. When samples conflict, preserve the specific task's source workbook first unless the user has made a clear change request.

### Exceptions: change is justified only when

- Explicitly requested (e.g., "highlight all mismatches in red", "redesign this dashboard");
- Required for correct usability of a requested native Excel feature, with minimal visual intrusion;
- Needed for accessibility, safety, mandatory reporting, or to avoid materially misleading presentation; use the smallest effective change and record why;
- An existing visual element is genuinely broken or unreadable and correcting it is necessary to fulfill the task, rather than subjective embellishment.

If a difference affects a decision, preserve the underlying numeric/status evidence whether or not color is added. Do not falsely imply that colored status is a required validation method.

### Example: reconciliation from existing user worksheet

The **original** workbook has `CLASSIFICADO` (`SIM/NÃO`), but lacks `CONCILIA`, `QTD` and `EMBARQUE`. The task asks for reconciliation/classification using a tolerance of `0,05`. Its header styling must also remain unchanged.

**Correct result:** identify the existing meaning of `CLASSIFICADO`; apply the tolerance to internal calculations and update only an existing semantically appropriate authorized result field. Do not manufacture helper columns or additional statuses. Retain original styles, filters, row count and first-screen appearance.

**Wrong result:** append `CONCILIA`, `QTD` and `EMBARQUE` for convenience; replace the meaning of `CLASSIFICADO` without checking; add green/red status fills, a `Tolerância: 0,05` box, a `Critério` label or an unsolicited `QA` sheet.

If the user **explicitly** asks for colored exception highlighting, then the new coloring is in scope. An internal QA check is not the same as authorization to redesign.

### Final visual-diff QA — small, targeted, decisive

1. Compare original and output **for the relevant existing sheets/ranges**, including fills, fonts, borders, alignments, number formats, CF rule definitions, widths, heights and sheet/tab settings.
2. Categorize differences: requested/necessary vs unexpected. Do not accept an unexplained style change because it seems attractive.
3. Remove unexpected color/format additions and rerun a **focused** validation of affected formulas, values, native features and layout.
4. If there is no original workbook file, compare available screenshots visually while making no claim of exact unseen style/CF/objects.
5. Stop after the requested changes and appropriate checks pass; do not run endless visual redesign cycles.

Use existing `scripts/workbook_diff.py` as a first-pass workbook check, not as full pixel or native-feature proof. If additional style comparison is available, review it for unexpected changes; no need to run the full suite for every minor workbook modification.

## Important distinction

**With original template:** preservation is the default; the burden of proof is on each change.

**Creating a new template from scratch:** design choices are needed; use accessible, restrained, purposeful styling suited to the reader.

**Explicit redesign request:** redesign is in scope; preserve correctness, requested native behavior, and content while considering the user's stated style constraints.
