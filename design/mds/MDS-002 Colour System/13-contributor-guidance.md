<!--
File: design/mds/MDS-002 Colour System/13-contributor-guidance.md
Document: MDS-002
Chapter: 13
Title: Contributor Guidance
Status: Draft
Version: 0.1
-->

# Contributor Guidance

---

# Purpose

The Colour System is one of the most frequently consumed parts of the Mosaic Design System.

Every contributor, regardless of discipline, will eventually make colour-related decisions.

This chapter provides practical guidance for ensuring those decisions reinforce the architectural principles established throughout MDL and MDS.

The objective is not to make contributors think about colours.

It is to make them think about meaning.

---

# Think In Meaning

Before selecting any colour ask:

> **What does this colour need to communicate?**

Never begin with:

- cyan
- purple
- blue
- grey

Instead begin with:

- Hero
- Action
- Surface
- Status
- Atmosphere

Meaning always precedes colour.

---

# Consume Semantic Colours

Applications should almost never consume Primitive Colours directly.

Preferred.

```text
Action.Primary
```

Avoid.

```text
Primitive.Colour.Cyan.500
```

The Semantic layer protects applications from future redesigns.

Always consume the highest semantic layer available.

---

# Let Atmosphere Do Its Job

Contributors should never manually tint components to match artwork.

Incorrect.

```text
Poster

↓

Tint Button
```

Preferred.

```text
Poster

↓

Runtime Atmosphere

↓

Material

↓

Button
```

The Colour System already understands how atmosphere should propagate.

Application code should not duplicate that logic.

---

# Preserve The Brand

Brand colours should be treated with restraint.

Ask:

> **Is this communicating Mosaic...**

or...

> **Is this merely decorating the interface?**

If the answer is decoration...

The Brand Colour probably does not belong there.

Brand gains strength through consistency rather than frequency.

---

# Think In Atmosphere

Artwork should influence mood.

Not identity.

Good question.

> **What kind of light would this artwork cast into the room?**

Poor question.

> **What colour should this interface become?**

The first produces Mosaic.

The second produces theme replacement.

---

# Accessibility First

Whenever colour decisions conflict with readability:

Accessibility wins.

Always.

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

A visually impressive interface that weakens understanding is considered a design failure.

---

# Avoid Component Colours

Components should never invent colours.

Example.

Poor.

```text
Button

↓

Choose Blue
```

Preferred.

```text
Button

↓

Action.Primary
```

The Design System owns colour.

Components communicate behaviour.

---

# Runtime Is Platform-Owned

Applications and extensions should never:

- analyse artwork
- generate atmosphere
- resolve palettes
- blend themes

These responsibilities belong exclusively to the Runtime Colour System.

The platform guarantees consistency.

Applications simply consume the results.

---

# Extensions

Extension authors should consume:

- Semantic Colours
- Runtime Tokens
- Composition Tokens

They should never introduce:

- brand palettes
- custom themes
- independent atmosphere
- alternative semantic colours

The extension should disappear into Mosaic rather than advertising itself.

---

# Think About Light

One useful mental model for contributors is to imagine that colour represents light rather than paint.

Brand.

↓

Identity.

Atmosphere.

↓

Environmental light.

Materials.

↓

Physical response.

Components.

↓

Objects inside that environment.

Thinking this way naturally produces calmer interfaces.

---

# Common Mistakes

Avoid the following.

### Primitive Consumption

Directly consuming raw colour values.

---

### Artwork Sampling

Applying extracted colours directly to components.

---

### Brand Saturation

Using Brand Colours everywhere.

---

### Decorative Colour

Adding colour because empty space feels uncomfortable.

---

### Theme Logic

Embedding Light/Dark decisions directly into application code.

The Theme Resolver already owns those responsibilities.

---

### Accessibility Overrides

Reducing readability for stronger atmosphere.

Accessibility always possesses higher authority.

---

# Colour Review Questions

Before implementing any colour-related change ask:

- What meaning does this colour communicate?
- Could an existing Semantic Colour already solve this?
- Does Runtime already provide this behaviour?
- Will this remain meaningful after a redesign?
- Does this strengthen understanding?
- Does this compete with the entertainment?

If uncertainty remains...

The colour decision probably belongs inside the Design System rather than application code.

---

# Colour Checklist

Every colour implementation should satisfy the following.

- [ ] Uses Semantic Colours rather than Primitive values.
- [ ] Preserves accessibility.
- [ ] Supports Runtime Atmosphere.
- [ ] Preserves Brand identity.
- [ ] Avoids component-specific colour logic.
- [ ] Remains implementation independent.
- [ ] Works across Light and Dark themes.
- [ ] Supports future runtime adaptation.

---

# Final Guidance

The strongest Colour System is one contributors eventually stop thinking about.

Instead of asking:

> "Which colour should this be?"

contributors should instinctively ask:

> "What does this need to communicate?"

When that question becomes habitual, implementation naturally begins to align with the Mosaic Design Language.

The Colour System then ceases to be a palette.

It becomes a language.

---

# Review Status

**Status**

Draft

**Next File**

`glossary.md`
