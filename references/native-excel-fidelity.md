# Native Spreadsheet Functionality — Real Objects, Not Lookalikes

## Non-negotiable contract

**When the user asks for an Excel feature, deliver the actual editable, functional feature in the Excel workbook, while preserving the original schema.** A real PivotTable does not authorize new source columns named `QTD`, `EMBARQUE` or `CONCILIA` unless they are expressly requested/approved. Use existing source fields, existing native objects, or separately authorized data support. Producing a visually similar range, screenshot, static export, formula simulation, styled grid, image, or generic dropdown is NOT equivalent unless the user explicitly chooses that alternative.

"Make it like I manually built it in Excel" refers to the **result**: a normal workbook whose real Excel objects respond to the same clicks and operations a human-made workbook would. The creation process can absolutely be automated via Excel, Office Scripts, VBA, COM, or supported libraries. Do not perform repetitive mouse clicks for theater when a supported native API creates the same object.

A functioning native feature is independently testable. A workbook that opens and looks convincing is not enough.

## 1. Define the interaction before building

For each explicitly requested feature identify:
1. **Native object type:** PivotTable, Excel Table (ListObject), chart, slicer, timeline, data validation, conditional format, formula, hyperlink, named range, connection, Power Query, macro, control, etc.
2. **Expected Excel UI behavior:** what the recipient clicks, what menu/field list appears, what can be edited, and what is recalculated or refreshed.
3. **Source and update relationship:** how the object connects to real data, including growth, source ranges, caches, relationships, and refresh conditions.
4. **Target runtime and file type:** Excel desktop/web/version/platform, allowed macros and connections, `.xlsx` vs `.xlsm`; user access and compatibility.
5. **Proof:** observable object existence AND a relevant interaction/refresh/calculation test when possible.

Do not silently downgrade fidelity because a familiar Python library is faster.

## 2. Native feature acceptance matrix

| User asks for | Required deliverable | Not equivalent | Minimum meaningful verification |
| --- | --- | --- | --- |
| **Tabela Dinâmica / PivotTable** | True Excel PivotTable + PivotCache + configured row/column/value/filter hierarchies; maintainable source | pandas pivot aggregation exported as cells, SUMIFS grid, screenshot, visually grouped range | Excel recognizes it as PivotTable; field list works, reconfigure fields, refresh after source change, control totals agree |
| **Tabela do Excel / Ctrl+T** | Actual Excel Table (ListObject), header/filter behavior, proper table range | header color/borders and manually drawn stripes | Excel shows Table Design, filter/structured references work, new rows included as intended |
| **Segmentação de dados / Slicer / Linha do Tempo** | Actual bound slicer/timeline with supported connection | colored shapes, buttons, cell-based imitation | selection filters the intended native Table/PivotTables correctly |
| **Gráfico do Excel** | Editable Excel chart object with live data references and correct series | PNG/image/canvas imitation | select/edit chart in Excel; changing source updates it |
| **Fórmulas / cálculos automáticos** | Actual cell formulas, valid syntax and calc state | precomputed numbers pasted as values | formula bar contains formula; edit inputs and confirm recalculation |
| **Validação de dados / menu suspenso** | Native data-validation rules associated with correct cells and source | an instruction saying "select one", static list | Excel data-validation behavior accepts permitted values and handles invalid values |
| **Formatação condicional** | Native conditional-formatting rules | manually painted cells | changing values changes formatting according to rule |
| **Filtros / ordenação** | Native AutoFilter or Table filters where requested | static sorted output only | native filter UI works correctly |
| **Power Query / conexão / Atualizar** | Genuine query and supported connection with valid source and refresh behavior | preprocessed snapshot labeled "Power Query" | query/connection visible in intended Excel and refresh tested within authorized environment |
| **Macro / botão funcional** | Genuine authorized macro/controller behavior in appropriate file type | shape with text "Atualizar" and no action | safe authorized macro/action invocation works in target Excel |
| **Links / referências entre abas** | Working references / native hyperlinks as requested | link-colored text | click / source update resolves correctly |
| **Dashboard interativo** | Appropriate combination of native tables/charts/pivots/slicers, connected to actual data | static graphic with fake filter controls | test each advertised interaction and the underlying metrics |

An Excel Table (`Ctrl+T`) and a PivotTable are different object types. Neither substitutes for the other. A worksheet that *looks* like a pivot does not become a PivotTable merely because its totals are correct.

For Google Sheets and other spreadsheet platforms, use **the platform's own native feature**, not an Excel-only structure that loses behavior after conversion. Explicitly separate unsupported features.

## 3. Tool choice by capability, not convenience

**Preferred when native Excel behavior is essential:**
- Use a **real Excel host** with supported automation (Windows Excel via COM/xlwings/VBA, or Microsoft 365 Office Scripts / Excel JavaScript APIs where the requested feature is exposed and permitted). Check platform and version support before assuming.
- For native pivots, Excel object model supports `PivotCaches.Create` / `PivotCache.CreatePivotTable`; Office Scripts exposes `addPivotTable`, pivot hierarchies and `refresh()`.
- Prefer an existing user/company workbook/template with the necessary native objects when appropriate, modifying it with a preservation-aware Excel-host workflow rather than reconstructing the objects in a less capable library.
- `openpyxl` can preserve/read existing pivots in supported scenarios; it is **not a general create-new-PivotTable API**. Round-trip preservation of complex objects must still be verified.
- XlsxWriter can create native Excel **Tables** and charts, but do not assume that native PivotTables, slicers, Power Query, or every F3 object can be authored merely because it writes valid `.xlsx`. Re-check current feature support.
- `pandas.pivot_table()` is a useful analytical **calculation**, NOT a native Excel PivotTable artifact.
- Avoid homemade OOXML object injection or hand-patching ZIP internals as a shortcut for unsupported API creation. Treat such work as specialist engineering requiring robust packaging/relationships/cache and real-Excel validation, not an ordinary agent fallback.

**If no suitable Excel host/API is available:** investigate an available supported path, including a native-template workflow. Do **not** quietly replace the required native feature with something cosmetic. State precisely what could/could not be delivered. A static preview or alternative can be supplied only **clearly labeled** and only if acceptable to the user; never falsely claim it meets native requirements.

## 4. Conventional human spreadsheet experience

For an **existing** workbook, keep its original names, fields, styles and sheet structure, even if a generic cleaner layout is possible. The examples below apply to **newly designed artifacts or explicitly authorized redesigns**, not automatic alterations of the user's file.

Build as a careful real Excel user would:
- direct, ordinary sheet names (for example, `Base`, `Resumo`, `Tabela Dinâmica`), easy-to-find objects, standard Excel behavior;
- filters in genuine Tables, sensible freeze panes, clean columns, usable formats and print settings;
- readable numbers, dates, units and source labels according to the user's language and conventions;
- easy refresh, understandable field names and appropriately expanding data source;
- no fake "dashboard controls", decoration that looks interactive but isn't, nonfunctional buttons, giant README/QA/log sheets or gratuitous execution metadata in the reader-facing workbook;
- internal provenance and required assurance can live in an appropriately scoped, separate evidence artifact or discreet checks, not by cluttering the finished report.

"Human" is **normal interaction, obvious semantics, and reliable updates**, not deliberately adding mistakes or claiming a person manually clicked through Excel.

## 5. Validate actual behavior, efficiently

Use **two complementary layers**:

1. **Structural inventory** (quick, preliminary): inspect workbook objects with a suitable library or XML package scanner; for a PivotTable, expect pivot-table/cache parts and relationships; for an Excel Table, expect Table/ListObject metadata. Absence can disprove a claimed feature; presence alone cannot guarantee full behavior.
2. **Target-application interaction** (decisive for F3): open in the intended Excel environment, locate the real feature, exercise the relevant action (e.g. edit pivot fields; refresh after controlled source change; change a formula input; operate slicer; click button), reconcile outputs, and preserve the final workbook.

Do not run elaborate UI sequences for every trivial formatting edit. Test **one representative interaction per required native feature**, more only if assurance, errors, or multiple dependencies warrant it.

**PivotTable suggested test:** first reuse the original source/PivotTable when available. For a specifically requested **new** native PivotTable, configure it using valid existing or approved source fields, save/reopen, inspect fields, refresh after a controlled change on a test copy, reconcile independent totals, and restore the original data. Do not auto-create new helper columns/sheets or transform the original into a Ctrl+T Table merely because an example workflow does so.

**Editing existing workbooks:** inventory important native objects before and after; preserve the original; do not assert F3 preservation from a successful `openpyxl.save()` or ZIP comparison alone. If real Excel cannot be run, mark interaction as **not verified**, even when structural parts exist.

### Fast native-object inventory (preliminary only)

Use the provided read-only script on an OOXML workbook:

```bash
python scripts/inspect_native_excel.py workbook.xlsx --require pivot_table --pretty
python scripts/inspect_native_excel.py workbook.xlsx --require excel_table --pretty
```

This checks expected OOXML parts and, for PivotTables, a worksheet-to-PivotTable relationship and a PivotTable-to-cache relationship. It is **not** a certification that Excel can open, configure, refresh, or preserve the feature. Keep full interactive verification separate and appropriate to F3 risk. A structural positive alone is not completion evidence.

## 6. Acceptance and truthful delivery

Check the native feature AND the preservation of the original workbook's allowed sheets/headers with `references/source-schema-contract.md`; real Excel interactivity and source-schema fidelity are **both** required.

**Definition of done for a native request:** the saved file contains the correct native object; recipient can use it through normal Excel UI; source update/refresh/calculation behavior works where required; content and style fit the user's actual workflow. The requested native object is a requirement, not an optional polish item.

Never claim "native PivotTable built" based only on a grouped summary table, a visual screenshot, or a script that was never executed. If a real native object cannot be created/verified, do not disguise that omission. State the missing capability and most practical supported route without promising unperformed actions.
