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

## Agent security / prompt injection

- OpenAI — Designing AI agents to resist prompt injection:
  https://openai.com/index/designing-agents-to-resist-prompt-injection/
  - external content can contain adversarial instructions;
  - layered defenses are required.

- OpenAI — Understanding prompt injections:
  https://openai.com/safety/prompt-injections/
  - distinguish trusted instructions from attacker-controlled content;
  - defense in depth, monitoring and confirmations.

- OpenAI — Deep research security guidance:
  https://developers.openai.com/api/docs/guides/deep-research
  - prompt injection can arrive through web/file/MCP retrieval;
  - data exfiltration is a key agent risk.

- OpenAI — MCP/connectors security:
  https://developers.openai.com/api/docs/guides/tools-connectors-mcp
  - remote tool content and actions require least privilege and prompt-injection safeguards.

- OpenAI — Computer-use integration:
  https://developers.openai.com/api/docs/guides/tools-computer-use-integration
  - suspicious prompt injection should block/interrupt consequential action;
  - sensitive transmission requires explicit trusted authorization.

- OWASP Top 10 for LLM Applications 2025 — LLM01 Prompt Injection:
  https://owasp.org/www-project-top-10-for-large-language-model-applications/
  - includes indirect injection from external files/web content;
  - RAG/fine-tuning alone do not eliminate the class of risk.

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

## Repository / CI security

- GitHub — Secure use reference:
  https://docs.github.com/en/actions/reference/security/secure-use
  - use least privilege for `GITHUB_TOKEN`;
  - pin actions to full-length commit SHAs for immutable execution.

- GitHub — Managing Actions settings:
  https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - repositories can require full-length SHA pinning.

## Spreadsheet practice

- ICAEW, 20 Principles for Good Spreadsheet Practice (2024):
  https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition
- Government Analysis Function accessibility guidance:
  https://analysisfunction.civilservice.gov.uk/policy-store/making-spreadsheets-accessible-a-brief-checklist-of-the-basics/
- Microsoft — Excel accessibility best practices:
  https://support.microsoft.com/accessibility/excel-accessibility-best-practices-with-excel-spreadsheets
  - simple tables and explicit headers;
  - avoid merged/split cells in data tables;
  - meaningful content/instructions at A1;
  - alt text and Accessibility Checker.

- Microsoft — Excel specifications and limits:
  https://support.microsoft.com/excel/excel-specifications-and-limits
  - 1,048,576 rows × 16,384 columns per worksheet;
  - 15-digit numeric precision.

- Microsoft — Format numbers as text:
  https://support.microsoft.com/excel/format-numbers-as-text
  - digit-only codes/identifiers with 16+ digits should be treated as text when exact preservation matters.

- Microsoft — Date systems in Excel:
  https://support.microsoft.com/excel/date-systems-in-excel
  - Excel supports 1900 and 1904 date systems;
  - the serial systems differ by 1,462 days.

- Microsoft — Change formula recalculation/precision:
  https://support.microsoft.com/excel/change-formula-recalculation-iteration-or-precision-in-excel
  - Excel stores numbers at up to 15 digits of precision;
  - precision-as-displayed can permanently change stored values.

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
