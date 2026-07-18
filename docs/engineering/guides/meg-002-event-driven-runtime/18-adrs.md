<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/18-adrs.md
Document: MEG-002
Status: Draft
-->

# Architectural Decision Guidance

> *Decision history belongs in decision records. This chapter identifies when MEG-002 needs them and where readers should look for the governing process.*

---

# Purpose

MEG-002 may require architecture decisions when changes alter long-lived engineering direction, compatibility expectations or responsibility boundaries. The decision process itself is governed by **[MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/index.md)**, so this chapter avoids repeating ADR process rules and the documentation library retains one authoritative home for decision practice.

---

# Decision Areas

Create or update a decision record when a change affects:

- Reactive Runtime
- At-Least-Once Delivery
- Idempotent Subscribers
- Event Envelope
- Event Ownership
- Public And Private Events
- Runtime Scheduling
- Worker Lifecycle
- Backpressure Strategy
- Module Integration Model
- Event Naming

---

# MEG-002 ADR-001 — Platform Transports Events, Modules Own Domain Events

**Status**

Accepted

**Decision Date**

2026-07-14

---

## Context

Mosaic needs event-driven communication between independently developed Modules. A traditional typed event bus would require the SDK or Platform to define every possible event type, which would make the SDK change whenever a Module adds or evolves a domain event. It would also make the Platform aware of domain concepts that should remain Module-owned.

---

## Decision

The Platform owns generic event infrastructure, which means the Platform owns:

- Event Bus
- Event Envelope
- routing
- subscription
- delivery
- reliability
- observability

The SDK owns:

- Event Envelope contract
- Event Bus interfaces
- core Platform lifecycle events

Modules own domain events, so Modules own:

- event names
- payload definitions
- semantics
- documentation
- versioning
- publishers
- subscribers

Event names must be namespaced. Module events may be public or private: public Module events form the Module's documented integration contract, whereas private Module events remain implementation details.

---

## Alternatives Considered

| Alternative | Outcome | Reason |
|-------------|---------|--------|
| SDK owns every event type | Rejected | The SDK would change every time a Module added or evolved a domain event. |
| Platform interprets event payloads | Rejected | It couples Platform infrastructure to business domains. |
| Flat un-namespaced event names | Rejected | It risks collisions and weakens diagnostics. |
| All Module events are public | Rejected | It prevents Modules from evolving internal implementation events freely. |
| Direct Module communication | Rejected | It breaks loose coupling and Module isolation. |

---

## Consequences

The SDK remains stable while the event ecosystem grows, because Modules can evolve domain events independently and the Platform can route, deliver, observe and replay events without understanding payload semantics. Public/private event visibility gives Module authors an explicit external API boundary, and manifests become the discovery and validation surface for published and subscribed events.

---

## Implementation Implications

[MIP-001](../../protocols/mip-001-event-protocol/index.md) defines the event protocol, and [MIP-002](../../protocols/mip-002-module-manifest-protocol/index.md) defines how Module manifests declare public/private event publications and subscriptions. The Event Bus should therefore route by namespaced event name and honour visibility metadata, while tooling should generate event documentation from manifests. Subscribers should depend on public Module events or Platform events, not another Module's private events.

---

# Relationship To [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md)

[MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md) defines ADR structure, review expectations, lifecycle and cross-reference rules. This guide should reference decisions that affect it, but should not redefine the decision process.

---

# Review Guidance

During review, confirm that the guide and any related decision record agree. If a decision changes the meaning of this guide, update the affected chapter and reference the decision from this page.
