# Source-First Workbook Schema: Minimum Authorized Change

## 0. The central rule

**When a user supplies an existing workbook, its actual sheets, headers, column order, field meanings, status vocabulary, filters, pivot structures and presentation are the deliverable's starting contract.** Do not create a new schema because it is easier to program, more detailed, visually clearer, or a familiar example appears in this skill.

**A request to classify, reconcile, review, group, aggregate, fix, automate or update an existing sheet is NOT authorization to add, rename, split, reorder, repurpose, populate from scratch or delete user-facing columns/sheets.**

- If the original has `CLASSIFICADO` with `SIM/NÃO`, do **not** append `CONCILIA` just to record the same or a different assessment, and do **not** replace the meaning of `CLASSIFICADO` with reconciliation results without establishing that they are the **same business decision**.
- `QTD` and `EMBARQUE` may be useful for internal grouping, but do **not** automatically become extra worksheet columns.
- Similarly do not add `STATUS`, `VALIDAÇÃO`, `OBSERVAÇÕES`, `CHAVE`, `CRITÉRIO`, `TOLERÂNCIA`, `AUXILIAR`, `REVISAR`, formula-explanation columns, or an extra `Resumo`/QA tab because it seems professionally useful.
- **Visual preservation and status vocabulary are insufficient if the delivered worksheet schema changed without authorization.** All three must hold: *schema, semantics, appearance*.

This guide intentionally corrects earlier examples that treated `CONCILIA` as original even though the user's supplied source had `CLASSIFICADO`. Names in examples are illustrative, NEVER evidence that a field actually exists in an uploaded workbook.

## 1. Discover the real workbook before designing a solution

For each in-scope sheet, inspect and record in a small *internal* contract:

- sheet names/order, visible/hidden state; actual header row(s), exact header spelling/accents, coordinates/order, duplicates, merged header cells;
- real column purposes: identifiers, values, derived/formula fields, status meanings and existing `SIM/NÃO` usage;
- existing Excel Tables, PivotTables, named ranges, formulas, data validation, filters and refresh relationships;
- expected input vs output sheets, original row count, range, source totals and styling baseline;
- requested change and its exact destination in the existing workbook (sheet/range/field), or whether the output is truly a *new* artifact.

**Do not derive schema from a screenshot, a similar report, a skill example, prior generated output or the assistant's own previous decisions when an original workbook is available.** Confirm against the actual original file; if only a screenshot exists, state what cannot be verified.

User statements such as "we use 5 cents as tolerance" provide a business **calculation rule**, not a new `Tolerância` column. A phrase like "classify shipments" provides the **task**, not a new `EMBARQUE` field.

## 2. The schema-change authorization ladder

Before every workbook-structure modification classify it:

**A. Existing-field update** — allowed when semantically correct and within the task: calculate or write to an existing field intended for that business result; preserve others.

**B. Internal intermediate** — allowed without appearing in delivery: compute `EMBARQUE_NORMALIZADO`, `QTD_POR_GRUPO`, `SALDO`, `KEY`, `MATCH`, diagnostic flags, etc. using dataframes, in-memory dictionaries, temp files or external QA artifacts, then deliver only the authorized result. Do not silently attach these to final worksheets.

**C. Necessary native Excel support** — if a specifically requested **real** PivotTable/query/control genuinely needs source/helper structures, prefer existing fields/objects or a temporary/isolated data source. Add a support sheet/field to the delivered file only if the native feature **cannot** be provided otherwise and the user has authorized the required structural change; keep changes minimal and explain material differences. A native feature's implementation convenience is not permission for visible new columns.

**D. User-authorized structural change** — allowed when explicitly requested, e.g. "acrescente uma coluna EMBARQUE ao lado da A", "crie uma nova aba para resultados", "faça um relatório novo com essas colunas". Preserve everything outside scope; use exactly requested headers, placement and meanings.

**E. Ambiguous/missing output slot** — if the existing `CLASSIFICADO` field does not represent the requested reconciliation verdict, do not hijack it or invent `CONCILIA`. Compute internally, retain source unchanged, and return the available result separately if compatible with the user's goal; identify the missing presentation authorization briefly rather than presenting a materially altered file as the original. Ask a targeted question only if the output genuinely cannot be represented correctly otherwise.

**Key distinction:** Preserve an existing column name *and* its business meaning. Do not merely change `CONCILIA` back to `CLASSIFICADO` while silently rewriting a classification flag with a different concept.

## 3. Definition of done = minimal, explained structural diff

For edits to an existing source workbook, preserve unless expressly in scope:

- original sheets and order; all preexisting headers, exact names, duplicates, positions and header rows;
- original visible data columns, table ranges, Excel-native objects, filters, formulas, links, row order and classification conventions;
- original number formats, fills, widths, conditional-formatting, tab styles and print behavior;
- business meaning of each status and metric.

**Required structural diff test:**
1. Snapshot actual original (not the prior AI-produced workbook).
2. Snapshot final.
3. Check for new/removed/renamed/moved headers, new/removed/reordered sheets, changed statuses/formulas and structural objects, beyond user-approved changes.
4. For each difference, attach internal reason: *requested*, *strictly necessary and authorized*, or *unexpected defect*. **Any unexplained user-facing column/sheet is a blocker**, even when counts and formulas are correct.
5. Correct unexpected changes and rerun **targeted** result and structure checks. Avoid unnecessarily running full suites.
6. Preserve original unchanged and do not call the deliverable final if it drifts.

The same idea applies to CSV/Google Sheets, not only Excel. If original rows may grow or filtering/grouping is required, use authorized native structures without silently restructuring a protected output.

## 4. Examples: what should have happened

**Original**: `CLASSIFICADO` exists, with `SIM/NÃO`; no `CONCILIA`, `QTD` or `EMBARQUE` columns. Agent must identify the intended workflow from source and user request.

**Wrong**: creates `CONCILIA` for a new outcome, `QTD` for aggregation, `EMBARQUE` for a parsed key; then claims the source layout was preserved.

**Correct (when the task is classification and CLASSIFICADO already holds that same result):** compute grouping and counts privately, then update **only authorized cells in `CLASSIFICADO`**, preserving the existing header, rows, style, native objects and status values.

**Correct (when CLASSIFICADO has a different meaning):** retain `CLASSIFICADO` intact. Compute requested reconciliation separately and use only a user-authorized output location or separate result; do **not** silently overwrite the original field or insert `CONCILIA`.

**Correct for explicitly requested new columns:** add only the specifically requested fields with the specified placement/meaning, preserving all others.

## 5. Minimal QA tools

Use `scripts/check_workbook_schema.py` with explicit sheet/header selectors to surface added/renamed/moved column names and unexpected sheets. It is a structural **signal**, not a proof of correct business meaning, pivot functionality or visually exact rendering.

Also use, when relevant:
- `scripts/workbook_diff.py` for formulas, contents and formatting drift;
- `scripts/check_status_values.py --column CLASSIFICADO` (or the **actual source** column, never an invented default) for allowed status values; semantic status correctness still needs business checks;
- `scripts/inspect_native_excel.py` for preliminary native-object presence.

**Do not expose QA details as extra worksheets or status labels** unless the real audience needs them. Keep lightweight evidence outside the finished workbook.

## 6. Pre-send question

> "Did I change the original workbook only where the user asked? Are every added header, tab, status and visible control genuinely required and authorized? Am I preserving not just the names, but the meanings?"

If no, this is **not final**. Fix it first. No amount of Excel refresh testing, formatting polish, confidence language, or number of workers compensates for structural changes the user did not request.
