# Claude Instructions

This repository stores internal Mosaic documentation: architecture notes, design specifications, decision records, and supporting references.

Follow the existing documentation structure and keep `README.md` up to date whenever the repository changes.

## Structure To Follow

Use the established layout:

```text
design/
  mdl/  Mosaic Design Language
  mds/  Mosaic Design System
```

Specifications are folder-based and split into chapter files. Match the existing pattern:

```text
README.md
00-document-control.md
01-...
02-...
...
glossary.md
references.md
```

## Working Expectations

- Keep MDL content under `design/mdl`.
- Keep MDS content under `design/mds`.
- Preserve existing naming conventions, metadata blocks, and chapter ordering.
- Keep ADRs and decision notes near the specification they affect.
- Validate Mermaid syntax after editing Mermaid diagrams.
- If committing, commit each major specification folder independently.

## README Requirement

When adding new documentation areas, specification folders, major sections, or repo conventions, update the root `README.md` as part of the same work.

The README should always explain the current repository purpose and structure clearly enough for a new contributor or agent to find the right place for documentation.

## Change Discipline

Do not reorganise the documentation taxonomy casually.

Prefer additive, focused updates that preserve the existing MDL/MDS structure unless the user explicitly requests a broader restructure.
