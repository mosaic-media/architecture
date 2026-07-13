<!--
File: engineering/meg/MEG-003 Domain-Driven Design/16-adrs.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Architectural Decision Records (ADRs)

> *The Domain Model is the most valuable intellectual asset within the platform. Changes to that model should always be intentional, documented and historically traceable.*

---

# Purpose

The Mosaic Domain Model defines:

- business language
- business ownership
- business behaviour
- business boundaries

Changes to these concepts affect every layer built upon them.

Architectural Decision Records (ADRs) ensure that significant domain modelling decisions are preserved alongside the architecture itself.

Future contributors should understand not only:

> **What the model is**

but also:

> **Why it became that model.**

---

# Philosophy

Within Mosaic:

> **The domain should evolve through deliberate understanding rather than accidental implementation.**

Changes to the Domain Model should represent improved understanding of the business.

Not convenience.

Not implementation pressure.

Not framework limitations.

---

# Why Domain ADRs Matter

Business understanding evolves.

For example.

Initially.

```
Media
```

Later.

```
Movie

Series

Book

Music
```

Why did the model change?

Without documentation:

Nobody knows.

Domain ADRs preserve the reasoning behind those decisions.

---

# When An ADR Is Required

A Domain ADR SHOULD be created whenever a decision changes:

- ubiquitous language
- bounded contexts
- aggregate boundaries
- entity ownership
- business terminology
- domain events
- invariants
- context relationships
- repository ownership

If the decision changes how the business is understood, it probably deserves an ADR.

---

# Examples

Examples of Domain ADRs include:

```
ADR-001

Library Is The Core Aggregate
```

```
ADR-002

Playback As Independent Context
```

```
ADR-003

Metadata Ownership
```

```
ADR-004

Continue Watching Model
```

```
ADR-005

Recommendation Domain
```

```
ADR-006

Media Identity Strategy
```

```
ADR-007

Collection Ownership
```

These decisions shape the business itself.

They should remain discoverable.

---

# Domain Stability

The Domain Model should evolve more slowly than implementation.

Changing:

```
Repository

↓

Implementation
```

is inexpensive.

Changing:

```
Library

↓

Business Meaning
```

affects:

- runtime
- APIs
- storage
- events
- documentation
- extensions

Domain evolution therefore deserves significantly greater care.

---

# ADR Structure

Every Domain ADR SHOULD contain:

```
Title

↓

Status

↓

Context

↓

Business Problem

↓

Options

↓

Decision

↓

Business Consequences

↓

Migration

↓

Related Specifications
```

Notice:

The problem is framed in business terms.

Not implementation terms.

---

# Context

The Context section should describe:

- existing business understanding
- terminology
- ownership
- modelling limitations
- business drivers

Readers unfamiliar with the domain should understand:

Why did this modelling discussion become necessary?

---

# Business Problem

The Business Problem should describe:

- business ambiguity
- ownership confusion
- inconsistent terminology
- unclear responsibilities

Poor.

```
Playback package too large.
```

Better.

```
Playback currently owns two unrelated business concepts.
```

The domain should describe the business.

Not the package structure.

---

# Options

Every Domain ADR SHOULD document alternative models.

Example.

```
Collections

↓

Library Context
```

versus.

```
Collections

↓

Independent Context
```

Every alternative should include:

- benefits
- drawbacks
- business implications

Rejected models remain valuable knowledge.

---

# Decision

The Decision section answers:

> **How should the business now be modelled?**

The wording should remain concise.

Detailed implementation belongs elsewhere.

---

# Consequences

Every modelling decision introduces trade-offs.

Example.

Choosing:

```
Playback

↓

Independent Context
```

Benefits.

- clearer ownership
- independent evolution
- simpler aggregates

Costs.

- additional events
- more explicit coordination
- increased context boundaries

Trade-offs should always be documented honestly.

---

# Migration

Changing a Domain Model often requires migration.

Examples include:

- renamed events
- renamed terminology
- aggregate restructuring
- context boundaries
- repository changes

Migration guidance should explain:

- affected capabilities
- compatibility expectations
- rollout strategy

The Domain should evolve predictably.

---

# Language Evolution

Changes to the ubiquitous language SHOULD always have an accompanying ADR.

Example.

```
Watch History

↓

Viewing History
```

The ADR should explain:

- why terminology changed
- expected business benefits
- affected specifications

Language is architecture.

Changing language changes understanding.

---

# Domain Ownership

Changes affecting ownership SHOULD always be documented.

Examples.

```
Metadata

↓

Owns Artwork
```

instead of:

```
Library

↓

Owns Artwork
```

Ownership decisions have long-term architectural consequences.

Future contributors should understand the reasoning.

---

# Context Maps

Changes to Context Maps SHOULD produce ADRs.

Example.

```
Recommendations

↓

Independent Context
```

This affects:

- ownership
- events
- extension boundaries
- runtime behaviour

Context relationships are architectural decisions.

Not implementation details.

---

# Repository Structure

Recommended layout.

```
architecture/

    adrs/

        ADR-001-library-context.md

        ADR-002-playback-domain.md

        ADR-003-metadata-ownership.md

        ADR-004-continue-watching.md

        ADR-005-recommendation-domain.md
```

Domain ADRs should remain close to the architectural specifications they support.

---

# Review Process

Domain ADRs SHOULD receive architectural review.

Review should consider:

- business correctness
- language consistency
- ownership clarity
- future evolution
- compatibility
- architectural simplicity

The objective is improving the business model.

Not merely approving implementation.

---

# Documentation

Accepted Domain ADRs SHOULD eventually be reflected within:

- MEG specifications
- architecture diagrams
- bounded context maps
- ubiquitous language
- contributor documentation

The Domain Model should remain internally consistent.

Documentation should evolve alongside it.

---

# Mosaic Guidelines

Within Mosaic:

- Significant domain modelling decisions SHOULD have ADRs.
- ADRs MUST describe business reasoning.
- Ubiquitous Language changes SHOULD be documented.
- Context ownership changes SHOULD be documented.
- Alternatives MUST be considered.
- Trade-offs MUST be acknowledged.
- Historical ADRs MUST remain available.
- Domain evolution SHOULD remain deliberate.

---

# Relationship to MEG

MEG-003 defines:

> **How the business is modelled today.**

Domain ADRs explain:

> **Why it is modelled that way.**

Together they preserve one of Mosaic's most valuable assets:

The understanding of the business itself.

Implementation can always change.

Business understanding is significantly harder to recover once lost.

---

# Summary

A Domain Model represents years of accumulated understanding.

Without ADRs, that understanding gradually disappears.

Within Mosaic, Domain ADRs ensure that future contributors inherit not only the model itself, but also the reasoning that shaped it.

That reasoning is often considerably more valuable than the implementation built upon it.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`15-modelling-guidelines.md`

**Next File**

`17-contributor-guidance.md`
