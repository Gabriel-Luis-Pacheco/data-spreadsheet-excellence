# Source Notes and Research Basis

This skill distills practical guidance rather than reproducing any single framework. Re-check live documentation when behavior is version-sensitive.

Research refresh: 2026-09-18.

## Agent Skills / Codex
- Agent Skills specification: https://agentskills.io/specification
  - `SKILL.md` with `name` and `description`
  - progressive disclosure
  - focused `references/`, `scripts/`, and `assets/`
- OpenAI skills repository: https://github.com/openai/skills
  - focused activation descriptions
  - OpenAI UI metadata
  - GitHub-based installation patterns

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

Prefer authoritative/current documentation for version-sensitive behavior. Keep durable decision principles in the skill and verify exact API/library behavior against current docs when it matters.
