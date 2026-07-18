# Claude Instructions

This repository stores internal Mosaic documentation: architecture notes, design specifications, decision records, and supporting references.

Follow the existing documentation structure and keep `README.md` up to date whenever the repository changes.

## [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) Authority

[MDG-001 — Documentation Authority Guide](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) is the source of truth for documentation work in this repository.

Before creating, splitting, renaming, reorganising, or materially editing specifications, consult the relevant [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) chapters:

- `02-document-types.md` for where each kind of content belongs.
- `03-versioning.md` for the Status lifecycle and contract versioning.
- `04-writing-standards.md` for tone, terminology, diagrams, references, glossary, and Markdown rules.
- `06-cross-references.md` for traceability and duplication control.
- `07-repository-organisation.md` for folders, chapter order, metadata, generated content, and navigation.
- `10-standards-mapping.md` for the open standard each document type profiles.

If this file conflicts with [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md), follow [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) and update this file.

## Structure To Follow

Use the established layout:

```text
docs/
  design/
    language/  Mosaic Design Language
    system/    Mosaic Design System
  engineering/
    documentation/  Mosaic Documentation Guides
    architecture/   Mosaic Architecture Canon
    guides/    Mosaic Engineering Guidelines
    protocols/      Mosaic Integration Protocols
    operations/     Mosaic Operations Playbooks
```

Specifications are folder-based and split into chapter files. Match the existing pattern:

```text
index.md
00-document-control.md
01-...
02-...
...
references.md
glossary.md
```

Start a new specification by copying the matching template from `templates/`, not by copying an existing document. Each template's chapters correspond one-to-one with its [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/02-document-types.md) type definition. See [templates/README.md](templates/README.md) for the copy procedure. Do not add `templates/` to the site build; it lives outside `docs/` so MkDocs and `scripts/validate_docs.py` never see it.

## Working Expectations

- Keep MDL content under `docs/design/language`.
- Keep MDS content under `docs/design/system`.
- Keep MDG content under `docs/engineering/documentation`.
- Keep MAC content under `docs/engineering/architecture`.
- Keep MEG content under `docs/engineering/guides`.
- Keep MIP content under `docs/engineering/protocols`.
- Keep MOP content under `docs/engineering/operations`.
- Preserve existing naming conventions, metadata blocks, and chapter ordering.
- Keep specification metadata accurate. The block contains exactly three fields: `File:` must match the current repo-relative Markdown path, and `Document:` and `Status:` must reflect the specification. Do not add a `Version:` field to any document.
- Change `Status:` only for a real lifecycle transition as defined by [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md). Do not change Status for typo-only or formatting-only edits. Only the contract a MIP defines carries a version, declared in the document body.
- Keep each document type within its [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) responsibility: MAC defines accepted architecture, MEG explains engineering practice, MIP defines integration contracts, MOP defines operational procedures, MDL/MDS define design language and system material, and MDG defines documentation standards.
- Prefer one authoritative home for each concept. Replace duplicated explanations with concise summaries and links to the owning specification.
- Make every reference to another published Mosaic document a relative Markdown hyperlink. Link identifier-only references to the target `index.md`, use the catalogued `ID — Canonical Title` when naming a document, and link directly to a chapter or anchor when appropriate. Leave unavailable identifiers unlinked and mark them `planned; not yet published` or `deferred; not yet published`.
- Use [MDG-001](docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md) canonical terminology, including `Platform` for Mosaic platform ownership and `Module` for Mosaic extensibility, while preserving established domain terms and external source titles.
- Keep ADRs and decision notes near the specification they affect.
- Keep References near the end and Glossary as the final chapter. `.pages` files should list references before glossary when both exist.
- Validate Mermaid syntax after editing Mermaid diagrams.
- Use Mermaid for flows, lifecycles, state transitions, hierarchies, dependencies and interactions. Do not author relationship diagrams with ASCII arrows or non-file tree glyphs; retain text fences only when fixed-width literal or spatial layout is the subject.
- Update `.pages` navigation files when adding or removing specification folders.
- If committing, commit each major specification folder independently.
- Treat authored Markdown under `docs/` as canonical. Do not make generated output the source of truth.

## README Requirement

When adding new documentation areas, specification folders, major sections, or repo conventions, update the root `README.md` as part of the same work.

The README should always explain the current repository purpose and structure clearly enough for a new contributor or agent to find the right place for documentation.

## Change Discipline

Do not reorganise the documentation taxonomy casually.

Prefer additive, focused updates that preserve the existing MDL/MDS structure unless the user explicitly requests a broader restructure.

Before finishing documentation work, run `python3 scripts/validate_docs.py`. For navigation, structure, or publication-impacting changes, also run `python3 -m mkdocs build --strict`.
