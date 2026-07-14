# Agent Instructions

This repository is the internal documentation home for Mosaic architecture, notes, designs, and decisions.

Agents working in this repo should preserve the existing documentation structure and keep the root `README.md` accurate as the repository grows.

## MDG-001 Authority

[MDG-001 — Documentation Authority Guide](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) is the governing standard for all authored documentation in this repository.

Before creating, splitting, renaming, reorganising, or materially editing specifications, read the relevant MDG-001 chapters:

- `02-document-types.md` for document-type responsibilities and separation of concerns.
- `03-versioning.md` for status and version progression.
- `04-writing-standards.md` for tone, terminology, diagrams, references, glossary, and Markdown rules.
- `06-cross-references.md` for references, traceability, and avoiding duplication.
- `07-repository-organisation.md` for folder, chapter, metadata, generated-content, and navigation conventions.

If these agent instructions ever conflict with MDG-001, MDG-001 wins. Update the agent instructions instead of bypassing the documentation rules.

## Repository Structure

Use the current taxonomy unless the user explicitly asks to change it:

```text
docs/
  design/
    language/  Mosaic Design Language specifications
    system/    Mosaic Design System specifications
  engineering/
    documentation/  Mosaic Documentation Guides
    architecture/   Mosaic Architecture Canon specifications
    guides/    Mosaic Engineering Guidelines specifications
    protocols/      Mosaic Integration Protocol specifications
    operations/     Mosaic Operations Playbooks
```

Each specification belongs in its own folder and should be split into focused Markdown chapters:

```text
index.md
00-document-control.md
01-...
02-...
...
glossary.md
references.md
```

## Documentation Rules

- Follow the existing `MDL-*`, `MDS-*`, `MDG-*`, `MAC-*`, `MEG-*`, `MIP-*`, and `MOP-*` folder naming conventions.
- Use URL-safe lowercase folder slugs in the MkDocs tree, such as `meg-005-runtime-architecture`.
- Choose the correct document type before adding content. Do not put Canon material in MEGs, protocol contracts outside MIPs, operational procedures outside MOPs, or ADR process rules outside MDG.
- Keep one authoritative home for each architectural concept. Summarise only when necessary and use references instead of duplicating explanations.
- Keep one major specification folder per commit when committing documentation imports or large additions.
- Preserve and maintain metadata comments at the top of specification Markdown files. `File:` must match the current repo-relative path, and `Document:`, `Status:`, and `Version:` must remain accurate.
- Update `Version:` only when MDG-001 says the change is meaningful. Do not bump versions for typo-only or formatting-only edits.
- Put decision records close to the specification they govern, usually in `*-adrs.md`.
- Update affected chapters when a decision changes the meaning of an existing specification.
- Keep References near the end and Glossary as the final chapter of each specification. `.pages` files should list references before glossary when both exist.
- Use MDG-001 canonical terminology, including `Platform` for Mosaic platform ownership and `Module` for Mosaic extensibility, while preserving established domain terms and external source titles.
- Validate Mermaid blocks before considering documentation work complete.
- Update `.pages` navigation files when adding or removing specification folders.
- Treat authored Markdown under `docs/` as canonical. Do not make generated output the source of truth.

## README Maintenance

When adding, removing, renaming, or materially reorganising documentation, update the root `README.md` in the same change.

The README should remain a current orientation guide for:

- what this repo is for
- how the documentation is organised
- where MDL, MDS, MDG, MAC, MEG, MIP, and MOP material lives
- how decisions and references should be maintained

Do not let the README drift behind the repository structure.

## Scope Discipline

Avoid introducing new top-level folders, naming schemes, or document formats unless the user asks for them or the existing structure cannot support the work.

Prefer small, reviewable Markdown changes over broad rewrites.

Before finishing documentation work, run `python3 scripts/validate_docs.py`. For navigation, structure, or publication-impacting changes, also run `python3 -m mkdocs build --strict`.
