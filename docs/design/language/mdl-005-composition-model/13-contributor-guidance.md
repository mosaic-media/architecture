<!--
File: docs/design/language/mdl-005-composition-model/13-contributor-guidance.md
Document: MDL-005
Chapter: 13
Title: Contributor Guidance
Status: Draft
Version: 0.4
-->

# Contributor Guidance

---

# Purpose

The Composition Model is one of the most frequently applied specifications within the Mosaic Design Language.

Unlike the Vision or Principles, contributors will make compositional decisions almost every day.

This chapter exists to ensure those decisions remain consistent across:

- foundational development
- community modules
- future client applications
- future engineering teams

The goal is not to make every interface identical.

The goal is to ensure every interface **feels** unmistakably Mosaic.

---

# Design Understanding First

Never begin by asking:

> Where should this component go?

Instead ask:

> What understanding should this composition create?

Composition exists to communicate understanding.

Everything else is implementation.

---

# Think In Understanding

When designing a new experience, contributors should follow the same conceptual sequence.

```mermaid
flowchart TD

N1["User Intent"]
N2["World"]
N3["Focus"]
N4["Context"]
N5["Information"]
N6["Relationships"]
N7["Priority"]
N8["Composition"]
N9["Expressions"]
N10["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
N8 --> N9
N9 --> N10
```

If implementation begins before this sequence has been completed, the resulting experience will usually become implementation-driven rather than user-driven.

---

# Never Design Pages

Avoid thinking:

```mermaid
flowchart TD

N1["Home Page"]
N2["Details Page"]
N3["Settings Page"]

N1 --> N2
N2 --> N3
```

Instead think:

```mermaid
flowchart TD

N1["Current World"]
N2["Current Focus"]
N3["Current Understanding"]

N1 --> N2
N2 --> N3
```

The interface should emerge naturally from those concepts.

If a contributor begins drawing screens before understanding the Composition, they are working in the wrong order.

---

# Design Hierarchy Before Layout

Contributors should determine:

- what matters
- why it matters
- what supports it
- what can wait

before considering:

- grids
- rows
- columns
- spacing
- breakpoints

Hierarchy always precedes geometry.

---

# Every Composition Tells One Story

A Composition should communicate one primary idea.

Examples.

```

Continue Watching
```

```

Continue Reading
```

```

Discover This Franchise
```

```

Manage Your Library
```

If several unrelated stories compete for attention, the Composition should be reconsidered.

---

# Preserve The Hero

Every Composition should naturally communicate one Hero.

Before introducing new information ask:

> Does this strengthen the Hero...

or...

> Does this compete with it?

Supporting information should reinforce the Hero.

Not challenge it.

---

# Respect Anchors

Anchors preserve orientation.

They should remain behaviourally stable while surrounding information evolves.

Contributors should avoid introducing unnecessary movement or reorganisation around:

- Navigation
- Search
- Current Focus
- Playback

The more adaptive the Composition becomes...

The more valuable Anchors become.

---

# Think In Priority

Contributors should never manually decide that something is visually important.

Instead determine:

```mermaid
flowchart TD

N1["Priority"]
N2["Hierarchy"]
N3["Composition"]
N4["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Visual emphasis should emerge naturally from conceptual importance.

---

# Think In Expressions

Do not think:

```

Timeline Tile
```

Think:

```

Timeline Expression
```

The Expression may later become:

- Tile
- Shelf
- Hero Detail
- Voice Output
- Notification

Expressions survive implementation.

Components rarely do.

---

# Modules

Module authors should contribute:

- Information
- Relationships

They should never attempt to contribute:

- layout
- hierarchy
- hero
- anchors
- density

Those responsibilities belong exclusively to the Composition Model.

Modules enrich understanding.

They do not organise it.

---

# Device Independence

Before implementing a Composition ask:

> Would this still make sense on a television?

On a phone?

On a voice interface?

If the answer is no...

The Composition probably depends upon presentation rather than understanding.

---

# Common Design Smells

The following usually indicate the Composition Model is being bypassed.

## Multiple Heroes

Several concepts compete for attention.

---

## Equal Hierarchy

Every region appears equally important.

---

## Layout Before Meaning

Grid created.

Meaning added afterwards.

---

## Module Layout

Module defines interface.

---

## Device Thinking

Composition changes because screen size changed.

Meaning should remain constant.

Only presentation adapts.

---

# Composition Review Questions

Before implementation ask:

- What is the Hero?
- Why is it the Hero?
- What supports it?
- What belongs in the background?
- Which information could disappear without reducing understanding?
- Which information must never disappear?
- Does this Composition communicate one story or several?

If these questions cannot be answered confidently, continue refining the Composition before implementing it.

---

# Composition Checklist

Every significant Composition should satisfy the following.

- [ ] One Hero exists.
- [ ] Priority is obvious.
- [ ] Hierarchy follows Priority.
- [ ] Anchors preserve orientation.
- [ ] Density matches user intent.
- [ ] Breathing Space reinforces understanding.
- [ ] Expressions remain reusable.
- [ ] Presentation remains replaceable.
- [ ] Modules contribute knowledge rather than layout.
- [ ] Device changes do not alter understanding.

---

# Final Guidance

The Composition Model should become so deeply understood that contributors stop consciously applying it.

Instead of thinking:

> "Where should this go?"

they should naturally think:

> "What understanding am I trying to create?"

When every contributor begins asking that question instinctively, Mosaic will cease feeling like a collection of interfaces.

It will begin feeling like one coherent world.

That is the ultimate objective of the Composition Model.
