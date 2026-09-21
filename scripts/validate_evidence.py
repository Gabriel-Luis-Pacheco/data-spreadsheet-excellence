#!/usr/bin/env python3
"""Validate an evidence-manifest YAML.

Default mode validates structure. --strict is intended for completed A2/A3
handoffs and requires material fields/check outcomes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")
MODES = {"lean", "balanced", "deep"}
ASSURANCE = {"a0_exploratory", "a1_standard", "a2_material", "a3_critical"}
FIDELITY = {"f0", "f1", "f2", "f3"}
CHECK_STATUS = {"pass", "warn", "fail", "not_run"}
APPROVAL_STATUS = {"not_required", "pending", "approved", "rejected"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        nargs="?",
        default="assets/evidence-manifest-template.yaml",
        help="Manifest to validate.",
    )
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    errors: list[str] = []

    if not isinstance(data, dict):
        print("[ERROR] manifest root must be a mapping", file=sys.stderr)
        return 1

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    task = data.get("task")
    if not isinstance(task, dict):
        errors.append("task must be a mapping")
        task = {}

    if task.get("execution_mode") not in MODES:
        errors.append(f"task.execution_mode must be one of {sorted(MODES)}")
    if task.get("assurance_tier") not in ASSURANCE:
        errors.append(f"task.assurance_tier must be one of {sorted(ASSURANCE)}")
    if task.get("fidelity") not in FIDELITY:
        errors.append(f"task.fidelity must be one of {sorted(FIDELITY)}")

    for list_key in ("sources", "checks", "exceptions", "limitations", "outputs"):
        if not isinstance(data.get(list_key), list):
            errors.append(f"{list_key} must be a list")

    for source in data.get("sources") or []:
        if not isinstance(source, dict):
            errors.append("each sources item must be a mapping")
            continue
        digest = str(source.get("sha256", "")).strip()
        if digest and not HEX64.fullmatch(digest):
            errors.append(f"invalid source sha256 for {source.get('id', '<unknown>')}")

    for output in data.get("outputs") or []:
        if not isinstance(output, dict):
            errors.append("each outputs item must be a mapping")
            continue
        digest = str(output.get("sha256", "")).strip()
        if digest and not HEX64.fullmatch(digest):
            errors.append(f"invalid output sha256 for {output.get('path_or_uri', '<unknown>')}")

    for check in data.get("checks") or []:
        if not isinstance(check, dict):
            errors.append("each checks item must be a mapping")
            continue
        if check.get("status") not in CHECK_STATUS:
            errors.append(f"invalid check status for {check.get('id', '<unknown>')}")

    approval = data.get("approval")
    if not isinstance(approval, dict):
        errors.append("approval must be a mapping")
        approval = {}
    if approval.get("status") not in APPROVAL_STATUS:
        errors.append(f"approval.status must be one of {sorted(APPROVAL_STATUS)}")

    drift = data.get("drift")
    if not isinstance(drift, dict):
        errors.append("drift must be a mapping")

    if args.strict:
        if not str(data.get("run_id", "")).strip():
            errors.append("strict: run_id is required")
        if not str(data.get("created_at", "")).strip():
            errors.append("strict: created_at is required")
        if not str(data.get("skill_version", "")).strip():
            errors.append("strict: skill_version is required")
        if not str(task.get("goal", "")).strip():
            errors.append("strict: task.goal is required")
        if not str(task.get("output", "")).strip():
            errors.append("strict: task.output is required")

        tier = task.get("assurance_tier")
        if tier in {"a2_material", "a3_critical"}:
            if not (data.get("sources") or []):
                errors.append("strict A2/A3: at least one source is required")
            if not (data.get("checks") or []):
                errors.append("strict A2/A3: at least one check is required")
            if not (data.get("outputs") or []):
                errors.append("strict A2/A3: at least one output is required")

        failed = [
            str(x.get("id", "<unknown>"))
            for x in (data.get("checks") or [])
            if isinstance(x, dict) and x.get("status") == "fail"
        ]
        if failed:
            errors.append(f"strict: failed checks present: {failed}")

        if approval.get("required") is True and approval.get("status") != "approved":
            errors.append("strict: required approval is not approved")

    if errors:
        for item in errors:
            print(f"[ERROR] {item}", file=sys.stderr)
        return 1

    print(f"[OK] evidence manifest valid: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
