# Coding Practices for AI Agents

The goal is maintainable, reviewable code with the smallest justified blast radius.

## 1. Understand locally before editing globally

Inspect:
- the target file/symbol;
- nearby tests;
- one analogous implementation if helpful;
- direct callers/dependencies only when the change can affect them.

Do not map the entire repository for a small change.

## 2. Prefer minimal diffs

Change only what is required for the requested behavior.

Avoid:
- opportunistic refactors;
- renaming unrelated symbols;
- mass formatting;
- dependency upgrades unrelated to the task;
- rewriting an entire file to change a few lines.

A small diff is easier to reason about, test, review, and revert.

## 3. Follow existing project patterns

Before inventing an abstraction, search for:
- existing helpers;
- naming conventions;
- error types;
- test fixtures;
- logging patterns;
- configuration mechanisms.

Consistency often beats a theoretically “better” local design.

## 4. Explicitness at data boundaries

Validate external inputs:
- schema;
- types;
- nullability;
- ranges;
- encodings/locales;
- identifiers;
- file formats.

Do not silently coerce invalid data into plausible values.

## 5. Functions and modules

Prefer functions with:
- one coherent responsibility;
- explicit inputs/outputs;
- low hidden state;
- names that describe domain intent;
- manageable branching.

Do not split code into tiny functions merely to satisfy a style rule. Do not create classes when a function/data structure is clearer.

## 6. Error handling

Fail loudly on violated invariants.

Catch exceptions only when you can:
- add useful context;
- retry a genuinely transient operation;
- translate to a domain-level error;
- clean up resources.

Avoid broad `except Exception: pass`.

## 7. Comments and documentation

Comments should explain **why**, invariants, non-obvious constraints, or external quirks.

Do not narrate obvious code.

Update docs when:
- user-facing behavior changes;
- workflow/run commands change;
- configuration changes;
- a non-obvious constraint would otherwise be rediscovered.

## 8. Dependencies

Before adding a production dependency:
- check whether standard library/current dependencies suffice;
- evaluate maintenance/security;
- justify size/complexity;
- pin/constrain appropriately for recurring automation.

Do not add a framework for one small helper.

## 9. Tests proportional to risk

For a bug:
1. reproduce with a focused test/fixture;
2. make it pass;
3. run nearby tests;
4. broaden only if blast radius warrants it.

For new behavior:
- test happy path;
- test the important edge/failure case;
- test invariants, not implementation trivia.

Do not run an hour-long suite for a typo unless repository policy requires it.

## 10. Data/Excel tests

Prefer semantic assertions:
- row counts;
- key uniqueness;
- totals;
- sheet/table names;
- formulas/values in critical cells;
- exception counts;
- output reopens;
- preservation of required artifacts.

For visual requirements, use rendering/screenshot/PDF review when possible.

## 11. Performance claims

Do not claim “faster” from intuition alone.

Use:
- representative benchmark;
- elapsed time;
- memory where relevant;
- input size;
- comparable environment.

Optimize algorithm/I/O before micro-optimizing syntax.

## 12. Security

Never embed credentials.

Treat file paths, CSV text, formulas, macros, URLs, queries, and external data as untrusted at boundaries.

Avoid:
- `eval` on input;
- shell command construction from raw strings;
- insecure temp files;
- automatically running workbook macros;
- disabling TLS/security checks for convenience.

## 13. Determinism

For recurring analytics:
- stable ordering where order matters;
- explicit random seeds;
- versioned schemas/config;
- deterministic file naming or run IDs;
- no dependence on current working directory if avoidable.

## 14. Resource lifecycle

Close files, database connections, browser sessions, and Excel/COM processes reliably.

Use context managers/finally blocks where appropriate.

## 15. Review discipline

Before finishing:
- inspect the diff;
- confirm no unrelated changes;
- run targeted checks;
- verify generated artifacts;
- check error messages/logging;
- report what was not tested.

## 16. AI-specific code anti-patterns

Watch for:
- unnecessary abstraction layers;
- duplicate helper functions;
- placeholder TODOs left behind;
- invented APIs/config keys;
- comments explaining every line;
- huge catch-all utility modules;
- mock-heavy tests that do not exercise behavior;
- tests rewritten to match buggy output;
- over-engineered “future-proof” architecture not requested.

## 17. Refactoring trigger

Refactor beyond the immediate change only when:
- current structure blocks a correct solution;
- duplication makes the requested change unsafe;
- tests reveal a coherent abstraction;
- user explicitly requests cleanup/refactor.

State the reason and keep the refactor bounded.
