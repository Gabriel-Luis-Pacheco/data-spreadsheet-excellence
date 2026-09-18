# Copilot repository instructions

- This repository is an Agent Skill; keep `SKILL.md` concise and route conditional detail to `references/`.
- Read only the files relevant to the current change; do not bulk-load all references.
- Keep repository-wide instructions short because they are recurring context.
- Prefer minimal diffs and existing patterns over speculative refactors.
- Follow `AGENTS.md` for repository workflow and verification.
- For Python under `scripts/`, follow the path-specific Python instructions.
- Run `python scripts/validate_skill.py` and `python scripts/context_budget.py --check` after instruction-architecture changes.
- Do not weaken correctness, safety, spreadsheet fidelity, or reconciliation checks merely to save tokens.
