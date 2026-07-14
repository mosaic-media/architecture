<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/14-adrs.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# Architectural Decision Records (ADRs)

> *Architectural boundaries are among the most expensive decisions to change. They should never exist without recorded reasoning.*

---

# Purpose

Hexagonal Architecture defines how the Mosaic platform is structured.

It determines:

- dependency direction
- ownership
- technology boundaries
- integration strategy
- long-term maintainability

Changes to these principles affect every capability built upon the platform.

Architectural Decision Records (ADRs) preserve the reasoning behind those decisions so that future contributors understand not only *what* the architecture is, but *why* it exists.

---

# Philosophy

Within Mosaic:

> **Architectural boundaries should be intentional, stable and historically traceable.**

The Hexagon should evolve because our understanding improves.

It should never evolve because implementation became convenient.

---

# Why Hexagonal ADRs Matter

Infrastructure changes frequently.

Architecture should not.

Without ADRs, engineers eventually ask:

- Why are Ports owned by the Domain?
- Why are Runtime Events outside the Hexagon?
- Why don't repositories return database models?
- Why are extensions treated as infrastructure?

Without documented reasoning, those discussions repeat.

ADRs preserve architectural knowledge.

---

# When An ADR Is Required

A Hexagonal ADR SHOULD be created whenever a decision changes:

- dependency direction
- Port ownership
- Adapter responsibilities
- Composition Root behaviour
- Application Service responsibilities
- Runtime boundaries
- integration strategy
- infrastructure boundaries

If the decision changes how the architecture is structured, it deserves an ADR.

---

# Examples

Examples of Hexagonal ADRs include:

```
ADR-001

Hexagonal Architecture
```

```
ADR-002

Domain Owns Ports
```

```
ADR-003

Reactive Runtime Outside The Hexagon
```

```
ADR-004

Application Service Responsibilities
```

```
ADR-005

Repository Ownership
```

```
ADR-006

Extension Integration Boundary
```

```
ADR-007

Composition Root Strategy
```

These decisions influence every implementation within the platform.

---

# Architectural Stability

Hexagonal Architecture should evolve conservatively.

Changing:

```
HTTP Framework
```

is inexpensive.

Changing:

```
Dependency Direction
```

affects:

- every package
- every Port
- every Adapter
- every test
- every extension

Architectural stability should therefore be prioritised.

---

# ADR Structure

Every Hexagonal ADR SHOULD contain:

```
Title

↓

Status

↓

Context

↓

Architectural Problem

↓

Options

↓

Decision

↓

Consequences

↓

Migration

↓

Related Specifications
```

Migration guidance is particularly important because architectural changes frequently affect many repositories.

---

# Context

The Context section should describe:

- current architecture
- dependency relationships
- technical constraints
- business requirements

Readers unfamiliar with Mosaic should understand why the architectural discussion became necessary.

---

# Architectural Problem

The problem statement should describe architecture.

Good.

```
The Domain currently depends upon runtime infrastructure.
```

Poor.

```
We should refactor some packages.
```

The problem should remain understandable independently of implementation.

---

# Options

Every significant architectural decision SHOULD evaluate alternatives.

Example.

```
Layered Architecture
```

```
Hexagonal Architecture
```

```
Clean Architecture
```

Each option should document:

- benefits
- drawbacks
- operational impact
- maintenance implications

Rejected alternatives remain valuable engineering knowledge.

---

# Decision

The Decision section answers one question.

> **Which architectural approach becomes the new standard?**

Implementation details belong elsewhere.

The ADR records the decision itself.

---

# Consequences

Every architectural decision introduces trade-offs.

Example.

Choosing:

```
Domain Owns Ports
```

Benefits.

- infrastructure independence
- testability
- replaceable adapters

Costs.

- additional interfaces
- more explicit composition
- initial learning curve

Trade-offs should always be documented honestly.

No architecture is free.

---

# Migration

Architectural changes often require gradual migration.

Migration guidance should explain:

- affected repositories
- dependency changes
- compatibility expectations
- rollout strategy

Large-scale architectural changes should never rely solely on implementation.

---

# Runtime Integration

Changes affecting the Runtime boundary SHOULD receive particular scrutiny.

Example.

```
Runtime

↓

Outside Hexagon
```

Moving this boundary affects:

- MEG-002
- MEG-003
- every Adapter
- every Application Service

Cross-specification changes should therefore be documented explicitly.

---

# Cross References

Hexagonal ADRs SHOULD reference:

- related MEG specifications
- relevant runtime ADRs
- domain ADRs
- implementation repositories

Architecture should remain navigable.

Knowledge should not become fragmented.

---

# Repository Structure

Recommended layout.

```
architecture/

    adrs/

        ADR-001-hexagonal-architecture.md

        ADR-002-domain-owns-ports.md

        ADR-003-runtime-boundary.md

        ADR-004-composition-root.md

        ADR-005-extension-boundary.md
```

Architectural decisions should remain close to the specifications they influence.

---

# Review Process

Hexagonal ADRs SHOULD receive architectural review.

Review should consider:

- dependency direction
- coupling
- maintainability
- testability
- runtime integration
- long-term evolution

Architecture should lead implementation.

Not follow it.

---

# Documentation

Accepted Hexagonal ADRs SHOULD eventually be reflected within:

- MEG specifications
- package documentation
- architecture diagrams
- contributor guidance

The written architecture should always reflect the implemented architecture.

---

# Mosaic Guidelines

Within Mosaic:

- Significant architectural boundary changes SHOULD have ADRs.
- Dependency direction changes MUST be documented.
- Alternatives SHOULD be evaluated explicitly.
- Architectural trade-offs MUST be acknowledged.
- Migration guidance SHOULD accompany major architectural changes.
- Historical ADRs MUST remain available.
- The implemented architecture SHOULD always be traceable back to documented architectural decisions.

---

# Relationship to MEG

MEG-004 defines:

> **How the architecture is structured today.**

Hexagonal ADRs explain:

> **Why the architecture is structured that way.**

Together they preserve the architectural intent of the platform.

Future contributors should inherit both the design and the reasoning behind it.

---

# Summary

Hexagonal Architecture protects the Domain from technology.

Architectural Decision Records protect that architecture from time.

Within Mosaic, the architecture should evolve through deliberate engineering judgement rather than accidental implementation.

Every significant boundary should therefore exist because somebody consciously chose it, documented it and accepted its trade-offs.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`13-modelling-guidelines.md`

**Next File**

`15-contributor-guidance.md`
