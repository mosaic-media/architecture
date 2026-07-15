<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/03-coordinates-and-radiance.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 03 — Coordinates And Radiance

---

# Artwork UV Coordinates

MIP-003 uses normalised artwork coordinates after visible orientation and crop have been applied.

| Coordinate | Meaning |
|------------|---------|
| `u = 0` | Left edge of displayed artwork. |
| `u = 1` | Right edge of displayed artwork. |
| `v = 0` | Top edge of displayed artwork. |
| `v = 1` | Bottom edge of displayed artwork. |

For texel coordinates `(x, y)` in a level of extent `(width, height)`, its centre is:

```text
u = (x + 0.5) / width
v = (y + 0.5) / height
```

The top-left texel is `(0, 0)`.

Sampling outside the normalised artwork extent is undefined by this protocol.

---

# Three-Dimensional Direction

MIP-003 v1 does not carry a per-texel direction plane.

Every sample emits from its artwork-local surface position along the outward artwork surface normal using a Lambertian emission model.

The artwork world transform converts that normal into Composition space.

The Refraction Engine derives the vector from the artwork sample to each Acrylic receiver from their Composition transforms.

Receiver position, receiver identity and receiver-relative direction MUST NOT appear in a `UVLightFrame`.

Receiver-specific optical-parallax offsets MUST NOT appear in a `UVLightFrame`.

Artwork and Acrylic may remain two-dimensional surfaces or composites positioned within a three-dimensional Composition coordinate system.

This protocol does not require mesh geometry, extrusion or volumetric scene data.

---

# Relative-Radiance Colour Model

The canonical colour model is:

- linear-light RGB
- ITU-R BT.2020 primaries
- D65 reference white
- relative reference white equal to `1.0`
- no absolute-nit interpretation

Producers MUST decode the source transfer function before filtering or averaging.

They MUST convert source colour into linear BT.2020 before frame generation.

An SDR source MUST NOT be assigned invented HDR headroom or absolute luminance.

Independent per-frame min-max normalisation is prohibited.

Values above `1.0` MAY occur only when supported by source information or a colour conversion; they MUST NOT be fabricated to increase visual impact.

---

# Transparency

Source alpha represents emission coverage rather than a fourth output colour channel.

Before aggregation, a producer MUST multiply source linear RGB and source luminance by effective displayed alpha.

Fully transparent source regions therefore contribute zero relative radiance.
