<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/00-document-control.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 00 — Document Control

---

# Document Information

| Field | Value |
|-------|-------|
| Document | MIP-003 |
| Title | UVLightFrame Protocol |
| Status | Draft |
| Version | 0.1 |
| Owner | AdamNi-7080 |
| Audience | Artwork-pipeline, MOS Cache, media-pipeline and client-renderer engineers |

---

# Authority

MIP-003 governs the interoperable `UVLightFrame` contract.

It owns:

- logical frame metadata
- canonical payload semantics
- serialised texture profile
- static and streamed compatibility
- producer and consumer validation

It does not own visual Material behaviour.

That authority remains with [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md).

---

# Maturity

Version 0.1 records the initial complete protocol design.

The 64-texel analysis size, half-float payload and permitted compression require implementation benchmarking before technical review.
