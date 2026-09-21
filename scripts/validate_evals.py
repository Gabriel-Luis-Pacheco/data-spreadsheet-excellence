#!/usr/bin/env python3
"""Validate the machine-readable eval catalog.

Requires PyYAML. This validates structure and minimum coverage; it does not run
an LLM benchmark.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "evals" / "cases.yaml"

ALLOWED_ACTIVATION = {"should_activate", "should_not_activate"}
ALLOWED_MODES = {"lean", "balanced", "deep"}
ALLOWED_ASSURANCE = {"a0_exploratory", "a1_standard", "a2_material", "a3_critical"}
REQUIRED_TAGS = {
    "efficiency",
    "excel",
    "reconciliation",
    "security",
    "visual",
    "performance",
    "data-contract",
    "activation",
    "locale",
    "review",
}


def main() -> int:
    errors: list[str] = []
    payload = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))

    if not isinstance(payload, dict):
        print("[ERROR] eval catalog must be a mapping", file=sys.stderr)
        return 1

    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    cases = payload.get("cases")
    if not isinstance(cases, list):
        errors.append("cases must be a list")
        cases = []

    ids: set[str] = set()
    tags_seen: set[str] = set()
    activations: set[str] = set()
    modes: set[str] = set()
    assurances: set[str] = set()

    for i, case in enumerate(cases, start=1):
        prefix = f"cases[{i}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be a mapping")
            continue

        required = [
            "id",
            "title",
            "prompt",
            "activation",
            "execution_mode",
            "assurance_tier",
            "tags",
            "must",
            "must_not",
        ]
        for key in required:
            if key not in case:
                errors.append(f"{prefix}.{key} missing")

        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}.id must be non-empty string")
        elif case_id in ids:
            errors.append(f"duplicate eval id: {case_id}")
        else:
            ids.add(case_id)

        activation = case.get("activation")
        if activation not in ALLOWED_ACTIVATION:
            errors.append(f"{prefix}.activation invalid: {activation!r}")
        else:
            activations.add(activation)

        mode = case.get("execution_mode")
        if mode not in ALLOWED_MODES:
            errors.append(f"{prefix}.execution_mode invalid: {mode!r}")
        else:
            modes.add(mode)

        assurance = case.get("assurance_tier")
        if assurance not in ALLOWED_ASSURANCE:
            errors.append(f"{prefix}.assurance_tier invalid: {assurance!r}")
        else:
            assurances.add(assurance)

        tags = case.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(x, str) and x for x in tags):
            errors.append(f"{prefix}.tags must be a non-empty string list")
        else:
            tags_seen.update(tags)

        for field in ("must", "must_not"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(x, str) and x.strip() for x in values):
                errors.append(f"{prefix}.{field} must be a non-empty string list")

        if not isinstance(case.get("prompt"), str) or len(case.get("prompt", "").strip()) < 8:
            errors.append(f"{prefix}.prompt is too short")

    if len(cases) < 10:
        errors.append("catalog should contain at least 10 representative evals")

    if activations != ALLOWED_ACTIVATION:
        errors.append("catalog must contain both activation-positive and activation-negative cases")

    missing_modes = ALLOWED_MODES - modes
    if missing_modes:
        errors.append(f"execution mode coverage missing: {sorted(missing_modes)}")

    missing_assurance = ALLOWED_ASSURANCE - assurances
    if missing_assurance:
        errors.append(f"assurance coverage missing: {sorted(missing_assurance)}")

    missing_tags = REQUIRED_TAGS - tags_seen
    if missing_tags:
        errors.append(f"required scenario coverage missing tags: {sorted(missing_tags)}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1

    print(f"[OK] eval catalog valid: {len(cases)} cases")
    print(f"[OK] modes={sorted(modes)} assurances={sorted(assurances)}")
    print(f"[OK] required tags covered={sorted(REQUIRED_TAGS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
