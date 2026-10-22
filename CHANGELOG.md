# Changelog

## 11.2.0 — 2026-10-22 — Human Spreadsheet Visual Design & Anti-Template QA

### Added
- `references/human-spreadsheet-design.md`: task-specific visual archetypes, neutral operational defaults, anti-preset warnings, clipping/locale checks and artifact-level visual acceptance.
- Three new behavioral evals for a fresh fiscal ledger, preservation of an existing blue-styled source and an explicitly authorized redesign; corresponding machine-readable eval catalog coverage.

### Changed
- `SKILL.md` now explicitly routes new / derived / authorized redesign work through the human spreadsheet design contract and real workbook visual QA.
- Expanded visual and F2 quality gates to flag clipped descriptions, artificial dark-blue/cyan zebra formatting, excessive decorations and Brazilian-number locale errors.
- Existing workbook style fidelity remains authoritative unless the user explicitly requests or narrowly requires a change.
- Skill validator now checks that the new design reference exists.

### Evidence limits
- This release updates policy and evaluation expectations. Static checks cannot prove future agent aesthetics or guarantee improvement over every no-skill run. Compare actual generated XLSX results under controlled eval prompts before claiming that.



## 11.1.0 — 2026-10-15 — Second-Pass Audit, Gate Closure and Codex Live Eval

### Fixed after critical review
- Closed a high-risk gap in `verify_delivery.py`: formerly an authorized new column skipped all existing-cell inspection on the same sheet. Validation is now insertion-aware and checks original values and styling even with authorized columns.
- Position-specific authorized headers now have targeted positive and negative regression tests.
- Detect unwanted changes to Excel sheet objects, conditional-format definitions, layout metadata, and loss of important native OOXML objects/relationships; static detection still cannot certify Excel UI behavior.
- Fail when an unrequested style is applied to a formerly empty cell outside the original used range.

### Added
- `scripts/live_eval_fixture.py` and `evals/live-codex-evaluation.md`: opt-in isolated workbook fixture, actual Codex output scoring and repeated version-comparison protocol.
- `tests/test_live_eval_fixture.py`: deterministic tests proving scoring rejects a wrong result even when structural checks pass, and rejects a fabricated output column even if result values are right.
- Regression tests for hidden changes elsewhere after a legitimate insertion, changed conditional formats, bad header positions and permitted inserts.

### Limits and next evidence
- CI verifies Python/OOXML checks and generated fixtures; it does NOT call Codex, establish the user's permission for each allowed change, infer business meaning, or prove Excel refresh. Real behavior claims require actual installed Codex runs in an isolated test environment.


## 11.0.0 — 2026-10-15 — Executable Delivery Contract (first improvement pass)

### Added
- `references/delivery-contract.md`: task modes, five universal invariants, trusted change contract, distinct business-vs-native assurance.
- `scripts/verify_delivery.py`: deterministic read-only existing-workbook gate for actual source versus output with explicit permitted cell ranges, headers, sheets, statuses and styles.
- `tests/test_delivery_contract.py`: synthetic XLSX fixtures for original-vs-output edits and known bad outcomes.
- `assets/delivery-contract.example.json`: reusable JSON contract example.

### Improved
- Condensed repeated specific anti-patterns at the top of SKILL.md into a universal contract with specialized references.
- Agent and harness now prioritize actual execution of the gate over merely stating it was validated.
- Separate editing existing workbooks from building a new derived analysis or intentional redesign.

### Boundaries
- This first-pass verifier checks the allowed structural/content/style scope, not actual human authorization, semantics, or target Excel UI behavior. Review and additional validation are still required for higher-assurance work.


## 10.0.0 — 2026-10-15 — Source-Schema Fidelity & Minimal Authorized Edits

### Critical correction
- Found a real contradiction in the earlier skill: examples assumed an AI-created `EMBARQUE | Quantidade | Saldo | CONCILIA` table was the original while the user's **real original** had `CLASSIFICADO` (SIM/NÃO) and lacked `CONCILIA`, `QTD` and `EMBARQUE`.
- The default is now **preserve actual original workbook schema, meanings, status labels, visuals and native behavior**. Derive temporary keys/quantities privately. An existing `CLASSIFICADO` field is not an automatic substitute for a new reconciliation outcome.

### Added
- `references/source-schema-contract.md`: strict original-schema inventory, authorized-edit ladder, distinct output semantics, no implicit columns/tabs, and original-versus-final acceptance gate.
- `scripts/check_workbook_schema.py`: read-only sheet/header inventory diff that flags added, removed, renamed or moved fields and unapproved sheets against the **actual original**, with explicit exemptions for authorized additions.
- `tests/test_schema_contract.py`: regression cases for newly invented `CONCILIA`, `QTD`, `EMBARQUE`, renamed `CLASSIFICADO`, authorized edits and gratuitous extra sheets.
- Five evaluation cases for no-new-column delivery, CLASSIFICADO semantic mismatch, explicitly requested addition, original-vs-prior-AI baseline and real native PivotTable without unauthorized source-header mutations.
- Harness schema policy v9 and validation requirements for dedicated schema/semantic fidelity coverage.

### Revised across the repository
- Reconciliation, spreadsheet engineering, status, template fidelity, native Excel, visual/writing, analytical quality, orchestration, pattern recipes, QA gates, agent defaults and prompt/assets now separate **internal analysis fields from visible user columns**.
- Removed default XlsxWriter guidance that silently encouraged `README`, `Summary`, `Data`, `Exceptions` and `QA` sheets, and removed the status checker default `CONCILIA` column.
- Actual original files take precedence over generic documentation examples or previous AI-generated workbook revisions.

### Assurance/limitations
- CI tests validate guides/scripts, **not** the contents of the user's original workbook, which was not attached here. Header comparison cannot prove semantic correctness or complete Excel F3 functionality. Do not claim a live workbook was fixed or its numbers verified by this release.


## 9.4.0 — 2026-10-15 — Closed Status Contracts & Accurate Reconciliation Scope

### Added
- `references/closed-status-reconciliation.md`: preserves authorized status vocabulary, distinguishes eligible identified evaluated groups from irrelevant/invalid inputs, and prevents treating ignored records as automatically failed.
- `scripts/check_status_values.py` read-only Excel check for exact allowed status labels, unexpected `REVISAR`, blanks and formula caches, with targeted regression tests.
- Four behavioral evals: unrequested REVISAR in SIM/NÃO model, recovery via alternate Atribuição column, ignore-versus-NÃO semantics, and explicitly authorized third status.
- Harness v8 status vocabulary, exclusion traceability and identifier-source coverage policy.

### Improved
- Core skill and reconciliation reference no longer promote internal exception labels or generic `Ambiguous`/`QA` tabs to the user's final workbook.
- Enforce search of relevant shipment ID columns before declaring missing keys; don't invent codes or infer associations from offsetting amounts.
- Audit source-to-eligible/excluded row and monetary totals when material, while keeping recipient-facing reports faithful to existing status/format conventions.

### Integrity rule
A closed set of labels is not permission to misclassify ineligible records. `NÃO` must mean a valid evaluated failure, not a missing or ignored identifier. A result called 'final' needs adequate evidence of key coverage, population and calculations; structural checks alone do not establish semantic correctness.


## 9.3.0 — 2026-10-15 — Original Template Fidelity & Visual Regression QA

### Added
- `references/template-fidelity.md`: a source workbook/screenshot is the default visual specification, not an invitation for AI redesign.
- Behavioral evals for status cells that must remain uncolored, explicitly authorized color changes, and conservative new-workbook design.
- Workbook-diff checks for changed cell visual styles (fills, fonts, borders, alignment) and changed conditional-formatting definitions, including rule changes with the same total count; targeted regression tests cover these cases.

### Improved
- Core skill, human deliverables, visual guide and engineering guidance now expressly prohibit **unsolicited green SIM/red NÃO styling**, colored fonts, borders, new CF rules and other cosmetic extras in existing templates.
- The original light-blue header, normal cell styles, layout, filters and presentation are preserved by default while the requested calculations and real Excel features are implemented.
- Harness v7 and evaluation coverage codify visual minimal-diff behavior.

### Limits
- Structural style hashes are **review signals**, not pixel-perfect Excel-renderer tests or proof a change was unauthorized; baseline screenshots cannot reveal all hidden styles/objects. Requested or necessary functional/accessibility/legal style changes remain permitted. Do not sacrifice correct calculations or native features to preserve looks.


## 9.2.0 — 2026-10-15 — Reader-First Workbook Surface

### Added
- A strict contract distinguishing **what the user tells the agent to do** (tolerances, reconciliation rules, methodology, QA, workplace conventions) from **what the finished workbook should visibly contain**.
- A concrete anti-pattern derived from a real reconciliation screenshot: `EMBARQUE | Quantidade | Saldo | CONCILIA` should not gain a detached `Tolerância 0,05` / `Critério` block merely because the user communicated the working rule.
- A final used-range / visible-sheets sweep for stray parameters, metadata, labels, unnecessary controls and orphan notes.
- Three behavioral evaluation cases: non-visible operational tolerance, explicitly user-editable tolerance, and mandatory threshold disclosure; harness and eval coverage updated.

### Improved
- Human-deliverables guide and Excel engineering default to the **recipient's actual working layout**. Internal calculation/verification is preserved without automatically creating `QA`, `Parâmetros`, `README` or methodology sheets.
- Visual design and QA prioritize removing unsolicited outside-the-table information before purely cosmetic polish.
- Agent default prompt explicitly refuses to turn internal operational context into visible workbook annotations.

### Limits
- Minimalism cannot hide a material decision rule when the recipient must understand it, an explicitly adjustable setting, incomplete coverage, or mandatory audit documentation. The skill improves behavior through guidance/evals and must still be used and verified on actual workbook tasks.


## 9.1.0 — 2026-10-15 — Native Excel Feature Authenticity

### Added
- `references/native-excel-fidelity.md`: a non-negotiable contract requiring the **actual editable Excel object** (especially PivotTable/PivotCache), not a static or visually convincing imitation.
- Native feature acceptance matrix for real PivotTables, Excel Tables (Ctrl+T), slicers, charts, formulas, data validation, conditional formatting, Power Query/connections and controls.
- `scripts/inspect_native_excel.py`: read-only OOXML parts/relationships inventory with `--require pivot_table`, `--require excel_table` and other preliminary object checks.
- Focused structural-inventory tests and behavioral evals for real PivotTables, Tables and unavailable native Excel authoring.

### Improved
- `SKILL.md`, spreadsheet engineering, tool selection, compatibility, human deliverables, provider adapters and quality gates now prioritize actual normal Excel interactions, refresh and source relationships.
- Harness v5 and validators encode native-feature requirements without mistaking package-level detection for full Excel F3 verification.
- Tool choice must match the requested native feature; no substitution by `pandas.pivot_table()`, styled ranges or screenshots without honest disclosure and user acceptance.

### Integrity rule
Automating native object creation is acceptable. A ZIP/package inspection is preliminary evidence, not proof of working native Excel behavior. If a real feature cannot be created or verified in the available environment, disclose the limitation rather than falsely claim full functionality.


## 9.0.0 — 2026-10-15 — Human-First Analyst Delivery & Parallel Assurance

### Added
- `references/human-deliverables.md`: distinguish finished client/management reports from AI execution traces, raw technical filenames and logs; preserve honest disclosure of material source failures.
- `references/analyst-workflow-orchestration.md`: proactive search for all distinct material context, templates and rules; bounded delegation to available subagents/workers; parallel scheduling and minimal risk-covering tests.
- machine-readable harness controls for author-style delivery, context discovery, bounded delegation, critical-path parallelism and non-ritual QA.
- agent behavior evaluations covering reader-facing output, missing sources, parallel research and fast low-risk tasks.

### Improved
- skill core now routes material analyst tasks to contextual investigation and reader-ready human deliverables without turning routine tasks into research projects.
- agent/provider guidance clarifies that Codex/Claude worker names are runtime dependent; this skill does not grant missing delegation capabilities.
- writing, handoff and QA gates distinguish evidence retained internally from what belongs in a business report.
- README and prompt template explain style, audience and source-example discovery.

### Integrity rule
Human-looking output must never fabricate validation or conceal unresolved material differences, missing sources, mandatory AI disclosure, or audit evidence.


## 8.0.0 — 2026-09-21 — Measurable Quality & Data Observability

Audit-driven release focused on gaps between strong written guidance and executable evidence.

### Added
- machine-readable behavioral eval catalog in `evals/cases.yaml`;
- `scripts/validate_evals.py` with activation/mode/assurance/coverage checks;
- `scripts/export_evals.py` for JSONL integration with external model-eval harnesses;
- `references/data-contracts-observability.md` for schema, semantic, unit, domain, freshness, volume and definition drift;
- `references/excel-compatibility.md` for Excel-version portability, dynamic arrays, 15-digit precision, date systems, worksheet limits and legacy-format risk;
- `scripts/tabular_diff.py` for privacy-conscious before/after semantic data comparison, including explicit comparison-completeness and schema/order/type drift;
- `assets/evidence-manifest-template.yaml` and `scripts/validate_evidence.py` for A2/A3 traceability;
- regression tests for tabular diff privacy/ambiguous keys, eval export, and evidence-manifest validation.

### Improved
- recurring pipelines now distinguish one-run validation from longitudinal observability/drift;
- workbook QA explicitly considers recipient Excel version/channel, not only authoring environment;
- CI validates eval coverage and evidence-manifest structure;
- runtime dependencies now include PyYAML because bundled YAML utilities require it;
- harness v3 includes recurring-data, compatibility and evidence policies;
- quality gates include freshness/drift, cross-version compatibility and evidence-package checks.

### Why this release matters
v7 strengthened trust and assurance. v8 makes more of that assurance **measurable and portable**: datasets can be compared semantically, recurring sources can drift without silently passing, eval coverage is machine-checkable, and material runs can leave a structured evidence trail.

## 7.0.0 — 2026-09-18 — Assurance & Agent Security

Deep audit/reliability release focused on gaps that were not adequately enforced by v6.

### Added
- independent `A0 / A1 / A2 / A3` assurance tiers, separate from LEAN/BALANCED/DEEP execution complexity;
- `references/assurance-model.md`;
- `references/agent-security.md` for indirect prompt injection, trust boundaries, exfiltration and consequential actions;
- `SECURITY.md`;
- canonical `VERSION` file and version-consistency validation;
- `scripts/workbook_diff.py` for before/after semantic workbook QA;
- executable regression tests in `tests/test_utilities.py`;
- `scripts/validate_harness.py` for machine-readable harness/OpenAI metadata validation;
- `requirements-ci.txt` and dependency-aware GitHub Actions testing;
- `assets/metric-contract-template.md`;
- `assets/agent-state-template.yaml`;
- `assets/data-dictionary-template.md` and `scripts/file_manifest.py` for schema/provenance handoff;
- `evals/README.md` with telemetry/comparison methodology;
- accessibility details including A1/table structure/alt-text checks;
- locale-aware delivery guidance and Excel size/precision/date-system safeguards;
- hardened GitHub Actions: least-privilege token permissions, immutable current-major action SHAs, non-persistent checkout credentials, stale-run cancellation, exact CI dependency locks, and Dependabot monitoring.

### Improved
- `SKILL.md` now separates execution depth from evidence strength;
- untrusted workbook/document/web/tool content is explicitly data, not authority;
- workbook inventory now surfaces comments, hyperlinks, hidden sheets, external links and macro-container hints;
- tabular profiler now reports formula-like text for review without unsafe blanket sanitization;
- quality gates now start with a trust/security gate and map to assurance tiers;
- CI now runs functional behavior tests instead of only compiling scripts;
- agent/Copilot instructions now include trust boundaries and executable test commands;
- false activation boundary clarified for unrelated generic coding tasks;
- workbook diff now checks defined-name targets, calculation settings, external-link count, VBA-container presence, comments, hyperlinks, and number-format changes;
- CI includes a no-change workbook regression test to reduce false-positive risk;
- profiler safe mode now preserves literal NA-like text, separates blanks from nulls, and hides real top values unless explicitly requested;
- recurring analysis guidance now covers schema/definition drift.

### Why this release matters
v6 optimized how much the agent reads and does. v7 adds stronger guarantees about **what evidence is required** and **which content the agent is allowed to trust**.

Token savings never justify weaker assurance or unsafe actions.

## 6.0.0 — 2026-09-18 — Efficiency Harness

Major prompt/context engineering and agent-efficiency release.

### Added
- adaptive `LEAN / BALANCED / DEEP` execution modes;
- prompt/context/token/coding references and provider adapters;
- portable harness;
- concise `AGENTS.md`;
- Copilot instructions;
- context budget CI;
- efficiency-focused evals.

### Design principle
Token savings cannot override correctness, safety, workbook fidelity, or material analytical validation.

## 5.0.0 — 2026-09-18

Major modular skill architecture and quality release.

## 4.0.0

Ten-round review release focused on professional analysis, spreadsheet design, data reconciliation, reproducibility, analytical writing, and QA.
