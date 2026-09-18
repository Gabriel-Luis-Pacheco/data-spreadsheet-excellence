# Tool Selection and Execution Environment

Choose tools from the requirements backward. The best library is the one that satisfies fidelity, scale, environment, maintainability, and validation needs with the least risk.

## 1. Ask these questions first

1. Is the source tabular data or an application-rich workbook?
2. Is the task read-only, create-new, or round-trip edit?
3. Must macros, pivots, queries, links, shapes, names, or chart behavior survive?
4. Does recalculation need to be current?
5. How large is the data?
6. Is Excel installed? Windows? headless Linux? cloud?
7. Is the process interactive, one-off, scheduled, or CI?
8. Must the result be easy for nontechnical people to maintain?

## 2. pandas

Use for the default analytical middle layer: cleaning, joins, reshaping, groupby, time series preparation, and moderate-size data.

Strengths:
- broad ecosystem;
- excellent interoperability;
- simple joins and reshaping;
- many Excel/CSV/SQL connectors.

Rules:
- use `dtype`/converters intentionally for IDs and codes;
- select only needed columns on large reads;
- profile keys before `merge`;
- use `validate=` to assert expected merge cardinality;
- use `indicator=True` or anti-joins to expose unmatched rows;
- remember null-key merge semantics can differ from SQL;
- avoid `iterrows()` for transformations that can be vectorized/set-based;
- test locale/date parsing explicitly.

## 3. Polars

Prefer when:
- data is large enough that pandas memory/runtime is material;
- lazy query optimization is valuable;
- streaming execution helps;
- pipelines are expression-heavy.

Rules:
- use `scan_*`/LazyFrame for large pipelines;
- let the optimizer push projections/filters when possible;
- sort explicitly if row order matters;
- do not rely on incidental ordering across joins/grouping/streaming engines;
- benchmark against pandas/DuckDB for the actual workload rather than assuming faster is always better.

## 4. DuckDB

Prefer for:
- SQL-native analysts;
- large joins/aggregations over CSV/Parquet;
- querying files without loading all data into pandas first;
- reproducible SQL transformations;
- mixing local files and dataframes.

Good pattern:
`raw files → DuckDB SQL → Parquet/validated dataframe → delivery workbook`

Avoid forcing DuckDB when the transformation is simple and pandas is clearer.

## 5. Parquet and Arrow

Use Parquet for repeated analytical pipelines when:
- types must survive better than CSV;
- column pruning matters;
- files are reused many times;
- compression/storage efficiency matters.

Keep CSV for interoperability, simple exchange, or systems that require it. Treat CSV as a serialization format, not a typed data model.

## 6. Excel ingestion engines

Choose based on format and features, not habit.

- `.xlsx`: `openpyxl` is common; `calamine` may be useful for fast/heterogeneous reading.
- `.xlsb`: use a compatible engine such as `pyxlsb` or calamine where appropriate.
- legacy `.xls`: choose an engine that explicitly supports it.
- formulas: know whether you are reading formula strings or cached values.

Reading an Excel file successfully does not imply you can safely round-trip it with the same engine.

## 7. XlsxWriter

Excellent for creating new `.xlsx` files with:
- polished formats;
- tables;
- charts;
- conditional formatting;
- formulas;
- controlled workbook layout.

Important:
- it creates new workbooks; it is not a general editor of existing files;
- it does not calculate Excel formulas itself;
- cached formula results and recalculation behavior matter for downstream consumers;
- `constant_memory` can reduce memory use but changes writing constraints and may restrict features.

## 8. openpyxl

Good for ordinary OOXML workbook inspection/editing when fidelity risk is understood.

Use for:
- values/formulas;
- common styles;
- worksheets;
- tables/names;
- many standard workbook structures.

Do not assume perfect round-trip fidelity. Complex drawings, external content, macros, pivots, queries, and application-specific artifacts require explicit risk assessment.

For `.xlsm`, preserve VBA only when the workflow and library mode support it, and still test the round trip.

## 9. xlwings / COM

Use the actual Excel application when:
- F3 behavior matters;
- formulas must recalculate in Excel;
- refresh behavior must run;
- macro-enabled or complex corporate workbooks must be preserved;
- export/print behavior needs the Excel renderer.

Risks:
- platform/environment dependency;
- interactive dialogs and security;
- orphan Excel processes;
- asynchronous refresh;
- concurrency fragility.

Automate lifecycle and cleanup carefully.

## 10. Office Scripts

Good for Microsoft 365/web-based workbook automation.

Performance:
- minimize calls between script and workbook;
- read ranges once, process locally, write back in batches;
- avoid workbook reads inside loops;
- pause/reduce calculation only when appropriate and restore state.

## 11. Google Sheets API

Use for collaborative cloud sheets.

Rules:
- prefer `batchUpdate`/batched value updates;
- retrieve only needed ranges;
- use field masks where applicable;
- avoid uncontrolled concurrent writes;
- use exponential backoff for quota/transient errors;
- keep payloads reasonably bounded;
- re-read critical ranges after material writes when correctness matters.

## 12. RapidFuzz and Splink

RapidFuzz:
- good for candidate scoring after normalization/blocking;
- use scorer appropriate to token order/structure;
- threshold is domain-specific;
- retain candidate, score, method, and ambiguity.

Splink/probabilistic linkage:
- useful when multiple imperfect fields jointly determine identity;
- requires modeling/threshold calibration and validation;
- do not use it to avoid understanding identifiers.

## 13. Pandera / validation frameworks

Use when:
- dataframe schemas are stable enough to encode;
- recurring pipelines benefit from contracts;
- type/range/uniqueness checks should fail loudly.

For small one-off jobs, explicit validation functions may be clearer than adding a framework.

## 14. Selection anti-patterns

Avoid:
- “always use openpyxl for Excel”;
- “always use pandas because everyone knows it”;
- using a dataframe for pixel-perfect workbook edits;
- using COM for simple CSV aggregation;
- fuzzy matching before deterministic matching;
- converting everything to strings to make errors disappear;
- switching stacks for novelty rather than a measurable benefit.
