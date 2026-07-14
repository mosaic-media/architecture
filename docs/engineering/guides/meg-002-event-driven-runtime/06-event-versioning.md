<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/06-event-versioning.md
Document: MEG-002
Status: Draft
Version: 0.1
-->

# Event Versioning

> *Events are contracts. Contracts evolve deliberately, never accidentally.*

---

# Purpose

The Mosaic Runtime is designed to support long-lived capabilities that evolve independently.

Extensions may be developed by different teams.

Some may update immediately.

Others may remain unchanged for months.

Without a clear versioning strategy, even small payload changes can break unrelated capabilities.

This document defines how events evolve while preserving compatibility across the Mosaic ecosystem.

---

# Philosophy

Within Mosaic:

> **Events are immutable. Contracts are versioned. Compatibility is intentional.**

Breaking subscribers because an event changed is considered an architectural failure.

Publishers own compatibility.

Subscribers own resilience.

The runtime coordinates both.

---

# Why Version Events?

Events represent contracts between independently developed capabilities.

Consider:

```
Library

↓

MediaImported

↓

Metadata

↓

Artwork

↓

Search

↓

Recommendations
```

A seemingly harmless payload modification could break every subscriber.

Versioning allows contracts to evolve safely.

---

# Event Contracts

Every event defines a public contract.

The contract consists of:

- Event Name
- Event Version
- Payload Schema
- Business Meaning

Changing any of these may require versioning.

Event versioning is therefore an architectural concern.

Not an implementation detail.

---

# Version Location

Event versions belong inside the runtime envelope.

Example.

```
Event

↓

Event Name

↓

Version

↓

Payload
```

Version numbers MUST NOT appear within:

```
MediaImportedV2
```

The name describes the business fact.

The version describes the payload contract.

These concerns remain separate.

---

# Semantic Compatibility

Changes fall into three categories.

```
Compatible

↓

Conditionally Compatible

↓

Breaking
```

Only breaking changes require a new major event version.

---

# Compatible Changes

The following changes are generally compatible.

- Adding optional fields.
- Expanding enum values where subscribers ignore unknown values.
- Improving documentation.
- Clarifying semantics without changing behaviour.

Existing subscribers should continue functioning without modification.

---

# Conditionally Compatible Changes

Some changes require careful consideration.

Examples include:

- introducing optional nested structures
- changing validation rules
- tightening constraints
- deprecating fields

These changes may require staged rollout.

Architectural review is recommended.

---

# Breaking Changes

Breaking changes require a new event version.

Examples include:

- removing fields
- renaming fields
- changing field meaning
- changing field type
- changing business semantics
- changing identifier behaviour

Subscribers should never unexpectedly observe these changes.

---

# Event Evolution

Events evolve through new versions.

Example.

```
MediaImported

↓

Version 1

↓

Version 2

↓

Version 3
```

The Event Name remains constant.

Only the schema evolves.

This preserves business language while allowing implementation to mature.

---

# Publisher Responsibilities

Publishers own event compatibility.

A publisher introducing a new version MUST:

- define the new schema
- document differences
- provide migration guidance
- consider existing subscribers

Compatibility is the publisher's responsibility.

Not the subscriber's.

---

# Subscriber Responsibilities

Subscribers should process only versions they understand.

If an unsupported version is received they SHOULD:

- reject gracefully
- log appropriately
- avoid undefined behaviour

Subscribers should never guess the meaning of unknown contracts.

---

# Forward Compatibility

Where practical, subscribers SHOULD ignore unknown optional fields.

Example.

```
Version 1

↓

Media ID
```

Later.

```
Version 2

↓

Media ID

Source
```

Version 1 subscribers continue operating.

They simply ignore the additional information.

Forward-compatible consumers significantly simplify rolling deployments.

---

# Backward Compatibility

Publishers SHOULD preserve previous event versions during migration periods.

Example.

```
Publisher

↓

Version 1

Version 2
```

Subscribers migrate independently.

Eventually:

```
Version 1

↓

Deprecated

↓

Removed
```

Migration should be deliberate.

Never immediate.

---

# Deprecation

Deprecated versions SHOULD remain supported for a defined period.

Every deprecation SHOULD include:

- announcement
- migration guidance
- removal timeline

Unexpected removal breaks trust in the runtime.

---

# Schema Evolution

Schema evolution should favour:

```
Addition

↓

Deprecation

↓

Removal
```

Rather than:

```
Replacement
```

Gradual evolution reduces migration risk.

---

# Event Meaning

Versioning should preserve business meaning.

Poor.

```
MediaImported

Version 2

↓

Now means "Media Indexed"
```

Business meaning changed.

A new event should exist instead.

Example.

```
MediaIndexed
```

Versioning evolves schemas.

It does not redefine history.

---

# Runtime Behaviour

The runtime routes events regardless of version.

Subscribers determine compatibility.

Example.

```
MediaImported

↓

Version 2

↓

Runtime

↓

Subscriber

↓

Supports?

↓

Process

or

Reject
```

The runtime remains version agnostic.

Business compatibility belongs to capabilities.

---

# Event Replay

Replay should preserve original versions.

Historical events MUST NOT be upgraded automatically.

Replay reproduces history.

It does not rewrite it.

This property makes replay trustworthy.

---

# Documentation

Every event version SHOULD document:

- schema
- added fields
- removed fields
- semantic changes
- migration guidance

Historical documentation should remain available.

Future contributors should understand why versions changed.

---

# Version Numbering

Event versions SHOULD use simple sequential integers.

Example.

```
Version 1

Version 2

Version 3
```

Semantic Versioning is unnecessary for individual event contracts.

The event version communicates schema evolution only.

Keeping version numbers simple reduces operational complexity.

---

# Version Lifecycle

Every version follows the same lifecycle.

```
Draft

↓

Published

↓

Supported

↓

Deprecated

↓

Retired
```

Only supported versions should be produced by publishers.

Deprecated versions may still be consumed during migration.

---

# Anti-Patterns

The following practices are prohibited.

## Silent Schema Changes

Changing payload structure without increasing the version.

---

## Reusing Version Numbers

Publishing different payloads using the same version.

---

## Renaming Event Types

```
MediaImported

↓

MediaImportedV2
```

Version belongs in metadata.

Not names.

---

## Redefining History

Changing what an existing event means.

History should remain immutable.

---

## Automatic Payload Mutation

Converting historical events into newer schemas during replay.

Replay should reproduce reality.

Not reinterpret it.

---

# Mosaic Guidelines

Within Mosaic:

- Every event MUST include a version.
- Event names MUST remain stable across versions.
- Breaking changes MUST increment the version.
- Compatible additions SHOULD preserve existing versions where possible.
- Publishers MUST own compatibility.
- Subscribers MUST process only supported versions.
- Historical events MUST remain immutable.
- Replay MUST preserve original versions.

---

# Summary

Versioning allows the Mosaic Runtime to evolve without sacrificing stability.

Well-versioned events enable:

- independent capability evolution
- safe extension development
- rolling deployments
- historical replay
- long-term maintainability

Every event is a public contract.

Like every public contract, it deserves deliberate stewardship.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`05-event-schema.md`

**Next File**

`07-event-bus.md`
