<!--
File: engineering/meg/MEG-003 Domain-Driven Design/02-ubiquitous-language.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Ubiquitous Language

> *If two engineers use the same word to mean different things, the architecture has already begun to fail.*

---

# Purpose

Software is built through communication.

Engineers discuss:

- requirements
- bugs
- architecture
- behaviour
- design

If every conversation uses different terminology, misunderstandings become inevitable.

Domain-Driven Design addresses this problem through a **Ubiquitous Language**.

Within Mosaic, every significant business concept should have:

- one name
- one meaning
- one owner

Everywhere.

This document defines how a common language is established and maintained throughout the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Every business concept should have one canonical name within its bounded context.**

The language used in:

- source code
- documentation
- ADRs
- architecture
- issues
- discussions

should all describe the domain identically.

Changing terminology changes understanding.

Consistency is therefore an architectural concern.

---

# Why Language Matters

Imagine three engineers discussing the same concept.

Engineer A says:

```
Library
```

Engineer B says:

```
Collection
```

Engineer C says:

```
Catalogue
```

Do they mean the same thing?

Perhaps.

Perhaps not.

The conversation itself becomes ambiguous.

Ubiquitous Language eliminates that ambiguity.

---

# One Concept, One Name

Every business concept should have exactly one canonical name.

Example.

```
Library
```

Never:

```
Catalogue
```

```
Media Collection
```

```
Content Repository
```

unless those genuinely represent different business concepts.

Synonyms create confusion.

Consistency creates understanding.

---

# One Name, One Meaning

Likewise:

One word should never describe multiple concepts.

Poor.

```
Collection
```

Meaning:

- Movie Collection
- Database Collection
- Garbage Collection

Instead:

```
Collection
```

```
Table
```

```
Garbage Collection
```

Different concepts deserve different names.

---

# Language Belongs To The Business

Business terminology should come from domain experts.

Not software engineers.

Example.

Users understand:

```
Continue Watching
```

They do not naturally understand:

```
Playback Resume Projection
```

The software should therefore adopt the business language.

Not invent its own.

---

# Code Should Read Like Documentation

Good domain code should read naturally.

Example.

```go
playback.Resume(user, media)
```

Rather than:

```go
playback.ExecuteResumeOperation(...)
```

Or:

```go
playback.ProcessPlaybackResumeHandler(...)
```

Business language naturally reduces unnecessary technical vocabulary.

---

# Conversations Should Match Code

Suppose someone asks:

> Why isn't Continue Watching updating?

Engineers should immediately recognise:

```
Continue Watching
```

because:

- the package
- the domain
- the events
- the documentation

all use exactly the same phrase.

No translation should be required.

---

# Business Before Technology

Avoid introducing technical terminology into the domain.

Poor.

```
Projection
```

```
DTO
```

```
Entity Model
```

```
Persistence Object
```

Preferred.

```
Playback

Library

Metadata

Artwork

Recommendation
```

Technical concepts belong in infrastructure.

Business concepts belong in the domain.

---

# Context Matters

One important idea in Domain-Driven Design is that words may legitimately have different meanings in different bounded contexts.

Example.

```
Collection
```

Within Library:

A user-created grouping of media.

Within Database:

A MongoDB collection.

These meanings are acceptable because they belong to different contexts.

Language should remain consistent *within* a context.

Not necessarily globally.

This principle is central to Evans' concept of bounded contexts. ([books.google.com](https://books.google.com/books/about/Domain_Driven_Design_Reference.html?id=ccRsBgAAQBAJ&utm_source=chatgpt.com))

---

# Domain Vocabulary

Every bounded context SHOULD maintain its own vocabulary.

Example.

## Playback

```
Play

Pause

Resume

Seek

Complete
```

---

## Library

```
Import

Scan

Collection

Folder

Source
```

---

## Metadata

```
Artwork

Synopsis

Cast

Episode

Season
```

Each vocabulary should remain focused upon its own business concerns.

---

# Events Use Ubiquitous Language

Event names should naturally reinforce the language.

Example.

```
PlaybackStarted
```

```
PlaybackPaused
```

```
PlaybackCompleted
```

Notice that every event reinforces:

```
Playback
```

Future contributors learn the language simply by reading the event stream.

---

# APIs Use Ubiquitous Language

Public APIs should expose business terminology.

Example.

```
/libraries
```

Not:

```
/catalogues
```

unless those concepts genuinely differ.

The public API is part of the ubiquitous language.

---

# Documentation Uses The Same Language

Architecture specifications.

README files.

ADRs.

Code comments.

All should use the same terminology.

Documentation should never introduce alternative names.

Doing so fragments understanding.

---

# Refactoring Language

Language evolves.

Suppose the business decides:

```
Watch History
```

is better expressed as:

```
Viewing History
```

The change should occur consistently.

Not partially.

The ubiquitous language should evolve together.

Half-completed terminology changes create architectural confusion.

---

# Avoid Abbreviations

Business concepts SHOULD rarely be abbreviated.

Poor.

```
Recs
```

Preferred.

```
Recommendations
```

Poor.

```
Lib
```

Preferred.

```
Library
```

Clarity outweighs brevity.

---

# Avoid Technical Suffixes

Avoid names such as:

```
MediaDTO
```

```
PlaybackEntity
```

```
LibraryRecord
```

The domain should simply contain:

```
Media
```

```
Playback
```

```
Library
```

Infrastructure concerns remain elsewhere.

---

# Language Review

Whenever introducing a new concept ask:

- Would a user understand this?
- Would a product owner use this term?
- Does another word already exist?
- Does this belong to the correct context?
- Does this conflict with existing terminology?

If uncertainty exists:

Improve the language before implementing the software.

---

# Living Language

The ubiquitous language is never complete.

It evolves alongside:

- product understanding
- user feedback
- architectural knowledge
- domain discovery

Language refinement should therefore be viewed as continuous architectural improvement.

---

# Mosaic Examples

Good.

```
Library
```

```
Collection
```

```
Continue Watching
```

```
Playback
```

```
Watch Progress
```

```
Metadata
```

Poor.

```
PlaybackManager
```

```
ContentDTO
```

```
LibraryServiceImpl
```

```
GenericProcessor
```

These names communicate implementation.

Not the business.

---

# Mosaic Guidelines

Within Mosaic:

- Every business concept MUST have one canonical name.
- The same concept MUST NOT have multiple names within one bounded context.
- Business terminology MUST appear consistently across code and documentation.
- Event names MUST reinforce the ubiquitous language.
- APIs SHOULD expose business terminology.
- Technical implementation details MUST remain outside the domain language.
- The language SHOULD evolve alongside business understanding.

---

# Relationship to the Domain

The ubiquitous language forms the foundation of every domain model.

Before defining:

- entities
- value objects
- aggregates
- services

engineers must first agree upon the language describing them.

Without a shared language, no shared model can exist.

The remaining chapters therefore build upon the vocabulary established here.

---

# Summary

The ubiquitous language is one of the most powerful ideas within Domain-Driven Design.

It transforms software from:

> **code describing implementation**

into

> **code describing the business itself.**

When every engineer, architect, product owner and contributor uses the same language, communication becomes dramatically simpler.

Good architecture begins with good conversations.

Good conversations begin with a shared language.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`01-domain-philosophy.md`

**Next File**

`03-subdomains.md`
