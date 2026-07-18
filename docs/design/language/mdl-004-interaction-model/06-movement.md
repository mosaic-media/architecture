<!--
File: docs/design/language/mdl-004-interaction-model/06-movement.md
Document: MDL-004
Status: Draft
-->

# Movement

---

# Purpose

Movement is the physical manifestation of behavioural change.

It exists to communicate the evolution of the user's World.

Within the Mosaic Design Language, movement is not decoration.

It is explanation.

If Composition determines **what changed**, movement communicates **how that change occurred**.

---

# Definition

Within MDL, **Movement** is defined as:

> **The visual communication of behavioural change while preserving the user's understanding of their World.**

Movement is a communication system.

It is not an animation system.

Animation is an implementation.

Movement is intent.

---

# Why Movement Exists

Every interaction changes something.

Examples include:

- Focus changes
- Context changes
- Relationships become important
- Information becomes available
- Composition evolves

Without movement the interface appears to change instantaneously.

Users must reconstruct understanding from scratch.

Movement preserves continuity by explaining:

- what changed
- where it changed
- why it changed

---

# Behaviour Before Motion

Movement should always communicate behaviour that already exists.

Incorrect process.

```mermaid
flowchart TD

N1["Animation"]
N2["Behaviour"]

N1 --> N2
```

Correct process.

```mermaid
flowchart TD

N1["Behaviour"]
N2["Movement"]
N3["Animation"]

N1 --> N2
N2 --> N3
```

Animation implements movement.

Movement implements behaviour.

Behaviour implements the Mental Model.

---

# The Purpose Of Movement

Movement exists for four reasons.

## Preserve Continuity

Users should understand where things came from.

---

## Explain Change

Users should understand why something changed.

---

## Reinforce Hierarchy

Important changes deserve greater emphasis than insignificant ones.

---

## Reduce Cognitive Effort

Movement should reduce interpretation rather than increase it.

---

# Movement Is Directional

Movement should always possess direction.

Direction communicates relationship.

Examples.

```mermaid
flowchart TD

N1["Focus"]
N2["Expands"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Supporting Information"]
N2["Moves Aside"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Completed Information"]
N2["Leaves Composition"]

N1 --> N2
```

Direction provides meaning.

Random movement provides none.

---

# Movement Is Intentional

Every visible movement should answer a question.

Examples.

Question.

```

Why did this move?
```

Answer.

```

Focus changed.
```

Question.

```

Why did this disappear?
```

Answer.

```

It is no longer relevant.
```

Question.

```

Why did this appear?
```

Answer.

```

New information became important.
```

If no meaningful answer exists...

The movement should not exist.

---

# Conceptual Weight

Movement should reflect conceptual weight rather than visual distance.

Example.

```mermaid
flowchart TD

N1["Episode 14"]
N2["Episode 15"]

N1 --> N2
```

Small conceptual change.

Small movement.

---

Example.

```mermaid
flowchart TD

N1["Anime"]
N2["Books"]

N1 --> N2
```

Large conceptual change.

Larger movement.

---

Example.

```mermaid
flowchart TD

N1["Playback"]
N2["Administration"]

N1 --> N2
```

Very large conceptual change.

The platform should clearly communicate that the user has entered a fundamentally different mode.

---

# Stable Objects

Objects should preserve identity wherever practical.

Users should recognise:

```mermaid
flowchart TD

N1["Current Progress"]
N2["Current Progress"]

N1 --> N2
```

rather than

```mermaid
flowchart TD

N1["Old Progress"]
N2["Destroyed"]
N3["New Progress"]

N1 --> N2
N2 --> N3
```

The object remains.

Only its state changes.

This greatly improves long-term learnability.

---

# Local Movement

Movement should normally remain local.

Changing:

```

Progress
```

should not cause:

- Search
- Navigation
- Hero
- Timeline

to animate unnecessarily.

Only objects participating in the behavioural change should move.

Local movement reduces visual noise.

---

# Hierarchical Movement

Movement should follow hierarchy.

Examples.

Primary Focus moves first.

Supporting information follows.

Background information moves last.

This naturally reinforces importance without additional interface elements.

---

# Arrival

New information should arrive naturally.

Poor.

```mermaid
flowchart TD

N1["Information"]
N2["Instantly Appears"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Information Becomes Relevant"]
N2["Composition Creates Space"]
N3["Information Joins"]

N1 --> N2
N2 --> N3
```

Users should understand why something has entered their World.

---

# Departure

Likewise...

Information should leave naturally.

Poor.

```mermaid
flowchart TD

N1["Information"]
N2["Disappears"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Information Becomes Less Relevant"]
N2["Priority Reduces"]
N3["Leaves Composition"]

N1 --> N2
N2 --> N3
```

Departure should feel like completion.

Not deletion.

---

# Movement And Time

Movement should communicate temporal progression.

Examples.

```mermaid
flowchart TD

N1["Watching"]
N2["Completed"]
N3["Continue"]
N4["Next Episode"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The interface should communicate that one experience has naturally progressed into another.

Users should never feel abruptly returned to the beginning.

---

# Module Behaviour

Modules never define movement.

Modules contribute:

- Information
- Relationships

The platform determines:

- arrival
- departure
- emphasis
- continuity

This ensures one coherent behavioural language regardless of installed modules.

---

# Good Examples

## Example 01

Episode completes.

Progress fills.

Timeline advances.

Next episode gains emphasis.

Playback controls reduce.

The World continues.

---

## Example 02

User opens Cast.

Character information expands naturally around the current Focus.

Playback remains recognisable.

The user understands they are exploring rather than navigating away.

---

## Example 03

New episode releases overnight.

The next morning.

Timeline quietly gains emphasis.

Nothing else unnecessarily changes.

The World has evolved.

---

# Anti-patterns

## Decorative Motion

Movement exists because it looks impressive.

Understanding does not improve.

---

## Teleportation

Objects disappear.

New objects appear elsewhere.

Identity is lost.

---

## Simultaneous Motion

Everything moves together.

Hierarchy disappears.

Users no longer know where to look.

---

## Performance Before Understanding

Movement is removed simply because it is technically expensive.

Understanding decreases.

Optimisation should preserve behavioural meaning wherever possible.

---

# Behavioural Model

```mermaid
flowchart TD

Behaviour
Behaviour --> Meaning
Meaning --> Movement
Movement --> Animation
Animation --> Presentation
```

Animation is the final implementation detail.

Behaviour always remains the primary concern.

---

# Summary

Movement is the behavioural language of Mosaic.

It communicates:

- continuity
- hierarchy
- evolution
- understanding

Movement should never exist because animation is possible.

It exists because users deserve to understand how their World has changed.
