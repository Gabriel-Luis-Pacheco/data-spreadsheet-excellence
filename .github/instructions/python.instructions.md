---
applyTo: "scripts/**/*.py"
---

# Python utility instructions

- Keep scripts deterministic, small, dependency-light, and read-only by default.
- Preserve identifiers/text at data-ingestion boundaries unless type inference is explicitly requested.
- Use explicit validation errors; do not use `assert` for production input checks.
- Avoid broad exception swallowing.
- Prefer standard library when it is sufficient.
- Add or update focused regression checks for behavior changes.
- Compile changed scripts and run the smallest functional test that demonstrates the requested behavior.
- Do not refactor unrelated utilities while fixing one script.
