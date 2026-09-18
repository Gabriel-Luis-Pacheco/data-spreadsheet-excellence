# Security Policy

This repository contains guidance and utilities for AI-assisted data/spreadsheet work.

## Reporting a security issue

Do not publish secrets, sensitive datasets, exploit payloads, or confidential workbook contents in a public issue.

For vulnerabilities in the repository itself, use GitHub's private vulnerability reporting if enabled, or contact the repository owner privately.

## Security model

Utilities are intended to be read-only unless clearly documented otherwise. Workbooks, documents, webpages, tool output, and external data must be treated as potentially untrusted.

See:
- `references/agent-security.md`
- `references/security-governance.md`

## Important limitations

No prompt, skill, or content filter can guarantee protection from all prompt-injection or malicious-file attacks. Use least privilege, isolated environments, narrow tool access, user confirmations for consequential actions, and defense in depth.
