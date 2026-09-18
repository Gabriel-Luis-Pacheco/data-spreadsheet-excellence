# Provider Adapters

The skill is intentionally provider-neutral. Use this file to translate its portable LEAN/BALANCED/DEEP policies into the controls and instruction surfaces available in a specific AI environment.

Do not copy all provider rules into the always-on core.

## OpenAI / Codex / ChatGPT Work

Persistent repository guidance:
- use a concise `AGENTS.md`;
- place local overrides near the relevant directory only when needed.

Reusable workflow:
- use `SKILL.md` + progressive references/scripts.

Reasoning:
- map LEAN/BALANCED/DEEP to the current available reasoning controls after checking current model documentation;
- do not hard-code “always high reasoning”;
- define objective, constraints, output, and done criteria rather than asking for exposed chain-of-thought.

Context:
- use compact/new sessions for unrelated objectives;
- use provider compaction/session-state features when available;
- preserve stable prompt/tool prefixes where prompt caching economics justify it.

API/harness:
- monitor input, cached input, output/reasoning, tool/subagent calls, and task-level success;
- keep tool definitions stable when cache reuse matters;
- use structured outputs only when downstream consumption benefits.

## GitHub Copilot

Repository-wide:
- `.github/copilot-instructions.md` only for broad recurring rules.

Path-specific:
- `.github/instructions/*.instructions.md` for language/folder rules.

Portable agent rules:
- `AGENTS.md` for shared agent expectations.

Efficiency:
- start a new conversation when changing objectives;
- compact long CLI sessions when useful;
- keep only relevant toolsets enabled;
- use skills for task workflows rather than stuffing workflows into repository-wide instructions.

This repository already includes concise Copilot + Python path-specific instructions.

## Claude / Claude Code style harnesses

Do not add a large `CLAUDE.md` merely to duplicate `AGENTS.md`.

If the environment requires a Claude-specific file:
- keep it as a short adapter;
- point to the same canonical project rules;
- put task-specific workflow in the skill;
- keep long reference material out of always-on instructions.

For long document contexts:
- put long source documents/context before the task query;
- clearly delimit documents;
- place the concrete query/output request after the long context;
- keep a compact progress/state artifact across long-horizon work when the harness supports context refresh/compaction.

Use prompt caching only after measuring repeated-prefix economics.

## Gemini / Gemini CLI style harnesses

Avoid duplicating the entire skill into `GEMINI.md`.

If a Gemini-specific instruction file is required:
- keep project invariants concise;
- reuse the skill/reference architecture;
- use long context selectively rather than filling the window because it is available.

For long contexts:
- put large context before the final query;
- use clear anchors/delimiters;
- cache repeated large context where the target Gemini API supports it and economics justify it;
- remember larger context can increase time/cost even when the model supports very large windows.

## Generic API agents

Recommended prompt order:

1. stable developer/system rules;
2. stable tool definitions/schemas;
3. stable reusable examples/reference when genuinely necessary;
4. retrieved/dynamic context;
5. current task and output contract.

Recommended state:

```yaml
objective:
success_criteria:
constraints:
decisions:
inputs_inspected:
artifacts_changed:
checks_completed:
unresolved:
next_action:
```

Do not preserve raw model chain-of-thought. Preserve decisions, evidence, and externally useful rationale.

## Model routing

Do not encode one vendor's product names as universal truth.

Portable mapping:

| Mode | Capability requirement |
| --- | --- |
| LEAN | fast/low-cost model that reliably handles the scoped task |
| BALANCED | general capable model / moderate reasoning |
| DEEP | strongest justified reasoning/capability, especially when ambiguity or risk is material |

Promote after a failed evaluation or clear complexity signal rather than starting every task on the largest model.

## Caching

Across providers, a durable principle is:
- stable repeated content earlier;
- dynamic content later;
- measure actual task-level economics.

Exact cache thresholds, prices, TTLs, eligible models, and API fields are provider/version specific. Re-check current official docs.

## Do not over-adapt

Provider adapters should translate:
- model/reasoning controls;
- persistent-instruction locations;
- compaction/session primitives;
- caching controls;
- toolset configuration.

They should **not** fork the domain logic. Data, Excel, reconciliation, QA, and writing standards remain canonical in the shared skill references.
