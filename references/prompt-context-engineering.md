# Prompt and Context Engineering

Use this reference when designing prompts, persistent instructions, long-context workflows, or reusable AI configurations.

## 1. Optimize the instruction hierarchy

Put instructions in the narrowest layer that truly needs them.

- **Always-on/project rules:** `AGENTS.md` or equivalent.
- **Task workflow:** skill.
- **Path/language-specific rules:** path-scoped instruction files.
- **One-off objective/context:** user/task prompt.
- **Detailed conditional knowledge:** references.
- **Deterministic repeated mechanics:** scripts/tools.

Do not copy the same rule into every layer.

## 2. A good task prompt

For nontrivial work, the highest-value fields are:

```text
Goal:
Context:
Constraints:
Output:
Done when:
```

Optional only when useful:
- examples;
- non-goals;
- known failure;
- target audience;
- performance/security budget.

More headings are not inherently better.

## 3. Specificity beats length

Prefer:
`Update scripts/profile_tabular.py so identifiers such as 00123 survive default CSV ingestion. Keep --infer-types as opt-in. Add a regression test. Done when the test demonstrates 00123 remains 00123.`

Over:
`Improve the data profiler and make it robust, high quality, production ready, efficient, and safe.`

The first prompt is shorter in ambiguity even if not shorter in characters.

## 4. Define success, not hidden reasoning

Tell the model what must be true at the end.

Good:
- “Preserve leading zeros.”
- “Run the targeted regression test.”
- “Report unmatched count and value.”
- “Do not modify unrelated files.”

Avoid relying on:
- “Think harder.”
- “Think step by step.”
- “Use maximum reasoning.”
- “Be a genius senior expert.”

Reasoning-capable models already reason internally. Externalized chain-of-thought also increases output cost and is not the same as verification.

## 5. Delimit context clearly

Use Markdown sections for human-readable hierarchy.

Use XML-like tags when boundaries between multiple documents or data blocks could be ambiguous, e.g.:

```xml
<source id="policy">
...
</source>
<source id="contract">
...
</source>
```

Do not wrap every sentence in tags.

## 6. Few-shot examples

Use zero-shot first when requirements are clear.

Add examples when:
- classification boundaries are subtle;
- exact output style/format is difficult to describe;
- transformations have edge cases;
- previous outputs repeatedly miss the same pattern.

A few high-quality, diverse examples are usually better than many redundant examples.

Bad examples consume tokens twice: once as context and again by teaching the wrong behavior.

## 7. Stable vs dynamic context

For API/harness design, split:

**Stable prefix**
- durable role/objective;
- security policy;
- tool definitions;
- stable schemas;
- reusable examples/reference.

**Dynamic suffix**
- current user task;
- retrieved documents;
- current file diff;
- tool results;
- new observations.

This improves maintainability and can improve prompt-cache reuse in systems that cache shared prefixes.

Do not distort the prompt merely to chase cache hits; evaluate cost and quality together.

## 8. Long-context ordering

For large document tasks, a robust pattern is:

1. stable instructions;
2. long context/documents;
3. concise task-specific query and output contract near the end.

Provider behavior differs, so benchmark with the target model. Both Anthropic and Google document benefits from placing the query after large context in their long-context guidance.

## 9. Retrieval before stuffing

A large context window is capacity, not a requirement.

Use retrieval/search when:
- only a small part of a corpus matters;
- the corpus changes frequently;
- full context is costly;
- many tools/files exist;
- the task can be solved from a few high-signal sections.

Use full context when:
- global relationships across the entire corpus matter;
- retrieval could omit cross-cutting evidence;
- the corpus is moderate and stable;
- evaluations show quality benefit.

Measure rather than assume.

## 10. Prompt caching

When the API/provider supports prompt caching:
- keep the reusable prefix stable;
- put changing content later;
- avoid reordering tool definitions each request;
- monitor cached-token usage, latency, and task-level cost;
- remember compaction can change the prefix and reduce cache reuse;
- compare total task cost, not only cache-hit percentage.

Do not add useless tokens solely to qualify for a cache threshold unless measured economics justify it.

## 11. Conversation hygiene

Start a new task/thread when the objective changes materially.

Within a long task:
- compact/summarize state when supported;
- carry forward decisions and unresolved items, not raw history;
- avoid repeatedly attaching the same large files;
- remove stale instructions that no longer apply.

Old context is not free: it can increase cost, latency, and instruction conflict.

## 12. Persistent instructions

Always-on instructions must be:
- short;
- repository-specific;
- broadly applicable;
- hard to infer from code alone;
- stable enough to justify repeated inclusion.

Do not put task-specific checklists into `AGENTS.md` just because they are useful once.

When a rule applies only to a path/type, scope it locally.

## 13. Prompt maintenance

Treat prompts/instructions as code:
- version them;
- review diffs;
- test representative cases;
- track regressions;
- remove rules that no longer improve outcomes;
- update after repeated observed failure, not hypothetical fear.

A prompt that only grows eventually becomes a context bug.

## 14. Output contracts

Prefer the lightest output contract that reliably supports downstream use.

Examples:
- prose: 3 concise paragraphs;
- machine use: strict JSON schema;
- review: severity, evidence, impact, fix;
- reconciliation: counts/values/exceptions.

Do not request verbose explanations if the downstream consumer only needs structured fields.

## 15. Negative instructions

Use “do not” rules for concrete failure modes:
- do not overwrite the source workbook;
- do not execute untrusted macros;
- do not drop unmatched records.

Avoid long generic prohibition lists. They consume attention and can cause over-conservative behavior.

## 16. Model portability

Do not bake one model generation's quirks into a universal skill unless required.

Prefer outcome-oriented language:
- “use the lightest reasoning that reliably passes the checks”
rather than
- “always use effort=high”.

Harness-specific adapters can map the generic policy to provider-specific controls.
