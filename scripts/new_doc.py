"""Scaffold a new Mosaic specification from the templates/ set.

Usage:
    python3 scripts/new_doc.py --type mad --title "Module Signing Policy"
    python3 scripts/new_doc.py --type mad --title "Module Signing Policy" --id mad-003
    python3 scripts/new_doc.py --type meg --title "Caching Strategy" --dry-run

The destination discipline directory for each type is defined by MDG-001 chapter 07.
Metadata follows the three-field schema from that chapter: File, Document, Status.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"
TEMPLATES_ROOT = ROOT / "templates"

# Where each document type belongs, per MDG-001 chapter 07.
DESTINATIONS = {
    "mdp": "engineering/architecture",
    "mad": "engineering/architecture",
    "mac": "engineering/architecture",
    "meg": "engineering/guides",
    "mip": "engineering/protocols",
    "mop": "engineering/operations",
    "mdg": "engineering/documentation",
    "mdl": "design/language",
    "mds": "design/system",
    "mrm": "roadmaps",
}

# The human-readable title placeholder each template uses.
TITLE_PLACEHOLDERS = {
    "mad": "Decision Title",
    "mdp": "Proposal Title",
    "mip": "Subject Protocol",
    "mop": "Subject Operations",
}
DEFAULT_TITLE_PLACEHOLDER = "Subject Title"
PAGES_TITLE_PLACEHOLDER = "Specification Title"

FOLDER_RE = re.compile(r"^(?P<prefix>[a-z]{3})-(?P<number>\d{3})-(?P<slug>[a-z0-9-]+)$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
METADATA_RE = re.compile(r"\A<!--\n(?P<body>.*?)\n-->", re.DOTALL)
# Every dash-like codepoint becomes a plain hyphen before slugging, so that a title such as
# "Platform–SDK Contract Protocol" slugs to "platform-sdk-contract-protocol".
DASHES = dict.fromkeys(map(ord, "‐‑‒–—―−"), "-")


class ScaffoldError(Exception):
    """A user-facing failure that should exit non-zero with a readable message."""


def slugify(title: str) -> str:
    """Return a URL-safe lowercase slug, per MDG-001 chapter 07 naming conventions."""
    normalised = unicodedata.normalize("NFKD", title.translate(DASHES))
    ascii_only = normalised.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_only.lower()).strip("-")
    if not slug:
        raise ScaffoldError(f"Title does not produce a usable slug: {title!r}")
    if not SLUG_RE.fullmatch(slug):
        raise ScaffoldError(f"Title produces an invalid slug: {slug!r}")
    return slug


def existing_numbers(destination: Path, doc_type: str) -> list[int]:
    """Return the sequence numbers already used by this document type."""
    if not destination.is_dir():
        return []

    numbers = []
    for child in destination.iterdir():
        if not child.is_dir():
            continue
        match = FOLDER_RE.fullmatch(child.name)
        if match and match.group("prefix") == doc_type:
            numbers.append(int(match.group("number")))
    return sorted(numbers)


def next_number(destination: Path, doc_type: str) -> int:
    """Allocate the next sequence number.

    Deliberately max + 1 rather than first-gap: identifiers are permanent references, so a
    number freed by a deleted or renumbered specification must never be reissued.
    """
    numbers = existing_numbers(destination, doc_type)
    number = (max(numbers) + 1) if numbers else 1
    if number > 999:
        raise ScaffoldError(f"No sequence numbers remain for {doc_type.upper()}")
    return number


def parse_id(raw: str, doc_type: str) -> int:
    """Accept mad-003, MAD-003, 003 or 3 and return the numeric part."""
    candidate = raw.strip().lower()
    match = re.fullmatch(r"(?:(?P<prefix>[a-z]{3})-)?(?P<number>\d{1,3})", candidate)
    if not match:
        raise ScaffoldError(f"Identifier is not recognised: {raw!r} (expected e.g. mad-003)")

    prefix = match.group("prefix")
    if prefix and prefix != doc_type:
        raise ScaffoldError(
            f"Identifier prefix {prefix!r} does not match --type {doc_type!r}"
        )

    number = int(match.group("number"))
    if number < 1:
        raise ScaffoldError(f"Identifier must be 001 or greater: {raw!r}")
    return number


@dataclass
class Plan:
    """Everything the scaffold will produce, resolved before anything is written."""

    doc_type: str
    document_id: str
    title: str
    slug: str
    folder: Path
    files: list[str]
    parent_pages: Optional[Path]

    @property
    def relative_folder(self) -> str:
        return self.folder.relative_to(ROOT).as_posix()


def template_files(template_dir: Path) -> list[str]:
    return sorted(path.name for path in template_dir.glob("*.md"))


def build_plan(doc_type: str, title: str, requested_id: Optional[str]) -> Plan:
    if doc_type not in DESTINATIONS:
        raise ScaffoldError(
            f"Unknown type {doc_type!r}. Expected one of: {', '.join(sorted(DESTINATIONS))}"
        )

    template_dir = TEMPLATES_ROOT / doc_type
    if not template_dir.is_dir():
        raise ScaffoldError(f"Template is missing: {template_dir}")

    title = title.strip()
    if not title:
        raise ScaffoldError("Title must not be empty")

    destination = DOCS_ROOT / DESTINATIONS[doc_type]
    number = parse_id(requested_id, doc_type) if requested_id else next_number(destination, doc_type)

    if requested_id and number in existing_numbers(destination, doc_type):
        raise ScaffoldError(f"{doc_type.upper()}-{number:03d} already exists")

    slug = slugify(title)
    folder = destination / f"{doc_type}-{number:03d}-{slug}"
    if folder.exists():
        raise ScaffoldError(f"Refusing to overwrite existing folder: {folder}")

    parent_pages = destination / ".pages"
    return Plan(
        doc_type=doc_type,
        document_id=f"{doc_type.upper()}-{number:03d}",
        title=title,
        slug=slug,
        folder=folder,
        files=template_files(template_dir) + [".pages"],
        parent_pages=parent_pages if parent_pages.is_file() else None,
    )


def stamp(text: str, plan: Plan, relative_path: str) -> str:
    """Rewrite a template file for its real destination."""
    placeholder_id = f"{plan.doc_type.upper()}-NNN"
    title_placeholder = TITLE_PLACEHOLDERS.get(plan.doc_type, DEFAULT_TITLE_PLACEHOLDER)

    match = METADATA_RE.match(text)
    if not match:
        raise ScaffoldError(f"Template file is missing its metadata block: {relative_path}")

    block = "\n".join(
        [
            "<!--",
            f"File: {relative_path}",
            f"Document: {plan.document_id}",
            "Status: Draft",
            "-->",
        ]
    )
    text = block + text[match.end() :]

    # Body placeholders. The Document Control table repeats the identifier, so this
    # substitution is what keeps it agreeing with the metadata block.
    text = text.replace(placeholder_id, plan.document_id)
    text = text.replace(title_placeholder, plan.title)
    return text


def render_pages(plan: Plan) -> str:
    """Generate the specification's own .pages navigation."""
    chapters = [name for name in plan.files if name.endswith(".md")]
    ordered = ["index.md", "00-document-control.md"]
    middle = sorted(
        name for name in chapters if name not in {*ordered, "references.md", "glossary.md"}
    )
    ordered = ordered + middle + ["references.md", "glossary.md"]

    lines = [f"title: {plan.title}", "arrange:"]
    lines.extend(f"  - {name}" for name in ordered)
    return "\n".join(lines) + "\n"


def register_in_parent_pages(pages: Path, folder_name: str, dry_run: bool) -> bool:
    """Add the new folder to its discipline .pages, keeping folder entries sorted.

    CLAUDE.md requires .pages navigation to be updated whenever a specification folder is
    added. Returns True when a change was made or would be made.
    """
    text = pages.read_text(encoding="utf-8")
    lines = text.splitlines()
    entries = [
        index
        for index, line in enumerate(lines)
        if line.startswith("  - ") and line[4:].strip() != "index.md"
    ]

    if any(lines[index][4:].strip() == folder_name for index in entries):
        return False

    new_line = f"  - {folder_name}"
    if not entries:
        insert_at = len(lines)
    else:
        insert_at = next(
            (index for index in entries if lines[index][4:].strip() > folder_name),
            entries[-1] + 1,
        )

    if not dry_run:
        lines.insert(insert_at, new_line)
        pages.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return True


def scaffold(plan: Plan, dry_run: bool) -> None:
    template_dir = TEMPLATES_ROOT / plan.doc_type

    if dry_run:
        print(f"Would create {plan.relative_folder}/")
    else:
        plan.folder.mkdir(parents=True)
        print(f"Created {plan.relative_folder}/")

    for name in plan.files:
        destination = plan.folder / name
        relative_path = destination.relative_to(ROOT).as_posix()

        if name == ".pages":
            content = render_pages(plan)
        else:
            content = stamp(
                (template_dir / name).read_text(encoding="utf-8"), plan, relative_path
            )

        if dry_run:
            print(f"  would write {name}")
        else:
            destination.write_text(content, encoding="utf-8", newline="\n")
            print(f"  wrote {name}")

    if plan.parent_pages:
        changed = register_in_parent_pages(plan.parent_pages, plan.folder.name, dry_run)
        relative_pages = plan.parent_pages.relative_to(ROOT).as_posix()
        if changed:
            verb = "would register" if dry_run else "registered"
            print(f"  {verb} {plan.folder.name} in {relative_pages}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="new_doc.py",
        description="Scaffold a new Mosaic specification from templates/.",
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=sorted(DESTINATIONS),
        help="Document type. Determines the discipline directory and the template used.",
    )
    parser.add_argument("--title", required=True, help='Specification title, e.g. "Module Signing Policy".')
    parser.add_argument(
        "--id",
        dest="document_id",
        help="Explicit identifier such as mad-003. Omit to allocate the next sequential number.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing anything.",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        plan = build_plan(args.type, args.title, args.document_id)
    except ScaffoldError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"{plan.document_id} — {plan.title}")
    scaffold(plan, args.dry_run)

    if args.dry_run:
        print("\nDry run. Nothing was written.")
    else:
        print(
            "\nNext: replace the guidance comments and placeholders, set the Owner, "
            "then run python3 scripts/validate_docs.py"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
