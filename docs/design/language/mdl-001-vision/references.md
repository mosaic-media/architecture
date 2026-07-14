<!--
File: docs/design/language/mdl-001-vision/references.md
Document: MDL-001
Title: References
Status: Draft
Version: 0.4
-->

# References

---

# Purpose

This document records the external references that informed MDL-001.

MDL is intentionally **not** derived from any single design system.

Instead, Mosaic synthesises ideas from multiple disciplines including:

- Human-centred design
- Product design
- Architecture
- Systems thinking
- Information architecture
- Software architecture

These references exist to provide context for future contributors.

They are **not** normative requirements.

---

# Reading Order

Future contributors are encouraged to read references in the following order.

1. Product Vision
2. Human Interface Design
3. Design Systems
4. Architecture Decision Records
5. Systems Architecture
6. Documentation Standards

---

# Human Interface Design

## Apple Human Interface Guidelines

Apple Inc.

https://developer.apple.com/design/human-interface-guidelines/

Referenced throughout MDL for:

- experience-first thinking
- consistency
- hierarchy
- interaction philosophy

**Not adopted directly.**

---

## Material Design

Google

https://m3.material.io/

Referenced for:

- design system organisation
- documentation structure
- token hierarchy

Material Design intentionally differs philosophically from MDL.

---

## Fluent Design

Microsoft

https://fluent2.microsoft.design/

Referenced for:

- adaptive interface systems
- cross-device thinking
- design governance

---

# Architecture

## Architectural Decision Records

Michael Nygard

https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

Referenced for:

- ADR structure
- architectural traceability
- decision preservation

Additional ADR guidance:

- Martin Fowler — Architecture Decision Record
- UK Government ADR Framework
- AWS ADR Guidance  [martinfowler.com](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)

---

## RFC Process

RFC Editor

https://www.rfc-editor.org/

Referenced for:

- document lifecycle
- versioning
- governance
- specification process

Relevant examples:

- RFC 2026
- RFC 3426
- RFC 7764  [RFC Editor](https://www.rfc-editor.org/rfc/rfc2026.html)

---

# Documentation

## Markdown Documentation

Markdown is the canonical source format for MDL.

Generated formats including:

- PDF
- HTML
- mdBook
- MkDocs

are considered publication artefacts.

The Markdown repository remains authoritative.

---

## Documentation As Code

Referenced principles include:

- version control
- peer review
- pull requests
- changelog
- traceability

Documentation should evolve using the same workflow as software.

---

# Product Philosophy

The following product philosophies strongly influenced MDL.

## Experience Before Interface

Software should support experiences rather than become experiences.

---

## Systems Before Features

Long-term maintainability is achieved through reusable systems rather than isolated feature development.

---

## Calm Technology

Technology should remain in the background until needed.

While not directly implemented, this philosophy aligns closely with the intended behaviour of Mosaic as a trusted entertainment companion.

---

# Design Language Inspirations

MDL intentionally studies—but does not attempt to replicate—the following systems.

| System | Inspiration |
|----------|-------------|
| Apple Human Interface Guidelines | Product philosophy |
| Material Design | Documentation structure |
| Fluent Design | Cross-device thinking |
| Carbon Design System | Enterprise governance |
| Atlassian Design System | Documentation quality |
| IBM Enterprise Design Thinking | Decision making |

MDL deliberately avoids inheriting visual identity from any existing design language.

Its objective is to create an original philosophy suitable for entertainment software.

---

# Mosaic-Specific Sources

The following documents directly informed MDL-001.

## Founder Discovery Workshops

Conducted during the initial design engagement.

Topics included:

- Product Vision
- Product Beliefs
- Mental Model
- Companion Philosophy
- Adaptive Composition
- Information Architecture
- Material Metaphor

These workshops are considered the primary source for MDL.

---

## Mosaic Platform Roadmap

The Mosaic roadmap establishes the long-term technical direction of the platform.

MDL intentionally remains implementation independent while ensuring philosophical alignment with that roadmap.

---

# Normative References

The following documents should be considered required reading for contributors working on MDL.

- MDL-001 Vision
- [MDL-002 — Principles](../mdl-002-principles/index.md)
- [MDL-003 — Mental Model](../mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../mdl-004-interaction-model/index.md)
- [MDL-005 — Composition Model](../mdl-005-composition-model/index.md)

---

# Informative References

The following documents provide additional context.

- [MDS-001 — Design Token Architecture](../../system/mds-001-design-token-architecture/index.md)
- [MDS-003 — Material System](../../system/mds-003-material-system/index.md)
- [MDS-006 — Composition Engine](../../system/mds-006-composition-engine/index.md)
- Future ADRs
- Engineering RFCs

These documents may evolve independently while remaining consistent with MDL.

---

# Living References

This reference list is intentionally expected to evolve.

New references should only be added when they:

- influenced a significant design decision,
- provide historical context,
- explain architectural reasoning, or
- materially improve contributor understanding.

References should not become an exhaustive catalogue of design literature.

Quality is preferred over quantity.
