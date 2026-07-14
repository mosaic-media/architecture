<!--
File: docs/design/system/mds-004-typography-system/glossary.md
Document: MDS-004
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines the terminology introduced by **MDS-004 — Typography System**.

Unlike previous glossaries, these definitions describe the architectural language of typography rather than implementation details.

These definitions should remain stable regardless of:

- rendering technology,
- font family,
- platform,
- device.

Future specifications should reuse these terms consistently.

---

# A

## Accessibility Typography

Typography resolved according to user accessibility requirements while preserving editorial hierarchy and reading rhythm.

Accessibility Typography strengthens readability without introducing a different editorial language.

---

# B

## Body

The primary editorial role for sustained reading.

Body typography is intended for:

- descriptions,
- reviews,
- biographies,
- long-form editorial content.

Body represents the default reading voice of the Companion.

---

# C

## Caption

The quietest editorial role.

Captions communicate:

- technical metadata,
- timestamps,
- diagnostics,
- secondary context.

Caption should remain readable while avoiding unnecessary visual emphasis.

---

# D

## Display

The highest editorial role.

Display typography is reserved for rare moments such as:

- Hero titles,
- onboarding,
- major transitions.

Display should communicate calm confidence rather than spectacle.

---

# E

## Editorial Hierarchy

The ordered organisation of written language according to conceptual importance.

Editorial Hierarchy is derived from Composition.

Typography expresses it.

---

## Editorial Role

A semantic typography role independent from physical implementation.

Examples include:

- Display
- Heading
- Section
- Body
- Supporting
- Caption

Applications should consume editorial roles rather than font sizes.

---

# H

## Heading

The editorial role responsible for introducing major concepts.

Examples include:

- film titles,
- book titles,
- artist names,
- collection titles.

Headings establish orientation rather than decoration.

---

## Hero Typography

The editorial expression of the current Hero.

Hero Typography introduces the user's current Focus while preserving the emotional dominance of entertainment artwork.

---

# O

## Optical Size

A variable font axis used to improve readability at different rendered sizes.

Optical Size is determined by the Typography Resolver.

Applications should never manipulate it directly.

---

# P

## Paragraph Rhythm

The pacing created by:

- paragraph spacing,
- line spacing,
- editorial hierarchy.

Paragraph Rhythm contributes significantly to long-form reading comfort.

---

## Platform Typography

The platform-specific implementation of the Mosaic Typography System.

Platform Typography preserves editorial meaning while adapting rendering for:

- Web,
- Flutter,
- SwiftUI,
- Compose,
- Television,
- future clients.

---

# R

## Reading Rhythm

The deliberate pacing of typography and spacing that guides readers naturally through a Composition.

Reading Rhythm transforms information into a comfortable reading experience.

---

## Responsive Typography

Typography that adapts to different viewing environments while preserving editorial hierarchy.

Responsive Typography changes implementation.

It does not change meaning.

---

## Runtime Typography Resolver

The runtime subsystem responsible for converting editorial roles into concrete typographic implementation.

Applications consume resolved typography rather than implementing typography themselves.

---

# S

## Section

The editorial role responsible for organising major conceptual groups.

Examples include:

- Continue Watching,
- Cast,
- Chapters,
- Related Works.

Section typography structures understanding.

---

## Supporting

The editorial role used for secondary information.

Examples include:

- runtime,
- author,
- release year,
- language.

Supporting typography remains readable while remaining visually quieter than Body.

---

# T

## Type Scale

The ordered system of editorial typography roles.

The Type Scale expresses hierarchy.

It does not define hierarchy.

---

## Typography Resolver

The conceptual runtime process that transforms editorial roles into resolved typography according to:

- accessibility,
- responsive rules,
- platform,
- viewing environment.

---

# V

## Variable Font

A font capable of continuously adapting properties such as:

- weight,
- width,
- optical size,
- grade.

Within Mosaic, Variable Fonts remain an implementation technique.

Editorial meaning remains unchanged.

---

# W

## Weight

The perceived visual strength of typography.

Weight communicates hierarchy.

It should never become decorative.

Within Mosaic, Weight is resolved by the Typography Resolver rather than selected manually.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| MDL-001 Vision | Companion, Immersion |
| MDL-002 Principles | Calm Interfaces |
| MDL-003 Mental Model | World, Focus |
| MDL-004 Interaction Model | Reading Behaviour |
| MDL-005 Composition Model | Hero, Hierarchy |
| MDS-001 Design Token Architecture | Semantic Roles |
| MDS-003 Material System | Hero Material, Canvas |

---

# Terminology Rules

Future contributors should:

- describe editorial roles before font sizes,
- describe reading before rendering,
- distinguish hierarchy from typography,
- distinguish editorial language from implementation,
- avoid platform-specific terminology inside architectural specifications.

Typography terminology should remain independent from rendering technology.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
