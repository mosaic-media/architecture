<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/04-canonical-texture-profile.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 04 — Canonical Texture Profile

---

# Container

The canonical serialised `UVLightFrame` MUST be a KTX 2 texture.

It MUST use the standard KTX 2 identifier and structural validation rules.

MIP-003 does not define a separate public file extension.

MOS Cache MAY store the KTX 2 payload as a derived cache entry.

---

# Texture Header Profile

| KTX 2 field | Required value |
|-------------|----------------|
| `vkFormat` | `VK_FORMAT_R16G16B16A16_SFLOAT` |
| `typeSize` | `2` |
| `pixelWidth` | Base-level width defined by the normalisation profile. |
| `pixelHeight` | Base-level height defined by the normalisation profile. |
| `pixelDepth` | `0` |
| `layerCount` | `0` |
| `faceCount` | `1` |
| `levelCount` | Complete mip chain through `1 × 1`. |
| `supercompressionScheme` | `0` for none or `2` for Zstandard. |

Consumers MUST support unsupercompressed frames.

Zstandard support is optional and MUST be capability-negotiated before interchange.

BasisLZ, ZLIB and vendor supercompression schemes are not conforming MIP-003 v1 encodings.

The Data Format Descriptor MUST declare linear transfer characteristics and BT.2020 primaries.

`KTXorientation` MUST be present with the value `rd`.

---

# Channel Model

Each texel contains four binary16 floating-point components.

| Component | Semantic |
|-----------|----------|
| `R` | Area-weighted mean linear BT.2020 red. |
| `G` | Area-weighted mean linear BT.2020 green. |
| `B` | Area-weighted mean linear BT.2020 blue. |
| `A` | Maximum coverage-weighted relative luminance within the represented source footprint. |

The `A` component is named **peak luminance** by this protocol.

It is not transparency and RGB values are not premultiplied by it.

Relative luminance MUST be calculated from linear BT.2020 values:

```text
Y = 0.2627 R + 0.6780 G + 0.0593 B
```

All components MUST be finite and non-negative.

Canonical writers MUST encode zero as positive zero and MUST NOT emit NaN or infinity.

Before binary16 quantisation, peak luminance MUST be greater than or equal to the luminance of mean RGB.

Validators SHOULD permit one binary16 unit in the last place when checking that relationship.

Peak luminance is a highlight-distribution hint.

A consumer MUST NOT interpret it as additional integrated energy beyond the mean RGB contribution represented by the texel.

---

# KTX Metadata

MIP-003 values MUST be NUL-terminated UTF-8 strings in KTX key/value data.

| Key | Requirement |
|-----|-------------|
| `mosaic.uvlf.version` | Required `major.minor` payload version. |
| `mosaic.uvlf.source-id` | Required `sourceId`. |
| `mosaic.uvlf.source-revision` | Required `sourceRevision`. |
| `mosaic.uvlf.generator` | Required producer identity and version. |
| `mosaic.uvlf.frame-kind` | Required `static` or `stream`. |
| `mosaic.uvlf.epoch` | Required unsigned decimal integer. |
| `mosaic.uvlf.sequence` | Required unsigned decimal integer. |
| `mosaic.uvlf.pts` | Required signed decimal integer for stream frames; absent for static frames. |
| `mosaic.uvlf.timescale` | Required positive decimal integer for stream frames; absent for static frames. |
| `mosaic.uvlf.channel-model` | Required value `mean-linear-bt2020+peak-y`. |
| `mosaic.uvlf.emission-model` | Required value `surface-normal-lambertian`. |

The total KTX key/value data section MUST NOT exceed 16 KiB.

No individual MIP-003 metadata value may exceed 1 KiB.
