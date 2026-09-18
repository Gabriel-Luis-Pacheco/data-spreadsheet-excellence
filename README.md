# Data & Spreadsheet Excellence

A portable Agent Skill for professional work with **data analysis, Python, Excel, spreadsheets, reconciliation, automation, review, visualization, and analytical writing**.

> A successful analytical task is not merely code that runs or a workbook that opens. The result should be correct, decision-useful, auditable, reproducible, efficient, understandable, and visually intentional.

## What it covers

- data cleaning, profiling, metric contracts, statistics and sense checks;
- pandas, Polars, DuckDB, Parquet/PyArrow;
- Excel/Google Sheets automation;
- openpyxl, XlsxWriter, xlwings/COM, Office Scripts;
- joins, reconciliation, fuzzy/probabilistic matching;
- workbook audit and formula/recalculation QA;
- professional spreadsheet and dashboard design;
- performance, idempotency, logging, security and reproducibility;
- review of another analyst's work;
- concise analytical writing without generic AI slop.

## Architecture

The skill uses progressive disclosure:

```text
SKILL.md
agents/openai.yaml
references/
  quick-reference.md
  tool-selection.md
  data-analysis-quality.md
  reconciliation-matching.md
  spreadsheet-engineering.md
  visual-design-reporting.md
  automation-performance.md
  security-governance.md
  writing-review-handoff.md
  quality-gates.md
  patterns-recipes.md
  source-notes.md
scripts/
  validate_skill.py
  inspect_workbook.py
  profile_tabular.py
assets/
  delivery-summary-template.md
  reconciliation-summary-template.md
  review-report-template.md
EVALS.md
```

The main `SKILL.md` stays compact. Deeper references are loaded only when required.

## Install in Codex

Use Codex's built-in `$skill-installer` and provide this repository:

```text
https://github.com/Gabriel-Luis-Pacheco/data-spreadsheet-excellence
```

Example:

```text
Use $skill-installer to install the skill from:
https://github.com/Gabriel-Luis-Pacheco/data-spreadsheet-excellence
```

Then:

```text
Use $data-spreadsheet-excellence to audit this workbook.
```

## Core philosophy

- Decision before tool.
- Integrity before aesthetics.
- Evidence before confidence.
- Preserve before overwrite.
- Deterministic matching before fuzzy matching.
- Reconciliation requires unmatched evidence, not just net balance.
- Formula written is not formula recalculated.
- A spreadsheet is an information product, not a colorful grid.
- Specific writing beats polished generic prose.
- High-risk work gets stronger assurance.
- Low-risk work should not become process theater.

## Utilities

Validate the skill:

```bash
python scripts/validate_skill.py
```

First-pass workbook inventory:

```bash
python scripts/inspect_workbook.py workbook.xlsx --pretty
```

First-pass data profile:

```bash
python scripts/profile_tabular.py data.csv --pretty
```

The profiler preserves CSV/Excel values as text where practical by default to reduce identifier loss such as `00123 → 123`. Use `--infer-types` only intentionally.

## Evaluation

`EVALS.md` contains scenarios for messy ERP data, XLSM fidelity, reconciliation, analyst review, dashboard design, causal claims, large data, Google Sheets automation, writing quality, and low-risk tasks.

## Research basis

The guidance was refined against current Agent Skills/OpenAI skill-authoring guidance, ICAEW spreadsheet practice, the 2025 AQuA Book, reproducible analytical pipeline guidance, pandas/Polars/openpyxl/XlsxWriter/Microsoft/Google documentation, and accessibility/data-visualization guidance.

See `references/source-notes.md`.

## Version

**v5.0.0**

MIT licensed.
