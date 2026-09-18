# Quality Gates

Use only the gates relevant to the task. High-risk work should pass more gates with stronger evidence.

## Gate A — Purpose
- [ ] user/decision identified
- [ ] central question stated
- [ ] artifact format appropriate
- [ ] period/scope clear
- [ ] critical metrics defined
- [ ] assumptions recorded

## Gate B — Input integrity
- [ ] source inventory complete
- [ ] row counts captured
- [ ] schema/types checked
- [ ] date range checked
- [ ] key nulls/duplicates checked
- [ ] control totals captured
- [ ] raw source preserved

## Gate C — Transformations
- [ ] normalization rules explicit
- [ ] no silent coercions
- [ ] exclusions logged
- [ ] row-count changes explained
- [ ] business rules separated from presentation logic
- [ ] deterministic/reproducible where practical

## Gate D — Joins/reconciliation
- [ ] expected cardinality stated
- [ ] duplicate keys checked
- [ ] null-key behavior handled
- [ ] matched/left-only/right-only reported
- [ ] total values compared before/after
- [ ] many-to-many expansion investigated
- [ ] fuzzy/probabilistic matches retain method/confidence
- [ ] material exceptions reviewed

## Gate E — Analysis
- [ ] denominator/population correct
- [ ] baseline correct
- [ ] partial-period/seasonality considered
- [ ] missing data handled deliberately
- [ ] outliers understood
- [ ] effect size/materiality considered
- [ ] uncertainty stated
- [ ] causal language appropriate
- [ ] sensitivity checked for fragile conclusions

## Gate F — Workbook F1
- [ ] expected sheets exist
- [ ] formulas/tables/names preserved as required
- [ ] number formats correct
- [ ] input/output/check areas clear
- [ ] external links/macros/queries inventoried
- [ ] original preserved

## Gate G — Workbook F2
- [ ] opened/rendered for visual QA
- [ ] widths/heights/wrap checked
- [ ] chart axes/labels/titles checked
- [ ] visual hierarchy clear
- [ ] print/PDF checked if relevant
- [ ] accessibility considerations applied for target audience

## Gate H — Workbook F3
- [ ] opened in target Excel environment where possible
- [ ] macro/security behavior understood
- [ ] formulas recalculated if required
- [ ] refresh completed and verified if required
- [ ] pivots/connections/objects behave as expected
- [ ] application state restored after automation

## Gate I — Automation
- [ ] idempotency considered
- [ ] bounded retries
- [ ] logs useful but not sensitive
- [ ] config validated
- [ ] dependencies constrained
- [ ] representative tests
- [ ] failure path leaves recoverable state
- [ ] output publication status confirmed

## Gate J — Visual/reporting
- [ ] primary message obvious
- [ ] units/period/source visible
- [ ] chart type suits question
- [ ] strong color is meaningful
- [ ] no false precision
- [ ] no misleading scale
- [ ] table sort/order intentional
- [ ] exceptions are easy to find

## Gate K — Writing
- [ ] answer first where appropriate
- [ ] claims tied to evidence
- [ ] fact vs interpretation separated
- [ ] generic filler removed
- [ ] terminology consistent
- [ ] limitations explicit
- [ ] recommendations executable
- [ ] no unsupported causal claims

## Gate L — Handoff
- [ ] outputs named clearly
- [ ] validation evidence included
- [ ] exceptions included
- [ ] limitations included
- [ ] recipient can continue without author
- [ ] no confidential temp/source artifacts unintentionally included

## Severity for failures

- **BLOCKER** — cannot safely deliver.
- **MAJOR** — deliver only with explicit limitation/approval.
- **MINOR** — fix when practical; does not change core conclusion.
- **IMPROVEMENT** — polish/maintainability.

## Completion rule

A material `BLOCKER` means the work is not complete. A `MAJOR` issue must either be resolved or clearly disclosed with its impact.
