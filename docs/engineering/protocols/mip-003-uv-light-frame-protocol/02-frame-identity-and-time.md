<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/02-frame-identity-and-time.md
Document: MIP-003
Status: Draft
-->

# 02 — Frame Identity And Time

---

# Logical Metadata

This Draft specification defines payload version `1.0`.

The document version and payload version are independent.

Every frame MUST carry the following logical metadata.

| Field | Type | Requirement |
|-------|------|-------------|
| `protocolVersion` | `major.minor` | MUST equal a supported MIP-003 payload version. |
| `sourceId` | UTF-8 string | MUST identify the artwork or moving-media source within its Platform scope. |
| `sourceRevision` | UTF-8 string | MUST change when source bytes, crop, orientation or colour interpretation changes. |
| `generator` | UTF-8 string | MUST identify the producing implementation and version. |
| `frameKind` | Enumeration | MUST be `static` or `stream`. |
| `epoch` | Unsigned 64-bit integer | MUST identify one continuous ordering domain. |
| `sequence` | Unsigned 64-bit integer | MUST order frames within an epoch. |

`sourceId`, `sourceRevision` and `generator` MUST each contain between 1 and 256 UTF-8 bytes.

They MUST NOT contain control characters.

---

# Static Frames

A static frame MUST use:

| Field | Value |
|-------|-------|
| `frameKind` | `static` |
| `epoch` | `0` |
| `sequence` | `0` |
| presentation timestamp | absent |
| timescale | absent |

A changed source or analysis transform MUST create a new `sourceRevision` rather than mutating a cached frame.

---

# Stream Frames

A stream frame MUST additionally carry:

| Field | Type | Requirement |
|-------|------|-------------|
| `presentationTimestamp` | Signed 64-bit integer | Source presentation time in timescale ticks. |
| `timescale` | Unsigned 32-bit integer | Ticks per second; MUST be greater than zero. |

Within one epoch:

- `sequence` MUST increase strictly
- `presentationTimestamp` MUST NOT decrease
- `timescale` MUST remain constant
- `sourceId` and `sourceRevision` MUST remain constant

A seek, discontinuity or source revision MUST begin a new epoch.

Consumers MUST discard queued frames from an earlier epoch when a newer epoch becomes active.
