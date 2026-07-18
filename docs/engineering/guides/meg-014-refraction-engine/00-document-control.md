<!--
File: docs/engineering/guides/meg-014-refraction-engine/00-document-control.md
Document: MEG-014
Status: Draft
-->

# Document Control

---

# Document Information

| Field | Value |
|-------|-------|
| Document | MEG-014 |
| Title | Refraction Engine |
| Status | Draft |
| Owner | AdamNi-7080 |
| Audience | Web, native-client, media-pipeline and renderer engineers |
| Classification | Engineering specification |
| Scope | Client-side Acrylic and Refraction implementation guidance |

---

# Authority

MEG-014 owns implementation guidance for:

- Refraction Engine boundaries
- source and Composition inputs
- coordinate and projection mathematics
- resolved Acrylic state
- three-layer Acrylic processing
- bounded secondary Acrylic interaction
- fixed apparent-thickness preservation
- renderer-independent processing
- renderer profiles
- fidelity degradation and overdraw governance
- scheduling and degradation
- engine diagnostics and testing

It does not own:

- Material visual meaning
- `UVLightFrame` serialisation
- Runtime SDUI component contracts
- video decoding

---

# Maturity

Version 0.1 is the first complete engineering design.

It requires prototype measurements before technical review, particularly for CSS filter cost, renderer crossover points, video sampling cadence and [MIP-003](../../protocols/mip-003-uv-light-frame-protocol/index.md) payload choices.

---

# Required Reading

- [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md)
- [MIP-003 — UVLightFrame Protocol](../../protocols/mip-003-uv-light-frame-protocol/index.md)
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/09-runtime-rendering.md)
- [MEG-010 — Performance Engineering](../meg-010-performance-engineering/index.md)
