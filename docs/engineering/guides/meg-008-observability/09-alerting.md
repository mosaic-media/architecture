<!--
File: engineering/meg/MEG-008 Observability/09-alerting.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Alerting

> *The purpose of alerting is not to report every failure. It is to notify humans only when human intervention is genuinely required.*

---

# Purpose

Logs.

Metrics.

Traces.

Diagnostics.

Health.

These systems collectively describe the behaviour of the platform.

Alerting decides when that behaviour requires operator attention.

Poor alerting produces:

- alert fatigue
- ignored notifications
- operational blindness

Good alerting produces:

- rapid awareness
- actionable information
- minimal noise

This document defines the alerting architecture of the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Alert people. Never alert systems.**

Automation should resolve:

- retries
- cache rebuilds
- worker replacement
- temporary failures

Operators should only receive alerts when:

- automation cannot recover
- business correctness is threatened
- platform availability is at risk

Alerting should remain the final step of operational escalation.

---

# Alerting Hierarchy

Alerting follows the Runtime Architecture.

```text
Platform

↓

Runtime

↓

Capabilities

↓

Storage

↓

Infrastructure
```

Each architectural layer may generate alerts.

Platform alerts should emerge naturally from lower-level conditions.

---

# Alert Lifecycle

Every alert progresses through the same lifecycle.

```text
Detected

↓

Validated

↓

Raised

↓

Acknowledged

↓

Resolved

↓

Closed
```

Each stage owns one operational responsibility.

Alerts should never disappear silently.

---

# Detection

Alerts originate from observable evidence.

Examples include:

- metrics
- health
- traces
- diagnostics

Logs alone should rarely trigger alerts.

Logs explain events.

Metrics and health indicate operational significance.

---

# Validation

Before raising an alert, the Runtime SHOULD determine:

- Is the condition persistent?
- Is automatic recovery already occurring?
- Is the signal reliable?

Transient failures should generally not generate alerts.

The Runtime should distinguish:

```
Temporary Failure
```

from

```
Operational Incident
```

---

# Severity Levels

Every alert SHOULD declare severity.

```text
Information
```

Operator awareness only.

```text
Warning
```

Reduced capability.

```text
Critical
```

Business impact imminent or occurring.

```text
Emergency
```

Platform cannot safely continue.

Severity should reflect:

Operational impact.

Not implementation difficulty.

---

# Runtime Alerts

The Runtime SHOULD generate alerts for:

- startup failure
- dependency failure
- worker exhaustion
- scheduler failure
- execution backlog
- resource exhaustion

These alerts describe platform operation.

Not business behaviour.

---

# Capability Alerts

Capabilities SHOULD generate alerts only when:

- business functionality becomes unavailable
- required dependencies remain unavailable
- automated recovery fails

Capabilities SHOULD NOT alert for:

- transient retries
- expected validation failures
- routine lifecycle transitions

Capabilities own business availability.

The Runtime owns infrastructure availability.

---

# Storage Alerts

Storage alerts SHOULD focus upon:

- PostgreSQL unavailable
- storage corruption
- backup failure
- restore failure
- blob integrity failure
- storage exhaustion

Derived storage should generally not produce critical alerts.

Examples include:

- cache rebuild
- analytical refresh

Business information always takes precedence.

---

# Resource Alerts

Resource Manager SHOULD generate alerts for:

- worker exhaustion
- memory pressure
- queue saturation
- connection exhaustion

Resource alerts indicate that platform capacity is approaching operational limits.

These alerts should encourage proactive intervention.

Not reactive firefighting.

---

# Dependency Alerts

The Runtime SHOULD alert when:

- required capability unavailable
- dependency graph invalid
- version incompatibility
- activation failure

Dependency problems frequently prevent business capabilities from executing correctly.

They deserve architectural visibility.

---

# Recovery Awareness

Automatic recovery SHOULD suppress unnecessary alerts.

Example.

```text
Worker Failure

↓

Replacement

↓

Recovered
```

The operator may receive:

```
Information
```

rather than:

```
Critical
```

Recovery is often more important than the failure itself.

Alerting should recognise successful recovery.

---

# Alert Correlation

Related failures SHOULD produce one alert.

Poor.

```text
50 Worker Alerts
```

Preferred.

```text
Worker Pool Exhausted
```

Alert correlation reduces operational noise.

Operators should investigate architectural failures.

Not individual symptoms.

---

# Alert Context

Every alert SHOULD include:

- affected component
- severity
- detection time
- architectural owner
- probable cause
- suggested action

Example.

```text
Scheduler

↓

Critical

↓

Queue Saturated

↓

Increase Worker Capacity
```

Alerts should explain themselves.

Operators should not require source code.

---

# Alert Routing

Alerts MAY be routed according to ownership.

Examples.

```text
Storage

↓

Storage Team
```

```text
Runtime

↓

Platform Team
```

```text
Capability

↓

Capability Owner
```

Routing should reinforce architectural ownership.

Not organisational convenience.

---

# Escalation

Escalation SHOULD occur only after:

- retry
- recovery
- validation

have failed.

Humans should remain the final recovery mechanism.

Not the first.

---

# Alert Suppression

The Runtime SHOULD suppress:

- duplicate alerts
- cascading failures
- repeated notifications

Suppression prevents:

- operator fatigue
- alert storms
- unnecessary escalation

Operators should receive:

One meaningful alert.

Not hundreds of symptoms.

---

# Maintenance Windows

Alerting SHOULD support maintenance mode.

During planned maintenance:

- expected shutdown
- migrations
- upgrades

should not generate unnecessary alerts.

Maintenance should remain observable.

It should not resemble failure.

---

# Historical Alerts

Resolved alerts SHOULD remain queryable.

Historical information supports:

- incident reviews
- trend analysis
- architectural improvements

Alerts should contribute to long-term platform learning.

Not disappear after resolution.

---

# Alerting And Health

Health determines:

```
Degraded
```

Alerting determines:

```
Operator Required
```

Not every unhealthy component deserves an alert.

The Runtime should distinguish between:

Operational state.

and

Operational intervention.

---

# Performance

Alert evaluation SHOULD remain inexpensive.

Avoid:

- expensive analytical queries
- complex correlation rules
- excessive polling

The Runtime should spend more time executing capabilities than evaluating alerts.

---

# Anti-Patterns

The following practices are prohibited.

## Alerting On Every Error

Treating every log entry as an alert.

---

## Duplicate Alerts

Multiple Runtime Services raising the same incident independently.

---

## Alert Storms

Flooding operators during cascading failures.

---

## Missing Context

Alerts without ownership or probable cause.

---

## Permanent Critical

Components remaining in a critical state without escalation or resolution.

---

## Manual Correlation

Operators required to correlate dozens of related alerts manually.

---

# Mosaic Guidelines

Within Mosaic:

- Alerts MUST follow architectural ownership.
- Automatic recovery SHOULD occur before operator notification.
- Related failures SHOULD produce correlated alerts.
- Alert severity MUST reflect operational impact.
- Alert context MUST remain actionable.
- Health MUST remain distinct from alerting.
- Duplicate alerts SHOULD be suppressed.
- Historical alerts SHOULD remain available for analysis.

---

# Relationship to MEG

Performance Telemetry explains:

> **How efficiently the platform is operating.**

Alerting explains:

> **When operational behaviour requires human intervention.**

The next chapter introduces **Debugging**, defining how Mosaic exposes safe, deterministic debugging capabilities without compromising Runtime stability or production reliability.

---

# Summary

Alerting is not about making noise.

It is about making good decisions.

Within Mosaic, alerts should represent:

- meaningful operational risk
- architectural failures
- unrecoverable conditions

Everything else should be handled automatically by the Runtime.

Because the best operational platform is one that solves most of its own problems before anyone's phone starts vibrating at three in the morning.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`08-performance-telemetry.md`

**Next File**

`10-debugging.md`
