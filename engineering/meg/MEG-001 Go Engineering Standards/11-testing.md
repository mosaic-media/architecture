<!--
File: engineering/meg/MEG-001 Go Engineering Standards/11-testing.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Testing

> *Testing is not about proving software works. It is about proving software continues to work after change.*

---

# Purpose

Software that cannot be tested cannot be changed with confidence.

Within Mosaic, testing is considered an architectural responsibility rather than a development afterthought.

Well-designed software naturally becomes easy to test.

Poorly-designed software usually requires increasingly complex tests to compensate for architectural deficiencies.

This document defines the testing philosophy and standards for all Go code within the Mosaic ecosystem.

---

# Philosophy

Within Mosaic:

> **Design for testability, not test around poor design.**

When code becomes difficult to test, the first question should be:

> "Is the design wrong?"

Not:

> "How do we mock this?"

Difficult tests often indicate architectural problems rather than testing problems.

---

# The Testing Pyramid

Mosaic adopts the classic testing pyramid.

```
                End-to-End
             Integration Tests
                Unit Tests
```

The majority of tests should exist at the unit level.

Integration tests verify architectural boundaries.

End-to-end tests verify complete workflows.

Each level answers different questions.

---

# Test Responsibilities

| Test Type | Purpose |
|-----------|---------|
| Unit Test | Verify behaviour of one component |
| Integration Test | Verify collaboration between components |
| End-to-End Test | Verify complete user workflows |
| Benchmark | Measure performance |
| Race Test | Detect concurrency defects |

No single type of test replaces another.

---

# Unit Tests

Unit tests SHOULD:

- execute quickly
- remain deterministic
- avoid external services
- avoid network access
- avoid databases
- avoid shared state

A unit test should exercise one unit of behaviour.

Not an entire application.

---

# Integration Tests

Integration tests verify collaboration between components.

Examples include:

```
Repository

↓

PostgreSQL
```

```
Metadata

↓

DuckDB
```

```
HTTP

↓

Authentication

↓

Service

↓

Repository
```

Real infrastructure SHOULD be used whenever practical.

Mocking databases during integration testing defeats the purpose.

---

# End-to-End Tests

End-to-end tests exercise complete workflows.

Example:

```
HTTP Request

↓

Authentication

↓

Metadata

↓

Playback

↓

Database

↓

Response
```

These tests provide the highest confidence.

They also provide the highest maintenance cost.

They should therefore remain focused on critical user journeys.

---

# Test Behaviour

Tests MUST verify behaviour.

They SHOULD NOT verify implementation details.

Poor:

```
Did function A call function B?
```

Better:

```
Was the expected behaviour observed?
```

Implementation changes should rarely require test changes.

Behaviour changes should.

---

# Test Naming

Tests SHOULD describe behaviour.

Good:

```go
func TestLibraryReturnsMediaByID(t *testing.T)
```

Better:

```go
func TestFindReturnsNotFoundWhenMediaDoesNotExist(t *testing.T)
```

The test name should describe the expected outcome.

---

# Table-Driven Tests

Whenever multiple scenarios exercise identical behaviour, table-driven tests SHOULD be used.

Example:

```go
tests := []struct {
    name string
    input string
    expected error
}{
    ...
}
```

Benefits include:

- reduced duplication
- improved readability
- easier extension
- consistent structure

Table-driven testing is an established Go convention. ([go.dev](https://go.dev/wiki/TableDrivenTests?utm_source=chatgpt.com))

---

# Test Independence

Tests MUST NOT depend upon:

- execution order
- global state
- previous tests
- shared files
- shared databases

Every test should be executable independently.

Parallel execution should not change results.

---

# Avoid Over-Mocking

Mocks have value.

Over-mocking does not.

Poor:

```
HTTP

↓

Mock Service

↓

Mock Repository

↓

Mock Database

↓

Mock Cache
```

Nothing meaningful is being exercised.

Instead:

Mock only the dependency whose behaviour is irrelevant to the current test.

Everything else should remain real.

---

# Fakes Over Mocks

Where practical, prefer lightweight fake implementations.

Example:

```go
type FakeRepository struct {
    media map[string]Media
}
```

Fakes are often:

- easier to understand
- deterministic
- reusable
- maintenance friendly

Mock frameworks should not become architectural dependencies.

---

# Assertions

Assertions SHOULD verify observable behaviour.

Good:

```go
if got != expected {
    t.Fatalf(...)
}
```

Avoid unnecessary assertion libraries unless they clearly improve readability.

The standard library should remain sufficient for most tests.

---

# Golden Files

Golden files SHOULD be used when verifying:

- generated JSON
- generated Markdown
- templates
- rendered output
- API specifications

Golden files reduce duplication while making expected output easy to review.

Updates should always be intentional.

---

# Benchmarking

Performance assumptions MUST be validated through benchmarks.

Example:

```go
func BenchmarkParser(b *testing.B)
```

Benchmarks should measure:

- allocations
- throughput
- latency

Optimisation without measurement is prohibited.

---

# Race Detection

Every repository SHOULD regularly execute:

```
go test -race ./...
```

The race detector identifies concurrent access to shared memory before defects reach production.

Concurrent code without race testing should be considered incomplete. The Go race detector is specifically designed to uncover data races during testing. ([go.dev](https://go.dev/doc/articles/race_detector?utm_source=chatgpt.com))

---

# Coverage

Code coverage is an indicator.

It is not a goal.

100% coverage can still produce poor software.

Focus on:

- meaningful behaviour
- critical paths
- failure cases
- boundary conditions

Not percentages.

Coverage should support engineering judgement.

It should never replace it.

---

# What To Test

Prioritise testing:

- business rules
- edge cases
- failure scenarios
- concurrency
- validation
- event ordering
- state transitions

These areas provide the highest engineering value.

---

# What Not To Test

Avoid testing:

- trivial getters
- language features
- third-party libraries
- generated code
- implementation details

Trust the language.

Test your behaviour.

---

# Continuous Integration

Every pull request SHOULD execute:

```
Formatting

↓

Static Analysis

↓

Unit Tests

↓

Integration Tests

↓

Race Detector

↓

Benchmarks (optional)

↓

Build
```

No code should be merged without automated verification.

---

# Test Data

Test data SHOULD remain:

- local
- deterministic
- representative
- minimal

Large fixtures should only exist when they significantly improve readability.

---

# Anti-Patterns

The following practices are prohibited.

## Sleep-Based Tests

```go
time.Sleep(...)
```

Waiting should be synchronised explicitly.

---

## Testing Private Functions

Private functions should generally be exercised through exported behaviour.

Testing implementation details creates brittle tests.

---

## Shared Mutable Fixtures

Tests modifying shared state introduce hidden coupling.

---

## Mocking Everything

Over-mocking verifies architecture diagrams rather than software behaviour.

---

## Ignoring Failure Paths

Every meaningful failure path deserves at least one test.

Happy-path-only testing creates false confidence.

---

# Mosaic Guidelines

Within Mosaic:

- Behaviour MUST be tested.
- Unit tests SHOULD remain fast.
- Integration tests SHOULD use real infrastructure where practical.
- Table-driven tests SHOULD be preferred for repeated scenarios.
- Fakes SHOULD be preferred over complex mock frameworks.
- Race detection SHOULD be part of CI.
- Benchmarks SHOULD accompany performance-sensitive code.
- Coverage SHOULD inform discussion rather than drive development.

---

# Summary

Testing is a design activity.

Good tests emerge naturally from good architecture.

When testing becomes painful, engineers should first question the architecture rather than the testing framework.

Within Mosaic, software is considered complete only when its behaviour can be verified confidently and repeatedly through automated tests.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`10-concurrency.md`

**Next File**

`12-performance.md`
