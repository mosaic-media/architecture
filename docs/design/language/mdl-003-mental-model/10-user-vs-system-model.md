<!--
File: docs/design/language/mdl-003-mental-model/10-user-vs-system-model.md
Document: MDL-003
Status: Draft
-->

# User Model vs System Model

---

# Purpose

Every successful software platform maintains two separate models.

The first describes how the software actually works.

The second describes how users believe it works.

These models should never be identical.

Instead, the implementation should exist to support the user's understanding while remaining largely invisible.

This chapter formally separates these two models within Mosaic.

---

# Two Models

Every Mosaic implementation contains:

```mermaid
flowchart TD

N1["System Model"]
N2["Mental Translation"]
N3["User Model"]

N1 --> N2
N2 --> N3
```

The System Model belongs to engineering.

The User Model belongs to experience.

MDL intentionally defines the User Model.

Engineering remains free to optimise the System Model provided the User Model remains stable.

---

# The System Model

The System Model describes technical reality.

Examples include:

- SQLite
- DuckDB
- GraphQL
- HTTP
- WebSockets
- Modules
- Authentication
- Caching
- Event Streams
- Composition Engine
- Rendering Pipeline

These concepts are important.

They are simply not important to the user.

---

# The User Model

The User Model describes conceptual reality.

Examples include:

- My World
- My Current Focus
- Continue Watching
- Reading Progress
- Next Episode
- Related Books
- My Collection

These concepts explain the platform without exposing implementation.

Users should never need to translate technical architecture into entertainment concepts.

Mosaic performs that translation for them.

---

# Why The Models Must Differ

Consider the following engineering implementation.

```mermaid
flowchart TD

N1["SQLite"]
N2["DuckDB"]
N3["Metadata Providers"]
N4["Relationship Graph"]
N5["Composition Engine"]
N6["Renderer"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

This architecture may be elegant.

It is also meaningless to the majority of users.

The equivalent User Model is:

```mermaid
flowchart TD

N1["My World"]
N2["What I&#x27;m Enjoying"]
N3["What Helps Me Continue"]

N1 --> N2
N2 --> N3
```

The second model is dramatically simpler.

It therefore becomes the model users naturally adopt.

---

# The Translation Layer

One of Mosaic's primary responsibilities is translating the System Model into the User Model.

```mermaid
flowchart LR

System["System Model"]

Translation["Mosaic"]

User["User Model"]

System --> Translation

Translation --> User
```

Users should never experience the System Model directly.

The quality of Mosaic depends upon how effectively this translation occurs.

---

# The Cost Of Leaking Implementation

Implementation details occasionally leak into user experience.

Examples include:

```

Refresh Metadata

Clear Cache

Module Failed

Provider Offline

Mapping Conflict

Sync Database
```

These concepts describe implementation.

Not entertainment.

Whenever possible they should be translated into language users naturally understand.

Example.

Instead of:

```

Metadata Refresh Failed
```

Prefer:

```

We couldn't update information for this series.

Your existing information is still available.
```

The implementation remains accurate.

The experience becomes significantly calmer.

---

# Administration

Administration intentionally occupies a unique position.

Administrators occasionally require access to parts of the System Model.

Examples include:

- storage
- modules
- providers
- users
- diagnostics

Even here, Mosaic should progressively reveal technical detail.

Family members sharing a server should not immediately encounter engineering terminology.

Administrators should be able to move from:

```mermaid
flowchart TD

N1["Simple"]
N2["Advanced"]
N3["Diagnostic"]

N1 --> N2
N2 --> N3
```

rather than beginning with raw implementation.

---

# Modules

Modules contribute primarily to the System Model.

They provide:

- information
- relationships
- capabilities

They should not redefine the User Model.

Regardless of how many modules are installed, users should continue experiencing:

- one World
- one Focus
- one Companion
- one Composition model

The platform is responsible for preserving conceptual consistency.

---

# Failure

Failures should be translated through the User Model whenever practical.

System Model.

```

AniList API Timeout
```

User Model.

```

Episode information couldn't be updated.

We'll try again automatically.

You can continue watching normally.
```

The user understands the consequence.

They do not need to understand the implementation.

---

# Engineering Freedom

Separating these models gives engineering significant freedom.

The following may change without affecting the User Model:

- databases
- APIs
- rendering engines
- frontend frameworks
- module architecture
- networking
- storage

Provided the conceptual experience remains stable.

This separation is one of the primary long-term objectives of MDL.

---

# Anti-patterns

## Implementation Terminology

```

DuckDB

SQLite

Provider

GraphQL

HTTP
```

appearing throughout the user experience.

---

## Module Personalities

Modules introducing competing terminology.

```mermaid
flowchart TD

N1["Library"]
N2["Collection"]
N3["Shelf"]
N4["Archive"]

N1 --> N2
N2 --> N3
N3 --> N4
```

for the same concept.

The User Model becomes fragmented.

---

## Engineering Navigation

Users navigating implementation rather than entertainment.

Example.

```mermaid
flowchart TD

N1["Metadata"]
N2["Providers"]
N3["Mappings"]

N1 --> N2
N2 --> N3
```

instead of

```mermaid
flowchart TD

N1["Series"]
N2["Characters"]
N3["Related Works"]

N1 --> N2
N2 --> N3
```

The implementation has become visible.

---

# User Confidence

The User Model should continuously reinforce confidence.

Users should increasingly feel:

"I know how Mosaic works."

without actually understanding:

- composition engines
- relationship graphs
- runtime systems
- metadata providers

Confidence comes from conceptual consistency.

Not technical knowledge.

---

# Relationship To Future Specifications

Future specifications should continue strengthening this separation.

Examples include:

- Composition Engine
- Runtime Atmosphere
- Module SDK
- GraphQL UI
- Information Model

These systems should become increasingly sophisticated internally while making the user experience progressively simpler.

---

# Summary

The Mental Model belongs to users.

The System Model belongs to engineers.

Mosaic succeeds when users never need to think about the System Model in order to enjoy their entertainment.

Every future engineering decision should therefore ask:

> **Does this strengthen the User Model...**

or

> **Does it leak the System Model?**

Only the first outcome aligns with the Mosaic Design Language.
