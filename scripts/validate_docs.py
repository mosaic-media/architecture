"""Validate repository documentation against MDG-001 before building MkDocs.

Every rule here enforces something MDG-001 states normatively. Findings are reported per
file with a stable rule name, and any finding fails the run.

Run:
    python3 scripts/validate_docs.py
    python3 scripts/validate_docs.py --rules      # list the rules and what they enforce
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Optional
from urllib.parse import unquote

from markdown.extensions.toc import slugify


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"
OUTPUT_ROOT = ROOT / "output"
CHAPTER_REGISTRY = ROOT / "chapter-registry.yml"
BOOK_ROOTS = [
    DOCS_ROOT / "engineering" / "documentation",
    DOCS_ROOT / "engineering" / "architecture",
    DOCS_ROOT / "engineering" / "guides",
    DOCS_ROOT / "engineering" / "protocols",
    DOCS_ROOT / "engineering" / "operations",
    DOCS_ROOT / "design" / "language",
    DOCS_ROOT / "design" / "system",
    DOCS_ROOT / "roadmaps",
]
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
METADATA_RE = re.compile(r"\A<!--\n(?P<body>.*?)\n-->", re.DOTALL)
REQUIRED_FIELDS = ("File", "Document", "Status")
# MDG-001 chapter 07 permits exactly three metadata fields and no others.
ALLOWED_FIELDS = frozenset(REQUIRED_FIELDS)
DOCUMENT_ID_RE = re.compile(r"\b(?:MDP|MAD|MAC|MEG|MIP|MOP|MDL|MDS|MDG|MRM)-\d{3}\b")
# MDG-001 chapter 03 defines the Status lifecycle. Proposal-only values apply to MDP.
STATUS_VALUES = frozenset({"Draft", "Review", "Active", "Deprecated", "Superseded"})
PROPOSAL_STATUS_VALUES = frozenset({"Deferred", "Accepted", "Rejected", "Withdrawn"})
# An owner must identify someone accountable. These values do not.
PLACEHOLDER_OWNERS = frozenset(
    {"", "tbd", "tbc", "todo", "unknown", "none", "n/a", "na", "owner", "git-username"}
)
H1_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)
SECTION_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
MARKDOWN_LINK_RE = re.compile(r"!?\[(?P<label>[^\]]*)\]\((?P<target>[^)]+)\)")
FENCED_BLOCK_RE = re.compile(
    r"^```(?P<language>[^\n]*)\n(?P<body>.*?)^```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
TEXT_DIAGRAM_ARROW_RE = re.compile(r"^\s*(?:↓|↑|→|←|↔|⇄|⇆|▼|▲)\s*$", re.MULTILINE)
TEXT_HIERARCHY_RE = re.compile(r"[├└]")
FILE_TREE_ENTRY_RE = re.compile(
    r"\b[^\s/]+\.(?:md|go|yaml|yml|json|css|toml|png|jpg|jpeg|svg|sql|sh|txt)\b",
    re.IGNORECASE,
)
NAMED_DOCUMENT_RE = re.compile(
    r"^(?P<id>(?:MDP|MAD|MAC|MEG|MIP|MOP|MDL|MDS|MDG|MRM)-\d{3})\s+—\s+(?P<title>.+)$"
)
UNAVAILABLE_MARKERS = ("planned; not yet published", "deferred; not yet published")
MANUAL_NAV_RE = re.compile(
    r"^(?:#{1,6}\s+|\*\*)(?:Previous|Next) File(?:\*\*)?\s*$",
    re.MULTILINE,
)
REVIEW_STATUS_RE = re.compile(r"^# Review Status\s*$", re.MULTILINE)
OWNER_RE = re.compile(r"^\|\s*Owner\s*\|\s*(?P<owner>[^|]+?)\s*\|$", re.MULTILINE)
GLOSSARY_BEFORE_REFERENCES_RE = re.compile(
    r"^(?P<indent>\s*)(?:- )?[Gg]lossary(?:\.md)?\n\n?"
    r"(?P=indent)(?:- )?[Rr]eferences(?:\.md)?$",
    re.MULTILINE,
)
# MDG-001 chapter 07: the landing page, References and Glossary use stable unnumbered names.
REFERENCE_PAGE_RE = re.compile(r"^references\.md$")
GLOSSARY_PAGE_RE = re.compile(r"^glossary\.md$")
NUMBERED_REFERENCE_RE = re.compile(r"^\d+-references\.md$")
NUMBERED_GLOSSARY_RE = re.compile(r"^\d+-glossary\.md$")
CHAPTER_RE = re.compile(r"^(?P<number>\d{2})-(?P<slug>[a-z0-9-]+)\.md$")
ARTIFACT_ID_RE = re.compile(
    r"^(?P<id>(?:MDP|MAD|MAC|MEG|MIP|MOP|MDL|MDS|MDG|MRM)-\d{3})", re.IGNORECASE
)

RULES = {
    "metadata-missing": "Every authored page begins with the MDG-001 metadata comment.",
    "metadata-field": "Metadata declares exactly File, Document and Status.",
    "metadata-file-path": "File must match the real repository-relative path.",
    "metadata-status": "Status must be a value from the MDG-001 chapter 03 lifecycle.",
    "metadata-version": "Prose documents carry no Version field; only MIP contracts are versioned.",
    "book-structure": "A specification folder has the required pages and a recognised identifier.",
    "book-consistency": "Every page in a specification declares the same Document and Status.",
    "chapter-sequence": "Numbered chapters run contiguously unless a gap is registered.",
    "chapter-naming": "References and Glossary are unnumbered and last; Document Control is first.",
    "book-stub": "A specification has at least one content chapter.",
    "empty-section": "An Active specification has no empty sections.",
    "owner": "Document Control names an accountable owner.",
    "pages-nav": "A .pages file exists, is ordered correctly and matches the files present.",
    "broken-link": "Every relative link resolves to a file and heading that exist.",
    "cross-reference": "Cross-document references are linked, canonical and correctly targeted.",
    "text-diagram": "Relationship diagrams use Mermaid rather than text fences.",
    "authored-page": "Authored pages carry no review-status blocks or manual navigation.",
    "orphan-artifact": "Generated artifacts under output/ trace back to an authored specification.",
    "catalog": "Every specification appears exactly once in the document catalog.",
}


@dataclass(frozen=True)
class Finding:
    """One rule violation, anchored to a file where possible."""

    path: Optional[str]
    rule: str
    message: str
    line: Optional[int] = None

    def sort_key(self) -> tuple:
        return (self.path or "", self.line or 0, self.rule, self.message)


class Report:
    def __init__(self) -> None:
        self.findings: list[Finding] = []

    def add(
        self,
        path: Optional[Path | str],
        rule: str,
        message: str,
        line: Optional[int] = None,
    ) -> None:
        if isinstance(path, Path):
            path = relative_path(path)
        assert rule in RULES, f"undeclared rule: {rule}"
        self.findings.append(Finding(path, rule, message, line))

    def __bool__(self) -> bool:
        return bool(self.findings)

    def render(self) -> str:
        by_path: dict[str, list[Finding]] = defaultdict(list)
        for finding in self.findings:
            by_path[finding.path or "(repository)"].append(finding)

        lines: list[str] = []
        for path in sorted(by_path):
            lines.append(path)
            for finding in sorted(by_path[path], key=Finding.sort_key):
                location = f":{finding.line}" if finding.line else ""
                lines.append(f"  {path}{location}: [{finding.rule}] {finding.message}")
            lines.append("")

        counts = Counter(finding.rule for finding in self.findings)
        lines.append(f"{len(self.findings)} findings in {len(by_path)} files")
        for rule, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"  {count:>4}  {rule:<20} {RULES[rule]}")
        return "\n".join(lines)


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_chapter_registry() -> dict[str, set[int]]:
    """Read the registry of deliberately retired chapter numbers.

    A gap in a chapter sequence is a defect unless it is recorded here, which forces the
    reason for the gap to be written down rather than inferred years later.
    """
    if not CHAPTER_REGISTRY.is_file():
        return {}

    registry: dict[str, set[int]] = {}
    book: Optional[str] = None
    for raw in CHAPTER_REGISTRY.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if not line.startswith((" ", "\t", "-")):
            book = line.rstrip(":").strip().strip('"').strip("'")
            registry.setdefault(book, set())
        elif book is not None:
            match = re.search(r"\b(\d{1,2})\b", line)
            if match:
                registry[book].add(int(match.group(1)))
    return registry


def authored_markdown_files() -> list[Path]:
    root_pages = [ROOT / name for name in ("README.md", "AGENTS.md", "CLAUDE.md")]
    docs_pages = sorted(
        path for path in DOCS_ROOT.rglob("*.md") if "output" not in path.relative_to(DOCS_ROOT).parts
    )
    return [path for path in root_pages if path.is_file()] + docs_pages


def navigational_lines(text: str):
    """Yield lines that contain authored prose rather than comments or examples."""
    in_fence = False
    in_comment = False
    for number, line in enumerate(text.splitlines(), start=1):
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if "<!--" in line:
            if "-->" not in line.split("<!--", 1)[1]:
                in_comment = True
            continue
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence or re.match(r"^( {4}|\t)", line):
            continue
        yield number, line


def mask_inline_code(line: str) -> str:
    """Preserve offsets while excluding inline code from navigation checks."""
    return re.sub(r"(`+)(.*?)\1", lambda match: " " * len(match.group(0)), line)


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        return target[1:-1]
    if " " in target:
        return target.split(" ", 1)[0]
    return target


def discover_document_catalog(
    metadata: dict[Path, dict[str, str]], report: Report
) -> dict[str, tuple[str, Path, Path]]:
    """Return document ID -> (canonical title, index path, specification folder)."""
    catalog: dict[str, tuple[str, Path, Path]] = {}
    for index in sorted(DOCS_ROOT.rglob("index.md")):
        fields = metadata.get(index)
        if not fields:
            continue
        document_id = fields.get("Document", "")
        if not DOCUMENT_ID_RE.fullmatch(document_id):
            continue
        heading = H1_RE.search(index.read_text(encoding="utf-8"))
        if not heading:
            report.add(index, "catalog", "Specification index is missing an H1 heading")
            continue
        title = re.sub(
            rf"^{re.escape(document_id)}\s*[—-]\s*", "", heading.group("title").strip()
        ).strip()
        if document_id in catalog:
            report.add(index, "catalog", f"Document catalog already contains {document_id}")
            continue
        catalog[document_id] = (title, index, index.parent)
    return catalog


def owning_document(path: Path, catalog: dict[str, tuple[str, Path, Path]]) -> Optional[str]:
    for document_id, (_, _, folder) in catalog.items():
        try:
            path.relative_to(folder)
            return document_id
        except ValueError:
            pass
    return None


def resolve_local_target(path: Path, raw_target: str) -> tuple[Optional[Path], str]:
    target = link_target(raw_target)
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
        return None, ""
    file_part, _, fragment = target.partition("#")
    file_part = unquote(file_part.split("?", 1)[0])
    destination = path if not file_part else (path.parent / file_part).resolve()
    return destination, unquote(fragment)


@lru_cache(maxsize=None)
def heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        visible = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", match.group(1))
        visible = re.sub(r"[`*_~]", "", visible)
        base = slugify(visible, "-")
        count = counts.get(base, 0)
        anchor = base if count == 0 else f"{base}_{count}"
        counts[base] = count + 1
        anchors.add(anchor)
    return anchors


def parse_metadata(path: Path, text: str, report: Report) -> Optional[dict[str, str]]:
    match = METADATA_RE.match(text)
    if not match:
        report.add(path, "metadata-missing", "File does not begin with the metadata comment")
        return None

    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in fields:
            report.add(path, "metadata-field", f"Metadata repeats the {key} field")
        fields[key] = value.strip()

    if "Specification" in fields:
        report.add(
            path, "metadata-field", "Metadata uses Specification; the field is named Document"
        )

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            report.add(path, "metadata-field", f"Metadata is missing the {field} field")

    # MDG-001 chapter 03 retires the document version. Reported separately from other
    # unexpected fields because it is the one every unmigrated specification still carries.
    if "Version" in fields:
        report.add(
            path,
            "metadata-version",
            f"Metadata declares Version: {fields['Version']}; prose documents carry no version. "
            "Remove the field. Only a MIP contract is versioned, inside the document body.",
        )

    for field in sorted(set(fields) - ALLOWED_FIELDS - {"Version", "Specification"}):
        report.add(
            path,
            "metadata-field",
            f"Metadata declares an unexpected field: {field}. "
            f"Permitted fields are {', '.join(REQUIRED_FIELDS)}.",
        )

    declared_file = fields.get("File")
    actual = relative_path(path)
    if declared_file and declared_file != actual:
        report.add(
            path,
            "metadata-file-path",
            f"File declares {declared_file} but the page lives at {actual}",
        )

    status = fields.get("Status")
    document_id = fields.get("Document", "")
    allowed = set(STATUS_VALUES)
    if document_id.startswith("MDP-"):
        allowed |= PROPOSAL_STATUS_VALUES
    if status and status not in allowed:
        report.add(
            path,
            "metadata-status",
            f"Status is {status!r}; expected one of {', '.join(sorted(allowed))}",
        )

    return fields


def page_value(line: str) -> Optional[str]:
    stripped = line.strip()
    if not stripped.startswith("- "):
        return None

    value = stripped[2:].strip()
    if value and value[0] in {"'", '"'} and value.endswith(value[0]):
        value = value[1:-1]
    return value


def find_page(names: list[str], pattern: re.Pattern[str]) -> Optional[str]:
    return next((name for name in names if pattern.fullmatch(name)), None)


def validate_pages_navigation(book: Path, markdown_names: list[str], report: Report) -> None:
    pages = book / ".pages"
    if not pages.is_file():
        report.add(book, "pages-nav", "Specification folder has no .pages navigation file")
        return

    text = pages.read_text(encoding="utf-8")
    entries = [value for line in text.splitlines() if (value := page_value(line))]

    if not text.strip().startswith("title:") and "title:" not in text:
        report.add(pages, "pages-nav", ".pages declares no title")

    reference = find_page(markdown_names, REFERENCE_PAGE_RE)
    glossary = find_page(markdown_names, GLOSSARY_PAGE_RE)
    required = ["index.md", "00-document-control.md", reference, glossary]

    missing = [name for name in required if name and name not in entries]
    if missing:
        report.add(
            pages,
            "pages-nav",
            f".pages omits required pages: {', '.join(missing)}",
        )
        return

    positions = [entries.index(name) for name in required if name]
    if positions != sorted(positions):
        report.add(
            pages,
            "pages-nav",
            ".pages lists index, Document Control, References and Glossary out of order",
        )

    # Entries naming a file that does not exist break navigation silently.
    for entry in entries:
        if entry == "..." or not entry.endswith(".md"):
            continue
        if entry not in markdown_names:
            report.add(pages, "pages-nav", f".pages lists a page that does not exist: {entry}")

    # Without an ellipsis, every page must be listed or it vanishes from the built nav.
    if "..." not in entries:
        for name in sorted(set(markdown_names) - set(entries)):
            report.add(pages, "pages-nav", f".pages does not list {name}")


def validate_chapter_sequence(
    book: Path, markdown_names: list[str], registry: dict[str, set[int]], report: Report
) -> None:
    """Chapter numbers must be contiguous unless a gap is registered."""
    numbers: dict[int, str] = {}
    for name in markdown_names:
        match = CHAPTER_RE.fullmatch(name)
        if not match:
            continue
        number = int(match.group("number"))
        if number in numbers:
            report.add(
                book,
                "chapter-sequence",
                f"Chapter number {number:02d} is used twice: {numbers[number]} and {name}",
            )
            continue
        numbers[number] = name

    if not numbers:
        return

    if 0 not in numbers:
        report.add(book, "chapter-naming", "Specification has no 00-document-control.md chapter")
    elif numbers[0] != "00-document-control.md":
        report.add(
            book,
            "chapter-naming",
            f"Chapter 00 must be 00-document-control.md, found {numbers[0]}",
        )

    registered = registry.get(relative_path(book), set())
    expected = range(min(numbers), max(numbers) + 1)
    gaps = [number for number in expected if number not in numbers and number not in registered]
    if gaps:
        report.add(
            book,
            "chapter-sequence",
            f"Chapter numbering is not sequential; missing {', '.join(f'{n:02d}' for n in gaps)}. "
            f"Renumber, or record the gap in {relative_path(CHAPTER_REGISTRY)} with a reason.",
        )


def validate_chapter_naming(book: Path, markdown_names: list[str], report: Report) -> None:
    """References and Glossary must be unnumbered, and nothing may follow the Glossary."""
    for name in markdown_names:
        if NUMBERED_REFERENCE_RE.fullmatch(name):
            report.add(
                book / name,
                "chapter-naming",
                "References must be unnumbered; rename to references.md and update .pages",
            )
        if NUMBERED_GLOSSARY_RE.fullmatch(name):
            report.add(
                book / name,
                "chapter-naming",
                "Glossary must be unnumbered; rename to glossary.md and update .pages",
            )


def section_bodies(text: str) -> list[tuple[str, int, str]]:
    """Split a page into (heading, line number, body) for each top-level section."""
    without_comments = HTML_COMMENT_RE.sub("", text)
    matches = list(SECTION_RE.finditer(without_comments))
    sections = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(without_comments)
        line = without_comments.count("\n", 0, match.start()) + 1
        sections.append((match.group("title").strip(), line, without_comments[start:end]))
    return sections


def is_empty_body(body: str) -> bool:
    """True when a section carries no substance beyond structural punctuation."""
    stripped = re.sub(r"^---+$", "", body, flags=re.MULTILINE)
    stripped = re.sub(r"^\s*[|>*-]\s*$", "", stripped, flags=re.MULTILINE)
    return not stripped.strip()


def validate_book_content(
    book: Path, markdown_files: list[Path], status: Optional[str], report: Report
) -> None:
    """Catch published stubs and empty sections."""
    content_chapters = [
        path.name
        for path in markdown_files
        if CHAPTER_RE.fullmatch(path.name) and path.name != "00-document-control.md"
    ]
    if not content_chapters:
        report.add(
            book,
            "book-stub",
            "Specification has no content chapters. It contains only Document Control, "
            "References and Glossary, which is a published stub rather than a specification.",
        )

    if status != "Active":
        return

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        # The first H1 is the page title. House style puts a horizontal rule and nothing else
        # beneath it before the first real section, so it is legitimately empty.
        for heading, line, body in section_bodies(text)[1:]:
            if is_empty_body(body):
                report.add(
                    path,
                    "empty-section",
                    f"Section {heading!r} is empty, and the specification is Active",
                    line,
                )


def table_value(text: str, field_names: tuple[str, ...]) -> Optional[str]:
    names = "|".join(re.escape(field) for field in field_names)
    match = re.search(rf"^\|\s*(?:{names})\s*\|\s*([^|]+?)\s*\|$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def validate_book(
    book: Path,
    metadata: dict[Path, dict[str, str]],
    registry: dict[str, set[int]],
    report: Report,
) -> None:
    if not SLUG_RE.fullmatch(book.name):
        report.add(book, "book-structure", "Folder name is not a URL-safe lowercase slug")

    expected_id = "-".join(book.name.split("-")[:2]).upper()
    if not DOCUMENT_ID_RE.fullmatch(expected_id):
        report.add(book, "book-structure", "Folder name carries no recognised document identifier")

    markdown_files = sorted(book.rglob("*.md"))
    markdown_names = [path.name for path in markdown_files]
    reference = find_page(markdown_names, REFERENCE_PAGE_RE)
    glossary = find_page(markdown_names, GLOSSARY_PAGE_RE)
    for required in ("index.md", "00-document-control.md"):
        if required not in markdown_names:
            report.add(book, "book-structure", f"Specification is missing {required}")
    if reference is None:
        report.add(book, "book-structure", "Specification is missing references.md")
    if glossary is None:
        report.add(book, "book-structure", "Specification is missing glossary.md")

    validate_pages_navigation(book, markdown_names, report)
    validate_chapter_sequence(book, markdown_names, registry, report)
    validate_chapter_naming(book, markdown_names, report)

    values: dict[str, set[str]] = {field: set() for field in ("Document", "Status", "Version")}
    for path in markdown_files:
        fields = metadata.get(path)
        if not fields:
            continue
        for field in values:
            if fields.get(field):
                values[field].add(fields[field])

    for field, distinct in values.items():
        # A migrated specification declares no Version at all.
        if field == "Version" and not distinct:
            continue
        if len(distinct) != 1:
            report.add(
                book,
                "book-consistency",
                f"Pages disagree about {field}: {', '.join(sorted(distinct)) or '(none declared)'}",
            )

    document_values = values["Document"]
    if document_values and next(iter(document_values)) != expected_id:
        report.add(
            book,
            "book-consistency",
            f"Metadata declares {next(iter(document_values))} but the folder says {expected_id}",
        )

    status = next(iter(values["Status"])) if len(values["Status"]) == 1 else None
    validate_book_content(book, markdown_files, status, report)

    control = book / "00-document-control.md"
    if not control.is_file() or control not in metadata:
        return

    text = control.read_text(encoding="utf-8")
    fields = metadata[control]
    table_fields = {
        "Document": table_value(text, ("Document", "Document ID")),
        "Status": table_value(text, ("Status",)),
    }
    if "Version" in fields:
        table_fields["Version"] = table_value(text, ("Version",))
    for field, value in table_fields.items():
        if value is None:
            report.add(control, "book-consistency", f"Document Control table has no {field} row")
        elif value != fields.get(field):
            report.add(
                control,
                "book-consistency",
                f"Document Control table says {field} is {value!r} "
                f"but the metadata says {fields.get(field)!r}",
            )

    owner_match = OWNER_RE.search(text)
    if not owner_match:
        report.add(control, "owner", "Document Control table has no Owner row")
    else:
        owner = owner_match.group("owner").strip()
        if owner.lower() in PLACEHOLDER_OWNERS or "<" in owner or ">" in owner:
            report.add(control, "owner", f"Owner is a placeholder: {owner!r}")
        elif owner.lower().startswith("lead "):
            report.add(
                control,
                "owner",
                f"Owner is a role rather than a person or team: {owner!r}",
            )


def validate_local_links(path: Path, text: str, report: Report) -> None:
    for line_number, raw_line in navigational_lines(text):
        line = mask_inline_code(raw_line)
        for match in LINK_RE.finditer(line):
            target = link_target(match.group("target"))
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                continue
            destination, fragment = resolve_local_target(path, target)
            if destination is None:
                continue
            if not destination.exists():
                report.add(path, "broken-link", f"Link target does not exist: {target}", line_number)
                continue
            if fragment and destination.is_file() and destination.suffix.lower() == ".md":
                if fragment not in heading_anchors(destination):
                    report.add(
                        path,
                        "broken-link",
                        f"Link fragment does not match any heading: {target}",
                        line_number,
                    )


def validate_cross_references(
    path: Path,
    text: str,
    catalog: dict[str, tuple[str, Path, Path]],
    report: Report,
) -> None:
    owner = owning_document(path, catalog)
    for line_number, raw_line in navigational_lines(text):
        line = mask_inline_code(raw_line)
        links = list(MARKDOWN_LINK_RE.finditer(line))

        references = list(DOCUMENT_ID_RE.finditer(line))
        for reference_number, reference in enumerate(references):
            document_id = reference.group(0)
            containing_link = next(
                (link for link in links if link.start() <= reference.start() < link.end()), None
            )
            if document_id in catalog:
                if document_id != owner and containing_link is None:
                    report.add(
                        path,
                        "cross-reference",
                        f"Reference to {document_id} is not a relative Markdown hyperlink",
                        line_number,
                    )
            else:
                if containing_link is not None:
                    report.add(
                        path,
                        "cross-reference",
                        f"{document_id} is not published but is linked",
                        line_number,
                    )
                next_reference = (
                    references[reference_number + 1].start()
                    if reference_number + 1 < len(references)
                    else len(line)
                )
                marker_text = line[reference.end():next_reference]
                if not any(marker in marker_text for marker in UNAVAILABLE_MARKERS):
                    report.add(
                        path,
                        "cross-reference",
                        f"{document_id} is not published and lacks a "
                        "'planned; not yet published' or 'deferred; not yet published' marker",
                        line_number,
                    )

        for link in links:
            label = link.group("label")
            destination, _ = resolve_local_target(path, link.group("target"))
            for document_id in DOCUMENT_ID_RE.findall(label):
                if document_id not in catalog:
                    continue
                if destination is None or owning_document(destination, catalog) != document_id:
                    report.add(
                        path,
                        "cross-reference",
                        f"Link labelled {document_id} points outside that specification",
                        line_number,
                    )

            named = NAMED_DOCUMENT_RE.fullmatch(label.strip())
            if named and named.group("id") in catalog:
                canonical_title = catalog[named.group("id")][0]
                if named.group("title").strip() != canonical_title:
                    report.add(
                        path,
                        "cross-reference",
                        f"Link title for {named.group('id')} is "
                        f"{named.group('title').strip()!r}; the catalogued title is "
                        f"{canonical_title!r}",
                        line_number,
                    )


def validate_text_diagrams(path: Path, text: str, report: Report) -> None:
    for match in FENCED_BLOCK_RE.finditer(text):
        if match.group("language").strip() not in {"", "text"}:
            continue

        body = match.group("body")
        line = text.count("\n", 0, match.start()) + 1
        if TEXT_DIAGRAM_ARROW_RE.search(body):
            report.add(
                path, "text-diagram", "Text fence uses diagram arrows; use Mermaid instead", line
            )

        if not TEXT_HIERARCHY_RE.search(body):
            continue

        nonempty = [candidate.strip() for candidate in body.splitlines() if candidate.strip()]
        has_directory = any(candidate.endswith("/") for candidate in nonempty)
        has_files = len(FILE_TREE_ENTRY_RE.findall(body)) >= 2
        if not has_directory and not has_files:
            report.add(
                path,
                "text-diagram",
                "Text fence draws a hierarchy that is not a file tree; use Mermaid instead",
                line,
            )


def validate_generated_artifacts(
    catalog: dict[str, tuple[str, Path, Path]], report: Report
) -> None:
    """Generated output must trace back to an authored specification.

    MDG-001 chapter 07 keeps generated content separate from authored content and forbids it
    becoming authoritative. An artifact whose source has been renamed or deleted is a stale
    document that still looks published.
    """
    if not OUTPUT_ROOT.is_dir():
        return

    for artifact in sorted(path for path in OUTPUT_ROOT.rglob("*") if path.is_file()):
        match = ARTIFACT_ID_RE.match(artifact.name)
        if not match:
            report.add(
                artifact,
                "orphan-artifact",
                "Artifact name carries no document identifier, so its source cannot be traced",
            )
            continue
        document_id = match.group("id").upper()
        if document_id not in catalog:
            report.add(
                artifact,
                "orphan-artifact",
                f"Artifact was generated from {document_id}, which no longer exists. "
                "Delete the artifact or restore its source.",
            )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="validate_docs.py", description="Validate documentation against MDG-001."
    )
    parser.add_argument(
        "--rules", action="store_true", help="List the rules this validator enforces and exit."
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.rules:
        for rule, description in sorted(RULES.items()):
            print(f"{rule:<20} {description}")
        return 0

    report = Report()
    registry = load_chapter_registry()
    markdown_files = sorted(
        path for path in DOCS_ROOT.rglob("*.md") if "output" not in path.relative_to(DOCS_ROOT).parts
    )
    authored_files = authored_markdown_files()
    metadata: dict[Path, dict[str, str]] = {}

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        fields = parse_metadata(path, text, report)
        if fields:
            metadata[path] = fields

        if REVIEW_STATUS_RE.search(text):
            report.add(path, "authored-page", "Page contains a Review Status block")
        if MANUAL_NAV_RE.search(text):
            report.add(path, "authored-page", "Page contains manual previous/next navigation")
        if GLOSSARY_BEFORE_REFERENCES_RE.search(text):
            report.add(path, "chapter-naming", "Page lists Glossary before References")

    catalog = discover_document_catalog(metadata, report)

    for path in authored_files:
        text = path.read_text(encoding="utf-8")
        validate_local_links(path, text, report)
        validate_cross_references(path, text, catalog, report)
        validate_text_diagrams(path, text, report)

    books: list[Path] = []
    for folder in BOOK_ROOTS:
        if not folder.is_dir():
            report.add(folder, "book-structure", "Documentation section directory is missing")
            continue
        books.extend(sorted(path for path in folder.iterdir() if path.is_dir()))

    for book in books:
        validate_book(book, metadata, registry, report)

    catalog_folders = {folder for _, _, folder in catalog.values()}
    for book in books:
        if book not in catalog_folders:
            report.add(book, "catalog", "Specification does not appear in the document catalog")

    book_files = {path for book in books for path in book.rglob("*.md")}
    for path in set(markdown_files) - book_files:
        fields = metadata.get(path)
        heading = H1_RE.search(path.read_text(encoding="utf-8"))
        if fields and heading and fields.get("Document") != heading.group("title").strip():
            report.add(
                path,
                "catalog",
                f"Landing page declares Document {fields.get('Document')!r} "
                f"but its H1 is {heading.group('title').strip()!r}",
            )

    validate_generated_artifacts(catalog, report)

    if report:
        print(report.render(), file=sys.stderr)
        print(
            "\nDocumentation validation FAILED. Every rule above is defined by MDG-001; "
            "run --rules to see what each one enforces.",
            file=sys.stderr,
        )
        return 1

    print(
        f"Documentation validation passed ({len(authored_files)} authored Markdown pages, "
        f"{len(catalog)} catalogued specifications)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
