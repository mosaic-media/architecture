"""Build one ordered PDF for every Mosaic specification in the MkDocs site."""

from __future__ import annotations

import argparse
import asyncio
import html
import re
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from typing import Iterator

import yaml
from playwright.async_api import Browser, Page, async_playwright


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"
MKDOCS_CONFIG = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
SITE_URL_MATCH = re.search(r"^site_url:\s*(?P<url>\S+)\s*$", MKDOCS_CONFIG, re.MULTILINE)
if not SITE_URL_MATCH:
    raise RuntimeError("mkdocs.yml must define site_url for external PDF links")
SITE_URL = SITE_URL_MATCH.group("url")
SPECIFICATION_RE = re.compile(
    r"^(?P<family>mdp|mad|mac|meg|mip|mop|mdl|mds|mdg)-(?P<number>\d{3})-(?P<title>.+)$"
)
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Specification:
    source_dir: Path
    relative_dir: PurePosixPath
    document_id: str
    title: str
    chapters: tuple[str, ...]

    @property
    def output_name(self) -> str:
        suffix = self.source_dir.name.split("-", 2)[2]
        return f"{self.document_id}-{suffix}.pdf"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--document",
        action="append",
        default=[],
        help="Build only this document ID; may be supplied more than once.",
    )
    parser.add_argument(
        "--jobs",
        type=int,
        default=3,
        help="Maximum number of PDFs rendered concurrently (default: 3).",
    )
    return parser.parse_args()


def discover_specifications() -> list[Specification]:
    specifications: list[Specification] = []
    for pages_file in sorted(DOCS_DIR.rglob(".pages")):
        match = SPECIFICATION_RE.fullmatch(pages_file.parent.name)
        if not match:
            continue

        config = yaml.safe_load(pages_file.read_text(encoding="utf-8")) or {}
        chapters = ordered_chapters(pages_file.parent, config.get("arrange", []))
        index = (pages_file.parent / "index.md").read_text(encoding="utf-8")
        heading = HEADING_RE.search(index)
        title = heading.group(1).strip() if heading else config.get("title", pages_file.parent.name)
        document_id = f"{match.group('family')}-{match.group('number')}".upper()
        specifications.append(
            Specification(
                source_dir=pages_file.parent,
                relative_dir=PurePosixPath(pages_file.parent.relative_to(DOCS_DIR).as_posix()),
                document_id=document_id,
                title=title,
                chapters=tuple(chapters),
            )
        )
    return specifications


def ordered_chapters(source_dir: Path, arrange: list[str]) -> list[str]:
    markdown = sorted(path.name for path in source_dir.glob("*.md"))
    explicit = [entry for entry in arrange if entry != "..."]
    unknown = [entry for entry in explicit if entry not in markdown]
    if unknown:
        raise ValueError(f"{source_dir / '.pages'} references missing pages: {', '.join(unknown)}")

    remaining = [name for name in markdown if name not in explicit]
    ordered: list[str] = []
    for entry in arrange:
        if entry == "...":
            ordered.extend(remaining)
        elif entry.endswith(".md"):
            ordered.append(entry)

    if "..." not in arrange:
        ordered.extend(remaining)
    if set(ordered) != set(markdown):
        raise ValueError(f"{source_dir / '.pages'} does not define every Markdown chapter")
    return ordered


def chapter_url(specification: Specification, chapter: str) -> str:
    base = specification.relative_dir.as_posix()
    return f"/{base}/" if chapter == "index.md" else f"/{base}/{Path(chapter).stem}/"


@contextmanager
def serve_site() -> Iterator[str]:
    if not (SITE_DIR / "index.html").is_file():
        raise FileNotFoundError("site/index.html is missing; run 'mkdocs build --strict' first")

    handler = partial(QuietHandler, directory=str(SITE_DIR))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()
        server.server_close()


async def extract_chapter(
    page: Page,
    origin: str,
    specification: Specification,
    chapter: str,
) -> dict[str, object]:
    path = chapter_url(specification, chapter)
    await page.goto(origin + path, wait_until="networkidle")
    await page.wait_for_selector("article.md-content__inner")
    if await page.locator(".mermaid").count():
        await page.wait_for_function(
            """
            () => {
              const diagrams = [...document.querySelectorAll("div.mermaid")];
              return diagrams.length > 0 && diagrams.every(
                (diagram) => diagram.shadowRoot?.querySelector("svg"),
              );
            }
            """
        )
    return await page.evaluate(
        """
        ({ path, origin, siteUrl }) => {
          const source = document.querySelector("article.md-content__inner");
          const article = source.cloneNode(true);
          const renderedDiagrams = source.querySelectorAll("div.mermaid");
          const clonedDiagrams = article.querySelectorAll("div.mermaid");
          renderedDiagrams.forEach((diagram, index) => {
            clonedDiagrams[index].innerHTML = diagram.shadowRoot.innerHTML;
          });

          const chapterId = `chapter-${path.replace(/^\\/|\\/$/g, "").replace(/[^a-z0-9]+/gi, "-")}`;
          const ids = new Map();
          article.querySelectorAll("[id]").forEach((element) => {
            const oldId = element.id;
            const newId = `${chapterId}--${oldId}`;
            ids.set(oldId, newId);
            element.id = newId;
          });
          article.querySelectorAll("*").forEach((element) => {
            [...element.attributes].forEach((attribute) => {
              if (attribute.name === "id") return;
              let value = attribute.value;
              ids.forEach((newId, oldId) => {
                value = value.replaceAll(`url(#${oldId})`, `url(#${newId})`);
                if (value === `#${oldId}`) value = `#${newId}`;
              });
              if (value !== attribute.value) element.setAttribute(attribute.name, value);
            });
          });
          article.querySelectorAll("style").forEach((style) => {
            ids.forEach((newId, oldId) => {
              style.textContent = style.textContent.replaceAll(`#${oldId}`, `#${newId}`);
            });
          });

          article.querySelectorAll("[src]").forEach((element) => {
            element.setAttribute("src", new URL(element.getAttribute("src"), location.href).href);
          });
          article.querySelectorAll("a[href]").forEach((link) => {
            const raw = link.getAttribute("href");
            if (raw.startsWith("#")) {
              const target = ids.get(raw.slice(1));
              if (target) link.setAttribute("href", `#${target}`);
              return;
            }
            const url = new URL(raw, location.href);
            if (url.origin === origin) {
              link.dataset.mosaicPath = url.pathname;
              link.dataset.mosaicHash = url.hash.slice(1);
              link.setAttribute("href", siteUrl.replace(/\\/$/, "") + url.pathname + url.hash);
            }
          });

          const heading = article.querySelector("h1");
          if (heading) heading.querySelectorAll(".headerlink").forEach((link) => link.remove());
          return {
            id: chapterId,
            title: heading ? heading.textContent.trim() : document.title,
            html: article.innerHTML,
            diagrams: renderedDiagrams.length,
          };
        }
        """,
        {
            "path": path,
            "origin": origin,
            "siteUrl": SITE_URL,
        },
    )


async def render_specification(
    browser: Browser,
    origin: str,
    specification: Specification,
    output_dir: Path,
) -> Path:
    page = await browser.new_page(color_scheme="light")
    await page.add_init_script(
        """
        const attachShadow = Element.prototype.attachShadow;
        Element.prototype.attachShadow = function(options) {
          return attachShadow.call(this, { ...options, mode: "open" });
        };
        """
    )
    try:
        chapters = [
            await extract_chapter(page, origin, specification, chapter)
            for chapter in specification.chapters
        ]
        expected_diagrams = sum(int(chapter["diagrams"]) for chapter in chapters)
        toc = "".join(
            f'<li><a href="#{chapter["id"]}">{html.escape(chapter["title"])}</a></li>'
            for chapter in chapters
        )
        body = "".join(
            f'<section class="mosaic-pdf-chapter" id="{chapter["id"]}">{chapter["html"]}</section>'
            for chapter in chapters
        )
        chapter_paths = {
            chapter_url(specification, source): chapter["id"]
            for source, chapter in zip(specification.chapters, chapters)
        }
        await page.goto(origin + chapter_url(specification, "index.md"), wait_until="networkidle")
        await page.evaluate(
            """
            ({ title, toc, body, chapterPaths, siteUrl }) => {
              document.title = title;
              document.querySelectorAll("header, nav, footer, .md-sidebar, .md-tabs").forEach((node) => node.remove());
              const main = document.querySelector("main");
              main.innerHTML = `<article class="md-content__inner md-typeset mosaic-pdf-document">
                <section class="mosaic-pdf-toc"><h1>Contents</h1><ol>${toc}</ol></section>${body}
              </article>`;
              main.querySelectorAll("a[data-mosaic-path]").forEach((link) => {
                const chapterId = chapterPaths[link.dataset.mosaicPath];
                if (chapterId) {
                  const suffix = link.dataset.mosaicHash ? `--${link.dataset.mosaicHash}` : "";
                  link.setAttribute("href", `#${chapterId}${suffix}`);
                } else {
                  link.setAttribute(
                    "href",
                    siteUrl.replace(/\\/$/, "") + link.dataset.mosaicPath +
                      (link.dataset.mosaicHash ? `#${link.dataset.mosaicHash}` : ""),
                  );
                }
              });
              const style = document.createElement("style");
              style.textContent = `
                @page { size: A4; margin: 18mm 16mm 20mm; }
                html, body, .md-container, .md-main, .md-main__inner, main {
                  display: block !important; width: auto !important; max-width: none !important;
                  margin: 0 !important; padding: 0 !important;
                  background: white !important; color: #202124 !important;
                }
                body { background: white !important; color: #202124 !important; }
                .mosaic-pdf-document { max-width: none !important; margin: 0 !important; padding: 0 !important; }
                .mosaic-pdf-toc { break-after: page; }
                .mosaic-pdf-toc ol { columns: 2; column-gap: 2rem; }
                .mosaic-pdf-toc li { break-inside: avoid; margin-bottom: .35rem; }
                .mosaic-pdf-chapter { break-before: page; }
                .mosaic-pdf-chapter:first-of-type { break-before: auto; }
                .mosaic-pdf-chapter h1:first-child { margin-top: 0; }
                .mosaic-pdf-document .mermaid {
                  break-inside: avoid; display: flex; justify-content: center;
                }
                .mosaic-pdf-document .mermaid svg { max-height: 235mm; }
                pre, table, figure, .admonition, details { break-inside: avoid; }
                a { color: #007c91 !important; }
                .headerlink, .mosaic-pdf-download { display: none !important; }
              `;
              document.head.appendChild(style);
            }
            """,
            {
                "title": specification.title,
                "toc": toc,
                "body": body,
                "chapterPaths": chapter_paths,
                "siteUrl": SITE_URL,
            },
        )
        actual_diagrams = await page.locator(".mosaic-pdf-document .mermaid svg").count()
        if actual_diagrams != expected_diagrams:
            raise RuntimeError(
                f"{specification.document_id} rendered {actual_diagrams} of "
                f"{expected_diagrams} Mermaid diagrams"
            )
        await page.emulate_media(media="print")
        output = output_dir / specification.output_name
        await page.pdf(
            path=str(output),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=(
                '<div style="font-size:8px;color:#666;width:100%;padding:0 16mm;'
                'box-sizing:border-box;display:flex;justify-content:space-between">'
                f"<span>{html.escape(specification.document_id)}</span>"
                '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span>'
                "</div>"
            ),
            outline=True,
            tagged=True,
        )
        return output
    finally:
        await page.close()


async def build_pdfs(specifications: list[Specification], origin: str, jobs: int) -> None:
    output_dir = SITE_DIR / "downloads"
    output_dir.mkdir(parents=True, exist_ok=True)
    for specification in specifications:
        (output_dir / specification.output_name).unlink(missing_ok=True)

    semaphore = asyncio.Semaphore(max(1, jobs))
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()

        async def render(specification: Specification) -> Path:
            async with semaphore:
                output = await render_specification(browser, origin, specification, output_dir)
                print(f"Built {output.relative_to(ROOT)}")
                return output

        try:
            outputs = await asyncio.gather(*(render(specification) for specification in specifications))
        finally:
            await browser.close()

    if len(outputs) != len(specifications):
        raise RuntimeError("Not every specification produced a PDF")


def main() -> None:
    args = parse_args()
    specifications = discover_specifications()
    requested = {document.upper() for document in args.document}
    if requested:
        specifications = [spec for spec in specifications if spec.document_id in requested]
        missing = requested - {spec.document_id for spec in specifications}
        if missing:
            raise SystemExit(f"Unknown document ID: {', '.join(sorted(missing))}")
    if not specifications:
        raise SystemExit("No specifications found")

    with serve_site() as origin:
        asyncio.run(build_pdfs(specifications, origin, args.jobs))
    print(f"Built {len(specifications)} specification PDF(s)")


if __name__ == "__main__":
    main()
