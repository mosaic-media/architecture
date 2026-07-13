<!--
File: engineering/meg/MEG-001 Go Engineering Standards/18-contributor-guidance.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Contributor Guidance

> *Consistency is the responsibility of every contributor. The goal is not simply to write working code, but to write code that belongs.*

---

# Purpose

This document provides practical guidance for engineers contributing to the Mosaic ecosystem.

The previous chapters establish engineering standards.

This chapter explains how contributors should apply those standards during day-to-day development.

Every contribution, regardless of size, should leave the codebase more understandable, more maintainable and more consistent than before.

---

# Philosophy

Within Mosaic:

> **Contributors do not add code. They improve the platform.**

Every commit should contribute towards one or more of the following:

- new functionality
- improved readability
- improved maintainability
- reduced complexity
- improved documentation
- improved reliability
- improved observability

Features alone are not progress.

Quality matters equally.

---

# Before Writing Code

Before beginning implementation, every contributor SHOULD understand:

- the problem being solved
- the architectural boundaries involved
- the affected packages
- existing engineering standards
- relevant ADRs
- related specifications

Code should be the final step.

Understanding comes first.

---

# Before Creating A Package

Ask:

- Does this responsibility already exist?
- Can the existing package evolve naturally?
- Would a new package improve clarity?
- Does this introduce unnecessary coupling?

New packages should emerge from architectural necessity.

Not personal preference.

---

# Before Creating An Interface

Ask:

- Is there more than one consumer?
- Does this reduce coupling?
- Am I solving today's problem?
- Would a concrete type be simpler?

If uncertainty exists, begin with a concrete implementation.

Interfaces are easier to introduce later than remove.

---

# Before Introducing Concurrency

Ask:

- What problem does concurrency solve?
- Who owns this goroutine?
- How is cancellation handled?
- How are errors propagated?
- What happens during shutdown?

Concurrency without ownership is prohibited.

---

# Before Optimising

Ask:

- Has the application been profiled?
- Is this actually a bottleneck?
- Can measurements demonstrate improvement?
- Does readability suffer?

Optimisation without evidence should not proceed.

---

# Before Merging

Every contributor SHOULD complete the following checklist.

## Architecture

- Responsibilities remain clear.
- Dependencies flow correctly.
- Package ownership remains consistent.
- No unnecessary abstraction introduced.

---

## Correctness

- Errors handled.
- Edge cases considered.
- Context propagated.
- Resources cleaned up.

---

## Testing

- New behaviour tested.
- Existing tests pass.
- Race detector considered.
- Benchmarks added where appropriate.

---

## Documentation

- Exported APIs documented.
- Package comments updated where necessary.
- ADR referenced if applicable.
- Architecture documentation updated if required.

Go expects exported packages and exported identifiers to have documentation comments. Documentation is part of the public API, not an optional extra.  [oai_citation:0‡Go](https://go.dev/doc/comment?utm_source=chatgpt.com)

---

## Quality

- Dead code removed.
- Naming improved.
- Duplication reduced.
- Complexity simplified where practical.

Every pull request should leave the surrounding code better than before.

---

# Commit Philosophy

Commits SHOULD represent one logical change.

Good commits are:

- focused
- reviewable
- reversible
- understandable

Avoid commits that simultaneously:

- refactor architecture
- introduce new features
- rename packages
- reformat unrelated files

Small commits produce better reviews.

---

# Pull Requests

A pull request should answer three questions.

## What changed?

Describe the behaviour.

Not merely the files.

---

## Why?

Explain the motivation.

Reference:

- issue
- ADR
- architecture specification

where appropriate.

---

## How was it validated?

Examples include:

- unit tests
- integration tests
- benchmarks
- manual verification

Confidence should be demonstrated.

Not assumed.

---

# Documentation Expectations

Documentation is considered production code.

Every contributor is responsible for maintaining it.

When behaviour changes:

Update documentation.

Do not defer documentation updates.

Documentation that disagrees with implementation is a defect.

---

# Naming

Engineers SHOULD spend time choosing names.

Good names reduce:

- comments
- documentation
- onboarding effort
- bugs

Poor names create confusion that persists for years.

Rename aggressively when understanding improves.

---

# Ask Questions

No contributor is expected to know everything.

When uncertainty exists:

- consult the MEG
- consult relevant ADRs
- discuss architectural trade-offs
- ask for review early

It is cheaper to ask questions than rewrite software.

---

# Learning The Codebase

New contributors SHOULD prioritise understanding before modification.

Recommended order:

```
Architecture Specifications

↓

ADRs

↓

Package Documentation

↓

Public APIs

↓

Implementation

↓

Tests
```

Understanding architecture first reduces accidental complexity later.

---

# Open Source Contributions

External contributors are expected to follow the same engineering standards as internal contributors.

Review criteria remain identical.

Code quality should never depend upon who authored the change.

Consistency matters more than authorship.

---

# Engineering Culture

Every contributor should strive to:

- leave constructive review comments
- share architectural knowledge
- improve documentation
- simplify existing code
- mentor newer contributors
- question unnecessary complexity

Healthy engineering culture produces healthy software.

---

# Things To Avoid

Avoid contributing code that:

- introduces hidden dependencies
- bypasses architecture
- duplicates existing behaviour
- ignores engineering standards
- increases complexity unnecessarily
- solves hypothetical future problems

The simplest correct solution is usually preferred.

---

# Contributor Checklist

Before requesting review, confirm:

- [ ] The implementation follows the MEG.
- [ ] Package ownership remains clear.
- [ ] Dependencies are explicit.
- [ ] Errors are handled correctly.
- [ ] Context is propagated.
- [ ] Tests pass.
- [ ] Documentation is updated.
- [ ] Dead code removed.
- [ ] Naming is clear.
- [ ] The repository is better than before.

---

# Relationship to the MEG

This document does not introduce additional engineering rules.

Instead, it explains how contributors should apply the standards established throughout MEG-001 during everyday development.

Engineering standards only improve software when contributors consistently follow them.

---

# Summary

Software quality is a shared responsibility.

Every contributor influences:

- architecture
- maintainability
- readability
- engineering culture

Within Mosaic, contributions are measured not only by the features they introduce, but by the lasting improvements they make to the platform.

The best contribution is one that future contributors barely notice because it feels like it has always belonged.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`17-adrs.md`

**Next File**

`glossary.md`
