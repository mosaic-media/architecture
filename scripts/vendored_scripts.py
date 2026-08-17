#!/usr/bin/env python3
"""Keep the vendored copies of the record tools identical to this repository's.

Twelve repositories carry a copy of ``adr_lint.py``, most also ``adr_index.py``,
and **each one runs its copy in its own gate**. That is the arrangement working
as intended — a repository's gate should not depend on a sibling being checked
out — and it has the failure mode every copy has: edit the source here, and
eleven gates keep running the version from before the edit, reporting clean
against a rule that has moved.

That is not hypothetical. Widening the lint's file-suffix list to include
``.mod`` found four unqualified citations that had survived the whole migration
inside ``go.mod`` files. The fix landed here, and for three commits the other
eleven copies still could not see a ``.mod`` file — so eleven gates would have
gone on reporting zero for exactly the citations the change existed to catch.

Two verbs, check and write:

    python scripts/vendored_scripts.py --fleet ..            # check every copy
    python scripts/vendored_scripts.py --fleet .. --write    # re-vendor them

**The check can only run where the siblings are on disk.** In CI only this
repository is checked out, so this cannot be a CI gate here the way the lint is;
it is a local check, run when a tool changes. A repository cannot check its own
copy either, having nothing to compare against. That is a real limit, stated
rather than papered over.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# The tools other repositories vendor. `adr_rewrite.py` is deliberately absent:
# it is a migration tool, run once from here, and nothing else should carry it.
VENDORED = ("adr_lint.py", "adr_index.py")

REPOS = (
    "platform", "supervisor", "sdk", "contracts", "web", "registry",
    "module-stremio-addons", "module-aiostreams", "module-cinemeta",
    "module-fanart-tv", "module-remote-playback", "module-tmdb",
)

HEADER = (
    "# VENDORED from architecture/scripts/{name} — do not edit here.\n"
    "# The source of truth is the architecture repository."
)


def vendored_form(canonical: str, name: str) -> str:
    """The canonical text with the vendoring header injected after the shebang.

    The header is added here rather than kept in each copy, so a copy differs
    from the source in exactly one known way and any other difference is drift.
    """
    lines = canonical.split("\n")
    return "\n".join([lines[0], HEADER.format(name=name)] + lines[1:])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fleet", type=Path, required=True,
                    help="directory holding the sibling repositories")
    ap.add_argument("--source", type=Path, default=Path("scripts"),
                    help="this repository's scripts directory")
    ap.add_argument("--write", action="store_true",
                    help="re-vendor differing copies instead of failing on them")
    args = ap.parse_args()

    stale: list[str] = []
    missing: list[str] = []
    checked = 0

    for repo in REPOS:
        for name in VENDORED:
            src = args.source / name
            if not src.exists():
                sys.exit(f"no such tool: {src}")
            dst = args.fleet / repo / "scripts" / name
            if not dst.exists():
                # Not every repository vendors every tool — a repository owning
                # no records needs no index generator. Absence is a fact, not a
                # failure, so it is reported and never written.
                missing.append(f"{repo}/scripts/{name}")
                continue
            checked += 1
            want = vendored_form(src.read_text(), name)
            if dst.read_text() == want:
                continue
            stale.append(f"{repo}/scripts/{name}")
            if args.write:
                dst.write_text(want)

    print(f"checked {checked} vendored copies across {len(REPOS)} repositories")
    if missing:
        print(f"not vendored ({len(missing)}): {', '.join(missing)}")

    if not stale:
        print("every vendored copy matches its source")
        sys.exit(0)

    verb = "re-vendored" if args.write else "STALE"
    print(f"{verb} ({len(stale)}):")
    for path in stale:
        print(f"  {path}")
    if args.write:
        print("\nCommit each repository separately; they are independent in git.")
        sys.exit(0)
    print("\nRun with --write, then commit each repository separately.")
    sys.exit(1)


if __name__ == "__main__":
    main()
