# Reconciliation and Matching

Reconciliation quality is determined by the exceptions you can explain, not by how close the final net number looks.

## 1. Start with the reconciliation contract

Define:
- source A and B;
- grain of each source;
- trusted identifiers;
- expected relationship/cardinality;
- amount/date tolerances;
- time window;
- currency/unit;
- matching priority;
- materiality threshold;
- allowed one-to-many cases;
- how duplicates are resolved.

## 2. Normalize conservatively

Keep original fields and create normalized versions.

Possible normalization:
- trim/collapse whitespace;
- case-fold;
- Unicode normalization;
- accent handling where domain-appropriate;
- punctuation/legal-suffix normalization;
- standardized phone/email;
- leading-zero handling for identifiers;
- date/time normalization;
- address token standardization.

Do not remove information blindly. “ACME 01” and “ACME 10” may be different entities.

## 3. Profile key quality

Before joining:
- null key rate;
- uniqueness;
- duplicate counts;
- collision rate after normalization;
- invalid format;
- length distribution;
- unexpected prefixes;
- keys present only in one source.

Normalization can create collisions; measure them.

## 4. Deterministic matching ladder

Prefer:
1. trusted unique ID;
2. normalized unique ID;
3. composite exact key;
4. deterministic business rule with tolerances;
5. candidate blocking + fuzzy scoring;
6. probabilistic linkage;
7. manual review.

Record which rule produced each match.

## 5. Join cardinality

State expected cardinality and validate it.

Examples:
- invoice header to invoice detail: `1:m`;
- account master to unique account snapshot: `1:1`;
- many-to-many only when genuinely expected.

Unexpected many-to-many joins can inflate rows, sums, counts, and apparent match rate.

Always compare pre/post row counts and totals.

## 6. Null join keys

Do not assume dataframe joins behave exactly like SQL. Explicitly isolate null keys and decide whether they are invalid, unmatched, a separate review population, or safely coalesced using another key.

Never let null-null matching silently create “matches” without a business rule.

## 7. Anti-joins / exception populations

Produce explicit tables for:
- matched;
- left-only;
- right-only;
- ambiguous;
- duplicate-key;
- invalid-key;
- tolerance-failed;
- manually reviewed.

The exception table is a first-class deliverable.

## 8. Amount/date tolerances

Define tolerances from business meaning.

Examples:
- exact cents for ledger posting;
- small FX/rounding tolerance;
- settlement date ±N business days;
- unit conversion tolerance.

Do not choose tolerance after seeing the result merely to increase match rate.

## 9. Fuzzy matching

Use fuzzy matching for candidate ranking, not as a magic identity oracle.

Good process:
1. normalize;
2. block candidates using geography/domain/first token/etc.;
3. choose scorer based on field structure;
4. inspect score distribution;
5. define accept/reject/review zones;
6. validate against labeled examples if possible;
7. retain score, candidate, scorer, threshold, and decision.

Do not use one universal threshold for every dataset.

## 10. Multiple fields

Combine signals such as name, address, postal code, phone, email, date, amount, and identifier fragments.

A strong name score with contradictory tax ID should not automatically match.

## 11. Probabilistic linkage

Use a probabilistic method when no single reliable identifier exists, multiple noisy fields jointly identify entities, or scale makes manual rules brittle.

Requirements:
- calibrated comparisons/weights;
- labeled or reviewed examples where possible;
- thresholds aligned to false-match/false-nonmatch costs;
- audit trail;
- review of uncertain zone.

## 12. Reconciliation summary

A professional summary should show both counts and values:
- source A rows / total value;
- source B rows / total value;
- matched rows / matched value;
- left-only rows/value;
- right-only rows/value;
- ambiguous rows/value;
- duplicates;
- manual-review population;
- gross unmatched value;
- net difference;
- top material exceptions;
- concentration by category/entity/period.

A zero net difference can hide two large offsetting errors.

## 13. Materiality

Rank exceptions by absolute value, percentage impact, frequency, regulatory/business importance, recurrence, and confidence.

Do not bury one critical mismatch inside thousands of trivial differences.

## 14. Review sampling

For high-risk matching:
- sample accepted matches near threshold;
- sample rejected candidates near threshold;
- sample exact matches when source key quality is questionable;
- review top-value matches and exceptions separately.

## 15. Reproducibility

Persist normalization rules, matching rules, thresholds, candidate blocking, software versions, manual overrides, reviewer, and reason for override.

Manual review is part of the model and must be traceable.

## 16. Recommended output tabs/files

For a business-facing reconciliation workbook:
- `Summary`
- `Matched`
- `Only_Source_A`
- `Only_Source_B`
- `Ambiguous`
- `Duplicates`
- `Rules_&_Definitions`
- `QA_Checks`

Keep raw source extracts separate or clearly marked.
