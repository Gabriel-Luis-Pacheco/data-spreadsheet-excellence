# Human Writing for Data Deliverables — Editorial Contract

Use for **reader-facing prose** in spreadsheets, fiscal/accounting reports, management notes, dashboards, chart annotations, business emails, and analytical summaries. This is a writer/editor workflow, not an authorship detector. Follow the original workbook's schema and established labels. Apply these checks to text the agent **writes**, never automatically to imported source records, user quotations, fixed legal or regulatory phrases.

## 1. Decide what actually needs writing

Not every spreadsheet needs prose. An existing numeric reconciliation may be complete without a new Resumo, Metodologia, Conclusão, explanatory note or a tab of recommendations. Do not add cells, comments, headings, tabs or summaries just to display writing skill.

Identify the intended reader, required decision, medium, language/register, available author samples, actual business vocabulary and minimum necessary length. Never pretend to know someone's personal voice without an example. Never invent facts, quotes, names, numbers, personal experiences, viewpoints or emotions merely to sound human.

## 2. Voice follows the work, not a global preset

- **Fiscal/working Excel:** ordinary concise Portuguese; accepted terminology and accurate labels. Example: “Diferença de ICMS”, not “Insight estratégico sobre o cenário tributário”.
- **Management/audit report:** precise and evidence-led; lead with the actual finding and scope. Include exposure, uncertainty and next check only when justified.
- **Technical evidence/formal regulatory:** exact and restrained; source identity, standard terminology and necessary repetition may be essential. Do not rewrite away mandatory formulas, accounting terms or caveats.
- **Informal message:** match genuinely observable voice and audience conventions. Never force slang, humor, dramatic punchlines or first person.
- **Executive/external report:** useful takeaway first, then support and required decision, without unsubstantiated claims of excellence or transformation.

Preference hierarchy: user sample > applicable organization example > audience-appropriate neutral voice. Protect intentional terms, punctuation, structure and idiosyncrasies. The minimum effective edit normally beats rewriting a good passage from scratch.

## 3. Draft from evidence, not decoration

Use this *privately*, not as printed headings inside the output:

1. Evidence ledger: checked facts, units, period, denominator, status meaning, relevant source, material exceptions and unresolved matters.
2. Reader's question: what will this sentence help them know, decide or do? A short report may need only one finding.
3. Draft: favor concrete nouns and natural verbs. Make the point early. Write at a register and detail level the reader would actually use.
4. Edit: remove anything that repeats the prompt, congratulates the process, reiterates the heading, explains the model's tools, or pads the document with ritual sections.
5. Validate: cross-check numbers, signs, dates, labels, source coverage, formula meaning and material caveats. Editing can never change the evidence.

Keep **fact / interpretation / hypothesis / estimate / recommendation** separate. Do not invent a recommendation when the task is merely to prepare a cleaned data table.

## 4. Signs to evaluate; not arbitrary hard bans

Consider removing or rewriting the following **when they contribute no meaning**:

- Generic inflation: “análise robusta e abrangente”, “insights valiosos”, “pilar fundamental”, “solução inovadora”, “oportunidade estratégica”, “alto impacto” without a measurable basis.
- Empty framing: “Neste relatório abordaremos”, “É importante destacar que”, “Cabe ressaltar”, “No atual cenário”, “Diante do exposto”, “Em conclusão”. If deleting it does not change meaning, delete it.
- Repeated academic/AI connectors: “Ademais”, “Além disso”, “Nesse sentido”, “Vale salientar” in every paragraph, particularly where no real relation is signaled.
- Artificial symmetry: unearned three-item lists, balanced contrasts for obvious facts, “não apenas X, mas também Y” with no meaningful comparison, a polished generic concluding sentence after every block.
- Flat rhythm: identical paragraphs and sentences, repeated staccato mini-sentences, excessive rhetorical dashes, excessive bold labels and list bullets where a sentence would work.
- Spreadsheet/report furniture: unsolicited Objetivo/Metodologia/Resultados/Conclusão sections, big status banners, a QA narrative, data-process explanations or duplicate commentary about obvious fields.
- Unverified authority: fabricated percentages, uplift, causes, citations, testimonials, “100% validado”, or false assurances about checks that did not occur.
- Domain translation errors: explaining normal NF-e / CST / CFOP labels to a specialist or changing technical column meanings in a hunt for more elegant prose.

**No blanket word bans.** A legal report may require formal wording. A deliberate dash is legitimate. Do not impose sentence-length quotas, artificial burstiness, “zero em-dash”, random unusual words, jokes or typos to manipulate detectors. The question is whether each choice improves clarity and truth for the intended reader.

## 5. Let the structure earn its place

- For existing Excel models keep field labels, tab names, status vocabularies and explanatory text unless change is authorized. Existing styles are part of the source contract.
- A new workbook's title should name actual work, only where a title is needed; no obligatory “executive dashboard” wrapper.
- Headings identify sections that readers actually navigate. A two-sentence finding does not need four titled sections.
- Lists are for genuinely parallel items, not a compulsory three-point pattern. Use paragraphs for connected arguments and tables for comparable measures.
- Chart notes should tie to an actual change, period or exception, not a slogan.
- Match familiar Portuguese dates, amounts and acronyms while preserving numeric data types and exact technical syntax.
- Do not write literal Markdown asterisks, hashes or backtick markers into normal Excel cell text.
- The correct length is **the shortest that retains material meaning and safe interpretation**. Cutting a meaningful limitation is not concision.

## 6. Internal instructions do not become workbook prose

Matching tolerances, parsing steps, formulas, test results, prompts, file paths, workers, and agent status are **execution context** unless asked for or needed by the recipient. Do not create report sections or Excel cells for them by default. No automatic “Método aplicado”, “Critérios técnicos”, “Relatório da IA”, “Resumo de QA” or “Processo de validação”.

A material excluded dataset, inability to verify a required check, missing source period or ambiguous identifier must still be disclosed in the appropriate recipient-facing language. Keep technical provenance separately where useful or required. Mandatory audit disclosures override the desire for minimalism.

## 7. Specific before/after cases (PT-BR)

**Poor:**
> Por meio de uma abordagem robusta e abrangente, foi possível obter insights relevantes sobre as divergências e oportunidades de melhoria no processo de conciliação fiscal.

**Better, only when facts support it:**
> A conciliação identificou divergências. Os documentos afetados foram separados para conferência.

If actual counts and monetary impact are available, state them. Do not invent them just to make the writing specific.

**Poor:**
> Foram utilizados recursos tecnológicos de última geração, garantindo máxima confiabilidade dos resultados.

**Better, if this information matters:**
> Base: EFD ICMS/IPI de setembro de 2026. Os registros sem identificação suficiente não entraram na comparação.

Only mention September or missing identifiers if verified; otherwise adapt to actual sources. Do not promise reliability that was not checked.

**Poor:**
> Em conclusão, os resultados demonstram a importância de uma gestão eficiente, fornecendo dados estratégicos para decisões assertivas.

**Better:** remove the conclusion. If there is a real decision, say which difference to verify and what is at stake.

**Bad workbook structure:** an unsolicited Metodologia e QA sheet listing prompts and automatic process logs. **Better:** retain this information as separate technical evidence when needed; deliver only the fields/reports the user requested.

## 8. Lightweight recipient-text acceptance

Check **written output**, not inherited data:

- Grounding: every factual claim is backed by actual data; unknowns are calibrated, not fabricated.
- Fidelity: figures, dates, signs, technical terms, mandatory text, status meaning and limitations survive editing.
- Reader-use: each added word, cell, section and tab helps actual interpretation or requested use.
- Voice: follows user sample/organization/audience instead of generic promotional prose.
- Rhythm: obvious repeated sentence and paragraph shapes are edited, without compulsory numeric targets.
- Brevity: remove duplicative headings, self-praise, process narration and ceremonial conclusions.
- Medium: spreadsheet cells contain normal cell text, not Markdown or chat syntax.
- Compliance: legal/regulatory/AI disclosure and necessary uncertainty are not concealed.
- Stop rule: if it already reads well and serves the audience, leave it alone.

For an explicit **audit**, cite concrete text spans, explain risk and propose the smallest effective fix. Do not guess whether a human or an AI wrote it. For an explicit **rewrite**, deliver the actual revised text, not a lengthy scorecard unless requested. For ordinary spreadsheet creation, apply the editing silently; never add an AI-slop score tab.

## 9. Cost-conscious execution

LEAN: one silent pass for short text + fact check. BALANCED: drafting and a focused editorial/factual check for substantive text. DEEP/A2–A3: independent review only when risk justifies it. Do not load every source or spawn editors for a one-cell change.

Use references/writing-review-handoff.md for analytical facts, references/human-deliverables.md for visible-content discipline, and references/writing-skill-comparison.md for provenance when maintaining this rule set only (not during ordinary spreadsheet work).
