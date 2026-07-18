<!--
File: docs/engineering/guides/meg-006-module-platform/references.md
Document: MEG-006
Status: Draft
-->

# References

> *The Module Platform is built upon decades of experience in module architectures, capability systems and software platforms, adapted into a capability-oriented ecosystem for Mosaic.*

---

# Purpose

This document records the primary references that influenced the Module Platform described throughout MEG-006.

Unlike a traditional module system, the Mosaic Module Platform combines ideas from:

- Module Architecture
- Microkernel Architecture
- Capability-Oriented Design
- Manifest-Driven Platforms
- SDK Design
- Runtime Composition

into a single platform model.

The objective is not to imitate existing systems.

It is to adapt proven architectural principles into a platform capable of evolving for many years.

---

# Primary References

## Eclipse Module Architecture

The Eclipse Platform remains one of the most influential module architectures ever developed.

Relevant concepts include:

- module manifests
- module boundaries
- module registry
- runtime discovery
- deployment-time composition

Many architectural ideas behind capability discovery and registration align closely with Eclipse's module registry, although Mosaic replaces module boundaries with capability contracts.  [Eclipse Foundation](https://www.eclipse.org/articles/Article-Plug-in-architecture/plugin_architecture.html)

---

## Microkernel Architecture

Microkernel architecture strongly influenced:

- Runtime Kernel
- Runtime Services
- Module isolation
- build-time capability composition

Within Mosaic:

The Runtime remains intentionally small.

Capabilities provide platform functionality.

This mirrors the architectural philosophy of microkernel operating systems while adapting it to an application platform.  [arc42 Quality Model](https://quality.arc42.org/approaches/plugin-architecture)

---

# Manifest-Driven Platforms

## Manifest-First Discovery

Modern module platforms increasingly separate:

- discovery
- validation
- activation
- execution

through machine-readable manifests.

This strongly influenced:

- Capability Manifest
- Discovery
- Registration
- Dependency Resolution

Within Mosaic, manifests are intentionally treated as architectural contracts rather than implementation details.  [OpenClaw](https://docs.openclaw.ai/modules/architecture-internals)

---

## Module Manifests

Modern browser module ecosystems demonstrate the value of:

- explicit permissions
- declarative metadata
- schema validation
- compatibility checking

Many permission and manifest concepts within MEG-006 were inspired by these approaches while remaining platform agnostic.  [emdashcms.org](https://emdashcms.org/learn/module-system)

---

# SDK Design

The Module SDK intentionally follows long-established SDK principles.

Relevant concepts include:

- stable contracts
- implementation hiding
- backwards compatibility
- explicit versioning

The SDK should remain considerably more stable than the Runtime implementation beneath it.

This separation protects module authors from internal Runtime evolution.

---

# Dependency Management

Dependency Resolution within Mosaic draws inspiration from module systems that:

- validate dependency graphs
- detect cycles
- resolve versions
- construct activation order

The Runtime intentionally performs these operations before executing capability code.  [GitHub](https://ithub.global.ssl.fastly.net/open-gsd/gsd-core/blob/next/docs/reference/capability-manifest.md)

---

# Capability-Oriented Design

Although "Capability-Oriented Architecture" is not yet a widely standardised software architecture term, several modern platforms have independently converged upon similar ideas.

Common themes include:

- capability discovery
- capability registries
- manifest-driven execution
- contract-based integration
- runtime validation

Mosaic extends these ideas into a unified Runtime Architecture centred around independently evolving business capabilities.  [Extentos](https://extentos.com/docs/concepts/capabilities)

---

# Software Engineering References

## Domain-Driven Design

**Author**

Eric Evans

The Module Platform deliberately preserves the Domain boundaries defined in [MEG-003](../meg-003-domain-driven-design/index.md).

Capabilities own:

- business behaviour
- business language
- business state

The Runtime owns execution.

---

## Hexagonal Architecture

**Author**

Alistair Cockburn

The Module Platform builds directly upon:

- Ports
- Adapters
- dependency inversion
- infrastructure isolation

Modules communicate exclusively through Runtime contracts.

Runtime implementation remains hidden.

---

## Clean Architecture

**Author**

Robert C. Martin

Referenced primarily for:

- dependency direction
- policy vs implementation
- long-term maintainability

Many Runtime contracts intentionally reinforce these architectural principles.

---

# Go References

The Module SDK intentionally embraces idiomatic Go.

Recommended references include:

## Effective Go

Topics include:

- interfaces
- package design
- composition
- explicit construction

https://go.dev/doc/effective_go

---

## Go Code Review Comments

Topics include:

- interface ownership
- dependency management
- package boundaries

https://go.dev/wiki/CodeReviewComments

---

# Internal Mosaic Specifications

The following specifications complement MEG-006.

## Engineering

- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)
- [MEG-002 — Event-Driven Runtime](../meg-002-event-driven-runtime/index.md)
- [MEG-003 — Domain-Driven Design](../meg-003-domain-driven-design/index.md)
- [MEG-004 — Hexagonal Architecture](../meg-004-hexagonal-architecture/index.md)
- [MEG-005 — Runtime Architecture](../meg-005-runtime-architecture/index.md)

---

## Planned Engineering Specifications

- [MEG-007 — Storage Architecture](../meg-007-storage-architecture/index.md)
- [MEG-008 — Observability](../meg-008-observability/index.md)
- [MEG-009 — Security Architecture](../meg-009-security-architecture/index.md)
- [MEG-010 — Performance Engineering](../meg-010-performance-engineering/index.md)

---

## Mosaic Design Language

- [MDL-001 — Mosaic Design Language Vision](../../../design/language/mdl-001-vision/index.md)
- [MDL-002 — Principles](../../../design/language/mdl-002-principles/index.md)
- [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../../../design/language/mdl-004-interaction-model/index.md)
- [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md)

---

## Mosaic Design Specifications

- [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/index.md)
- [MDS-002 — Colour System](../../../design/system/mds-002-colour-system/index.md)
- [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md)
- [MDS-004 — Typography System](../../../design/system/mds-004-typography-system/index.md)
- [MDS-005 — Motion System](../../../design/system/mds-005-motion-system/index.md)
- [MDP-001 — Adaptive Composition Runtime](../../architecture/mdp-001-adaptive-composition-runtime/index.md)
- [MDP-001 — Adaptive Composition Runtime](../../architecture/mdp-001-adaptive-composition-runtime/14-adaptive-tile-model.md)
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)

---

# Platform Principles

The Module Platform established throughout MEG-006 intentionally builds upon several enduring architectural principles.

These include:

- The Runtime remains small.
- Capabilities provide business value.
- Discovery precedes execution.
- Manifests define contracts.
- SDKs hide implementation.
- Permissions follow least privilege.
- Dependencies remain explicit.
- Capabilities remain independently deployable.
- Built-in and module-delivered capabilities are architectural equals.
- Platform growth occurs through composition rather than modification.

These principles should remain considerably more stable than the implementation techniques used to realise them.

---

# Keeping References Current

Module platforms continue to evolve.

Marketplace ecosystems continue to mature.

Manifest standards continue to improve.

This reference list SHOULD therefore be reviewed periodically to ensure:

- architectural guidance remains relevant
- obsolete practices are removed
- better ecosystem patterns are incorporated

The platform philosophy should remain stable even as module technology evolves.

---

# Closing Statement

MEG-006 intentionally does not describe a traditional module framework.

Instead, it describes an ecosystem architecture built around independently evolving capabilities.

The resulting Module Platform intentionally emphasises:

- capability-oriented design
- manifest-first discovery
- Runtime stability
- SDK contracts
- explicit permissions
- long-term ecosystem evolution

Every future capability should integrate into the platform by satisfying Runtime contracts rather than modifying Runtime implementation.

The Runtime provides execution.

Capabilities provide value.

The platform exists so that those capabilities can continue evolving long after the Runtime itself has stabilised.
