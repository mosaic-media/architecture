<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/00-document-control.md
Document: MEG-004
Status: Draft
-->

# Document Control

---

# Document Information

| Field | Value |
|---------|--------|
| Document ID | MEG-004 |
| Title | Hexagonal Architecture |
| File | 00-document-control.md |
| Status | Draft |
| Owner | AdamNi-7080 |
| Classification | Internal Architecture Specification |

---

# Purpose

This document establishes the governance, authority and lifecycle of the Mosaic Hexagonal Architecture specification.

MEG-004 defines the architectural rules governing how the Domain Model interacts with infrastructure.

Unlike implementation documentation, this specification defines **dependency boundaries**, not implementation details.

Its primary purpose is to ensure that the Domain remains independent of technology for the lifetime of the Mosaic platform.

---

# Authority

MEG-004 is the authoritative specification governing architectural boundaries throughout the Mosaic ecosystem.

This specification applies to:

- Mosaic Platform
- First-party Modules
- Third-party Modules
- Runtime Capabilities
- SDKs
- Infrastructure Components

Every capability developed within the Mosaic platform SHOULD comply with the dependency rules established by this specification.

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
N6["MEG-004"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Specifically:

- **MDL** defines product philosophy.
- **MDS** defines presentation.
- **[MEG-001](../meg-001-go-engineering-standards/index.md)** defines engineering standards.
- **[MEG-002](../meg-002-event-driven-runtime/index.md)** defines runtime behaviour.
- **[MEG-003](../meg-003-domain-driven-design/index.md)** defines business modelling.
- **MEG-004** defines dependency boundaries.

Future specifications build upon the architectural separation established here.

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

# Architectural Principles

The Mosaic Hexagonal Architecture is built upon several foundational principles.

- The Domain owns business behaviour.
- Dependencies flow towards the Domain.
- Infrastructure adapts to the Domain.
- Ports define contracts.
- Adapters implement contracts.
- Technology remains replaceable.
- Business logic remains isolated.
- The Domain never imports infrastructure.

Every subsequent chapter expands one or more of these principles.

---

# Document Lifecycle

MEG specifications evolve alongside the platform.

Each document progresses through the following lifecycle.

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

Accepted specifications become part of the canonical Mosaic architecture.

Historical versions SHOULD remain available for future reference.

---

# Architectural Evolution

Hexagonal Architecture is intentionally stable.

Changes affecting:

- dependency direction
- port definitions
- adapter responsibilities
- application services
- runtime integration
- infrastructure boundaries

SHOULD be accompanied by an Architectural Decision Record (ADR).

Architectural consistency should remain more important than implementation convenience.

---

# Compliance

All repositories implementing Mosaic capabilities SHOULD comply with MEG-004.

Where deviation becomes necessary, the repository SHOULD document:

- the reason
- affected boundaries
- architectural impact
- migration strategy

Temporary deviations should eventually be removed.

Permanent deviations should generally result in updates to this specification.

---

# Design Philosophy

MEG-004 intentionally favours:

- explicit dependencies
- replaceable infrastructure
- domain independence
- clear ownership
- technology isolation
- long-term maintainability

The architecture should continue functioning even if:

- databases change
- frameworks change
- transports change
- infrastructure changes

Only the adapters should require modification.

The Domain should remain unchanged.

Hexagonal Architecture exists precisely to achieve this separation between business logic and infrastructure by ensuring dependencies point inward towards the application core. ([alistair.cockburn.us](https://alistair.cockburn.us/hexagonal-architecture))

---

# Scope of Authority

MEG-004 governs architectural boundaries.

It does **not** define:

- business behaviour
- runtime execution
- storage technologies
- deployment topology
- user interface design

Those concerns belong to other MEG specifications.

Keeping these concerns separate allows each architectural layer to evolve independently.
