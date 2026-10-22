#!/usr/bin/env python3
"""Advisory audit of author-written reader-facing prose (not AI detection).

Text files: inspect narrative outside fenced code / markdown blockquotes.
Excel: require explicit --xlsx-range so imported business data is NEVER
automatically rewritten, judged or treated as agent-authored.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

# High-confidence, contextual phrases only. Do not prohibit individual words.
PHRASES = {
    "empty_opening": [
        r"\bneste relat[oó]rio (?:iremos|ser[aá]|abordaremos|vamos)\b",
        r"\b(?:in|throughout) this report (?:we will|you will)\b",
    ],
    "promotional_filler": [
        r"\binsights? valiosos?\b",
        r"\ban[aá]lise robusta e abrangente\b",
        r"\b(?:valuable insights|robust and comprehensive analysis)\b",
        r"\boportunidades? (?:estrat[eé]gicas?|de melhoria) significativas?\b",
    ],
    "agent_process_leak": [
        r"\brelat[oó]rio de execu[cç][aã]o da ia\b",
        r"\b(?:worker|subagent) (?:executou|realizou|processou)\b",
        r"\b(?:the ai|o modelo de ia) (?:performed|realizou|gerou)\b",
    ],
    "empty_conclusion": [
        r"\bem conclus[aã]o,? (?:os resultados|a an[aá]lise) demonstram\b",
        r"\bin conclusion,? (?:these results|the analysis) (?:show|demonstrate)\b",
    ],
}
PATTERNS = [
    (rule, re.compile(pattern, re.IGNORECASE))
    for rule, patterns in PHRASES.items()
    for pattern in patterns
]
MARKDOWN_MARKERS = re.compile(r"(?<!\*)\*\*[^*\n]+\*\*|\x60[^\x60\n]+\x60")


def audit_text(text: str, *, cell: bool = False, skip_examples: bool = False) -> list[dict[str, str | int]]:
    """Return candidates for *human* review, never an authorship score."""
    issues: list[dict[str, str | int]] = []
    in_fence = False
    for index, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if skip_examples:
            if stripped.startswith(("\x60\x60\x60", "~~~")):
                in_fence = not in_fence
                continue
            if in_fence or stripped.startswith(">"):
                continue
        for rule, pattern in PATTERNS:
            match = pattern.search(line)
            if match:
                issues.append({
                    "rule": rule,
                    "line": index,
                    "excerpt": match.group(0),
                    "note": "Review only if this is authored prose and not a required quote or source value.",
                })
        if cell and MARKDOWN_MARKERS.search(line):
            issues.append({
                "rule": "markdown_in_excel",
                "line": index,
                "excerpt": line[:100],
                "note": "Check whether literal Markdown formatting leaked into a cell.",
            })
    return issues


def audit_file(path: Path, xlsx_range: str | None) -> list[dict[str, str | int]]:
    suffix = path.suffix.lower()
    if suffix == ".xlsx":
        if not xlsx_range or "!" not in xlsx_range:
            raise ValueError("Excel requires --xlsx-range Sheet!A1:D10 for author-written cells only.")
        from openpyxl import load_workbook
        from openpyxl.utils.cell import range_boundaries

        sheet, coordinate = xlsx_range.rsplit("!", 1)
        sheet = sheet.strip("'")
        min_col, min_row, max_col, max_row = range_boundaries(coordinate)
        if not all((min_col, min_row, max_col, max_row)):
            raise ValueError("The Excel range must be bounded, e.g. Report!A1:D10.")
        if (max_row - min_row + 1) * (max_col - min_col + 1) > 10000:
            raise ValueError("Review at most 10,000 designated authored cells per call.")
        wb = load_workbook(path, read_only=True, data_only=False, keep_links=False)
        try:
            ws = wb[sheet]
            issues: list[dict[str, str | int]] = []
            for row in ws.iter_rows(
                min_row=min_row, max_row=max_row, min_col=min_col, max_col=max_col
            ):
                for c in row:
                    if c.data_type == "f" or not isinstance(c.value, str):
                        continue
                    for issue in audit_text(c.value, cell=True):
                        issues.append({**issue, "cell": f"{sheet}!{c.coordinate}"})
            return issues
        finally:
            wb.close()
    if suffix not in {".md", ".txt"}:
        raise ValueError("Supported formats: .md, .txt, or .xlsx with --xlsx-range.")
    return audit_text(path.read_text(encoding="utf-8"), skip_examples=suffix == ".md")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--xlsx-range", help="Explicit sheet + bounded range of authored prose.")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if candidate issues exist.")
    args = parser.parse_args(argv)
    try:
        issues = audit_file(args.file, args.xlsx_range)
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))
    print(json.dumps({
        "file": str(args.file),
        "issues": issues,
        "note": "Advisory editorial hints only. Not proof of AI origin or factual correctness.",
    }, ensure_ascii=False, indent=2))
    return 1 if args.strict and issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
