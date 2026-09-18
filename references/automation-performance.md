# Automation, Performance, and Reproducibility

Automation quality is measured by reliability and recoverability, not by how few clicks remain.

## 1. Pipeline shape

A robust recurring pipeline often looks like:

`ingest → validate → normalize → transform → analyze/reconcile → validate → render/export → QA → publish → manifest`

Separate stages enough that failures are diagnosable.

## 2. Idempotency

A rerun with the same inputs/parameters should not create uncontrolled duplication.

Use deterministic output naming, run IDs, upserts where appropriate, staging directories, atomic replace/move, and checkpoints only when needed.

## 3. Input manifest

Capture file names/URIs, sizes, modified timestamps, hashes for high-risk work, source system, extraction timestamp, schema/version, and period.

Do not rely only on “latest file in folder” for critical workflows without guards.

## 4. Configuration

Keep changing business parameters outside code when appropriate: paths, thresholds, date windows, mappings, tolerances, output naming, and environment settings. Validate configuration before execution.

## 5. Performance hierarchy

Optimize in this order:
1. remove unnecessary work;
2. reduce I/O;
3. batch operations;
4. vectorize/use set-based transforms;
5. use efficient storage;
6. choose a more suitable engine;
7. parallelize only when safe;
8. micro-optimize last.

## 6. pandas

Avoid row-by-row loops for normal transforms. Prefer joins, groupby, vectorized string/datetime operations, selected columns/types, and categorical dtypes where beneficial. Move repeated large pipelines to Parquet/DuckDB/Polars when justified.

## 7. Polars

Use lazy execution for large workflows:
- scan rather than eagerly read;
- select/filter early;
- let optimizer push down operations;
- use streaming-compatible operations where helpful;
- explicitly sort when deterministic order matters.

Benchmark representative data.

## 8. DuckDB

Use file-native SQL to avoid unnecessary dataframe materialization. Good for multi-file aggregations, large joins, Parquet scans, and SQL-based audit queries.

## 9. Excel writing

Cell-by-cell writing is slow.

- write arrays/ranges;
- reuse format objects;
- avoid formatting unused worksheets;
- reduce volatile formulas;
- limit conditional formatting to actual ranges;
- use memory-optimized modes only after checking feature trade-offs.

## 10. Office Scripts

Performance depends heavily on workbook round-trips.

- get values once;
- process in arrays;
- set values in bulk;
- avoid workbook reads inside loops;
- reduce logging;
- manage calculation only when necessary.

## 11. Google Sheets

- batch reads/writes;
- limit ranges/fields;
- avoid high concurrency on one spreadsheet;
- use exponential backoff with jitter for transient/quota errors;
- bound retries;
- do not retry validation/auth failures blindly.

## 12. Retry taxonomy

Retry 429/throttling, transient network failures, selected 5xx errors, and temporary locks when safe.

Do not blindly retry invalid schemas, bad credentials without a refresh path, deterministic formula errors, invalid file formats, or failed business invariants.

Retries must not duplicate side effects.

## 13. Logging

Useful logs include run ID, start/end, input manifest, parameters, row counts, warnings, validation results, outputs, and exception counts.

Avoid full PII rows, credentials, access tokens, or sensitive free-text dumps.

## 14. Errors

Fail loudly on material invariants.

Good: `Expected account_id unique in master; found 318 duplicate rows across 147 IDs.`

Bad: `Something went wrong.`

For recoverable exceptions, write an exception artifact rather than dropping records.

## 15. Dependency management

Recurring automation should have version constraints, reproducible environments, representative tests, and upgrade notes for libraries that can change I/O behavior.

## 16. Testing pyramid

**Unit:** normalization, metrics, matching, dates.

**Integration:** readers, joins, workbook writers, APIs.

**Artifact regression:** sheet names, row counts, formulas, named ranges, key styles, selected rendered images/PDFs.

**End-to-end:** representative source → final artifact → checks.

## 17. Golden files

Keep small representative fixtures. Compare semantics rather than volatile metadata. Normalize timestamps. Document intentional changes. Avoid tests so brittle that every cosmetic change fails.

## 18. Observability

For recurring jobs track success/failure, duration, input size, exception count, match rate, critical KPI drift, and publication status.

Alert on meaningful conditions, not every warning.

## 19. Concurrency

Be cautious with Excel desktop automation, simultaneous writes to one workbook, shared cloud sheets, temporary filenames, and stateful COM objects. Use locks/queues or isolated runs when necessary.

## 20. Handoff

A recurring pipeline should explain how to run, dependencies, inputs/outputs, configuration, controls, common failures, rollback/recovery, ownership, and how to validate success.
