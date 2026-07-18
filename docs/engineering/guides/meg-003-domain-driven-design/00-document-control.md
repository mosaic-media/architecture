<!--
File: docs/engineering/guides/meg-003-domain-driven-design/00-document-control.md
Document: MEG-003
Status: Draft
-->

# Document Control

---

# Document Information

| Field | Value |
|---------|--------|
| Document ID | MEG-003 |
| Title | Domain-Driven Design |
| File | 00-document-control.md |
| Status | Draft |
| Owner | AdamNi-7080 |
| Classification | Internal Architecture Specification |

---

# Purpose

This document establishes the governance, authority and lifecycle of the Mosaic Domain-Driven Design specification. MEG-003 defines the canonical approach to modelling business domains throughout the Mosaic platform, so unlike implementation documentation it describes how business complexity is understood, organised and communicated rather than how it is built. That separation of business thinking from implementation thinking is intentional, and it shapes everything the specification governs.

---

# Authority

MEG-003 is the authoritative specification governing business modelling within the Mosaic ecosystem. Its reach is deliberately broad, because a modelling standard observed only by the platform would not produce the shared language it exists to create. This specification therefore applies to:

- Mosaic Platform
- First-party Modules
- Third-party Modules
- SDK Development
- Runtime Capabilities
- Future Platform Features

Every business capability introduced into Mosaic should align with the modelling principles defined within this specification.

---

# Relationship to Other Specifications

MEG specifications intentionally build upon one another.

```mermaid
flowchart TD

N1["MDL"]
N2["MDS"]
N3["MEG-001"]
N4["MEG-002"]
N5["MEG-003"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Specifically:

- **MDL** defines product philosophy.
- **MDS** defines presentation.
- **[MEG-001](../meg-001-go-engineering-standards/index.md)** defines engineering practices.
- **[MEG-002](../meg-002-event-driven-runtime/index.md)** defines runtime behaviour.
- **MEG-003** defines business modelling.

Future specifications use the domain model established here as the foundation for architectural boundaries.

---

# Normative Language

Unless explicitly stated otherwise, the following keywords are interpreted according to RFC 2119.

| Keyword | Meaning |
|----------|---------|
| **MUST** | Mandatory requirement. |
| **MUST NOT** | Prohibited behaviour. |
| **SHOULD** | Strong recommendation. Deviation requires architectural justification. |
| **SHOULD NOT** | Discouraged except where clearly justified. |
| **MAY** | Optional behaviour based upon engineering judgement. |

Examples and diagrams are informative unless explicitly identified as normative.

---

# Domain Principles

The Mosaic domain model is built upon several foundational principles.

- Business language comes first.
- Software reflects the business.
- Every concept has one meaning within one context.
- Contexts own their own models.
- Business behaviour belongs inside the domain.
- Technical concerns remain outside the domain.
- Domain models evolve continuously as understanding improves.
- Simplicity is preferred over theoretical completeness.

Every subsequent chapter expands one or more of these principles.

---

# Document Lifecycle

MEG specifications evolve alongside the platform, and each document progresses through the following lifecycle.

```mermaid
flowchart TD

N1["Draft"]
N2["Review"]
N3["Accepted"]
N4["Implemented"]
N5["Maintained"]
N6["Superseded (optional)"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Accepted specifications become part of the canonical Mosaic architecture. Historical versions should remain available for future reference, so that the evolution of the architecture stays traceable.

---

# Domain Evolution

Business understanding is expected to evolve, and consequently the domain model will evolve with it. Not every such change carries the same weight, but changes affecting:

- bounded contexts
- ubiquitous language
- aggregates
- business ownership
- domain relationships
- core business concepts

should be accompanied by an Architectural Decision Record (ADR). The evolution of the business model should remain deliberate and historically traceable, and the ADR is what records that intent at the moment it is formed.

---

# Compliance

All business capabilities should comply with MEG-003. Where deviation becomes necessary, the repository should document:

- the reason
- business motivation
- architectural implications
- migration strategy

Temporary deviations should eventually be removed, whereas permanent deviations should generally result in updates to this specification. A deviation that is neither removed nor absorbed leaves the specification describing a platform that no longer exists.

---

# Design Philosophy

MEG-003 intentionally favours:

- business-first thinking
- explicit ownership
- cohesive models
- bounded complexity
- expressive language
- evolutionary modelling

The domain model should become deeper as the platform matures, and it should never become more technical. This follows the central ideas of Domain-Driven Design: focusing on the Platform foundation domain, collaborating around a ubiquitous language and modelling within explicitly bounded contexts.  [Google Books](https://books.google.com/books/about/Domain_Driven_Design_Reference.html?id=ccRsBgAAQBAJ)

---

# Scope of Authority

MEG-003 governs business modelling. It does **not** define:

- runtime execution
- event delivery
- scheduling
- transport protocols
- storage technologies
- deployment architecture

Those concerns belong to other MEG specifications. Separating business modelling from technical implementation allows each to evolve independently.
