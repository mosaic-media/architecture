<!--
File: engineering/meg/MEG-001 Go Engineering Standards/01-engineering-philosophy.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Engineering Philosophy

> *Architecture determines how software evolves. Engineering philosophy determines why it evolves that way.*

---

# Purpose

Every engineering decision made within Mosaic should be guided by a small set of enduring principles rather than personal preference.

Programming languages evolve.

Frameworks come and go.

Libraries are replaced.

Good engineering principles remain remarkably stable.

This document establishes the philosophical foundation upon which every future Go engineering standard is built.

---

# Philosophy Statement

Within Mosaic:

> **Software is engineered for the next engineer, not the current one.**

Every implementation should optimise for:

- Understanding
- Maintainability
- Predictability
- Correctness
- Observability
- Evolvability

The primary consumer of source code is not the compiler.

It is another engineer.

---

# Core Principles

## 1. Simplicity Over Cleverness

> **"Simple things should be simple."**

The simplest solution that correctly solves the problem is almost always preferred.

Complexity should only be introduced when it provides measurable value.

Avoid engineering solutions that require significant explanation to understand.

If an implementation appears "clever", it should be assumed to require further simplification.

### Why

Simple systems are easier to:

- review
- debug
- optimise
- extend
- replace

Complexity accumulates interest.

---

## 2. Explicit Over Implicit

Hidden behaviour creates hidden bugs.

Software should communicate what it is doing directly.

Avoid:

- hidden state
- implicit side effects
- surprising control flow
- reflection where unnecessary
- unnecessary indirection

A reader should rarely need to leave the current function to understand what is happening.

### Example

Prefer:

```go
service.Start(ctx)
```

Over:

```go
service.Execute()
```

where `Execute()` internally creates goroutines, opens database connections and ignores cancellation.

Behaviour should be visible.

---

## 3. Readability Is A Feature

Readable code is easier to verify.

Easier to test.

Easier to optimise.

Easier to replace.

Readable software therefore has a lower long-term cost.

A function should communicate intent before implementation.

If comments are required to explain *what* code is doing, the implementation should usually be rewritten.

Comments should explain **why**, not **what**.

---

## 4. Design For Change

Requirements will change.

Architecture should make those changes inexpensive.

Good engineering reduces the cost of future change.

This generally means:

- small packages
- clear boundaries
- loose coupling
- explicit dependencies
- cohesive responsibilities

Software should be difficult to break accidentally.

---

## 5. Favour Composition

Mosaic adopts composition as its primary mechanism for building complex systems.

Large inheritance hierarchies are intentionally avoided.

Instead:

Small components collaborate.

Small packages compose.

Small interfaces connect systems.

Complex behaviour emerges from combining simple responsibilities.

Later chapters define how composition should be applied throughout Go projects.

---

## 6. Make The Correct Thing Easy

Good architecture encourages correct behaviour.

Poor architecture relies upon discipline.

Whenever possible:

- invalid states should be impossible
- dangerous operations should be difficult
- correct usage should be obvious

Good APIs reduce mistakes by design.

---

## 7. Optimise Last

Performance matters.

Premature optimisation does not.

Optimisation should be driven by:

- profiling
- measurement
- production evidence

Never by assumption.

Simple code that is slightly slower is usually preferable to complicated code that is theoretically faster.

When optimisation becomes necessary, it should be isolated and well documented.

This reflects long-standing Go guidance to measure first and optimise second. ([go.dev](https://go.dev/blog/profiling-go-programs))

---

## 8. Consistency Over Preference

Every engineer has preferences.

A shared codebase cannot.

Consistency reduces cognitive load.

The best engineering standard is often not the theoretically perfect one, but the one applied consistently across the entire platform.

Future contributors should spend their time understanding business logic rather than adapting to different coding styles.

---

## 9. The Compiler Is A Design Tool

Go's type system exists to eliminate categories of bugs before software executes.

Types should communicate intent.

Interfaces should model behaviour.

The compiler should detect mistakes wherever practical.

Whenever a runtime validation can reasonably become a compile-time guarantee, the compile-time solution should be preferred.

---

## 10. Engineering Is Communication

Every engineering artefact communicates.

Source code communicates.

Tests communicate.

Documentation communicates.

Naming communicates.

Architecture communicates.

The goal is not merely to produce software that functions.

The goal is to produce software whose intent remains obvious years after it was written.

---

# Decision Framework

When evaluating multiple implementations, engineers SHOULD ask the following questions.

1. Which implementation is easiest to understand?
2. Which implementation is easiest to test?
3. Which implementation introduces the least coupling?
4. Which implementation is easiest to change?
5. Which implementation communicates intent most clearly?
6. Which implementation aligns with established Go conventions?
7. Which implementation best supports the long-term health of the codebase?

The implementation that scores highest overall should generally be preferred.

---

# Engineering Priorities

When trade-offs exist, Mosaic evaluates engineering decisions using the following priority order.

```
Correctness

↓

Maintainability

↓

Readability

↓

Testability

↓

Observability

↓

Performance

↓

Convenience
```

This ordering intentionally places long-term maintainability above short-term development speed.

Convenience should never justify unnecessary complexity.

---

# Boy Scout Rule

Every engineer shares responsibility for improving the codebase.

Whenever modifying existing code:

- improve naming where appropriate
- simplify unnecessary complexity
- remove dead code
- improve documentation
- increase test coverage
- reduce duplication

Small improvements made consistently produce significant long-term gains.

Large refactors are not required.

Continuous improvement is.

---

# Philosophy Summary

The engineering philosophy of Mosaic can be summarised as follows.

> Build software that another engineer can confidently change without fear.

Every future engineering standard defined within the MEG should reinforce that objective.

If a rule makes software harder to understand, harder to test or harder to evolve, it should be challenged.

Engineering standards exist to improve software.

Never to burden it.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`00-document-control.md`

**Next File**

`02-thinking-in-go.md`
