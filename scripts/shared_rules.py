#!/usr/bin/env python3
"""Hold the shared block of every repository's CLAUDE.md identical.

The rules every Mosaic repository shares were eleven hand-kept copies in four
variants. They had already drifted: two were truncated, one was abridged to
bare bullets with every *reason* deleted, and that same copy had lost a rule
outright — the prohibition on running the toolchain on the host, which its
siblings all carry. Nothing anywhere reported it, because nothing compared them.

So the block is generated into each file between two markers, and ``--check``
fails when a copy differs from the source. That is the same shape as the
`contracts` drift guard: the artefact is output, and the guard is what makes
"generated" mean something rather than describing an intention.

Only the region between the markers is managed. Everything outside is the
repository's own — which is the division the audit argued for: shared rules are
identical everywhere by construction, and local facts belong only where someone
edits them alongside the code.

Usage:
    python scripts/shared_rules.py --write            # update every repository
    python scripts/shared_rules.py --check            # fail if any copy differs
    python scripts/shared_rules.py --check --repo sdk
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

BEGIN = "<!-- shared-rules:begin -->"
END = "<!-- shared-rules:end -->"

REPOS = [
    "architecture", "platform", "supervisor", "sdk", "contracts", "web", "registry",
    "module-stremio-addons", "module-aiostreams", "module-cinemeta",
    "module-fanart-tv", "module-remote-playback", "module-tmdb",
]


def block(source: Path) -> str:
    body = source.read_text().strip()
    return f"{BEGIN}\n{body}\n{END}"


def apply(text: str, rendered: str) -> str | None:
    """Replace the managed region. None when the file carries no markers."""
    start = text.find(BEGIN)
    end = text.find(END)
    if start == -1 or end == -1 or end < start:
        return None
    return text[:start] + rendered + text[end + len(END) :]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, default=Path("shared/repository-rules.md"))
    ap.add_argument("--fleet", type=Path, default=Path(".."), help="directory holding the repositories")
    ap.add_argument("--repo", action="append", default=None, help="limit to these repositories")
    ap.add_argument("--write", action="store_true", help="update the files (default is --check)")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    rendered = block(args.source)
    repos = args.repo or REPOS
    stale: list[str] = [];  missing: list[str] = [];  updated: list[str] = []

    for name in repos:
        path = args.fleet / name / "CLAUDE.md"
        if not path.exists():
            missing.append(f"{name}: no CLAUDE.md")
            continue
        text = path.read_text()
        new = apply(text, rendered)
        if new is None:
            missing.append(f"{name}: CLAUDE.md carries no {BEGIN} / {END} markers")
            continue
        if new == text:
            continue
        if args.write:
            path.write_text(new)
            updated.append(name)
        else:
            stale.append(name)

    for line in missing:
        print(f"  MISSING  {line}")
    for name in updated:
        print(f"  updated  {name}")
    for name in stale:
        print(f"  STALE    {name}: shared block differs from {args.source}")

    if args.write:
        print(f"\n{len(updated)} updated, {len(repos) - len(updated) - len(missing)} already current")
        sys.exit(1 if missing else 0)

    if stale or missing:
        print(f"\n{len(stale)} stale, {len(missing)} missing — run scripts/shared_rules.py --write")
        sys.exit(1)
    print(f"shared block identical across {len(repos) - len(missing)} repositories")


if __name__ == "__main__":
    main()
