<!--
File: docs/engineering/guides/meg-006-extension-platform/index.md
Document: MEG-006
Status: Draft
Version: 0.1
-->

# MEG-006 — Extension Platform

> *The Runtime provides execution. Extensions provide evolution.*

---

# Purpose

The previous engineering specifications established:

- how software is written
- how the Runtime executes
- how the business is modelled
- how the Domain is protected
- how the Runtime itself is structured

MEG-006 answers the final architectural question.

> **How does the platform evolve without modifying Core?**

The Mosaic Extension Platform allows new capabilities to be:

- installed
- discovered
- validated
- loaded
- executed
- upgraded
- removed

without changing the Runtime itself.

Unlike traditional plugin systems, extensions are not an afterthought.

They are a first-class architectural concept.

The Runtime is intentionally designed to grow through extensions rather than through continual modification of Core.

---

# Relationship to MEG

```
MEG-001

↓

Engineering Standards

↓

MEG-002

↓

Reactive Runtime

↓

MEG-003

↓

Domain Model

↓

MEG-004

↓

Hexagonal Architecture

↓

MEG-005

↓

Capability Runtime

↓

MEG-006

↓

Extension Platform
```

MEG-005 defines:

> **How the Runtime executes capabilities.**

MEG-006 defines:

> **How new capabilities become part of that Runtime.**

---

# Scope

This specification defines:

- Extension philosophy
- Extension lifecycle
- Extension manifest
- Capability manifests
- Discovery
- Registration
- Activation
- Dependency resolution
- Extension contracts
- Extension permissions
- Configuration
- Versioning
- Compatibility
- Isolation
- SDK architecture

This specification intentionally does **not** define:

- business domains
- runtime internals
- storage architecture
- deployment topology

Those concerns belong to previous or future MEG specifications.

---

# Core Question

MEG-006 exists to answer one question.

> **How should Mosaic evolve through independently developed capabilities while preserving Runtime stability?**

---

# Extension Statement

Within Mosaic:

> **Everything beyond the Runtime is a capability. Every capability may be delivered as an extension.**

Core capabilities.

Third-party capabilities.

Enterprise capabilities.

Experimental capabilities.

The Runtime should treat them identically.

The only distinction should be **how they are delivered**, not **how they execute**.

---

# Platform Hierarchy

The Mosaic platform intentionally separates concerns into architectural layers.

```
Runtime Kernel

↓

Runtime Services

↓

Capability Registry

↓

Capabilities

↓

Extensions

↓

Business Behaviour
```

Notice:

The Runtime never grows by adding business logic.

It grows by loading additional capabilities.

---

# Expected Outcome

After reading MEG-006 contributors should understand:

- how extensions are discovered
- how capabilities register
- how manifests define platform contracts
- how dependencies are validated
- how extensions integrate with the Runtime
- how permissions are enforced
- how extensions evolve safely
- how Core and third-party capabilities coexist

without modifying the Runtime itself.

---

# Repository Structure

```
engineering/

└── meg/

    └── MEG-006 Extension Platform/

        README.md

        00-document-control.md

        01-extension-philosophy.md

        02-capability-manifest.md

        03-discovery.md

        04-registration.md

        05-dependency-resolution.md

        06-activation.md

        07-extension-lifecycle.md

        08-extension-sdk.md

        09-permissions.md

        10-configuration.md

        11-versioning.md

        12-isolation.md

        13-platform-guidelines.md

        14-adrs.md

        15-contributor-guidance.md

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Runtime Architecture

Future companion specifications:

- MEG-007 Storage Architecture
- MEG-008 Observability
- MEG-009 Security

---

# Design Goals

The Extension Platform is intended to produce a platform that is:

- Extensible
- Discoverable
- Manifest driven
- Capability oriented
- Version aware
- Secure
- Replaceable
- Operationally predictable

Every extension should feel like a natural part of the platform rather than an external add-on.

Manifest-driven discovery and registration have become the dominant architecture for extensible platforms because they allow capabilities to be discovered, validated and loaded before execution.  [oai_citation:0‡zylos.ai](https://zylos.ai/research/2026-02-21-ai-agent-plugin-extension-architecture/?utm_source=chatgpt.com)

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Next File**

`00-document-control.md`
