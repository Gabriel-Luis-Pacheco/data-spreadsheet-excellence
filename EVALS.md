# Evaluation Cases

Use these cases to check whether the skill improves quality **and** efficiency. The skill should not turn simple work into process theater, nor use token savings as an excuse to weaken material validation.

## Eval 1 — messy ERP exports
Prompt: combine monthly CSV exports, clean customer IDs, calculate revenue, create a management workbook.

Expected:
- preserve leading-zero IDs;
- inventory/profile relevant inputs;
- choose pandas/Polars/DuckDB based on scale;
- validate period coverage and control totals;
- separate data and presentation;
- visually QA the workbook.

Failure:
- IDs silently converted to integers;
- dropped rows;
- no totals;
- decorative formatting without hierarchy.

## Eval 2 — dangerous XLSM edit
Prompt: edit a corporate `.xlsm` with openpyxl and save over it.

Expected:
- classify F3 risk;
- inspect macros/links/queries/pivots/objects;
- preserve original;
- avoid claiming openpyxl guarantees fidelity;
- prefer Excel application automation if behavior matters.

## Eval 3 — reconciliation
Prompt: reconcile supplier lists whose names differ.

Expected:
- trusted/deterministic identifiers first;
- key cardinality profile;
- normalized exact/composite rules;
- blocked fuzzy candidates;
- review zone;
- matched/unmatched counts and values;
- exception table and materiality.

Failure:
- all-pairs fuzzy matching;
- universal score threshold;
- match percentage only.

## Eval 4 — analyst review
Prompt: review another analyst's workbook.

Expected:
- distinguish defects from preferences;
- severity classification;
- evidence, impact, resolution criterion;
- check data, method, workbook, visual, and writing.

## Eval 5 — executive dashboard
Prompt: make a workbook beautiful for the board.

Expected:
- understand decision and key metrics;
- simplify rather than decorate;
- hierarchy before color;
- limited primary KPIs;
- trend/context;
- exceptions;
- visual QA.

Failure:
- rainbow colors, merged-title excess, gauges, 3D charts.

## Eval 6 — causal overclaim
Prompt: write that training caused sales because they correlate.

Expected:
- do not overclaim;
- distinguish association from causation;
- identify evidence/design needed.

## Eval 7 — very large data
Prompt: join 300 million Parquet rows and export summary to Excel.

Expected:
- avoid full pandas materialization;
- use DuckDB/Polars/lazy scans;
- aggregate before Excel;
- export decision-useful summary/exceptions, not raw 300m rows.

## Eval 8 — Google Sheets recurring job
Expected:
- batch operations;
- range/field minimization;
- backoff;
- idempotency;
- avoid write races;
- post-write validation.

## Eval 9 — anti-slop writing
Input: “Our robust and comprehensive analysis generated valuable insights...”

Expected:
- replace with specific findings;
- quantify;
- shorten;
- separate fact/interpretation/action.

## Eval 10 — low-risk quick task
Prompt: add a total column to a 40-row CSV.

Expected:
- LEAN mode;
- no formal project-wide plan;
- no bulk reference loading;
- simple safe transform;
- one quick check;
- concise response.

Failure:
- reading every reference;
- spawning reviewers/subagents;
- running unrelated full test suites.

## Eval 11 — context selection
Prompt: modify only the XlsxWriter dashboard formatting.

Expected:
- read `SKILL.md`, visual/spreadsheet reference as needed, and target code;
- do **not** load reconciliation, statistical, security, and every other reference without a reason.

Failure:
- “read all docs first” behavior.

## Eval 12 — adaptive escalation
Prompt: change one formula in a macro-enabled financial model with external links and Power Query.

Expected:
- begin with risk/fidelity classification;
- escalate to DEEP/F3 because workbook behavior is material;
- inventory active features;
- preserve original;
- use target Excel engine where required;
- stronger validation.

Failure:
- stay LEAN merely to save tokens.

## Eval 13 — repeated context
Scenario: the agent has already read a 600-line source file and only a separate test file changes.

Expected:
- retain a compact summary of relevant source behavior;
- do not reread the unchanged 600-line file unless a new uncertainty appears.

Failure:
- reread the same full file after every tool call.

## Eval 14 — prompt quality
Prompt request: design an agent prompt for recurring spreadsheet audits.

Expected:
- Goal / Context / Constraints / Output / Done when;
- stable reusable rules separated from dynamic workbook data;
- few-shot examples only if they solve a real ambiguity;
- no request for exposed chain-of-thought;
- explicit validation criteria.

Failure:
- giant persona prompt filled with generic adjectives.

## Eval 15 — coding discipline
Prompt: fix leading-zero loss in `profile_tabular.py`.

Expected:
- inspect target + relevant regression behavior;
- minimal diff;
- no unrelated refactor or new framework;
- targeted functional test;
- compile script;
- report what changed.

Failure:
- redesign entire repository or add unnecessary dependencies.

## Eval 16 — long-session compaction
Scenario: long-running audit approaches context limit.

Expected compact state:
- objective;
- critical constraints;
- files already inspected;
- decisions/assumptions;
- checks completed;
- unresolved items;
- next step.

Failure:
- preserve raw transcript/tool dumps;
- lose material decisions and reread repository from scratch.

## Eval 17 — tool economy
Prompt: answer a question already resolved by a small local config file.

Expected:
- use targeted file read;
- no web search, subagent, or unrelated MCP tool;
- stop after sufficient evidence.

## Eval 18 — cache-aware API harness
Scenario: an application repeatedly analyzes different workbooks with the same instruction/tool prefix.

Expected:
- keep stable instructions/tool definitions stable and early;
- put workbook-specific/retrieved content later;
- measure cached tokens **and total task cost/quality**;
- do not add useless padding solely to chase cache hits.

## Scoring

Score 0–2 on:
- routing/tool choice;
- data integrity;
- validation;
- risk proportionality;
- context efficiency;
- tool-call efficiency;
- coding/diff discipline where applicable;
- communication;
- usability;
- honesty about limitations.

Target:
- no zero on integrity/validation for medium/high-risk cases;
- no zero on context/tool efficiency for LEAN cases;
- average ≥1.7;
- low-risk cases remain concise.
