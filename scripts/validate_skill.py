#!/usr/bin/env python3
"""Validate core Agent Skills structure and local references.

No third-party dependencies required.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\((references/[^)#\s]+|scripts/[^)#\s]+|assets/[^)#\s]+)\)")

def fail(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)

def main() -> int:
    errors: list[str] = []

    if not SKILL.exists():
        fail("SKILL.md missing")
        return 1

    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        try:
            _, fm, _body = text.split("---", 2)
        except ValueError:
            errors.append("Malformed YAML frontmatter delimiters")
            fm = ""

        name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", fm)
        desc_match = re.search(r"(?m)^description:\s*(.+?)\s*$", fm)

        if not name_match:
            errors.append("frontmatter.name missing")
        else:
            name = name_match.group(1).strip().strip('"\'')
            if len(name) > 64 or not NAME_RE.fullmatch(name):
                errors.append(f"invalid skill name: {name!r}")

        if not desc_match:
            errors.append("frontmatter.description missing")
        else:
            desc = desc_match.group(1).strip().strip('"\'')
            if not (1 <= len(desc) <= 1024):
                errors.append(f"description length {len(desc)} outside 1..1024")

    if len(lines) > 500:
        errors.append(f"SKILL.md has {len(lines)} lines; target is <=500")

    words = len(text.split())
    if words > 4500:
        errors.append(f"SKILL.md has {words} whitespace words; likely too long")

    for rel in LINK_RE.findall(text):
        if not (ROOT / rel).exists():
            errors.append(f"referenced file missing: {rel}")

    required_refs = [
        "references/quick-reference.md",
        "references/tool-selection.md",
        "references/data-analysis-quality.md",
        "references/reconciliation-matching.md",
        "references/spreadsheet-engineering.md",
        "references/visual-design-reporting.md",
        "references/automation-performance.md",
        "references/security-governance.md",
        "references/writing-review-handoff.md",
        "references/quality-gates.md",
        "references/patterns-recipes.md",
    ]
    for rel in required_refs:
        if not (ROOT / rel).exists():
            errors.append(f"required reference missing: {rel}")

    if not (ROOT / "agents" / "openai.yaml").exists():
        errors.append("agents/openai.yaml missing")

    if errors:
        for e in errors:
            fail(e)
        return 1

    print(f"[OK] Skill structure valid: {ROOT}")
    print(f"[OK] SKILL.md lines={len(lines)} words={words}")
    print(f"[OK] references={len(list((ROOT/'references').glob('*.md')))}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
