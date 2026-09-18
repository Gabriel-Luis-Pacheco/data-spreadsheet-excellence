# Security and Governance

Spreadsheets are documents, code containers, and data interfaces. Treat them accordingly.

## 1. Threat model

Potential risks include VBA/macros, Excel 4.0 macros, external links, Power Query/connectors, embedded objects, formulas, CSV/formula injection, untrusted Python/R scripts, sensitive data, credentials, malformed archives, and accidental publication.

## 2. Preserve and isolate

For untrusted inputs:
- work on a copy;
- avoid executing active content;
- use temporary/sandboxed locations;
- keep source immutable;
- write outputs separately.

## 3. Excel automation security

`DisplayAlerts=False` suppresses ordinary alerts; it is not macro security.

When opening workbooks programmatically in desktop Excel:
- capture current automation security;
- set a safer mode appropriate to the task before opening untrusted files;
- process;
- restore the prior setting promptly;
- do not automatically enable macros to “make the workbook work”.

Legacy Excel 4.0 macro behavior needs separate consideration.

## 4. Macros

Do not execute macros from unknown workbooks.

When macro behavior must be tested:
- establish trust/source;
- use an isolated/test environment;
- document whether macros were executed;
- preserve signatures when relevant;
- verify outputs separately.

## 5. External links and Power Query

Inspect data source URLs/paths, credentials, privacy levels, native queries, custom connectors, gateways, and refresh destinations.

Use trusted/certified connectors where possible. Treat Python/R scripts inside refresh workflows as code with user-level permissions.

## 6. Formula and CSV injection

Untrusted text beginning with formula-triggering characters can execute as formulas in spreadsheet software.

Mitigation depends on consumer and format:
- use typed XLSX cells where possible;
- escape/prefix untrusted text according to target-system guidance;
- do not blindly prefix legitimate numeric negatives;
- test how the target spreadsheet interprets exported values.

Separate external untrusted text from intentional formula.

## 7. Secrets

Never store secrets in source code, committed `.env`, workbook hidden cells, logs, screenshots, or README examples.

Use environment variables, secret managers, managed identity, or secure credential stores.

## 8. Least privilege

Grant only needed permissions: read-only when possible, limited spreadsheet scopes, restricted folders, and narrow service-account access.

## 9. Privacy and data minimization

Before sending data to third-party APIs, AI services, cloud storage, or external consultants, confirm authorization and minimize fields/rows. Use pseudonymization/tokenization when identity is unnecessary.

## 10. Temporary data

Clean up temp extracts, intermediate workbooks, rendered sensitive screenshots, and local caches. Hidden folders are not a security boundary.

## 11. Logging

Log operational metadata, not raw sensitive records. If debugging needs samples, mask, hash, truncate, or use synthetic data.

## 12. Version control

Do not commit production data, secrets, client workbooks, sensitive screenshots, or generated confidential outputs. Use `.gitignore` and secret scanning where appropriate.

## 13. Supply-chain safety

Prefer maintained packages, constrain versions for recurring jobs, review new dependencies, and avoid executing scripts from unknown workbooks/repos without inspection.

## 14. Governance for high-risk analysis

Document owner, purpose, source, approval/reviewer, metric definitions, material assumptions, validation, change history, retention policy, and publication status.

## 15. Publication

Before external sharing:
- remove hidden/sensitive sheets;
- inspect document properties;
- break/remove links only if intended;
- validate accessibility;
- verify formulas/results;
- verify comments/notes do not expose private data;
- open the exact final file that will be sent.

## 16. Security anti-patterns

- disabling macro security to avoid prompts;
- assuming hidden PII is safe;
- logging entire rejected records;
- committing source extracts;
- refreshing unknown external queries automatically;
- using `eval()` on spreadsheet text;
- trusting file extension alone.
