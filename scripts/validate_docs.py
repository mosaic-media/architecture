"""Validate repository documentation structure before building MkDocs."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Optional


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
REFERENCE_PAGES = {"references.md", "10-references.md", "16-references.md"}
GLOSSARY_PAGES = {"glossary.md", "11-glossary.md"}


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def metadata_value(body: str, field: str) -> Optional[str]:
    prefix = f"{field}:"
    for line in body.splitlines():
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return None


def page_value(line: str) -> Optional[str]:
    stripped = line.strip()
    if not stripped.startswith("- "):
        return None

    value = stripped[2:].strip()
    if value and value[0] in {"'", '"'} and value.endswith(value[0]):
        value = value[1:-1]
    return value


def validate_pages_navigation(book: Path, errors: list[str]) -> None:
    pages = book / ".pages"
    if not pages.is_file():
        return

    reference_positions: list[int] = []
    glossary_positions: list[int] = []
    for index, line in enumerate(pages.read_text(encoding="utf-8").splitlines()):
        value = page_value(line)
        if value in REFERENCE_PAGES:
            reference_positions.append(index)
        elif value in GLOSSARY_PAGES:
            glossary_positions.append(index)

    if reference_positions and glossary_positions and min(reference_positions) > min(glossary_positions):
        errors.append(f"Book .pages places references after glossary: {relative_path(pages)}")


def validate_markdown_file(path: Path, errors: list[str]) -> Optional[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    metadata = METADATA_RE.match(text)
    if not metadata:
        errors.append(f"Markdown file is missing top metadata comment: {relative_path(path)}")
        return None

    body = metadata.group("body")
    declared_file = metadata_value(body, "File")
    if declared_file is None:
        errors.append(f"Markdown file metadata is missing File: {relative_path(path)}")
    elif declared_file != relative_path(path):
        errors.append(
            f"Markdown file metadata has stale File path: {relative_path(path)} "
            f"(declares {declared_file})"
        )

    return body, text


def main() -> int:
    errors: list[str] = []

    for folder in BOOK_ROOTS:
        if not folder.is_dir():
            errors.append(f"Missing documentation section: {folder.relative_to(ROOT)}")
            continue

        for book in sorted(path for path in folder.iterdir() if path.is_dir()):
            if not SLUG_RE.fullmatch(book.name):
                errors.append(f"Book folder is not URL-safe: {relative_path(book)}")

            validate_pages_navigation(book, errors)

            index = book / "index.md"
            if not index.is_file():
                errors.append(f"Book is missing index.md: {relative_path(book)}")
                continue

            index_metadata: Optional[tuple[str, str]] = None
            for markdown_file in sorted(book.rglob("*.md")):
                metadata = validate_markdown_file(markdown_file, errors)
                if markdown_file == index:
                    index_metadata = metadata

            if index_metadata is None:
                continue

            body, text = index_metadata
            for field in REQUIRED_FIELDS:
                if field not in body:
                    errors.append(f"Book index metadata is missing {field[:-1]}: {relative_path(index)}")

            if not DOCUMENT_ID_RE.search(body) and not DOCUMENT_ID_RE.search(text):
                errors.append(f"Book index metadata or heading is missing document ID: {relative_path(index)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Documentation structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
