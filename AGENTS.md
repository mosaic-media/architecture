# Agent Instructions

This repository is the internal documentation home for Mosaic architecture, notes, designs, and decisions.

Agents working in this repo should preserve the existing documentation structure and keep the root `README.md` accurate as the repository grows.

## Repository Structure

Use the current taxonomy unless the user explicitly asks to change it:

```text
docs/
  design/
    language/  Mosaic Design Language specifications
    system/    Mosaic Design System specifications
  engineering/
    documentation/  Mosaic Documentation Guides
    guides/    Mosaic Engineering Guidelines specifications
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

- Follow the existing `MDL-*`, `MDS-*`, `MDG-*`, and `MEG-*` folder naming conventions.
- Use URL-safe lowercase folder slugs in the MkDocs tree, such as `meg-005-runtime-architecture`.
- Keep one major specification folder per commit when committing documentation imports or large additions.
- Preserve metadata comments at the top of generated or split files when present.
- Put decision records close to the specification they govern, usually in `*-adrs.md`.
- Update affected chapters when a decision changes the meaning of an existing specification.
- Validate Mermaid blocks before considering documentation work complete.
- Update `.pages` navigation files when adding or removing specification folders.

## README Maintenance

When adding, removing, renaming, or materially reorganising documentation, update the root `README.md` in the same change.

The README should remain a current orientation guide for:

- what this repo is for
- how the documentation is organised
- where MDL, MDS, MDG, and MEG material lives
- how decisions and references should be maintained

Do not let the README drift behind the repository structure.

## Scope Discipline

Avoid introducing new top-level folders, naming schemes, or document formats unless the user asks for them or the existing structure cannot support the work.

Prefer small, reviewable Markdown changes over broad rewrites.
