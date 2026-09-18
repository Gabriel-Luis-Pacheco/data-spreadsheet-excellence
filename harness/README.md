# Agent Harness

`harness.yaml` is a **portable advisory configuration** for agents using this skill.

It does not magically configure every model. A hosting application, Codex setup, or custom agent can translate its concepts into provider-specific controls such as model selection, reasoning effort, verbosity, toolsets, caching, and compaction.

Core ideas:
- adaptive LEAN / BALANCED / DEEP execution;
- progressive context loading;
- minimal relevant tools;
- targeted testing first;
- deterministic scripts for deterministic work;
- quality floor that token savings cannot override.

Detailed behavior: [../references/agent-harness.md](../references/agent-harness.md)
