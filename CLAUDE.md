# Claude Instructions

This repository holds Mosaic's architecture and direction in three documents. The implementation lives in `platform`, alongside this repository on disk.

- **[docs/index.md](docs/index.md)** — what Mosaic is, the decisions, the tradeoffs, the controlled vocabulary
- **[docs/architecture.md](docs/architecture.md)** — how the platform is built
- **[docs/roadmap.md](docs/roadmap.md)** — what is next and what blocks it

---

## The source is authoritative, not this repository

`platform` is ~37,500 lines of Go and it is the truth. These documents describe it. The SDK, the two modules, `sdui` and `web` are the truth about themselves in the same way.

**Read the code before writing about it.** Do not describe a contract, package or behaviour from what a document says it is. Open the file. This repository previously contained two hundred documents describing a system nobody had checked against the source, and the result was a roadmap built against an abandoned storage model.

If a document here disagrees with the source, **the document is wrong** — fix it, in the same session, rather than working around it.

---

## Rules

**Delete, do not annotate.** Superseded content is removed. Git retains it permanently, so nothing is lost. A banner reading "this section is historical" does not outweigh the three hundred lines beneath it that still assert the old thing — that exact pattern is what caused a discarded analytical database to reappear in a roadmap.

**No description ahead of implementation.** Roadmaps may look forward. Descriptions of the system may not. If it is not built, either omit it or state plainly that it does not exist.

**One authoritative statement per fact.** Never explain the same thing in two places. If something belongs in the architecture page, it is not also summarised in the overview.

**Do not create new documents.** Three is the number, plus the [unreachable capability](docs/unreachable-capability.md) register. A fifth needs a reason that survives being asked "why does this not belong in one of the existing four?" Decision records are the one sanctioned exception — `docs/adr/0001-kebab-case-title.md`, sequential, in the standard Context / Decision / Alternatives / Consequences form.

**Decision records are append-only.** This is the rule most easily broken with good intentions, and breaking it costs the thing an ADR is for — a faithful account of what was decided, at a time, unedited afterwards.

- **Never rewrite a record's body to match what was built**, to correct it, or to annotate it with "as built, this differs". That turns a record into a running commentary.
- **State changes go in the `**Status:**` line and nowhere else** — built, built in part (naming the part), or superseded, wholly ("Superseded by ADR N") or partly ("Partly superseded: X was reversed by ADR N; the rest stands").
- **A changed decision earns a new record that supersedes it.** If the code deliberately does what a record decided against, that is a decision: write it as one, and point both records at each other through their Status lines. The old body stays exactly as it was.
- **An unbuilt decision is not a superseded one.** "Not done yet" belongs in the Status line and the roadmap; only a reversal earns a new record.

**The roadmap is derived, and it is maintained here.** `docs/roadmap.md` is the single record of where the build is, for every repository. It is written from the code rather than from the plan that preceded it, so a slice is marked landed with whatever it left out named in the same breath, and an implementation that departed from its ADR says where it departed. A change in any sibling repository that dates the roadmap is a change to the roadmap, in the same session. Nothing else — no `CLAUDE.md`, no README — carries a second copy of "what is built".

**Do not resurrect the old taxonomy.** No MDL, MDS, MEG, MAC, MIP, MOP, MAD, MDP or MRM identifiers. No document-type system, no chapter numbering, no cross-reference discipline, no metadata blocks. Conventional filenames only.

**Respect the controlled vocabulary** in `docs/index.md`. One word, one meaning. *Transport* meaning three different things is how an agent invented a module transport layer the architecture forbids. When a word starts carrying two meanings, add it to that table.

**State tradeoffs, do not smooth them over.** Compiling modules into one binary trades isolation for speed. The previous corpus claimed both, and that claim would have shipped a false security guarantee.

---

## The site

`docs/` is the published content. It builds to GitHub Pages with MkDocs Material, and every page is also exported as a PDF for handing to a tool that cannot reach the site.

- **Diagrams are Mermaid**, in a ```` ```mermaid ```` fence. They render on the site and in GitHub's own Markdown view. Do not draw structure with ASCII arrows — it renders as a code block and reads as noise. A fenced text block is still right when fixed-width layout *is* the subject, such as a directory tree.
- **Adding a page means editing `nav:` in `mkdocs.yml` and `PAGES` in `scripts/build_pdfs.py`.** That friction is deliberate. It is a reminder that a fourth page needs justifying.
- `mkdocs build --strict` fails on a broken internal link, which is the only automated check this repository keeps. **It runs in a container** — see below.

The previous system's tooling — Vale, lychee, markdownlint, the structure validator, the chapter registry, the document templates — is gone and stays gone. One of those rules mechanically rewrote *Extension* to *Module* everywhere, which destroyed the Open/Closed Principle in prose and turned vendor documentation URLs into dead links. Linters that rewrite terminology across a corpus cause more damage than they prevent.

---

## The build runs in a container, nothing runs on the host

**Do not run `pip install`, `mkdocs` or `python scripts/build_pdfs.py` directly
on this machine.** The check runs inside this repository's container:

```bash
docker compose -f docker-compose.test.yml run --rm test
```

That installs the pinned `requirements.txt` and runs `mkdocs build --strict`.
Append `bash` for a shell in the same environment.

The rule is the same in all seven repositories, and it costs least here — but
the check is also the one most likely to be skipped, because running it on the
host means installing a Python toolchain to lint some Markdown. Skipping it
costs exactly what this repository exists to prevent: a document pointing at a
page or an anchor that no longer exists, which is the ordinary consequence of
"delete, do not annotate" and which nothing else will catch.

The PDF export is a **separate service**, because it downloads a Chromium and
its system libraries — minutes and hundreds of megabytes — to produce artefacts
CI publishes anyway:

```bash
docker compose -f docker-compose.test.yml run --rm pdfs
```

Run it when changing `scripts/build_pdfs.py`, or to check that a Mermaid diagram
renders as a diagram rather than as a code block. That is the whole reason the
export drives a browser instead of a Markdown-to-PDF converter: the diagrams are
drawn by JavaScript.

---

## Working expectations

- Verify claims against `platform` rather than against another document.
- Prefer deleting to adding. This repository got into trouble by growing.
- When something is undecided, say so. An honest gap is worth more than a plausible invention that reads as settled.
- Commit with a message explaining what changed and why. If a change corrects something the previous documentation got wrong, say what it got wrong.
