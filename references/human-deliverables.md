# Human-Authored Deliverables — Reader-Facing Output Contract

Use this when the user asks an agent to produce **the work they would personally submit**: reports, summaries, spreadsheets, dashboards, slides, client notes, audit findings, emails, or similar artifacts. "Make it like I did it" means use the user's legitimate voice, audience, context, and normal workplace conventions — **not** inventing facts, pretending to be a real person in a conversation, or adding deliberate mistakes.

## 1. Two distinct output surfaces

**A. Reader-facing deliverable:** the finished report/workbook/note that its real audience will read. It should look like competent human work done for that purpose, without exposing the machinery used to generate it.

**B. Internal execution/evidence trail:** scripts, raw input paths, run logs, debug output, rejected files, worker messages, prompts, test outputs, source manifests, checksums, and technical limitations. Preserve this separately when useful or mandatory. An internal trail is not a section of the normal report.

An author-facing handoff in chat may briefly say what was delivered and disclose material blockers. Never paste that handoff verbatim into a reader-facing document unless requested.

## 2. Start from the actual author's conventions

Before drafting, identify:
- audience and purpose: internal quick update, management report, client document, regulatory evidence, or engineering/debugging;
- examples of the user's previous work, existing company template, terminology, language, date/number conventions, and expected length when available;
- what the author would actually name, explain, tabulate, omit, and put in an appendix;
- what needs to be said for a reliable decision.

Infer ordinary formatting only when no example exists. Do not claim to know a personal style without examples. Match complexity and tone to the audience, not to the model's ability to generate elaborate output.

## 3. Internal instructions are NOT automatic deliverable content

**The user telling the agent a rule, tolerance, formula criterion, validation method, coding decision, file-processing constraint, or recurring workplace convention is not permission to display it in the final workbook/report.** Treat that context as an instruction for doing the work, not as a content requirement. Passing an internal decision rule into visible cells because it was mentioned in the prompt is a common and serious failure.

Use a **visibility decision** for every proposed title, worksheet, range, legend, note, control, metric, parameter, and methodology section:

1. **Requested?** Was this explicitly requested as content or as an adjustable user-facing control?
2. **Useful to the recipient?** Does it support a real task, correct interpretation, an actionable exception, or required compliance?
3. **Conventional here?** Would it naturally appear in the supplied example/template and this audience's everyday workflow?
4. **Functionally necessary?** If a formula/query needs the value, can it exist in the formula, a named constant or an unobtrusive support structure rather than taking presentation space?
5. **Necessary disclosure?** Could hiding this information mislead a recipient about scope, classification, material limitations, or a mandatory audit rule?

By default, **only visibly include content that passes a reader-use test or is explicitly required**. Keep internal criteria, calculations, tolerance thresholds, debugging, evidence and technical settings out of view **without deleting the underlying logic, accuracy, or traceability**. Do not reflexively create a `Parâmetros`, `Critérios`, `Metodologia`, `Config`, `QA` or `Execução` sheet, block or section.

Do not assume all business parameters should be hidden: when the intended user must edit a threshold, when the workbook is an explicit analytical model, when a regulatory/audit recipient must see the basis, or when omitting a criterion would be misleading, the parameter/criterion belongs in a deliberately designed, understandable control or explanation. A hidden sheet is not a confidentiality/security mechanism.

### Exact failure from an ordinary reconciliation workbook

The user told the agent: *"We use a tolerance of 0.05 in everyday reconciliation."* The **actual original** workbook uses a `CLASSIFICADO` column with `SIM/NÃO`; `EMBARQUE`, `QTD` and `CONCILIA` were **not present**. First verify the meaning of `CLASSIFICADO`, rather than assuming it means reconciliation.

**Wrong addition:** putting `Tolerância` in F1, `0,05` in G1, and `Critério` in F3 simply because the user mentioned the threshold. It makes a clean operational table look like an AI execution worksheet.

**Correct by default:** preserve actual headers, sheet structure, field meanings, filters and original styles. Apply the tolerance during analysis without inventing `CONCILIA`/`QTD`/`EMBARQUE`. Update `CLASSIFICADO` only when the requested decision matches its established meaning. No unsolicited threshold/criteria blocks or colored statuses.

A real formula may implement the rule **only in an authorized field with the matching business meaning**. Otherwise calculate in memory or in separately authorized output; do not overwrite a different existing classification just because it also uses `SIM/NÃO`. If reused logic needs controlled parameters, prefer internal support over unexplained visible columns. Test correctness, compatibility and auditability. **Never hide material coverage failures, fabricate formula results, or present a static snapshot as a functioning formula.**

If the user instead asks to *change the tolerance inside Excel*, an intentionally visible, labeled input cell may be necessary. This is a different deliverable requirement.

### Visible-minimum principle

When an existing example is supplied, preserve the user's working surface as the default. Add a visible element only if it was requested or passes the recipient-use/accuracy test. Avoid filling empty space beside a report with metadata, definitions, timestamps, detached KPIs, criteria blocks, or explanatory labels to make the workbook look "complete".

**Final cleanup:** inspect visible non-data cells *outside* the intended report/table, every extra sheet, top-of-sheet metadata, notes and print area. Ask of each: "Would this be in the real finished workbook if the person had completed this task?" Remove or relocate anything unjustified, then verify formulas, references, native Excel features, and counts still work.

### Business status labels are also part of the author's original deliverable

For a verified existing status field (e.g. `CLASSIFICADO`) with only `SIM/NÃO`, do not add `REVISAR` merely because the agent could not identify some shipment references. **Also never invent a new `CONCILIA` column.** The user's instruction to ignore strange codes is about matching **scope**, not permission to mark them `NÃO`: an unclassified/ineligible item is not equivalent to a valid group failing its tolerance. Do not add a new category in a cell, pivot filter, extra tab or visual legend. Search alternate authorized key fields first; retain out-of-scope records in source evidence and account for exclusions. See `references/closed-status-reconciliation.md`.

## 4. The reader never needs the orchestration transcript

By default, keep OUT of the reader-facing artifact:
- "Execution report", "Agent run report", "AI-generated analysis", "Technical pipeline", "What the AI did", worker/subagent/model names, prompt descriptions, token/time statistics, and unsolicited testing sections;
- OS paths, temporary directories, stack traces, command names, environment variables, raw TXT/XML/CSV/XLSX filenames or extension-heavy identifiers when a business-friendly source label is enough;
- "File x_y_2026_09_final.txt failed to run", failed intermediate attempts, retries, irrelevant source manifests, empty headings, ceremonial disclaimers, or boilerplate conclusions;
- decorative boxes, aggressive gradients, emoji-heavy sections, gratuitous KPIs/charts, giant headings, and generic executive prose when the user's example is simple.

**Exception:** If the task is explicitly technical, a traceability artifact, audit evidence, or a run log, those details may be the product. For business reports, use a human source label such as "EFD de setembro/2026" rather than a raw filename unless exact file identity is essential to a finding. Source identity and lineage must remain retrievable for reviewers.

Never remove a material failed source, missing period, unresolved exception, uncertainty, or incomplete coverage simply to make a report cleaner. Translate it into reader-relevant language in the main report; move the precise technical evidence to an appendix/exception file/internal manifest as appropriate.

### Existing visual styling is not an invitation to "improve" it

If the user supplies an Excel model, **keep its actual appearance**. Do not introduce conditional green `SIM` fills, red `NÃO` fills, bold status text, extra colors, zebra striping, borders, illustrations, icons or reworked widths merely because those choices look polished to an AI. The original model's visual pattern is authoritative by default. Preserve intentional original formatting, including existing color cues; add colors only when expressly requested or truly required for accessibility or a material user workflow. See `references/template-fidelity.md`.

### Final-file header and sheet audit

Compare the actual source to the final output: any new `EMBARQUE`, `QTD`, `CONCILIA`, other helper column or unrequested sheet is an error even if the values are correct. User-supplied original labels such as `CLASSIFICADO` should be preserved **without changing their meaning**. See `references/source-schema-contract.md`.

## 5. Write the way a competent analyst would

- Use factual, natural, direct prose, appropriate for the author's language (for PT-BR, normal business Portuguese).
- Prefer a short introduction or a single finding over mandatory "Executive Summary", "Methodology", "Execution", and "Conclusion" sections.
- Use only sections that a real reader benefits from. A short comparison may need a title, a table, and two observations.
- State amount, period, basis, exceptions and implications when material; never hide uncertainty.
- Distinguish verified facts from interpretation, estimates and recommended action.
- Use genuine business labels and descriptive filenames for deliverables.
- Design visuals for reading and decision-making, not to look like a synthetic dashboard.
- Do not manufacture "human errors", colloquialisms, fabricated interviews or unverifiable checks to impersonate the author.

## 6. Quick final artifact audit

Imagine the intended author opens the output and forwards it immediately:
1. Would every visible heading, paragraph, chart, and column plausibly belong in that report?
2. Could the audience understand it without seeing prompts, code, error logs, or agent history?
3. Are there any raw filenames, paths, model/worker references, unnecessary "execution" explanations, or generic AI filler? Remove or move to technical evidence unless indispensable.
4. Are material coverage gaps, exceptions, assumptions, and uncertainty still honestly represented?
5. Are title, dates, terminology, number formats, visual density, and file naming consistent with known templates?

If the answer to (1) or (2) is no, revise the deliverable before calling it done. Do not initiate a lengthy redesign loop once these checks pass.

## 7. Before / after examples (PT-BR)

**Poor reader-facing text:**
> Relatório de execução da IA — O arquivo `b040_202609_final_rev2.txt` falhou no parser Python e o worker Haiku refez 3 chamadas. Foram realizadas diversas validações automatizadas.

**Normal analyst-facing text:**
> A conferência de setembro identificou divergências nos registros B040. Parte dos dados não pôde ser validada; por isso, os totais afetados permanecem pendentes de confirmação.

Keep the exact file path, parser error, worker activity, and checks in an internal exception log if they matter for remediation. Do not claim that the source was validated when it was not.

**Poor report heading:** "Relatório de execução da pipeline inteligente e evidências de QA".

**Human alternative:** "Conferência de ICMS — setembro/2026".

**Poor closing:** "A IA entregou uma análise abrangente com insights valiosos."

**Human alternative:** "As diferenças concentram-se em três documentos; recomendo verificar os lançamentos antes do fechamento." (Only if supported by actual evidence.)

## 8. Real spreadsheet features are part of human quality

For Excel, "as if I built it manually" also means a normal user can select a real PivotTable and change its fields; a native Ctrl+T Table expands and filters; actual slicers filter; charts are editable; formulas recompute; requested buttons work when authorized. A static lookalike fails even if its styling is perfect. Automating supported Excel object creation is fully acceptable: the workbook should behave as if a careful analyst created it in Excel. See `references/native-excel-fidelity.md`.

## 9. Exceptions and required disclosure

Some professions, clients, regulations, or task instructions require methods, disclosure of AI use, source file identifiers, detailed exception logs, or approval/signoff. Follow those requirements. This contract **never** authorizes concealing AI use when disclosure is required or claiming independent human review that did not occur.

For A2/A3 evidence, maintain an audit trail; deliver it as a distinct appendix/file or appropriately scoped section, not as gratuitous filler in the ordinary report.
