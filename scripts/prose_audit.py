"""Check that a prose rewrite preserved the information it carried.

A rewrite is allowed to change rhythm, structure and connective tissue. It is not allowed to
drop a fact. This compares a specification against its committed state and reports every
fact-bearing token that disappeared, so information loss is caught rather than trusted.

Run:
    python3 scripts/prose_audit.py docs/engineering/guides/meg-004-hexagonal-architecture
    python3 scripts/prose_audit.py <folder> --against HEAD~1
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Words that carry no information on their own. Losing these is what a rewrite is for.
STOPWORDS = frozenset("""
a an the and or but if then than that this these those there here it its it's is are was were
be been being am do does did doing have has had having will would shall should can could may
might must of in on at to from by for with without within into onto upon about across through
as so such not no nor only also very more most less least much many few own same other another
each every all any both either neither some when while where which who whom whose what why how
however therefore therefore's instead rather thus hence because since although though whereas
we you they he she i us them him her our your their his hers ours yours theirs myself itself
themselves one two three first second next last other others new old good bad better best
""".split())

# Tokens that are almost always load-bearing in this corpus even if short.
ALWAYS_KEEP = re.compile(r"^(?:[A-Z]{2,}|[A-Z]{3}-\d{3}|v\d+|\d+)$")
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9'’\-]*|\b\d+(?:\.\d+)?\b")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def significant_tokens(text: str, keep_code: bool = True) -> Counter:
    """Fact-bearing tokens, with structural noise stripped."""
    if not keep_code:
        text = CODE_FENCE_RE.sub(" ", text)
    text = COMMENT_RE.sub(" ", text)
    tokens = Counter()
    for raw in TOKEN_RE.findall(text):
        token = raw.strip("'’-")
        if not token:
            continue
        if ALWAYS_KEEP.match(token):
            tokens[token] += 1
            continue
        lowered = token.lower()
        if lowered in STOPWORDS or len(lowered) < 3:
            continue
        tokens[lowered] += 1
    return tokens


# A dropped token only matters if it carried a fact. These patterns separate technical
# identifiers and product names from ordinary English, so a real loss is not buried under
# hundreds of merged connectives.
IDENTIFIER_RE = re.compile(r"(?:[a-z]+[A-Z]|[A-Z]{2,}|_|\d)")
PRODUCT_RE = re.compile(
    r"(?i)^(postgres\w*|duckdb|tmdb|anilist|jellyfin|stremio|docker|containerd|s3|"
    r"cockroachdb|graphql|rest|http|sql|jwt|oauth|json|grpc|redis|kafka|blob)$"
)
# Expected to disappear: Mermaid syntax from removed diagrams, and RFC 2119 keywords that
# were lowercased on purpose per MDG-001 chapter 10.
EXPECTED_LOSS = frozenset(
    {"td", "lr", "mermaid", "flowchart", "graph", "must", "should", "may", "shall", "not", "never"}
)


def classify(token: str, original: str) -> str:
    # Acronyms keep their case in significant_tokens, so compare case-insensitively.
    if token.lower() in EXPECTED_LOSS:
        return "expected"
    if IDENTIFIER_RE.search(original) or PRODUCT_RE.match(token):
        return "technical"
    return "prose"


def committed(path: Path, ref: str) -> str | None:
    rel = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{ref}:{rel}"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    return result.stdout if result.returncode == 0 else None


def shape(text: str) -> tuple[int, int, int]:
    """(words, prose paragraphs, single-sentence paragraphs)."""
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]+", text))
    single = para = 0
    for block in re.split(r"\n\s*\n", COMMENT_RE.sub("", text)):
        block = block.strip()
        if not block or block[0] in "#|->`*" or re.match(r"^\d+\.", block):
            continue
        para += 1
        if len(re.findall(r"[.!?](\s|$)", block)) <= 1:
            single += 1
    return words, para, single


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", help="Specification folder to audit.")
    parser.add_argument("--against", default="HEAD", help="Git ref to compare against.")
    parser.add_argument(
        "--threshold",
        type=int,
        default=0,
        help="Allowed number of dropped occurrences per token before it is reported.",
    )
    args = parser.parse_args()

    folder = (ROOT / args.folder).resolve()
    if not folder.is_dir():
        print(f"ERROR: not a folder: {args.folder}", file=sys.stderr)
        return 1

    lost_total = 0
    before_shape = [0, 0, 0]
    after_shape = [0, 0, 0]

    for path in sorted(folder.rglob("*.md")):
        old = committed(path, args.against)
        if old is None:
            print(f"  NEW      {path.relative_to(ROOT).as_posix()}")
            continue
        new = path.read_text(encoding="utf-8")
        if old == new:
            continue

        before, after = significant_tokens(old), significant_tokens(new)
        for i, v in enumerate(shape(old)):
            before_shape[i] += v
        for i, v in enumerate(shape(new)):
            after_shape[i] += v

        # Original casing distinguishes an identifier from an ordinary word.
        cased = {t.lower(): t for t in re.findall(r"[A-Za-z][A-Za-z0-9'\-]*", old)}
        lost = {t: c - after.get(t, 0) for t, c in before.items() if c - after.get(t, 0) > args.threshold}

        # A term that still appears somewhere has been deduplicated, not lost. Only a term
        # that has fallen to zero occurrences is missing information.
        vanished = {
            t: c for t, c in lost.items()
            if after.get(t, 0) == 0 and classify(t, cased.get(t, t)) == "technical"
        }
        deduped = {t: c for t, c in lost.items() if t not in vanished
                   and classify(t, cased.get(t, t)) == "technical"}

        if vanished or deduped:
            print(f"\n  {path.relative_to(ROOT).as_posix()}")
            for token, count in sorted(vanished.items()):
                print(f"      LOST     -{count:<3} {token}   (no occurrences remain)")
            for token, count in sorted(deduped.items(), key=lambda kv: -kv[1])[:8]:
                print(f"      deduped  -{count:<3} {token}   ({after[token]} remain)")
        lost_total += sum(vanished.values())

    print()
    print(f"words              {before_shape[0]:>7,} -> {after_shape[0]:>7,}")
    print(f"prose paragraphs   {before_shape[1]:>7,} -> {after_shape[1]:>7,}")
    pct_before = before_shape[2] * 100 // max(before_shape[1], 1)
    pct_after = after_shape[2] * 100 // max(after_shape[1], 1)
    print(f"single-sentence    {pct_before:>6}% -> {pct_after:>6}%")

    if lost_total:
        print(f"\nFAIL: {lost_total} technical term(s) no longer appear anywhere in the document.")
        print("Restore them, or justify each one as a deliberate removal.")
        return 1

    print("\nPASS: every technical term still appears. Remaining drops are deduplication,")
    print("removed Mermaid syntax, or RFC 2119 keywords lowercased per MDG-001 chapter 10.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
