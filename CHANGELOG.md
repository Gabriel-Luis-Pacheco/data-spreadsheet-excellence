# Changelog

## 6.0.0 — 2026-09-18 — Efficiency Harness

Major prompt/context engineering and agent-efficiency release.

### Added
- adaptive `LEAN / BALANCED / DEEP` execution modes;
- `references/agent-harness.md`;
- `references/prompt-context-engineering.md`;
- `references/token-economy.md`;
- `references/coding-practices.md`;
- `references/provider-adapters.md` for Codex/OpenAI, Copilot, Claude, Gemini, and generic harness mapping;
- portable `harness/harness.yaml`;
- concise repository `AGENTS.md`;
- GitHub Copilot repository/path-specific instructions;
- `assets/task-prompt-template.md`;
- `scripts/context_budget.py` to detect always-on context creep;
- efficiency-focused evals for context selection, tool economy, coding discipline, compaction, and prompt caching.

### Changed
- `SKILL.md` now treats context/tool/token efficiency as an adaptive execution concern rather than a generic “be concise” rule;
- core instructions now explicitly prohibit bulk-loading references;
- prompt guidance emphasizes Goal / Context / Constraints / Output / Done when;
- reasoning guidance avoids unnecessary exposed chain-of-thought instructions;
- deterministic computation is routed to code/SQL/tools instead of language-model arithmetic;
- CI now enforces core context budgets;
- source notes include current OpenAI, GitHub, Anthropic, and Google prompt/context guidance.

### Design principle
Token savings cannot override correctness, safety, workbook fidelity, or material analytical validation.

## 5.0.0 — 2026-09-18

Major skill architecture and quality release.

### Added
- modular progressive-disclosure references;
- tool-selection, analytical-quality, reconciliation, spreadsheet-engineering, visual-design, automation, security, writing and quality-gate guides;
- patterns/recipes and source notes;
- evaluation suite (`EVALS.md`);
- read-only workbook inventory utility;
- safe-by-default tabular profiler;
- OpenAI/Codex `agents/openai.yaml`;
- reusable delivery, reconciliation and review templates.

### Improved
- stronger activation description in `SKILL.md`;
- explicit F0–F3 workbook fidelity routing;
- null-key and merge-cardinality safeguards;
- deterministic → fuzzy → probabilistic matching ladder;
- safer handling of identifiers and leading zeros;
- accessibility guidance separated from internal workbook conventions;
- formula/recalculation state model;
- security around macros, Power Query, links and formula injection;
- low-risk tasks remain lightweight while high-risk tasks get stronger assurance.

## 4.0.0
Ten-round review release focused on professional analysis, spreadsheet design, data reconciliation, reproducibility, analytical writing, and QA.
