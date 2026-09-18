# Writing, Review, and Handoff

Professional analytical writing is compressed reasoning, not polished filler.

## 1. Start with reader and decision

A finance controller, operations manager, executive, engineer, and auditor need different levels of detail. Choose the decision, reader knowledge, evidence threshold, required caveats, and actionability.

## 2. Put important information first

A strong short analytical note often follows:
1. answer/finding;
2. magnitude and baseline;
3. driver/concentration;
4. implication;
5. limitation/uncertainty;
6. action or next check.

Do not open with generic scene setting.

## 3. Fact vs interpretation

**Fact:** `Late deliveries rose from 4.1% to 7.3% in August.`

**Interpretation:** `The increase is concentrated in two carriers.`

**Hypothesis:** `Capacity constraints may explain part of the increase.`

**Recommendation:** `Review carrier capacity and SLA breaches before changing allocation.`

Do not collapse all four into one confident sentence.

## 4. Specificity test

Weak: `The analysis identified important insights and opportunities for improvement.`

Strong: `214 duplicate invoices account for R$381k of gross exposure; 71% belongs to two suppliers.`

A sentence that could be pasted into almost any report probably adds little.

## 5. Compression test

Ask:
- can 30 words become 15 without losing evidence?
- does the second sentence repeat the first?
- is a table better than prose?
- is the heading carrying its share?

## 6. Anti-slop phrase watchlist

Review phrases such as:
- it is important to highlight;
- it is worth noting;
- valuable insights;
- robust analysis/solution;
- comprehensive approach;
- in today's dynamic environment;
- plays a crucial role;
- efficient and effective;
- actionable insights;
- leveraging data;
- informed decision-making.

Keep them only when they genuinely add meaning.

## 7. Numbers

Always include unit, period, denominator, baseline, and whether change is absolute or relative when ambiguity is plausible.

`Growth was 20%` is incomplete if it means 10 → 12 customers.

## 8. Uncertainty

Use calibrated language: exact/verified, estimated, indicative, associated, or unknown. Use likely/possibly only when evidence justifies it.

Do not use confident prose to hide weak evidence.

## 9. Recommendations

A useful recommendation includes action, trigger/reason, responsible decision point/owner when useful, timeframe when relevant, expected effect only when supported, and the metric to monitor.

Avoid recommendations that simply restate the problem.

## 10. Executive summaries

A good executive summary lets a busy reader answer:
- what happened?
- why does it matter?
- what is driving it?
- what should happen next?
- what is uncertain?

Do not summarize every section equally.

## 11. Review another analyst's work

Separate objective defects from style preferences.

Severity:
- `BLOCKER` — unsafe/materially wrong/unusable;
- `MAJOR` — can change interpretation or decision;
- `MINOR` — limited impact;
- `IMPROVEMENT` — quality/usability preference.

Each finding needs issue, evidence, impact, and resolution criterion.

Example:
`MAJOR — Customer count is inflated by a many-to-many join. Source A has 1 row/customer, Source B has repeated customer-month records; output rows increase 38%. Fix by aggregating Source B to customer grain or using the intended composite key.`

## 12. Five-pass review

**Analyst:** question, baseline, denominator, conclusion.

**Auditor:** reproducibility, joins/filters, exceptions, totals.

**Designer:** hierarchy, labels, visual noise, scales.

**Editor:** specificity, concision, natural language, filler.

**End user:** usability, period/source/units, next action, exceptions.

## 13. Handoff package

Depending on task, deliver final artifact, short summary, exception file/table, README/run instructions, validation evidence, limitations, source/parameter manifest, and change log.

The recipient should not need the original author for basic operation.

## 14. Good completion language

Prefer:
`Reconciled 42,318 of 42,911 records (98.6%). 593 remain unmatched; 81% of unmatched value is concentrated in 17 invoices. Row counts and source totals were preserved. Formula recalculation was not verified in desktop Excel.`

Avoid:
`The reconciliation was successfully completed and yielded valuable insights.`

## 15. Do not mimic fake “human imperfection”

Do not add typos, awkwardness, or randomness to “sound human”. Human-quality writing comes from specificity, judgment, rhythm, and restraint.


## 16. Language, locale, and audience conventions

Default the **human-facing delivery** to the user's or intended audience's language unless another language is explicitly required.

Localize deliberately:
- decimal and thousands separators;
- currency symbol/code and negative-number convention;
- percentage precision;
- date/time display;
- terminology used by the business;
- month/day names and report labels.

Do not confuse localization with data coercion.

For example:
- a Brazilian-facing report may display `R$ 1.234,56`;
- the underlying numeric cell/dataframe value should remain numeric where possible;
- identifiers should remain text where appropriate;
- machine-readable exchange formats should follow their defined schema rather than a visual locale.

Keep technical/library names, code, field identifiers, formulas, APIs, and file paths in the form required by the system. Translate explanation around them, not the syntax itself.

When source data mixes locales, determine the parsing rule before conversion; do not guess whether `01/02/2026` means 1 February or 2 January without context.
