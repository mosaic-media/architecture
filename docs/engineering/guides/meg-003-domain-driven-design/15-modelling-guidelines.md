<!--
File: docs/engineering/guides/meg-003-domain-driven-design/15-modelling-guidelines.md
Document: MEG-003
Status: Draft
-->

# Modelling Guidelines

> *The purpose of modelling is not to describe software. It is to understand the business.*

---

# Purpose

The previous chapters introduced the building blocks of Domain-Driven Design:

- Ubiquitous Language
- Bounded Contexts
- Entities
- Value Objects
- Aggregates
- Aggregate Roots
- Domain Services
- Domain Events
- Repositories
- Factories
- Domain Invariants

This document brings those concepts together into practical modelling guidance, and its purpose is to help engineers answer one question.

> **"How should I model a new business capability?"**

---

# Philosophy

Within Mosaic:

> **Model the business as it exists today. Allow tomorrow's understanding to evolve naturally.**

Good models emerge through understanding rather than arriving complete, which is why they are rarely designed perfectly on the first attempt. Model discovery is continuous.

---

# Start With The Business

Every modelling exercise should begin with business questions:

- What problem is being solved?
- What language do users use?
- What concepts exist?
- What behaviours exist?
- What business rules always remain true?

Modelling should not begin with database tables, HTTP endpoints, events or packages, because technology follows the model and never the reverse.

---

# Find The Ubiquitous Language

Before writing code, identify the language by asking:

- What nouns exist?
- What verbs exist?
- Which concepts appear repeatedly?
- Which words are ambiguous?

The answers become the ubiquitous language, and that language then becomes the documentation, the code, the package names and the event names. Every future engineering decision builds upon this vocabulary.

---

# Identify The Bounded Context

Ask:

> **Who owns this concept?**

Every new concept belongs to one Bounded Context, such as Playback, Metadata or Library. If ownership is unclear, do not continue modelling; clarify ownership first.

---

# Identify The Aggregate

Ask:

> **What business rules must always remain consistent together?**

Not:

> **Which objects reference one another?**

Consistency determines Aggregate boundaries and object graphs do not, which is one of the central heuristics for aggregate design in Domain-Driven Design. ([dddcommunity.org](https://dddcommunity.org/wp-content/uploads/files/pdf_articles/Vernon_2011_1.pdf))

---

# Find The Aggregate Root

Every Aggregate should answer:

> **Which object protects the business rules?**

The answer becomes the Aggregate Root, and everything else remains internal. If multiple objects appear equally important, the Aggregate boundary probably requires refinement.

---

# Identify Entities

Ask:

> **Which concepts possess identity?**

Media, Collection and Playback Session are examples. Identity determines Entities, not storage.

---

# Identify Value Objects

Ask:

> **Which concepts are defined entirely by their value?**

Duration, Language and Resolution are examples. Whenever identity is unnecessary, prefer a Value Object.

---

# Model Behaviour

Ask:

> **What does this concept do?**

Not:

> **What fields does it contain?**

A Media reduced to its fields records nothing the business actually asked for, whereas a Media that exposes behaviour describes what the business can do with it.

```mermaid
flowchart TD

N1["Media"]
N2["Rename()"]
N3["Archive()"]
N4["Move()"]
N5["Restore()"]

N1 --> N2
N1 --> N3
N1 --> N4
N1 --> N5
```

Business behaviour should dominate the model.

---

# Protect Invariants

Every Aggregate should answer:

> **What business rules must never become false?**

Those rules become Domain Invariants, and they should be enforced automatically, consistently and immediately. Business correctness should never depend upon callers remembering validation.

---

# Raise Domain Events

Whenever an important business fact becomes true, raise a Domain Event: when Playback reaches `Complete()`, it raises `PlaybackCompleted`. Do not ask:

> Should other capabilities care?

That question belongs to the runtime.

---

# Introduce Domain Services Carefully

Ask:

> **Does this behaviour naturally belong to an Aggregate?**

If it does, keep it there; if it does not, consider a Domain Service. Domain Services should remain rare, because they represent important business behaviour that has no natural owner.

---

# Introduce Repositories Last

Repositories exist only after the Domain Model exists, so do not begin with persistence. Model first and persist later. Repositories support the Domain; they do not define it.

---

# Model Small

Prefer Playback over Media Platform, and RecommendationEngine over BusinessManager. Small models are easier to understand, easier to evolve and easier to test, whereas large models usually hide multiple responsibilities.

---

# Evolve Continuously

Do not expect the first model to remain correct. As understanding improves, expect to:

- rename concepts
- split Aggregates
- refine language
- move behaviour
- redefine boundaries

Changing the model is evidence of improved understanding, not failure.

---

# Resist Technical Thinking

A model assembled from a DTO, an Entity, a Controller and a Repository communicates implementation, whereas a model in which Playback reaches `Complete()` and raises `PlaybackCompleted` communicates the business. The second describes something the business recognises, and the Domain should therefore remain free from technical vocabulary.

---

# Avoid Premature Generalisation

Do not model hypothetical future concepts. A Universal Media Item that supports everything and might be useful later is a poor model, whereas Movie, Series and Book are better because each is a concept the business already has. Generalisation should emerge naturally, not speculatively.

---

# Draw The Model

Before implementing, draw. A sketch of a Playback Session alongside its Progress, Duration and Resume Position costs almost nothing to produce.

```mermaid
flowchart TD

N1["Playback Session"]
N2["Progress"]
N3["Duration"]
N4["Resume Position"]

N1 --> N2
N1 --> N3
N1 --> N4
```

Simple diagrams frequently reveal missing concepts, incorrect ownership and unnecessary coupling, so visual modelling is often cheaper than implementation.

---

# Ask Better Questions

The questions worth asking repeatedly during modelling stay on the business side of the boundary:

- What does the business call this?
- Who owns this concept?
- What happens when this changes?
- What business rules exist?
- What events naturally occur?
- What cannot be allowed to happen?

Good questions produce good models.

---

# Modelling Checklist

Before implementing a new capability ask:

- [ ] Is the ubiquitous language clear?
- [ ] Does the concept belong to one Bounded Context?
- [ ] Is ownership obvious?
- [ ] Have Entities been distinguished from Value Objects?
- [ ] Are Aggregate boundaries driven by consistency?
- [ ] Does one Aggregate Root protect the Aggregate?
- [ ] Are Domain Events identified?
- [ ] Are invariants explicit?
- [ ] Does the model avoid infrastructure concerns?
- [ ] Can another engineer explain the model in business terms?

If any answer is "no", continue modelling and let implementation wait.

---

# Common Modelling Mistakes

Modelling mistakes tend to take the same shape, in that the model describes the machinery rather than the business. Avoid:

- modelling databases
- modelling APIs
- modelling transport
- modelling frameworks
- modelling packages

Model behaviour, business rules, ownership, identity and language instead, so that the software becomes an expression of the business rather than of the implementation.

---

# Mosaic Guidelines

Within Mosaic:

- Model the business before the software.
- Prefer rich domain models.
- Behaviour should remain inside the domain.
- Aggregates should remain small.
- Ubiquitous Language should remain consistent.
- Infrastructure must remain outside the domain.
- Models should evolve continuously.
- Simplicity should always be preferred over speculative flexibility.

---

# Relationship to MEG

This chapter completes the tactical modelling guidance of MEG-003, and the remaining documents describe architectural reasoning (ADRs), contributor expectations, terminology and references. The next engineering specification, **[MEG-004](../meg-004-hexagonal-architecture/index.md) – Hexagonal Architecture**, will describe how these Domain Models interact with infrastructure without compromising their integrity. Together, MEG-003 and [MEG-004](../meg-004-hexagonal-architecture/index.md) define both **what** the business model is and **how** it remains protected from technical concerns.

---

# Summary

Domain-Driven Design is not a collection of patterns; it is a way of thinking. Within Mosaic, every model should answer one simple question:

> **"Does this make the business easier to understand?"**

If the answer is yes the model is probably improving, and if the answer is no the implementation is almost certainly modelling technology rather than the business. That distinction is the difference between software that merely works and software that continues to evolve gracefully for years.
