# Evaluation Strategy

The repository uses two evaluation layers.

## 1. Deterministic CI tests

These test things a normal program can verify exactly:

- skill structure and required files;
- instruction/context budgets;
- Python compilation;
- leading-zero preservation in the profiler;
- workbook inventory behavior;
- workbook before/after diff behavior.

Run:

```bash
python -m unittest discover -s tests -v
```

## 2. Behavioral agent evals

`../EVALS.md` contains scenarios that require an AI agent/harness.

For each run record:

- model/provider/version;
- skill commit SHA;
- execution mode selected;
- assurance tier selected;
- references actually loaded;
- tool calls;
- subagent calls;
- retries;
- input tokens;
- cached input tokens when available;
- output/reasoning tokens when available;
- elapsed time;
- qualitative score by rubric;
- failure notes.

## Comparison principle

Optimize **cost/latency/context per successful task**, not token count in isolation.

A new version is not better merely because it:
- uses fewer tokens;
- has a higher cache-hit ratio;
- makes fewer tool calls;
- answers faster.

It should preserve or improve required quality and safety.

## Suggested experiment design

When comparing two skill/harness versions:

1. use the same eval prompts and fixtures;
2. randomize run order when practical;
3. repeat nondeterministic cases;
4. keep provider/model settings recorded;
5. compare medians, not one lucky run;
6. inspect quality failures, not only averages;
7. stratify by LEAN/BALANCED/DEEP and A0–A3.

## Regression policy

Treat as a regression when:
- integrity/validation score drops on material cases;
- prompt injection causes an unauthorized action;
- a LEAN task begins loading broad irrelevant context;
- A2/A3 tasks lose required evidence;
- workbook preservation failures increase;
- cost/latency rises materially without a quality benefit.

Behavioral eval execution is provider/harness-specific; this repository intentionally does not pretend a static Markdown file can execute model evals by itself.
