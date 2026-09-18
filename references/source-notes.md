# Source Notes and Research Basis

This skill distills practical guidance rather than reproducing any single framework. Re-check live documentation when behavior is version-sensitive.

Research refresh: 2026-09-18.

## Agent Skills / Codex / prompt engineering

- Agent Skills specification:
  https://agentskills.io/specification
  - progressive disclosure;
  - focused `SKILL.md`, references, scripts, assets.

- OpenAI Skill Creator:
  https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
  - context window is shared;
  - concise core;
  - conditional details in references;
  - deterministic repeated mechanics in scripts;
  - avoid duplication.

- OpenAI — Create skills:
  https://developers.openai.com/docs/build-skills
  - progressive disclosure;
  - skill metadata/context limits;
  - references loaded only when needed.

- OpenAI — Rethinking skills and prompts for GPT-6 Astra:
  https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
  - shorter/discriminating skill descriptions;
  - do not force broad document reads;
  - avoid over-scripted instructions;
  - explicit completion boundaries.

- OpenAI — Codex best practices:
  https://developers.openai.com/guides/best-practices
  - Goal / Context / Constraints / Done;
  - short practical `AGENTS.md`;
  - one coherent outcome per chat;
  - tools added only when useful.

- OpenAI — Prompt engineering:
  https://developers.openai.com/api/docs/guides/prompt-engineering
  - clear prompt sections/delimiters;
  - few-shot when useful;
  - stable reusable content earlier for caching.

- OpenAI — Reasoning best practices:
  https://developers.openai.com/api/docs/guides/reasoning-best-practices
  - direct prompts;
  - avoid unnecessary chain-of-thought prompting;
  - explicit goals/constraints/success criteria.

- OpenAI — Prompt caching:
  https://developers.openai.com/api/docs/guides/prompt-caching
  - stable shared prefix;
  - measure cached-token economics at task level;
  - tool/config changes can alter cache reuse.

- OpenAI — Latency optimization:
  https://developers.openai.com/api/docs/guides/latency-optimization
  - generated output often dominates latency;
  - fewer requests and less unnecessary output;
  - filter huge input context;
  - do not call an LLM by default for deterministic work.

- OpenAI — Cost optimization:
  https://developers.openai.com/api/docs/guides/cost-optimization

- OpenAI — Compaction:
  https://developers.openai.com/api/docs/guides/compaction
  - compact long-lived state rather than indefinitely growing history.

- OpenAI — Agent observability/usage:
  https://developers.openai.com/api/docs/guides/agents-api/observability
  - measure root + subagent calls, input/cached/output/reasoning tokens and task cost.

- OpenAI — Skill evaluations:
  https://developers.openai.com/blog/eval-skills
  - test skill activation and behavior with representative evals.

## Cross-provider context/prompt research

- GitHub Copilot — optimize AI usage:
  https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
  - keep context lean;
  - new conversation for unrelated objectives;
  - compact long sessions;
  - enable only relevant toolsets.

- GitHub Copilot — response customization:
  https://docs.github.com/en/copilot/concepts/prompting/response-customization
  - short always-on instructions;
  - path-specific instructions reduce irrelevant recurring context.

- GitHub Copilot — customization cheat sheet:
  https://docs.github.com/en/copilot/reference/customization-cheat-sheet
  - separate always-on instructions, prompt files, agents, subagents, and skills by purpose.

- Anthropic — prompting best practices:
  https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables
  - long-context document ordering;
  - structured document boundaries;
  - persistent long-horizon state.

- Google Gemini — prompt design:
  https://ai.google.dev/gemini-api/docs/prompting-strategies
  - clear/specific instructions;
  - long context first with task query anchored after it.

- Google Gemini — long context:
  https://ai.google.dev/gemini-api/docs/long-context
  - avoid unnecessary tokens despite large capacity;
  - context caching for repeated large context;
  - longer context can increase latency/cost.

- Google Gemini — context caching:
  https://ai.google.dev/gemini-api/docs/caching

Provider-specific details change. The skill keeps durable principles portable and isolates provider-specific mappings in the harness/docs.

## Spreadsheet practice

- ICAEW, 20 Principles for Good Spreadsheet Practice (2024):
  https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition
- Government Analysis Function accessibility guidance:
  https://analysisfunction.civilservice.gov.uk/policy-store/making-spreadsheets-accessible-a-brief-checklist-of-the-basics/

## Analytical quality

- AQuA Book (2025):
  https://www.gov.uk/guidance/the-aqua-book
- Reproducible Analytical Pipelines:
  https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/

## Data tooling

- pandas merge:
  https://pandas.pydata.org/docs/reference/api/pandas.merge.html
- Polars:
  https://docs.pola.rs/
- RapidFuzz:
  https://rapidfuzz.github.io/RapidFuzz/
- DuckDB:
  https://duckdb.org/docs/

## Excel / Microsoft

- openpyxl:
  https://openpyxl.readthedocs.io/
- XlsxWriter:
  https://xlsxwriter.readthedocs.io/
- Excel AutomationSecurity:
  https://learn.microsoft.com/office/vba/api/excel.application.automationsecurity
- Office Scripts performance:
  https://learn.microsoft.com/office/dev/scripts/develop/web-client-performance
- Power Query security:
  https://learn.microsoft.com/power-query/security-best-practices-power-query

## Google Sheets

- API limits:
  https://developers.google.com/workspace/sheets/api/limits
- API troubleshooting/performance:
  https://developers.google.com/workspace/sheets/api/troubleshoot-api-errors

## Writing and visualization

- Microsoft Writing Style Guide:
  https://learn.microsoft.com/style-guide/scannable-content/
- Datawrapper resources:
  https://www.datawrapper.de/blog/

## Maintenance rule

Prefer authoritative/current documentation for version-sensitive behavior. Keep durable decision principles in the skill and verify exact model/API/library behavior against current docs when it matters. Remove stale prompt/harness rules when newer models no longer benefit from them.
