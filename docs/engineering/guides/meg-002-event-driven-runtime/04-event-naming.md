<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/04-event-naming.md
Document: MEG-002
Status: Draft
-->

# Event Naming

> *Event names are part of the protocol. Engineering practice should protect their meaning.*

---

# Purpose

[MIP-001](../../protocols/mip-001-event-protocol/index.md) defines the event naming protocol, and this chapter explains how engineers should apply that protocol while building capabilities.

---

# Engineering Guidance

Event names should describe completed business facts in the language of the publishing capability. Preferred examples include:

```text
media.imported
playback.started
metadata.updated
platform.module.installed
```

Avoid names that describe handlers, transports, queues or implementation mechanics.

Event names should be namespaced according to [MIP-001](../../protocols/mip-001-event-protocol/index.md), and the namespace should identify the event owner. Examples include:

```text
anime.episode.released
jellyfin.library.scanned
platform.started
```

---

# Review Criteria

A new event name should be accepted only when it:

- describes a completed fact
- uses stable domain language
- avoids transport details
- remains meaningful to subscribers
- has a clear publisher owner
- uses a stable namespace
- is declared as public or private in the Module manifest when module-owned

---

# Reference

Protocol authority is provided by:

- [MIP-001 — Event Protocol](../../protocols/mip-001-event-protocol/index.md)
