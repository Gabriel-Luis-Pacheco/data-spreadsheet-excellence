# Agent Harness

`harness.yaml` is a **portable advisory configuration** for agents using this skill.

It separates two controls:

- **execution mode** — LEAN / BALANCED / DEEP, based on technical complexity and ambiguity;
- **assurance tier** — A0 / A1 / A2 / A3, based on consequence and required evidence.

A hosting application, Codex setup, or custom agent can map these concepts into provider-specific model/reasoning, verbosity, toolsets, confirmations, caching, and compaction.

Core ideas:
- progressive context loading;
- minimal relevant tools;
- explicit untrusted-content boundary;
- targeted testing first;
- deterministic scripts for deterministic work;
- evidence strength proportional to consequence;
- token savings never override correctness/security.

Detailed behavior:
- [agent harness](../references/agent-harness.md)
- [assurance model](../references/assurance-model.md)
- [agent security](../references/agent-security.md)
- [provider adapters](../references/provider-adapters.md)
