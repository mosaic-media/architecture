<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/05-event-schema.md
Document: MEG-002
Status: Draft
Version: 0.1
-->

# Event Schema

> *Every event should look familiar before its payload is understood.*

---

# Purpose

A runtime containing hundreds of event types requires consistency.

Subscribers should not need to learn a different structure for every capability.

Instead, every event published within the Mosaic Runtime follows a common schema.

This document defines the canonical event schema used throughout the platform.

It intentionally separates runtime concerns from business concerns.

---

# Philosophy

Within Mosaic:

> **Every event consists of an immutable runtime envelope surrounding an immutable business payload.**

The runtime understands the envelope.

Business capabilities understand the payload.

Neither should depend upon the other.

---

# Event Structure

Every event consists of two logical components.

```
Event

├── Envelope
└── Payload
```

The envelope describes:

- identity
- routing
- observability
- tracing
- compatibility

The payload describes:

- business facts

This separation allows the runtime to evolve independently from business domains.

---

# Canonical Event

Conceptually, every event follows the same structure.

```text
Event

├── Metadata
│
│   ├── Event ID
│   ├── Event Name
│   ├── Event Version
│   ├── Occurred At
│   ├── Correlation ID
│   ├── Causation ID
│   ├── Producer
│   └── Trace Information
│
└── Payload
```

Capabilities should primarily concern themselves with the payload.

The runtime owns the metadata.

---

# Envelope

The envelope exists for the runtime.

Business capabilities SHOULD NOT inspect runtime metadata unless explicitly required.

The envelope enables:

- routing
- retries
- replay
- tracing
- observability
- diagnostics

Every event contains the same envelope.

---

# Event ID

Every event MUST contain a globally unique identifier.

Purpose:

- deduplication
- replay
- tracing
- diagnostics
- idempotency

The Event ID identifies the occurrence of a business fact.

Not the business entity itself.

Example.

```
Media ID

≠

Event ID
```

A media item may generate hundreds of events.

Each event receives its own identifier.

---

# Event Name

The Event Name identifies the business fact.

Examples include:

```
MediaImported
```

```
PlaybackStarted
```

```
MetadataFetched
```

Naming standards are defined in the previous chapter.

The Event Name should remain stable across versions.

---

# Event Version

The version identifies the payload contract.

It allows:

- backwards compatibility
- gradual migration
- extension compatibility

Versioning is discussed in detail in the next chapter.

The Event Name identifies **what** happened.

The Event Version identifies **how** the payload should be interpreted.

---

# Occurred At

The timestamp records when the business event occurred.

Not:

- when delivered
- when processed
- when persisted
- when replayed

Time belongs to the business event.

Not the runtime.

---

# Correlation ID

The Correlation ID links related events together.

Example.

```
HTTP Request

↓

MediaImported

↓

MetadataFetched

↓

ArtworkDownloaded

↓

LibraryUpdated
```

Every event shares the same Correlation ID.

This allows complete workflows to be reconstructed through logs and traces.

Correlation IDs are a common practice in distributed and event-driven systems because they enable end-to-end tracing across asynchronous workflows. ([opentelemetry.io](https://opentelemetry.io/docs/concepts/signals/traces/))

---

# Causation ID

The Causation ID records:

> **Which event directly caused this event?**

Example.

```
MediaImported

↓

MetadataFetched

↓

ArtworkDownloaded
```

```
MetadataFetched

↓

Causation ID

↓

MediaImported Event ID
```

Unlike Correlation ID:

The Causation ID changes every time a new event is produced.

Together they form an event graph.

---

# Producer

Every event identifies the capability that produced it.

Examples.

```
Library
```

```
Metadata
```

```
Playback
```

The Producer communicates ownership.

It does **not** imply who should consume the event.

---

# Trace Metadata

Where tracing exists, runtime metadata SHOULD include trace identifiers.

This allows:

- distributed tracing
- performance analysis
- debugging
- request reconstruction

Tracing metadata belongs entirely to the runtime.

Business payloads should remain unaware of tracing.

---

# Payload

The payload contains immutable business facts.

Example.

```
MediaImported

↓

Media ID

Library ID

Source

Imported At
```

Payloads SHOULD contain:

- identifiers
- immutable business data
- sufficient subscriber context

Payloads SHOULD NOT contain:

- retry count
- subscriber state
- delivery status
- processing instructions

---

# Business Context

Payloads should provide enough information for subscribers to make decisions.

Poor.

```
MediaImported

↓

Media ID
```

Every subscriber now performs another lookup.

Better.

```
MediaImported

↓

Media ID

Library ID

Media Type

Source
```

The event communicates useful business context without duplicating the entire domain model.

---

# Payload Ownership

Only the publishing capability defines the payload.

Consumers MUST treat payloads as immutable.

Consumers SHOULD NOT assume additional fields will appear unexpectedly.

Future compatibility is achieved through versioning.

Not runtime mutation.

---

# Event Size

Events SHOULD remain lightweight.

Good payloads contain:

- identifiers
- immutable facts
- small contextual values

Poor payloads contain:

- binary artwork
- video streams
- large metadata blobs
- complete object graphs

Large artefacts should be referenced.

Not embedded.

---

# Event Serialization

The runtime SHOULD serialise events into a transport-neutral format.

Examples include:

- JSON
- Protocol Buffers
- MessagePack

Capabilities MUST remain unaware of serialization details.

Transport is infrastructure.

Events are business concepts.

---

# Unknown Fields

Subscribers SHOULD ignore unknown fields where possible.

This enables:

- gradual evolution
- forward compatibility
- rolling deployments

Consumers should only depend upon fields they actually require.

---

# Validation

Every event SHOULD be validated before publication.

Validation includes:

- required metadata
- payload completeness
- version correctness
- identifier presence

Invalid events should never enter the runtime.

Preventing invalid data is significantly cheaper than recovering from it later.

---

# Example Conceptual Schema

```
Event

├── Event ID
├── Event Name
├── Version
├── Occurred At
├── Correlation ID
├── Causation ID
├── Producer
│
└── Payload

    ├── Business Identifier

    ├── Business Facts

    └── Immutable Context
```

Notice the strict separation between runtime concerns and business concerns.

---

# Mosaic Guidelines

Within Mosaic:

- Every event MUST contain a runtime envelope.
- Every event MUST contain a business payload.
- Envelope metadata MUST remain transport agnostic.
- Payloads MUST remain immutable.
- Event IDs MUST be globally unique.
- Correlation IDs SHOULD span complete workflows.
- Causation IDs SHOULD identify immediate parent events.
- Payloads SHOULD remain compact.
- Business payloads MUST NOT contain runtime state.

---

# Summary

A consistent event schema allows:

- capabilities to remain independent
- runtime infrastructure to evolve
- observability to improve
- replay to function
- versioning to remain manageable
- extensions to interoperate safely

The event schema is therefore one of the most important contracts within the Mosaic Runtime.

Every capability speaks the same language because every event shares the same structure.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`04-event-naming.md`

**Next File**

`06-event-versioning.md`
