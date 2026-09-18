# Repository agent instructions

This repository defines the `data-spreadsheet-excellence` Agent Skill.

## Work efficiently

- Read `SKILL.md` first, then only the reference(s) relevant to the requested change.
- Do not bulk-read `references/` or regenerate files that are not part of the task.
- Prefer search/targeted reads before opening large files.
- Keep diffs minimal; do not rewrite unrelated guidance for style.
- Reuse existing terminology and architecture before adding a new concept.
- Put always-needed routing in `SKILL.md`; put conditional detail in `references/`; put deterministic repeatable mechanics in `scripts/`.
- Avoid duplicating the same instruction across `SKILL.md`, `AGENTS.md`, harness files, and references.

## Research

- For version-sensitive AI/model/API/tool behavior, verify current primary documentation before changing guidance.
- Prefer official OpenAI, GitHub, Microsoft, Google, library docs, standards, or other primary sources.
- Record durable source links in `references/source-notes.md`; do not turn the skill into a bibliography.

## Code

- Follow `references/coding-practices.md` when modifying scripts.
- Preserve text identifiers by default in profiling/ingestion utilities unless inference is explicitly requested.
- Do not add production dependencies unless the benefit is clear and documented.
- Keep utilities read-only by default unless mutation is the explicit purpose.

## Verify changes

For instruction-only changes:
- run `python scripts/validate_skill.py`;
- run `python scripts/context_budget.py --check`.

For Python changes also run:
- `python -m py_compile scripts/*.py`;
- targeted functional checks for the changed script.

Do not run broader work only for ritual; broaden validation when risk or blast radius justifies it.

## Completion

A change is complete when:
- the requested behavior/documentation is implemented;
- references from `SKILL.md` resolve;
- validation passes;
- no unrelated files changed;
- version/changelog/docs are updated when the change is release-significant.
