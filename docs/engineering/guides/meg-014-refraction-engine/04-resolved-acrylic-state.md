<!--
File: docs/engineering/guides/meg-014-refraction-engine/04-resolved-acrylic-state.md
Document: MEG-014
Status: Draft
-->

# 04 — Resolved Acrylic State

---

# Purpose

The engine should produce one immutable `ResolvedAcrylicState` for each active Acrylic receiver and resolution cycle.

This is a logical client-internal contract rather than a network protocol.

---

# Logical Fields

| Group | Values |
|-------|--------|
| Identity | Receiver identity, Material profile and semantic priority. |
| Source | `sourceId`, `sourceRevision`, epoch and sequence. |
| Projection | Artwork UV transform and selected mip level. |
| Rear Optical Plane | Backdrop availability, sampling transform, bounded displacement, transmission and overscan margin. |
| Acrylic Volume | Tint transmission, incident colour and energy, absorption, scattering, pigmentation falloff and internal parallax. |
| Front Surface Response | Per-boundary incident energy, contour spread, Fresnel, specular and reflection response. |
| Parallax | Whole-surface depth response and fixed cross-layer optical offsets. |
| Secondary response | Bounded aggregate colour and intensity from related Acrylic. |
| Accessibility | Applied contrast, motion and translucency constraints. |
| Quality | Active techniques, update cadence and omitted refinements. |
| Timing | Source timestamp, transition progress and stable-state age. |

---

# Renderer Independence

Resolved state should describe behaviour rather than CSS properties, Dart objects or shader uniforms.

Renderer adapters may translate the same logical state into:

- CSS custom properties
- Flutter widget and paint values
- fragment-shader uniforms
- native compositor parameters

Renderer-specific state must not leak back into Runtime SDUI or `UVLightFrame`.

---

# Immutability

The renderer should receive a complete state snapshot.

It should not observe a partially updated combination of source, edge or parallax values.

When a resolution cycle is cancelled, the previous stable snapshot remains active.

---

# Minimum Acrylic Invariants

Every accepted state should preserve:

- visible material presence
- readable foreground content
- coherent artwork-derived colour
- one fixed apparent-thickness profile
- distinct Rear Optical Plane, Acrylic Volume and Front Surface responsibilities
- source-facing contour response that remains attached to the Acrylic boundary
- bounded motion
- no invented energy

Backdrop distortion, secondary transport and fine parallax may be absent when capability or budget requires simplification.

Tint is the only authored Material parameter.

Renderer or semantic-role changes must not produce a thicker, thinner, glass, frosted or independently configurable Acrylic variant.
