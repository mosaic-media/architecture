<!--
File: docs/design/system/mds-004-typography-system/glossary.md
Document: MDS-004
Status: Draft
-->

# Glossary

---

# A

## Accessibility Typography

Typography resolved according to user accessibility requirements while preserving semantic hierarchy and reading rhythm.

Accessibility may reflow Composition and relax preferred line limits.

---

# B

## Body

The semantic typography role for descriptions, biographies, reviews and sustained reading.

Body establishes the reference size for the provisional Type Scale.

---

# E

## Editorial Hierarchy

The ordered relationship between semantic typography roles derived from Composition.

Typography expresses Editorial Hierarchy but does not create conceptual importance.

## Editorial Role

A semantic typography responsibility independent from physical implementation.

Mosaic defines Hero, Title, Heading, Body, Label and Metadata.

---

# H

## Heading

The semantic typography role that organises a section or conceptual group.

## Hero

The highest semantic typography role, used with restraint to introduce the current Focus when Composition requires a visible typographic title.

## Hero Typography

The editorial expression of the current Hero while preserving the emotional dominance of entertainment artwork.

---

# L

## Label

The semantic typography role for navigation, controls, actions and compact field identification.

---

# M

## Metadata

The subordinate semantic typography role for facts such as runtime, year, rating, timestamp or technical context.

## Mona Sans

The provisional single Platform typeface used across Mosaic semantic typography roles.

Script-specific compatibility fallbacks do not become additional brand typefaces.

---

# O

## Optical Size

A variable-font axis that adapts glyph construction for rendered size.

Mosaic resolves Optical Size automatically where supported.

---

# R

## Reading Rhythm

The deliberate pacing created by type scale, line height, measure, paragraph spacing and hierarchy.

## Responsive Typography

The capability-driven client resolution of semantic typography roles into readable physical values.

Responsive Typography does not use a permanent device class.

## Runtime Typography Resolver

The client-owned subsystem that combines editorial role, viewing context, accessibility, content pressure and renderer capability into concrete typography.

---

# T

## Title

The semantic typography role that identifies the primary page, collection or object.

## Type Scale

The ordered ratio system through which semantic typography hierarchy becomes physically readable.

The current values are provisional alpha baselines.

---

# V

## Variable Font

A font resource that can continuously adapt supported axes such as weight and optical size.

Variable-font behaviour remains behind the Typography Resolver.

---

# W

## Weight

The perceived visual strength of typography.

Mosaic uses weight to reinforce hierarchy and not as decoration.

---

# Cross References

| Specification | Primary concepts |
|---------------|------------------|
| [MDL-005 — Composition Model](../../language/mdl-005-composition-model/index.md) | Hero and hierarchy |
| [MDS-001 — Design Token Architecture](../mds-001-design-token-architecture/index.md) | Primitive type resources and runtime resolution |
| [MDS-003 — Material System](../mds-003-material-system/index.md) | Acrylic information planes |
| [MDS-005 — Motion System](../mds-005-motion-system/index.md) | Reflow continuity |
| [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) | Artwork-title selection and Adaptive Layout |

---

# Terminology Rules

Use Hero, Title, Heading, Body, Label and Metadata for current semantic typography roles.

Describe roles before values and reading conditions before client categories.
