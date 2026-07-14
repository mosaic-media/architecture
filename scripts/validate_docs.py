"""Validate repository documentation structure before building MkDocs."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"
BOOK_ROOTS = [
    DOCS_ROOT / "engineering" / "documentation",
    DOCS_ROOT / "engineering" / "architecture",
    DOCS_ROOT / "engineering" / "guides",
    DOCS_ROOT / "engineering" / "protocols",
    DOCS_ROOT / "engineering" / "operations",
    DOCS_ROOT / "design" / "language",
    DOCS_ROOT / "design" / "system",
]
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
METADATA_RE = re.compile(r"\A<!--\n(?P<body>.*?)\n-->", re.DOTALL)
REQUIRED_FIELDS = ("Status:", "Version:")
DOCUMENT_ID_RE = re.compile(r"\b(?:MAC|MDG|MDP|MEG|MIP|MOP|MDL|MDS)-\d{3}\b")


def main() -> int:
    errors: list[str] = []

    for folder in BOOK_ROOTS:
        if not folder.is_dir():
            errors.append(f"Missing documentation section: {folder.relative_to(ROOT)}")
            continue

        for book in sorted(path for path in folder.iterdir() if path.is_dir()):
            if not SLUG_RE.fullmatch(book.name):
                errors.append(f"Book folder is not URL-safe: {book.relative_to(ROOT)}")

            index = book / "index.md"
            if not index.is_file():
                errors.append(f"Book is missing index.md: {book.relative_to(ROOT)}")
                continue

            text = index.read_text(encoding="utf-8")
            metadata = METADATA_RE.match(text)
            if not metadata:
                errors.append(f"Book index is missing top metadata comment: {index.relative_to(ROOT)}")
                continue

            body = metadata.group("body")
            for field in REQUIRED_FIELDS:
                if field not in body:
                    errors.append(f"Book index metadata is missing {field[:-1]}: {index.relative_to(ROOT)}")

            if not DOCUMENT_ID_RE.search(body) and not DOCUMENT_ID_RE.search(text):
                errors.append(f"Book index metadata or heading is missing document ID: {index.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Documentation structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
