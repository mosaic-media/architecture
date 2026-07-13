<!--
File: design/mdl/MDL-003 Mental Model/13-contributor-guidance.md
Document: MDL-003
Chapter: 13
Title: Contributor Guidance
Status: Draft
Version: 0.1
-->

# Contributor Guidance

---

# Purpose

The purpose of MDL-003 is not simply to document concepts.

Its purpose is to change how contributors think.

A contributor who has fully internalised the Mosaic Mental Model should begin solving user problems from conceptual understanding rather than implementation.

This chapter provides practical guidance for applying the Mental Model throughout everyday engineering and design work.

---

# Think In Concepts

One of the easiest mistakes contributors can make is beginning implementation too early.

Avoid thinking:

```
I need a card.

↓

I need a widget.

↓

I need a GraphQL type.
```

Instead think:

```
What does the user need to understand?

↓

What information exists?

↓

How is it related?

↓

What deserves attention?

↓

How should it be expressed?
```

Implementation naturally follows.

---

# Design From The Top

Contributors should approach every feature using the same conceptual pipeline.

```
World

↓

Focus

↓

Context

↓

Information

↓

Relationships

↓

Composition

↓

Expressions

↓

Presentation

↓

Implementation
```

Skipping layers almost always produces poorer experiences.

---

# Build Understanding

Before writing code, contributors should be capable of describing the proposed feature without mentioning:

- components
- pages
- APIs
- GraphQL
- databases
- plugins

Instead describe:

- World
- Focus
- Context
- Information
- Relationships

If this cannot be done, implementation has begun too early.

---

# Ask Better Questions

Poor design questions include:

> Where should this button go?

> Which page should this live on?

> What widget should display this?

Better questions include:

> What information exists?

> Why is it important?

> What relationship does it reveal?

> How does it strengthen the user's World?

The second set of questions naturally produces more coherent solutions.

---

# Information First

Contributors should think in terms of Information.

Not interface.

Poor.

```
Timeline Widget
```

Better.

```
Episode Release
```

Poor.

```
Recommendation Card
```

Better.

```
Relationship
```

Poor.

```
Progress Bar
```

Better.

```
Progress
```

Information survives interface.

Interface rarely survives information.

---

# Relationships Before Navigation

When users need additional understanding...

Ask:

> Which relationship should be revealed?

before asking:

> Which page should we navigate to?

The first strengthens the Mental Model.

The second strengthens software architecture.

Only one of those belongs to MDL.

---

# Expressions Before Components

Contributors should avoid directly selecting components.

Instead determine the required Expression.

Example.

```
Information

↓

Relationship

↓

Composition

↓

Timeline Expression

↓

Timeline Tile
```

The component becomes an implementation detail.

This approach significantly improves future flexibility.

---

# Think Like A Companion

Every implementation should reinforce the Companion metaphor.

Before introducing interface ask:

> Would a knowledgeable friend mention this?

If yes...

The information probably belongs.

If not...

Question whether the capability genuinely improves the experience.

---

# Plugins

Plugin authors should never ask:

> What interface should I build?

Instead ask:

> What new knowledge can I contribute?

Examples.

Anime Plugin.

```
Episode Release

Characters

Studio

Soundtrack
```

Book Plugin.

```
Reading Progress

Author

Series Order

Audiobook
```

The plugin contributes knowledge.

Mosaic contributes understanding.

---

# The World Is Sacred

Every feature exists inside the user's World.

Features should never fragment that World.

Avoid creating concepts such as:

- separate applications
- isolated dashboards
- disconnected workflows

Instead strengthen the existing World.

---

# Design Smells

The following often indicate the Mental Model is being bypassed.

## New Terminology

A proposal invents a completely new concept.

Question whether an existing concept already exists.

---

## New Navigation

A proposal introduces another navigation path.

Question whether an existing relationship could reveal the same understanding.

---

## Duplicate Information

The same knowledge appears in multiple places for different reasons.

Question whether composition should determine emphasis instead.

---

## Plugin UI

An extension attempts to create custom interface.

Question whether the extension should instead contribute Information.

---

# Review Questions

Before implementation ask:

- What concept am I implementing?
- Where does it exist within the Mental Model?
- Does this strengthen the user's World?
- Is this Information or interface?
- Does this introduce unnecessary concepts?
- Could another contributor explain this feature using only MDL terminology?

If the answers remain unclear...

Return to the Mental Model.

---

# Mental Model Checklist

Every substantial proposal should satisfy the following.

- [ ] The user's World remains coherent.
- [ ] Focus remains understandable.
- [ ] Context determines relevance.
- [ ] Information remains independent from presentation.
- [ ] Relationships strengthen understanding.
- [ ] Composition determines emphasis.
- [ ] Expressions remain reusable.
- [ ] Presentation remains replaceable.

If any item fails, reconsider the design before implementation.

---

# Final Guidance

The Mental Model is not documentation.

It is the conceptual architecture of Mosaic.

Every feature should leave the Mental Model simpler...

...never more complicated.

If contributors consistently think using the concepts introduced by MDL-003, implementation across every client, plugin and platform will naturally begin to feel like one coherent product.

That is the ultimate purpose of the Mental Model.

---

# Review Status

**Status**

Draft

**Next File**

`glossary.md`
