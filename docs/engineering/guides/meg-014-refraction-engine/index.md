<!--
File: docs/engineering/guides/meg-014-refraction-engine/index.md
Document: MEG-014
Status: Draft
-->

# MEG-014 — Refraction Engine

> *Resolve one artwork-light source into coherent, physical Acrylic without making rendering technology part of the design language.*

---

# Purpose

MEG-014 explains how Mosaic clients should implement the Refraction Engine defined visually by [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md).

[MIP-003 — UVLightFrame Protocol](../../protocols/mip-003-uv-light-frame-protocol/index.md) defines the source-data contract.

This guide defines the client-owned resolution pipeline between those authorities and Presentation.

---

# Engineering Statement

Within Mosaic:

> **The Refraction Engine resolves two-dimensional Acrylic composites in Composition Space. It does not build a three-dimensional mesh scene.**

The same semantic engine may drive CSS, Flutter composites or two-dimensional fragment renderers.

---

# Scope

This guide covers:

- focused-or-Hero source selection
- local backdrop participation
- two-dimensional Composition surfaces
- direct and secondary Acrylic response
- bounded Acrylic interaction graphs
- Rear Optical Plane, Acrylic Volume and Front Surface resolution
- fixed apparent-thickness and tint-authority invariants
- bounded optical parallax
- coordinate, projection and highlight-rotation mathematics
- resolved Acrylic state
- renderer profiles
- capability-driven fidelity levels and overdraw governance
- temporal scheduling
- playback protection
- resilience, telemetry and validation

It does not redefine Material appearance or the `UVLightFrame` payload.
