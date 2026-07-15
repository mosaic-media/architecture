<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/08-compatibility-and-validation.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 08 — Compatibility And Validation

---

# Protocol Versioning

The payload version uses `major.minor` numbering.

| Change | Version effect |
|--------|----------------|
| Incompatible channel meaning, coordinate system or required representation | Major version. |
| Backward-compatible optional metadata or representation capability | Minor version. |
| Editorial clarification without payload change | No payload-version change. |

A consumer MUST reject an unsupported major version.

A consumer MAY accept a newer minor version only when all required semantics remain understood.

Unknown keys under `mosaic.uvlf.optional.*` MUST be ignored safely.

Any other unknown key under `mosaic.uvlf.*` MUST cause rejection until a compatible protocol revision defines it.

Unknown non-Mosaic KTX metadata follows the KTX 2 specification.

---

# Structural Validation

Before allocating payload storage, a consumer MUST validate:

- KTX 2 identifier, offsets, lengths and alignment
- permitted header-profile values
- dimension and mip-count bounds
- Data Format Descriptor consistency
- metadata size limits
- supercompression support
- decompressed level sizes

The consumer MUST reject overlapping, overflowing or out-of-range sections.

---

# Semantic Validation

Before activation, a consumer MUST validate:

- every required metadata key
- static or stream timing consistency
- supported channel and emission models
- `rd` orientation
- finite non-negative texel values
- peak-luminance relationship
- complete mip-chain dimensions
- sequence and epoch rules for a stream

Invalid frames MUST NOT replace the last stable field.

Consumers SHOULD expose a diagnostic reason suitable for renderer telemetry.

---

# Resource Safety

A MIP-003 v1 base dimension greater than 64 is invalid.

A metadata section greater than 16 KiB is invalid.

Consumers MUST enforce these limits before decompression or GPU upload.

Implementations SHOULD parse untrusted frames using bounded arithmetic and MUST NOT trust KTX offsets or declared uncompressed sizes before validation.

---

# Conformance Cases

A protocol test suite should include:

| Case | Expected result |
|------|-----------------|
| Static 64 × 36 frame with full mip chain | Accept. |
| Stream frame without timestamp | Reject. |
| Static frame with timestamp | Reject. |
| Frame using `KTXorientation=ru` | Reject. |
| Frame containing NaN or negative radiance | Reject. |
| Frame with peak below mean luminance beyond tolerance | Reject. |
| Zstandard frame without negotiated support | Reject without affecting playback. |
| New epoch following a seek | Accept and discard the older epoch queue. |
