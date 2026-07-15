<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/index.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# MIP-003 — UVLightFrame Protocol

> *Artwork light should be computed once, exchanged consistently and resolved according to the Composition.*

---

# Purpose

MIP-003 defines the machine-readable contract through which artwork analysis, MOS Cache and client renderers exchange a `UVLightFrame`.

[MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md) defines the visual meaning of artwork-derived relative radiance and Acrylic transport.

This protocol defines the compatible frame representation.

---

# Protocol Statement

Within Mosaic:

> **A UVLightFrame describes the artwork source. The Composition determines how that source reaches Acrylic.**

The frame preserves spatially varying colour and relative brightness without asserting that source artwork is HDR or storing receiver-relative lighting.

---

# Scope

This protocol defines:

- frame identity and timing
- artwork UV coordinates
- relative-radiance interpretation
- brightness-preserving normalisation
- the canonical KTX 2 texture profile
- mip-level semantics
- streamed-frame ordering
- MOS Cache representation
- compatibility and validation

It does not define:

- visible artwork presentation
- Acrylic transport algorithms
- Acrylic surface bounds, masks, transforms and parallax
- quality-budget policy
- video decode or presentation
