<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/06-event-versioning.md
Document: MEG-002
Status: Draft
Version: 0.3
-->

# Event Versioning

> *Versioning is an engineering discipline around a protocol contract.*

---

# Purpose

MIP-001 defines event versioning responsibilities.

This chapter explains the engineering expectations for publishers and subscribers.

---

# Publisher Guidance

Publishers should preserve event meaning and evolve payload contracts deliberately.

They should document compatibility expectations before changing an event used by other capabilities or modules.

---

# Subscriber Guidance

Subscribers should treat event versions as part of the contract.

They should reject unsupported versions explicitly and tolerate compatible additions where the protocol allows them.

---

# Runtime Guidance

The Runtime should expose version information to routing, diagnostics and observability without interpreting business payload meaning.

---

# Reference

Protocol authority is provided by:

- MIP-001 — Event Protocol
