#!/usr/bin/env python3
"""Create a compact provenance manifest for input/output files.

Streams SHA-256 hashes without reading file contents into model context.
Does not upload or modify source files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def file_record(path: Path, include_hash: bool) -> dict:
    stat = path.stat()
    record = {
        "path": str(path),
        "name": path.name,
        "size_bytes": stat.st_size,
        "modified_utc": datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat(),
        "suffix": path.suffix.lower(),
    }
    if include_hash:
        record["sha256"] = sha256_file(path)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    parser.add_argument(
        "--no-hash",
        action="store_true",
        help="Skip SHA-256 hashing when metadata-only inventory is sufficient.",
    )
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    records = []
    for raw in args.paths:
        path = Path(raw)
        if not path.exists():
            raise SystemExit(f"File not found: {path}")
        if not path.is_file():
            raise SystemExit(f"Expected a file: {path}")
        records.append(file_record(path, include_hash=not args.no_hash))

    result = {
        "generated_utc": datetime.now(tz=timezone.utc).isoformat(),
        "hash_algorithm": None if args.no_hash else "sha256",
        "files": records,
    }

    print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
