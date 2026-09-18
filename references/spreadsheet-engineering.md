# Spreadsheet Engineering

This reference covers workbook structure, preservation, formulas, and application behavior. Visual design is covered separately.

## 1. Workbook as a system

A serious workbook has layers:
- input/raw;
- staging/normalization;
- calculation/business logic;
- outputs;
- checks;
- documentation/control.

Small workbooks do not need a worksheet for every layer, but the conceptual separation should remain clear.

## 2. Inventory before round-trip editing

Inspect:
- file extension;
- worksheets and visibility;
- used dimensions;
- tables;
- formulas;
- named ranges;
- merged cells;
- data validation;
- conditional formatting;
- charts/drawings;
- hyperlinks;
- external links;
- VBA/macros;
- pivot tables/caches;
- Power Query/connections;
- protection;
- print areas/page setup;
- hidden rows/columns;
- calculation settings.

Choose an editor only after this inventory.

## 3. Preserve the original

Default:
- read original;
- write to a separate output path;
- compare;
- replace only when explicitly requested.

For business-critical files, retain a source checksum or immutable copy.

## 4. Fidelity levels

**F0:** data values/schema.
**F1:** structure/formulas/tables/names.
**F2:** layout/charts/printing.
**F3:** Excel application behavior and complex objects.

The test plan must match the fidelity level.

## 5. openpyxl round-trip risk

openpyxl is powerful but not an Excel application.

Use it when:
- workbook features are within supported scope;
- exact object preservation is not critical;
- you can validate the round trip.

Be cautious with:
- macros;
- drawings/shapes;
- complex charts;
- pivots;
- external links;
- Power Query/connections;
- embedded objects;
- advanced conditional formatting.

Do not interpret “save succeeded” as “preservation succeeded”.

## 6. Macro-enabled files

For `.xlsm`:
- preserve VBA only with the correct library options/workflow;
- do not rename to `.xlsx`;
- test in Excel when macros matter;
- do not execute untrusted macros merely to validate the file.

## 7. Formula state model

Track four separate states:

1. formula text was written;
2. target application recognizes it;
3. calculation engine recalculated it;
4. cached displayed result is current.

Python libraries that write formulas generally do not implement the full Excel calculation engine.

If downstream processing relies on cached values, ensure actual recalculation happens in a compatible engine.

## 8. Formula quality

Prefer:
- consistent formulas down tables;
- structured references where they improve readability;
- bounded ranges;
- readable helper calculations;
- checks for totals and balances.

Avoid:
- hidden constants inside formulas without explanation;
- accidental mixed absolute/relative references;
- unbounded whole-column array formulas when expensive;
- volatile functions when unnecessary;
- long opaque formulas that cannot be audited.

## 9. Calculation and refresh

For Excel application automation:
- record calculation mode;
- trigger calculation appropriate to the workbook;
- wait for calculation completion;
- refresh external connections only when authorized;
- wait for asynchronous refresh;
- verify refreshed timestamps/control cells where possible;
- restore application state.

Do not save immediately after `RefreshAll` and assume data finished refreshing.

## 10. Workbook structure

Use sheet names that describe function.

Good examples:
- `README`
- `Inputs`
- `Raw_ERP`
- `Calc`
- `Summary`
- `Exceptions`
- `QA`

Avoid `Sheet1`, `Final_Final2`, or ambiguous abbreviations.

For recurring processes, include:
- owner;
- period;
- generated timestamp;
- source;
- version;
- refresh instructions.

## 11. Tables and ranges

Use structured tables when they improve:
- filtering;
- formulas;
- growth;
- readability;
- data validation.

Do not convert decorative report layouts into tables mechanically.

Keep one logical dataset per tab when feasible.

## 12. Inputs and protection

Inputs should be:
- clearly discoverable;
- validated;
- unit-labeled;
- separated from formulas;
- protected from accidental overwrite where risk justifies it.

Protection is usability control, not strong security.

## 13. Checks

Useful checks:
- balance equals zero;
- row counts;
- source totals;
- duplicate keys;
- missing mappings;
- date coverage;
- formula consistency;
- reconciliation status;
- refresh timestamp.

A check should have an expected state and make failure visible.

## 14. External links and connections

Inventory before editing.

Ask:
- are links expected?
- are sources trusted?
- should links remain live?
- will paths work for the recipient?
- is refresh authorized?
- is the workbook portable?

Do not silently break or “fix” links without understanding ownership.

## 15. Print/export

For F2:
- page orientation;
- margins;
- repeated headers;
- print area;
- scaling;
- page breaks;
- headers/footers;
- PDF/export output.

A workbook can look good on screen and fail when printed.

## 16. Google Sheets

Design for collaboration:
- protect formula regions;
- use validation;
- avoid excessive volatile/complex formulas;
- batch API writes;
- document ownership and automation;
- avoid API write races.

## 17. Python in Excel

Treat it as a distinct environment:
- code executes in Microsoft's managed environment;
- local filesystem/network assumptions differ from normal local Python;
- external data access follows supported paths such as Power Query;
- workbook integration is the strength, not arbitrary local automation.

## 18. Round-trip validation

After editing:
- reopen with the intended reader;
- compare sheet list and visibility;
- compare named ranges/tables;
- compare formula counts or hashes where meaningful;
- compare key styles/print settings for F2;
- validate macro container presence for `.xlsm`;
- visually inspect;
- open in Excel for F3.

## 19. Anti-patterns

- editing an unknown `.xlsm` with openpyxl and overwriting the original;
- relying on `data_only=True` as proof of recalculation;
- declaring a workbook valid because the ZIP structure opens;
- using Excel COM for a task that only needs CSV aggregation;
- mixing raw data and manual reporting cells in the same uncontrolled range;
- hiding errors with `IFERROR(...,"")` everywhere.

## 20. Before/after preservation evidence

For round-trip edits where preservation matters, compare the source and output semantically.

Use:

```bash
python scripts/workbook_diff.py original.xlsx output.xlsx --pretty
```

The comparator checks sheet order/state, defined names, formulas/content hashes (within scan budget), tables, merged ranges, validation, conditional formatting counts, charts/images counts, protection, print area, and selected presentation metadata.

Use `--fail-on-risk` as an opt-in regression gate.

Important: this is an **OOXML/openpyxl first-pass comparator**, not proof of F3 fidelity. It does not recalculate formulas, run macros, refresh queries, or guarantee preservation of every Excel object.


## 21. Excel boundary hazards: size, precision, and dates

Excel is a delivery/analysis application, not an unlimited typed database.

### Worksheet size

A worksheet supports at most:
- **1,048,576 rows**
- **16,384 columns**

Do not design a pipeline that needs to dump larger raw datasets into one worksheet. Aggregate/filter for Excel and keep the detailed layer in Parquet, DuckDB, a database, or another suitable store.

### Numeric precision

Excel numeric precision is limited to **15 significant digits**.

Therefore:
- account numbers, card-like numbers, tax IDs, tracking IDs, SAP/document codes, and other digit-only identifiers may need to be text;
- never “convert to number for convenience” when exact digit preservation matters;
- verify source-to-workbook round trips for long digit strings.

### Financial arithmetic

Binary floating-point can introduce tiny representation differences. For financial controls:
- define materiality/tolerance explicitly;
- use integer minor units (for example cents) or decimal/fixed-point arithmetic when exactness requires it;
- do not round intermediate values simply to make a reconciliation pass unless the business rule says to.

### Excel date systems

Excel workbooks can use different date epochs (1900 or 1904). Raw serial values can therefore represent different calendar dates across workbooks.

When copying/merging workbooks or manipulating date serials:
- inspect the workbook date system;
- prefer actual date/datetime objects over hand-written serial arithmetic;
- test cross-workbook date transfer;
- treat unexplained multi-year shifts as a potential date-system mismatch.

### Precision-as-displayed

Excel's “precision as displayed” option can permanently alter stored values to the displayed precision. Treat changing this setting as consequential and do not enable it casually.


## 22. Formula syntax vs user locale

Do not translate programmatic formula syntax merely because the workbook's audience uses another language.

When writing formulas with `openpyxl`:
- use English function names;
- use commas between function arguments rather than locale-specific semicolons;
- keep formula syntax compatible with the file format/library;
- localize labels, explanatory text, and display formats separately.

A Portuguese-facing workbook can display Portuguese labels and Brazilian number/date formats while its programmatically written OOXML formulas still use the syntax required by the library.
