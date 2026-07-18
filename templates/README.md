# Mosaic Specification Templates

Authoritative starting points for every Mosaic document type.

These templates are the machine-readable form of [MDG-001 — Documentation Authority Guide](../docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md). Each template's chapter skeleton corresponds one-to-one with that type's responsibility in [chapter 02 — Document Types](../docs/engineering/documentation/mdg-001-documentation-authority-guide/02-document-types.md), and its file layout follows [chapter 07 — Repository Organisation](../docs/engineering/documentation/mdg-001-documentation-authority-guide/07-repository-organisation.md).

Where a template and MDG-001 disagree, MDG-001 governs and the template is a defect.

## Why This Directory Is Outside `docs/`

Templates are not specifications. They live at the repository root so that:

- MkDocs never renders them as pages, since `docs_dir` is `docs/`;
- `scripts/validate_docs.py` never scans them, so placeholder identifiers such as `MAD-NNN` and unresolved link targets do not register as documentation defects.

No `exclude_docs` entry is required. That setting only affects files inside `docs/`.

## Using A Template

1. Copy the type folder into the correct discipline directory. [MDG-001 chapter 07](../docs/engineering/documentation/mdg-001-documentation-authority-guide/07-repository-organisation.md) defines where each type belongs.
2. Rename the folder to a URL-safe slug that keeps the document identifier visible, such as `mac-014-capability-routing`.
3. Rewrite every `File:` metadata value to the real repository-relative path of that file. Stale `File:` values fail validation.
4. Replace `MAD-NNN` and similar placeholders with the real identifier, and update the `.pages` title.
5. Delete every guidance comment as you replace it. A guidance comment left in a published specification is a defect.
6. Delete any chapter the specification genuinely does not need, and add chapters where the subject requires them. The skeleton is a floor, not a ceiling.
7. Add the folder to the parent `.pages` navigation.
8. Run `python3 scripts/validate_docs.py` before committing.

Every template ships with `Status: Draft`. Advance it only through a real lifecycle transition, as defined by [chapter 03 — Status And Versioning](../docs/engineering/documentation/mdg-001-documentation-authority-guide/03-versioning.md). No template carries a `Version` field, because prose documents do not have one.

## The Templates

| Template | Type | Answers | Destination |
|----------|------|---------|-------------|
| [`mdp/`](mdp) | Mosaic Design Proposal | What should we build? | `docs/engineering/architecture/` |
| [`mad/`](mad) | Mosaic Architecture Decision | Why was this decided? | `docs/engineering/architecture/` |
| [`mac/`](mac) | Mosaic Architecture Canon | What is Mosaic? | `docs/engineering/architecture/` |
| [`meg/`](meg) | Mosaic Engineering Guide | How should engineers build it? | `docs/engineering/guides/` |
| [`mip/`](mip) | Mosaic Integration Protocol | How do components communicate? | `docs/engineering/protocols/` |
| [`mop/`](mop) | Mosaic Operations & Playbook | How do operators run it? | `docs/engineering/operations/` |
| [`mdg/`](mdg) | Mosaic Documentation Guide | How should documentation be written? | `docs/engineering/documentation/` |
| [`mdl/`](mdl) | Mosaic Design Language | How should Mosaic look and behave? | `docs/design/language/` |
| [`mds/`](mds) | Mosaic Design System | What reusable design assets exist? | `docs/design/system/` |
| [`mrm/`](mrm) | Mosaic Roadmap | What is delivered, and in what order? | `docs/roadmaps/` |

## What Each Template Enforces

The skeletons are deliberately minimal, so that structure alone keeps the types apart.

**`mdp/`** — Problem, objectives, proposed solution, alternatives, anticipated impact, unresolved questions. Every page states that the proposal is non-authoritative. Proposal lifecycle is carried by `Status`, which for MDP documents also admits `Deferred`, `Accepted`, `Rejected` and `Withdrawn`. There is no separate `Disposition` field.

**`mad/`** — Context, decision, alternatives considered, consequences, implementation implications. Codified from the shared skeleton of [MAD-001](../docs/engineering/architecture/mad-001-transactional-store-extensibility/index.md) and [MAD-002](../docs/engineering/architecture/mad-002-module-storage-and-delivery-model/index.md). Document Control separates `Status`, which is the record's own lifecycle, from `Decision Status`, which is the decision's. The template has no chapter in which architecture could be defined, so a MAD cannot quietly grow into canon.

**`mac/`** — Philosophy, concepts, architectural model, responsibilities, relationships. Diátaxis explanation and reference. There is no chapter for alternatives, decision history, code samples or procedures, because those belong to MAD, MEG and MOP respectively.

**`meg/`** — Engineering philosophy, patterns, implementation guidance, anti-patterns, decision records, contributor guidance. The only type whose template invites code samples. It links the Canon it realises and states that the Canon governs.

**`mip/`** — Protocol model, contract structure, semantics, versioning and compatibility, validation. The only type that declares a version: the contract's major compatibility version, stated on the landing page and in Document Control, separate from the document's `Status`.

**`mop/`** — Operational model, procedures, monitoring and alerting, diagnostics and recovery, operational review. Procedures carry preconditions, steps, verification and rollback, written for an operator working under time pressure.

**`mdl/`** — Design philosophy, principles, experience model, governance, decision records, contributor guidance. Intent only. Concrete values are pushed to the Design System.

**`mds/`** — System philosophy, asset model, asset definitions, runtime resolution, governance, decision records, contributor guidance. Concrete assets, each recorded with the intent it carries, linked back to the Design Language that owns that intent.

**`mdg/`** — Scope and authority, standards, review expectations, governance. Subordinate to MDG-001 by construction; the template says so on the landing page and in Document Control.

**`mrm/`** — Release outcomes, scope and non-goals, delivery horizons, dependency sequence, completion evidence. Every outcome names its owning specification, and every horizon declares whether it is committed, candidate or research.

## Shared Structure

Every template contains, in this order:

```text
.pages
index.md
00-document-control.md
NN-...
references.md
glossary.md
```

`references.md` and `glossary.md` are unnumbered and always last, in that order. Guidance comments are HTML comments placed after the metadata block, never before it — the metadata comment must be the first thing in the file for tooling to find it.
