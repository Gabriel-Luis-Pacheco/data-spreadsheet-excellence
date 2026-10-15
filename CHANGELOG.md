# Changelog

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
