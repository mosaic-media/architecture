<!--
File: docs/design/language/mdl-002-principles/03-principle-01-context-before-prediction.md
Document: MDL-002
Chapter: 03
Principle: 01
Title: Context Before Prediction
Status: Draft
Version: 0.1
-->

# Principle 01 — Context Before Prediction

---

# Principle Statement

> **Mosaic should first understand what someone is currently doing before attempting to determine what they might do next.**

Current context is considered a more reliable foundation for design than speculative prediction.

Whenever uncertainty exists, contributors should favour present behaviour over inferred future behaviour.

---

# Why This Principle Exists

Most entertainment platforms attempt to answer the question:

> *"What will keep this person engaged?"*

This is a valid objective for commercial services whose success depends upon maximising viewing time.

It is **not** the objective of Mosaic.

Mosaic exists to deepen enjoyment of the entertainment a person has already chosen.

Consequently, Mosaic begins with a different question.

> **"What is this person doing right now?"**

Everything else follows from that answer.

---

# Definition

Within MDL, **context** is defined as:

> The user's current entertainment activity together with the information immediately surrounding that activity.

Context is temporary.

Context evolves naturally.

Context should never permanently define the user.

Examples include:

- currently watching *Frieren*
- currently reading *The Hobbit*
- currently listening to an album
- currently browsing Studio Ghibli films

Context is not:

- favourite genre
- long-term recommendations
- demographic assumptions
- historical engagement scores

Those are historical signals.

Context describes the present.

---

# Design Rationale

People consume entertainment in temporary worlds.

Someone watching anime today may spend tomorrow reading a novel.

Someone immersed in a television series may spend next week listening exclusively to its soundtrack.

These temporary worlds deserve respect.

By recognising current context, Mosaic reduces unnecessary decision making.

Instead of repeatedly asking:

> "What should I do now?"

The interface quietly supports the activity already taking place.

This produces a calmer experience with significantly less cognitive interruption.

Understanding a person's current context is a recognised design principle because people use products within specific situations, environments and goals rather than in isolation.  [oai_citation:0‡GOV.UK](https://www.gov.uk/guidance/government-design-principles?utm_source=chatgpt.com)

---

# What Context Includes

Context may include:

- current media
- current progress
- active domain
- recent interactions
- immediate relationships
- available next actions

Context intentionally excludes:

- advertising priorities
- engagement targets
- commercial promotion
- arbitrary popularity

---

# Examples

## Good

Current Context

```
Watching

Frieren
```

Mosaic presents:

- next episode countdown
- manga continuation
- soundtrack
- production information
- cast
- related novels

Every suggestion strengthens the current experience.

---

## Good

Current Context

```
Reading

The Lord of the Rings
```

Mosaic presents:

- reading progress
- table of contents
- author's other works
- soundtrack
- film adaptations

Again, every suggestion belongs naturally within the current world.

---

## Poor

Current Context

```
Watching

Frieren
```

Interface presents:

- Trending Horror Films
- Popular Reality Shows
- Featured Originals
- Recommended Podcasts

None of these strengthen the current activity.

They interrupt it.

---

# Design Consequences

Applying this principle results in several observable behaviours.

The interface becomes:

- calmer
- more predictable
- less promotional
- easier to understand
- more trustworthy

Users gradually learn that Mosaic responds to what they are doing rather than attempting to redirect them elsewhere.

---

# Engineering Implications

Future engineering systems should preserve context wherever practical.

Examples include:

- composition engine
- runtime atmosphere
- adaptive layouts
- plugin framework
- GraphQL responses

Engineering systems should ask:

> "What information strengthens the current context?"

before asking:

> "What additional information could be shown?"

---

# Plugin Guidance

Extensions should contribute information relevant to the user's current context.

Good examples:

Anime extension

```
Episode airs tomorrow.
```

Book extension

```
Chapter progress updated.
```

Music extension

```
Live concert announced nearby.
```

The extension contributes information.

Mosaic decides whether and how that information becomes part of the current composition.

---

# Relationship To Other Principles

This principle influences:

- Enhancement Before Persuasion
- Content Leads
- Respect the User's Flow
- Be A Companion

It is intentionally evaluated before recommendation strategies, visual hierarchy and interaction design.

---

# Review Questions

Before approving a proposal, reviewers should ask:

- Does this strengthen the user's current context?
- Does it reduce the need for additional decisions?
- Does it respect the user's current activity?
- Does it avoid unnecessary prediction?
- Would this still make sense if popularity metrics disappeared?

If any answer is "no", the proposal should be reconsidered.

---

# Anti-patterns

The following behaviours violate this principle.

- Promoting unrelated content while someone is immersed in another experience.
- Assuming historical preferences outweigh present behaviour.
- Replacing contextual information with trending content.
- Interrupting current entertainment to maximise engagement.

---

# Summary

Context is the starting point for every Mosaic experience.

Prediction may become valuable later.

Context always comes first.

By respecting the user's current world, Mosaic behaves less like an algorithm and more like a trusted companion.

---

# Related Specifications

- MDL-001 Vision
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model

---

# Architectural Decisions

| ADR | Decision |
|------|----------|
| ADR-005 | Context is the primary design input for all user experiences. |
| ADR-006 | Current activity is considered more valuable than inferred future behaviour. |
| ADR-007 | Recommendation systems must strengthen current context before introducing new contexts. |

---

# Review Status

**Status**

Draft

**Next File**

`04-principle-02-enhancement-before-persuasion.md`
