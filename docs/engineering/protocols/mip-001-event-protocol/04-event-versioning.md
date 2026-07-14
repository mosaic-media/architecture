<!--
File: docs/engineering/protocols/mip-001-event-protocol/04-event-versioning.md
Document: MIP-001
Status: Draft
Version: 0.2
-->

# 04 — Event Versioning

---

# Purpose

Event versions communicate payload compatibility.

They do not describe implementation progress.

---

# Version Ownership

Event owners own event versioning.

Subscribers own defensive consumption.

The Platform coordinates compatibility by preserving envelope metadata and making version information visible to routing, diagnostics and tooling.

The SDK version should not change simply because a Module evolves one of its own domain events.

Only the owning Module's event contract changes.

Platform lifecycle events are different.

They belong to the Platform contract and therefore evolve through SDK and Platform compatibility policy.

---

# Compatibility

Compatible changes may evolve the payload without breaking existing subscribers.

Breaking semantic changes should use a new version and a deliberate migration path.

The event name describes the fact.

The event version describes how to interpret the payload contract.

---

# Public And Private Event Evolution

Public Module events are integration contracts.

Their payloads should evolve deliberately and maintain documented compatibility expectations.

Private Module events are implementation details.

They may change freely between Module versions unless exposed as public events.

Promoting a private event to public should create documentation, manifest declarations and compatibility expectations before other Modules depend on it.
