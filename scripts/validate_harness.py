#!/usr/bin/env python3
"""Validate machine-readable harness and OpenAI metadata."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def error(message: str) -> None:
    print(f"[ERROR] {message}", file=sys.stderr)


def main() -> int:
    try:
        import yaml
    except ImportError:
        error("PyYAML is required for harness validation")
        return 1

    failures: list[str] = []

    harness_path = ROOT / "harness" / "harness.yaml"
    try:
        harness = yaml.safe_load(harness_path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(f"invalid harness YAML: {exc}")
        return 1

    if not isinstance(harness, dict):
        failures.append("harness root must be a mapping")
        harness = {}

    if not isinstance(harness.get("version"), int):
        failures.append("harness.version must be an integer")

    modes = harness.get("execution_modes")
    if not isinstance(modes, dict):
        failures.append("execution_modes must be a mapping")
        modes = {}
    expected_modes = {"lean", "balanced", "deep"}
    if set(modes) != expected_modes:
        failures.append(f"execution_modes must be exactly {sorted(expected_modes)}")

    tiers = harness.get("assurance_tiers")
    if not isinstance(tiers, dict):
        failures.append("assurance_tiers must be a mapping")
        tiers = {}
    expected_tiers = {"a0_exploratory", "a1_standard", "a2_material", "a3_critical"}
    if set(tiers) != expected_tiers:
        failures.append(f"assurance_tiers must be exactly {sorted(expected_tiers)}")

    defaults = harness.get("defaults")
    if not isinstance(defaults, dict):
        failures.append("defaults must be a mapping")
        defaults = {}

    for key in ("context_policy", "trust_policy", "tool_policy", "coding_policy", "output_policy"):
        if not isinstance(defaults.get(key), dict):
            failures.append(f"defaults.{key} must be a mapping")

    stop_conditions = harness.get("stop_conditions")
    if not isinstance(stop_conditions, list) or not stop_conditions:
        failures.append("stop_conditions must be a non-empty list")

    openai_path = ROOT / "agents" / "openai.yaml"
    try:
        openai_meta = yaml.safe_load(openai_path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"invalid agents/openai.yaml: {exc}")
        openai_meta = {}

    interface = openai_meta.get("interface") if isinstance(openai_meta, dict) else None
    if not isinstance(interface, dict):
        failures.append("agents/openai.yaml interface must be a mapping")
    else:
        for key in ("display_name", "short_description", "default_prompt"):
            if not interface.get(key):
                failures.append(f"agents/openai.yaml interface.{key} missing")
        prompt = str(interface.get("default_prompt", ""))
        if "$data-spreadsheet-excellence" not in prompt:
            failures.append("default_prompt must reference $data-spreadsheet-excellence")

    if failures:
        for item in failures:
            error(item)
        return 1

    print("[OK] harness/harness.yaml structure valid")
    print("[OK] agents/openai.yaml structure valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
