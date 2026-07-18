<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/index.md
Document: MDG-001
Status: Active
-->

# MDG-001 — Documentation Authority Guide

> *Architecture is built from decisions. Decisions are preserved through documentation. Documentation is therefore part of the architecture itself.*

---

# Purpose

Mosaic is intended to evolve over many years.

During that time:

- contributors will join and leave
- technologies will change
- implementations will be rewritten
- ideas will mature
- assumptions will be challenged

Without a consistent documentation system, the architecture itself becomes difficult to understand, maintain and evolve.

Documentation is therefore treated as a first-class engineering discipline.

MDG-001 establishes the governing principles for every document produced within the Mosaic Architecture repository.

It defines:

- the philosophy of documentation
- documentation responsibilities
- document taxonomy
- authorship standards
- the document status lifecycle
- review requirements
- organisational conventions
- the open standards each document type profiles

Rather than documenting Mosaic itself, this guide documents **how Mosaic documentation is created and maintained**.

Every Architecture Canon, Engineering Guide, Integration Protocol, Design Language specification and Operations Playbook derives its structure and intent from this guide.

---

# Scope

This document governs documentation contained within the Mosaic Architecture repository.

This includes, but is not limited to:

- Mosaic Architecture Canon (MAC)
- Mosaic Design Proposals (MDP)
- Mosaic Roadmaps (MRM)
- Mosaic Architecture Decisions (MAD)
- Mosaic Engineering Guides (MEG)
- Mosaic Integration Protocols (MIP)
- Mosaic Operations & Playbooks (MOP)
- Mosaic Design Language (MDL)
- Mosaic Design System (MDS)
- Mosaic Documentation Guides (MDG)

Future documentation types shall follow the principles defined here unless explicitly stated otherwise.

---

# Documentation Philosophy

Documentation is not an afterthought.

Documentation is not generated solely to satisfy process.

Documentation is not a copy of implementation.

Instead, documentation is treated as the authoritative description of Mosaic.

Implementation exists to realise the documented architecture.

Where implementation and documentation diverge, one of two things must happen:

- the implementation must change to match the documentation; or
- the documentation must be formally revised to reflect an accepted architectural change.

Documentation therefore becomes the long-term memory of the project.

It captures:

- architectural intent
- engineering principles
- accepted decisions
- integration contracts
- operational knowledge

while remaining independent of any particular implementation language or technology.

---

# Guiding Principles

Every Mosaic document should strive to satisfy the following principles.

## Authority

Documentation represents the authoritative understanding of the system.

It should never speculate about implementation behaviour.

## Longevity

Documentation should outlive implementations.

Technologies may change.

Architectural principles should remain understandable many years later.

## Clarity

Documentation should explain ideas before describing mechanisms.

Readers should understand *why* before learning *how*.

## Separation of Concerns

Each document type exists for a specific purpose.

Documents should not duplicate responsibilities belonging to another document type.

## Stability

Accepted architectural documentation should evolve deliberately rather than continuously.

Frequent implementation changes should rarely require changes to the Canon.

## Traceability

Architectural concepts should be traceable across the documentation set through references rather than duplication.

## Consistency

Readers should encounter familiar structure regardless of document type.

Navigation, terminology and organisation should remain predictable throughout the repository.

---

# Intended Audience

The Mosaic documentation is written for multiple audiences.

These include:

- platform architects
- software engineers
- module developers
- designers
- contributors
- maintainers
- future project owners

Documentation should therefore assume technical competence while remaining accessible to readers unfamiliar with the implementation history.

---

# Relationship to Other Documents

MDG-001 governs every document contained within the Mosaic Architecture repository.

It does not replace those documents.

Instead, it defines the standards those documents must follow.

Subsequent chapters describe:

- the documentation hierarchy
- individual document responsibilities
- the status lifecycle and contract versioning
- writing standards
- review processes
- repository organisation
- standards mapping

Together these chapters establish a coherent documentation system capable of evolving alongside the Mosaic platform for many years.
