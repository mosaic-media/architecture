<!--
File: engineering/meg/MEG-001 Go Engineering Standards/17-adrs.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Architectural Decision Records (ADRs)

> *Every significant architectural decision should be recorded once, explained clearly and referenced often.*

---

# Purpose

Architecture is a sequence of decisions.

Over time, engineers inevitably ask:

- Why was this technology chosen?
- Why is the package structured this way?
- Why don't we use a dependency injection framework?
- Why are events preferred over direct service calls?

Without documentation, these discussions repeat.

Architectural Decision Records (ADRs) capture the reasoning behind significant engineering decisions so future contributors understand **why** the software exists in its current form.

---

# Philosophy

Within Mosaic:

> **Architecture should explain itself.**

The codebase explains *what* the software does.

ADRs explain *why* it does it that way.

Every major engineering decision should remain understandable years after it was made.

---

# What Is An ADR?

An Architectural Decision Record is a short document describing:

- the problem
- the available options
- the chosen solution
- the reasoning
- the consequences

An ADR records a decision at a point in time.

It is **not** intended to become a design document or implementation guide.

---

# Why ADRs Matter

Software outlives conversations.

Months later, engineers rarely remember:

- trade-offs
- rejected alternatives
- historical constraints
- business drivers

Without ADRs, teams often repeat previous discussions because the original reasoning has been lost.

ADRs preserve architectural knowledge.

---

# When To Write An ADR

An ADR SHOULD be created whenever a decision:

- significantly influences architecture
- changes engineering standards
- introduces new infrastructure
- affects multiple repositories
- changes dependency direction
- introduces a new pattern
- removes an existing pattern
- establishes a long-term convention

Small implementation decisions do not require ADRs.

Architectural decisions do.

---

# Examples

Examples of decisions that SHOULD have ADRs include:

- Choosing Go as the implementation language.
- Choosing PostgreSQL as the primary database.
- Introducing DuckDB for analytics.
- Event-driven architecture.
- Repository package structure.
- Extension SDK architecture.
- Refraction rendering engine.
- Blob storage abstraction.
- Background worker model.
- Docker orchestration strategy.

These decisions affect the platform for years.

Their rationale should therefore remain discoverable.

---

# What Should Not Become An ADR

The following generally SHOULD NOT become ADRs.

- Bug fixes
- Refactoring
- Naming changes
- Package moves
- Small implementation details
- Formatting standards

If reversing the decision would not significantly affect architecture, an ADR is probably unnecessary.

---

# ADR Lifecycle

Every ADR follows the same lifecycle.

```
Proposed

↓

Accepted

↓

Implemented

↓

Superseded (optional)

↓

Archived
```

Most ADRs will remain "Accepted" for many years.

Superseded ADRs remain valuable historical references.

They should never be deleted.

---

# ADR Structure

Every ADR SHOULD follow a consistent structure.

```
Title

↓

Status

↓

Context

↓

Problem

↓

Options Considered

↓

Decision

↓

Consequences

↓

Related Documents
```

Consistency makes ADRs significantly easier to navigate.

---

# Context

The Context section explains:

- the current situation
- existing constraints
- relevant background
- why the decision became necessary

Readers unfamiliar with the project should understand why the discussion exists.

---

# Problem Statement

The problem statement should be objective.

Good:

> The platform requires a high-performance metadata store capable of analytical queries.

Poor:

> We wanted to try DuckDB.

The problem should exist independently of the proposed solution.

---

# Options

Every significant alternative SHOULD be documented.

Example.

```
PostgreSQL

DuckDB

SQLite
```

Each option should include:

- benefits
- drawbacks
- implementation impact

Rejected alternatives are often as valuable as accepted ones.

---

# Decision

The decision section answers one question.

> **What was chosen?**

The decision should be concise.

The reasoning belongs elsewhere.

---

# Consequences

Every architectural decision introduces consequences.

Examples include:

Positive:

- improved performance
- reduced coupling
- easier testing

Negative:

- additional complexity
- operational cost
- migration effort

Trade-offs should be documented honestly.

No architecture is free.

---

# Superseding Decisions

Architecture evolves.

When replacing an existing ADR:

- create a new ADR
- reference the previous ADR
- mark the old ADR as superseded

Do not modify history.

Record evolution instead.

---

# Cross References

Every ADR SHOULD reference related specifications where appropriate.

Examples:

```
MEG-001

↓

MDS-006

↓

ADR-012
```

Architecture should form a navigable knowledge graph.

Not isolated documents.

---

# Repository Structure

Recommended layout.

```
architecture/

    adrs/

        ADR-001-go-language.md

        ADR-002-event-driven.md

        ADR-003-postgresql.md

        ADR-004-duckdb.md

        ADR-005-extension-sdk.md
```

ADRs should remain close to the architectural documentation.

Not hidden inside implementation repositories.

---

# Writing Guidelines

An ADR should be:

- concise
- objective
- factual
- timeless

Avoid:

- implementation details
- emotional language
- unnecessary technical depth

The objective is to explain a decision.

Not reproduce the implementation.

---

# Review

Architectural decisions SHOULD be reviewed before acceptance.

Reviews should consider:

- alternatives
- trade-offs
- long-term impact
- alignment with existing architecture

Accepted ADRs become part of Mosaic's engineering history.

---

# Mosaic Guidelines

Within Mosaic:

- Significant architectural decisions SHOULD have ADRs.
- ADRs MUST explain why, not merely what.
- Alternatives SHOULD be documented.
- Consequences MUST be acknowledged.
- Historical ADRs MUST NOT be deleted.
- Superseded ADRs SHOULD remain discoverable.
- Architecture specifications SHOULD reference relevant ADRs where appropriate.

---

# Relationship to the MEG

The MEG defines engineering standards.

ADRs explain why those standards exist.

Whenever an engineering standard changes significantly, the corresponding ADR should explain the reasoning behind the change.

Together they provide:

```
ADR

↓

Reasoning

↓

MEG

↓

Engineering Standard

↓

Implementation
```

This relationship ensures that architectural intent remains preserved long after individual contributors have moved on.

---

# Summary

Software changes.

Architecture evolves.

People leave projects.

ADRs ensure that engineering knowledge remains.

Future contributors should never need to rediscover important architectural decisions through trial and error.

Instead, they should be able to read the decision, understand the reasoning and continue building upon it with confidence.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`16-boy-scout-rule.md`

**Next File**

`18-contributor-guidance.md`
