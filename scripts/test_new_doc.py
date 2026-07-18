"""Tests for the specification scaffolder."""

from __future__ import annotations

import pytest

import new_doc
from new_doc import ScaffoldError


# --------------------------------------------------------------------------- slugs


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        ("Module Signing Policy", "module-signing-policy"),
        ("  Leading And Trailing  ", "leading-and-trailing"),
        ("Multiple   Inner   Spaces", "multiple-inner-spaces"),
        ("Platform–SDK Contract Protocol", "platform-sdk-contract-protocol"),
        ("Observability & Diagnostics", "observability-diagnostics"),
        ("Storage (v2) Architecture", "storage-v2-architecture"),
        ("MOS Cache: Retention", "mos-cache-retention"),
        ("Café Résumé", "cafe-resume"),
        ("UV Light Frame Protocol", "uv-light-frame-protocol"),
    ],
)
def test_slugify_produces_url_safe_slugs(title, expected):
    assert new_doc.slugify(title) == expected


@pytest.mark.parametrize("title", ["", "   ", "!!!", "—"])
def test_slugify_rejects_titles_with_no_usable_slug(title):
    with pytest.raises(ScaffoldError):
        new_doc.slugify(title)


def test_slugify_output_satisfies_the_validator_slug_rule():
    slug = new_doc.slugify("Platform–SDK  Contract (v2) & Beyond!")
    assert new_doc.SLUG_RE.fullmatch(slug)
    assert not slug.startswith("-") and not slug.endswith("-")
    assert "--" not in slug


# ------------------------------------------------------------------- id allocation


def make_folders(destination, names):
    destination.mkdir(parents=True, exist_ok=True)
    for name in names:
        (destination / name).mkdir()


def test_next_number_starts_at_one_when_empty(tmp_path):
    assert new_doc.next_number(tmp_path / "absent", "mad") == 1

    empty = tmp_path / "empty"
    empty.mkdir()
    assert new_doc.next_number(empty, "mad") == 1


def test_next_number_follows_the_highest_existing(tmp_path):
    make_folders(tmp_path, ["mad-001-first", "mad-002-second"])
    assert new_doc.next_number(tmp_path, "mad") == 3


def test_next_number_does_not_refill_gaps(tmp_path):
    # meg jumps 010 -> 014 in this repository. A freed number must never be reissued,
    # because identifiers are permanent references.
    make_folders(tmp_path, ["meg-001-a", "meg-010-b", "meg-014-c"])
    assert new_doc.next_number(tmp_path, "meg") == 15


def test_next_number_counts_only_its_own_type(tmp_path):
    make_folders(tmp_path, ["mac-001-a", "mad-001-b", "mad-002-c", "mdp-009-d"])
    assert new_doc.next_number(tmp_path, "mad") == 3
    assert new_doc.next_number(tmp_path, "mac") == 2
    assert new_doc.next_number(tmp_path, "mdp") == 10


def test_next_number_ignores_files_and_malformed_folders(tmp_path):
    make_folders(tmp_path, ["mad-001-real", "mad-2-short", "madness-003-x", "mad-003"])
    (tmp_path / "mad-009-not-a-folder.md").write_text("", encoding="utf-8")
    assert new_doc.next_number(tmp_path, "mad") == 2


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("mad-003", 3), ("MAD-003", 3), ("003", 3), ("3", 3), (" mad-012 ", 12)],
)
def test_parse_id_accepts_the_documented_forms(raw, expected):
    assert new_doc.parse_id(raw, "mad") == expected


@pytest.mark.parametrize("raw", ["meg-003", "mad_003", "mad-", "abc", "0", "mad-0000"])
def test_parse_id_rejects_bad_input(raw):
    with pytest.raises(ScaffoldError):
        new_doc.parse_id(raw, "mad")


# ------------------------------------------------------------------------- dry run


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    """Point the scaffolder at a throwaway tree that mirrors the real layout."""
    docs = tmp_path / "docs"
    templates = tmp_path / "templates"
    destination = docs / new_doc.DESTINATIONS["mad"]
    destination.mkdir(parents=True)
    (destination / ".pages").write_text(
        "title: Architecture\narrange:\n  - index.md\n  - mad-001-existing\n",
        encoding="utf-8",
    )
    (destination / "mad-001-existing").mkdir()

    template = templates / "mad"
    template.mkdir(parents=True)
    for name in ("index.md", "00-document-control.md", "01-context.md", "references.md", "glossary.md"):
        template.joinpath(name).write_text(
            "<!--\n"
            "File: docs/engineering/architecture/mad-nnn-subject-slug/PLACE\n"
            "Document: MAD-NNN\n"
            "Status: Draft\n"
            "-->\n\n"
            "# MAD-NNN — Decision Title\n\n"
            "| Document | MAD-NNN |\n",
            encoding="utf-8",
        )

    monkeypatch.setattr(new_doc, "ROOT", tmp_path)
    monkeypatch.setattr(new_doc, "DOCS_ROOT", docs)
    monkeypatch.setattr(new_doc, "TEMPLATES_ROOT", templates)
    return tmp_path, destination


def test_dry_run_writes_nothing(sandbox, capsys):
    tmp_path, destination = sandbox
    before = sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*"))

    assert new_doc.main(["--type", "mad", "--title", "Module Signing Policy", "--dry-run"]) == 0

    after = sorted(path.relative_to(tmp_path).as_posix() for path in tmp_path.rglob("*"))
    assert before == after
    assert not (destination / "mad-002-module-signing-policy").exists()

    out = capsys.readouterr().out
    assert "MAD-002 — Module Signing Policy" in out
    assert "Would create docs/engineering/architecture/mad-002-module-signing-policy/" in out
    assert "would write index.md" in out
    assert "Nothing was written." in out


def test_dry_run_leaves_the_parent_pages_untouched(sandbox):
    _, destination = sandbox
    pages = destination / ".pages"
    before = pages.read_text(encoding="utf-8")

    new_doc.main(["--type", "mad", "--title", "Module Signing Policy", "--dry-run"])

    assert pages.read_text(encoding="utf-8") == before


def test_real_run_writes_stamped_files(sandbox):
    _, destination = sandbox

    assert new_doc.main(["--type", "mad", "--title", "Module Signing Policy"]) == 0

    folder = destination / "mad-002-module-signing-policy"
    index = (folder / "index.md").read_text(encoding="utf-8")
    assert index.startswith(
        "<!--\n"
        "File: docs/engineering/architecture/mad-002-module-signing-policy/index.md\n"
        "Document: MAD-002\n"
        "Status: Draft\n"
        "-->"
    )
    assert "# MAD-002 — Module Signing Policy" in index
    assert "| Document | MAD-002 |" in index
    assert "MAD-NNN" not in index
    assert "Decision Title" not in index

    pages = (folder / ".pages").read_text(encoding="utf-8")
    assert pages.splitlines()[0] == "title: Module Signing Policy"
    assert pages.splitlines()[2:] == [
        "  - index.md",
        "  - 00-document-control.md",
        "  - 01-context.md",
        "  - references.md",
        "  - glossary.md",
    ]

    parent = (destination / ".pages").read_text(encoding="utf-8")
    assert "  - mad-002-module-signing-policy" in parent


def test_refuses_to_overwrite_an_existing_folder(sandbox, capsys):
    _, destination = sandbox
    (destination / "mad-002-module-signing-policy").mkdir()

    assert new_doc.main(["--type", "mad", "--title", "Module Signing Policy", "--id", "mad-002"]) == 1
    assert "already exists" in capsys.readouterr().err


def test_explicit_id_is_honoured(sandbox):
    _, destination = sandbox

    assert new_doc.main(["--type", "mad", "--title", "Module Signing Policy", "--id", "mad-007"]) == 0
    assert (destination / "mad-007-module-signing-policy").is_dir()
