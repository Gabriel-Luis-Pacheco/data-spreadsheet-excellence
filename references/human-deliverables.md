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

## 3. The reader never needs the orchestration transcript

By default, keep OUT of the reader-facing artifact:
- "Execution report", "Agent run report", "AI-generated analysis", "Technical pipeline", "What the AI did", worker/subagent/model names, prompt descriptions, token/time statistics, and unsolicited testing sections;
- OS paths, temporary directories, stack traces, command names, environment variables, raw TXT/XML/CSV/XLSX filenames or extension-heavy identifiers when a business-friendly source label is enough;
- "File x_y_2026_09_final.txt failed to run", failed intermediate attempts, retries, irrelevant source manifests, empty headings, ceremonial disclaimers, or boilerplate conclusions;
- decorative boxes, aggressive gradients, emoji-heavy sections, gratuitous KPIs/charts, giant headings, and generic executive prose when the user's example is simple.

**Exception:** If the task is explicitly technical, a traceability artifact, audit evidence, or a run log, those details may be the product. For business reports, use a human source label such as "EFD de setembro/2026" rather than a raw filename unless exact file identity is essential to a finding. Source identity and lineage must remain retrievable for reviewers.

Never remove a material failed source, missing period, unresolved exception, uncertainty, or incomplete coverage simply to make a report cleaner. Translate it into reader-relevant language in the main report; move the precise technical evidence to an appendix/exception file/internal manifest as appropriate.

## 4. Write the way a competent analyst would

- Use factual, natural, direct prose, appropriate for the author's language (for PT-BR, normal business Portuguese).
- Prefer a short introduction or a single finding over mandatory "Executive Summary", "Methodology", "Execution", and "Conclusion" sections.
- Use only sections that a real reader benefits from. A short comparison may need a title, a table, and two observations.
- State amount, period, basis, exceptions and implications when material; never hide uncertainty.
- Distinguish verified facts from interpretation, estimates and recommended action.
- Use genuine business labels and descriptive filenames for deliverables.
- Design visuals for reading and decision-making, not to look like a synthetic dashboard.
- Do not manufacture "human errors", colloquialisms, fabricated interviews or unverifiable checks to impersonate the author.

## 5. Quick final artifact audit

Imagine the intended author opens the output and forwards it immediately:
1. Would every visible heading, paragraph, chart, and column plausibly belong in that report?
2. Could the audience understand it without seeing prompts, code, error logs, or agent history?
3. Are there any raw filenames, paths, model/worker references, unnecessary "execution" explanations, or generic AI filler? Remove or move to technical evidence unless indispensable.
4. Are material coverage gaps, exceptions, assumptions, and uncertainty still honestly represented?
5. Are title, dates, terminology, number formats, visual density, and file naming consistent with known templates?

If the answer to (1) or (2) is no, revise the deliverable before calling it done. Do not initiate a lengthy redesign loop once these checks pass.

## 6. Before / after examples (PT-BR)

**Poor reader-facing text:**
> Relatório de execução da IA — O arquivo `b040_202609_final_rev2.txt` falhou no parser Python e o worker Haiku refez 3 chamadas. Foram realizadas diversas validações automatizadas.

**Normal analyst-facing text:**
> A conferência de setembro identificou divergências nos registros B040. Parte dos dados não pôde ser validada; por isso, os totais afetados permanecem pendentes de confirmação.

Keep the exact file path, parser error, worker activity, and checks in an internal exception log if they matter for remediation. Do not claim that the source was validated when it was not.

**Poor report heading:** "Relatório de execução da pipeline inteligente e evidências de QA".

**Human alternative:** "Conferência de ICMS — setembro/2026".

**Poor closing:** "A IA entregou uma análise abrangente com insights valiosos."

**Human alternative:** "As diferenças concentram-se em três documentos; recomendo verificar os lançamentos antes do fechamento." (Only if supported by actual evidence.)

## 7. Real spreadsheet features are part of human quality

For Excel, "as if I built it manually" also means a normal user can select a real PivotTable and change its fields; a native Ctrl+T Table expands and filters; actual slicers filter; charts are editable; formulas recompute; requested buttons work when authorized. A static lookalike fails even if its styling is perfect. Automating supported Excel object creation is fully acceptable: the workbook should behave as if a careful analyst created it in Excel. See `references/native-excel-fidelity.md`.

## 8. Exceptions and required disclosure

Some professions, clients, regulations, or task instructions require methods, disclosure of AI use, source file identifiers, detailed exception logs, or approval/signoff. Follow those requirements. This contract **never** authorizes concealing AI use when disclosure is required or claiming independent human review that did not occur.

For A2/A3 evidence, maintain an audit trail; deliver it as a distinct appendix/file or appropriately scoped section, not as gratuitous filler in the ordinary report.
