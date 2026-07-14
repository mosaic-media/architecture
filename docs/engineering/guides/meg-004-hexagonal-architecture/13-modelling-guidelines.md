<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/13-modelling-guidelines.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# Modelling Guidelines

> *Every architectural decision should strengthen the boundary between the business and the outside world.*

---

# Purpose

The previous chapters introduced the structural building blocks of Hexagonal Architecture:

- Ports
- Adapters
- Dependency Direction
- Composition Root
- Application Services
- Runtime Boundaries

This document brings those concepts together into practical guidance for engineers implementing new capabilities within the Mosaic platform.

Its purpose is to answer one question.

> **"Where should this code actually live?"**

---

# Philosophy

Within Mosaic:

> **Model the business first. Connect it to technology afterwards.**

When designing a new capability:

1. Discover the business.
2. Model the Domain.
3. Define the Ports.
4. Implement the Adapters.
5. Assemble everything in the Composition Root.

Never reverse this order.

---

# Start With The Domain

Every feature should begin inside the Domain.

Ask:

- What business capability exists?
- Which Aggregate owns it?
- Which business rules apply?
- Which Domain Events occur?

Do **not** begin with:

- database schema
- HTTP endpoints
- REST APIs
- runtime events

Technology follows the Domain.

Never the reverse.

---

# Define Ports Last

One of the most common mistakes is designing Ports before understanding the Domain.

Instead:

```
Business Behaviour

↓

Domain Model

↓

Port

↓

Adapter
```

Ports should emerge naturally from business requirements.

Not hypothetical infrastructure.

---

# One Dependency Rule

Whenever adding a dependency ask:

> **Does this dependency point towards the Domain?**

If yes:

Proceed.

If no:

The dependency probably belongs elsewhere.

Dependency direction should answer more architectural questions than folder structure.

---

# Business Before Infrastructure

Suppose a new feature requires TMDB.

Incorrect thought process.

```
TMDB API

↓

How do I use it?
```

Preferred.

```
Metadata

↓

What business capability do I need?

↓

MetadataProvider

↓

TMDB Adapter
```

The business requirement comes first.

The infrastructure follows.

---

# Choosing A Port

Before introducing a Port ask:

- Does the Domain genuinely depend upon this capability?
- Is this a business requirement?
- Can another Port already satisfy this behaviour?

Avoid creating Ports because:

> "We might need another implementation later."

Ports exist because the Domain requires stable contracts.

Not speculative flexibility.

AWS recommends introducing ports where the business genuinely requires external interaction, rather than creating unnecessary abstraction layers.  [oai_citation:0‡AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/best-practices.html?utm_source=chatgpt.com)

---

# Choosing An Adapter

Every Adapter should answer:

> **Which technology am I isolating?**

Examples.

```
PostgreSQL
```

```
TMDB
```

```
Filesystem
```

```
HTTP
```

If an Adapter cannot answer that question clearly, its responsibility should be reconsidered.

---

# One Adapter, One Concern

Adapters should remain cohesive.

Good.

```
TMDB Adapter
```

Poor.

```
ExternalServicesAdapter

↓

TMDB

AniList

Trakt

Jellyfin

Docker
```

Technology boundaries should remain explicit.

---

# Keep The Domain Pure

The following should never appear inside the Domain.

- SQL
- HTTP
- JSON
- Docker
- Runtime
- Logging
- Environment variables
- Framework annotations

If these concepts appear:

The boundary has already been crossed.

---

# Keep Application Services Thin

Application Services should follow the same structure.

```
Receive Request

↓

Load Aggregate

↓

Invoke Behaviour

↓

Persist Aggregate

↓

Return Result
```

If additional business logic appears:

Move it into:

- Aggregate
- Entity
- Value Object
- Domain Service

Application Services coordinate.

They do not decide.

---

# Translate At The Boundary

Every translation should occur at a boundary.

Examples.

```
JSON

↓

Request DTO

↓

Business Request
```

```
Aggregate

↓

Database Row
```

```
TMDB Response

↓

Metadata
```

Translation should never occur inside the Domain.

---

# Prefer Explicit Mapping

Avoid magical mapping libraries where they obscure intent.

Good.

```go
Metadata{
    Title: response.Title,
    Year:  response.Year,
}
```

Poor.

```go
mapper.Map(...)
```

Explicit mapping is usually:

- easier to debug
- easier to review
- easier to evolve

Clarity is generally more valuable than reducing a few lines of code.

---

# Infrastructure Should Be Replaceable

Ask:

> **Could I replace this technology without modifying the Domain?**

Examples.

```
PostgreSQL

↓

CockroachDB
```

```
TMDB

↓

AniList
```

```
REST

↓

GraphQL
```

If the answer is "no":

Technology has probably leaked through the boundary.

---

# Design For Testing

A useful architectural question is:

> **Can I test this without infrastructure?**

If the answer is yes:

The boundary is probably correct.

If the answer is no:

Determine which dependency has entered the wrong layer.

---

# Runtime Is Infrastructure

One subtle guideline deserves repeating.

The Reactive Runtime belongs outside the Hexagon.

The Domain should never know:

- workers
- retries
- scheduling
- queues
- event buses

Those concepts remain infrastructure.

Business behaviour remains pure.

---

# Folder Structure Follows Architecture

Packages should reflect architectural ownership.

Example.

```
internal/

    domain/

    application/

    adapters/

        http/

        postgres/

        tmdb/

        runtime/

    bootstrap/
```

The folder structure should communicate:

- dependency direction
- ownership
- boundaries

It should never encourage architectural violations.

A clear separation between domain, entry points and adapters is a common recommendation for Ports and Adapters implementations.  [oai_citation:1‡AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/best-practices.html?utm_source=chatgpt.com)

---

# Refactor Towards The Hexagon

Existing code rarely starts perfectly.

When refactoring ask:

- Can this dependency move outward?
- Can this behaviour move inward?
- Can this translation occur at the boundary?
- Can this Port become smaller?
- Can this Adapter become simpler?

The Hexagon should become more explicit over time.

Not less.

---

# Architecture Checklist

Before merging a new capability confirm:

- [ ] Business behaviour lives in the Domain.
- [ ] Dependencies point inward.
- [ ] Ports describe business capabilities.
- [ ] Adapters isolate technology.
- [ ] Application Services remain thin.
- [ ] Runtime concerns remain outside the Domain.
- [ ] Infrastructure remains replaceable.
- [ ] Tests can execute without infrastructure.
- [ ] The Composition Root assembles all concrete implementations.

---

# Common Modelling Mistakes

Avoid:

- designing around frameworks
- exposing infrastructure through Ports
- placing business rules in Adapters
- generic "manager" classes
- large Ports
- large Adapters
- Domain imports of infrastructure packages

Most architectural problems begin as small convenience decisions.

---

# Mosaic Guidelines

Within Mosaic:

- The Domain MUST be designed before infrastructure.
- Ports SHOULD emerge naturally from business requirements.
- Adapters MUST isolate technology.
- Translation MUST occur at architectural boundaries.
- Application Services SHOULD remain orchestration only.
- Runtime concerns MUST remain outside the Domain.
- Infrastructure MUST remain replaceable.
- Architectural simplicity SHOULD always outweigh unnecessary abstraction.

---

# Relationship to MEG

This chapter completes the practical implementation guidance of MEG-004.

The remaining documents describe:

- architectural reasoning (ADRs)
- contributor expectations
- terminology
- references

Together, MEG-001 through MEG-004 now define:

- how software is written
- how it executes
- how the business is modelled
- how technology is prevented from corrupting that model

---

# Summary

Hexagonal Architecture is ultimately about one idea.

> **Protect the business from technology.**

Every Port.

Every Adapter.

Every dependency.

Every package.

Every layer.

Should reinforce that principle.

When implemented consistently, changing technologies becomes routine.

Changing the business remains deliberate.

That is the architectural foundation upon which the rest of the Mosaic platform is built.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`12-testing-the-hexagon.md`

**Next File**

`14-adrs.md`
