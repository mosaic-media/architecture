<!--
File: docs/engineering/guides/meg-014-refraction-engine/glossary.md
Document: MEG-014
Status: Draft
-->

# Glossary

---

# Acrylic Interaction Graph

A bounded directed graph describing eligible secondary light transport between spatially related Acrylic receivers.

The graph limits bounce depth and contributing neighbours so direct artwork response remains dominant and runtime cost cannot grow through unbounded feedback.

---

# Acrylic Volume

The middle logical optical layer that filters incident source light through tint, absorption and scattering and carries directional contour energy inward as pigmentation.

---

# Backdrop Participation

Receiver-local sampling, distortion and diffusion of actual Presentation behind Acrylic.

---

# Brand Illumination Pair

The default Mosaic Indigo and Cyan pair, or a resolved co-brand pair containing Mosaic Indigo and one normalised registered partner accent, used to generate a stable synthetic Material-light field when focused and Hero artwork are absent.

---

# Essential Fidelity

The minimum stable Refraction presentation using cached artwork-derived flat or gently graded Acrylic without continuous backdrop, parallax or secondary-transport refinement.

It uses cached artwork-light data, an approved Brand Illumination Pair or the default Mosaic pair without requiring continuous refinement.

---

# Fidelity Level

A capability-driven selection of Refraction refinement identified as Enhanced, Balanced or Essential.

Fidelity Level is independent from renderer technology and device category.

---

# Fidelity Maximum

The highest Refraction fidelity allowed by user preference before accessibility, capability and budget constraints are applied.

---

# Focused Artwork Source

Artwork associated with current Focus and selected before Hero artwork as the primary source.

---

# Front Surface Response

The polished logical optical layer supplying thin contour-bound Fresnel, reflection and specular behaviour.

---

# Optical Parallax

Bounded movement of internal Acrylic composite layers relative to a stable outer mask.

---

# Rear Optical Plane

The logical optical layer that samples structured visible Presentation behind Acrylic using fixed bounded displacement and safe overscan.

---

# Renderer Profile

A measured set of rendering techniques used to realise the same resolved Material semantics.

---

# Resolved Acrylic State

One immutable client-internal snapshot containing the complete renderer-independent behaviour of an Acrylic receiver.

---

# Sampling Window

The receiver-local footprint mapped through Composition transforms into stable artwork UV space.

Moving an Acrylic receiver moves this window over the `UVLightField`; it does not move or regenerate the source `UVLightFrame`.

---

# Stable State

The most recent complete and valid resolved Material snapshot safe for continued Presentation.

---

# Static Brand Emitter

A page-level artwork-free source definition containing normalised `x`, `y` and bounded logical `z` coordinates in the Composition Space parent.

The client combines it with an approved Brand Illumination Pair to generate a stable procedural field without artwork analysis or `.mos` serialisation.

---

# Surface Relationship

The projected position, distance, z separation, orientation, masks and visibility connecting two-dimensional Composition surfaces.
