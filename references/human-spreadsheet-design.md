# Human Spreadsheet Design — Anti-Template / Anti-Slop Contract

Use for **CREATE_NEW**, **DERIVED_REPORT** and **EXPLICIT_REDESIGN** when producing a workbook that a human will open. For **EDIT_EXISTING**, the actual source workbook is the visual authority: use this reference only to diagnose explicitly authorized readability repairs, not to restyle it. See `template-fidelity.md`.

## Principle

Design a useful worksheet, not an AI-generated "professional Excel" skin. A believable human-made workbook has the density, hierarchy and small practical choices of someone who uses it every day. **Professional does not mean colorful.** It may be mostly ordinary Excel cells. Every extra color, band, card, border, title block, chart and tab must earn its place.

Do not try to disguise AI authorship by introducing mistakes. Make correct, restrained work adapted to the actual analyst, industry and recipient.

## 1. Choose a layout archetype before formatting

Decide from content, audience and workflow — never choose a house style first:

| Workbook role | Starting visual approach | Avoid |
| --- | --- | --- |
| Source export / working data | Plain grid, one clear header, practical filters and number formats; mostly neutral cells | "Luxury" colored table themes and executive-style title banners |
| Fiscal/accounting reconciliation | Compact comparable columns, right-aligned amounts, clear period/units, visible exception evidence where authorized | KPI-card dashboard over every reconciliation and red/green status by reflex |
| Human working model | Preserve/localize established cell conventions, clearly distinguish genuinely editable inputs where needed | Decorative themes, extra helper sheets/columns, unexplained formatting |
| Analytical report | A title and concise finding only if useful; structured summaries before detail | Ceremony: `Resumo Executivo`, methodology, source cards, random notes without a reader need |
| Executive dashboard | Deliberate hierarchy, a few decision-relevant metrics and explanatory charts | Default navy header + cyan striped grid, dozens of equally weighted KPI tiles |

If the user supplied a **style exemplar**, analyze its actual visual grammar (density, typography, spacing, header treatment, borders, alignment, highlight frequency). Borrow those conventions only where relevant; do not copy the exemplar's underlying private data. If the supplied file is a **source to edit**, its original formatting stays in place unless the user requested a redesign.

## 2. Default appearance is deliberately unbranded

**No default navy / electric blue / turquoise / purple dashboard palette.** No blue banded rows by default. Neither blue nor banding is forbidden where the user's original workbook genuinely uses them or an explicit design brief calls for them.

For an ordinary NEW operational table with no applicable reference:
- Start with Excel-native-looking typography (Aptos/Calibri or the recipient's established font), approximately 10–11 pt body text.
- Keep cells white/neutral with one subtle header treatment: plain bold labels, or a light neutral fill, or a modest bottom border. Choose one, not all possible decorations.
- Prefer thin, unobtrusive separators where needed; no boxes around every cell or bright outline.
- Reserve strong fill or accent color for *real* grouping, approved branding, exceptions or actionable status.
- Do not introduce huge merged banners, ornamental subtitles, large dead zones, emoji/symbol badges, floating KPI cards, ornamental gradients or auto-created logos into working sheets.
- Do not forcibly create an Excel `Table` solely to obtain a preset stripe style. Create real native Tables if the user needs structured table behavior; pick a minimal compatible table style when presentation is discretionary.
- Use compact human-readable labels. Retain supplied names exactly in existing workbooks. Avoid needless title case, ALL CAPS, English labels in a Portuguese-facing workbook, and AI-sounding generic section titles.
- Keep source data in its proper contiguous machine-readable region: no decorative blank/merged rows interrupting a dataset.

These are a conservative starting point, not a mandatory style preset.

## 3. Usability beats screenshot aesthetics

A visually handsome workbook is a failure when the actual job is harder:
- **Never leave essential headers, accounting descriptions, identifiers or ordinary values visibly clipped** in the delivered first view. Check both typical and long values. Widen appropriately, wrap and increase row height where justified, or deliberately move long narrative to an appropriate existing/authorized location. Do not hide content to keep a pretty narrow layout.
- Size columns according to their real content, not equal-width cards. Abbreviations only if commonplace to the intended team. Do not truncate a header like "Descrição do ajuste".
- Keep amounts numeric, aligned right and shown at meaningful precision. For a Brazilian audience, use localized display (e.g. `2.872,10`, appropriate date format) without turning values into text. Put `R$` in the appropriate header or custom numeric format consistently; avoid duplicated currency decoration.
- Text/description left; amounts/quantities right; codes/identifiers treated as text when leading zeros or precision matter. Identifiers are not measures.
- Use normal working row heights and natural text density; don't make every row tall merely for visual drama.
- Freeze panes and filters only when they improve navigation; avoid hiding important columns to perfect a cropped screenshot.
- Respect the Excel viewport: inspect at least the top-left, the widest descriptions, representative amounts and any exceptions; inspect horizontal scroll and print view when delivery requires printing.
- For real Excel reports verify native functionality alongside layout: styling a range is not the same as creating a functional Table.

## 4. Six anti-slop failure signals

An output needs redesign/repair when any of these apply **in a new or explicitly redesigned artifact**:

1. **Recognizable AI preset:** dark navy full-width headers + saturated light-blue alternating rows, copied across unrelated tasks by default.
2. **Decorative overload:** vivid borders, status palettes, merged title ribbons, unrelated KPIs, charts, cards or legends that provide no decision value.
3. **Clipping and fake neatness:** cropped descriptions, unreadable headers, arbitrary symmetric widths, tiny text or cramped height for the sake of a clean thumbnail.
4. **Template-first information structure:** an ornamental dashboard instead of the compact fiscal/operational table the recipient actually needs.
5. **Agent artifacts:** new `QA`, `Critério`, `Tolerância`, `Parâmetros`, `Resumo`, helper columns or statuses created for the agent's convenience, without authorization.
6. **Cultural/semantic mismatch:** `2,872.10` in a pt-BR finance report, mixed locale, misleading status colors, inconsistent negative values, money as text, or visual emphasis without meaning.

**Scope protection:** None of these signals justify silently recoloring an EXISTING user's workbook. In that mode preserve visual provenance; ask for/act on explicit redesign permission or fix only a truly broken or materially unreadable element when necessary for the task.

## 5. Visual QA acceptance checklist

For a newly created or expressly redesigned workbook, inspect the actual XLSX render/opened workbook, not merely code or a styled preview. Answer all:

- Is this the simplest visual form that accomplishes the task?
- Would an experienced analyst in this domain recognize the layout as practical?
- Did an applicable existing example/template genuinely guide the output?
- Are every header and representative long description readable without accidental truncation?
- Are all numbers truly numeric and formatted for the audience, with consistent precision and negative treatment?
- Is every non-neutral fill/border/conditional format/merged region needed? Remove unjustified visual artifacts.
- Were formula behavior, source structure, and native features preserved or correctly implemented?
- Are the first visible viewport and a dense detail section equally usable?
- Does the sheet contain only recipient-useful content, with no tool/process residue?
- If print/export matters, is the intended width and content complete on paper?

If a material item fails, fix it and render/inspect once more. Do not conclude that a workbook "looks human" from cell styles alone. Use measured example-to-output comparisons, not claims of universal aesthetic superiority.

## 6. Quick sanitized case: adjustment ledger

**Bad generic rendering:** a fiscal listing with navy header, bright-blue zebra rows, US-style `2,872.10`, truncated `Descrição do ajuste`, thin bright outlines and an unrelated adjacent `Efeito` presentation invented solely to look analytical.

**Better for a NEW, simple operational adjustment ledger:** a readable, compact table with exact task-relevant fields, neutral header emphasis, correctly localized values, sensibly wide/wrapped adjustment description, and only meaningful exception highlighting. Whether `Efeito` is present depends on the *actual source contract*, not the designer's taste. A comprehensive reporting job may justify summary sections; a raw adjustment ledger may not.

**Important:** The "bad" image is a negative example of automatic styling, not a claim that every dark-blue table is wrong. A source workbook with that palette remains untouched under EDIT_EXISTING unless a redesign was explicitly authorized.

## 7. Evaluation is artifact-based

Static policy/tests do not establish that a model creates tasteful work. For regressions, produce a real XLSX under each scenario with and without the skill, evaluate independently on: task fit, schema fidelity, content accuracy, native behavior, locale, clipping/readability, restraint, functional navigation and print if relevant. Compare identical prompts/inputs. Use cases in `EVALS.md` and `evals/cases.yaml`; record observed failures rather than promising the skill will always win.
