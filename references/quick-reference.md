# Quick Reference

Use this file when the task is routine and you need a compact execution checklist.

## Triage in 60 seconds

1. What decision/action does the output support?
2. Is the task low, medium, or high risk?
3. What is the spreadsheet fidelity: F0 data, F1 structure, F2 visual, or F3 Excel behavior?
4. What are the critical metrics, keys, totals, and exceptions?
5. Is this creation from scratch or round-trip editing of an existing workbook?
6. Which checks would catch a plausible material failure?

## Default workflow

`inventory → profile → contract → transform → reconcile/analyze → validate → design → visual QA → edit narrative → handoff`

## Fast tool matrix

| Problem | Start with |
| --- | --- |
| CSV / normal tabular analysis | pandas |
| Very large/lazy dataframe work | Polars |
| SQL joins/aggregations over files | DuckDB |
| Repeated analytical storage | Parquet |
| New polished XLSX | XlsxWriter |
| Simple existing XLSX edit | openpyxl |
| Macro/Power Query/pivot/complex Excel | Excel app via xlwings/COM |
| Google Sheets automation | Sheets API |
| Fuzzy names | RapidFuzz after deterministic matching |
| Probabilistic record linkage | Splink when justified |
| Statistical inference | SciPy / statsmodels |
| Dataframe contracts | Pandera or explicit validation |

## Join checklist

- profile each key;
- count null keys;
- count duplicate keys;
- state expected cardinality;
- normalize conservatively;
- use `validate=` where supported;
- use merge indicator / explicit anti-joins;
- report left-only, right-only, matched;
- compare control totals before/after;
- investigate unexpected many-to-many expansion.

## Spreadsheet visual checklist

- purpose obvious in seconds;
- one primary focus per view;
- consistent number formats and units;
- inputs/outputs/checks discoverable;
- no decorative rainbow formatting;
- restrained semantic color;
- labels close to data;
- chart titles tell the takeaway when justified;
- axes/scales honest;
- blanks/zero/N/A semantically distinct;
- visual QA performed when presentation matters.

## Writing checklist

Delete or rewrite a sentence if it:
- repeats the prompt;
- says “important”, “robust”, “valuable”, “strategic”, or “insight” without evidence;
- could fit almost any dataset;
- hides the denominator, period, baseline, or unit;
- mixes fact and speculation;
- recommends action without linking it to evidence.

Prefer:
`what changed → where → magnitude → comparison → implication → limitation/action`

## Final evidence

A credible delivery says:
- what was processed;
- what changed;
- what matched / did not match;
- what checks passed;
- what was not verified;
- where exceptions are;
- what the recipient should do next.
