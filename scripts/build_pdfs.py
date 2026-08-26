#!/usr/bin/env python3
"""Render the built MkDocs site to PDF, one file per page.

Serves ``site/`` locally and drives headless Chromium's print-to-PDF, so
Mermaid diagrams render as diagrams rather than as code blocks — they are
drawn by JavaScript in the browser, which is why a Markdown-to-PDF
converter cannot produce them.

Usage:
    python scripts/build_pdfs.py            # after `mkdocs build`
    python scripts/build_pdfs.py --out dist

Requires ``playwright`` and its Chromium browser:
    python -m pip install playwright
    python -m playwright install --with-deps chromium
"""

from __future__ import annotations

import argparse
import asyncio
import re
import threading
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# The top-level pages, by hand. Adding one is a deliberate edit here as well as
# in `nav:`, and that friction is the point — a fifth page needs justifying.
TOP_LEVEL = {
    "": "Mosaic.pdf",
    "architecture/": "Mosaic-Architecture.pdf",
    "roadmap/": "Mosaic-Roadmap.pdf",
    "unreachable-capability/": "Mosaic-Unreachable-Capability.pdf",
    "work-graph/": "Mosaic-Work-Graph.pdf",
}

# Words that are acronyms rather than words, so the PDF filename reads
# `sdk#1-SDK-...` rather than `sdk#1-Sdk-...`.
ACRONYMS = {"sdk", "sdui", "ui", "api", "ci", "cd", "pdf", "tv", "hls", "totp", "rpc", "id"}

# The `nav:` entry for a decision record, e.g.
#     - 12. Capabilities do not own stores: adr/0012-capabilities-do-not-own-stores.md
NAV_ADR = re.compile(r"^\s+-\s.*:\s*(adr/(\d{4})-([a-z0-9-]+)\.md)\s*$")


def adr_pages(mkdocs: Path) -> dict[str, str]:
    """Derive the decision-record pages from `nav:`.

    Hand-maintaining a second list of 135 records is what left this export
    covering fourteen of them, and `unreachable-capability.md` covering none,
    with nothing to report the gap. Records are routine; deriving them means a
    new one cannot be missed. Top-level pages stay explicit above.
    """
    pages: dict[str, str] = {}
    for line in mkdocs.read_text().splitlines():
        m = NAV_ADR.match(line)
        if not m:
            continue
        _, number, slug = m.groups()
        words = [w.upper() if w in ACRONYMS else w.capitalize() for w in slug.split("-")]
        pages[f"adr/{number}-{slug}/"] = f"ADR-{number}-{'-'.join(words)}.pdf"
    return pages


def pages_for(mkdocs: Path, docs: Path) -> dict[str, str]:
    """Every page to render, with `nav:` and the record files cross-checked.

    The check is the other half of deriving: `nav:` is the only index this
    repository has, so a record missing from it publishes silently and appears
    on no map at all.
    """
    pages = dict(TOP_LEVEL) | adr_pages(mkdocs)
    # README.md is the generated index, not a record.
    on_disk = {p.name for p in (docs / "adr").glob("*.md") if p.name != "README.md"}
    in_nav = {path.rstrip("/").split("/", 1)[1] + ".md" for path in pages if path.startswith("adr/")}
    if missing := sorted(on_disk - in_nav):
        raise SystemExit(f"Records absent from nav: in mkdocs.yml: {', '.join(missing)}")
    if dangling := sorted(in_nav - on_disk):
        raise SystemExit(f"nav: entries with no file: {', '.join(dangling)}")
    return pages


@contextmanager
def serve(directory: Path):
    """Serve `directory` on an ephemeral port for the life of the context."""
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{httpd.server_port}"
    finally:
        httpd.shutdown()
        httpd.server_close()


async def render(site: Path, out: Path, pages: dict[str, str]) -> int:
    from playwright.async_api import async_playwright

    out.mkdir(parents=True, exist_ok=True)

    with serve(site) as origin:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            # Light scheme prints legibly; the site's dark palette does not.
            page = await browser.new_page(color_scheme="light")
            for path, filename in pages.items():
                await page.goto(f"{origin}/{path}", wait_until="networkidle")
                # docs/assets/js/mermaid-init.js sets this once every diagram
                # has been drawn, so a page is never printed mid-render.
                await page.wait_for_selector("html[data-mermaid-ready]", timeout=60_000)
                await page.pdf(
                    path=str(out / filename),
                    format="A4",
                    print_background=True,
                    margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
                )
                print(f"  {filename}")
            await browser.close()

    return len(pages)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"), help="built site directory")
    parser.add_argument("--out", type=Path, default=Path("site/pdf"), help="output directory")
    parser.add_argument("--mkdocs", type=Path, default=Path("mkdocs.yml"), help="nav source")
    parser.add_argument("--docs", type=Path, default=Path("docs"), help="docs directory")
    args = parser.parse_args()

    if not (args.site / "index.html").exists():
        raise SystemExit(f"No built site at {args.site}. Run `mkdocs build` first.")

    pages = pages_for(args.mkdocs, args.docs)
    count = asyncio.run(render(args.site, args.out, pages))
    print(f"Built {count} PDF(s) into {args.out}")


if __name__ == "__main__":
    main()
