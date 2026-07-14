<!--
File: docs/engineering/guides/meg-005-runtime-architecture/11-shutdown.md
Document: MEG-005
Status: Draft
Version: 0.1
-->

# Shutdown

> *A Runtime should stop with the same discipline with which it starts. Shutdown is a lifecycle transition, not an emergency.*

---

# Purpose

Eventually every Runtime stops.

Reasons include:

- deployment
- maintenance
- upgrade
- configuration changes
- host shutdown
- scaling
- operator request

A controlled shutdown is one of the defining characteristics of a production-grade Runtime.

Within Mosaic, shutdown should be:

- deterministic
- observable
- graceful
- recoverable

Business correctness should always take priority over shutdown speed.

---

# Philosophy

Within Mosaic:

> **The Runtime should stop accepting new work before it stops existing work.**

Shutdown should never interrupt business behaviour unnecessarily.

Instead, the Runtime should transition through well-defined phases until every component has safely completed its responsibilities.

---

# Shutdown Goals

A successful shutdown should ensure:

- no new work admitted
- active work completes where practical
- resources released
- Runtime state preserved
- capabilities stopped safely
- observability maintained

No Runtime component should disappear without first participating in the shutdown lifecycle.

---

# Shutdown Sequence

Every Runtime follows the same shutdown sequence.

```
Shutdown Requested

↓

Cooldown

↓

Capability Drain

↓

Worker Drain

↓

Runtime Services Stop

↓

Resource Release

↓

Kernel Shutdown

↓

Process Exit
```

Each stage owns exactly one responsibility.

Shutdown order is the reverse of startup.

Graceful shutdown in distributed systems commonly follows this pattern: stop accepting new work, drain in-flight work, release resources and terminate cleanly.  [oai_citation:0‡GeeksforGeeks](https://www.geeksforgeeks.org/system-design/graceful-shutdown-in-distributed-systems-and-microservices/?utm_source=chatgpt.com)

---

# Stage 1 — Shutdown Requested

Shutdown begins when the Runtime receives:

- SIGTERM
- SIGINT
- administrator request
- orchestrator request
- maintenance request

The Runtime immediately transitions into:

```
Stopping
```

The Runtime Kernel now owns shutdown coordination.

---

# Stage 2 — Cooldown

The Runtime enters cooldown.

Cooldown means:

> **No new externally initiated work is accepted.**

Examples include:

- HTTP stops accepting requests
- schedulers stop creating work
- event consumers stop consuming
- extension entry points close

Existing work continues.

New work does not begin.

Cooldown is distinct from draining because it closes admission before attempting to complete in-flight work.  [oai_citation:1‡Reddit](https://www.reddit.com/r/node/comments/1s4x8gp/application_lifecycle_is_one_of_the_most_ignored/?utm_source=chatgpt.com)

---

# Stage 3 — Capability Drain

Capabilities finish existing business work.

Examples include:

- playback updates
- metadata imports
- library scans
- recommendation generation

Capabilities should receive:

```
Cancellation Requested
```

They decide:

How to leave business state consistent.

The Runtime never decides business correctness.

---

# Stage 4 — Worker Drain

Workers continue executing remaining Work Units.

```
Worker Pool

↓

Running Tasks

↓

Complete

↓

Idle
```

Workers should not begin executing newly admitted work.

Only already accepted work should continue.

---

# Stage 5 — Runtime Services

Once workers finish:

Runtime Services begin stopping.

Typical order.

```
Scheduler

↓

Execution Engine

↓

Worker Manager

↓

Capability Registry
```

Services stop according to the reverse dependency graph.

No service should outlive the services upon which it depends.

---

# Stage 6 — Resource Release

Resources are released.

Examples include:

- database pools
- blob storage
- HTTP servers
- timers
- worker pools
- network sockets

Every Runtime Service releases only the resources it owns.

Ownership determines cleanup responsibility.

---

# Stage 7 — Kernel Shutdown

Once every Runtime Service has terminated:

```
Runtime Kernel

↓

Shutdown Complete
```

The Kernel records final Runtime state before process termination.

At this point:

The Runtime no longer exists.

---

# Admission Control

The Runtime should distinguish between:

```
External Work
```

and

```
Internal Continuations
```

Example.

```
PlaybackCompleted

↓

RecommendationGenerated
```

This follow-up work may still execute during draining because it belongs to an already admitted workflow.

New user requests should not.

This distinction prevents partially completed business workflows while still allowing shutdown to complete predictably.  [oai_citation:2‡Reddit](https://www.reddit.com/r/node/comments/1s4x8gp/application_lifecycle_is_one_of_the_most_ignored/?utm_source=chatgpt.com)

---

# Shutdown Deadlines

Graceful shutdown SHOULD remain bounded.

Example.

```
Shutdown

↓

60 Second Budget

↓

Graceful Completion

↓

Forced Termination
```

The timeout should remain configurable.

Infinite shutdown is prohibited.

---

# Forced Shutdown

If graceful shutdown cannot complete within the configured deadline:

```
Timeout

↓

Forced Stop
```

Forced shutdown should remain exceptional.

The Runtime should make every reasonable attempt to:

- finish work
- persist state
- release resources

before termination.

---

# Capability Behaviour

Capabilities should respond to shutdown through lifecycle notifications.

They should never:

- intercept process signals
- stop Runtime Services
- terminate workers

Lifecycle remains owned by the Runtime Kernel.

---

# Scheduler Shutdown

The Scheduler should:

- stop accepting new schedules
- persist recurring schedules
- preserve delayed work
- stop dispatching executable work

Scheduled work should survive controlled restarts where appropriate.

---

# Execution Engine Shutdown

The Execution Engine should:

- reject new Work Units
- continue tracking active work
- report completion
- stop after all active execution ends

Execution should conclude before worker disposal begins.

---

# Worker Manager Shutdown

The Worker Manager should:

- stop allocating workers
- wait for active workers
- retire idle workers
- dispose worker pools

Worker disposal should occur only after execution completes.

---

# Capability Registry Shutdown

The Capability Registry should remain available until every capability has completed shutdown.

Only then should:

```
Capability Registry

↓

Disposed
```

Dependency information may still be required during shutdown coordination.

---

# Restart Recovery

Following restart:

```
Startup

↓

Recover Durable Runtime State

↓

Resume Scheduling

↓

Resume Execution
```

Recovery should depend upon persisted Runtime state.

Not on graceful shutdown always succeeding.

---

# Observability

Shutdown SHOULD produce Runtime Events.

Examples include:

```
RuntimeStopping
```

```
CooldownStarted
```

```
WorkerDraining
```

```
RuntimeStopped
```

Operators should always understand:

- current shutdown phase
- remaining work
- blocked services
- timeout progress

Shutdown should never appear silent.

---

# Health

During shutdown:

Health should transition:

```
Healthy

↓

Not Ready

↓

Stopping

↓

Stopped
```

The Runtime should become unavailable before terminating.

This prevents additional work from entering during shutdown.

---

# Testing

Shutdown SHOULD be tested explicitly.

Typical tests verify:

- cooldown
- draining
- dependency ordering
- timeout behaviour
- resource release
- restart recovery

Shutdown correctness is as important as startup correctness.

---

# Anti-Patterns

The following practices are prohibited.

## Immediate Exit

Calling:

```go
os.Exit(...)
```

without Runtime shutdown.

---

## New Work During Shutdown

Continuing to admit new Runtime work.

---

## Worker Termination

Killing workers before active work completes.

---

## Hidden Cleanup

Background goroutines performing undisclosed shutdown behaviour.

---

## Runtime-Owned Business Decisions

The Runtime deciding which business work should be abandoned.

---

## Silent Failure

Suppressing shutdown failures without observability.

---

# Mosaic Guidelines

Within Mosaic:

- Shutdown MUST remain deterministic.
- Cooldown MUST occur before draining.
- New work MUST NOT be admitted during shutdown.
- Existing work SHOULD complete where practical.
- Runtime Services MUST stop in reverse dependency order.
- Resources MUST be released by their owners.
- Shutdown MUST remain observable.
- Restart recovery MUST NOT depend upon graceful shutdown always succeeding.
- Business correctness MUST remain more important than shutdown speed.

---

# Relationship to MEG

Startup explains:

> **How the Runtime becomes operational.**

Shutdown explains:

> **How the Runtime safely ceases operation.**

Together they define the complete operational lifecycle of the Mosaic Runtime.

The next chapter introduces **Runtime State**, describing the operational information maintained by the Runtime throughout its lifetime.

---

# Summary

A mature Runtime is defined as much by how it stops as by how it starts.

Within Mosaic, shutdown is:

- deliberate
- observable
- dependency aware
- resource aware
- business safe

The Runtime should leave the platform in a predictable state regardless of whether shutdown occurs because of deployment, maintenance or failure.

That predictability is one of the defining characteristics of a reliable platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`10-startup.md`

**Next File**

`12-runtime-state.md`
