<!--
File: docs/design/language/mdl-005-composition-model/07-density.md
Document: MDL-005
Chapter: 07
Title: Density
Status: Draft
Version: 0.4
-->

# Density

---

# Purpose

Density describes **how much understanding should be communicated at one time**.

Within traditional user interface design, density is frequently treated as a visual concern.

Examples include:

- spacing
- margins
- compact mode
- comfortable mode

Within the Mosaic Design Language, density is **not** a visual property.

Density is a property of the Composition.

It determines how much understanding should be communicated before presentation begins.

---

# Definition

Within MDL, **Density** is defined as:

> **The amount of conceptual information intentionally communicated within a Composition.**

Density describes understanding.

Not pixels.

Not spacing.

Not screen size.

---

# Why Density Exists

The amount of information appropriate for one situation is rarely appropriate for another.

Examples.

Watching a film.

The user typically needs:

- playback
- progress
- subtitles
- next episode

Everything else should quietly recede.

Exploring a franchise.

The user now expects:

- relationships
- chronology
- cast
- soundtrack
- adaptations
- production

The Composition naturally becomes denser.

The difference is driven by intent.

Not available space.

---

# Density Is Behaviour

Density should emerge from the user's current activity.

Poor.

```mermaid
flowchart TD

N1["Desktop"]
N2["Dense"]
N3["Phone"]
N4["Sparse"]

N1 --> N2
N1 --> N3
N2 --> N4
N3 --> N4
```

Preferred.

```mermaid
flowchart TD

N1["Watching"]
N2["Sparse"]
N3["Exploring"]
N4["Dense"]

N1 --> N2
N1 --> N3
N2 --> N4
N3 --> N4
```

The behavioural state determines density.

Presentation simply communicates it.

---

# Sparse Composition

Sparse compositions intentionally communicate very little.

Their purpose is clarity.

Characteristics include:

- one obvious Hero
- minimal competing information
- generous breathing space
- strong hierarchy
- low cognitive effort

Examples include:

- playback
- reading
- listening
- continuing

Sparse compositions should help users disappear into entertainment.

---

# Moderate Composition

Moderate density balances:

- continuation
- exploration
- understanding

Examples include:

- series overview
- current season
- artist profile
- author profile

Most everyday interactions should naturally occupy this level.

---

# Rich Composition

Rich compositions support investigation.

Examples include:

- franchise exploration
- collections
- relationship browsing
- administration
- metadata editing

Rich compositions intentionally communicate more understanding.

However...

Hierarchy should remain obvious.

Rich does **not** mean cluttered.

---

# Density Is Relative

The same information may contribute to different density levels depending upon Context.

Example.

```

Reviews
```

Watching.

Low relevance.

Exploring.

High relevance.

The information remains unchanged.

Density changes.

---

# Density Is Adaptive

Density should naturally increase and decrease over time.

Example.

```mermaid
flowchart TD

N1["Playback Begins"]
N2["Sparse"]
N3["Playback Ends"]
N4["Moderate"]
N5["Exploration Begins"]
N6["Rich"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The user should never consciously notice this transition.

They should simply feel that the platform continues supporting their current intent.

---

# Density And Space

Available space influences expression.

It does **not** determine density.

Example.

Television.

Large display.

Current activity.

```

Watching
```

The Composition should remain sparse.

Additional space should strengthen clarity.

Not introduce unrelated information.

Likewise.

Phone.

Limited display.

Current activity.

```

Exploring
```

The Composition should remain rich.

Information should compress.

Not disappear arbitrarily.

Meaning remains stable.

Expression adapts.

---

# Density And Priority

Density should always respect Priority.

```mermaid
flowchart TD

N1["Critical"]
N2["High"]
N3["Medium"]
N4["Low"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Increasing density should reveal progressively lower-priority information.

Reducing density should hide lower-priority understanding first.

Priority therefore governs density.

Never the reverse.

---

# Density And Breathing Space

Sparse compositions naturally contain more breathing space.

Rich compositions naturally contain less.

However...

Breathing space should never disappear completely.

Every Composition requires visual rhythm.

Without rhythm...

Understanding becomes difficult regardless of information quality.

---

# Density Across Domains

Every entertainment domain should support the same density model.

Television.

```mermaid
flowchart TD

N1["Playback"]
N2["Sparse"]

N1 --> N2
```

Books.

```mermaid
flowchart TD

N1["Reading"]
N2["Sparse"]

N1 --> N2
```

Anime.

```mermaid
flowchart TD

N1["Franchise Exploration"]
N2["Rich"]

N1 --> N2
```

Music.

```mermaid
flowchart TD

N1["Artist Discovery"]
N2["Rich"]

N1 --> N2
```

Different media.

Identical behavioural expectations.

---

# Good Examples

## Playback

```mermaid
flowchart TD

N1["Hero"]
N2["Playback"]
N3["Progress"]
N4["Timeline"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Nothing more.

The Composition remains intentionally quiet.

---

## Series Overview

```mermaid
flowchart TD

N1["Hero"]
N2["Continue"]
N3["Timeline"]
N4["Relationships"]
N5["Cast"]
N6["Reviews"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Composition communicates significantly more understanding.

Yet hierarchy remains clear.

---

## Administration

```mermaid
flowchart TD

N1["Navigation"]
N2["Current Task"]
N3["Configuration"]
N4["Diagnostics"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Rich information.

Strong organisation.

No unnecessary decoration.

---

# Anti-patterns

## Artificial Density

Adding information simply because additional space exists.

Understanding decreases.

---

## Responsive Density

Changing density purely because screen size changed.

Behaviour becomes inconsistent.

---

## Maximum Density

Displaying every available concept simultaneously.

The Composition becomes a catalogue.

Not an experience.

---

## Decorative Density

Using visual effects to imply richness without increasing understanding.

Complexity increases.

Meaning does not.

---

# Density Model

```mermaid
flowchart TD

Intent
Intent --> Priority
Priority --> Density
Density --> Composition
Composition --> Expressions
Expressions --> Presentation
```

Density emerges from intent.

Presentation communicates density.

Not the other way around.

---

# Relationship To Future Specifications

Future specifications should treat Density as a conceptual property.

Examples include:

- Composition Engine
- Tile Framework
- Material System
- Motion System
- Responsive Behaviour

Density should influence every one of these systems.

None of them should redefine it.

---

# Summary

Density describes how much understanding should be communicated.

Not how tightly information is arranged.

Sparse compositions optimise immersion.

Rich compositions optimise exploration.

The correct density is always determined by the user's current World.

Never by the available pixels.
