<!--
File: docs/engineering/architecture/mac-001-platform-architecture/03-capability-model.md
Document: MAC-001
Status: Draft
Version: 0.4
-->

# 03 — Capability Model

---

# Purpose

The Capability Model is the architectural mechanism that lets Mosaic remain modular while still compiling into a single statically linked Go executable.

Capabilities are the units of product behaviour that run on the Mosaic Platform.

The Platform discovers, hosts and governs capabilities.

It does not need to understand their internal behaviour.

Modules contribute implementations.

The Platform owns the capability architecture.

---

# Definition

A capability is a self-contained unit of Mosaic behaviour.

A capability may be:

- built into the initial Platform distribution
- delivered as a first-party module
- delivered as a third-party module
- enabled
- disabled
- upgraded
- removed

The delivery mechanism does not change how the capability participates in the Platform.

Examples include:

- Metadata
- Media
- Artwork
- Authentication
- Search
- Recommendations
- Notifications
- Subtitles
- Storage

The Platform owns the capability contract.

Modules provide implementations.

---

# Philosophy

Within Mosaic:

> **The Platform defines capabilities, the SDK exposes them, Modules implement them and the Platform orchestrates them.**

A Module should never depend on another Module.

Modules should only know about the SDK.

They should never need to know which other Modules exist.

This creates a system that is:

- loosely coupled,
- highly composable,
- naturally extensible,
- compatible with static Go linking.

---

# Capability Responsibilities

Capabilities own:

- business behaviour
- domain rules
- product workflows
- emitted business events
- consumed business events
- user-facing outcomes

Capabilities should express their needs through Platform contracts rather than direct implementation dependencies.

---

# Capability Contracts

Every capability is defined by a Platform contract exposed through the SDK.

The contract is the port.

Modules provide adapters.

Example.

```go
type MetadataProvider interface {
    Lookup(...)
}
```

The Platform defines the interface.

The SDK publishes it.

Modules implement it.

The Platform does not implement domain behaviour merely because it owns the contract.

---

# Platform Responsibilities

The Platform owns the common services capabilities depend upon:

- registration
- dependency validation
- execution
- scheduling
- permissions
- lifecycle
- diagnostics
- provider discovery
- provider routing
- orchestration policy

The Platform should treat built-in and module-delivered capabilities consistently.

---

# Capability Managers

Every capability family should be managed independently by a Platform-owned Capability Manager.

For example, a Metadata Manager may own:

- provider discovery
- routing tables
- orchestration policy
- response merging
- caching
- fallback
- provider validation

Modules never coordinate themselves.

The Platform owns orchestration through Capability Managers.

---

# Capability Types

Capabilities may participate through different cooperation models.

## Single Provider

Exactly one implementation is active.

Examples include:

- storage
- permission engine

Attempting to register multiple active providers for a single-provider capability should produce an error.

## Multiple Providers

Many implementations can contribute to the same capability family.

Examples include:

- metadata
- artwork
- search

Capability Managers decide how providers cooperate.

## Broadcast

Any number of subscribers may react to an event.

Examples include:

- playback started
- media added
- metadata updated

Broadcast behaviour is mediated through the Event Bus.

---

# Provider Routing

Providers advertise what they support.

Example.

```yaml
provider: AniList
supports:
  media:
    - Anime
identifiers:
  - AniList
  - MAL
priority: 100
```

```yaml
provider: TMDB
supports:
  media:
    - Movie
    - TV
priority: 90
```

The Platform routes by capability policy.

Simple numeric priority should not be the only routing mechanism.

Provider selection may account for:

- supported media types,
- supported identifiers,
- supported languages,
- permissions,
- health,
- configuration,
- fallback policy,
- user intent,
- Capability Manager rules.

---

# Capability Metadata

Every provider should expose metadata describing its support and operational requirements.

Typical metadata includes:

- supported media types,
- supported identifiers,
- supported languages,
- priority,
- permissions,
- published events,
- subscribed events.

This metadata allows the Platform to orchestrate providers without hard-coded knowledge of individual Modules.

Capability metadata should be declared in the Module manifest and validated before build.

Runtime registration may expose the same metadata through the SDK registry.

---

# Orchestration Policy

The Platform owns orchestration policy.

Examples include:

| Capability | Policy Examples |
|------------|-----------------|
| Metadata | Route by media type, apply priority, merge results, cache. |
| Search | Broadcast query, merge responses, rank results. |
| Recommendations | Execute multiple providers, combine scores, return unified recommendations. |

Modules implement provider behaviour.

They do not implement cross-provider orchestration policy.

---

# Event Integration

Capabilities may publish and consume events.

The SDK defines:

- Event Envelope
- Event Bus contracts

Modules define:

- event payloads,
- published events,
- subscribed events.

The Platform routes events without understanding every payload.

Events should communicate facts rather than commands.

---

# Runtime Lifecycle

Capability discovery happens automatically as part of normal Go startup after the Supervisor activates a Platform Generation.

Conceptually.

```mermaid
flowchart TD

N1["Supervisor"]
N2["Downloads Modules"]
N3["Builds Platform"]
N4["Platform Starts"]
N5["Go init"]
N6["SDK Registry Populated"]
N7["Capability Managers Built"]
N8["Platform Ready"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

The Platform builds Capability Managers from registered Modules without runtime plugin loading.

---

# Capability Rule

> **A capability is defined by the behaviour it contributes, not by where it is delivered from.**

This keeps first-party and third-party evolution aligned with the same architectural model.

New capabilities require Platform and SDK evolution.

New providers for existing capabilities should usually require only new Modules.
