# Claude Instructions

This repository holds Mosaic's architecture and direction in three documents. The implementation lives in `platform`, alongside this repository on disk.

- **[docs/index.md](docs/index.md)** — what Mosaic is, the decisions, the tradeoffs, the controlled vocabulary
- **[docs/architecture.md](docs/architecture.md)** — how the platform is built
- **[docs/roadmap.md](docs/roadmap.md)** — what is next and what blocks it

---

## The source is authoritative, not this repository

`platform` is ~15,300 lines of Go and it is the truth. These documents describe it.

**Read the code before writing about it.** Do not describe a contract, package or behaviour from what a document says it is. Open the file. This repository previously contained two hundred documents describing a system nobody had checked against the source, and the result was a roadmap built against an abandoned storage model.

If a document here disagrees with the source, **the document is wrong** — fix it, in the same session, rather than working around it.

---

## Rules

**Delete, do not annotate.** Superseded content is removed. Git retains it permanently, so nothing is lost. A banner reading "this section is historical" does not outweigh the three hundred lines beneath it that still assert the old thing — that exact pattern is what caused a discarded analytical database to reappear in a roadmap.

**No description ahead of implementation.** Roadmaps may look forward. Descriptions of the system may not. If it is not built, either omit it or state plainly that it does not exist.

**One authoritative statement per fact.** Never explain the same thing in two places. If something belongs in the architecture page, it is not also summarised in the overview.

**Do not create new documents.** Three is the number. A fourth needs a reason that survives being asked "why does this not belong in one of the existing three?" Decision records are the one sanctioned exception — `docs/adr/0001-kebab-case-title.md`, sequential, in the standard Context / Decision / Alternatives / Consequences form.

**Do not resurrect the old taxonomy.** No MDL, MDS, MEG, MAC, MIP, MOP, MAD, MDP or MRM identifiers. No document-type system, no chapter numbering, no cross-reference discipline, no metadata blocks. Conventional filenames only.

**Respect the controlled vocabulary** in `docs/index.md`. One word, one meaning. *Transport* meaning three different things is how an agent invented a module transport layer the architecture forbids. When a word starts carrying two meanings, add it to that table.

**State tradeoffs, do not smooth them over.** Compiling modules into one binary trades isolation for speed. The previous corpus claimed both, and that claim would have shipped a false security guarantee.

---

## The site

`docs/` is the published content. It builds to GitHub Pages with MkDocs Material, and every page is also exported as a PDF for handing to a tool that cannot reach the site.

- **Diagrams are Mermaid**, in a ```` ```mermaid ```` fence. They render on the site and in GitHub's own Markdown view. Do not draw structure with ASCII arrows — it renders as a code block and reads as noise. A fenced text block is still right when fixed-width layout *is* the subject, such as a directory tree.
- **Adding a page means editing `nav:` in `mkdocs.yml` and `PAGES` in `scripts/build_pdfs.py`.** That friction is deliberate. It is a reminder that a fourth page needs justifying.
- `mkdocs build --strict` fails on a broken internal link, which is the only automated check this repository keeps.

The previous system's tooling — Vale, lychee, markdownlint, the structure validator, the chapter registry, the document templates — is gone and stays gone. One of those rules mechanically rewrote *Extension* to *Module* everywhere, which destroyed the Open/Closed Principle in prose and turned vendor documentation URLs into dead links. Linters that rewrite terminology across a corpus cause more damage than they prevent.

---

## Working expectations

- Verify claims against `platform` rather than against another document.
- Prefer deleting to adding. This repository got into trouble by growing.
- When something is undecided, say so. An honest gap is worth more than a plausible invention that reads as settled.
- Commit with a message explaining what changed and why. If a change corrects something the previous documentation got wrong, say what it got wrong.
