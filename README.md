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
```

The current imported specification set lives in:

- `docs/design/language` for MDL documents
- `docs/design/system` for MDS documents
- `docs/engineering/documentation` for MDG documents
- `docs/engineering/guides` for MEG documents

The remaining engineering sections are reserved for future document types.

## Document Types

The structure is intended to support these document families without another major reorganisation:

- `MAC` — Mosaic Architecture
- `MDG` — Mosaic Documentation Guides
- `MDP` — Mosaic Design Process
- `MEG` — Mosaic Engineering Guidelines
- `MIP` — Mosaic Integration Protocol
- `MOP` — Mosaic Operations
- `MDL` — Mosaic Design Language
- `MDS` — Mosaic Design System

## Documentation Conventions

Each specification is stored as its own folder with one Markdown file per chapter.

Most specification folders follow this shape:

```text
index.md
00-document-control.md
01-...
02-...
...
glossary.md
references.md
```

Folder names are URL-safe slugs such as `meg-001-go-engineering-standards`. The generated site uses `.pages` files so navigation presents human-readable titles such as `Go Engineering Standards` while the document ID remains visible on the page.

Chapter-level files are preferred over large monolithic documents because they are easier to review, diff, discuss, and evolve independently.

## Decision Records

Decision records live inside the relevant specification folder, usually in `*-adrs.md`.

Place decisions close to the system they govern:

- MDL decisions belong under `docs/design/language`
- MDS decisions belong under `docs/design/system`
- MDG decisions belong under `docs/engineering/documentation`
- MEG decisions belong under `docs/engineering/guides`
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
- GitHub repository and edit-page links

Specification metadata comments are preserved in source files. A MkDocs hook renders Document ID, Status, and Version visibly in the generated site at build time.

## Branding

Light Mosaic branding is configured through `mkdocs.yml` and `docs/stylesheets/mosaic.css`.

The temporary header logo is stored at `docs/assets/images/mosaic-logo-dark.jpg`. Keep this first branding layer intentionally small: Material for MkDocs remains responsible for typography, layout, navigation, and component styling.

## Working Guidelines

- Keep documents focused on durable reasoning, not transient implementation details.
- Prefer explicit ownership, status, version, and scope metadata.
- Preserve links between vision, principles, design language, design system, and implementation-facing guidance.
- Use Mermaid diagrams where they clarify relationships, and validate Mermaid syntax before committing.
- Commit each major specification folder independently so history remains reviewable.

## Current Status

The current documentation set is draft material.

Draft does not mean disposable. Treat these documents as evolving architecture: changes should be intentional, reviewed, and traceable.
