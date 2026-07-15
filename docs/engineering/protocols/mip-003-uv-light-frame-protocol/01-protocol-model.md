<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/01-protocol-model.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 01 — Protocol Model

---

# Conformance Language

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** express normative requirements as defined by RFC 2119 and RFC 8174.

---

# Participants

```mermaid
flowchart LR

N1["Artwork Source"]
N2["UVLightFrame Producer"]
N3["Canonical Frame"]
N4["MOS Cache"]
N5["UVLightFrame Consumer"]
N6["Acrylic Transport"]

N1 --> N2
N2 --> N3
N3 --> N4
N3 --> N5
N4 --> N5
N5 --> N6
```

| Participant | Responsibility |
|-------------|----------------|
| Producer | Interprets source colour, normalises artwork coordinates and generates conforming frame data. |
| MOS Cache | May retain reproducible static frames without becoming authoritative. |
| Consumer | Validates frames, reconstructs an active `UVLightField` and exposes it to Acrylic transport. |
| Refraction Engine | Combines the field with three-dimensional Composition state. |

---

# Logical Units

| Unit | Contract |
|------|----------|
| `UVLightFrame` | One immutable artwork-light sample. |
| `UVLightStream` | An ordered sequence of frames from one moving source epoch. |
| `UVLightField` | Consumer-owned temporal reconstruction; not a serialised unit in this protocol. |

One frame MUST remain independent from:

- a particular Acrylic object
- Composition position or orientation
- screen resolution
- renderer API
- final display tone mapping

---

# Conformance Profiles

MIP-003 v1 defines two representations of the same semantics.

| Profile | Use |
|---------|-----|
| Canonical serialised profile | Interchange and MOS Cache using KTX 2. |
| Runtime profile | In-process or GPU-resident data using equivalent fields and channel meaning. |

A runtime representation MAY use different memory layout or precision.

It MUST preserve behaviour equivalent to the canonical profile within its declared numeric precision.
