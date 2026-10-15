# Closed-World Status Contracts and Reconciliation Eligibility

## Rule: status values are governed by the user's workflow, not by an AI's taxonomy

If the supplied workbook or task establishes a **closed set of status values**, use **only** those values, spelled exactly as the recipient expects. For a `CONCILIA` column defined as `SIM` and `NÃO`, **never introduce** `REVISAR`, `PENDENTE`, `INDEFINIDO`, `ERRO`, `N/A`, `OUTRO` or a synonymous color/emoji code in that column, unless the user explicitly revises the contract.

Do not copy internal exception categories from audit methodology into recipient-facing status fields, sheets, pivot filters, legends, formula outputs, chart labels, or new columns. Inherited legitimate values in the original source are data, not permission to invent new classifications.

**This applies beyond reconciliation**: authorized company labels, spreadsheet data-validation values, financial categories, client-facing verdicts, workflow states, document classifications and business codes are closed unless explicitly made extensible.

## Separate three different decisions before calculation

1. **Eligibility** — Is this record in scope for the requested reconciliation? A valid shipment/embarque identifier in an authorized field and other documented criteria may be prerequisites.
2. **Association** — Which legitimate shipment/group does an eligible record belong to? An alternative-looking reference, similar amount, matching invoice or opposite amount is not by itself proof of identity.
3. **Outcome** — For a sufficiently identified and eligible group, do the validated amounts meet the specified tolerance or business conditions?

These are **not interchangeable**:
- `SIM`: only an eligible, properly identified group that meets the actual reconciliation rule.
- `NÃO`: only an eligible, properly identified group that has been evaluated and does **not** meet that rule.
- **Invalid/irrelevant/unidentified identifier:** *not classified as either verdict* unless a **trusted, explicit business rule** defines its treatment.

Do not force a third-state record into `NÃO` merely because the display accepts only `SIM/NÃO`. A two-value contract does not magically make every source line eligible. Also do not turn unmatched or missing evidence into `SIM` because sums cancel.

## "Ignore" means exclude from the relevant operation, not falsify status

If the user says, for example, *"referências estranhas que não são códigos de embarque, ignora; não cria outro status"*, apply the instruction to the **matching/aggregation/classification scope**:
- Do not treat `LT063/14`, `AMOSTRA`, an AWB code, arbitrary numeric identifier, or invoice note as a valid shipment code merely because it appears in a text field; accept **only** codes meeting the **actual authorized identifier contract**. Do not assume a particular prefix/pattern without evidence.
- Do not assign those records to an invented shipment or a guessed matching group.
- Do not create `REVISAR` or quietly label them `NÃO`.
- Exclude **out-of-scope** records from the reconciliation classification/aggregates when the user authorized ignoring them. **Preserve raw source rows** unless removal is explicitly requested; record a compact internal excluded-count/value reconciliation to prevent silent financial disappearance.
- If the final sheet should contain only eligible classified rows, show only those results **when filtering/excluding is authorized**. If source rows must remain visible, retain them without fabricating a verdict (blank as genuinely unclassified if compatible with the existing layout), or use an existing user-approved presentation convention. A blank is **not** a third status, but must not be misrepresented as a completed classification.
- If the requested presentation makes truthful disclosure impossible, do not misrepresent the data to fill every cell. Explain the material remaining limitation in the short handoff, not through an unsolicited workbook category.

**Critical:** "Ignore" does not automatically mean delete raw accounting records, silently drop their monetary values, or override statutory completeness. Where financial/regulatory consequences are material, reconcile source-to-included/excluded counts and totals and preserve reviewable evidence separately.

## Search the full eligible key chain before declaring missing

For legitimate shipment identifiers, inventory likely source columns and aliases (e.g., `Embarque`, `Atribuição`, `Referência`, `Histórico`, or other observed fields), prior working formulas, actual source patterns, and cross-sheet relationships. Do **not** assume these exact columns or their priority exists in every dataset. Establish the rule using samples, source examples and user-approved constraints.

For each record, search prioritized authorized fields; validate any candidate against the **actual code format and source relationship**, not a substring that merely resembles a shipment. Investigate collisions/conflicts before choosing a key. One line containing a note or an invoice number is not evidence of a shipment.

Before reporting "unidentified" rows or marking work complete, do a targeted coverage audit:
- valid shipment key located by which field;
- eligible records and groups, identified vs unresolved;
- out-of-scope ignored records and monetary values;
- conflicting identifiers or duplicate group memberships;
- totals by B010/B040 or requested dimension;
- real outcome count `SIM/NÃO` and the same population's control totals;
- formulas, pivots, filters and layout still represent only the intended population.

If 36 records were "not found" but 16 had a valid key in `Atribuição`, the original "36 missing" count was **premature**, not a final confirmed result. Fix the extraction criteria, rerun affected checks, then report counts consistent with the actual source and scope. Do not declare success solely because a workbook opens or PivotTables refresh.

## Internal exceptions versus final presentation

You may classify excluded, malformed, ambiguous or unidentified inputs **internally** for QA/audit. These classifications must not leak into a closed user-facing status field unless authorized. A separate technical log is optional, proportionate to risk, and not an automatic visible `Revisar` worksheet.

If exact excluded rows must be communicated to the user to avoid a misleading financial result, give a **short, business-readable** note in the handoff; keep technical row references and detailed evidence separately when needed. Never claim "everything reconciled" when exclusions affect coverage.

## Minimal acceptance checks

- **Allowed-value check:** every populated final `CONCILIA` result belongs to the exact permitted vocabulary.
- **Meaning check:** sample `NÃO` rows and confirm they are valid identified groups failing the rule, *not* merely missing/ignored references.
- **Eligibility check:** excluded/ignored row population is separate from evaluated `SIM/NÃO`; source-to-result count/value bridge where material.
- **Source completeness:** relevant key-bearing columns were examined; no easily recoverable identifiers remain "missing".
- **Invariant:** no newly invented shipment IDs, no duplicate group assignments without a valid rule, no changed B010/B040 totals from uncontrolled dropping or merging.
- **Human-facing QA:** no extra `REVISAR` labels/pivots/color legends or visible exception panels were added to the user's supplied template.

Use fast deterministic validations, not an elaborate testing ritual. If a source/Excel engine is unavailable, state precisely what was and was not checked.

## Examples of correct and incorrect reactions (PT-BR)

**User:** "Essas referências diferentes, que não são código de embarque, ignora. Não cria outro status além de SIM/NÃO."

**Incorrect:** "Retirei REVISAR e transformei os 20 registros em NÃO." This wrongly treats absence of a valid shipment as a failed reconciliation.

**Correct behavior:** "Desconsiderei as referências fora do padrão na identificação dos embarques, sem incluí-las nos grupos conciliados nem criar um terceiro status. Mantive os lançamentos originais e conferi a quantidade e os valores excluídos da apuração. Na coluna CONCILIA, preservei somente os resultados legítimos SIM/NÃO." Say this only after actually executing and verifying those steps; do not invent findings or counts.

**User explicitly changes the contract:** "Inclui também PENDENTE para embarques identificados, mas com documento faltante."

**Correct behavior:** explicitly update the authorized state set and the rule that triggers `PENDENTE`; ensure formulas, validations, native pivots, downstream reports, and tests stay consistent. No other states are authorized.
