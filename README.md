# Mosaic Architecture

This repository holds internal Mosaic documentation: architecture notes, design specifications, decision records, and supporting reference material.

It is intended to be the source of truth for how Mosaic is understood, designed, and evolved before implementation work is planned or built.

## Repository Structure

```text
design/
  mdl/  Mosaic Design Language
  mds/  Mosaic Design System
```

### Mosaic Design Language

`design/mdl` contains foundational product and design-language specifications.

These documents describe:

- why Mosaic exists
- how design decisions are made
- how Mosaic models the user's entertainment world
- how interaction, behaviour, and composition should be understood

Start here when a decision affects product philosophy, user experience, interaction behaviour, or conceptual architecture.

### Mosaic Design System

`design/mds` contains implementation-facing design-system specifications.

These documents describe:

- design token architecture
- colour, material, typography, and motion systems
- runtime composition
- tile and component architecture

Start here when a decision affects visual systems, presentation primitives, runtime design infrastructure, or component behaviour.

## Documentation Conventions

Each specification is stored as a folder with one Markdown file per chapter.

Most specification folders follow this shape:

```text
README.md
00-document-control.md
01-...
02-...
...
glossary.md
references.md
```

Chapter-level files are preferred over large monolithic documents because they are easier to review, diff, discuss, and evolve independently.

## Decision Records

Decision records live inside the relevant specification folder, usually in `*-adrs.md`.

Place decisions close to the system they govern:

- MDL decisions belong under `design/mdl`
- MDS decisions belong under `design/mds`
- cross-cutting decisions should reference the upstream specification they depend on

When a decision changes the meaning of an existing specification, update both the ADR section and the affected chapter.

## Working Guidelines

- Keep documents focused on durable reasoning, not transient implementation details.
- Prefer explicit ownership, status, version, and scope metadata.
- Preserve links between vision, principles, design language, design system, and implementation-facing guidance.
- Use Mermaid diagrams where they clarify relationships, and validate Mermaid syntax before committing.
- Commit each major specification folder independently so history remains reviewable.

## Current Status

The current documentation set is draft material.

Draft does not mean disposable. Treat these documents as evolving architecture: changes should be intentional, reviewed, and traceable.
