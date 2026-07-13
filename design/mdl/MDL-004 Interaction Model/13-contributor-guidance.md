<!--
File: design/mdl/MDL-004 Interaction Model/13-contributor-guidance.md
Document: MDL-004
Chapter: 13
Title: Contributor Guidance
Status: Draft
Version: 0.1
-->

# Contributor Guidance

---

# Purpose

The purpose of this chapter is to help contributors apply the Mosaic Interaction Model consistently.

Unlike the Mental Model, which explains **what exists**, the Interaction Model explains **how those concepts behave**.

Every contributor implementing behaviour should begin here before writing interface code.

Whether working on:

- backend services
- composition engines
- GraphQL
- Flutter
- HTMX
- web
- mobile
- television

the behavioural expectations remain identical.

---

# Design Behaviour First

One of the most common mistakes in software development is implementing interaction before understanding behaviour.

Poor process.

```
Button

↓

Click

↓

Animation

↓

Done
```

Preferred process.

```
User Intent

↓

Behaviour

↓

Composition

↓

Expression

↓

Presentation

↓

Implementation
```

Behaviour should always precede interface.

---

# Think In Behaviour

Avoid describing features using interface terminology.

Poor.

```
Open Details Page
```

Better.

```
Shift Focus
```

Poor.

```
Show Dialog
```

Better.

```
Request Confirmation
```

Poor.

```
Navigate Home
```

Better.

```
Return To Previous Context
```

Behaviour should describe the user's experience.

Not implementation.

---

# Preserve Continuity

Every contribution should preserve continuity.

Ask:

> If the user disappears for thirty seconds...

...will they still understand what happened when they return?

Good interactions preserve:

- Focus
- Context
- Progress
- Relationships
- Understanding

Poor interactions reset them.

---

# Design Around Intent

Every interaction begins with user intent.

Before implementation ask:

> What is the user trying to achieve?

Not:

> What interface should appear?

This distinction should influence:

- API design
- state management
- composition
- motion
- navigation

Intent always precedes implementation.

---

# Avoid Page Thinking

One of the easiest mistakes contributors can make is reverting to traditional page-based thinking.

Avoid asking:

- Which page?
- Which route?
- Which screen?

Instead ask:

- Which World?
- Which Focus?
- Which Context?
- Which Composition?

The interface should emerge naturally from those answers.

---

# Behaviour Is Shared

Interaction behaviour should remain consistent across every Mosaic client.

Desktop.

Television.

Mobile.

Tablet.

Future devices.

Presentation may differ.

Behaviour should not.

If contributors find themselves inventing different behavioural models for different clients, the implementation should be reconsidered.

---

# Think In Evolution

Whenever information changes, ask:

> How should the World evolve?

Not:

> Which interface should replace the current one?

Good behaviour evolves.

Poor behaviour replaces.

This distinction should become instinctive.

---

# Plugins

Plugin authors should never implement behavioural models.

Instead they contribute:

- Information
- Relationships
- Capability

The platform determines:

- Focus transitions
- Context transitions
- Composition evolution
- Movement
- Presentation

This separation allows every extension to feel native.

---

# Preserve Behavioural Identity

Before introducing any new interaction ask:

Does this interaction reinforce:

- continuity
- understanding
- companionship
- calmness

or merely introduce novelty?

Novel interaction should never become a goal in itself.

Understanding remains the objective.

---

# Common Mistakes

The following usually indicate contributors are bypassing the Interaction Model.

## Treating Navigation As Behaviour

Users care about changing intent.

Not routes.

---

## Behaviour Driven By Components

Components should communicate behaviour.

They should never define it.

---

## Behaviour Driven By Frameworks

Framework limitations should never redefine interaction.

Technology adapts to behaviour.

Behaviour does not adapt to technology.

---

## Plugin Behaviour

Plugins introducing:

- navigation
- custom interaction
- independent animation
- competing behavioural models

This fragments the product.

---

# Review Questions

Before implementation ask:

- Does this preserve continuity?
- Does this strengthen understanding?
- Does this reduce cognitive effort?
- Would users naturally predict this behaviour?
- Is the World evolving...
  or being replaced?
- Would this behaviour remain valid regardless of implementation technology?

If the answers remain unclear...

Return to the Interaction Model.

---

# Behaviour Checklist

Every substantial behavioural proposal should satisfy the following.

- [ ] User intent is understood.
- [ ] Focus behaves consistently.
- [ ] Context evolves naturally.
- [ ] Composition changes progressively.
- [ ] Continuity is preserved.
- [ ] Behaviour remains platform independent.
- [ ] Plugins participate without redefining interaction.
- [ ] Presentation communicates rather than invents behaviour.

---

# Final Guidance

Users should never think:

> "That interface changed."

They should instead think:

> "That makes sense."

If contributors consistently optimise for understanding rather than interface, Mosaic will gradually become easier to use without users ever consciously noticing why.

That is the ultimate objective of the Interaction Model.

---

# Review Status

**Status**

Draft

**Next File**

`glossary.md`
