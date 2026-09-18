# Patterns and Recipes

These are patterns, not copy-paste mandates. Adapt to the environment and data.

## 1. Safe pandas merge

```python
import pandas as pd

left = pd.read_parquet("left.parquet")
right = pd.read_parquet("right.parquet")

key = ["customer_id"]

left_dupes = left.duplicated(key, keep=False)
right_dupes = right.duplicated(key, keep=False)

if left_dupes.any():
    raise ValueError("Expected left key unique; investigate duplicates")

result = left.merge(
    right,
    on=key,
    how="outer",
    validate="1:m",
    indicator=True,
)

summary = result["_merge"].value_counts(dropna=False)
```

Use explicit validation errors in production; Python `assert` can be disabled.

## 2. Anti-join populations

```python
matched = result[result["_merge"].eq("both")]
left_only = result[result["_merge"].eq("left_only")]
right_only = result[result["_merge"].eq("right_only")]
```

Never discard unmatched populations before reporting.

## 3. Control totals

```python
controls = {
    "source_rows": len(left),
    "source_amount": left["amount"].sum(min_count=1),
    "output_rows": len(result),
    "matched_rows": int(result["_merge"].eq("both").sum()),
}
```

Use domain-appropriate numeric tolerance.

## 4. Identifier normalization

```python
import re
import unicodedata

def normalize_id(value):
    if value is None:
        return None
    text = str(value).strip()
    return text or None

def normalize_name(value):
    if value is None:
        return None
    text = unicodedata.normalize("NFKC", str(value)).casefold().strip()
    text = re.sub(r"\s+", " ", text)
    return text or None
```

Do not remove punctuation/legal suffixes automatically unless domain rules justify it.

## 5. Fuzzy candidate review

Store source ID, original text, normalized text, candidate ID/text, scorer, score, decision (`accept`/`review`/`reject`), and reviewer/manual override.

Use score bands based on observed validation, not folklore.

## 6. DuckDB over Parquet

```sql
SELECT
    customer_id,
    date_trunc('month', order_date) AS month,
    sum(net_amount) AS revenue
FROM read_parquet('data/orders/*.parquet')
WHERE order_date >= DATE '2026-01-01'
GROUP BY 1, 2;
```

Push filtering/aggregation close to scan.

## 7. Polars lazy pipeline

```python
import polars as pl

lf = (
    pl.scan_parquet("data/*.parquet")
    .filter(pl.col("status") == "active")
    .group_by("customer_id")
    .agg(pl.col("amount").sum().alias("amount"))
)

df = lf.collect()
```

Sort explicitly if output ordering matters.

## 8. XlsxWriter layout pattern

Typical workbook:
- `README`
- `Summary`
- `Data`
- `Exceptions`
- `QA`

Apply reusable format objects, intentional widths, and freeze/filter only where workflow benefits.

## 9. openpyxl safe-edit pattern

```python
from pathlib import Path
from openpyxl import load_workbook

src = Path("input.xlsx")
out = Path("output.xlsx")

wb = load_workbook(src, data_only=False, keep_links=True)
ws = wb["Inputs"]
ws["B2"] = "Updated"
wb.save(out)
```

Before using this on complex corporate workbooks, inventory unsupported-feature risk and validate round trip.

## 10. Excel COM lifecycle sketch

```python
# pseudocode
excel = start_excel()
try:
    old_security = excel.AutomationSecurity
    old_calc = excel.Calculation
    set_safe_security()
    wb = excel.Workbooks.Open(path)
    try:
        wait_until_calculation_done()
        wb.SaveAs(output_path)
    finally:
        wb.Close(SaveChanges=False)
        restore_application_state()
finally:
    excel.Quit()
```

Never suppress security and assume that equals safe execution.

## 11. Run manifest

```json
{
  "run_id": "2026-09-18T18:00:00-03:00",
  "inputs": [{"path": "orders.parquet", "rows": 1200345}],
  "parameters": {"period_start": "2026-08-01", "period_end": "2026-08-31"},
  "outputs": ["management_report.xlsx"],
  "checks": {"source_total_reconciled": true, "unmatched_rows": 17}
}
```

Include hashes for higher-risk work.

## 12. Executive finding pattern

`[Finding]. [Magnitude/baseline]. [Driver/concentration]. [Implication]. [Action or limitation].`

Example:
`Late-delivery rate rose from 4.1% to 7.3% in August. Two carriers explain 71% of the increase, concentrated on the South route. Review capacity/SLA breaches before reallocating volume; 6% of orders still lack a reliable carrier code and are excluded from the driver split.`

## 13. Third-party review finding

```text
MAJOR — Revenue is overstated after the customer merge.

Evidence: source has 98,220 rows / R$12.4m; post-merge output has 131,480 rows / R$16.7m.
Cause: customer_id is non-unique in the right table; merge is many-to-many.
Resolution: aggregate the right table to one row/customer or use the intended composite key, then rerun control totals.
```

## 14. Workbook inventory checklist

Before editing inspect extension, sheet visibility, formulas, merged ranges, tables, names, charts/drawings, VBA, pivots, queries/connections, external links, protection, and print settings.

Use `scripts/inspect_workbook.py` for a first-pass inventory, then inspect high-risk features with target application/tooling.

## 15. Tabular profiling

Use `scripts/profile_tabular.py` for a first-pass profile. Treat automated profiling as triage, not final analytical judgment.
