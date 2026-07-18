<!--
File: docs/engineering/guides/meg-006-module-platform/00-document-control.md
Document: MEG-006
Status: Draft
-->

# Document Control

---

# Document Information

| Field | Value |
|---------|--------|
| Document ID | MEG-006 |
| Title | Module Platform |
| File | 00-document-control.md |
| Status | Draft |
| Owner | AdamNi-7080 |
| Classification | Internal Architecture Specification |

---

# Purpose

This document establishes the governance, authority and lifecycle of the Mosaic Module Platform specification. MEG-006 defines how independently developed capabilities become part of the Mosaic platform, which makes it the mechanism through which the platform evolves without modifying the Platform.

Unlike Runtime Architecture, which defines **how capabilities execute**, this specification defines the path a capability travels before it ever runs:

- how capabilities are discovered
- how they are described
- how they are validated
- how they are composed into Platform packages
- how they become operational

Version 0.8 defines the Test Harness as a deterministic suite of development-only Modules, records event-simulation ownership and defers versioned Scenario Profiles pending a protocol decision.

---

# Authority

MEG-006 is the authoritative specification governing module development throughout the Mosaic ecosystem, and its authority extends to every route by which a capability reaches the platform rather than only to externally authored ones. It therefore applies to:

- Built-In Capabilities
- First-party Modules
- Third-party Modules
- Enterprise Modules
- SDK Development
- Developer Platform tooling
- Local Module development
- Test Harness Modules
- Test Harness deterministic datasets
- Test Harness event simulation
- deferred Scenario Profiles
- Marketplace Integration

Every capability intended to execute within the Mosaic Runtime should comply with this specification, whether it ships with the Platform or arrives from a third party. That breadth follows from the principle that built-in and third-party capabilities are architectural equals: a rule that applied only to external Modules would reintroduce the distinction the Module Platform exists to remove.

---

# Relationship to Other Specifications

MEG specifications intentionally build upon one another, so each one assumes the vocabulary the previous ones established.

```mermaid
flowchart TD

N1["MDL"]
N2["MDS"]
N3["MEG-001"]
N4["MEG-002"]
N5["MEG-003"]
N6["MEG-004"]
N7["MEG-005"]
N8["MEG-006"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Each guide in that chain settles one question before the next one is asked:

- **[MEG-001](../meg-001-go-engineering-standards/index.md)** defines engineering.
- **[MEG-002](../meg-002-event-driven-runtime/index.md)** defines runtime behaviour.
- **[MEG-003](../meg-003-domain-driven-design/index.md)** defines business modelling.
- **[MEG-004](../meg-004-hexagonal-architecture/index.md)** defines architectural boundaries.
- **[MEG-005](../meg-005-runtime-architecture/index.md)** defines the Capability Runtime.
- **MEG-006** defines how capabilities join that Runtime.

Together they establish the complete lifecycle of a Mosaic capability, from the way its code is written to the way it joins a running platform. MEG-006 is the last link in that chain, so it assumes the preceding definitions rather than restating them.

---

# Normative Language

Unless explicitly stated otherwise, the following keywords are interpreted according to RFC 2119. This table defines them, so it retains the uppercase convention; elsewhere in MEG-006 the same terms carry the same meaning in ordinary capitalisation.

| Keyword | Meaning |
|----------|---------|
| **MUST** | Mandatory requirement. |
| **MUST NOT** | Prohibited behaviour. |
| **SHOULD** | Strong recommendation. Deviation requires architectural justification. |
| **SHOULD NOT** | Discouraged except where clearly justified. |
| **MAY** | Optional behaviour based upon engineering judgement. |

Examples and diagrams are informative unless explicitly identified as normative, so an illustration in a later chapter never widens or narrows a requirement stated in prose.

---

# Module Principles

The Mosaic Module Platform is built upon several foundational principles, and the rest of this specification is largely an elaboration of them:

- Everything beyond the Runtime is a capability.
- Every capability is described by a manifest.
- Discovery precedes execution.
- Validation precedes activation.
- Module composition occurs at build time.
- Runtime plugins are prohibited.
- Runtime stability takes precedence over module flexibility.
- Capabilities remain independently deployable.
- Built-in and third-party capabilities are architectural equals.
- Modules evolve the platform without modifying the Runtime.

Every subsequent chapter expands one or more of these principles rather than introducing new ones, which makes this list the shortest complete statement of what the Module Platform is.

---

# Document Lifecycle

MEG specifications evolve alongside the platform, so each document progresses through a defined lifecycle rather than being published once and left alone.

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

Accepted specifications become part of the canonical Mosaic architecture, which is why historical revisions should remain available for future reference: a decision that has been superseded still explains why the current one was made.

---

# Platform Evolution

The Module Platform is expected to evolve. However, because a module ecosystem depends on contracts that outlive any single release, changes affecting:

- capability manifests
- registration
- discovery
- dependency resolution
- permissions
- activation
- SDK contracts
- build-time composition
- generated imports
- Developer Platform boundaries
- local development composition
- testing and publication workflow ownership

should be accompanied by an Architectural Decision Record (ADR), so that platform evolution remains deliberate and predictable rather than arriving as a surprise to the capabilities already built against those contracts.

---

# Compliance

All modules intended for the Mosaic Runtime should comply with MEG-006. Where deviation becomes necessary, module authors should document:

- architectural reason
- compatibility impact
- migration strategy
- operational implications

The Runtime should remain capable of validating compliance before activation, because a deviation discovered only once a capability is executing has already cost the platform the guarantee that validation precedes activation.

---

# Design Philosophy

Every preference recorded here serves a single objective, which is that the Runtime should understand a module completely before executing it. MEG-006 therefore intentionally favours:

- manifest-driven discovery
- explicit capability contracts
- deterministic build-time composition
- dependency validation
- runtime isolation
- version compatibility
- operational transparency

That preference is not unique to Mosaic. A machine-readable manifest describing identity, dependencies, permissions and capabilities has become the dominant approach for modern module ecosystems because it enables validation and discovery before code execution.  [Chrome for Developers](https://developer.chrome.com/modules/manifest)

---

# Scope of Authority

MEG-006 governs the Module Platform, and it does **not** define:

- business modelling
- runtime execution
- storage architecture
- deployment topology

Those concerns belong to other MEG specifications, because keeping module concerns separate from runtime concerns allows both to evolve independently.
