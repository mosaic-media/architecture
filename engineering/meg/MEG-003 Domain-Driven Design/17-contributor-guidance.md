<!--
File: engineering/meg/MEG-003 Domain-Driven Design/17-contributor-guidance.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Contributor Guidance

> *Every contribution changes the model. The question is whether it improves our understanding of the business.*

---

# Purpose

The Domain Model is the intellectual centre of the Mosaic platform.

Unlike infrastructure, which changes to support the business, the Domain Model exists to describe the business itself.

Every contributor therefore shares responsibility for protecting:

- business language
- business ownership
- business boundaries
- business behaviour

This document provides practical guidance for engineers contributing to the Mosaic Domain Model.

---

# Philosophy

Within Mosaic:

> **Protect the model before extending it.**

Adding functionality should never weaken:

- ubiquitous language
- aggregate boundaries
- bounded contexts
- business ownership
- domain consistency

The Domain Model should become clearer over time.

Never more complicated.

---

# Before Writing Code

Before implementing a new feature ask:

- What business problem exists?
- Which Bounded Context owns it?
- Which Aggregate protects it?
- Which business rules apply?
- Which Domain Events naturally occur?

Implementation should begin only after these questions have clear answers.

---

# Before Creating A New Domain Concept

Ask:

- Does this concept already exist?
- Is the language consistent?
- Does another Aggregate already own this behaviour?
- Is this genuinely a new business concept?

Avoid creating duplicate concepts with different names.

The ubiquitous language should remain consistent.

---

# Before Creating A New Bounded Context

A new Bounded Context SHOULD only be introduced when:

- the language differs significantly
- ownership differs
- business rules differ
- independent evolution is desirable

A new package does **not** automatically justify a new Bounded Context.

Bounded Contexts represent business boundaries.

Not code organisation.

---

# Before Creating An Entity

Ask:

> Does the business recognise this concept through its identity?

If yes:

Entity.

If no:

Consider a Value Object.

Identity should always have business meaning.

---

# Before Creating A Value Object

Ask:

- Is identity irrelevant?
- Is the concept immutable?
- Does equality depend entirely upon value?

If the answer is yes:

Model a Value Object.

Do not introduce identity unnecessarily.

---

# Before Creating An Aggregate

Ask:

> Which business rules must always remain true together?

Do **not** ask:

> Which objects reference each other?

Consistency determines Aggregate boundaries.

Object relationships do not.

---

# Before Creating A Domain Service

A Domain Service should be the last modelling choice.

Ask:

- Can this behaviour belong to an Aggregate?
- Can it belong to a Value Object?
- Can it belong to an Entity?

Only if the answer is "no" should a Domain Service be introduced.

Large numbers of Domain Services usually indicate weak Aggregate modelling.  [oai_citation:0‡Reddit](https://www.reddit.com/r/DomainDrivenDesign/comments/1sgqsv8/most_ddd_advice_starts_in_the_wrong_place/?utm_source=chatgpt.com)

---

# Before Creating A Repository

Repositories should appear only after:

- the Aggregate exists
- the Aggregate Root is understood
- persistence requirements become necessary

Do not design repositories first.

Model first.

Persist later.

---

# Before Creating A Domain Event

Ask:

- Did something important happen?
- Would the business describe this as a fact?
- Does another capability care about this fact?

If the event describes:

```
Do Something
```

it is probably a command.

If it describes:

```
Something Happened
```

it is probably a Domain Event.

---

# Before Renaming A Business Concept

Changing language changes understanding.

Before renaming:

- update documentation
- update diagrams
- update events
- update repositories
- update package names where appropriate

Language should evolve consistently.

Half-completed terminology changes create architectural confusion.

---

# Before Merging

Every Domain contribution SHOULD satisfy the following checklist.

## Business Language

- Ubiquitous Language remains consistent.
- No duplicate terminology introduced.
- Names communicate business concepts.

---

## Ownership

- Ownership remains explicit.
- Aggregate boundaries remain clear.
- Bounded Context responsibilities remain unchanged unless intentionally modified.

---

## Behaviour

- Business behaviour remains inside the Domain.
- Aggregates enforce invariants.
- Domain Services remain focused.

---

## Events

- Domain Events describe completed facts.
- Aggregate ownership remains correct.
- Event names reinforce business language.

---

## Documentation

- MEG updated where required.
- ADR created for significant modelling changes.
- Context Maps updated where appropriate.
- Glossary updated when introducing new terminology.

The model and its documentation should evolve together.

---

# Avoid Technical Thinking

During modelling discussions avoid asking:

- Which database table?
- Which HTTP endpoint?
- Which JSON schema?

Instead ask:

- What does the business call this?
- Who owns this concept?
- What behaviour exists?
- What rules always remain true?

The domain should remain independent of implementation.

---

# Refactor The Model

Refactoring the Domain Model is encouraged.

Examples include:

- improving terminology
- refining Aggregate boundaries
- simplifying Value Objects
- extracting clearer concepts

Improving understanding is one of the primary goals of Domain-Driven Design.

Refactoring should therefore be viewed positively when it improves the model.

---

# Review Mindset

Domain reviews should focus on:

- business correctness
- language
- ownership
- modelling clarity
- consistency
- maintainability

Questions such as:

> "Does this model better represent the business?"

are significantly more valuable than:

> "Could this be implemented differently?"

Implementation should support the model.

Not redefine it.

---

# Domain Tests

Business behaviour should be verified through domain tests.

Examples include:

- Aggregate invariants
- Entity behaviour
- Value Object validation
- Domain Service decisions
- Domain Events

The Domain should be testable without:

- HTTP
- databases
- runtime infrastructure

Pure domain tests provide the fastest feedback and the clearest business validation.

---

# Learning The Domain

New contributors SHOULD study the Domain Model in the following order.

```
Ubiquitous Language

↓

Subdomains

↓

Bounded Contexts

↓

Context Maps

↓

Aggregates

↓

Entities

↓

Value Objects

↓

Domain Services

↓

Domain Events
```

Understanding terminology first dramatically improves modelling quality.

---

# Engineering Culture

Domain modelling should be collaborative.

Contributors are encouraged to:

- question terminology
- challenge unclear ownership
- simplify concepts
- refine language
- improve documentation
- discuss business behaviour with domain experts

The Domain Model should improve through conversation.

Not individual opinion.

---

# Contributor Checklist

Before requesting review, confirm:

- [ ] The ubiquitous language remains consistent.
- [ ] Business ownership is explicit.
- [ ] Aggregate boundaries remain clear.
- [ ] Domain behaviour remains inside the domain.
- [ ] Invariants remain protected.
- [ ] Domain Events describe completed business facts.
- [ ] Infrastructure concerns have not leaked into the model.
- [ ] Documentation has been updated.
- [ ] The Domain Model is clearer than before.

---

# Relationship to MEG

This document explains how contributors should evolve the Domain Model established throughout MEG-003.

The previous chapters define:

> **How the business should be modelled.**

This chapter defines:

> **How engineers should improve that model over time.**

Protecting the integrity of the Domain Model is a shared engineering responsibility.

---

# Summary

The Domain Model is not simply another layer of the application.

It is the shared understanding upon which the entire platform is built.

Every contribution should strengthen:

- clarity
- ownership
- language
- correctness

Within Mosaic, the highest compliment a contributor can receive is not:

> "That is clever."

It is:

> **"That models the business perfectly."**

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`16-adrs.md`

**Next File**

`glossary.md`
