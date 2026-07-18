<!--
File: docs/engineering/protocols/mip-001-event-protocol/02-event-envelope.md
Document: MIP-001
Status: Draft
-->

# 02 — Event Envelope

---

# Envelope Model

Every Mosaic event contains:

```mermaid
flowchart TD

N1["Event"]
N2["Envelope"]
N3["Payload"]

N1 --> N2
N1 --> N3
```

The envelope is stable across event families.

The payload is owned by the publishing capability.

The SDK defines the standard Event Envelope.

The SDK does not define every event payload.

Conceptually.

```mermaid
flowchart TD

N1["Event"]
N2["ID"]
N3["Name"]
N4["Source"]
N5["Timestamp"]
N6["Version"]
N7["Payload"]

N1 --> N2
N1 --> N3
N1 --> N4
N1 --> N5
N1 --> N6
N1 --> N7
```

Implementations may expose typed envelopes such as `Event[T]`, but the protocol boundary remains the same.

---

# Envelope Fields

The envelope should provide enough metadata for Platform responsibilities:

- event identifier
- event name
- event version
- occurrence timestamp
- correlation identifier
- causation identifier
- producer identity
- event visibility
- trace context

These fields support routing, diagnostics, replay, idempotency and observability.

---

# Payload Boundary

The payload describes the business fact.

The Platform should not inspect payload structure except where validation or routing explicitly requires it.
