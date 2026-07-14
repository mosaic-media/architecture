<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/18-adrs.md
Document: MEG-002
Status: Draft
Version: 0.1
-->

# Architectural Decision Records (ADRs)

> *The runtime is one of the most stable parts of the Mosaic platform. Changes to its behaviour should be deliberate, documented and historically traceable.*

---

# Purpose

The Mosaic Runtime forms the foundation upon which every capability and extension operates.

Changes to runtime behaviour have platform-wide consequences.

Architectural Decision Records (ADRs) ensure that significant runtime decisions are:

- documented
- reviewed
- understood
- discoverable

long after the original implementation has changed.

---

# Philosophy

Within Mosaic:

> **Every significant runtime behaviour should exist because of a documented architectural decision.**

The runtime should never evolve accidentally.

Future contributors should understand:

- why a decision exists
- what alternatives were considered
- what trade-offs were accepted
- how the decision affects the wider platform

without reading implementation code.

---

# Why Runtime ADRs Matter

Unlike ordinary application code, runtime behaviour affects:

- every capability
- every extension
- every worker
- every scheduler
- every deployment

Changing runtime semantics without documentation creates architectural drift.

ADRs preserve intent.

---

# When An ADR Is Required

Runtime ADRs SHOULD be created whenever a decision changes:

- event semantics
- delivery guarantees
- runtime lifecycle
- scheduling behaviour
- retry behaviour
- ordering guarantees
- extension interaction
- worker lifecycle
- shutdown semantics
- observability contracts

If the decision changes how the runtime behaves, it probably deserves an ADR.

---

# Examples

The following runtime decisions SHOULD each have their own ADR.

```
ADR-001

Reactive Runtime
```

```
ADR-002

At-Least-Once Delivery
```

```
ADR-003

Idempotent Subscribers
```

```
ADR-004

Event Envelope
```

```
ADR-005

Runtime Scheduling
```

```
ADR-006

Worker Lifecycle
```

```
ADR-007

Backpressure Strategy
```

```
ADR-008

Extension Integration Model
```

These decisions influence the architecture of every capability built upon the runtime.

---

# Runtime Stability

The runtime is intentionally conservative.

Changes should be rare.

Every runtime change affects:

- backwards compatibility
- extension compatibility
- operational behaviour
- developer expectations

Architectural stability is therefore prioritised over rapid evolution.

---

# ADR Structure

Every runtime ADR SHOULD contain:

```
Title

↓

Status

↓

Context

↓

Problem

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

Runtime decisions frequently require migration guidance.

This section should therefore be mandatory.

---

# Context

The Context section should describe:

- existing runtime behaviour
- operational constraints
- architectural limitations
- motivating problems

Readers unfamiliar with the platform should understand why the decision became necessary.

---

# Options

Every significant runtime decision SHOULD document reasonable alternatives.

Example.

```
Exactly Once

↓

At Least Once

↓

At Most Once
```

Rejected options are valuable architectural knowledge.

They explain why the runtime behaves as it does today.

---

# Decision

The Decision section should state:

> **What behaviour becomes the new runtime standard?**

The wording should be concise.

Implementation belongs elsewhere.

---

# Consequences

Every runtime decision introduces trade-offs.

Example.

Choosing:

```
At Least Once
```

Produces:

Benefits.

- simpler runtime
- greater resilience
- better scalability

Costs.

- idempotent subscribers required
- duplicate delivery possible

Every ADR should acknowledge both.

Architecture is always compromise.

---

# Migration

Runtime behaviour changes frequently require migration.

Migration guidance should explain:

- affected capabilities
- extension impact
- compatibility strategy
- rollout expectations

Migration planning should exist before implementation begins.

---

# Runtime Compatibility

Runtime ADRs should consider compatibility across:

- Core
- First-party extensions
- Third-party extensions
- Development tooling
- Operational tooling

The runtime exists for the entire ecosystem.

Not merely Core.

---

# Cross References

Runtime ADRs SHOULD reference:

- MEG specifications
- related ADRs
- affected capabilities
- extension specifications

Example.

```
ADR-007

↓

MEG-002

↓

Section 15

Backpressure
```

Architecture should remain navigable.

Knowledge should not become fragmented.

---

# Superseding Runtime Decisions

The runtime will evolve.

When replacing behaviour:

```
ADR-005

↓

Superseded By

↓

ADR-014
```

History should remain intact.

Previous reasoning remains valuable even after behaviour changes.

---

# Repository Structure

Recommended layout.

```
architecture/

    adrs/

        ADR-001-reactive-runtime.md

        ADR-002-event-delivery.md

        ADR-003-worker-lifecycle.md

        ADR-004-runtime-scheduling.md

        ADR-005-extension-runtime.md
```

Runtime ADRs should remain close to the architectural specifications governing them.

---

# Review Process

Runtime ADRs SHOULD receive architectural review before acceptance.

Reviewers should evaluate:

- correctness
- scalability
- operational impact
- compatibility
- long-term maintenance
- alignment with MEG

Runtime behaviour should never change through implementation alone.

Architecture should lead implementation.

---

# Documentation

Every accepted runtime ADR SHOULD eventually be reflected within:

- MEG specifications
- runtime documentation
- contributor guidance
- implementation comments where appropriate

The MEG defines current standards.

ADRs explain how those standards emerged.

---

# Mosaic Guidelines

Within Mosaic:

- Significant runtime decisions SHOULD have ADRs.
- Runtime ADRs MUST explain architectural reasoning.
- Alternatives MUST be documented.
- Trade-offs MUST be acknowledged.
- Migration guidance SHOULD accompany runtime changes.
- Historical ADRs MUST remain available.
- Runtime behaviour SHOULD never change without corresponding architectural documentation.

---

# Relationship to MEG-002

MEG-002 defines:

> **How the runtime behaves today.**

Runtime ADRs explain:

> **Why it behaves that way.**

Together they create a complete architectural record.

Future contributors should rarely need to rediscover runtime design decisions through experimentation.

Instead, the reasoning should already exist.

---

# Summary

The Mosaic Runtime is the platform's execution engine.

Changes to its behaviour affect every capability.

Documenting those changes is therefore an architectural responsibility rather than a documentation exercise.

Well-maintained ADRs preserve not only implementation history, but architectural intent.

That intent is one of the most valuable assets of any long-lived software platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`17-runtime-shutdown.md`

**Next File**

`19-contributor-guidance.md`
