# Data Contracts, Drift, and Observability

Use this reference for recurring pipelines, monthly/weekly reporting, external data feeds, APIs, ERP extracts, and any workflow where the same logical dataset arrives repeatedly.

A pipeline can keep running while becoming wrong. Schema validation alone is not enough: semantic meaning, units, freshness, category domains, and business definitions can drift without changing column names.

## 1. Contract layers

A useful data contract can contain several layers.

### Structural
- required columns;
- optional columns;
- expected types;
- key columns;
- uniqueness;
- nullability;
- allowed nested/array structure where relevant.

### Semantic
- unit/currency;
- business meaning;
- grain;
- timezone;
- identifier semantics;
- numerator/denominator;
- whether zero differs from missing;
- whether values are gross/net, booked/settled, local/base currency, etc.

### Domain
- allowed status/category values;
- code lists/reference tables;
- min/max or logical ranges;
- monotonic/ordering rules;
- cross-field invariants.

### Temporal
- expected refresh cadence;
- reporting period;
- timezone/calendar;
- maximum acceptable staleness;
- late-arriving data policy;
- backfill/revision policy.

### Volume/distribution
- expected row-count range;
- duplicate-key rate;
- null-rate bands;
- amount/count control totals;
- distribution or category-share drift where useful.

Do not encode every historical value as a hard rule. Contracts should detect material drift without making normal business change impossible.

## 2. Drift taxonomy

Distinguish:

- **schema drift:** columns/types/structure changed;
- **semantic drift:** same field name now means something different;
- **unit drift:** cents → currency units, kg → g, local → base currency;
- **domain drift:** new/removed status codes or reference values;
- **grain drift:** transaction-level feed becomes line-item or daily aggregate;
- **freshness drift:** data arrives late/stale;
- **volume drift:** unusual row/event count;
- **distribution drift:** mix/range/shape changes;
- **definition drift:** KPI logic, denominator, inclusion rule, or period changes;
- **source drift:** upstream system/extract mechanism changes.

Schema tests will not catch all of these.

## 3. Contract evolution

A contract is versioned behavior, not a frozen forever schema.

When a change is intentional:
1. identify breaking vs compatible change;
2. record effective date;
3. update contract/version;
4. update transformation logic;
5. test historical comparability;
6. document whether trends before/after remain comparable;
7. communicate downstream impact.

Do not silently loosen validation merely to make a new file pass.

## 4. Freshness

For time-sensitive workflows, define:
- source event/update timestamp;
- extraction timestamp;
- expected delivery cadence;
- accepted lag;
- stale-data behavior.

A file being present does not mean the data is current.

If freshness is uncertain, surface it near the result. Great Expectations and similar frameworks explicitly treat freshness as a first-class data-quality concern.

## 5. Reference data and code lists

Track:
- version/effective date;
- source/owner;
- new values;
- retired values;
- unmapped values.

Never silently map a new status to “Other” in a critical pipeline unless that is the documented rule.

## 6. Comparability across periods

Before trend analysis, ask whether:
- source system changed;
- definition changed;
- entity population changed;
- restatements/backfills occurred;
- currency/unit changed;
- calendar/fiscal boundaries changed.

If comparability is broken, annotate the break or restate history if appropriate.

## 7. Drift severity

Classify drift by impact.

- **INFO:** compatible addition, no material downstream effect.
- **WARN:** plausible effect; review required.
- **BREAKING:** transformation/metric behavior changes or output may be wrong.
- **BLOCKER:** cannot safely continue without a decision.

Avoid auto-accepting BREAKING/BLOCKER drift.

## 8. Observability for recurring jobs

Track over time:
- row count;
- source/control totals;
- null rates;
- duplicate rates;
- key coverage;
- category frequencies;
- unmatched rate/value;
- freshness lag;
- processing duration;
- rejected rows;
- schema/contract version;
- publication status.

Alert on decision-relevant change, not every fluctuation.

## 9. Baselines

Use baselines carefully:
- rolling historical bands;
- same weekday/month last year;
- expected contractual limits;
- control source totals;
- previous successful run.

Do not turn every deviation from yesterday into an anomaly.

## 10. Response to drift

When drift is detected:
1. identify dimension and magnitude;
2. determine intentional vs unexpected;
3. estimate downstream impact;
4. isolate affected outputs;
5. stop or continue based on severity/assurance;
6. update contract only after an explicit decision;
7. revalidate.

For A2/A3 work, preserve the drift decision in the evidence manifest.

## 11. Tool choices

Small/clear:
- explicit Python validation functions;
- Pandera.

Broader data quality:
- Great Expectations or equivalent.

Warehouse/model pipelines:
- dbt tests/contracts where appropriate.

Large analytical stores:
- SQL/DuckDB checks against schema/control tables.

Tooling does not replace metric/business definitions.

## 12. Anti-patterns

- “column exists, therefore data is valid”;
- silently casting incompatible values;
- automatically accepting new categories;
- treating stale data as current because the file timestamp changed;
- updating the contract to match every failing input;
- comparing KPI history across a definition break without disclosure;
- alerting on hundreds of low-value metrics while missing a unit change.
