<!--
File: docs/engineering/architecture/mdp-002-tile-framework/03-expression-mapping.md
Document: MDP-002
Status: Deferred
-->

# Expression Mapping

> **Proposal status:** Deferred and non-authoritative. This chapter preserves post-v1 research; it is not a Mosaic v1 requirement.

---

# Purpose

The Composition Engine produces Expressions.

The Tile Framework produces Tiles.

This chapter defines the deterministic process that connects the two.

Expression Mapping is intentionally one of the strongest architectural boundaries within Mosaic.

Expressions communicate understanding.

Tiles communicate presentation.

Neither system should know implementation details belonging to the other.

---

# Definition

Within MDS, **Expression Mapping** is defined as:

> **The deterministic process through which solved runtime Expressions are transformed into appropriate Tile identities while preserving behavioural meaning.**

Expression Mapping communicates presentation intent.

It does not perform rendering.

---

# Why Mapping Exists

Without Expression Mapping, rendering systems would need to understand runtime concepts directly.

Example.

```mermaid
flowchart TD

N1["Playback"]
N2["Widgets"]

N1 --> N2
```

This tightly couples behaviour to implementation.

Instead.

```mermaid
flowchart TD

N1["Playback"]
N2["Expressions"]
N3["Tiles"]
N4["Components"]
N5["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every layer owns one responsibility.

---

# One Expression

Every Expression should normally resolve to one primary Tile.

Example.

```mermaid
flowchart TD

N1["Hero"]
N2["Hero Tile"]

N1 --> N2
```

The Tile may later be implemented differently.

Its behavioural identity remains unchanged.

---

# Behaviour Before Mapping

Mapping should always begin from behavioural meaning.

Incorrect.

```mermaid
flowchart TD

N1["Poster"]
N2["Poster Card"]

N1 --> N2
```

Correct.

```mermaid
flowchart TD

N1["Hero Expression"]
N2["Hero Tile"]

N1 --> N2
```

Presentation follows behaviour.

Never the reverse.

---

# Deterministic Mapping

Given identical:

- Runtime World
- Expressions
- Behaviour
- Context

Expression Mapping should always produce identical Tile identities.

This determinism enables:

- caching
- testing
- replay
- cross-platform consistency

---

# Mapping Inputs

Expression Mapping evaluates:

```mermaid
flowchart TD

N1["Expression"]
N2["Runtime Hierarchy"]
N3["Behaviour"]
N4["Context"]
N5["Device Capability"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Rendering technology is intentionally absent.

Tiles remain implementation independent.

---

# Mapping Outputs

The Mapping stage produces:

```mermaid
flowchart TD

N1["Tile Identity"]
N2["Material Intent"]
N3["Typography Intent"]
N4["Motion Intent"]
N5["Interaction Intent"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Component Library later consumes these outputs.

---

# Hero Mapping

Example.

```mermaid
flowchart TD

N1["Hero Expression"]
N2["Hero Tile"]

N1 --> N2
```

The Hero Tile inherits:

- Hero Material
- Hero Typography
- Hero Motion

The renderer later decides how this appears physically.

---

# Timeline Mapping

Example.

```mermaid
flowchart TD

N1["Timeline Expression"]
N2["Timeline Tile"]

N1 --> N2
```

Timeline Tiles inherit:

- Supporting Motion
- Acrylic Material
- Supporting Typography

The behavioural role remains identical across every platform.

---

# Relationship Mapping

Example.

```mermaid
flowchart TD

N1["Relationship Expression"]
N2["Relationship Tile"]

N1 --> N2
```

Relationship Tiles communicate:

- recommendations
- cast
- author
- franchise

without introducing domain-specific presentation.

---

# Action Mapping

Example.

```mermaid
flowchart TD

N1["Resume Expression"]
N2["Action Tile"]

N1 --> N2
```

The Tile communicates behavioural opportunity.

Not button implementation.

Buttons remain platform components.

---

# Metadata Mapping

Example.

```mermaid
flowchart TD

N1["Metadata Expression"]
N2["Metadata Tile"]

N1 --> N2
```

Metadata remains:

- supporting,
- editorial,
- behaviourally quiet.

It should never unexpectedly become primary because of implementation choices.

---

# Runtime Hierarchy

Runtime Hierarchy may influence Tile behaviour.

Example.

```mermaid
flowchart TD

N1["Content Expression"]
N2["Hero"]
N3["Hero Tile"]

N1 --> N2
N2 --> N3
```

The Expression remains:

```

Content
```

Its runtime role changes.

Mapping respects that role.

---

# Device Adaptation

Different devices may receive different Tile variants.

Desktop.

↓

Expanded Hero Tile.

Phone.

↓

Compact Hero Tile.

Voice.

↓

Spoken Hero Tile.

These remain behavioural variants of one Tile identity.

The mapping remains conceptually identical.

---

# Material Intent

Expression Mapping also assigns Material Intent.

Example.

```mermaid
flowchart TD

N1["Overlay Expression"]
N2["Overlay Tile"]
N3["Overlay Material"]

N1 --> N2
N2 --> N3
```

Rendering systems remain unaware of behavioural reasoning.

They simply receive Tile metadata.

---

# Typography Intent

Expressions also inherit editorial behaviour.

Example.

```mermaid
flowchart TD

N1["Hero"]
N2["Hero Tile"]
N3["Heading"]

N1 --> N2
N2 --> N3
```

```mermaid
flowchart TD

N1["Metadata"]
N2["Metadata Tile"]
N3["Supporting"]

N1 --> N2
N2 --> N3
```

Typography therefore becomes another consequence of behavioural mapping.

---

# Motion Intent

Motion also follows Tile identity.

Example.

Hero Tile.

↓

Hero Motion.

Timeline Tile.

↓

Supporting Motion.

Overlay Tile.

↓

Overlay Motion.

Movement therefore remains behaviourally consistent without components defining transitions independently.

---

# Interaction Intent

Tiles also communicate interaction.

Examples.

```mermaid
flowchart TD

N1["Hero Tile"]
N2["Primary Interaction"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Relationship Tile"]
N2["Exploration"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Metadata Tile"]
N2["Passive"]

N1 --> N2
```

Interaction therefore emerges naturally from behavioural understanding.

---

# Incremental Mapping

Expression Mapping should update incrementally.

Example.

Playback progress.

↓

Timeline Tile updates.

Hero Tile unchanged.

Only affected mappings should recompute.

This preserves runtime efficiency and behavioural continuity.

---

# Modules

Modules contribute:

- Expressions,
- information,
- relationships.

Modules never perform mapping.

The Tile Framework owns:

- Tile identity,
- Material intent,
- Motion intent,
- Typography intent.

Every module therefore automatically inherits future presentation improvements.

---

# Good Examples

## Playback

Expression.

↓

Timeline.

↓

Timeline Tile.

↓

Platform Component.

Behaviour remains intact.

---

## Reading

Expression.

↓

Bookmarks.

↓

Relationship Tile.

↓

Presentation.

The runtime vocabulary remains consistent.

---

## Music

Expression.

↓

Current Track.

↓

Hero Tile.

↓

Presentation.

Behaviour determines presentation.

---

# Anti-patterns

## Widget Mapping

Expressions directly selecting components.

---

## Platform Mapping

Different platforms inventing different Tile identities.

---

## Module Mapping

Modules deciding presentation.

---

## Domain Mapping

Creating Film Tiles, Anime Tiles or Book Tiles.

Behaviour should remain media independent.

---

# Expression Mapping Model

```mermaid
flowchart TD

Expression
Expression --> RuntimeHierarchy
RuntimeHierarchy --> ExpressionMapping
ExpressionMapping --> TileIdentity
TileIdentity --> MaterialIntent
MaterialIntent --> TypographyIntent
TypographyIntent --> MotionIntent
MotionIntent --> Component
```

Expressions determine Tiles.

Tiles determine presentation.

Components remain implementation.

---

# Relationship To Future Chapters

The next chapter defines **Tile Lifecycle**.

Expression Mapping explains:

> **How Expressions become Tiles.**

Tile Lifecycle explains:

> **How those Tiles evolve over time while preserving behavioural continuity.**

Together they establish the runtime life of every presentation primitive within Mosaic.

---

# Summary

Expression Mapping is one of the most important abstraction boundaries within the Mosaic architecture.

It ensures that:

- runtime behaviour remains independent,
- presentation remains reusable,
- rendering remains replaceable.

Expressions describe understanding.

Tiles describe presentation.

Components simply render the result.
