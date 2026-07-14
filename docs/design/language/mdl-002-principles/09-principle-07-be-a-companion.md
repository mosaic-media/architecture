<!--
File: docs/design/language/mdl-002-principles/09-principle-07-be-a-companion.md
Document: MDL-002
Chapter: 09
Principle: 07
Title: Be A Companion
Status: Draft
Version: 0.1
-->

# Principle 07 — Be A Companion

---

# Principle Statement

> **Every interaction within Mosaic should reinforce the feeling that the software is a trusted companion rather than a platform demanding attention.**

Mosaic exists to accompany the user.

Not to become the centre of the experience.

This principle is the behavioural identity of the entire platform.

Every future interaction should be evaluated against it.

---

# Why This Principle Exists

Technology has become increasingly demanding.

Modern applications compete for attention through:

- notifications
- recommendations
- engagement loops
- badges
- autoplay
- promotions
- interruptions

These patterns are commercially successful because attention has become a measurable business metric.

Mosaic has a different objective.

The software exists to support a person's entertainment.

Not to become another source of competition for their attention.

This philosophy aligns closely with the ideas behind *Calm Technology*, where technology should inform without constantly demanding focus, moving between the centre and periphery of attention only when necessary.  [oai_citation:0‡Wikipedia](https://en.wikipedia.org/wiki/Calm_technology?utm_source=chatgpt.com)

---

# Definition

Within MDL, a **companion** is software that:

- understands context
- quietly provides useful information
- respects attention
- remains predictable
- disappears when no longer needed

A companion is not passive.

It is attentive.

The distinction is important.

Passive software waits.

A companion prepares.

---

# Design Rationale

Imagine sitting on a sofa watching a favourite television series.

A trusted friend sitting beside you might occasionally say:

> "The next episode airs tomorrow."

or

> "Did you know this was adapted from a novel?"

or

> "The composer also worked on Interstellar."

Then...

They stop talking.

They do not interrupt the episode every five minutes.

They do not recommend an unrelated reality television programme.

They do not insist you should be watching something more popular.

They simply help.

That is the behavioural model for Mosaic.

---

# Presence

A companion should always feel present.

It should rarely feel visible.

Presence means the user trusts that useful information will be available when required.

Visibility means the interface continually competes for attention.

The objective is presence without intrusion.

---

# Behaviour

The companion should:

- anticipate useful information
- reduce uncertainty
- minimise effort
- preserve continuity
- quietly reassure

The companion should not:

- persuade
- advertise
- distract
- compete
- dominate

---

# Good Examples

## Example 01

Current Context

```
Watching

The Good Wife
```

Mosaic quietly shows:

- progress
- remaining episodes
- next unwatched episode
- related legal dramas
- cast information

No unrelated promotion exists.

The companion strengthens the current experience.

---

## Example 02

Current Context

```
Reading

Project Hail Mary
```

Mosaic quietly provides:

- reading progress
- chapter location
- audiobook availability
- author's previous novels

The software enriches the experience already taking place.

---

## Example 03

Current Context

```
Music Playing
```

The interface fades into the background.

Playback continues uninterrupted.

Only essential controls remain immediately visible.

The companion has completed its task.

---

# Poor Examples

## Promotional Behaviour

```
Trending Today

↓

Featured Releases

↓

Popular This Week

↓

Sponsored Content
```

The software has become the primary experience.

The companion has become a salesperson.

---

## Attention Seeking

Repeated:

- badges
- flashing indicators
- autoplay trailers
- unnecessary alerts

These behaviours interrupt rather than assist.

---

## Excessive Conversation

Every interaction generates:

- tips
- recommendations
- explanations
- onboarding
- encouragement

The companion has forgotten when to remain silent.

---

# Silence Is A Feature

One of the defining characteristics of a good companion is restraint.

Silence should be considered an intentional design decision.

Choosing **not** to interrupt is often the correct interaction.

The absence of unnecessary interface is therefore a positive outcome rather than missing functionality.

---

# The Periphery

Good companions remain at the edge of attention until needed.

They move naturally between:

Peripheral awareness

↓

Focused assistance

↓

Peripheral awareness

This mirrors one of the core ideas of Calm Technology, where technology should remain mostly in the user's periphery and move into focus only when required.  [oai_citation:1‡Wikipedia](https://en.wikipedia.org/wiki/Calm_technology?utm_source=chatgpt.com)

---

# Companion Across The Platform

This principle applies equally to:

- playback
- reading
- music
- search
- administration
- plugins

Administration should also behave like a companion.

Although more structured than entertainment experiences, it should remain calm, predictable and respectful of attention.

---

# Plugin Guidance

Extensions should strengthen the companion.

They should never replace it.

Plugins contribute:

- information
- capability
- knowledge

The platform determines:

- timing
- presentation
- emphasis
- interaction

This ensures users experience a single companion rather than multiple competing personalities.

---

# Review Questions

Before approving a proposal ask:

- Does this feel helpful?
- Does it interrupt unnecessarily?
- Would a trusted companion behave this way?
- Does this reduce uncertainty?
- Does the interface become quieter after completing its task?

If the proposal increases interaction without increasing understanding, it should be reconsidered.

---

# Litmus Test

Imagine sitting beside the user.

Would saying this aloud feel helpful...

...or annoying?

If it feels annoying in conversation...

It will almost certainly feel annoying in software.

---

# Summary

A companion is measured by trust.

Trust is earned through:

- consistency
- restraint
- understanding
- respect

Mosaic should quietly help people disappear into the worlds they love.

When it succeeds, users should remember the entertainment...

...not the software that helped them enjoy it.

---

# Related Specifications

- MDL-001 Vision
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model
- MDS-003 Composition Engine

---

# Architectural Decisions

| ADR | Decision |
|------|----------|
| ADR-023 | Mosaic adopts the companion as its primary behavioural metaphor. |
| ADR-024 | The interface should occupy attention only while providing value. |
| ADR-025 | Silence is considered a valid interaction outcome. |
| ADR-026 | Plugins extend the companion rather than creating independent personalities. |

---

# Review Status

**Status**

Draft

**Next File**

`10-when-principles-conflict.md`
