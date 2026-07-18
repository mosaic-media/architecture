<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/03-event-model.md
Document: MEG-002
Status: Draft
-->

# Event Model

> *Engineering should implement events as protocol contracts, not local message shapes.*

---

# Purpose

MEG-002 explains how engineers build an event-driven Runtime. The authoritative event model is defined by **[MIP-001 — Event Protocol](../../protocols/mip-001-event-protocol/index.md)**, and this chapter describes the engineering implications of that protocol.

---

# Engineering Guidance

Every published event should be implemented as an immutable fact that has already occurred, so engineers should avoid using events as:

- commands
- mutable state snapshots
- transport-specific messages
- implementation callbacks

When a component needs to request work, model that request explicitly rather than disguising it as an event.

---

# Runtime Responsibility

The Runtime should preserve the event lifecycle described by [MIP-001](../../protocols/mip-001-event-protocol/index.md), providing routing, delivery, tracing, replay and diagnostics without owning business meaning. The Platform owns the Event Bus, Event Envelope, routing, subscriptions, delivery and reliability, but it should not own Module domain event definitions.

---

# Capability Responsibility

Capabilities own the business facts they publish, and they should use event names and payloads that reflect domain language rather than implementation details. Modules own their domain events, including payloads, documentation and versioning, whereas the SDK owns the shared Event Envelope and Platform lifecycle events. The SDK should not grow every time a Module introduces or evolves a domain event.

---

# Public And Private Module Events

Capabilities should distinguish public and private Module events: public events are part of a Module's documented integration contract, whereas private events are implementation details. Subscribers should depend only on public Module events or Platform events.

---

# Reference

Protocol authority is provided by:

- [MIP-001 — Event Protocol](../../protocols/mip-001-event-protocol/index.md)
