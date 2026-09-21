# Excel Compatibility and Portability

Use this reference when a workbook will be opened in different Excel versions, exchanged across Windows/Mac/web environments, exported to legacy formats, or relies on newer formulas/features.

A workbook can be structurally valid and still fail for the recipient because the **target Excel environment** differs from the environment used to create or test it.

## 1. Declare the target environment

For material work, record:
- Excel version/channel when known;
- desktop Windows/Mac vs Excel for web;
- file format (`.xlsx`, `.xlsm`, `.xlsb`, legacy `.xls`);
- locale;
- whether external links/macros/Power Query are allowed;
- whether recipients may use older versions.

Do not design for “Excel” as if it were one fixed runtime.

## 2. Worksheet limits

Modern Excel worksheets support up to:
- **1,048,576 rows**;
- **16,384 columns**.

Do not use Excel as the raw storage layer for datasets that exceed or approach practical workbook limits. Aggregate/summarize and keep raw data in Parquet/database/warehouse storage.

Cell content and formula/style counts also have limits; very large styled workbooks may become slow or unstable before hard limits are reached.

## 3. Numeric precision

Excel numeric precision is limited to **15 significant digits**.

Therefore identifiers such as:
- 18-digit document numbers;
- account/card-like identifiers;
- long shipment/tracking codes;
- large integer keys

must generally be stored as **text**, not numeric cells, when every digit matters.

Formatting a numeric cell as text after precision was already lost does not restore the digits.

## 4. Date systems

Excel supports 1900 and 1904 date systems.

A workbook/date transfer can shift dates when date systems are mixed. Before round-trip editing or workbook comparison:
- inventory the workbook date epoch;
- preserve it;
- treat unexpected epoch change as a material risk.

Do not assume serial number `1` means the same date across workbooks using different systems.

## 5. Modern/dynamic-array formulas

Newer Excel versions support dynamic-array behavior and functions such as `FILTER`, `UNIQUE`, and spill ranges.

Compatibility concerns:
- older Excel may not understand newer functions/behavior;
- spilled formulas can be blocked by existing cells;
- linked dynamic arrays across workbooks have restrictions and may return `#REF!` when the source workbook is closed.

For workbooks distributed broadly, test the formulas in the **oldest supported target environment** or intentionally choose more compatible formulas.

## 6. Function compatibility

Functions such as newer lookup, dynamic-array, text, or lambda-related functions may not exist in older versions.

Do not choose a formula merely because it is elegant in Microsoft 365.

For each critical formula:
- know the minimum target version;
- prefer backward-compatible alternatives when required;
- use Excel Compatibility Checker when legacy compatibility matters.

## 7. Legacy file formats

Saving modern workbooks to older formats can cause:
- row/column truncation;
- formula loss;
- array limitations;
- formatting loss;
- PivotTable feature loss;
- unsupported object loss.

Treat a format downgrade as a transformation requiring validation, not a simple extension change.

## 8. Excel for web vs desktop

Features can differ across:
- VBA/macros;
- COM/add-ins;
- connectors;
- Power Query;
- advanced objects;
- printing/rendering;
- external-data refresh.

If the workflow depends on desktop-only behavior, state that clearly.

## 9. Locale

Human-facing display should follow the recipient:
- date format;
- decimal/group separators;
- currency;
- language;
- accounting conventions.

But keep typed data typed. Do not convert numbers to localized strings merely to make them look right.

Formula/API syntax can depend on the interface/tool used. Follow the library/application contract and verify in the target environment rather than blindly localizing formula strings.

## 10. Calculation compatibility

Even when a formula string saves successfully:
1. the library may not calculate it;
2. Excel may recalculate it differently by version/features;
3. cached values may be stale;
4. unsupported functions may become `#NAME?` or similar errors.

Critical cross-version work requires target-engine recalculation and error inspection.

## 11. Compatibility QA

For F2/F3 or A2/A3 work:
- preserve source;
- compare before/after structure;
- reopen in intended target version;
- recalculate;
- inspect formula errors;
- run compatibility checker when backward compatibility is required;
- verify representative dynamic formulas/links;
- test print/export if relevant;
- confirm macros/queries/pivots where required.

## 12. Anti-patterns

- writing 18-digit IDs as numeric cells;
- assuming Microsoft 365 formulas work in Excel 2019;
- changing 1900/1904 date system accidentally;
- exporting >1,048,576 rows to one worksheet;
- saving to legacy format without compatibility review;
- equating “openpyxl saved it” with “recipient Excel can execute it”.
