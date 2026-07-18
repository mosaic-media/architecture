<!--
File: docs/design/language/mdl-005-composition-model/09-composition-solving.md
Document: MDL-005
Status: Draft
-->

# Composition Solving

---

# Purpose

Previous chapters defined what a Composition is and how it should behave.

This chapter introduces one of the most important concepts within the Mosaic Design Language.

The **Composition Solver**.

Unlike traditional layout engines, the Composition Solver does not solve geometry.

It solves understanding.

Its responsibility is to determine the best possible Composition for the user's current World before any visual layout occurs.

This chapter represents the conceptual foundation for the future **MDS Composition Engine**.

---

# Definition

Within MDL, **Composition Solving** is defined as:

> **The process of determining the optimal organisation of understanding for the user's current World.**

The Composition Solver answers one question.

> **Given everything we currently know, what should the user understand first?**

---

# Why A Solver Exists

Traditional interfaces frequently rely upon manually authored layouts.

Examples.

```mermaid
flowchart TD

N1["Home"]
N2["Fixed Sections"]
N3["Render"]

N1 --> N2
N2 --> N3
```

or

```mermaid
flowchart TD

N1["Screen"]
N2["Grid"]
N3["Populate Widgets"]

N1 --> N2
N2 --> N3
```

These systems assume every user requires the same organisation.

Mosaic intentionally rejects this assumption.

Every World is different.

Every Focus is different.

Every Context is different.

The Composition should therefore be solved.

Not hardcoded.

---

# Solving Understanding

The Composition Solver is **not** a layout algorithm.

It never asks:

- Which row?
- Which column?
- Which pixel?

Instead it asks:

- What matters?
- Why?
- What supports it?
- What can wait?
- What should disappear?

The output is understanding.

Presentation is solved afterwards.

---

# Inputs

The Composition Solver receives conceptual inputs.

```mermaid
flowchart TD

N1["World"]
N2["Focus"]
N3["Context"]
N4["Information"]
N5["Relationships"]
N6["Priority"]
N7["Available Capabilities"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Notice that layout information is intentionally absent.

The solver operates entirely within the conceptual domain.

---

# Outputs

The Composition Solver produces:

- Hero
- Hierarchy
- Priority Ordering
- Groupings
- Adaptive Density
- Expressions
- Behavioural Intent

These outputs are consumed later by the Design System.

The solver never creates interface directly.

---

# Solving Order

Every Composition should be solved using the same conceptual sequence.

```mermaid
flowchart TD

N1["1.<br/>Current World"]
N2["2.<br/>Current Focus"]
N3["3.<br/>Current Context"]
N4["4.<br/>Relevant Information"]
N5["5.<br/>Relationships"]
N6["6.<br/>Priority"]
N7["7.<br/>Composition"]
N8["8.<br/>Expressions"]
N9["9.<br/>Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
N8 --> N9
```

Skipping stages weakens understanding.

---

# The Solver Never Guesses

The Composition Solver should never invent understanding.

It should only organise understanding that already exists.

Poor.

```

Maybe this is important.
```

Preferred.

```

Current Context indicates this is important.
```

Understanding should emerge from evidence.

Not assumption.

---

# Solving Is Deterministic

Given identical inputs...

The Composition Solver should always produce the same conceptual output.

Example.

```mermaid
flowchart TD

N1["World"]
N2["Frieren"]
N3["Watching"]
N4["Episode 15"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Every client should produce the same Composition.

Presentation may differ.

Understanding must remain identical.

This deterministic behaviour is fundamental to preserving the Mosaic Mental Model across platforms.

---

# Solving Priority

Priority should be determined before solving Composition.

Example.

```mermaid
flowchart TD

N1["Episode<br/>High"]
N2["Timeline<br/>Medium"]
N3["Reviews<br/>Low"]

N1 --> N2
N2 --> N3
```

The solver should never determine Priority.

Priority is an input.

Composition is the result.

---

# Solving Relationships

Relationships significantly influence Composition.

Example.

```mermaid
flowchart TD

N1["Episode"]
N2["Manga"]
N3["Author"]
N4["Next Episode"]

N1 --> N2
N2 --> N3
N3 --> N4
```

These relationships naturally suggest:

```mermaid
flowchart TD

N1["Continue"]
N2["Timeline"]
N3["Related Works"]

N1 --> N2
N2 --> N3
```

The solver should therefore prefer meaningful relationships over arbitrary ordering.

---

# Solving For Intent

The Composition Solver should optimise the user's current intent.

Example.

Intent.

```

Continue Watching
```

Preferred Composition.

```mermaid
flowchart TD

N1["Playback"]
N2["Progress"]
N3["Next Episode"]

N1 --> N2
N2 --> N3
```

Not.

```mermaid
flowchart TD

N1["Trending"]
N2["Collections"]
N3["Statistics"]

N1 --> N2
N2 --> N3
```

Intent always possesses higher authority than inventory.

---

# Solving Across Devices

The Composition Solver should remain device independent.

Desktop.

```mermaid
flowchart TD

N1["Composition"]
N2["Desktop Presentation"]

N1 --> N2
```

Phone.

```mermaid
flowchart TD

N1["Composition"]
N2["Phone Presentation"]

N1 --> N2
```

Television.

```mermaid
flowchart TD

N1["Composition"]
N2["TV Presentation"]

N1 --> N2
```

The solved understanding remains identical.

Only the presentation changes.

---

# Solving With Modules

Modules should never influence the solving process directly.

Modules contribute:

- Information
- Relationships

The platform determines:

- Priority
- Hierarchy
- Hero
- Expressions

This preserves one coherent behavioural language.

Modules strengthen the World.

They do not redesign it.

---

# Failure Conditions

A Composition should be considered unsolved when:

- multiple Heroes compete
- hierarchy is unclear
- unrelated information dominates
- understanding depends upon presentation
- users must consciously search for what matters

The solver has failed if users ask:

> "Where should I look?"

---

# Good Examples

## Watching

Inputs.

```mermaid
flowchart TD

N1["Current Episode"]
N2["Progress"]
N3["Next Episode"]
N4["Cast"]
N5["Reviews"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Solved Composition.

```mermaid
flowchart TD

N1["Hero"]
N2["Progress"]
N3["Timeline"]
N4["Relationships"]
N5["Metadata"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Understanding emerges naturally.

---

## Reading

Inputs.

```mermaid
flowchart TD

N1["Current Chapter"]
N2["Bookmarks"]
N3["Series"]
N4["Author"]
N5["Statistics"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Solved Composition.

```mermaid
flowchart TD

N1["Hero"]
N2["Reading Progress"]
N3["Bookmarks"]
N4["Series"]
N5["Statistics"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Again...

Understanding leads.

---

# Anti-patterns

## Layout Solving

Choosing positions before determining importance.

---

## Component Solving

Thinking in:

- cards
- shelves
- widgets

instead of understanding.

---

## Responsive Solving

Changing hierarchy because screen size changed.

Meaning should remain constant.

Only expression adapts.

---

## Module Solving

Modules determining:

- Hero
- Priority
- Hierarchy

The platform loses ownership of understanding.

---

# Conceptual Solver

```mermaid
flowchart TD

World
World --> Focus
Focus --> Context
Context --> Information
Information --> Relationships
Relationships --> Priority
Priority --> CompositionSolver["Composition Solver"]
CompositionSolver["Composition Solver"] --> Expressions
Expressions --> Presentation
```

The Composition Solver exists entirely before presentation.

Its output is understanding.

Not interface.

---

# Relationship To MDS

This chapter intentionally avoids implementation.

The future **MDS Composition Engine** will define:

- algorithms
- heuristics
- runtime solving
- optimisation
- caching
- adaptive rendering

MDL defines only the conceptual expectations.

MDS defines the implementation.

---

# Summary

Composition Solving is one of the defining architectural ideas of Mosaic.

Instead of manually arranging interface...

Mosaic first solves understanding.

Everything else becomes a consequence of that decision.

Users should therefore experience interfaces that feel naturally organised around their current World rather than manually designed around arbitrary layouts.
