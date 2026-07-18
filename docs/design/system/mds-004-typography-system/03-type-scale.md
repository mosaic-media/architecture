<!--
File: docs/design/system/mds-004-typography-system/03-type-scale.md
Document: MDS-004
Status: Draft
-->

# Type Scale

---

# Purpose

The Type Scale defines the provisional physical relationship between Mosaic's semantic typography roles.

It does not expose fixed sizes to SDUI, Modules or ordinary components.

---

# Definition

Within MDS, the **Type Scale** is defined as:

> **The ordered ratio system through which semantic typography hierarchy becomes physically readable.**

The client resolves one reference Body size for the current viewing context.

Every other role derives from that reference.

---

# Provisional Alpha Scale

| Role | Scale | Weight | Line height |
|------|------:|-------:|------------:|
| Hero | `2.50×` | `600` | `1.05` |
| Title | `1.75×` | `600` | `1.10` |
| Heading | `1.25×` | `600` | `1.20` |
| Body | `1.00×` | `400` | `1.45` |
| Label | `0.875×` | `500` | `1.20` |
| Metadata | `0.75×` | `400` or `500` | `1.30` |

These values are a provisional alpha baseline.

They become authoritative only after reference compositions validate reading distance, dense layouts, long titles, localisation, accessibility scaling and cross-renderer output.

---

# Weight Discipline

Mosaic permits four normal product weights:

| Weight | Responsibility |
|-------:|----------------|
| `400` | Body and ordinary metadata |
| `500` | Labels, controls and emphasised metadata |
| `600` | Hero, Title and Heading |
| `700` | Exceptional emphasis only |

Weights `800` and `900` are excluded from normal product presentation.

Large typography gains presence through scale and Composition rather than excessive weight.

---

# Client Resolution

The client determines the Body reference from:

- viewing distance
- available extent
- typography metrics
- accessibility preferences
- content density
- renderer capability

It must not select the reference from a permanent device category.

The relative role hierarchy remains stable when physical values change.

---

# Scale Constraints

The resolver must not:

- shrink text arbitrarily to fit a fixed box
- flatten role relationships to display more content
- use weight as decoration
- expose measurements through SDUI
- allow Modules to select a scale stop

When content does not fit, Composition must reflow, disclose progressively or reduce lower-priority information before typography becomes uncomfortable.

---

# Optical Size

Mona Sans optical sizing should resolve automatically where supported.

Clients without optical-size support approximate the same editorial result through validated static instances.

Applications and Modules cannot manipulate optical size.

---

# Validation Backlog

The alpha Design System must test:

- Hero and Title restraint beside artwork
- portrait poster labels below artwork
- long and localised media titles
- television viewing distance
- mobile and windowed reading
- dense calendar and administration layouts
- accessibility text scaling and reflow
- Web and native font metric parity

---

# Summary

The Type Scale establishes stable ratios rather than device-specific pixels.

It preserves one hierarchy while allowing each client to produce readable physical typography.
