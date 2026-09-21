#!/usr/bin/env python3
"""Export machine-readable eval cases as JSONL for external harnesses."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default=str(ROOT / "evals" / "cases.yaml"))
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--activation", choices=["should_activate", "should_not_activate"])
    args = parser.parse_args()

    payload = yaml.safe_load(Path(args.catalog).read_text(encoding="utf-8"))
    cases = payload.get("cases", [])

    required_tags = set(args.tag)
    emitted = 0
    for case in cases:
        tags = set(case.get("tags") or [])
        if required_tags and not required_tags.issubset(tags):
            continue
        if args.activation and case.get("activation") != args.activation:
            continue

        record = {
            "id": case["id"],
            "prompt": case["prompt"],
            "expected": {
                "activation": case["activation"],
                "execution_mode": case["execution_mode"],
                "assurance_tier": case["assurance_tier"],
                "must": case["must"],
                "must_not": case["must_not"],
            },
            "tags": case["tags"],
        }
        print(json.dumps(record, ensure_ascii=False))
        emitted += 1

    if emitted == 0:
        raise SystemExit("No eval cases matched the filters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
