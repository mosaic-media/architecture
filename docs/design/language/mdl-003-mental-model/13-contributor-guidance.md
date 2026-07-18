<!--
File: docs/design/language/mdl-003-mental-model/13-contributor-guidance.md
Document: MDL-003
Status: Draft
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

```mermaid
flowchart TD

N1["I need a card."]
N2["I need a widget."]
N3["I need a GraphQL type."]

N1 --> N2
N2 --> N3
```

Instead think:

```mermaid
flowchart TD

N1["What does the user need to understand?"]
N2["What information exists?"]
N3["How is it related?"]
N4["What deserves attention?"]
N5["How should it be expressed?"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Implementation naturally follows.

---

# Design From The Top

Contributors should approach every feature using the same conceptual pipeline.

```mermaid
flowchart TD

N1["World"]
N2["Focus"]
N3["Context"]
N4["Information"]
N5["Relationships"]
N6["Composition"]
N7["Expressions"]
N8["Presentation"]
N9["Implementation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
N8 --> N9
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
- modules

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

```mermaid
flowchart TD

N1["Information"]
N2["Relationship"]
N3["Composition"]
N4["Timeline Expression"]
N5["Timeline Tile"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
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

# Modules

Module authors should never ask:

> What interface should I build?

Instead ask:

> What new knowledge can I contribute?

Examples.

Anime Module.

```

Episode Release

Characters

Studio

Soundtrack
```

Book Module.

```

Reading Progress

Author

Series Order

Audiobook
```

The module contributes knowledge.

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

## Module UI

A module attempts to create custom interface.

Question whether the module should instead contribute Information.

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

If contributors consistently think using the concepts introduced by MDL-003, implementation across every client, module and platform will naturally begin to feel like one coherent product.

That is the ultimate purpose of the Mental Model.
