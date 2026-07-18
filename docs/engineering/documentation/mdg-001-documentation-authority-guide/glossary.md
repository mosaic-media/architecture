<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/glossary.md
Document: MDG-001
Status: Active
-->

# Glossary

---

# Purpose

This glossary defines terminology used throughout the Mosaic documentation library.

Terms defined here should be used consistently across every Mosaic specification.

Where a concept evolves, its definition should be updated in one authoritative location rather than allowing multiple conflicting definitions to emerge.

---

# Architecture Canon (MAC)

The collection of authoritative architectural specifications describing the accepted architecture of Mosaic.

The Canon defines **what Mosaic is** rather than how it is implemented.

---

# Architecture Decision (MAD)

A permanent record describing why an architectural decision was made.

Architecture Decisions preserve historical context, alternatives considered and the consequences of accepted architectural choices.

MAD documents are historical records and should remain immutable after acceptance.

---

# Build of Record

The officially accepted build produced from the current Platform, Supervisor and selected Modules.

The Build of Record represents the authoritative runtime produced by the Supervisor.

---

# Canon

The authoritative collection of accepted architectural specifications governing the Mosaic platform.

Within Mosaic, the Canon is represented by the MAC document series.

---

# Capability

A behaviour or responsibility exposed by the Mosaic Platform.

Capabilities are owned by the Platform and implemented by Modules.

Examples include:

- Metadata
- Media
- Artwork
- Authentication
- Search

---

# Capability Manager

A Platform component responsible for coordinating providers implementing a specific capability.

Capability Managers determine routing, orchestration, validation and provider selection.

---

# Contract Version

The major compatibility version of a contract defined by an Integration Protocol.

A contract version describes whether independently developed components interoperate. It belongs to the contract rather than to the document describing it, and uses a major integer only, such as `Event Protocol v1`.

Prose documents carry no version of any kind.

---

# Design Language (MDL)

The collection of documents defining the visual philosophy of Mosaic.

The Design Language establishes:

- materials
- motion
- interaction
- lighting
- presentation behaviour

MDL defines intent rather than implementation.

---

# Design Proposal (MDP)

A document proposing a significant architectural or design change.

Design Proposals are discussion documents.

Accepted proposals normally result in one or more Architecture Decisions.

Every MDP declares its lifecycle through Status, which for proposals additionally admits Deferred, Accepted, Rejected and Withdrawn.

---

# Design System (MDS)

The collection of reusable visual assets implementing the Mosaic Design Language.

Examples include:

- colours
- typography
- spacing
- icons
- components

---

# Documentation Guide (MDG)

A document defining standards governing Mosaic documentation.

Documentation Guides establish:

- writing standards
- organisational conventions
- review processes
- governance

---

# Engineering Guide (MEG)

A document explaining how engineers implement the Mosaic Architecture Canon.

Engineering Guides provide implementation guidance, examples and engineering practices while remaining aligned with the Canon.

---

# Event

A statement describing something that has occurred within the platform.

Events communicate facts.

They do not represent commands.

Modules may publish and subscribe to events through the Platform's Event Bus.

---

# Event Envelope

The standard structure used by the Platform to transport events independently of their payload.

The Event Envelope defines how events travel through the platform rather than the meaning of individual events.

---

# Integration Protocol (MIP)

A specification defining communication contracts between Mosaic components.

Protocols describe machine-readable interfaces including:

- manifests
- schemas
- APIs
- event formats

---

# Module

A statically compiled unit of functionality contributing capabilities to the Mosaic Platform.

Modules are ordinary Go projects built against the Mosaic SDK.

Modules are not runtime modules.

---

# Mosaic Platform

The compiled runtime responsible for executing Mosaic.

The Platform owns:

- capabilities
- orchestration
- permissions
- storage
- scheduling
- GraphQL
- the Event Bus

The Platform does not own application-specific behaviour.

---

# Mosaic Roadmap (MRM)

A planning document that defines release outcomes, delivery sequence, dependencies and completion evidence by reference to owning specifications and active proposals.

An MRM does not define architecture, Design Language, reusable assets, protocols or implementation requirements.

---

# Mosaic SDK

The public contract between the Platform and Modules.

The SDK defines:

- interfaces
- models
- events
- registration APIs
- helper utilities

The SDK intentionally contains minimal implementation.

---

# Operations & Playbook (MOP)

A document describing operational procedures associated with the Mosaic platform.

Operations documentation includes:

- deployment
- upgrades
- recovery
- diagnostics
- maintenance

---

# Platform

See **Mosaic Platform**.

---

# Provider

A Module implementation satisfying a Platform capability.

Examples include:

- Metadata Provider
- Media Provider
- Artwork Provider

Multiple providers may satisfy the same capability depending upon Platform policy.

---

# Proposal Disposition

A retired field previously used to classify an MDP independently from its document Status.

Proposal lifecycle is now expressed through Status. Existing MDP documents retaining a `Disposition` row within Document Control keep it as a legacy alias until migrated. Where the two disagree, Status governs.

---

# Reference Implementation

The implementation considered authoritative for validating architectural behaviour.

Reference implementations should remain aligned with the Architecture Canon.

---

# Repository Discipline

The highest-level organisational grouping within the Mosaic Architecture repository.

Examples include:

- Engineering
- Design

Repository disciplines organise documentation by subject matter rather than document type.

---

# Specification

A self-contained architectural publication composed of multiple chapters.

Every specification contains:

- `index.md`
- Document Control
- numbered chapters
- References
- Glossary

Specifications are treated as complete publications rather than collections of unrelated Markdown files.

---

# Status

The declared authority of a document.

Status answers whether a reader may rely upon a document. Valid values are Draft, Review, Active, Deprecated and Superseded, with Deferred, Accepted, Rejected and Withdrawn additionally available to Mosaic Design Proposals.

Status replaces the numeric document version formerly used to communicate maturity.

---

# Supervisor

The permanent control plane responsible for managing the Mosaic runtime.

Responsibilities include:

- lifecycle management
- runtime composition
- updates
- recovery
- diagnostics
- rollback
- shell deployment

The Supervisor exists independently of the Platform runtime.

---

# Traceability

The ability to follow architectural concepts through proposals, decisions, specifications and implementation using documented relationships and references.

Traceability reduces duplication while preserving architectural history.
