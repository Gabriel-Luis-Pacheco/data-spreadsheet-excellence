# Data Analysis Quality

The objective is not to produce more statistics. It is to create evidence that is correct, interpretable, decision-relevant, and proportionate to uncertainty.

## 1. Define the analytical contract

Before calculating a critical KPI, document:

- name and business meaning;
- formula;
- numerator/denominator;
- population;
- inclusion/exclusion rules;
- period/date field;
- unit/currency;
- source fields;
- treatment of missing/zero/error values;
- expected range;
- owner/source of definition when available.

If two teams use the same metric name with different definitions, do not silently pick one.

For recurring/A2/A3 metrics, use `assets/metric-contract-template.md` (or an equivalent data contract) so definition changes are reviewable.

## 2. Profile before interpreting

At minimum consider:

- row/column counts;
- schema and types;
- null counts/rates;
- duplicate rows and duplicate keys;
- unique values/cardinality;
- date range and gaps;
- invalid categories;
- numeric ranges/quantiles;
- outliers;
- control totals;
- distribution shifts by period/source;
- suspicious constants or default values.

Profiling should change what you do next. Do not generate a 50-page profiling report nobody uses.

## 3. Data quality dimensions

Assess relevant dimensions:
- completeness;
- validity;
- uniqueness;
- consistency;
- timeliness;
- accuracy where a trusted reference exists;
- integrity across related tables;
- representativeness when analysis generalizes beyond observed data.

Tie quality findings to materiality. “3% missing” is not enough; identify which fields, populations, and decisions are affected.

## 4. Denominators and populations

Many misleading analyses use a correct numerator over the wrong population.

Always ask:
- eligible population?
- active vs inactive records?
- snapshot vs cohort?
- records vs customers vs transactions?
- weighted or unweighted?
- are repeated entities counted multiple times?

State denominators next to rates when ambiguity is plausible.

## 5. Baselines and comparisons

Every “increase/decrease” needs a baseline.

Specify:
- prior period, prior year, plan, target, control group, benchmark, or model expectation;
- absolute change and relative change when both matter;
- calendar effects;
- partial-period bias;
- inflation/FX effects where relevant.

Avoid choosing the comparison that produces the most dramatic story.

## 6. Time series

Check:
- missing dates;
- irregular frequency;
- business-day vs calendar-day logic;
- seasonality;
- holidays;
- structural breaks;
- changing definitions;
- backfills/revisions;
- rolling-window alignment;
- timezone effects.

Do not call two points a trend.

## 7. Missing data

Classify why data may be missing:
- not collected;
- not applicable;
- system failure;
- delayed;
- suppressed;
- unknown.

Do not impute automatically. If imputing:
- state method;
- justify assumptions;
- compare results with/without imputation;
- preserve an imputation flag.

## 8. Outliers

Do not delete outliers just because they are inconvenient.

Determine whether they are:
- data errors;
- legitimate rare events;
- separate population;
- unit/scale mistakes;
- process changes.

Show sensitivity with and without influential values when the conclusion depends on them.

## 9. Statistical inference

Use inference only when it adds information.

Distinguish:
- effect size;
- uncertainty/confidence interval;
- p-value;
- practical/material significance.

Check assumptions and dependence structure. Correct or contextualize multiple comparisons. Avoid “statistically significant” as a synonym for important.

## 10. Causality

Observational association is not causal evidence by default.

Use proportional language:
- “associated with” for observational relationships;
- “consistent with” when evidence is suggestive;
- causal language only when design supports it.

Consider confounding, reverse causality, selection, leakage, and post-treatment variables.

## 11. Segmentation and Simpson's paradox

Averages can hide composition effects.

Segment by business-relevant dimensions:
- region;
- customer type;
- channel;
- tenure;
- product;
- cohort;
- risk band;
- process stage.

Compare aggregate and segment patterns before generalizing.

## 12. Robustness and sensitivity

For material conclusions:
- vary uncertain assumptions;
- test alternate definitions;
- test alternate thresholds;
- remove influential segments;
- compare reasonable windows;
- recompute with an independent method.

A conclusion that disappears under a minor reasonable change should be presented as fragile.

## 13. Insight ladder

Do not confuse data with insight.

1. **Value:** “12.4%”
2. **Observation:** “up 3.1 p.p.”
3. **Context:** “increase is concentrated in new customers”
4. **Diagnosis:** “onboarding >7 days is associated with 2.3× the rate”
5. **Implication:** “this group represents X exposure”
6. **Action:** “reduce backlog >7 days and monitor weekly”

Stop at the highest level the evidence supports. Never invent diagnosis/action to make the analysis sound impressive.

## 14. Sense checks

Independent checks often catch errors faster than code review.

Examples:
- recompute a sample manually;
- compare with a known external/internal benchmark;
- compare totals to finance/ERP control totals;
- test impossible values;
- perturb one input and check response direction;
- compare historical ranges;
- reverse-calculate an input from the output.

## 15. Analytical failure modes

Watch for:
- survivorship bias;
- selection bias;
- target leakage;
- denominator drift;
- duplicated entities;
- partial-period comparisons;
- multiple testing;
- regression to the mean;
- confounding;
- Simpson's paradox;
- cherry-picked windows;
- false precision;
- causal overclaim;
- silently excluded records.

## 16. Evidence package for material analysis

Preserve:
- source manifest/hash where appropriate (use `scripts/file_manifest.py` for a simple local manifest);
- data dictionary/schema contract for shared or recurring datasets (see `assets/data-dictionary-template.md`);
- metric definitions;
- transformations;
- parameters;
- row counts/control totals;
- exception tables;
- version/environment;
- key charts/tables;
- limitations;
- review notes.

The goal is not bureaucracy. It is enabling another competent analyst to reproduce or challenge the result.


## 17. Numerical precision and financial materiality

Choose numeric representation from the decision requirement.

- Use normal floating point when its precision is adequate for the analysis.
- Use decimal/fixed-point or integer minor units when exact currency/accounting arithmetic requires it.
- State rounding rules and when they are applied.
- Compare money using a documented tolerance/materiality rule rather than ad hoc equality.
- Distinguish source precision from display precision.
- Avoid rounding each intermediate step unless that is part of the business rule.
- Reconcile totals using the same currency, FX basis, unit scale, and rounding policy.

A result that differs by 0.01 can be immaterial in one analysis and a control failure in another; encode that distinction explicitly.


## 18. Schema and definition drift

Recurring analysis must detect changes in what the data **means**, not only whether the pipeline still runs.

Watch for:
- added/removed/renamed columns;
- type changes;
- unit/currency changes;
- enum/category expansion;
- key uniqueness/cardinality changes;
- source-system migrations;
- changed null/default semantics;
- metric-definition revisions;
- historical backfills that alter prior periods.

Classify changes as:
- **compatible/additive** — downstream logic still valid;
- **behavior-changing** — results can change and require review;
- **breaking** — pipeline/metric contract is no longer valid.

For A2/A3 recurring outputs, version the schema/metric contract and require review when a material definition changes.
