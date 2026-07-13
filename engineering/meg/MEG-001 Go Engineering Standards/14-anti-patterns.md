<!--
File: engineering/meg/MEG-001 Go Engineering Standards/14-anti-patterns.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Anti-Patterns

> *Technical debt rarely begins with obviously bad decisions. It begins with seemingly convenient decisions that slowly become architectural constraints.*

---

# Purpose

Good engineering is not only about recognising good design.

It is equally important to recognise poor design before it becomes deeply embedded within a system.

This document catalogues the architectural anti-patterns that are prohibited within the Mosaic ecosystem.

Many of these patterns appear attractive initially.

Nearly all become increasingly expensive as software evolves.

---

# Philosophy

Within Mosaic:

> **Every abstraction carries a maintenance cost.**

Architecture should become simpler over time.

Not more complicated.

Whenever an anti-pattern appears, engineers should ask:

> "What problem created this?"

Fixing the underlying cause is almost always preferable to accommodating the symptom.

---

# God Objects

## Description

A God Object owns too many unrelated responsibilities.

Example:

```
MediaService

↓

Authentication

Metadata

Playback

Caching

Logging

Scheduling

Analytics

Notifications
```

Every new feature eventually finds its way into the same component.

The result is:

- high coupling
- poor cohesion
- merge conflicts
- difficult testing
- slow development

God objects violate the Single Responsibility Principle and are widely recognised as a major software design anti-pattern.  [oai_citation:0‡Bitloops](https://bitloops.com/resources/software-design/anti-patterns-in-software-design?utm_source=chatgpt.com)

---

## Symptoms

- Thousands of lines of code.
- Hundreds of methods.
- Large constructor.
- Frequent merge conflicts.
- Difficult to explain responsibility.
- Constant modification.

---

## Preferred Solution

Split responsibilities.

Prefer:

```
Metadata

Playback

Search

Analytics

Events
```

Each package owns one concern.

---

# God Packages

## Description

A package that gradually becomes responsible for unrelated concepts.

Examples:

```
common
```

```
utils
```

```
shared
```

```
helpers
```

These names communicate convenience rather than ownership.

Eventually every engineer adds another unrelated function.

The package becomes impossible to navigate.

---

## Preferred Solution

Move functionality into the package that owns the behaviour.

Ownership should always be obvious.

---

# Premature Abstraction

## Description

Creating abstractions before multiple implementations exist.

Example:

```
Repository

↓

RepositoryImpl
```

when only one repository exists.

Or:

```
MediaService

↓

MediaServiceInterface
```

with exactly one implementation.

This creates additional files without reducing coupling.

---

## Preferred Solution

Build concrete implementations first.

Extract interfaces only after they naturally emerge.

---

# Interface Pollution

## Description

Creating interfaces simply because "everything should have one."

Example:

```
Every struct

↓

Matching interface
```

Large numbers of unused interfaces reduce clarity.

They also encourage unnecessary indirection.

Go developers commonly identify premature interface creation as a frequent source of unnecessary complexity.  [oai_citation:1‡Reddit](https://www.reddit.com/r/golang/comments/1oc5is8/writing_better_go_lessons_from_10_code_reviews/?utm_source=chatgpt.com)

---

## Preferred Solution

Interfaces belong to consumers.

Not producers.

---

# Service Locator

## Description

Dependencies retrieved dynamically.

Example:

```go
service := container.Resolve("metadata")
```

The dependency graph becomes hidden.

Readers can no longer understand component requirements from constructors.

---

## Problems

- hidden dependencies
- runtime failures
- poor discoverability
- difficult testing

---

## Preferred Solution

Constructor injection.

Every dependency should be visible.

---

# Global Mutable State

## Description

Application state exposed globally.

Example:

```go
var Database *sql.DB
```

Every package can modify shared state.

Testing becomes increasingly difficult.

Race conditions become easier to introduce.

Google's Go best practices specifically caution against global package state and global service locators because they obscure ownership and complicate reasoning.  [oai_citation:2‡Chromium Git Repositories](https://chromium.googlesource.com/external/github.com/google/styleguide/%2B/HEAD/go/best-practices.md?utm_source=chatgpt.com)

---

## Preferred Solution

Pass dependencies explicitly.

---

# Base Types

## Description

Attempting to recreate inheritance.

Examples:

```
BaseService
```

```
AbstractRepository
```

```
BaseHandler
```

These components inevitably accumulate unrelated behaviour.

Eventually every implementation inherits unnecessary functionality.

---

## Preferred Solution

Composition.

Shared behaviour should become reusable components.

Not parent types.

---

# Utility Packages

## Description

General-purpose dumping grounds.

Examples:

```
utils
```

```
common
```

```
helpers
```

These packages typically exist because ownership has not been identified.

---

## Preferred Solution

Move code to the package that owns the behaviour.

If ownership cannot be identified, the design probably requires reconsideration.

---

# Boolean Parameters

## Description

Functions controlled by flags.

Example:

```go
Process(media, true)
```

The meaning of:

```
true
```

is invisible.

Adding additional flags rapidly becomes unreadable.

---

## Preferred Solution

Split behaviour into separate functions.

Or introduce explicit configuration types.

---

# Magic Strings

## Description

Business logic relying upon hard-coded string literals.

Example:

```go
if status == "completed"
```

Problems include:

- spelling mistakes
- inconsistent values
- poor discoverability
- difficult refactoring

---

## Preferred Solution

Define constants.

Example:

```go
const (
    StatusCompleted = "completed"
)
```

Or preferably:

```go
type Status string
```

This communicates intent through the type system.

---

# Magic Numbers

## Description

Literal numeric values without meaning.

Example:

```go
cacheTTL := 3600
```

Questions immediately arise.

3600 what?

Seconds?

Milliseconds?

Minutes?

---

## Preferred Solution

Prefer named constants.

Example:

```go
const DefaultCacheTTL = time.Hour
```

The intent becomes immediately obvious.

---

# Deep Nesting

## Description

Excessive indentation.

Example:

```
if

↓

for

↓

switch

↓

if

↓

select
```

Deep nesting reduces readability.

---

## Preferred Solution

Return early.

Handle error cases immediately.

Flatten control flow wherever practical.

---

# Long Functions

## Description

Functions performing many unrelated operations.

Symptoms include:

- scrolling required to understand behaviour
- multiple abstraction levels
- repeated comments
- unrelated responsibilities

---

## Preferred Solution

Extract cohesive behaviour into well-named functions.

Each function should communicate one idea.

---

# Large Constructors

## Description

Constructors accepting excessive dependencies.

Example:

```
NewService(

12 parameters
)
```

This usually indicates excessive responsibility.

---

## Preferred Solution

Split the service.

Or introduce cohesive supporting components.

---

# Hidden Goroutines

## Description

Constructors starting background work automatically.

Example:

```go
NewCache()
```

Internally:

```
Starts goroutines

Starts timers

Starts cleanup workers
```

Construction should never unexpectedly begin application behaviour.

---

## Preferred Solution

Separate:

```
New()

↓

Start()

↓

Stop()
```

Lifecycle becomes explicit.

---

# Ignored Errors

## Description

Silently discarding errors.

Example:

```go
_, _ = writer.Write(data)
```

Ignored errors create undefined behaviour.

Every error deserves an intentional decision.

---

# Reflection As Architecture

## Description

Reflection replacing explicit code.

Examples include:

- runtime dependency injection
- automatic registration
- generic service discovery

Reflection increases:

- runtime failures
- hidden behaviour
- debugging difficulty

---

## Preferred Solution

Explicit construction.

Compile-time guarantees.

---

# Circular Dependencies

## Description

Package A depends upon Package B.

Package B depends upon Package A.

The Go compiler prohibits this.

Within Mosaic this is considered an architectural warning rather than an inconvenience.

---

## Preferred Solution

Extract shared behaviour.

Or redesign ownership.

---

# Over-Generalisation

## Description

Designing software for hypothetical future requirements.

Examples:

- plugin systems before plugins exist
- generic frameworks before use cases exist
- configuration options nobody uses

---

## Preferred Solution

Solve today's problem well.

Allow tomorrow's abstractions to emerge naturally.

---

# Recognising Anti-Patterns

Most anti-patterns share common characteristics.

They usually:

- increase coupling
- reduce readability
- hide ownership
- introduce indirection
- complicate testing
- make debugging harder

If a proposed solution exhibits several of these characteristics, it deserves additional architectural scrutiny.

---

# Mosaic Guidelines

Within Mosaic:

- God Objects are prohibited.
- God Packages are prohibited.
- Premature abstraction is prohibited.
- Service locators are prohibited.
- Global mutable state is prohibited.
- Base classes are prohibited.
- Utility packages should be avoided.
- Hidden goroutines are prohibited.
- Reflection should not define architecture.
- Magic strings and magic numbers should be replaced with meaningful types or constants.

Good architecture removes accidental complexity.

It never institutionalises it.

---

# Summary

Anti-patterns rarely appear overnight.

They emerge gradually through many individually reasonable decisions.

The responsibility of every engineer is therefore not merely to write good code.

It is to recognise when good code begins drifting towards bad architecture.

The earlier an anti-pattern is identified, the cheaper it is to remove.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`13-design-patterns.md`

**Next File**

`15-code-review-standards.md`
