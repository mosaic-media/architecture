<!--
File: docs/engineering/protocols/mip-001-event-protocol/03-event-naming.md
Document: MIP-001
Status: Draft
-->

# 03 — Event Naming

---

# Naming Rule

Event names should describe completed business facts.

Preferred structure:

```text
<namespace>.<fact>
```

Examples:

```text
media.imported
playback.started
metadata.updated
platform.module.installed
```

Event names must be namespaced.

Avoid:

```text
PlaybackStarted
MetadataUpdated
```

Prefer:

```text
playback.started
metadata.updated
```

Namespacing provides:

- collision avoidance
- self-documenting ownership
- easier filtering
- easier debugging

---

# Stability

An event name identifies what happened.

It should remain stable across compatible payload versions.

If the meaning changes, define a new event name rather than overloading the old one.

---

# Vocabulary

Event names should use the ubiquitous language of the publishing capability.

Avoid names that expose infrastructure, transport or handler implementation details.

---

# Namespace Ownership

The event namespace should identify the owner of the event.

Examples:

| Owner | Event Examples |
|-------|----------------|
| Platform | `platform.started`, `platform.configuration.changed` |
| Playback Module | `playback.started`, `playback.buffering` |
| AniList Module | `anime.episode.released`, `anime.metadata.updated` |
| Jellyfin Module | `jellyfin.library.scanned`, `jellyfin.user.synced` |

Modules should not publish events in another Module's namespace.

If a Module reacts to another Module's event, it should publish a new event in its own namespace when it creates a new fact.
