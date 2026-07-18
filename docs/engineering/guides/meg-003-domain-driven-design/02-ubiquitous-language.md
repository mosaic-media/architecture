<!--
File: docs/engineering/guides/meg-003-domain-driven-design/02-ubiquitous-language.md
Document: MEG-003
Status: Draft
-->

# Ubiquitous Language

> *If two engineers use the same word to mean different things, the architecture has already begun to fail.*

---

# Purpose

Software is built through communication. Engineers discuss requirements, bugs, architecture, behaviour and design, and if every conversation uses different terminology, misunderstandings become inevitable. Domain-Driven Design addresses this problem through a **Ubiquitous Language**, under which every significant business concept within Mosaic has one name, one meaning and one owner, everywhere. This document defines how a common language is established and maintained throughout the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Every business concept should have one canonical name within its bounded context.**

The language used in source code, documentation, ADRs, architecture, issues and discussions should all describe the domain identically. Changing terminology changes understanding, so consistency is an architectural concern rather than a matter of style.

---

# Why Language Matters

Imagine three engineers discussing the same concept. Engineer A says Library, Engineer B says Collection and Engineer C says Catalogue. Do they mean the same thing? Perhaps, perhaps not — and while the question remains open the conversation itself is ambiguous. Ubiquitous Language eliminates that ambiguity.

---

# One Concept, One Name

Every business concept should have exactly one canonical name. Where the concept is Library, it is never also called Catalogue, Media Collection or Content Repository, unless those genuinely represent different business concepts. Synonyms create confusion, whereas consistency creates understanding.

---

# One Name, One Meaning

Likewise, one word should never describe multiple concepts. Allowing Collection to mean a Movie Collection, a Database Collection and Garbage Collection is poor, because the word no longer tells the reader which one is meant. Reserve Collection for the business concept and name the others Table and Garbage Collection: different concepts deserve different names.

---

# Language Belongs To The Business

Business terminology should come from domain experts, not software engineers. Users understand Continue Watching, but they do not naturally understand Playback Resume Projection. The software should therefore adopt the business language rather than invent its own.

---

# Code Should Read Like Documentation

Good domain code should read naturally, so that the call itself describes the business behaviour:

```go
playback.Resume(user, media)
```

Neither of the alternatives below reads that way, because each buries the business verb inside technical vocabulary:

```go
playback.ExecuteResumeOperation(...)
```

```go
playback.ProcessPlaybackResumeHandler(...)
```

Business language naturally reduces unnecessary technical vocabulary.

---

# Conversations Should Match Code

Suppose someone asks:

> Why isn't Continue Watching updating?

Engineers should immediately recognise Continue Watching, because the package, the domain, the events and the documentation all use exactly the same phrase. No translation should be required.

---

# Business Before Technology

Avoid introducing technical terminology into the domain. Names such as Projection, DTO, Entity Model and Persistence Object describe the machinery rather than the business, whereas Playback, Library, Metadata, Artwork and Recommendation describe what the platform actually does. Technical concepts belong in infrastructure and business concepts belong in the domain.

---

# Context Matters

One important idea in Domain-Driven Design is that words may legitimately have different meanings in different bounded contexts. Within Library, Collection means a user-created grouping of media; within Database, Collection means a MongoDB collection. These meanings are acceptable because they belong to different contexts, which means language should remain consistent *within* a context rather than necessarily globally. This principle is central to Evans' concept of bounded contexts. ([books.google.com](https://books.google.com/books/about/Domain_Driven_Design_Reference.html?id=ccRsBgAAQBAJ))

---

# Domain Vocabulary

Every bounded context should maintain its own vocabulary, drawn from the concerns that context owns rather than from the platform as a whole.

## Playback

Playback speaks of Play, Pause, Resume, Seek and Complete.

---

## Library

Library speaks of Import, Scan, Collection, Folder and Source.

---

## Metadata

Metadata speaks of Artwork, Synopsis, Cast, Episode and Season.

Each vocabulary should remain focused upon its own business concerns, so a term belongs in one of these lists only where that context genuinely owns the concept it names.

---

# Events Use Ubiquitous Language

Event names should naturally reinforce the language. PlaybackStarted, PlaybackPaused and PlaybackCompleted each repeat the word Playback, so every record of what happened restates the vocabulary at the same time. Future contributors learn the language simply by reading the event stream.

---

# APIs Use Ubiquitous Language

Public APIs should expose business terminology, which means the resource is `/libraries` and not `/catalogues`, unless those concepts genuinely differ. The public API is part of the ubiquitous language.

---

# Documentation Uses The Same Language

Architecture specifications, README files, ADRs and code comments should all use the same terminology. Documentation should never introduce alternative names, because doing so fragments understanding.

---

# Refactoring Language

Language evolves. Suppose the business decides that Watch History is better expressed as Viewing History: the change should then occur consistently rather than partially, because the ubiquitous language is only useful while it holds together. Half-completed terminology changes create architectural confusion.

---

# Avoid Abbreviations

Business concepts should rarely be abbreviated. Recs is poor where Recommendations is preferred, and Lib is poor where Library is preferred, because clarity outweighs brevity.

---

# Avoid Technical Suffixes

Avoid names such as MediaDTO, PlaybackEntity and LibraryRecord. The domain should simply contain Media, Playback and Library, because infrastructure concerns remain elsewhere.

---

# Language Review

Whenever introducing a new concept, the name deserves as much scrutiny as the code, so ask:

- Would a user understand this?
- Would a product owner use this term?
- Does another word already exist?
- Does this belong to the correct context?
- Does this conflict with existing terminology?

If uncertainty exists, improve the language before implementing the software.

---

# Living Language

The ubiquitous language is never complete. It evolves alongside product understanding, user feedback, architectural knowledge and domain discovery, so language refinement should be viewed as continuous architectural improvement.

---

# Mosaic Examples

Good names describe the business, as Library, Collection, Continue Watching, Playback, Watch Progress and Metadata all do. Poor names describe the machinery instead: PlaybackManager, ContentDTO, LibraryServiceImpl and GenericProcessor communicate implementation, not the business.

---

# Mosaic Guidelines

Within Mosaic:

- Every business concept must have one canonical name.
- The same concept must not have multiple names within one bounded context.
- Business terminology must appear consistently across code and documentation.
- Event names must reinforce the ubiquitous language.
- APIs should expose business terminology.
- Technical implementation details must remain outside the domain language.
- The language should evolve alongside business understanding.

---

# Relationship to the Domain

The ubiquitous language forms the foundation of every domain model, because before defining entities, value objects, aggregates and services, engineers must first agree upon the language describing them. Without a shared language, no shared model can exist, and the remaining chapters therefore build upon the vocabulary established here.

---

# Summary

The ubiquitous language is one of the most powerful ideas within Domain-Driven Design. It transforms software from:

> **code describing implementation**

into

> **code describing the business itself.**

When every engineer, architect, product owner and contributor uses the same language, communication becomes dramatically simpler. Good architecture begins with good conversations, and good conversations begin with a shared language.
