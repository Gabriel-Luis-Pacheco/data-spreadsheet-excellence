# Live Codex Eval — Actual Agent Output, Not Just Prompt Checklists

The ordinary GitHub Actions tests generate/edit real XLSX files **using deterministic Python code**, not Codex. Passing CI means the gates and fixtures work; it does **not** show that an LLM obeyed the skill.

To test **the installed skill in a real Codex run** (with the Codex CLI authenticated and the skill installed in the user environment):

1. Create an empty, isolated directory for each run. For example:
   `python scripts/live_eval_fixture.py prepare ./eval-runs/v11-run1`
2. Navigate into that fixture directory, read `prompt.txt` and run it with the installed Codex CLI. In a shell where `codex` is available, a documented invocation is:
   `codex exec --sandbox workspace-write "Use the $data-spreadsheet-excellence skill ..."`
   Pass the **full contents of `prompt.txt`**, not just the abbreviated example above. Keep sandbox restrictions active. Do not enable unrestricted system access for this fixture. The only authorized workbook output is `output.xlsx`.
3. Evaluate the actual output with:
   `python <skill-repo>/scripts/live_eval_fixture.py score ./eval-runs/v11-run1`
4. Record the Codex version, model/reasoning settings, skill commit, command flags, elapsed time, retries, token/cost observations if available, file-gate result, required-value result and any deviations.
5. Repeat on fresh isolated directories. Compare against the v10 baseline with the **same prompt and expected values**, at least three runs per version when affordable, and report error rates/latency without interpreting one lucky pass as reliability.

A passing score checks the **actual artifact**: original sheet/header schema, changed-cell permissions, existing style preservation, status domain and requested values. The evaluator never auto-grants permissions to explain away an agent's structural deviations.

### Critical negative tests

Also have the operator or test harness intentionally produce:
- a new `CONCILIA` field;
- a `QA` or `Parâmetros` tab;
- green conditional formatting on `SIM`;
- `REVISAR` instead of `SIM/NÃO`;
- correct schema but wrong `C2/C3` outcomes.

All must fail the appropriate gate/value assertion. CI contains independent synthetic tests for these.

### What this still does not prove

This fixture is small and does not establish performance on 10,000 real tax transactions, semantic correctness, real Excel PivotTable interactions or safe handling of confidential financial data. Those require additional authorized datasets/environments and human review where consequential. A skill alone cannot guarantee a model invokes a tool; an external orchestrator or pre-delivery approval gate is the strongest enforcement.
