<!--
File: engineering/meg/MEG-001 Go Engineering Standards/16-boy-scout-rule.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# The Boy Scout Rule

> *Leave the code cleaner than you found it.*

---

# Purpose

Software quality is rarely transformed through large rewrites.

Instead, quality improves through thousands of small, deliberate decisions made by engineers every day.

The Boy Scout Rule provides a simple philosophy for maintaining long-lived software systems.

Every change, regardless of size, should improve the codebase in some measurable way.

Within Mosaic, this principle is considered a core engineering responsibility.

---

# Philosophy

Within Mosaic:

> **Every commit should leave the repository in a better state than it was found.**

Improvement does not require large refactoring.

It requires continuous attention.

Small improvements made consistently prevent the accumulation of technical debt.

---

# Continuous Improvement

Engineering quality is cumulative.

One engineer:

- improves a variable name

Another:

- removes dead code

Another:

- adds missing tests

Another:

- simplifies a complex function

Months later the software has become significantly easier to maintain.

None of these changes were individually transformative.

Together they fundamentally improve the health of the project.

---

# What Counts As Improvement?

Improvement may include:

- clearer naming
- simpler control flow
- reduced duplication
- smaller functions
- better documentation
- improved package boundaries
- stronger typing
- improved test coverage
- additional benchmarks
- clearer logging
- improved observability
- dead code removal
- removing unnecessary abstraction

Even fixing a spelling mistake contributes positively.

Quality compounds.

---

# Small Changes Matter

Large refactoring efforts are risky.

Small improvements are sustainable.

Example.

Poor:

```
"I'm not touching that because this isn't my feature."
```

Preferred:

```
"I'm already here.

I'll improve this function while I'm modifying it."
```

Improvement should naturally accompany development.

Not wait for dedicated cleanup projects.

---

# Refactoring Is Not Rewriting

The Boy Scout Rule does **not** encourage unnecessary rewrites.

If software is:

- stable
- understandable
- correct

Leave it alone.

Refactor only where improvement provides genuine value.

Every modification carries risk.

Improvement should reduce that risk.

Not increase it.

---

# Opportunistic Refactoring

Refactor code when:

- already modifying the surrounding area
- behaviour is well understood
- tests provide confidence
- architectural improvements are obvious

Avoid unrelated large-scale refactoring during feature development.

Keep changes cohesive.

---

# Incremental Improvement

Examples include:

Before:

```go
func Do(a string, b int) {}
```

After:

```go
func ProcessMedia(
    mediaID string,
    retryCount int,
) {}
```

Behaviour has not changed.

Understanding has improved.

---

Another example.

Before:

```go
if err != nil {

    return err
}
```

Repeated dozens of times.

After:

Shared behaviour extracted into a focused helper where doing so genuinely improves readability.

Reduce duplication carefully.

Not mechanically.

---

# Naming Is Architecture

One of the highest value improvements an engineer can make is improving names.

Good names reduce documentation.

Good names reduce bugs.

Good names reduce onboarding time.

If a clearer name is discovered while modifying code, it SHOULD be adopted where practical.

---

# Delete Code

Deleting unnecessary code is one of the most valuable forms of improvement.

Dead code:

- increases maintenance cost
- confuses readers
- expands testing surface
- slows refactoring

Unused code SHOULD be removed.

Version control remembers history.

The repository does not need to.

---

# Remove Duplication Carefully

Duplication is not automatically bad.

Sometimes duplication improves clarity.

Extract shared behaviour only when:

- duplication represents the same concept
- abstraction simplifies the design
- future changes become easier

Do not abstract merely because two functions appear similar.

---

# Improve Documentation

Whenever behaviour becomes clearer, documentation should evolve alongside it.

Examples include:

- package comments
- exported API documentation
- ADRs
- architecture specifications
- README updates

Code and documentation should describe the same system.

Documentation drift is technical debt.

---

# Improve Tests

Every modification should consider testing.

Examples:

- additional edge case
- improved assertions
- removal of duplicate tests
- clearer fixtures
- improved test names

Tests are first-class engineering artefacts.

They deserve the same attention as production code.

---

# Respect Existing Style

Improvement should move software towards consistency.

Not personal preference.

Follow:

- existing repository conventions
- Go conventions
- MEG standards

The objective is a coherent codebase.

Not individual expression.

---

# Know When To Stop

The Boy Scout Rule encourages improvement.

It does not encourage perfectionism.

If a refactoring begins expanding beyond the original scope, stop.

Consider:

- separate pull request
- ADR
- future engineering task

Small improvements are sustainable because they remain small.

---

# Engineering Ownership

Every engineer shares responsibility for the quality of the codebase.

Ownership does not end at package boundaries.

If improvement is obvious and safe, it should be made.

The codebase belongs to the team.

Not individual authors.

---

# Examples

## Good

```
Implement feature

↓

Rename confusing variable

↓

Add missing test

↓

Improve package comment
```

---

## Better

```
Implement feature

↓

Simplify control flow

↓

Remove duplication

↓

Improve logging

↓

Update documentation

↓

Add benchmark
```

---

## Poor

```
Implement feature

↓

Ignore obvious problems

↓

Leave dead code

↓

Introduce more duplication
```

Technical debt rarely arrives dramatically.

It accumulates quietly.

---

# Engineering Mindset

The Boy Scout Rule encourages engineers to ask one simple question before every commit.

> **"Is this repository better than it was before I started?"**

The improvement does not need to be large.

It simply needs to be genuine.

---

# Mosaic Guidelines

Within Mosaic:

- Every pull request SHOULD improve the surrounding code where practical.
- Naming SHOULD become clearer over time.
- Dead code SHOULD be removed.
- Documentation SHOULD evolve alongside implementation.
- Tests SHOULD improve continuously.
- Refactoring SHOULD remain incremental.
- Engineers SHOULD optimise for the long-term health of the repository.
- Large rewrites SHOULD be avoided unless architecturally justified.

---

# Relationship to the MEG

The Boy Scout Rule is not another engineering principle.

It is the mechanism through which every other principle remains effective over time.

Without continuous improvement:

- architecture drifts
- consistency erodes
- complexity accumulates
- technical debt compounds

With continuous improvement:

- software remains understandable
- standards remain enforceable
- onboarding becomes easier
- refactoring becomes cheaper

The Boy Scout Rule transforms engineering quality from a periodic activity into a daily habit.

---

# Summary

Every engineer leaves a mark on a codebase.

Within Mosaic, that mark should always be positive.

No change is too small to improve something.

The cumulative effect of thousands of small improvements is a platform that remains maintainable, understandable and enjoyable to work on for many years.

That is the true objective of the Boy Scout Rule.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`15-code-review-standards.md`

**Next File**

`17-adrs.md`
