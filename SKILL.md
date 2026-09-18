---
name: data-spreadsheet-excellence
description: Professional data analysis, spreadsheet automation, reconciliation, audit, review, reporting, visualization, and analytical writing. Use for Excel/planilhas, CSV, Google Sheets, Python/pandas/Polars/DuckDB, openpyxl/XlsxWriter/xlwings, data cleaning, joins/cruzamentos, fuzzy matching/conciliação, dashboards, workbook design, formula QA, large-data pipelines, or reviewing another analyst's work. Produces decision-useful, auditable, visually polished outputs without generic AI slop.
---

# Data & Spreadsheet Excellence

**Goal:** produce analytical work that is correct, decision-useful, auditable, maintainable, efficient, visually intentional, and written like a competent professional.

Do not treat “code ran” or “file opens” as completion.

## 1. Start with the decision

Before touching data, determine:

- who will use the result;
- what decision or action it supports;
- the central question;
- the required artifact(s);
- the source scope and time period;
- the critical metrics and definitions;
- the cost of a wrong answer;
- whether the work is one-off, recurring, collaborative, regulated, or externally published.

If the user has already supplied this context, do not ask again. Infer only low-risk details; surface material assumptions.

## 2. Classify risk and spreadsheet fidelity

Use the lightest process that is safe.

**Risk**
- **Low:** exploratory, reversible, limited consequence.
- **Medium:** operational decisions, recurring workflows, shared workbooks.
- **High:** financial, regulatory, client-facing, executive, irreversible, or materially consequential.

**Workbook fidelity**
- **F0 — Data:** values/schema only.
- **F1 — Structure:** sheets, formulas, tables, names, basic formatting.
- **F2 — Visual:** layout, charts, printing, spacing, visual fidelity.
- **F3 — Excel behavior:** macros, pivots, Power Query, external links, objects, calculation/refresh behavior, application-specific features.

Higher risk/fidelity requires more preservation, independent checks, and evidence.

## 3. Core execution workflow

1. **Inventory** inputs before modification.
2. **Profile** schema, types, nulls, duplicates, keys, dates, ranges, distributions, and control totals.
3. **Define** metric contracts, join cardinality, exclusions, tolerances, and assumptions.
4. **Choose** tools based on data size, fidelity, environment, and delivery requirements.
5. **Preserve** raw inputs and originals unless replacement is explicitly requested.
6. **Transform** with explicit, reproducible rules.
7. **Analyze/reconcile** while retaining unmatched and exception records.
8. **Validate independently** using control totals, invariants, samples, plausibility checks, and alternate calculations where material.
9. **Build** the final artifact around the user's workflow, not around the code.
10. **QA visually** when appearance matters.
11. **Edit the narrative** for specificity, brevity, and evidence.
12. **Deliver evidence**: what changed, what was checked, what failed, and what remains uncertain.

## 4. Tool router

Choose the smallest safe stack. Do not default to one library for every task.

| Need | Good starting point |
| --- | --- |
| General dataframe wrangling | `pandas` |
| Large/parallel/lazy dataframe workloads | `Polars` |
| SQL over CSV/Parquet/dataframes; large joins | `DuckDB` |
| Columnar interchange/storage | Parquet / `PyArrow` |
| Spreadsheet ingestion | `pandas.read_excel()` with an appropriate engine |
| Create polished `.xlsx` from scratch | `XlsxWriter` |
| Edit ordinary existing `.xlsx` | `openpyxl` after preservation-risk inspection |
| Control installed Excel / F3 behavior | `xlwings` or Windows COM |
| Google Sheets | Sheets API with batched operations |
| Microsoft 365 web automation | Office Scripts / Power Automate |
| Exact/fuzzy entity matching | deterministic keys → `RapidFuzz`; probabilistic linkage such as `Splink` when justified |
| Dataframe contracts | `Pandera`, explicit check functions, or domain-specific validation |
| Statistical inference | `SciPy` / `statsmodels` |
| Interactive analytical charts | Plotly/Altair when the delivery format supports interactivity |
| Static analytical charts | Matplotlib or spreadsheet-native charts, depending on delivery |

Read `references/tool-selection.md` when the stack is not obvious.

## 5. Data rules that are almost always worth enforcing

- Treat identifiers as text unless arithmetic is meaningful.
- Preserve source values before normalization.
- Define critical metrics: formula, unit, population, denominator, period, source, null treatment, exclusions.
- Distinguish zero, blank, missing, not applicable, suppressed, and error states.
- Validate locale-sensitive dates, decimal separators, currencies, percentages, and time zones.
- Check duplicate keys before joins.
- Declare join cardinality (`1:1`, `1:m`, `m:1`, `m:m`) before or during merge validation.
- Never silently discard unmatched records.
- Beware that dataframe libraries can have join semantics different from SQL, especially around null keys.
- Record row counts and control totals before and after material transformations.
- Treat missingness and outliers as signals to understand, not automatic cleanup targets.
- Do not infer causality from correlation without a defensible design.
- Separate statistical significance from practical/material significance.
- For time series, state baseline, comparison window, calendar, seasonality, and known structural breaks.
- Sort explicitly when row order matters; do not rely on incidental engine order.

For deeper analysis rules, read `references/data-analysis-quality.md`.

## 6. Reconciliation and entity matching

Use an escalation ladder:

1. exact match on trusted identifiers;
2. exact match on normalized deterministic keys;
3. composite-key matching;
4. blocked fuzzy candidate generation;
5. scored fuzzy matching with review zones;
6. probabilistic linkage when the problem warrants it;
7. manual review for unresolved material cases.

A good reconciliation output includes source counts/totals, matched and unmatched count/value, duplicate or ambiguous keys, match method, score/confidence where applicable, material exceptions, net difference **and** gross unmatched amounts.

Read `references/reconciliation-matching.md`.

## 7. Spreadsheet engineering

Treat a workbook as an information product, not a decorated grid.

- Make purpose and primary output obvious within seconds.
- Separate inputs, calculations, outputs, checks, and raw/staging data when useful.
- Keep assumptions and editable cells discoverable.
- Prefer readable formulas over compressed cleverness.
- Avoid hidden logic unless there is a documented reason.
- Use tables, validation, protection, filters, freeze panes, grouping, and named ranges only when they improve the target workflow.
- Preserve formulas, names, macros, links, queries, objects, formatting, and calculation behavior according to required fidelity.
- Remember: formula written ≠ formula accepted ≠ formula recalculated ≠ cached result current.
- Do not use `openpyxl` as a universal Excel round-trip engine; inspect unsupported-feature risk first.
- For F3 work, validate in the target Excel environment when possible.

Read `references/spreadsheet-engineering.md`.

## 8. Visual design and dashboards

A professional spreadsheet should communicate hierarchy before color.

- Establish one primary focus per view.
- Use restrained, semantic color.
- Reserve strong color for exceptions, action, selection, or the key series.
- Align numbers for comparison; use consistent units and precision.
- Use whitespace and grouping to create structure.
- Prefer tables for exact lookup/comparison; charts for pattern, trend, distribution, or relationship.
- Use declarative titles when evidence supports a clear takeaway.
- Label close to the data when that reduces decoding effort.
- Remove decorative chart junk, not necessary context.
- Use honest scales and show uncertainty where material.
- Design operational workbooks differently from executive dashboards.
- When publishing for broad accessibility, apply accessibility-specific guidance rather than blindly reusing internal-workbook conventions.

Read `references/visual-design-reporting.md`.

## 9. Automation and performance

- Prefer vectorized, set-based, batched operations over row/cell loops.
- Minimize workbook/API round-trips.
- Read only required rows/columns where practical.
- Use Parquet for repeated analytical pipelines when suitable.
- Use lazy/streaming engines when data size warrants them.
- Profile before micro-optimizing.
- Make recurring jobs idempotent where possible.
- Use bounded retries only for transient failures; do not retry deterministic validation errors.
- Log enough to reproduce a run without leaking sensitive data.
- Pin/constrain dependencies for recurring workflows and regression-test important templates.

Read `references/automation-performance.md`.

## 10. Security and governance

Treat spreadsheets and connected data sources as potentially active/untrusted content.

- Preserve originals and use safe output paths.
- Do not expose credentials in code, logs, workbook cells, or committed config.
- Be cautious with macros, external links, Power Query, connectors, embedded objects, and formula/CSV injection.
- `DisplayAlerts=False` is not macro security.
- Use least privilege and trusted connectors.
- Do not send confidential data to external services without authorization.
- For programmatic Excel opening, manage automation security intentionally and restore prior state.
- Record provenance/lineage for high-risk work.

Read `references/security-governance.md`.

## 11. Writing without AI slop

- Lead with the answer/finding when appropriate.
- Use concrete nouns, verbs, numbers, dates, units, and denominators.
- State what changed, where, how much, versus what, and why it matters.
- Separate **fact**, **interpretation**, **hypothesis**, **limitation**, and **recommendation**.
- Remove filler such as “it is important to highlight,” “valuable insights,” “robust solution,” and “in today's dynamic environment.”
- Do not repeat the prompt as an introduction.
- Prefer a short specific paragraph to a long generic one.
- Do not label something “significant,” “anomaly,” “trend,” or “insight” without a criterion.
- If evidence is insufficient, say what is unknown and what would resolve it.

Read `references/writing-review-handoff.md`.

## 12. Five-lens review

Before material delivery, review independently as:

**Analyst:** Does this answer the real question? Are comparisons and conclusions justified?

**Auditor:** Can another person reproduce the result? Are sources, joins, filters, exclusions, assumptions, and control totals traceable?

**Information designer:** Does attention go to the right thing first? Is visual emphasis proportional to importance?

**Editor:** Does every sentence earn its place? Is the language specific, natural, concise, and evidence-based?

**End user:** Can the intended person understand and use the result without contacting the author?

For review of third-party work, classify findings as `BLOCKER`, `MAJOR`, `MINOR`, or `IMPROVEMENT`; every material finding needs evidence, impact, and a resolution criterion.

## 13. Definition of done

Completion evidence should be proportional to risk and may include:

- output exists and reopens successfully;
- expected sheets/tables/files exist;
- row counts, schemas, keys, and control totals reconcile;
- material joins have matched/unmatched evidence;
- formulas were checked at the correct layer;
- current formula results were recalculated in a real engine when required;
- output was visually inspected when presentation matters;
- original/source data remains recoverable;
- exceptions and limitations are disclosed;
- final narrative is specific and free of material ambiguity;
- another person can continue the workflow from delivered artifacts.

Use `references/quality-gates.md` for the full QA rubric.

## 14. Reference map

Load only what is needed:

- `references/quick-reference.md`
- `references/tool-selection.md`
- `references/data-analysis-quality.md`
- `references/reconciliation-matching.md`
- `references/spreadsheet-engineering.md`
- `references/visual-design-reporting.md`
- `references/automation-performance.md`
- `references/security-governance.md`
- `references/writing-review-handoff.md`
- `references/quality-gates.md`
- `references/patterns-recipes.md`
- `references/source-notes.md`

## 15. Boundary behavior

- Low-risk tasks should not become process theater.
- High-risk work should favor explicit evidence and independent checks over speed.
- If the environment cannot validate something, state that limitation instead of implying validation.
- If a workbook contains features the chosen library cannot safely preserve, switch tools or make the limitation explicit before editing.
- If the best final artifact is not a spreadsheet, do not force one.
