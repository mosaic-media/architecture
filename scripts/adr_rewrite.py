#!/usr/bin/env python3
"""Rewrite `ADR NNNN` citations to the qualified, linked form.

Driven by a mapping of old number to new home, so it never guesses. A record
that is not in the mapping is left alone and reported, because the alternative
— assuming a record stayed put — is how a rewrite silently repoints a citation
at a different decision.

The form written depends on what the file can express, which is the whole
reason this is a tool and not a `sed`:

* **Markdown, same repository** — ``[platform#12](0012-slug.md)``
* **Markdown, another repository** — ``[platform#12](https://github.com/…)``
* **Go doc comment** — the link-reference form Go renders:
  ``// [platform#12]: https://github.com/…`` appended to the comment block
* **Anything else** — ``platform#12`` bare, because no URL is possible in a
  test name or a YAML comment and a broken link there helps nobody.

Existing Markdown links are rewritten in place rather than nested: a citation
already written ``[ADR 0012](0012-slug.md)`` becomes ``[platform#12](…)``,
never ``[[platform#12](…)](…)``.

Usage:
    python scripts/adr_rewrite.py --map mapping.tsv --root ../platform --repo platform
    python scripts/adr_rewrite.py --map mapping.tsv --root . --repo architecture --apply
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

GITHUB = "https://github.com/mosaic-media"

SKIP_DIRS = {".git", "node_modules", "vendor", "site", "dist", "build", "__pycache__", ".venv"}
SKIP_NAMES = {"package-lock.json", "go.sum"}
TEXT_SUFFIXES = {
    ".md", ".go", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".py", ".sh", ".yml", ".yaml",
    ".json", ".proto", ".toml", ".txt", ".sql", ".css", ".html",
    # Extensionless files carry citations too — Dockerfile, .gitignore. This set
    # must stay equal to the lint's, or the lint reports what the rewriter
    # cannot reach and the ratchet stops at a floor nobody can lower.
    "",
}

# `[ADR 0012](anything)` — an existing link, whose target is replaced wholesale.
LINKED = re.compile(r"\[ADR[\s-]?(\d{1,4})\]\([^)]*\)")
# A bare `ADR 0012` / `ADR-0012` / `ADR0012` not already consumed above.
BARE = re.compile(r"\bADR[\s-]?(\d{1,4})\b")
# An already-qualified citation of a record that is about to move *again*.
# A repository migrated in an earlier phase carries links to records still in
# their old home; when those move, the links break. Phase N's outbound links
# are phase N+1's work, which the pilot found the hard way.
def requalify_pattern(repo: str) -> re.Pattern:
    return re.compile(r"\[" + re.escape(repo) + r"#(\d+)\]\([^)]*\)|\b" + re.escape(repo) + r"#(\d+)\b")
# The number buried in an identifier — `TestRoleClassTableMatchesADR0063`. It
# cannot be rewritten: `platform#42` is not a legal identifier in any language
# here. So it is reported instead, because a test asserting against a record
# number that no longer exists stays permanently green.
IN_IDENTIFIER = re.compile(r"(?<=\w)ADR[\s-]?(\d{1,4})\b")


@dataclass(frozen=True)
class Home:
    repo: str
    number: int
    filename: str

    def label(self) -> str:
        return f"{self.repo}#{self.number}"

    def url(self) -> str:
        return f"{GITHUB}/{self.repo}/blob/main/docs/adr/{self.filename}"


def is_generated(rel: Path, patterns: list[str]) -> bool:
    """True when *rel* is declared generated — by exact path, glob, or parent directory."""
    text = str(rel)
    for pattern in patterns:
        if text == pattern or rel.match(pattern):
            return True
        if text.startswith(pattern.rstrip("/") + "/"):
            return True
    return False


def load_mapping(path: Path) -> dict[int, Home]:
    """old_number <TAB> new_repo <TAB> new_number <TAB> new_filename."""
    mapping: dict[int, Home] = {}
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 4:
            raise SystemExit(f"{path}:{lineno}: expected 4 tab-separated fields, got {len(parts)}")
        old, repo, number, filename = parts
        mapping[int(old)] = Home(repo, int(number), filename)
    return mapping


def rewrite_markdown(
    text: str, mapping: dict[int, Home], repo: str, from_dir: Path, adr_dir: Path,
    requalify: str | None = None,
) -> tuple[str, Counter]:
    hits: Counter = Counter()

    def link_for(home: Home) -> str:
        if home.repo != repo:
            return f"[{home.label()}]({home.url()})"
        # Relative to the *citing file*, not to the record directory. A README
        # at the repository root and a record inside docs/adr/ do not share a
        # parent, and a bare filename resolves only from the second.
        # Both sides resolved, or neither: resolving only one of them walks a
        # symlink out of the repository. /home/user/supervisor is a link to
        # /workspace/supervisor, and the mismatch produced ../../../../../workspace/…
        # in four committed links — paths that work here and 404 on GitHub.
        target = os.path.relpath(adr_dir.resolve(), from_dir.resolve())
        target = os.path.join(target, home.filename) if target != "." else home.filename
        return f"[{home.label()}]({target})"

    def on_linked(m: re.Match) -> str:
        home = mapping.get(int(m.group(1)))
        if home is None:
            hits["unmapped"] += 1
            return m.group(0)
        hits["linked"] += 1
        return link_for(home)

    def on_bare(m: re.Match) -> str:
        home = mapping.get(int(m.group(1)))
        if home is None:
            hits["unmapped"] += 1
            return m.group(0)
        hits["bare"] += 1
        return link_for(home)

    # Requalification runs FIRST, and the order is load-bearing. Run it after,
    # and a citation the bare pass has just rewritten to `architecture#4` is
    # re-read as though 4 were an *old* record number and mapped a second time.
    # The two number spaces are different and only collide once a repository has
    # been renumbered — which is why the pilot did not catch this.
    if requalify:
        def on_requalify(m: re.Match) -> str:
            number = int(m.group(1) or m.group(2))
            home = mapping.get(number)
            # Skip only when nothing changed. A record that stays in the same
            # repository can still be renumbered — architecture#22 became
            # architecture#1 — and skipping on repository alone leaves a
            # citation naming a number that no longer exists.
            if home is None or (home.repo == requalify and home.number == number):
                return m.group(0)
            hits["requalified"] += 1
            return link_for(home)
        text = requalify_pattern(requalify).sub(on_requalify, text)
    text = LINKED.sub(on_linked, text)
    text = BARE.sub(on_bare, text)
    return text, hits


def rewrite_plain(
    text: str, mapping: dict[int, Home], requalify: str | None = None
) -> tuple[str, Counter]:
    """Everything that is not Markdown: the label alone, no link.

    Go, TypeScript, YAML and shell carry these in comments and test names,
    where a Markdown link would be noise. The lint resolves the label against
    the index instead.
    """
    hits: Counter = Counter()

    def on_bare(m: re.Match) -> str:
        home = mapping.get(int(m.group(1)))
        if home is None:
            hits["unmapped"] += 1
            return m.group(0)
        hits["bare"] += 1
        return home.label()

    if requalify:
        def on_requalify(m: re.Match) -> str:
            number = int(m.group(1) or m.group(2))
            home = mapping.get(number)
            # Skip only when nothing changed. A record that stays in the same
            # repository can still be renumbered — architecture#22 became
            # architecture#1 — and skipping on repository alone leaves a
            # citation naming a number that no longer exists.
            if home is None or (home.repo == requalify and home.number == number):
                return m.group(0)
            hits["requalified"] += 1
            return home.label()
        text = requalify_pattern(requalify).sub(on_requalify, text)
    text = BARE.sub(on_bare, text)
    return text, hits


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--map", type=Path, required=True, help="TSV: old, repo, number, filename")
    ap.add_argument("--root", type=Path, required=True, help="repository to rewrite")
    ap.add_argument("--repo", required=True, help="its name, for deciding relative vs absolute links")
    ap.add_argument("--apply", action="store_true", help="write the changes (default is a dry run)")
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument(
        "--generated", action="append", default=[],
        help="path or glob, relative to --root, that is generated output. Repeatable. "
             "Rewriting generated output makes the drift guard fail and loses the change "
             "on the next regeneration, so these are named and refused. Take the list from "
             "the repository's own guard — contracts declares its set in "
             "scripts/check-generated.sh — rather than guessing from filenames: ts/ui.ts is "
             "generated and buf.gen.yaml is not, and no naming rule gets both right.",
    )
    ap.add_argument(
        "--requalify", default=None, metavar="REPO",
        help="also rewrite citations already qualified against REPO, whose records are "
             "moving again. A repository migrated in an earlier phase links to records "
             "still in their old home, and those links break when they move.",
    )
    ap.add_argument("--show", type=int, default=10)
    ap.add_argument(
        "--adr-dir", type=Path, default=Path("docs/adr"),
        help="where this repository's records live, relative to --root. Used to make a "
             "same-repository Markdown link relative to the file doing the citing.",
    )
    args = ap.parse_args()

    mapping = load_mapping(args.map)
    totals: Counter = Counter()
    changed: list[tuple[str, int]] = []
    generated: list[str] = []
    suspect: list[str] = []
    identifiers: list[str] = []

    for path in sorted(args.root.rglob("*")):
        if not path.is_file() or path.name in SKIP_NAMES:
            continue
        rel = path.relative_to(args.root)
        if SKIP_DIRS & set(rel.parts) or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(rel.match(p) for p in args.exclude):
            continue
        try:
            text = path.read_text()
        except (UnicodeDecodeError, OSError):
            continue
        # Cheap early-out. It must also consider the requalify prefix: a file
        # migrated in an earlier phase carries only qualified citations and no
        # longer contains the literal "ADR" at all, so testing for that alone
        # skips exactly the files requalification exists to fix.
        if "ADR" not in text and not (args.requalify and f"{args.requalify}#" in text):
            continue

        # A generated file's citations came from its source; change them there
        # and regenerate.
        if is_generated(rel, args.generated):
            if BARE.search(text):
                generated.append(str(rel))
            continue

        # Not declared generated, but it looks it. Better a false alarm than a
        # rewritten binding nobody noticed until the guard went red.
        if BARE.search(text) and (".gen." in path.name or rel.parts[0].startswith("gen")):
            suspect.append(str(rel))

        for m in IN_IDENTIFIER.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            identifiers.append(f"{rel}:{line}: {m.group(0)}")

        if path.suffix == ".md":
            new, hits = rewrite_markdown(
                text, mapping, args.repo, path.parent,
                (args.root / args.adr_dir).resolve(), args.requalify,
            )
        else:
            new, hits = rewrite_plain(text, mapping, args.requalify)
        totals.update(hits)
        if new != text:
            changed.append((str(rel), hits["linked"] + hits["bare"] + hits["requalified"]))
            if args.apply:
                path.write_text(new)

    verb = "rewrote" if args.apply else "would rewrite"
    moved_total = totals["linked"] + totals["bare"] + totals["requalified"]
    print(f"{args.repo}: {verb} {moved_total} citations in {len(changed)} files")
    print(f"  already-linked rewritten in place : {totals['linked']}")
    print(f"  bare citations                    : {totals['bare']}")
    print(f"  requalified from an earlier phase : {totals['requalified']}")
    print(f"  left alone, not in the mapping    : {totals['unmapped']}")
    for rel, n in sorted(changed, key=lambda x: -x[1])[: args.show]:
        print(f"    {n:5}  {rel}")
    if len(changed) > args.show:
        print(f"    … and {len(changed) - args.show} more files")
    if generated:
        print(f"\n  {len(generated)} generated file(s) carry citations and were NOT touched —")
        print("  change them at source and regenerate:")
        for rel in generated[: args.show]:
            print(f"    {rel}")
    if suspect:
        print(f"\n  {len(suspect)} file(s) look generated but were not declared with --generated,")
        print("  and were rewritten. Check the repository's drift guard:")
        for rel in suspect[: args.show]:
            print(f"    {rel}")
    if identifiers:
        print(f"\n  {len(identifiers)} citation(s) are inside an identifier and CANNOT be rewritten —")
        print("  `platform#42` is not a legal identifier. Rename these by hand or accept that")
        print("  they name a number that no longer resolves:")
        for line in identifiers[: args.show]:
            print(f"    {line}")
    if totals["unmapped"]:
        print("\n  A citation left alone names a record absent from the mapping. Add it, or")
        print("  confirm deliberately that the record has not moved.")
    if not args.apply:
        print("\nDry run. Pass --apply to write.")


if __name__ == "__main__":
    main()
