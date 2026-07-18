<!--
File: docs/design/language/mdl-002-principles/05-principle-03-content-leads.md
Document: MDL-002
Status: Draft
-->

# Principle 03 — Content Leads

---

# Principle Statement

> **Entertainment is always the primary experience. The interface exists to reveal it, never compete with it.**

Within Mosaic, content is the destination.

The interface is merely the path.

Whenever the interface becomes more memorable than the entertainment it presents, the design has failed.

---

# Why This Principle Exists

People do not launch Mosaic because they enjoy user interfaces.

They launch Mosaic because they want to:

- watch a film
- continue an anime
- read a novel
- discover a soundtrack
- explore a franchise

The interface is therefore a supporting actor.

Not the protagonist.

Many design systems begin with components.

Mosaic begins with content.

The interface should emerge naturally from the needs of the entertainment rather than forcing entertainment into predefined layouts. This reflects content-first design approaches, where meaning and user needs are defined before interface structure.  [Content-first Design](https://contentfirstdesign.com/how-we-work-ux/)

---

# Definition

Within MDL, **content** refers to the thing the user actually values.

Examples include:

- films
- television
- anime
- books
- music
- artwork
- metadata
- relationships
- progress

Content does **not** refer to interface chrome.

Buttons are not content.

Navigation is not content.

Settings are not content.

The interface should always communicate the content rather than drawing attention to itself.

---

# Design Rationale

Entertainment already possesses identity.

Books have covers.

Albums have artwork.

Films have cinematography.

Anime has key visuals.

The interface does not need to invent emotion.

It should allow existing emotion to dominate the experience.

Mosaic therefore intentionally separates responsibilities.

| Content | Interface |
|----------|-----------|
| Emotion | Structure |
| Identity | Hierarchy |
| Story | Navigation |
| Atmosphere | Consistency |

Whenever those responsibilities become blurred, the experience becomes visually noisy.

---

# Design Consequences

Applying this principle produces several observable behaviours.

Artwork becomes the primary visual focus.

Whitespace becomes valuable.

Typography becomes quieter.

Navigation becomes secondary.

Motion becomes restrained.

The interface gradually disappears as confidence increases.

---

# Good Examples

## Example 01

A user opens a television series.

The interface immediately establishes:

- current progress
- artwork
- title
- next episode

Supporting information is arranged around the series.

The artwork remains visually dominant.

---

## Example 02

A user opens a novel.

The interface presents:

- book cover
- reading progress
- chapter position
- author

Navigation fades into the background.

Nothing distracts from the reading experience.

---

## Example 03

A user begins playback.

As playback starts:

- interface chrome reduces
- overlays disappear
- controls become contextual

The entertainment now owns the screen.

---

# Anti-patterns

The following behaviours violate this principle.

## Promotional Interfaces

Large promotional banners competing with current content.

---

## Decorative Interfaces

Heavy gradients.

Large glass effects.

Decorative animations.

Visual flourishes with no communicative purpose.

---

## Dashboard Thinking

Attempting to display every possible piece of information simultaneously.

This forces users to interpret the interface rather than enjoy the entertainment.

---

## Interface-Led Design

Designing layouts before understanding the content they must communicate.

The result is content forced into arbitrary containers.

---

# Engineering Implications

Future engineering systems should expose information.

Not presentation.

Presentation should emerge from:

- content
- context
- composition
- relationships

This principle reinforces the long-term separation between information and interface established elsewhere within MDL.

---

# Material Implications

Future MDS specifications should assume:

Artwork provides:

- colour
- emotion
- atmosphere

The interface provides:

- order
- rhythm
- clarity

This distinction should remain consistent regardless of future themes or material systems.

---

# Module Guidance

Modules should contribute meaningful content.

Not decorative interface.

Good module contribution:

```mermaid
flowchart TD

N1["Episode Release"]
N2["Tomorrow"]

N1 --> N2
```

Poor module contribution:

```

Custom animated dashboard
```

Modules strengthen Mosaic by contributing knowledge.

The platform decides how that knowledge should be presented.

---

# Relationship To Other Principles

Content Leads reinforces:

- Context Before Prediction
- Enhancement Before Persuasion
- Be A Companion

It also provides the philosophical foundation for:

- Material System
- Runtime Atmosphere
- Composition Engine

---

# Review Questions

Before approving a proposal ask:

- Does this strengthen the entertainment experience?
- Is the interface supporting rather than competing?
- Would removing interface decoration improve clarity?
- Is the artwork still the strongest visual element?
- Is this communicating content or showcasing interface?

---

# Design Litmus Test

A contributor should be able to cover the interface with their hand and still understand:

- what the user is watching
- where they are
- what comes next

If covering the content instead leaves only an attractive interface...

The interface has become too important.

---

# Summary

Content is why Mosaic exists.

Everything else exists to support it.

The interface should become increasingly invisible as the entertainment becomes increasingly meaningful.

---

# Related Specifications

- [MDL-001 — Mosaic Design Language Vision](../mdl-001-vision/index.md)
- [MDL-005 — Composition Model](../mdl-005-composition-model/index.md)
- [MDS-003 — Material System](../../system/mds-003-material-system/index.md)

---

# Architectural Decisions

| ADR | Decision |
|------|----------|
| ADR-011 | Entertainment is the primary visual hierarchy. |
| ADR-012 | Interface chrome exists only to support content. |
| ADR-013 | Artwork is the primary source of emotion within Mosaic. |
