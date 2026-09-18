# Evaluation Cases

Use these cases to check whether the skill improves behavior without making simple tasks bloated.

## Eval 1 — messy ERP exports
Prompt: combine monthly CSV exports, clean customer IDs, calculate revenue, create a management workbook.

Expected:
- preserve leading-zero IDs;
- inventory/profile first;
- choose pandas/Polars/DuckDB based on scale;
- validate period coverage and control totals;
- separate data and presentation;
- visually QA the workbook.

Failure:
- IDs silently converted to integers;
- dropped rows;
- no totals;
- decorative formatting without hierarchy.

## Eval 2 — dangerous XLSM edit
Prompt: edit a corporate `.xlsm` with openpyxl and save over it.

Expected:
- classify F3 risk;
- inspect macros/links/queries/pivots/objects;
- preserve original;
- avoid claiming openpyxl guarantees fidelity;
- prefer Excel application automation if behavior matters.

## Eval 3 — reconciliation
Prompt: reconcile supplier lists whose names differ.

Expected:
- trusted/deterministic identifiers first;
- key cardinality profile;
- normalized exact/composite rules;
- blocked fuzzy candidates;
- review zone;
- matched/unmatched counts and values;
- exception table and materiality.

Failure:
- all-pairs fuzzy matching;
- universal score threshold;
- match percentage only.

## Eval 4 — analyst review
Prompt: review another analyst's workbook.

Expected:
- distinguish defects from preferences;
- severity classification;
- evidence, impact, resolution criterion;
- check data, method, workbook, visual, and writing.

## Eval 5 — executive dashboard
Prompt: make a workbook beautiful for the board.

Expected:
- understand decision and key metrics;
- simplify rather than decorate;
- hierarchy before color;
- limited primary KPIs;
- trend/context;
- exceptions;
- visual QA.

Failure:
- rainbow colors, merged-title excess, gauges, 3D charts.

## Eval 6 — causal overclaim
Prompt: write that training caused sales because they correlate.

Expected:
- do not overclaim;
- distinguish association from causation;
- identify evidence/design needed.

## Eval 7 — very large data
Prompt: join 300 million Parquet rows and export summary to Excel.

Expected:
- avoid full pandas materialization;
- use DuckDB/Polars/lazy scans;
- aggregate before Excel;
- export decision-useful summary/exceptions, not raw 300m rows.

## Eval 8 — Google Sheets recurring job
Expected:
- batch operations;
- range/field minimization;
- backoff;
- idempotency;
- avoid write races;
- post-write validation.

## Eval 9 — anti-slop writing
Input: “Our robust and comprehensive analysis generated valuable insights...”

Expected:
- replace with specific findings;
- quantify;
- shorten;
- separate fact/interpretation/action.

## Eval 10 — low-risk quick task
Prompt: add a total column to a 40-row CSV.

Expected:
- no process theater;
- simple safe transform;
- quick check.

## Scoring

Score 0–2 on:
- routing/tool choice;
- data integrity;
- validation;
- risk proportionality;
- communication;
- usability;
- honesty about limitations.

Target:
- no zero on integrity/validation for medium/high-risk cases;
- average ≥1.7;
- low-risk cases remain concise.
