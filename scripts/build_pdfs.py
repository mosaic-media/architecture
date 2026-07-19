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
import threading
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# Site-relative page paths mapped to their output filename.
PAGES = {
    "": "Mosaic.pdf",
    "architecture/": "Mosaic-Architecture.pdf",
    "roadmap/": "Mosaic-Roadmap.pdf",
    "adr/0001-transactional-store-extensibility/": "ADR-0001-Transactional-Store-Extensibility.pdf",
    "adr/0002-module-storage-and-delivery-model/": "ADR-0002-Module-Storage-And-Delivery-Model.pdf",
}


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


async def render(site: Path, out: Path) -> int:
    from playwright.async_api import async_playwright

    out.mkdir(parents=True, exist_ok=True)

    with serve(site) as origin:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            # Light scheme prints legibly; the site's dark palette does not.
            page = await browser.new_page(color_scheme="light")
            for path, filename in PAGES.items():
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

    return len(PAGES)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"), help="built site directory")
    parser.add_argument("--out", type=Path, default=Path("site/pdf"), help="output directory")
    args = parser.parse_args()

    if not (args.site / "index.html").exists():
        raise SystemExit(f"No built site at {args.site}. Run `mkdocs build` first.")

    count = asyncio.run(render(args.site, args.out))
    print(f"Built {count} PDF(s) into {args.out}")


if __name__ == "__main__":
    main()
