<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/04-event-naming.md
Document: MEG-002
Status: Draft
Version: 0.1
-->

# Event Naming

> *An event name should describe a business fact so clearly that an engineer unfamiliar with the codebase immediately understands what has happened.*

---

# Purpose

Events form the language of the Mosaic Runtime.

Every capability communicates through events.

Poorly named events create confusion, coupling and ambiguity.

Well-named events create a ubiquitous language shared across:

- Core
- Extensions
- Workers
- Tooling
- Observability
- Documentation

This document defines the naming standards for every event published within the Mosaic ecosystem.

---

# Philosophy

Within Mosaic:

> **Event names describe completed business facts.**

An event should read naturally as a sentence.

For example:

> Playback started.

becomes

```
PlaybackStarted
```

An engineer should never need additional documentation simply to understand what an event represents.

---

# Event Grammar

Every event name follows the same grammatical structure.

```
<Noun><Past Tense Verb>
```

Examples:

```
MediaImported
```

```
PlaybackStarted
```

```
ArtworkDownloaded
```

```
ExtensionInstalled
```

This convention makes event streams readable.

---

# Events Describe History

Events always describe something that has **already happened**.

Correct:

```
MediaDeleted
```

Incorrect:

```
DeleteMedia
```

Correct:

```
UserAuthenticated
```

Incorrect:

```
AuthenticateUser
```

Commands request work.

Events describe completed work.

---

# Business Language

Event names should reflect business terminology.

Good:

```
PlaybackCompleted
```

Poor:

```
UpdatePlaybackFlag
```

Good:

```
LibraryScanned
```

Poor:

```
RunLibraryScanTask
```

Implementation details should never leak into event names.

---

# Singular Events

Events describe a single occurrence.

Prefer:

```
MediaImported
```

Not:

```
MediaImportedBatch
```

If multiple entities are involved, the payload should describe them.

The event itself remains singular.

---

# PascalCase

Event names MUST use PascalCase.

Examples:

```
MetadataFetched
```

```
LibraryCreated
```

```
PlaybackResumed
```

Avoid:

```
metadata_fetched
```

```
metadataFetched
```

```
metadata-fetched
```

Consistency improves discoverability throughout tooling and documentation.

---

# No Technical Prefixes

Avoid implementation-specific prefixes.

Poor:

```
KafkaMediaImported
```

```
RabbitPlaybackStarted
```

```
InternalMetadataUpdated
```

The transport mechanism should never appear within the event name.

Events belong to the business.

Not the messaging infrastructure.

---

# No Version Numbers

Event names MUST remain stable.

Avoid:

```
MediaImportedV2
```

```
PlaybackStarted2
```

Versioning belongs within the event envelope.

Not within the event name.

Future chapters define event versioning.

---

# Avoid Generic Names

Poor:

```
Updated
```

```
Changed
```

```
Completed
```

These names communicate almost nothing.

Instead:

```
MetadataUpdated
```

```
PlaybackCompleted
```

```
LibraryRefreshed
```

The subject should always be explicit.

---

# Avoid Internal Terminology

Suppose the implementation uses:

```
Projection
```

Internally.

The business may understand:

```
Library
```

The event should therefore be:

```
LibraryUpdated
```

Not:

```
ProjectionRebuilt
```

Event names should communicate domain concepts.

Not implementation details.

---

# Avoid CRUD Thinking

Many systems naturally produce events such as:

```
UserCreated

UserUpdated

UserDeleted
```

While acceptable, they often reveal CRUD-centric modelling.

Prefer richer business events where appropriate.

Instead of:

```
MediaUpdated
```

Consider:

```
ArtworkChanged
```

```
MetadataCorrected
```

```
WatchProgressSynced
```

These communicate actual business meaning.

---

# Capability Ownership

The capability owning a business concept owns its events.

Example.

```
Library

↓

MediaImported
```

Only Library should publish:

```
MediaImported
```

Other capabilities may react.

They should not redefine ownership.

---

# Event Families

Related events naturally form families.

Example.

```
PlaybackStarted

PlaybackPaused

PlaybackResumed

PlaybackCompleted

PlaybackStopped
```

This creates a predictable event vocabulary.

New contributors quickly understand relationships.

---

# Event Consistency

Choose one verb.

Use it everywhere.

Example.

If the platform uses:

```
Imported
```

Do not later introduce:

```
Loaded
```

for the same business concept.

Likewise:

```
Installed
```

should not later become:

```
Added
```

Consistency is more valuable than perfect wording.

---

# Avoid Tense Changes

Events always use past tense.

Never mix:

```
PlaybackStarting

PlaybackStarted

PlaybackStart
```

Only one should exist.

Within Mosaic:

```
PlaybackStarted
```

Past tense reinforces that the event represents history.

---

# Naming Checklist

Before introducing a new event ask:

- Does this describe a completed fact?
- Would a business stakeholder understand this?
- Is the name implementation agnostic?
- Does it follow existing terminology?
- Is it sufficiently specific?
- Does it belong to the owning capability?

If any answer is "no", reconsider the name.

---

# Examples

## Good

```
MediaImported
```

```
MetadataFetched
```

```
ArtworkDownloaded
```

```
PlaybackStarted
```

```
PlaybackCompleted
```

```
ExtensionInstalled
```

```
UserAuthenticated
```

---

## Poor

```
DoImport
```

```
UpdateMedia
```

```
TaskFinished
```

```
HandlerExecuted
```

```
MessageReceived
```

```
KafkaImport
```

```
EventV2
```

These names expose implementation rather than business behaviour.

---

# Event Streams

Well-named events naturally produce readable timelines.

```
MediaImported

↓

MetadataFetched

↓

ArtworkDownloaded

↓

LibraryIndexed

↓

RecommendationsUpdated
```

An engineer should understand the entire workflow simply by reading the event stream.

That is the objective.

---

# Mosaic Guidelines

Within Mosaic:

- Event names MUST describe completed facts.
- Event names MUST use PascalCase.
- Event names MUST use past tense.
- Event names MUST represent business concepts.
- Event names MUST NOT contain implementation details.
- Event names MUST NOT include transport technology.
- Event names MUST NOT include version numbers.
- Related events SHOULD use consistent vocabulary.
- Every business concept SHOULD have one canonical event family.

---

# Summary

Event names are more than identifiers.

They form the ubiquitous language of the Mosaic Runtime.

Good event names make:

- documentation easier
- observability clearer
- debugging simpler
- onboarding faster
- extension development more intuitive

Every event should read like a sentence describing something that has already become true.

That simple principle keeps the entire runtime understandable as it continues to grow.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`03-event-model.md`

**Next File**

`05-event-schema.md`
