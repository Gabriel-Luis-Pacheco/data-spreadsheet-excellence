# Token, Cost, and Latency Economy

Token economy should be measured at the **task level**: total input + cached input + output/reasoning + tool/subagent calls + retries + latency + quality.

## 1. Highest-value savings

Usually prioritize:

1. avoid unnecessary model calls;
2. reduce unnecessary generated output;
3. prevent repeated context/tool results;
4. expose fewer irrelevant tools;
5. load fewer irrelevant files/references;
6. use deterministic code instead of repeated LLM arithmetic/transforms;
7. choose the smallest model/reasoning level that reliably passes evaluation;
8. use caching/batching where the workload benefits.

Do not spend engineering effort trimming a few input words while the agent makes ten redundant calls.

## 2. Output tokens are expensive in latency

Generated tokens are sequential. Asking for a concise result can materially reduce latency.

Agent behavior:
- do not restate the prompt;
- do not narrate obvious operations;
- do not print large datasets already saved to files;
- return diffs/findings, not whole unchanged documents;
- prefer structured compact summaries for machine consumers.

## 3. Input tokens

Input reduction matters most for large/recurring contexts.

Reduce input by:
- progressive disclosure;
- retrieval/search;
- targeted file ranges;
- concise persistent instructions;
- compaction;
- removing duplicated examples/instructions;
- not bulk-loading tool schemas or MCP servers.

Do not remove context that prevents material errors.

## 4. Stable prefix and cache

Prompt caches typically benefit from stable repeated prefixes.

Keep stable:
- durable developer instructions;
- tool definitions/order;
- stable schemas;
- reusable reference context.

Put dynamic user/retrieval/tool data later.

Provider-specific details differ. Re-check current documentation before hard-coding cache thresholds or pricing.

## 5. Cache economics

A cache hit is not the objective. Lower total cost at equal quality is.

Track:
- total input tokens;
- cached input tokens;
- cache-write tokens if applicable;
- output/reasoning tokens;
- number of model calls;
- number of tool calls;
- elapsed time;
- success/quality score.

A workflow can have a high cache-hit percentage and still be expensive because it repeatedly processes a large conversation.

## 6. Compaction

Use compaction when history becomes large but the task should continue.

A good compact state preserves:
- goal;
- constraints;
- key decisions;
- facts/evidence;
- changed files;
- tests/checks;
- unresolved items;
- next step.

Discard:
- greetings;
- redundant status updates;
- stale hypotheses;
- raw repeated tool output;
- dead-end exploration that no longer affects decisions.

Compaction can reduce cache reuse because the prefix changes. Compare total task economics, not one metric.

## 7. Tool schemas count too

Tool names, descriptions, schemas, instructions, and results all consume context in many agent systems.

Prefer:
- task-relevant toolsets;
- concise tool descriptions;
- server-side filtering/search;
- bounded result sizes;
- structured responses;
- avoiding redundant metadata.

## 8. Model/reasoning routing

Use an adaptive ladder.

**Fast/low reasoning**
- deterministic edits;
- extraction;
- obvious transformations;
- formatting;
- simple code changes with direct tests.

**Standard**
- normal analysis;
- moderate debugging;
- joins/reconciliation;
- workbook generation.

**Deep/high reasoning**
- ambiguous architecture;
- high-risk statistical/financial claims;
- complex debugging;
- conflicting evidence;
- large refactors.

Escalate after evidence of need, not by default.

The exact model/control names are provider-specific.

## 9. Fewer calls vs bigger calls

Batch independent work when:
- inputs are already known;
- outputs can be returned compactly;
- one larger call avoids round-trip overhead.

Split work when:
- a tool result determines the next step;
- context would become noisy;
- independent subtasks can use cheaper models;
- partial failure/retry should be isolated.

## 10. Retrieval economics

For a corpus:
- retrieve top relevant sections;
- deduplicate;
- include source metadata;
- rerank when necessary;
- expand around a hit only when surrounding context matters.

Do not retrieve 20 nearly identical chunks to make the prompt look grounded.

## 11. Code execution beats language-model arithmetic

Use Python/SQL/spreadsheet engines for:
- aggregation;
- joins;
- statistics;
- parsing;
- hashing;
- comparison;
- schema checks.

Use the model for:
- deciding what to compute;
- interpreting outputs;
- selecting tools;
- communicating results.

This both saves tokens and improves determinism.

## 12. Reuse artifacts

If a deterministic step produced:
- a cleaned Parquet file;
- an inventory JSON;
- a schema/profile;
- a rendered image;
- a test result;
reuse it until inputs/code change.

Do not rerun or reread solely from habit.

## 13. Budget telemetry

For agent applications, log per task:
- model;
- reasoning/verbosity setting;
- input/cached/output tokens;
- calls;
- tool calls;
- retries;
- subagent usage;
- wall-clock;
- result/eval score.

Optimize **cost per successful task**, not cost per call.

## 14. Anti-patterns

- “always use the biggest model”
- “always read all references”
- “always produce a detailed plan”
- “always run the full suite”
- “always spawn reviewers/subagents”
- repeating large system instructions inside user prompts
- pasting tool output the model can already access
- asking the model to calculate large tables manually
- generating verbose explanations nobody consumes
- starting a second LLM call to reformat output that could have been structured correctly in the first call
