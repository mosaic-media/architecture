<!--
File: docs/engineering/protocols/mip-001-event-protocol/glossary.md
Document: MIP-001
Status: Draft
-->

# Glossary

---

# Envelope

The Platform-owned metadata surrounding an event payload.

---

# Event

An immutable record of a completed fact.

---

# Event Bus

The Platform-owned infrastructure responsible for publishing, subscribing, routing, delivering and observing events.

The Event Bus transports events.

It does not interpret domain payloads.

---

# Event Name

The stable identifier describing what happened.

Event names are namespaced.

---

# Event Version

The identifier describing how the event payload should be interpreted.

---

# Module Event

A domain event owned by a Module.

The Module owns payload, semantics, documentation and versioning.

---

# Payload

The capability-owned business data carried by an event.

---

# Platform Event

A small Platform-owned lifecycle or operational event that belongs to the SDK and Platform contract.

Examples include `platform.started` and `platform.configuration.changed`.

---

# Private Event

A Module-owned event used as an internal implementation detail.

Private events are not part of the Module's external integration contract.

---

# Public Event

A Module-owned event that is part of the Module's documented integration contract.

Other Modules may subscribe to public events through manifest-declared subscriptions.
