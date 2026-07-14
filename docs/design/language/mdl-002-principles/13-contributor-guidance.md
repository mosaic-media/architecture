<!--
File: docs/design/language/mdl-002-principles/13-contributor-guidance.md
Document: MDL-002
Chapter: 13
Title: Contributor Guidance
Status: Draft
Version: 0.1
-->

# Contributor Guidance

---

# Purpose

The purpose of this chapter is to help every contributor apply the Mosaic Design Language consistently.

MDL exists to produce coherent decisions across many contributors working independently.

A contributor should not need to ask:

> "What would the original designers have done?"

Instead they should be able to read MDL and arrive at similar conclusions through shared reasoning.

The objective of this guidance is not to limit creativity.

It is to focus creativity on solving user problems rather than inventing new interaction models.

---

# Every Contribution Is A Design Decision

Design is not limited to visual interfaces.

Every pull request changes the user experience.

Examples include:

- GraphQL schemas
- plugin APIs
- database models
- navigation
- loading behaviour
- animation
- accessibility
- terminology

Every contributor therefore participates in the design language.

---

# Design Before Implementation

Contributors should avoid beginning implementation immediately after identifying a problem.

Instead they should first ask:

1. What problem exists?
2. Why does it exist?
3. Which MDL principles apply?
4. Does an existing system already solve this?
5. What is the simplest solution?

Implementation should be the final stage of the process.

Not the first.

---

# The Companion Test

Whenever uncertainty exists, imagine Mosaic as a trusted companion sitting beside the user.

Ask:

> Would the companion behave like this?

Examples.

## Good

"You stopped halfway through this chapter."

"Would you like to continue?"

---

## Good

"The next episode airs tomorrow."

---

## Poor

"Trending Now!"

---

## Poor

"People are watching this instead."

The companion helps.

It does not compete.

---

# Build Systems

Contributors should favour extending systems over creating isolated features.

Prefer:

```
Progress System

↓

Audiobook Progress

↓

Book Progress

↓

Episode Progress
```

Instead of:

```
Book Progress Widget

Movie Progress Widget

Anime Progress Widget

Music Progress Widget
```

The first creates one evolving system.

The second creates four independent implementations.

---

# Respect Existing Concepts

Before introducing:

- new terminology
- new interaction
- new component
- new motion
- new pattern

Contributors should determine whether an existing concept already satisfies the requirement.

Examples.

Instead of introducing:

```
Media Card
```

Can the existing Tile evolve?

Instead of introducing:

```
Recommendation Panel
```

Can the existing Composition model solve the problem?

Every unnecessary concept increases long-term cognitive complexity.

---

# Design For The Next Contributor

A contribution is considered complete only when another contributor can understand why it exists.

Whenever possible include:

- rationale
- references
- ADR links
- specification references

Future maintainability is considered part of implementation quality.

---

# Extension Authors

Extension authors should think in terms of capability.

Not interface.

Good contribution:

```
Information

↓

Relationships

↓

Capability
```

Poor contribution:

```
Custom HTML

↓

Custom CSS

↓

Custom Layout
```

The extension should enrich Mosaic.

It should never fragment it.

---

# Challenge The Right Thing

Contributors are encouraged to challenge:

- implementations
- interactions
- patterns
- systems

They should challenge principles only with evidence.

Principles represent accumulated product knowledge.

Changing one should be treated as a significant architectural event.

---

# Simplicity

Whenever two solutions appear equally valid, prefer the one that:

- introduces fewer concepts
- requires fewer explanations
- produces fewer exceptions
- strengthens existing systems

Simplicity is not measured by lines of code.

It is measured by the amount of understanding required from users.

---

# Design Reviews

Every substantial contribution should identify:

- relevant MDL principle(s)
- relevant ADR(s)
- affected specifications

Example.

```
Supports

P-01 Context Before Prediction

P-03 Content Leads

ADR-042

ADR-046
```

This creates traceability between implementation and philosophy.

---

# What Success Looks Like

A successful contributor should eventually stop consciously applying MDL.

Instead, the principles become part of how they naturally reason about design.

When multiple contributors independently produce experiences that feel unmistakably Mosaic...

MDL has succeeded.

---

# Common Mistakes

Avoid:

- solving implementation before understanding the problem
- introducing special cases
- inventing new terminology unnecessarily
- creating one-off components
- exposing implementation details
- designing around frameworks rather than people

These mistakes create long-term design debt.

---

# Final Guidance

If only one sentence from this chapter is remembered, it should be this:

> **Build systems that quietly help people enjoy entertainment, not interfaces that ask people to admire software.**

Everything else within MDL exists to support that goal.

---

# Review Status

**Status**

Draft

**Next File**

`14-design-review-checklist.md`
