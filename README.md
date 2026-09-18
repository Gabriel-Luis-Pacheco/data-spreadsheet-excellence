# Data & Spreadsheet Excellence

A portable Agent Skill for professional work with **data analysis, Python, Excel, spreadsheets, reconciliation, automation, review, visualization, analytical writing, and efficient AI execution**.

> A successful analytical task is not merely code that runs or a workbook that opens. The result should be correct, decision-useful, auditable, reproducible, efficient, understandable, and visually intentional — without wasting context, tool calls, or output tokens.

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
- concise analytical writing without generic AI slop;
- prompt/context engineering;
- token, latency and tool-call economy;
- adaptive agent execution (LEAN / BALANCED / DEEP);
- AI coding discipline and minimal-diff workflows.

## Efficiency harness

The skill now includes an explicit execution harness.

It does **not** mean “always use fewer tokens.” It means:

- load only context that can change the next decision;
- keep reusable instructions stable;
- use progressive disclosure;
- avoid rereading unchanged content;
- prefer deterministic scripts for deterministic work;
- use the smallest relevant toolset;
- keep outputs proportional to the consumer;
- escalate reasoning/verification only when risk or ambiguity warrants it;
- never trade away material correctness, safety, or validation merely to save tokens.

Portable defaults live in:

`harness/harness.yaml`

Detailed guidance:

- `references/agent-harness.md`
- `references/prompt-context-engineering.md`
- `references/token-economy.md`
- `references/coding-practices.md`

## Architecture

The skill uses progressive disclosure:

```text
SKILL.md
AGENTS.md
agents/openai.yaml
harness/
  harness.yaml
  README.md
references/
  agent-harness.md
  prompt-context-engineering.md
  token-economy.md
  coding-practices.md
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
  context_budget.py
  inspect_workbook.py
  profile_tabular.py
assets/
  task-prompt-template.md
  delivery-summary-template.md
  reconciliation-summary-template.md
  review-report-template.md
.github/
  copilot-instructions.md
  instructions/python.instructions.md
  workflows/validate.yml
EVALS.md
```

The main `SKILL.md` stays compact. Detailed references are loaded only when the task needs them.

## Adaptive modes

### LEAN
For clear, reversible, low-risk work.

- little or no formal planning;
- 0–1 reference initially;
- one focused verification;
- concise response.

### BALANCED
Default for normal analysis and automation.

- brief plan/state;
- 1–3 references initially;
- targeted + relevant end-to-end checks;
- compact handoff.

### DEEP
For high-risk, ambiguous, F3 Excel, complex debugging/refactoring, conflicting evidence, or failed validation.

- explicit completion criteria;
- stronger evidence and independent verification;
- additional context only when it resolves a material uncertainty.

The skill escalates rather than starting deep by default.

## Install in Codex

Use Codex's built-in `$skill-installer` and provide:

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

## Efficient task prompt

For larger tasks, this is usually enough:

```text
Goal:
Context:
Constraints:
Output:
Done when:
```

See `assets/task-prompt-template.md`.

Do not turn every request into a giant prompt. Specificity matters more than length.

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
- Useful context beats maximum context.
- Minimal relevant tools beat maximum tool access.
- High-risk work gets stronger assurance.
- Low-risk work should not become process theater.

## Utilities

Validate the skill:

```bash
python scripts/validate_skill.py
```

Inspect instruction/context growth:

```bash
python scripts/context_budget.py --check
```

The token figure reported by that script is intentionally a **rough proxy**, not a billing/tokenizer truth.

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

`EVALS.md` covers spreadsheet/data quality and also the efficiency harness: selective context loading, tool economy, minimal diffs, adaptive depth, compaction/state handling, and prompt quality.

## Research basis

The guidance is periodically refreshed against current primary documentation, including:

- OpenAI Codex/Agent Skills, prompt engineering, prompt caching, compaction, cost/latency and skill-evaluation guidance;
- GitHub Copilot context/custom-instruction efficiency guidance;
- Anthropic prompt/long-context guidance;
- Google Gemini prompt/long-context/caching guidance;
- ICAEW spreadsheet practice;
- the AQuA Book and reproducible analytical pipeline guidance;
- pandas/Polars/openpyxl/XlsxWriter/Microsoft/Google documentation;
- accessibility and data-visualization guidance.

See `references/source-notes.md`.

## Version

**v6.0.0 — Efficiency Harness**

MIT licensed.
