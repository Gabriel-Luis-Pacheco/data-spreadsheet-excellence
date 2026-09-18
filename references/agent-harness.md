# Agent Harness — Efficient High-Quality Operation

This reference defines how an AI agent should execute the skill efficiently. The goal is **quality per unit of context, tool use, latency, and cost** — not minimal tokens at any price.

## 1. First principle: minimize waste, not useful context

Do not optimize by blindly shortening every prompt or skipping validation.

Optimize by removing:
- duplicated instructions;
- irrelevant references;
- repeated file reads;
- repeated tool output;
- unnecessary tool definitions;
- unnecessary subagents;
- verbose status narration;
- speculative work outside scope;
- redundant tests;
- repeated transformations the computer can execute deterministically.

Keep context that changes a decision, prevents a material error, or is required to validate the result.

## 2. Adaptive execution modes

Choose a mode before deep work and escalate only when justified.

### LEAN

Use for:
- small, reversible tasks;
- one-file or one-table edits;
- straightforward formatting;
- simple calculations;
- low-risk requests with clear success criteria.

Behavior:
- no formal plan unless needed;
- load at most the directly relevant reference;
- inspect the target, not the entire project;
- make the smallest correct change;
- run one focused verification;
- answer concisely.

### BALANCED — default

Use for:
- normal analysis;
- moderate spreadsheet automation;
- joins/reconciliation;
- recurring business outputs;
- multi-file edits with clear scope.

Behavior:
- brief plan/state;
- load only 1–3 relevant references initially;
- profile/inspect before material changes;
- use targeted tests plus relevant end-to-end checks;
- preserve a compact decision ledger;
- summarize results, exceptions, and limitations.

### DEEP

Use for:
- financial/regulatory/client-facing work;
- F3 Excel behavior;
- ambiguous or contradictory requirements;
- large migrations/refactors;
- high-value reconciliation;
- complex statistical claims;
- repeated failed validation.

Behavior:
- explicit plan and completion criteria;
- broader evidence gathering, still selective;
- independent validation path;
- stronger provenance and change log;
- targeted second-pass review;
- use subagents only for genuinely separable work;
- do not cap context artificially if additional evidence is necessary.

## 3. Context loading policy

Use progressive disclosure.

1. Read the task and the core skill.
2. Identify the specific unknown that blocks the next decision.
3. Load the smallest reference/file range that resolves that unknown.
4. Act or validate.
5. Load more only if a new material uncertainty appears.

Prefer:
- search/find before full-file reads;
- headings/targeted ranges before whole documents;
- summaries of long tool output;
- a small number of high-signal source files;
- direct primary documentation for version-sensitive behavior.

Avoid:
- loading every reference “just in case”;
- reading the same unchanged file repeatedly;
- chasing references recursively without a blocking reason;
- pasting full files into prompts when the agent can read them from disk;
- carrying unrelated conversation history into a new task.

## 4. Context ledger

For work lasting more than a few steps, keep a compact internal/external working state with only:

- objective;
- success criteria;
- material constraints;
- chosen mode;
- source files/inputs already inspected;
- decisions made and why;
- assumptions;
- unresolved questions;
- validations completed;
- next action.

Do **not** store raw transcripts, full tool outputs, or every intermediate thought.

If the harness supports compaction or context refresh, preserve this ledger and the current artifacts; do not rebuild state by rereading the whole repository.

## 5. Prompt contract

For substantial tasks, convert the request into this minimal contract:

### Goal
What must change or be produced?

### Context
Which files/data/examples are relevant?

### Constraints
What must not change? What standards, fidelity, security, or performance limits matter?

### Output
What artifact or response format is expected?

### Done when
Which observable checks prove completion?

Do not add sections that do not help the task.

## 6. Prompt engineering behavior

Prefer direct outcome-oriented instructions over micromanaged reasoning scripts.

- State the objective and success criteria precisely.
- Use Markdown headings or XML-style delimiters when they clarify boundaries.
- Keep reusable stable instructions separate from dynamic task data.
- Start zero-shot when the expected pattern is obvious.
- Add few-shot examples only when they materially clarify a hard-to-describe format, classification boundary, or transformation.
- Make examples representative and mutually consistent.
- Do not ask reasoning-capable models to expose chain-of-thought or “think step by step”.
- Ask for verification, assumptions, evidence, or a concise rationale instead.
- Prefer positive instructions (“write the output to X”) to long lists of vague prohibitions.
- Use explicit exclusions only for plausible, costly failure modes.

## 7. Tool-use policy

Before each tool call ask: **what decision will this result change?**

Use a tool when it:
- retrieves unavailable evidence;
- executes deterministic computation;
- validates a claim;
- edits/creates an artifact;
- performs an authorized external action.

Do not use a tool merely to appear thorough.

Efficiency rules:
- batch independent reads/searches when supported;
- run dependent calls sequentially;
- prefer one precise query over many broad queries;
- use domain-specific tools instead of generic scraping when available;
- prefer scripts for repeatable mechanics;
- capture only needed output fields/ranges;
- stop searching when the evidence is sufficient for the requested confidence level;
- if two sources disagree materially, resolve the disagreement rather than accumulating more similar sources.

## 8. File-reading policy

For code:
1. locate symbol/file;
2. inspect nearby implementation/tests;
3. inspect dependency/caller only if needed;
4. patch;
5. run targeted tests;
6. broaden tests only when blast radius warrants it.

For data:
1. schema/profile;
2. inspect failing/representative samples;
3. aggregate with code;
4. do not dump huge datasets into model context.

For long documents:
1. search for relevant sections;
2. read contiguous context around matches;
3. summarize;
4. expand only when needed.

## 9. Reuse instead of regeneration

Prefer:
- existing project utilities;
- current templates;
- existing style objects;
- shared validation functions;
- previously computed deterministic artifacts;
- stable schemas/configuration.

Do not regenerate large boilerplate if an existing artifact can be reused or patched.

## 10. Tool definition economy

In custom agent/API harnesses:
- expose only toolsets relevant to the task;
- keep tool names/descriptions precise;
- avoid mounting large MCP servers “just in case”;
- preserve tool definitions/order when prompt caching matters;
- delegate to a specialist tool only when it reduces ambiguity or round trips.

A large irrelevant tool catalog consumes context and can reduce routing quality.

## 11. Subagent economy

Subagents are not free.

Use them when:
- subtasks are independent;
- they need distinct expertise/context;
- parallel exploration has real value;
- isolating noisy research protects the main context.

Avoid them when:
- the root agent can do the task in one or two calls;
- agents would inspect the same files;
- results require expensive reconciliation;
- the task is sequential.

Pass a compact brief to each subagent: objective, relevant context, constraints, expected return format, stop condition.

## 12. Stop conditions

Stop when:
- the requested artifact exists;
- defined quality gates pass;
- material exceptions are disclosed;
- additional search/testing has diminishing expected value;
- remaining uncertainty cannot be resolved with available evidence.

Do not keep iterating merely to use the full context window.

Conversely, do not stop at the first plausible implementation when the task explicitly requires validation/correction.

## 13. Communication economy

Status updates should report:
- a material finding;
- a decision/change of approach;
- a blocker;
- completion of a major phase.

Do not narrate every tool call.

Final answers should prioritize:
1. result;
2. important validation/evidence;
3. material exceptions/limitations;
4. links/files/next action.

Do not repeat the entire methodology unless the user asks.

## 14. Quality floor

Token savings must **never** justify:
- skipping a material reconciliation check;
- overwriting the only source file;
- inventing evidence;
- hiding exceptions;
- skipping required security controls;
- making unsupported causal claims;
- declaring F3 Excel behavior validated without a real compatible engine.

Efficiency is subordinate to correctness and the user's actual goal.
