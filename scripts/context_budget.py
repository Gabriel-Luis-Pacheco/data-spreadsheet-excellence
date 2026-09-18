#!/usr/bin/env python3
"""Report context-size proxies for always-on/core skill files.

This is not an exact tokenizer. Tokenization varies by model/provider/language.
The script tracks lines, words, characters, and a deliberately rough token
proxy so instruction growth is visible in CI.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE_LIMITS = {
    "SKILL.md": {"lines": 500, "words": 4500},
    "AGENTS.md": {"lines": 200, "words": 1800},
    ".github/copilot-instructions.md": {"lines": 150, "words": 1200},
}

def metrics(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    words = len(text.split())
    chars = len(text)
    # Very rough portability proxy only. Never use as billing/tokenizer truth.
    token_proxy = max(round(words * 1.35), round(chars / 4))
    return {
        "lines": len(text.splitlines()),
        "words": words,
        "chars": chars,
        "token_proxy": token_proxy,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="Fail if core instruction files exceed repository guardrails.")
    args = parser.parse_args()

    failures: list[str] = []
    rows: list[tuple[str, dict[str, int], str]] = []

    for rel, limits in CORE_LIMITS.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing core file: {rel}")
            continue
        m = metrics(path)
        status = "OK"
        for key, limit in limits.items():
            if m[key] > limit:
                status = "OVER"
                failures.append(f"{rel}: {key}={m[key]} exceeds {limit}")
        rows.append((rel, m, status))

    refs = sorted((ROOT / "references").glob("*.md"))
    ref_total = {"lines": 0, "words": 0, "chars": 0, "token_proxy": 0}
    for path in refs:
        m = metrics(path)
        for key in ref_total:
            ref_total[key] += m[key]

    print("Core context proxies (token_proxy is approximate, not billing truth):")
    for rel, m, status in rows:
        print(
            f"{status:>4}  {rel:<36} "
            f"lines={m['lines']:<4} words={m['words']:<5} "
            f"chars={m['chars']:<6} token_proxy≈{m['token_proxy']}"
        )

    print(
        f"INFO  references/*.md ({len(refs)} files): "
        f"lines={ref_total['lines']} words={ref_total['words']} "
        f"chars={ref_total['chars']} token_proxy≈{ref_total['token_proxy']} "
        "(not loaded by default)"
    )

    if failures:
        for item in failures:
            print(f"[ERROR] {item}", file=sys.stderr)
        return 1 if args.check else 0

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
