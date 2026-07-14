<!--
File: docs/design/language/mdl-002-principles/04-principle-02-enhancement-before-persuasion.md
Document: MDL-002
Chapter: 04
Principle: 02
Title: Enhancement Before Persuasion
Status: Draft
Version: 0.1
-->

# Principle 02 — Enhancement Before Persuasion

---

# Principle Statement

> **Mosaic exists to deepen the entertainment experience a user has already chosen, not persuade them to choose something else.**

The role of Mosaic is to enhance.

It is never to influence for the sake of engagement.

---

# Why This Principle Exists

Most commercial entertainment platforms have objectives that extend beyond helping people consume media.

They optimise business outcomes.

Those outcomes naturally produce behaviours such as:

- trending lists
- promoted releases
- autoplay
- endless recommendation feeds
- "continue watching something else"

These behaviours are not inherently wrong.

They simply optimise for a different objective.

Mosaic has no commercial catalogue to promote.

It therefore has no reason to compete with the user's attention.

---

# Definition

Within MDL, **enhancement** is defined as:

> Providing information or functionality that naturally enriches the user's current entertainment experience.

Enhancement should feel inevitable.

It should never feel promotional.

Persuasion, by contrast, attempts to redirect the user's attention towards another experience.

---

# Design Rationale

Entertainment is emotionally valuable.

People rarely decide:

> "Tonight I'll consume content."

They decide:

> "Tonight I want to watch *Frieren*."

or

> "I'm going to finish my book."

or

> "I'm listening to this album again."

Mosaic should respect that decision.

The software's responsibility begins **after** the user has chosen.

Not before.

---

# The Difference

Enhancement asks:

- What naturally comes next?
- What belongs here?
- What makes this experience richer?
- What removes uncertainty?

Persuasion asks:

- What keeps the user engaged?
- What should replace this experience?
- What is currently popular?
- What maximises interaction?

The distinction appears small.

It fundamentally changes product behaviour.

---

# Examples

## Good

Current Activity

```
Watching

Attack on Titan
```

Mosaic displays:

- Next episode release
- Manga continuation
- Watch order
- Soundtrack
- Related films
- Production history

Every item strengthens the current experience.

---

## Good

Current Activity

```
Reading

Dune
```

Mosaic displays:

- Reading progress
- Character guide
- Sequels
- Audiobook availability
- Film adaptations

Again, nothing attempts to replace the current activity.

---

## Poor

Current Activity

```
Watching

Attack on Titan
```

Interface presents:

- Top 10 Netflix Originals
- Trending Horror
- Popular Comedy
- "Users also watched..."

The current experience has been abandoned.

The interface is now competing with the user's own decision.

---

# Design Consequences

Applying this principle results in interfaces that:

- feel calmer
- build trust
- reward curiosity
- reduce decision fatigue
- encourage deeper exploration

Over time, users begin to understand that Mosaic exists to support them rather than influence them.

That trust becomes part of the product.

---

# Engineering Implications

Future engineering systems should distinguish between:

## Enhancement Information

Information that strengthens the current context.

Examples:

- release schedules
- chapter progress
- soundtrack
- author
- cast
- production studio

---

## Persuasive Information

Information intended primarily to redirect attention.

Examples:

- global popularity
- promoted releases
- sponsored content
- engagement rankings

The core Mosaic experience should prioritise enhancement information.

Persuasive information may exist within optional community extensions but should not become part of the default experience.

---

# Extension Guidance

Plugins should contribute information that naturally extends the current experience.

Examples.

Anime plugin

```
Next episode
```

Book plugin

```
Chapter progress
```

Music plugin

```
Live performance nearby
```

Plugins should avoid injecting unrelated promotional content simply because it is available.

The plugin framework exists to deepen experiences.

Not fragment them.

---

# Relationship To Other Principles

This principle reinforces:

- Context Before Prediction
- Content Leads
- Be A Companion

It is intentionally evaluated before recommendation strategies and content discovery systems.

---

# Review Questions

Reviewers should ask:

- Does this strengthen the user's current experience?
- Does this reduce unnecessary decision making?
- Does this respect the user's existing choice?
- Is this helping...
  or redirecting?
- Would the experience remain valuable if engagement metrics disappeared?

If persuasion becomes the primary objective, the proposal should normally be rejected.

---

# Anti-patterns

The following behaviours conflict with this principle.

- Trending banners replacing current context.
- Promotional homepages.
- Recommendation loops.
- Engagement-first ranking.
- Artificial urgency.
- "Because everyone else watched..."

These patterns optimise attention.

Mosaic optimises enjoyment.

---

# Principle Summary

The user has already made the most important decision.

They have chosen what they wish to enjoy.

Mosaic should respect that decision.

Everything the platform presents afterwards should answer one question.

> **"How can we make this experience even better?"**

Not:

> **"How can we make them choose something else?"**

---

# Related Specifications

- MDL-001 Vision
- MDL-003 Mental Model
- MDL-005 Composition Model
- MDS-003 Composition Engine

---

# Architectural Decisions

| ADR | Decision |
|------|----------|
| ADR-008 | Core Mosaic enhances rather than persuades. |
| ADR-009 | Recommendation systems are subordinate to current context. |
| ADR-010 | The platform should deepen user intent rather than replace it. |

---

# Review Status

**Status**

Draft

**Next File**

`05-principle-03-content-leads.md`
