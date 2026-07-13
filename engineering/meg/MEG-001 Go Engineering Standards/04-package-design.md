<!--
File: engineering/meg/MEG-001 Go Engineering Standards/04-package-design.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Package Design

> *The package is the fundamental unit of architecture in Go. Good packages make good software. Poor packages make every line of code harder to understand.*

---

# Purpose

Packages are the primary mechanism by which Go organises software.

Unlike many object-oriented languages, where classes represent the fundamental organisational unit, Go places architectural responsibility at the package level.

For this reason, package design is one of the most important architectural decisions made within a Go codebase.

This document defines how packages should be designed throughout the Mosaic ecosystem.

---

# Why Packages Matter

Every engineer interacting with a Go project spends most of their time moving between packages.

Good packages answer three questions immediately.

> What responsibility does this package own?

> What does this package expose?

> What should never belong here?

When those questions are difficult to answer, the package has usually become too broad.

---

# Philosophy

Within Mosaic:

> **Packages own responsibilities. Types merely implement them.**

Packages are architectural boundaries.

Types are implementation details.

A package should communicate purpose before implementation.

---

# The Responsibility Rule

Every package MUST own exactly one responsibility.

Examples include:

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

A package should never become a collection of unrelated utilities simply because they happen to be used together.

---

# Cohesion

Everything inside a package should naturally belong together.

A useful question is:

> "Would removing this file make the package easier to explain?"

If the answer is yes, the file probably belongs elsewhere.

Packages should feel cohesive.

Not convenient.

---

# Coupling

Packages SHOULD minimise knowledge of one another.

The fewer packages required to understand a feature, the easier the software becomes to maintain.

Signs of excessive coupling include:

- frequent circular dependency attempts
- packages importing one another indirectly
- unrelated changes requiring edits across multiple packages
- large dependency graphs

Good package boundaries reduce these problems naturally.

---

# Package Size

Package size should emerge naturally.

Neither extremely small nor extremely large packages are desirable.

A package containing a single type is not automatically better.

Likewise, a package containing fifty unrelated types is almost certainly worse.

Engineers should optimise for conceptual clarity.

Not line counts.

---

# Public API

Every exported identifier becomes part of the package's public contract.

Exporting something should therefore be considered an architectural decision.

Ask:

> Does another package genuinely need this?

If the answer is no, keep it unexported.

Smaller public APIs are easier to evolve.

---

# Package Names

Package names SHOULD be:

- short
- descriptive
- lowercase
- singular where practical
- nouns rather than verbs

Good examples:

```
metadata
```

```
library
```

```
playback
```

```
scheduler
```

Poor examples:

```
metadataservice
```

```
helpers
```

```
common
```

```
misc
```

```
stuff
```

Go package names become part of every import statement.

Short, meaningful names improve readability throughout the codebase. The Go team explicitly recommends short, clear package names and discourages meaningless names such as `util`, `common`, `api`, `types` or `interfaces`.  [oai_citation:0‡Go](https://go.dev/blog/package-names?utm_source=chatgpt.com)

---

# Avoid Package Stutter

Identifiers should not repeat the package name.

Poor:

```go
package library

type LibraryService struct{}
```

Usage:

```go
library.LibraryService
```

Better:

```go
package library

type Service struct{}
```

Usage:

```go
library.Service
```

Or better still, if the type represents the domain:

```go
package library

type Manager struct{}
```

or

```go
package library

type Catalogue struct{}
```

The package already provides context.

Avoid repeating it.

---

# Avoid Generic Packages

The following package names SHOULD NOT exist.

```
util
```

```
utils
```

```
common
```

```
shared
```

```
base
```

```
types
```

```
interfaces
```

```
helpers
```

These names communicate implementation convenience rather than architectural responsibility.

Over time they become dumping grounds.

If something belongs in `utils`, its true ownership has probably not yet been identified.

---

# Package Ownership

Every package should have a clear owner.

Ownership answers:

- what belongs here
- what does not belong here
- who is responsible for changes

Example:

```
metadata
```

Owns:

- metadata models
- metadata ingestion
- metadata translation
- metadata providers

It does not own:

- HTTP handlers
- playback
- authentication
- persistence for unrelated domains

Responsibilities should not leak.

---

# Internal Collaboration

Packages should collaborate through exported behaviour.

They should not rely upon one another's implementation details.

Good:

```
metadata.Provider

↓

library.Service
```

Poor:

```
library

↓

metadata/internal/parser

↓

metadata/private/cache
```

If another package requires access to implementation details, the abstraction is probably incorrect.

---

# Package Dependencies

Imports should naturally form a directed graph.

Preferred:

```
transport

↓

application

↓

domain

↓

infrastructure
```

Avoid:

```
library

↓

metadata

↓

library
```

Circular dependencies are prohibited by the Go compiler.

Rather than viewing this as a limitation, Mosaic treats it as an architectural safeguard.

If two packages require one another, they probably represent a single responsibility or require a new shared abstraction.

---

# Package Documentation

Every exported package MUST include a package comment.

The package comment should explain:

- why the package exists
- what responsibility it owns
- what it intentionally does not own

Example:

```go
// Package metadata manages the ingestion, transformation and
// persistence of media metadata from external providers.
package metadata
```

Package comments are part of Go's documentation conventions and are expected for exported packages.  [oai_citation:1‡Go](https://go.dev/wiki/CodeReviewComments?utm_source=chatgpt.com)

---

# When To Create A New Package

A new package SHOULD only be created when at least one of the following becomes true.

- A new business capability exists.
- Dependencies need separating.
- Visibility needs restricting.
- Ownership has changed.
- Reuse naturally emerges.

A package SHOULD NOT be created merely because:

- a file is becoming large
- another project used the same structure
- "everything should have its own package"

Packages should emerge from architecture.

Not aesthetics.

---

# Mosaic Package Principles

Every package within Mosaic should satisfy the following checklist.

- Own one responsibility.
- Have one reason to change.
- Expose the smallest possible API.
- Hide implementation details.
- Minimise dependencies.
- Avoid circular knowledge.
- Communicate purpose through its name.
- Be easy to explain in one sentence.

If these conditions are not met, the package should be reconsidered.

---

# Summary

Good packages make software understandable.

They reduce coupling.

They improve discoverability.

They encourage clear ownership.

Within Mosaic, packages are considered architectural boundaries rather than folders.

They should therefore be designed with the same care as public APIs.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`03-project-structure.md`

**Next File**

`05-dependency-management.md`
