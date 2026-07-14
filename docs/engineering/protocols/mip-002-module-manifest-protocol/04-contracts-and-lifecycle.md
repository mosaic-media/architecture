<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/04-contracts-and-lifecycle.md
Document: MIP-002
Status: Draft
Version: 0.4
-->

# 04 — Contracts And Lifecycle

---

# Provided Contracts

A module should declare the contracts it provides to the Platform or to other capabilities.

Examples include:

- capability contracts
- provider contracts
- event families
- diagnostic surfaces
- health surfaces

---

# Consumed Contracts

A module should declare the contracts it consumes.

This allows the Platform to validate whether required providers exist before activation.

---

# Lifecycle

The manifest should identify lifecycle expectations such as:

- discovery requirements
- activation requirements
- readiness conditions
- shutdown requirements
- health reporting

Lifecycle declarations help the Runtime coordinate modules consistently.

---

# Capability Support

Provider capabilities should declare what they support.

Example.

```yaml
capabilities:
  metadata:
    supports:
      media:
        - Anime
      identifiers:
        - AniList
        - MAL
    priority: 100
```

Capability Managers use these declarations to build routing tables.

The Platform should route work to eligible providers instead of calling every provider.

Capability support metadata should be sufficient for the Platform to make deterministic routing decisions without hard-coded knowledge of the Module.

Typical capability metadata includes:

- supported media types
- supported identifiers
- supported languages
- priority
- required permissions
- published events
- subscribed events

The manifest is the build-time source of truth for this metadata.

Runtime registration may expose the same metadata through the SDK registry, but it must not introduce new undeclared capability support.

---

# Capability Ownership

The manifest may declare implementations for Platform-defined capabilities.

It must not invent new Platform capability contracts.

New capabilities require Platform and SDK evolution.

New providers for existing capabilities may be added by declaring and implementing the existing capability contract.

---

# Events

Modules should declare event publications and subscriptions.

Example.

```yaml
events:
  publishes:
    public:
      - anime.episode.released
      - anime.metadata.updated
    private:
      - anilist.cache.refresh.started
      - anilist.sync.completed
  subscribes:
    - library.item.added
    - platform.started
```

The Platform routes events through the Event Bus.

The Platform does not need to understand every event payload.

Published events should be separated by visibility.

Public published events become part of the Module's documented integration contract.

Private published events remain internal implementation details.

Subscriptions should target public Module events or Platform events.

Modules should not subscribe to another Module's private events.

Every event name should follow the MIP-001 namespaced event naming rules.

The manifest provides:

- documentation
- validation
- discoverability
- compatibility review

without requiring the Platform to understand event payload semantics.
