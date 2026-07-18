# Mosaic Architecture

This repository holds internal Mosaic documentation: architecture notes, design specifications, decision records, and supporting reference material.

It is the source of truth for how Mosaic is understood, designed, and evolved before implementation work is planned or built. The repository is also configured as a Material for MkDocs documentation portal published through GitHub Pages.

## Documentation Website

The generated site uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Local development:

```bash
python -m pip install -r requirements.txt
python scripts/validate_docs.py
mkdocs serve
```

Production validation:

```bash
mkdocs build --strict
```

Build the portal with one combined PDF per specification:

```bash
python -m playwright install chromium
ENABLE_PDF_DOWNLOADS=true mkdocs build --strict
python scripts/build_pdfs.py
```

The PDF build discovers specification folders automatically and follows each
folder's `.pages` chapter order. Generated files are written to
`site/downloads/`; authored Markdown remains the source of truth.

GitHub Actions builds and deploys the site to GitHub Pages on every push to `main`.

## Repository Structure

```text
docs/
  design/
    language/    Mosaic Design Language specifications
    system/      Mosaic Design System specifications
  engineering/
    documentation/  Documentation governance and authoring standards
    architecture/  Platform and system architecture specifications
    guides/        Mosaic Engineering Guidelines specifications
    protocols/     Integration and interoperability protocol specifications
    operations/    Runtime, support, and operational specifications
  roadmaps/        Cross-disciplinary Mosaic Roadmaps
templates/         Authoritative starting point for each document type
```

`templates/` sits outside `docs/` deliberately: MkDocs never renders it and `scripts/validate_docs.py` never scans it, so placeholder identifiers do not register as defects. See [templates/README.md](templates/README.md).

The current imported specification set lives in:

- `docs/design/language` for MDL documents
- `docs/design/system` for MDS documents
- `docs/engineering/documentation` for MDG documents
- `docs/engineering/architecture` for MAC, MAD and MDP documents
- `docs/engineering/guides` for MEG documents
- `docs/engineering/protocols` for MIP documents
- `docs/engineering/operations` for MOP documents
- `docs/roadmaps` for MRM documents

[MEG-006](docs/engineering/guides/meg-006-module-platform/index.md) contains the Module Platform and its integrated Developer Platform guidance, including SDK, CLI, local development, deterministic Test Harness Modules and publication workflow boundaries.

[MIP-003](docs/engineering/protocols/mip-003-uv-light-frame-protocol/index.md) defines the canonical artwork-light frame exchanged between artwork analysis, MOS Cache and client renderers.

[MEG-014](docs/engineering/guides/meg-014-refraction-engine/index.md) defines how CSS, Flutter and two-dimensional shader clients resolve that source into stable Acrylic rendering without mesh geometry.

[MEG-015](docs/engineering/guides/meg-015-platform-foundation-implementation/index.md) defines the implementation-grade first build path for the Mosaic Platform foundation before SDK extraction.

## Document Types

The structure is intended to support these document families without another major reorganisation:

- `MDP` — Mosaic Design Proposal
- `MAD` — Mosaic Architecture Decision
- `MAC` — Mosaic Architecture Canon
- `MEG` — Mosaic Engineering Guide
- `MIP` — Mosaic Integration Protocol
- `MOP` — Mosaic Operations & Playbook
- `MDL` — Mosaic Design Language
- `MDS` — Mosaic Design System
- `MDG` — Mosaic Documentation Guide
- `MRM` — Mosaic Roadmap

Each type has an authoritative template under [`templates/`](templates/README.md). The templates are the machine-readable form of [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/02-document-types.md): their chapter skeletons match the type definitions one-to-one, so structure alone keeps the types apart.

## Creating a New Document

Scaffold a new specification with `scripts/new_doc.py` rather than copying an existing folder by hand:

```bash
python3 scripts/new_doc.py --type mad --title "Module Signing Policy"
```

```text
MAD-003 — Module Signing Policy
Created docs/engineering/architecture/mad-003-module-signing-policy/
  wrote 00-document-control.md
  wrote 01-context.md
  ...
  wrote .pages
  registered mad-003-module-signing-policy in docs/engineering/architecture/.pages
```

The script resolves the discipline directory from the type, allocates the next sequential identifier, creates the slugged folder, copies the matching template and stamps `File`, `Document` and `Status: Draft` into every page. It also rewrites the identifier and title placeholders in the body, so the Document Control table agrees with the metadata block, and registers the folder in its discipline `.pages`.

| Flag | Purpose |
|------|---------|
| `--type` | One of `mdp`, `mad`, `mac`, `meg`, `mip`, `mop`, `mdg`, `mdl`, `mds`, `mrm`. |
| `--title` | The specification title. Also becomes the folder slug and the `.pages` title. |
| `--id` | Optional explicit identifier such as `mad-003`. Omit to allocate the next number. |
| `--dry-run` | Print what would be created and write nothing. |

Identifiers are allocated as the highest existing number plus one. Gaps are never refilled, because an identifier is a permanent reference and must not be reissued. The script refuses to overwrite an existing folder.

A freshly scaffolded specification passes `scripts/validate_docs.py` as generated. Replace the guidance comments and placeholders, set the `Owner`, then validate again before committing.

Run the scaffolder's own tests with:

```bash
python3 -m pytest scripts/test_new_doc.py
```

## Documentation Conventions

Each specification is stored as its own folder with one Markdown file per chapter.

Most specification folders follow this shape:

```text
index.md
00-document-control.md
01-...
02-...
...
references.md
glossary.md
```

Folder names are URL-safe slugs such as `meg-001-go-engineering-standards`. The generated site uses `.pages` files so navigation presents human-readable titles such as `Go Engineering Standards` while the document ID remains visible on the page.

Chapter-level files are preferred over large monolithic documents because they are easier to review, diff, discuss, and evolve independently.

References should appear near the end of a specification and glossary should remain the final authored chapter.

Every authored Markdown page begins with exactly three metadata fields: `File`, `Document`, and `Status`. The schema is defined by [MDG-001 — Documentation Authority Guide](docs/engineering/documentation/mdg-001-documentation-authority-guide/07-repository-organisation.md).

`Status` is one of `Draft`, `Review`, `Active`, `Deprecated`, or `Superseded`, with `Deferred`, `Accepted`, `Rejected`, and `Withdrawn` additionally available to MDP proposals. Prose documents carry no version number; only the contracts defined by MIP documents carry a major compatibility version such as `Event Protocol v1`, declared in the document body. Specifications still carrying a legacy `Version` field are tolerated by tooling until they are migrated.

Source pages do not carry review-status summaries or manual previous/next links; document authority comes from `Status` and page transitions come from MkDocs.

Every reference to another published Mosaic document is a relative Markdown hyperlink. Identifier-only references link to the target specification's `index.md`; named references use the catalogued `ID — Canonical Title`, while chapter-specific references may link directly to the relevant chapter or anchor. Unpublished identifiers remain unlinked and are marked `planned; not yet published` or `deferred; not yet published`.

Relationship diagrams use Mermaid rather than ASCII arrows or hierarchy glyphs. Text fences remain appropriate for literal fixed-width material such as repository trees, commands, configuration, logs, templates, notation and interface wireframes.

## Decision Records

Decision records live inside the relevant specification folder, usually in `*-adrs.md`.

Place decisions close to the system they govern:

- MDL decisions belong under `docs/design/language`
- MDS decisions belong under `docs/design/system`
- MDG decisions belong under `docs/engineering/documentation`
- MEG decisions belong under `docs/engineering/guides`
- MAC decisions belong under `docs/engineering/architecture`
- MIP decisions belong under `docs/engineering/protocols`
- MOP decisions belong under `docs/engineering/operations`
- MRM documents reference decisions and owning specifications but do not own architectural decisions
- cross-cutting decisions should reference the upstream specification they depend on

When a decision changes the meaning of an existing specification, update both the ADR section and the affected chapter.

## Website Features

The MkDocs portal is configured with:

- full-text search with suggestions and highlighting
- dark and light theme toggle
- Mermaid diagram rendering
- admonitions
- code copy buttons
- previous and next navigation
- table of contents
- section index pages
- one-click, whole-specification PDF downloads
- GitHub repository and edit-page links

Metadata comments are preserved in source files. A MkDocs hook renders the document identity and Status visibly in the generated site at build time, along with a legacy Version row where one is still declared.

## Landing Pages and Navigation

The portal uses landing pages as a concise orientation layer over the authoritative specifications:

- `docs/index.md` provides a short overview and goal-based starting points.
- discipline landing pages route readers into Design or Engineering.
- document-family landing pages catalogue the specifications they contain with one-sentence summaries and reading guidance.
- specification `index.md` pages introduce the purpose and scope of the authoritative document before its detailed chapters.

Landing-page summaries must link to the specification that owns each concept and must not become a second source of normative requirements. When a specification is added, removed, renamed or materially changes purpose, update its nearest catalogue and any affected reading path in the same change. Keep `.pages` navigation and this README synchronised when the visible structure changes.

## Branding

Light Mosaic branding is configured through `mkdocs.yml` and `docs/stylesheets/mosaic.css`.

The temporary header logo is stored at `docs/assets/images/mosaic-logo-dark.jpg`. Keep this first branding layer intentionally small: Material for MkDocs remains responsible for typography, layout, navigation, and component styling.

## Working Guidelines

- Keep documents focused on durable reasoning, not transient implementation details.
- Keep ownership explicit in Document Control and keep page metadata synchronised.
- Preserve links between vision, principles, design language, design system, and implementation-facing guidance.
- Use Mermaid diagrams where they clarify relationships, and validate Mermaid syntax before committing.
- Commit each major specification folder independently so history remains reviewable.

## Current Status

The current documentation set is draft material.

Draft does not mean disposable. Treat these documents as evolving architecture: changes should be intentional, reviewed, and traceable.
