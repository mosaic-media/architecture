<!--
File: docs/design/language/mdl-003-mental-model/06-relationships.md
Document: MDL-003
Status: Draft
-->

# Relationships

---

# Purpose

Information, by itself, is useful.

Relationships transform information into understanding.

This chapter introduces one of the most important concepts within the Mosaic Mental Model.

Without relationships, Mosaic becomes a searchable database.

With relationships, Mosaic becomes an entertainment companion.

Relationships explain **why** pieces of information matter together.

---

# Definition

Within MDL, a **Relationship** is defined as:

> **A meaningful connection between two or more pieces of information.**

Relationships create context.

Relationships create understanding.

Relationships create discovery.

Information provides facts.

Relationships provide meaning.

---

# Why Relationships Exist

People rarely experience entertainment as isolated media.

Instead they naturally connect experiences.

Examples include:

> "That actor was also in..."

> "This anime was adapted from..."

> "The composer also wrote..."

> "The next book continues..."

These connections are not interface features.

They are relationships that already exist.

Mosaic's responsibility is to reveal them naturally.

---

# Relationships Before Navigation

Traditional applications encourage navigation.

```mermaid
flowchart TD

N1["Movie"]
N2["Actor Page"]
N3["Filmography"]
N4["Another Movie"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Every step requires navigation.

Mosaic instead understands the relationship directly.

```mermaid
flowchart TD

N1["Movie"]
N2["Actor"]
N3["Related Works"]

N1 --> N2
N2 --> N3
```

The interface simply reveals that relationship.

The user explores naturally rather than navigating mechanically.

---

# Types Of Relationships

Relationships exist at many levels.

## Sequential

Describes progression.

Examples include:

- next episode
- previous episode
- next chapter
- sequel
- chronological order

---

## Structural

Describes ownership or composition.

Examples include:

- season belongs to series
- episode belongs to season
- chapter belongs to book
- track belongs to album

---

## Creative

Describes people and production.

Examples include:

- actor
- director
- composer
- author
- illustrator
- studio

---

## Narrative

Describes fictional connections.

Examples include:

- spin-off
- adaptation
- prequel
- alternate timeline
- shared universe

---

## Personal

Describes relationships to the user.

Examples include:

- currently watching
- completed
- bookmarked
- favourite
- continue reading

These relationships are unique to each World.

---

# Relationships Are First-Class Concepts

A common mistake is treating relationships as metadata.

Within MDL they are significantly more important.

Metadata describes objects.

Relationships describe worlds.

Consider:

```mermaid
flowchart TD

N1["Frieren"]
N2["Fantasy"]

N1 --> N2
```

Metadata.

Now consider:

```mermaid
flowchart TD

N1["Frieren"]
N2["Adapted From"]
N3["Manga"]

N1 --> N2
N2 --> N3
```

Relationship.

The second naturally leads somewhere.

The first merely categorises.

Mosaic should favour meaningful relationships over passive categorisation whenever practical.

---

# Relationship Density

Not every relationship deserves equal emphasis.

Some relationships are fundamental.

Others are incidental.

Example.

```mermaid
flowchart TD

N1["Frieren"]
N2["Episode 15"]

N1 --> N2
```

Strong.

```mermaid
flowchart TD

N1["Frieren"]
N2["Composer"]

N1 --> N2
```

Medium.

```mermaid
flowchart TD

N1["Frieren"]
N2["Won Award"]
N3["2023"]

N1 --> N2
N2 --> N3
```

Weak.

The strength of a relationship should influence future composition systems.

Not every relationship deserves equal visual weight.

---

# Relationships Are Directional

Relationships intentionally possess direction.

Example.

```mermaid
flowchart TD

N1["Book"]
N2["Adapted Into"]
N3["Film"]

N1 --> N2
N2 --> N3
```

is not necessarily identical to

```mermaid
flowchart TD

N1["Film"]
N2["Based On"]
N3["Book"]

N1 --> N2
N2 --> N3
```

Both describe the same connection.

Each answers a different user question.

Future engineering systems should preserve relationship direction where practical.

---

# Relationships Build Worlds

A World is not simply a collection of information.

It is a network.

```mermaid
graph TD

World

--> Frieren

Frieren --> Episode15

Frieren --> Manga

Frieren --> Composer

Frieren --> Studio

Frieren --> Characters
```

As relationships increase...

The World becomes richer.

Not because more information exists.

Because understanding increases.

---

# Good Examples

## Example 01

Current Focus

```

Dune
```

Relationships.

- sequel
- author
- audiobook
- film
- soundtrack

The interface naturally supports exploration.

---

## Example 02

Current Focus

```

Hans Zimmer
```

Relationships.

- Interstellar
- Dune
- Gladiator
- Live Performances

No recommendation engine required.

The relationships already exist.

---

## Example 03

Current Focus

```

Breaking Bad
```

Relationships.

- Better Call Saul
- El Camino
- Vince Gilligan
- Bryan Cranston

Again...

The experience expands naturally.

---

# Anti-patterns

The following behaviours weaken the relationship model.

## Flat Lists

```

Movie

Movie

Movie

Movie
```

Nothing explains why these belong together.

---

## Artificial Relationships

```mermaid
flowchart TD

N1["Trending"]
N2["Because Popular"]

N1 --> N2
```

Popularity is not a meaningful relationship.

It is a ranking.

---

## Hidden Relationships

Relationships exist but remain inaccessible behind unnecessary navigation.

Understanding becomes fragmented.

---

# Relationships And Composition

Relationships do not directly determine interface.

They influence composition.

```mermaid
flowchart TD

N1["Information"]
N2["Relationships"]
N3["Importance"]
N4["Composition"]

N1 --> N2
N2 --> N3
N3 --> N4
```

This distinction is critical.

Relationships create meaning.

Composition communicates meaning.

Presentation renders composition.

Each layer possesses one responsibility.

---

# Modules

Modules should contribute relationships.

Not interface.

Example.

Anime Module.

```mermaid
flowchart TD

N1["Episode"]
N2["Next Episode"]

N1 --> N2
```

Book Module.

```mermaid
flowchart TD

N1["Book"]
N2["Audiobook"]

N1 --> N2
```

Music Module.

```mermaid
flowchart TD

N1["Artist"]
N2["Concert"]

N1 --> N2
```

The platform remains responsible for deciding:

- emphasis
- hierarchy
- timing
- interaction

Relationships enrich the World.

The platform decides how users experience them.

---

# Relationship Graph

Long-term, Mosaic should increasingly understand entertainment as a graph rather than a hierarchy.

Traditional hierarchy.

```mermaid
flowchart TD

N1["Series"]
N2["Season"]
N3["Episode"]

N1 --> N2
N2 --> N3
```

Relationship graph.

```mermaid
graph LR

Episode

--- Series

Episode

--- Manga

Series

--- Studio

Series

--- Composer

Series

--- Characters

Characters

--- VoiceActors
```

This richer model enables future experiences without requiring additional interface concepts.

---

# Summary

Relationships transform information into understanding.

Without relationships...

Mosaic organises media.

With relationships...

Mosaic understands entertainment.

This distinction is one of the defining characteristics of the Mosaic Mental Model.
