# Agent Instructions

This repository is the internal documentation home for Mosaic architecture, notes, designs, and decisions.

Agents working in this repo should preserve the existing documentation structure and keep the root `README.md` accurate as the repository grows.

## [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) Authority

[MDG-001 — Documentation Authority Guide](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) is the governing standard for all authored documentation in this repository.

Before creating, splitting, renaming, reorganising, or materially editing specifications, read the relevant [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) chapters:

- `02-document-types.md` for document-type responsibilities and separation of concerns.
- `03-versioning.md` for the Status lifecycle and contract versioning.
- `10-standards-mapping.md` for the open standard each document type profiles.
- `04-writing-standards.md` for tone, terminology, diagrams, references, glossary, and Markdown rules.
- `06-cross-references.md` for references, traceability, and avoiding duplication.
- `07-repository-organisation.md` for folder, chapter, metadata, generated-content, and navigation conventions.

If these agent instructions ever conflict with [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md), [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) wins. Update the agent instructions instead of bypassing the documentation rules.

## Repository Structure

Use the current taxonomy unless the user explicitly asks to change it:

```text
docs/
  design/
    language/  Mosaic Design Language specifications
    system/    Mosaic Design System specifications
  engineering/
    documentation/  Mosaic Documentation Guides
    architecture/   Mosaic Architecture Canon, decisions and proposals
    guides/    Mosaic Engineering Guidelines specifications
    protocols/      Mosaic Integration Protocol specifications
    operations/     Mosaic Operations Playbooks
  roadmaps/         Mosaic Roadmaps
```

Each specification belongs in its own folder and should be split into focused Markdown chapters:

```text
index.md
00-document-control.md
01-...
02-...
...
references.md
glossary.md
```

Start a new specification by copying the matching template from `templates/`, not by copying an existing document. Each template's chapters correspond one-to-one with its [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/02-document-types.md) type definition, and each ships with `Status: Draft` and no `Version` field. See [templates/README.md](templates/README.md). `templates/` deliberately lives outside `docs/`, so MkDocs and `scripts/validate_docs.py` never see it; do not move it or add it to the site build.

## Documentation Rules

- Follow the existing `MDP-*`, `MAD-*`, `MAC-*`, `MEG-*`, `MIP-*`, `MOP-*`, `MDL-*`, `MDS-*`, `MDG-*`, and `MRM-*` folder naming conventions.
- Use URL-safe lowercase folder slugs in the MkDocs tree, such as `meg-005-runtime-architecture`.
- Choose the correct document type before adding content. Do not put Canon material in MEGs, protocol contracts outside MIPs, operational procedures outside MOPs, or ADR process rules outside MDG.
- Keep one authoritative home for each architectural concept. Summarise only when necessary and use references instead of duplicating explanations.
- Make every reference to another published Mosaic document a relative Markdown hyperlink. Link identifier-only references to the target `index.md`, use the catalogued `ID — Canonical Title` when naming a document, and link directly to a chapter or anchor when appropriate. Leave unavailable identifiers unlinked and mark them `planned; not yet published` or `deferred; not yet published`.
- Keep one major specification folder per commit when committing documentation imports or large additions.
- Preserve and maintain metadata comments at the top of every authored Markdown file under `docs/`. The block contains exactly three fields: `File:` must match the current repo-relative path, and `Document:` and `Status:` must remain accurate. Do not add a `Version:` field to any document.
- Do not add Review Status sections or manual previous/next page links. Metadata communicates authority through Status and MkDocs provides page transitions.
- Use `AdamNi-7080` for personally owned specifications; preserve explicit team or organisational ownership where responsibility genuinely belongs to that group.
- Change `Status:` only for a real lifecycle transition as defined by [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md). Do not change Status for typo-only or formatting-only edits. Only the contract a MIP defines carries a version, declared in the document body.
- Put decision records close to the specification they govern, usually in `*-adrs.md`.
- Update affected chapters when a decision changes the meaning of an existing specification.
- Keep References near the end and Glossary as the final chapter of each specification. `.pages` files should list references before glossary when both exist.
- Use [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) canonical terminology, including `Platform` for Mosaic platform ownership and `Module` for Mosaic extensibility, while preserving established domain terms and external source titles.
- Validate Mermaid blocks before considering documentation work complete.
- Use Mermaid for flows, lifecycles, state transitions, hierarchies, dependencies and interactions. Do not author relationship diagrams with ASCII arrows or non-file tree glyphs; retain text fences only when fixed-width literal or spatial layout is the subject.
- Update `.pages` navigation files when adding or removing specification folders.
- Treat authored Markdown under `docs/` as canonical. Do not make generated output the source of truth.

## README Maintenance

When adding, removing, renaming, or materially reorganising documentation, update the root `README.md` in the same change.

The README should remain a current orientation guide for:

- what this repo is for
- how the documentation is organised
- where MDP, MAD, MAC, MEG, MIP, MOP, MDL, MDS, MDG, and MRM material lives
- how decisions and references should be maintained

Do not let the README drift behind the repository structure.

## Landing Page Maintenance

Landing pages are the concise orientation layer for the documentation portal. Keep them useful without allowing them to compete with authoritative specifications.

- Keep `docs/index.md` focused on a short Mosaic overview, documentation map, and goal-based starting points.
- Keep discipline and document-family `index.md` pages as curated catalogues with one-sentence summaries, reading guidance, and direct links to authoritative specification `index.md` pages.
- When adding, removing, renaming, or materially changing the purpose of a specification, update its nearest document-family landing page in the same change.
- Update the parent Design or Engineering landing page when a reader journey, document family, or discipline-level relationship changes.
- Update the root landing page only when the overall documentation map or a goal-based starting point changes.
- Treat landing-page descriptions as non-normative summaries. Do not duplicate requirements, definitions, protocol rules, or operational procedures from the owning specification.
- Keep `.pages` navigation labels and ordering synchronised with the catalogues. Use clear reader-facing names while preserving URL-safe source paths.
- Update the root `README.md` when visible documentation organisation or navigation conventions change.

## Scope Discipline

Avoid introducing new top-level folders, naming schemes, or document formats unless the user asks for them or the existing structure cannot support the work.

Prefer small, reviewable Markdown changes over broad rewrites.

Before finishing documentation work, run `python3 scripts/validate_docs.py`. For navigation, structure, or publication-impacting changes, also run `python3 -m mkdocs build --strict`.
