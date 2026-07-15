<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/05-normalisation-and-mip-levels.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 05 — Normalisation And Mip Levels

---

# Base Extent

The MIP-003 v1 base level uses a longest edge of 64 texels.

The producer MUST:

1. apply displayed orientation and crop
2. preserve the resulting artwork aspect ratio
3. set the longest output edge to 64 texels
4. round the other edge to the nearest positive integer

A source smaller than the calculated extent MUST NOT be upscaled solely for analysis.

Both dimensions MUST remain between 1 and 64 texels in v1.

The aspect-ratio error MUST NOT exceed one base-level texel.

---

# Footprint Aggregation

Each output texel represents one rectangular footprint of the normalised source.

For every footprint, the producer MUST calculate:

- area-weighted mean linear BT.2020 RGB
- maximum coverage-weighted relative luminance

Filtering encoded or gamma-adjusted RGB is prohibited.

The mean preserves integrated spatial influence.

The peak preserves evidence of a concentrated highlight that mean filtering alone would erase.

---

# Mip Chain

Every canonical frame MUST contain the complete KTX mip chain ending at `1 × 1`.

Each mip texel MUST preserve the same footprint semantics as the base level:

- RGB is the area-weighted mean of the represented base-level region
- peak luminance is the maximum of the represented base-level region

Implementations MAY generate a level directly from the source or recursively from a higher-resolution level if the result preserves those semantics within binary16 precision.

```mermaid
flowchart LR

N1["Normalised Source"]
N2["64-Texel Base Level"]
N3["Lower Mip Levels"]
N4["Renderer-Selected Level"]

N1 --> N2
N2 --> N3
N2 --> N4
N3 --> N4
```

A consumer MAY select a lower mip level to meet its Dynamic Material Budget.

It SHOULD change levels without changing the frame's exposure relationship.

---

# Temporal Exposure Stability

Frames in one stream epoch MUST share one stable source-to-relative-radiance mapping.

A producer MUST NOT independently stretch the darkest and brightest value of every sampled video frame.

Adaptive analysis MAY change exposure only through a temporally damped source-level transform that avoids visible pumping.

If a transform changes discontinuously, the producer MUST begin a new epoch.
