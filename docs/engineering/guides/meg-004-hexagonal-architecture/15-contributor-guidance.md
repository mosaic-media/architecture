<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/15-contributor-guidance.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# Contributor Guidance

> *Every contribution either strengthens or weakens the architectural boundary. There is no neutral change.*

---

# Purpose

The Hexagonal Architecture protects the most valuable part of the Mosaic platform:

> **The Domain Model.**

Every contributor therefore shares responsibility for preserving:

- dependency direction
- technology independence
- architectural boundaries
- replaceable infrastructure

This document provides practical guidance for engineers implementing new capabilities within the Hexagonal Architecture.

---

# Philosophy

Within Mosaic:

> **Protect the Domain before adding infrastructure.**

Business behaviour should remain stable.

Infrastructure should remain replaceable.

Whenever these goals conflict:

The Domain wins.

Always.

---

# Before Writing Code

Before implementing a new feature ask:

- Which Bounded Context owns this?
- Which Aggregate owns the behaviour?
- Does the Domain already model this concept?
- Is infrastructure influencing the design?

If implementation discussions begin before business modelling:

Return to MEG-003.

The Domain should always lead implementation.

---

# Before Creating A Port

Ask:

- Does the Domain genuinely require this capability?
- Is this describing business behaviour?
- Could an existing Port already satisfy this requirement?

Avoid introducing Ports simply because:

> "We might need another implementation."

Ports should emerge from business requirements.

Not speculation.

---

# Before Creating An Adapter

Ask:

- Which technology am I isolating?
- Does this Adapter perform translation?
- Does any business behaviour appear here?

If the Adapter contains business rules:

The architecture has already begun drifting.

Business behaviour belongs inside the Domain.

---

# Before Adding A Dependency

Ask one question.

> **Does this dependency point inward?**

If yes:

Proceed.

If no:

Reconsider the design.

Dependency direction is one of the strongest architectural indicators available.

---

# Before Importing A Package

Every import should reinforce the Hexagon.

Allowed.

```
Adapter

↓

Application

↓

Domain
```

Prohibited.

```
Domain

↓

Infrastructure
```

The compiler should naturally reinforce the architecture.

Imports should tell the same architectural story as the documentation.

---

# Before Adding Infrastructure

Ask:

- Does the Domain already expose a Port?
- Should infrastructure implement that Port?
- Does the Domain actually require this capability?

Infrastructure should adapt itself to existing Ports whenever practical.

Avoid changing the Domain solely because a new technology has been introduced.

---

# Before Modifying A Port

Ports are long-lived contracts.

Changing one affects:

- the Domain
- every Adapter
- every test
- every extension

Before modifying a Port ask:

- Is the business changing?
- Or only the infrastructure?

If only infrastructure changes:

The Port probably should not.

---

# Before Modifying An Adapter

Adapters should evolve freely.

Examples include:

- SQL optimisation
- API version upgrades
- SDK replacement
- protocol changes

These changes should rarely affect the Domain.

If they do:

Review the architectural boundary.

---

# Before Creating An Application Service

Application Services should coordinate.

Not decide.

Ask:

- Am I loading an Aggregate?
- Am I invoking business behaviour?
- Am I persisting changes?

If additional business logic appears:

Move it into:

- Aggregate
- Entity
- Value Object
- Domain Service

The Application layer should remain intentionally thin.

---

# Before Introducing Runtime Behaviour

The Reactive Runtime is infrastructure.

Ask:

- Does the Domain need to know this?
- Or should an Adapter translate it?

Examples.

Poor.

```
Aggregate

↓

Publish Runtime Event
```

Preferred.

```
Aggregate

↓

Raise Domain Event

↓

Runtime Adapter

↓

Runtime Event
```

MEG-002 and MEG-004 should reinforce one another.

Never compete.

---

# Before Merging

Every architectural contribution SHOULD satisfy the following checklist.

## Domain

- Business behaviour remains inside the Domain.
- No infrastructure packages imported.
- Ubiquitous Language remains consistent.

---

## Ports

- Ports describe business capabilities.
- Ports remain technology independent.
- Ports remain focused.

---

## Adapters

- Technology isolated.
- Translation only.
- No business rules.

---

## Dependencies

- Dependencies point inward.
- No circular imports.
- Infrastructure remains replaceable.

---

## Runtime

- Runtime remains outside the Domain.
- Domain Events remain infrastructure independent.
- Runtime integration occurs through Adapters.

---

## Documentation

- MEG updated if required.
- ADR created where appropriate.
- Diagrams remain accurate.
- Examples remain consistent.

Architecture documentation should evolve alongside implementation.

---

# Recognising Architectural Drift

The following symptoms usually indicate the Hexagon is weakening.

- SQL inside the Domain.
- HTTP types crossing Port boundaries.
- Runtime APIs imported by Aggregates.
- Growing Application Services.
- Business logic inside Adapters.
- Infrastructure exceptions leaking into the Domain.

Architectural drift should be corrected early.

Small violations accumulate quickly.

---

# Refactoring Towards The Hexagon

When improving existing code ask:

- Can this dependency move outward?
- Can this translation move into an Adapter?
- Can this business rule move into an Aggregate?
- Can this Port become smaller?
- Can this technology disappear behind a Port?

Refactoring should make boundaries more explicit.

Not blur them.

---

# Review Mindset

Architecture reviews should ask:

- Does this strengthen dependency direction?
- Does this improve replaceability?
- Does this reduce coupling?
- Does the Domain remain pure?
- Would replacing this technology require Domain changes?

These questions are generally more valuable than debating implementation style.

---

# Learning The Architecture

New contributors SHOULD study MEG-004 in the following order.

```
Hexagonal Philosophy

↓

Ports

↓

Adapters

↓

Dependency Direction

↓

Composition Root

↓

Application Services

↓

Runtime Boundary
```

Understanding dependency direction first makes every later concept significantly easier to understand.

---

# Engineering Culture

Contributors should strive to:

- simplify dependencies
- reduce coupling
- improve naming
- remove technology leakage
- preserve Domain purity
- question unnecessary abstraction

The architecture should become more obvious over time.

Not more clever.

---

# Contributor Checklist

Before requesting review, confirm:

- [ ] The Domain remains technology independent.
- [ ] Dependencies point inward.
- [ ] Ports describe business capabilities.
- [ ] Adapters isolate technology.
- [ ] Application Services remain orchestration only.
- [ ] Runtime concerns remain outside the Domain.
- [ ] Infrastructure remains replaceable.
- [ ] Documentation has been updated.
- [ ] The architecture is simpler or clearer than before.

---

# Relationship to MEG

This document explains how contributors should evolve the Hexagonal Architecture established throughout MEG-004.

The previous chapters define:

> **How the architecture should be structured.**

This chapter defines:

> **How engineers should preserve that structure over time.**

Architecture survives not because diagrams exist.

It survives because contributors consistently reinforce its principles.

---

# Summary

Hexagonal Architecture is not maintained through frameworks.

It is maintained through engineering discipline.

Every contributor influences whether the Domain remains:

- independent
- testable
- replaceable
- understandable

Within Mosaic, every change should strengthen the architectural boundary between the business and technology.

Because once that boundary begins to erode, the cost of every future change begins to increase with it.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`14-adrs.md`

**Next File**

`glossary.md`
