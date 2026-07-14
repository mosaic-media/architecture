<!--
File: docs/engineering/guides/meg-007-storage-architecture/13-adrs.md
Document: MEG-007
Status: Draft
Version: 0.1
-->

# Architectural Decision Records (ADRs)

> *Storage decisions are among the most difficult architectural decisions to reverse. They should always be intentional, documented and historically traceable.*

---

# Purpose

The Storage Architecture defines where every category of information within Mosaic is preserved.

Changes to that architecture affect:

- every capability
- every repository
- every migration
- every backup
- every deployment

Architectural Decision Records (ADRs) preserve the reasoning behind these decisions.

Future contributors should understand not only:

> **Where information is stored**

but also:

> **Why it is stored there.**

---

# Philosophy

Within Mosaic:

> **Storage Architecture should evolve because our understanding of information improves, not because a new database becomes fashionable.**

Storage technologies will change.

Information ownership should remain stable.

---

# Why Storage ADRs Matter

Changing storage boundaries is expensive.

Examples include:

- moving Business State
- changing repository ownership
- replacing storage engines
- redesigning archive formats

Without documented reasoning, future engineers will eventually ask:

- Why does PostgreSQL own Business State?
- Why is DuckDB analytical only?
- Why are MOS Archives separate from MOS Cache?
- Why are Blob identifiers stable?

Architectural reasoning should remain discoverable.

Not tribal knowledge.

---

# When An ADR Is Required

A Storage ADR SHOULD be created whenever a decision changes:

- storage taxonomy
- storage ownership
- repository boundaries
- storage engine selection
- archive format
- cache architecture
- migration strategy
- backup strategy
- recovery strategy

If the decision changes where information lives, it deserves an ADR.

---

# Examples

Examples of Storage ADRs include:

```text
ADR-001

Polyglot Persistence
```

```text
ADR-002

Business State In PostgreSQL
```

```text
ADR-003

DuckDB For Analytics
```

```text
ADR-004

MOS Archive Format
```

```text
ADR-005

MOS Cache Strategy
```

```text
ADR-006

Blob Identifier Design
```

```text
ADR-007

Repository Ownership
```

```text
ADR-008

Backup Strategy
```

These decisions define the long-term persistence model of the platform.

---

# Storage Stability

Storage Architecture should evolve cautiously.

Changing:

```text
Blob Compression
```

is relatively inexpensive.

Changing:

```text
Business State Ownership
```

affects:

- repositories
- migrations
- backups
- Runtime behaviour
- capabilities

Architectural stability should therefore outweigh implementation convenience.

---

# ADR Structure

Every Storage ADR SHOULD contain:

```text
Title

↓

Status

↓

Context

↓

Storage Problem

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

Migration guidance is especially important because storage decisions frequently require data transformation.

---

# Context

The Context section should describe:

- current storage model
- ownership
- lifecycle
- operational constraints
- recovery requirements

Readers unfamiliar with the platform should understand:

> **Why did this storage decision become necessary?**

---

# Storage Problem

The problem statement should describe information architecture.

Good.

```text
Analytical workloads are degrading transactional performance.
```

Poor.

```text
DuckDB looks interesting.
```

The problem should remain architectural.

Not technology driven.

---

# Options

Every Storage ADR SHOULD evaluate alternatives.

Example.

```text
Single Database
```

versus

```text
Polyglot Persistence
```

or

```text
Embedded Artwork
```

versus

```text
Blob Storage
```

Each option should document:

- advantages
- disadvantages
- operational implications
- maintenance cost

Rejected alternatives remain valuable architectural knowledge.

---

# Decision

The Decision section answers:

> **Which storage architecture becomes the Mosaic standard?**

Implementation belongs elsewhere.

The ADR records the architectural commitment.

---

# Consequences

Every storage decision introduces trade-offs.

Example.

Choosing:

```text
Polyglot Persistence
```

Benefits.

- specialised workloads
- improved scalability
- cleaner ownership

Costs.

- additional operational complexity
- multiple backup strategies
- more infrastructure components

Trade-offs should always be documented honestly.

---

# Migration

Storage decisions frequently require migration.

Migration guidance SHOULD explain:

- affected storage engines
- repository changes
- compatibility strategy
- recovery implications

Migration planning should exist before implementation begins.

---

# Archive Evolution

Changes affecting MOS Archives SHOULD always receive ADRs.

Archive compatibility is a long-term platform commitment.

Breaking archive compatibility without documented reasoning should be considered an architectural failure.

---

# Cache Evolution

Changes affecting MOS Cache SHOULD distinguish between:

- rebuild strategy
- storage implementation
- cache invalidation

Cache evolution should never compromise business correctness.

---

# Repository Boundaries

Repository ownership changes SHOULD always be documented.

Repositories define the boundary between:

- Domain
- Storage

Changing those boundaries affects the entire architecture.

---

# Repository Structure

Recommended layout.

```text
architecture/

    adrs/

        ADR-001-polyglot-persistence.md

        ADR-002-postgresql-business-state.md

        ADR-003-duckdb-analytics.md

        ADR-004-mos-archives.md

        ADR-005-storage-lifecycle.md
```

Storage ADRs should remain close to the Storage Architecture they explain.

---

# Review Process

Storage ADRs SHOULD receive architectural review.

Review should consider:

- ownership
- recoverability
- consistency
- scalability
- observability
- operational simplicity

Storage decisions should optimise information first.

Technology second.

---

# Documentation

Accepted Storage ADRs SHOULD eventually be reflected within:

- MEG specifications
- storage diagrams
- migration documentation
- repository documentation
- operational runbooks

Documentation should evolve alongside the Storage Architecture.

---

# Mosaic Guidelines

Within Mosaic:

- Significant storage decisions SHOULD have ADRs.
- Storage ownership MUST remain explicitly documented.
- Alternative storage designs SHOULD be evaluated.
- Trade-offs MUST be acknowledged.
- Migration guidance SHOULD accompany storage evolution.
- Historical ADRs MUST remain available.
- Storage Architecture SHOULD evolve deliberately rather than opportunistically.

---

# Relationship to MEG

MEG-007 defines:

> **How information is stored today.**

Storage ADRs explain:

> **Why information is stored that way.**

Together they preserve the architectural intent of the platform's persistence model.

---

# Summary

Storage decisions often outlive the technologies implementing them.

Architectural Decision Records ensure that the reasoning behind those decisions survives as well.

Within Mosaic, information is one of the platform's most valuable assets.

The architectural decisions governing its preservation deserve the same permanence.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`12-storage-guidelines.md`

**Next File**

`14-contributor-guidance.md`
