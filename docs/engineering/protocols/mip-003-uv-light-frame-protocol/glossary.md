<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/glossary.md
Document: MIP-003
Status: Draft
-->

# Glossary

---

# Epoch

One continuous ordering domain within a `UVLightStream`.

A seek, discontinuity or source revision begins a new epoch.

---

# Mean Linear Colour

The area-weighted average colour of a source footprint after transfer decoding and conversion into linear BT.2020.

Its magnitude carries relative brightness.

---

# Peak Luminance

The maximum coverage-weighted relative luminance found within one represented source footprint.

It preserves evidence of concentrated highlights without adding integrated energy.

Runtime layouts may call this component `E` or `peakEnergy`, but its protocol meaning remains relative peak luminance rather than absolute HDR energy.

---

# Relative Radiance

Spatially varying colour and light intensity expressed relative to source reference white rather than absolute nits.

---

# Source Revision

An identifier that changes when source content or any analysis-affecting orientation, crop or colour interpretation changes.

---

# UVLightField

The consumer-owned, temporally reconstructed source sampled by Acrylic transport.

---

# UVLightFrame

One immutable, normalised and downscaled snapshot of artwork-derived relative radiance.

---

# UVLightStream

An ordered sequence of timestamped `UVLightFrame` values from a moving source.
