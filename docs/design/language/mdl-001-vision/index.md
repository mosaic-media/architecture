<!--
File: docs/design/language/mdl-001-vision/index.md
Document: MDL-001
Status: Draft
-->

# MDL-001 — Mosaic Design Language Vision

> *Mosaic exists to remove the friction between people and the entertainment they love.*

---

## Purpose

MDL-001 is the constitutional document of the Mosaic Design Language (MDL).

Unlike traditional design specifications, this document does **not** define colours, typography, layouts or components.

Instead it defines **why** Mosaic exists.

Every future design and engineering decision should be traceable back to the philosophy established here.

If another MDL or MDS specification appears to conflict with MDL-001, that specification should be reconsidered before this document is modified.

---

## Scope

This specification defines:

- Product vision
- Product beliefs
- Design philosophy
- Long-term objectives
- Contributor mindset
- Design governance

This specification intentionally does **not** define:

- Colour systems
- Typography
- Motion
- Components
- Design tokens
- Layout rules
- Engineering implementation

Those concerns are defined by later MDL and MDS specifications.

---

# Specification Structure

- 00 Document Control
- 01 Background & Problem Statement
- 02 Vision
- 03 Product Beliefs
- 04 Goals
- 05 Non-Goals
- 06 Design Philosophy
- 07 Governance
- 08 Architectural Decision Records
- 09 Contributor Guidance
- 10 Design Review Checklist
- 11 Future Considerations
- References
- Glossary

---

# Dependencies

This specification has no dependencies.

All remaining MDL specifications depend on MDL-001.

```mermaid
flowchart TD

MDL001["MDL-001 Vision"]

MDL001 --> MDL002["MDL-002 Principles"]
MDL001 --> MDL003["MDL-003 Mental Model"]
MDL001 --> MDL004["MDL-004 Interaction Model"]
MDL001 --> MDL005["MDL-005 Composition Model"]

MDL001 --> MDS001["MDS-001 Design Token Architecture"]
MDL001 --> MDS002["MDS-003 Material System"]
MDL001 --> MDS003["MDP-001 — Adaptive Composition Runtime"]
```

---

# Repository Convention

Each chapter exists as an individual Markdown document.

This intentionally mirrors software architecture.

Small documents:

- review more easily
- version more cleanly
- minimise merge conflicts
- encourage focused discussion
- can be assembled into PDF, mdBook or documentation websites using tooling such as mdBook's `SUMMARY.md` and `book.toml`.  [Rust Language](https://rust-lang.github.io/mdBook/guide/creating.html)
