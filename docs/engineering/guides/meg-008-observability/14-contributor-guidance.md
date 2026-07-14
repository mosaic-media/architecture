<!--
File: docs/engineering/guides/meg-008-observability/14-contributor-guidance.md
Document: MEG-008
Status: Draft
Version: 0.4
-->

# Contributor Guidance

> *Every new architectural responsibility should introduce corresponding observability. If it cannot be observed, it does not yet fully exist.*

---

# Purpose

The Mosaic platform has been designed around explicit architectural ownership.

Every Runtime Service.

Every Capability.

Every Repository.

Every Storage System.

Owns one responsibility.

The same principle applies to observability.

This document provides practical guidance for engineers implementing new Runtime components and capabilities while preserving the observability architecture defined throughout MEG-008.

---

# Philosophy

Within Mosaic:

> **Build observability alongside the architecture. Never afterwards.**

Observability should emerge naturally during implementation.

Retrofitting telemetry usually produces:

- inconsistent naming
- missing context
- duplicated metrics
- incomplete traces

The easiest observability to maintain is the observability that was designed from the beginning.

---

# Before Writing Code

Before implementing a new component ask:

- Who owns this responsibility?
- How will operators know it exists?
- How will operators know it failed?
- How will operators measure it?
- How will operators debug it?

If these questions cannot be answered:

Continue designing.

Implementation should wait.

---

# Before Adding Logs

Ask:

> **Is this an architectural event?**

Good examples include:

- Capability Activated
- Worker Replaced
- Dependency Resolution Failed
- Storage Migration Completed

Poor examples include:

- Entered function
- Variable changed
- Loop iteration

Logs should describe significant architectural events.

Not implementation mechanics.

---

# Before Adding Metrics

Ask:

> **Does this measurement describe long-term behaviour?**

Good:

- execution latency
- worker utilisation
- queue depth
- storage growth

Poor:

- local variable values
- helper function timing
- temporary counters

Metrics should describe behaviour over time.

Not transient implementation state.

---

# Before Creating A Span

Create spans around architectural boundaries.

Examples.

```mermaid
flowchart TD

N1["Runtime Service"]
N2["Capability"]
N3["Repository"]
N4["Storage"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Avoid tracing:

- utility functions
- formatting
- validation helpers

Traces should explain journeys.

Not implementation.

---

# Before Adding Health

Health should answer one question.

> **Can this component currently fulfil its responsibility?**

Avoid health endpoints that report:

- feature completeness
- business correctness
- implementation status

Health remains an operational concern.

---

# Before Adding Diagnostics

Diagnostics should expose:

- ownership
- relationships
- configuration
- lifecycle
- dependencies

Avoid exposing:

- implementation classes
- internal data structures
- temporary debugging information

Diagnostics explain architecture.

They do not replace documentation.

---

# Before Creating Alerts

Ask:

> **Does this genuinely require human intervention?**

If automatic recovery is possible:

Do not alert.

Examples that rarely require alerts:

- worker replacement
- cache rebuild
- retry scheduled

Examples that frequently do:

- PostgreSQL unavailable
- dependency graph invalid
- startup failed

Humans should solve exceptional problems.

The Runtime should solve routine ones.

---

# Before Exporting Telemetry

Remember:

OpenTelemetry transports telemetry.

It does not define it.

The Runtime should continue owning:

- telemetry semantics
- ownership
- context

Export should remain an infrastructure concern.

---

# Before Naming Metrics

Metric names should describe:

- owner
- responsibility
- measurement

Examples.

```text
runtime_workers_active
```

```text
capability_execution_duration_seconds
```

```text
storage_blob_usage_bytes
```

Names should remain stable.

Dashboards should survive implementation refactoring.

---

# Before Logging Sensitive Data

Never log:

- passwords
- API keys
- OAuth tokens
- session tokens
- encryption keys
- personally identifiable information

Observability should increase operational understanding.

Not operational risk.

---

# Before Requesting Review

Every observability contribution SHOULD satisfy the following checklist.

## Ownership

- [ ] Architectural owner identified.
- [ ] Telemetry follows ownership.
- [ ] Responsibilities remain clear.

---

## Logging

- [ ] Structured logs.
- [ ] Meaningful architectural events.
- [ ] Context included.

---

## Metrics

- [ ] Appropriate metric type selected.
- [ ] Stable naming.
- [ ] Explicit units.

---

## Tracing

- [ ] Trace context propagated.
- [ ] Architectural spans.
- [ ] Low-cardinality attributes.

---

## Health

- [ ] Readiness correct.
- [ ] Health meaningful.
- [ ] Dependencies reflected.

---

## Diagnostics

- [ ] Runtime explainability improved.
- [ ] Sensitive information redacted.
- [ ] Read-only behaviour preserved.

---

## Documentation

- [ ] MEG updated if required.
- [ ] Metric names documented.
- [ ] Health semantics documented.
- [ ] Diagnostic endpoints documented.

---

# Recognising Observability Drift

The following symptoms usually indicate architectural drift.

- Runtime Services sharing telemetry ownership.
- Duplicate metrics.
- Free-form logs.
- Missing trace propagation.
- Alerts without ownership.
- Diagnostics exposing implementation details.
- Runtime behaviour requiring manual debugging.

Observability drift should be corrected early.

It compounds surprisingly quickly.

---

# Refactoring Observability

When improving telemetry ask:

- Can ownership become clearer?
- Can metrics become architectural?
- Can spans become fewer but more meaningful?
- Can diagnostics explain more with less?
- Can alerts become quieter?

Observability refactoring should improve understanding.

Not simply increase telemetry volume.

---

# Review Mindset

Observability reviews should focus upon:

- ownership
- consistency
- explainability
- operational usefulness
- implementation independence

Questions such as:

> **Will an operator immediately understand this?**

are generally more valuable than:

> **Does this produce another metric?**

The objective is understanding.

Not quantity.

---

# Learning The Observability Architecture

New contributors SHOULD study MEG-008 in the following order.

```mermaid
flowchart TD

N1["Observability Philosophy"]
N2["Logging"]
N3["Metrics"]
N4["Tracing"]
N5["Health"]
N6["Diagnostics"]
N7["Alerting"]
N8["OpenTelemetry"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Understanding ownership first makes every later observability concept significantly easier.

---

# Engineering Culture

Observability contributors should strive to:

- simplify telemetry
- reduce duplication
- improve architectural clarity
- preserve Runtime ownership
- expose meaningful behaviour
- remove operational ambiguity

The platform should become easier to operate with every release.

Not noisier.

---

# Contributor Checklist

Before requesting review, confirm:

- [ ] Observability follows architectural ownership.
- [ ] Logs describe architectural events.
- [ ] Metrics describe trends.
- [ ] Traces describe execution journeys.
- [ ] Health reflects operational readiness.
- [ ] Diagnostics explain architecture.
- [ ] Sensitive information remains protected.
- [ ] Operators understand the component without reading source code.
- [ ] The platform is more explainable than before.

---

# Relationship to MEG

This document explains how contributors should evolve the Observability Architecture established throughout MEG-008.

The previous chapters define:

> **How the platform explains itself.**

This chapter defines:

> **How engineers preserve that explainability over time.**

Observability survives because contributors consistently reinforce architectural ownership rather than treating telemetry as an afterthought.

---

# Summary

Observability is successful when operators spend less time asking questions.

Every new Runtime component should naturally explain:

- what it owns
- what it is doing
- why it failed
- how it recovered

Within Mosaic, observability should emerge from architecture itself.

The clearer the architecture becomes, the easier the platform becomes to operate.
