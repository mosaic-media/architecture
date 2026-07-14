<!--
File: docs/engineering/documentation/mdg-001-documentation-authority-guide/02-document-types.md
Document: MDG-001
Status: Draft
Version: 0.1
-->

# 02 — Document Types

---

# Purpose

Each Mosaic document type exists to fulfil a specific responsibility.

No document should attempt to fulfil multiple responsibilities.

This separation ensures:

- architectural intent remains clear
- duplication is minimised
- documentation remains maintainable
- readers can easily determine where information belongs

Selecting the correct document type is therefore the first architectural decision made when creating new documentation.

---

# Overview

The Mosaic documentation system currently defines the following document types.

| Prefix | Name | Primary Responsibility |
|---------|------|------------------------|
| MDP | Mosaic Design Proposal | Propose architectural change |
| MAD | Mosaic Architecture Decision | Record accepted decisions |
| MAC | Mosaic Architecture Canon | Define accepted architecture |
| MEG | Mosaic Engineering Guide | Explain implementation practices |
| MIP | Mosaic Integration Protocol | Define integration contracts |
| MOP | Mosaic Operations & Playbook | Define operational procedures |
| MDL | Mosaic Design Language | Define design philosophy |
| MDS | Mosaic Design System | Define reusable design assets |
| MDG | Mosaic Documentation Guide | Define documentation standards |

Each document type complements the others.

No document type replaces another.

---

# MDP — Mosaic Design Proposal

## Responsibility

A Mosaic Design Proposal captures an architectural idea before it becomes part of the platform.

An MDP exists to encourage discussion.

It should evolve during review.

An accepted proposal normally results in:

- one or more Architecture Decisions
- updates to the Architecture Canon
- new Engineering Guides
- new Integration Protocols

## Typical Contents

An MDP should normally contain:

- problem statement
- objectives
- proposed solution
- alternatives considered
- anticipated impact
- unresolved questions

## Should Not Contain

An MDP should not:

- define accepted architecture
- provide implementation guidance
- become permanent reference documentation

---

# MAD — Mosaic Architecture Decision

## Responsibility

A Mosaic Architecture Decision records why an architectural decision was accepted.

MAD documents preserve architectural history.

They explain the reasoning behind the platform rather than the platform itself.

## Typical Contents

A MAD should normally contain:

- context
- decision
- alternatives considered
- consequences
- implementation implications

## Should Not Contain

A MAD should not:

- redefine architecture
- duplicate Canon documents
- contain tutorials
- become implementation guidance

MAD documents should remain immutable after acceptance.

Future changes should create new decisions rather than rewriting historical ones.

---

# MAC — Mosaic Architecture Canon

## Responsibility

The Architecture Canon defines the accepted architecture of Mosaic.

MAC documents answer:

> **What is Mosaic?**

The Canon establishes the stable architectural principles upon which every implementation depends.

## Typical Contents

A MAC should normally contain:

- purpose
- philosophy
- concepts
- architectural models
- responsibilities
- relationships
- references

## Should Not Contain

A MAC should not:

- explain historical decisions
- compare alternatives
- provide code samples
- describe operational procedures

Implementation examples belong within Engineering Guides.

Decision history belongs within Architecture Decisions.

---

# MEG — Mosaic Engineering Guide

## Responsibility

Engineering Guides explain how engineers realise the Canon.

MEGs answer:

> **How should this be built?**

They are expected to evolve alongside engineering practice.

## Typical Contents

A MEG should normally contain:

- engineering guidance
- patterns
- examples
- implementation recommendations
- code samples
- best practices

## Should Not Contain

A MEG should not redefine architectural principles.

Where architecture changes, the Canon should be updated first.

---

# MIP — Mosaic Integration Protocol

## Responsibility

Integration Protocols define how Mosaic components communicate.

MIPs describe machine-readable contracts.

They establish compatibility between independently developed components.

## Typical Contents

Examples include:

- message envelopes
- schemas
- APIs
- manifests
- compatibility rules
- protocol semantics

## Should Not Contain

MIPs should avoid implementation-specific behaviour wherever possible.

---

# MOP — Mosaic Operations & Playbook

## Responsibility

Operations & Playbooks describe how Mosaic is operated.

MOPs answer:

> **How should Mosaic be deployed, maintained and recovered?**

## Typical Contents

Examples include:

- deployment
- upgrades
- diagnostics
- monitoring
- recovery
- maintenance

## Should Not Contain

MOPs should not define architecture.

They describe operational practice rather than engineering intent.

---

# MDL — Mosaic Design Language

## Responsibility

The Mosaic Design Language defines how Mosaic should feel.

It establishes:

- visual philosophy
- materials
- interaction
- motion
- lighting
- presentation behaviour

MDL documents intentionally avoid platform-specific implementation.

They describe design intent.

---

# MDS — Mosaic Design System

## Responsibility

The Mosaic Design System defines the reusable building blocks that realise the Design Language.

Examples include:

- colour systems
- typography
- spacing
- icons
- components
- composition

MDS documents transform philosophy into reusable assets.

---

# MDG — Mosaic Documentation Guide

## Responsibility

Documentation Guides define how Mosaic documentation itself is authored and maintained.

They establish:

- writing standards
- organisational rules
- review expectations
- documentation governance
- versioning conventions

MDGs govern the documentation ecosystem rather than the Mosaic platform.

---

# Choosing the Correct Document Type

When creating new documentation, authors should first determine the primary question being answered.

| Question | Document Type |
|-----------|---------------|
| What should we build? | MDP |
| Why was this decision made? | MAD |
| What is the accepted architecture? | MAC |
| How should engineers implement it? | MEG |
| How do systems communicate? | MIP |
| How do operators run it? | MOP |
| How should Mosaic look and behave? | MDL |
| What reusable design assets exist? | MDS |
| How should documentation be written? | MDG |

Selecting the correct document type is more important than selecting the correct directory.

Document prefixes communicate purpose.

Directory structure communicates discipline.
