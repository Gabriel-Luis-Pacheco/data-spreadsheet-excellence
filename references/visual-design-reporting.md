# Visual Design, Dashboards, and Reporting

A beautiful spreadsheet is not a colorful spreadsheet. It is an information interface with hierarchy, clarity, and deliberate emphasis.

## 1. Design from the user task

Identify whether the artifact is an operational table, review/audit workbook, management report, executive dashboard, financial model, published statistical table, or ad hoc analysis. Each needs a different density and interaction model.

## 2. Hierarchy before color

The first view should answer: where am I, what period/entity am I seeing, what matters most, what changed, what requires action, and where is the detail?

Use size, position, whitespace, grouping, and typography before strong color.

## 3. Color

Use a restrained semantic system:
- neutral base;
- one primary emphasis color;
- warning/error colors only for real status meaning;
- categorical palettes only when categories genuinely need distinction.

Do not use red/green as the only signal. Avoid “heatmap everywhere” formatting. Keep semantic meaning consistent across sheets.

## 4. Typography and alignment

- one or two font families at most;
- clear heading levels;
- avoid tiny text;
- left-align text for scanning;
- align numeric columns consistently;
- use whitespace instead of excessive border boxes.

## 5. Number formats

Format conveys meaning.

Use:
- units in headers/titles or formats;
- sensible decimal precision;
- thousands separators;
- consistent percentage decimals;
- unambiguous dates;
- consistent negative-number treatment.

Do not show more precision than the data justifies.

## 6. Blank, zero, N/A, suppressed

These are different states:
- `0` = known zero;
- blank = absent/unentered;
- `N/A` = not applicable;
- `—` = display convention only if documented;
- suppressed = withheld;
- error = data/logic problem.

Do not use blank to hide every undesirable state.

## 7. Tables

Use tables when readers need exact lookup or row-level action.

Good operational tables have descriptive titles, period/source notes, stable columns, clear units, meaningful sort, filters/freeze panes only when useful, and exception/status fields near the relevant row.

Avoid unrelated tables mashed together, decorative blank rows inside machine-readable data, merged cells inside datasets, and arbitrary color schemes.

## 8. Dashboards

An executive dashboard should not expose every metric.

Prefer:
- 3–7 primary KPIs;
- trend/context next to KPI;
- exceptions/risks;
- one or two decision-relevant breakdowns;
- explicit period;
- source/last refresh;
- definitions available nearby.

A dashboard is not a museum of chart types.

## 9. Chart selection

- trend → line;
- category comparison → bar;
- part-to-whole → stacked bar/simple composition;
- distribution → histogram/box/violin as audience allows;
- relationship → scatter;
- ranking → sorted bar/table;
- variance → diverging bar/waterfall where appropriate.

Use pie charts only for a few categories when exact comparison is not required. Use funnels only for real stages.

## 10. Titles

Bad: `Sales by Region`

Better: `South region accounted for 64% of the quarterly decline`

Use declarative conclusions only when supported. Otherwise use a neutral descriptive title.

## 11. Labels and legends

Reduce decoding:
- direct-label key series;
- label important points;
- annotate structural breaks/events;
- avoid redundant legends;
- do not label every point when clutter dominates.

## 12. Scales

- bars usually start at zero;
- line charts may use narrower scales when justified, but retain context;
- do not truncate to manufacture drama;
- keep comparable charts on comparable scales when comparison is intended;
- log scales require clear labeling and suitable audiences.

## 13. Uncertainty

Show when material:
- confidence/credible intervals;
- forecast ranges;
- scenario bands;
- sample size;
- sensitivity.

Do not present a point estimate as certainty when uncertainty drives the decision.

## 14. Conditional formatting

Use for threshold breach, risk, aging, missing action, or exception severity.

Avoid color scales on IDs, excessive icon sets, inconsistent meanings, and red/green-only encoding.

## 15. Operational vs published/accessibility mode

Internal features such as filters/freeze panes can improve workflow. For broad/public accessibility, minimize or document hidden structures and follow accessibility-specific guidance.

For published work:
- clear sheet names;
- titles/instructions near top-left;
- no merged cells in data regions;
- clearly marked tables;
- no unexplained blanks;
- no hidden rows/columns unless documented;
- language/title metadata where supported;
- accessibility checker plus manual review.

## 16. Visual QA

When presentation matters:
1. render/open workbook;
2. inspect first screen;
3. check widths/heights;
4. check wrapping/truncation;
5. check number formats;
6. check chart labels/axes;
7. check contrast;
8. inspect print/PDF if relevant;
9. inspect dense and exception sheets;
10. correct and repeat.

## 17. Design anti-patterns

- 20 equally strong colors;
- merged title blocks that break navigation;
- borders on every cell;
- tiny fonts to fit everything;
- centered numeric tables;
- charts for exact lookup tasks;
- 3D charts;
- gauges when a number + threshold is clearer;
- decorative icons with no decision meaning;
- branding that overwhelms data.

## 18. Executive reporting pattern

A strong management view often follows:
1. headline finding;
2. current KPI vs baseline/target;
3. trend;
4. concentration/driver;
5. exceptions/risks;
6. decision/action;
7. methodology/definitions available but not dominant.

The goal is fast comprehension without loss of necessary context.

## 19. Accessibility details worth checking

For broadly shared/published workbooks:
- put a meaningful title or instruction in/near A1 when appropriate; screen readers begin there;
- use simple table structures with explicit headers;
- avoid merged/split/nested cells in data tables;
- avoid unexplained fully blank rows/columns inside navigational data regions;
- provide alt text for meaningful charts/images where the target platform supports it;
- use sufficient contrast and do not encode meaning by color alone;
- run Excel's Accessibility Checker where available;
- verify with manual keyboard/screen-reader-aware inspection for high-assurance publication.

Accessibility can conflict with dense internal operational conventions; choose deliberately for the target audience.
