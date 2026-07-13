<!--
File: engineering/meg/MEG-001 Go Engineering Standards/03-project-structure.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Project Structure

> *A project's directory structure is its first piece of documentation. Before a single line of code is read, contributors should understand where responsibility lives.*

---

# Purpose

A consistent project structure allows engineers to navigate unfamiliar codebases quickly and confidently.

Within Mosaic, directories are organised around **architectural responsibility**, not personal preference.

Every package should have a clear owner, a clear purpose and a clearly defined dependency direction.

The structure should communicate the architecture.

It should never hide it.

---

# Philosophy

Project structure exists to reduce cognitive load.

When engineers know where something belongs, they spend less time searching and more time solving problems.

A well-structured repository should answer questions such as:

- Where does business logic live?
- Where are HTTP handlers implemented?
- Where should database code exist?
- Where are background workers located?
- Where are events defined?
- Where should new features be added?

Without opening a single source file.

---

# Design Principles

The Mosaic project structure is built upon the following principles.

## Feature Ownership

Packages own business capabilities.

Examples:

```
library
```

```
metadata
```

```
playback
```

```
authentication
```

rather than technical concepts such as:

```
helpers
```

```
common
```

```
misc
```

Feature-oriented organisation improves discoverability and reduces accidental coupling.

---

## Single Responsibility

Every package SHOULD have one reason to change.

If a package contains unrelated concepts, it should be split.

Large "catch-all" packages inevitably become architectural bottlenecks.

---

## Dependency Direction

Dependencies always flow inward.

```
Transport

↓

Application

↓

Domain

↓

Infrastructure
```

Lower layers MUST NOT depend upon higher layers.

For example:

```
HTTP Handler

↓

Service

↓

Repository

↓

Database
```

The repository must never import an HTTP package.

Likewise, domain logic must never depend on transport concerns.

---

## Encapsulation

Implementation details should remain private.

Packages should expose only what other packages require.

Everything else should remain unexported.

Go's `internal` mechanism exists specifically to enforce package boundaries at compile time and is encouraged for application implementation details. ([go.dev](https://go.dev/doc/modules/layout))

---

# Standard Repository Layout

Every Mosaic service SHOULD follow the same high-level structure.

```
cmd/

internal/

pkg/

api/

configs/

scripts/

docs/

test/
```

Not every repository will require every directory.

Unused directories SHOULD NOT be created simply to satisfy the standard.

Structure should emerge from actual requirements.

---

# Directory Responsibilities

## cmd/

Contains application entry points.

Examples:

```
cmd/server

cmd/migrate

cmd/worker
```

Each directory represents an independently executable application.

Business logic MUST NOT be implemented here.

Responsibilities include:

- dependency construction
- configuration loading
- application startup
- graceful shutdown

Nothing more.

---

## internal/

Contains private application code.

Everything inside `internal` is considered implementation detail.

Typical contents include:

```
internal/

    app/

    domain/

    transport/

    infrastructure/

    scheduler/

    events/

    middleware/
```

Most Mosaic code will exist here.

---

## pkg/

Contains reusable packages intended for external consumption.

This directory SHOULD be used sparingly.

Code belongs in `pkg` only if another repository is expected to import it.

Moving code into `pkg` should be considered an architectural commitment.

---

## api/

Contains externally published API contracts.

Examples include:

- OpenAPI specifications
- Protobuf definitions
- JSON schemas

Generated code SHOULD NOT be manually modified.

---

## configs/

Stores example configuration files.

Configuration templates belong here.

Actual secrets MUST NOT.

---

## docs/

Repository-specific documentation.

Architecture specifications belong within the architecture repository rather than individual services whenever practical.

---

## scripts/

Automation utilities.

Examples:

- build scripts
- release scripts
- migration helpers
- local development tooling

Scripts SHOULD remain idempotent whenever possible.

---

## test/

Cross-package integration tests.

Unit tests SHOULD remain beside the package they exercise.

Large end-to-end scenarios belong here.

---

# Package Organisation

Within `internal`, packages SHOULD be organised around business capabilities.

Preferred:

```
internal/

    library/

    metadata/

    playback/

    users/

    authentication/
```

Avoid:

```
internal/

    services/

    managers/

    implementations/

    interfaces/
```

The former communicates purpose.

The latter communicates implementation mechanics.

Purpose should always win.

---

# Naming Conventions

Package names MUST:

- be singular where practical
- use lowercase
- avoid underscores
- avoid abbreviations unless universally recognised
- describe responsibility

Good examples:

```
library
```

```
metadata
```

```
playback
```

Poor examples:

```
helpers
```

```
common
```

```
shared
```

```
utils
```

These names communicate ownership poorly and tend to become dumping grounds for unrelated code.

---

# Package Size

Large packages should be viewed with suspicion.

Signs a package has grown too large include:

- hundreds of exported identifiers
- multiple unrelated responsibilities
- frequent merge conflicts
- unclear ownership
- circular dependencies beginning to emerge

When this occurs, responsibilities SHOULD be extracted into cohesive packages.

---

# Internal Before Shared

Engineers frequently overestimate the likelihood that code will become reusable.

Within Mosaic:

Code SHOULD begin inside `internal`.

Only after multiple repositories demonstrate a genuine need should it be promoted into `pkg`.

Sharing code prematurely often creates tighter coupling than duplication.

---

# Example Structure

A typical Mosaic service may resemble:

```
cmd/

    mosaic-server/

internal/

    app/

    authentication/

    events/

    library/

    metadata/

    playback/

    scheduler/

    transport/

        http/

        websocket/

    infrastructure/

        postgres/

        duckdb/

        blob/

pkg/

api/

configs/

docs/

scripts/

test/
```

This structure balances discoverability, encapsulation and future growth while remaining familiar to experienced Go developers.

---

# Anti-Patterns

The following package names SHOULD NOT exist without exceptional justification.

```
utils
```

```
common
```

```
base
```

```
shared
```

```
misc
```

```
manager
```

```
helper
```

These packages usually indicate responsibilities have not yet been properly identified.

If a function belongs in `utils`, it probably belongs somewhere else.

---

# Summary

Project structure should communicate architecture.

Every directory should answer:

> **What responsibility does this own?**

If that question cannot be answered clearly, the structure should be reconsidered.

Good structure enables good engineering.

Poor structure amplifies technical debt long before implementation quality begins to decline.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`02-thinking-in-go.md`

**Next File**

`04-package-design.md`
