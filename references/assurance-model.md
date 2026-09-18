# Assurance Model — Separate Work Depth from Evidence Strength

Execution complexity and assurance are different dimensions. Do not couple them.

A task may be simple to execute but require strong evidence (for example, changing one formula in a financial model). Another task may be technically complex but low consequence (for example, exploratory visualization).

## 1. Execution mode

Execution mode controls how much context, planning, tooling, and exploration the agent uses.

- **LEAN** — narrow, clear, reversible.
- **BALANCED** — ordinary multi-step analytical work.
- **DEEP** — ambiguous, technically complex, conflicting, or repeatedly failing work.

## 2. Assurance tier

Assurance controls how strong the validation and evidence must be.

### A0 — exploratory

Use for disposable exploration where errors have limited consequence.

Typical evidence:
- basic sanity check;
- no claim of production readiness.

### A1 — standard

Use for normal internal analysis and routine automation.

Typical evidence:
- schema/key checks;
- control totals where applicable;
- targeted tests;
- output opens/looks correct.

### A2 — material

Use when the result informs meaningful operational, financial, client, or management decisions.

Typical evidence:
- independent or alternate checks;
- explicit exceptions;
- preservation evidence;
- traceable metric definitions;
- focused review of material outputs;
- stronger visual/workbook QA.

### A3 — critical

Use for regulatory, materially consequential official/external publication, high-value financial, irreversible, safety-sensitive, or otherwise critical work.

Typical evidence:
- independent validation path or reviewer where feasible;
- source/provenance manifest;
- change control;
- documented assumptions and limitations;
- explicit sign-off/approval gates for consequential actions;
- target-application verification for F3 workbook behavior;
- reproducibility package.

## 3. Examples

| Task | Execution | Assurance |
| --- | --- | --- |
| Add total column to a 40-row scratch CSV | LEAN | A0/A1 |
| Build monthly sales workbook | BALANCED | A1 |
| Reconcile supplier balances for close | BALANCED | A2 |
| Change one formula in a regulated XLSM | LEAN/BALANCED | A3 |
| Explore 100M rows for hypotheses | DEEP | A0/A1 |
| Publish official KPI report | BALANCED | A3 |

The table is illustrative, not a fixed rule.

## 4. Escalation

Escalate **execution** when:
- requirements are unclear or contradictory;
- technical blast radius is large;
- repeated tests fail;
- multiple systems interact;
- evidence sources conflict;
- the solution requires architecture/research.

Escalate **assurance** when:
- the cost of a wrong result rises;
- the output leaves the team/company **and** an error would be materially consequential;
- money, compliance, reputation, or irreversible action is involved;
- the user explicitly requests audit-grade/review-grade work;
- input provenance or calculation behavior is uncertain.

A failed validation can escalate either or both dimensions.

## 5. Evidence budget

Before validation, identify the plausible failure modes that could materially change the answer.

Spend assurance effort on those failure modes first.

Examples:
- wrong denominator → independently recompute denominator;
- many-to-many merge → cardinality + pre/post control totals;
- stale formula cache → recalc in target engine;
- workbook preservation risk → before/after structural diff + application test;
- dashboard misleading scale → visual review of axis/baseline;
- fuzzy false matches → sample near threshold + high-value matches.

Do not replace high-value checks with many low-value checks.

## 6. Completion language by assurance

A0:
“Exploratory result; basic sanity checks passed.”

A1:
“Validated row counts/keys/totals and reopened the output.”

A2:
“Primary checks plus independent reconciliation/sampling passed; material exceptions are listed.”

A3:
“Critical controls, independent validation, provenance, and required application/reviewer checks passed; remaining limitations are explicitly documented.”

Never use stronger completion language than the evidence supports.
