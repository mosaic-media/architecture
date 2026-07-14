<!--
File: docs/design/system/mds-004-typography-system/13-contributor-guidance.md
Document: MDS-004
Chapter: 13
Title: Contributor Guidance
Status: Draft
Version: 0.1
-->

# Contributor Guidance

---

# Purpose

Typography is one of the few systems every Mosaic contributor will influence, whether intentionally or not.

Designers choose hierarchy.

Engineers implement typography.

Extension authors contribute language.

Writers define content.

The purpose of this guidance is to ensure every contributor strengthens one coherent editorial voice.

The user should always feel they are interacting with the same Companion.

---

# Think In Editorial Roles

Never begin with:

> "What font size should this use?"

Instead ask:

> **"What editorial role does this text perform?"**

Good.

```
Heading
```

Poor.

```
24px
```

Editorial meaning should always precede implementation.

---

# Write Before Styling

Typography exists to communicate language.

Good process.

```text
Meaning

↓

Language

↓

Editorial Role

↓

Typography

↓

Presentation
```

Poor process.

```text
Typography

↓

Visual Style

↓

Write Content
```

The words should determine the typography.

Never the reverse.

---

# One Editorial Voice

Every part of Mosaic should sound as though it comes from the same Companion.

Examples include:

- onboarding,
- playback,
- search,
- administration,
- settings,
- extensions.

Tone may adapt slightly.

Voice should remain consistent.

Users should never feel they have entered another application.

---

# Respect Reading Rhythm

Before introducing additional typography ask:

> Does this improve reading...

or simply add another label?

Typography should reduce effort.

Not increase it.

Whenever possible:

Remove words before reducing typography.

---

# Prefer Hierarchy Over Decoration

If emphasis is required:

Prefer:

- Composition
- spacing
- hierarchy
- editorial structure

before introducing:

- heavier weights,
- larger sizes,
- brighter colours.

Typography should communicate confidence through restraint.

---

# Components Consume Roles

Components should never request:

```
18px

Bold
```

Instead request:

```
Heading
```

or

```
Supporting
```

The Typography Resolver owns physical implementation.

Applications should remain implementation independent.

---

# Let Materials Speak

Typography exists inside Materials.

Do not attempt to compete with them.

Hero Material already communicates importance.

Typography should reinforce that importance.

Not duplicate it.

---

# Respect Accessibility

Whenever typography choices conflict with readability:

Readability wins.

Examples.

Poor.

```
Beautiful

↓

Unreadable
```

Preferred.

```
Readable

↓

Beautiful
```

Typography exists to communicate.

Everything else is secondary.

---

# Responsive Thinking

Avoid asking:

> "How does this shrink?"

Instead ask:

> "How should this read on another device?"

The editorial role should remain identical.

Only the implementation changes.

---

# Variable Fonts

Contributors should never manipulate:

- weight,
- optical size,
- width,
- grade

directly.

Applications request editorial roles.

The Typography Resolver determines appropriate variable font behaviour.

---

# Extensions

Extensions should contribute:

- titles,
- descriptions,
- metadata,
- editorial content.

They should never define:

- font families,
- scales,
- hierarchy,
- spacing.

The platform owns typography.

Extensions inherit it.

---

# Language

Typography cannot compensate for poor writing.

Before adjusting typography ask:

> Can the text itself become clearer?

Simple language usually improves understanding more than visual refinement.

Good typography amplifies good writing.

It rarely rescues poor writing.

---

# Common Mistakes

Avoid the following.

### Pixel Thinking

Choosing typography using measurements rather than editorial roles.

---

### Marketing Language

Every heading sounding promotional.

---

### Decorative Hierarchy

Typography competing with entertainment.

---

### Platform Typography

Each client inventing independent editorial behaviour.

---

### Component Fonts

Components selecting their own typography.

---

### Dense Interfaces

Reducing text size instead of improving Composition.

---

# Typography Review Questions

Before implementing typography ask:

- What editorial role does this perform?
- Does it strengthen reading rhythm?
- Does it reinforce Composition?
- Will it remain understandable without colour?
- Would this still feel like Mosaic after a redesign?
- Does it sound like the Companion?

If uncertainty remains...

Return to the editorial hierarchy before implementation.

---

# Typography Checklist

Every typography implementation should satisfy the following.

- [ ] Editorial role is clearly defined.
- [ ] Reading rhythm is preserved.
- [ ] Accessibility is maintained.
- [ ] Responsive behaviour is supported.
- [ ] Components consume editorial roles.
- [ ] Runtime Typography Resolver owns implementation.
- [ ] Platform independence is preserved.
- [ ] Typography supports rather than competes with entertainment.

---

# Final Guidance

The Typography System should eventually disappear from conscious thought.

Contributors should stop asking:

> "What font should this use?"

and instinctively begin asking:

> **"How should the Companion say this?"**

When every contributor naturally thinks in editorial language rather than typography, the system has achieved its purpose.

Readers will simply experience calm, confident understanding.

That is the ultimate objective of the Mosaic Typography System.

---

# Review Status

**Status**

Draft

**Next File**

`glossary.md`
