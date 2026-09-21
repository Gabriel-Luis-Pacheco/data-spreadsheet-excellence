# Changelog

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
