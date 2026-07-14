<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/10-worker-lifecycle.md
Document: MEG-002
Status: Draft
Version: 0.3
-->

# Worker Lifecycle

> *Workers execute work. The runtime owns their lifecycle.*

---

# Purpose

Workers perform the asynchronous processing that powers the Mosaic Runtime.

Every background task, scheduled operation and event subscriber ultimately executes within one or more workers.

Workers are intentionally simple.

They do not own business behaviour.

They provide an execution environment in which business behaviour can safely run.

This document defines how workers are created, managed and terminated throughout the Mosaic Runtime.

---

# Philosophy

Within Mosaic:

> **Workers execute work. They never own it.**

Business capabilities decide **what** should happen.

The runtime decides **where**, **when** and **how** that work executes.

Separating execution from behaviour allows the runtime to evolve independently of business capabilities.

---

# Worker Responsibilities

Workers are responsible for:

- executing tasks
- respecting cancellation
- acknowledging completion
- reporting failures
- exposing health
- shutting down gracefully

Workers are **not** responsible for:

- scheduling work
- discovering work
- retry strategy
- orchestration
- business workflows

Those responsibilities belong elsewhere within the runtime.

---

# Worker Lifecycle

Every worker follows the same lifecycle.

```
Registered

↓

Initialised

↓

Started

↓

Waiting

↓

Processing

↓

Idle

↓

Stopping

↓

Stopped
```

The runtime manages every lifecycle transition.

Workers should never manage themselves.

---

# Startup

During runtime initialisation:

```
Runtime Starts

↓

Workers Created

↓

Dependencies Injected

↓

Subscriptions Registered

↓

Workers Started

↓

Ready
```

Workers should be fully initialised before accepting work.

A worker should never begin processing while partially configured.

---

# Idle State

Workers spend most of their lifetime waiting.

```
Waiting

↓

Task Arrives

↓

Process

↓

Waiting
```

Idle workers should consume minimal resources.

Busy waiting is prohibited.

Workers should block efficiently until work becomes available.

---

# Task Acquisition

Workers receive work from the runtime.

```
Runtime

↓

Queue

↓

Worker
```

Workers should never poll business capabilities directly.

The runtime owns work distribution.

This keeps execution infrastructure independent from business behaviour.

---

# One Task At A Time

Unless explicitly designed otherwise, a worker processes one task at a time.

```
Receive

↓

Process

↓

Complete

↓

Next Task
```

Parallelism is achieved by increasing worker count.

Not by increasing complexity inside individual workers.

---

# Cancellation

Every worker MUST honour context cancellation.

```
Task Running

↓

Shutdown Requested

↓

Context Cancelled

↓

Cleanup

↓

Exit
```

Workers should terminate promptly.

Long-running operations should periodically check:

```go
ctx.Done()
```

Ignoring cancellation is prohibited.

---

# Graceful Shutdown

Shutdown should always be graceful.

```
Stop Accepting Work

↓

Finish Current Task

↓

Acknowledge

↓

Cleanup

↓

Exit
```

Workers should never abandon partially completed business operations unless immediate termination is unavoidable.

Graceful shutdown improves consistency and reduces unnecessary retries.

---

# Worker Ownership

Every worker has exactly one owner.

Typically:

```
Runtime

↓

Worker Pool

↓

Worker
```

Ownership answers:

- Who started this worker?
- Who stops it?
- Who monitors it?
- Who replaces it?

Workers should never exist without a clearly defined owner.

---

# Worker Identity

Every worker SHOULD have a unique runtime identifier.

Example.

```
Metadata Worker #3
```

Worker identity improves:

- observability
- diagnostics
- tracing
- metrics

Business capabilities should remain unaware of worker identity.

Worker identity belongs to runtime infrastructure.

---

# Failure Handling

Worker failure should affect only the current task.

```
Worker

↓

Task Failure

↓

Report

↓

Retry Scheduled

↓

Continue Processing
```

The runtime should recover automatically wherever possible.

A single task failure should not terminate the worker.

---

# Panic Recovery

Workers SHOULD recover from unexpected panics.

Recovery should:

- log diagnostic information
- mark the task as failed
- clean up resources
- continue serving future work

The runtime should remain resilient to isolated programming errors.

Panic recovery belongs at execution boundaries rather than within business logic.

---

# Long Running Tasks

Some tasks naturally require extended execution.

Examples include:

- library scanning
- metadata synchronisation
- artwork generation
- cache rebuilding

These tasks should:

- expose progress
- honour cancellation
- checkpoint where practical

Workers should remain observable throughout execution.

---

# Concurrency

Worker concurrency should be controlled by the runtime.

Example.

```
Queue

↓

Worker Pool

↓

Workers

↓

Results
```

Capabilities should never create arbitrary worker pools independently.

Runtime-managed execution keeps concurrency predictable.

---

# Resource Ownership

Workers may temporarily own resources such as:

- database transactions
- file handles
- network connections

Workers MUST release every acquired resource before completing.

Resource ownership ends with task completion.

---

# Worker Health

Every worker SHOULD expose runtime health.

Examples include:

- current state
- active task
- processing duration
- restart count
- failure count

Health information enables operators to diagnose runtime behaviour quickly.

---

# Worker Pools

Workers SHOULD execute within managed pools.

Benefits include:

- bounded concurrency
- predictable resource usage
- simplified scheduling
- easier monitoring

Worker pools are discussed further in future runtime specifications.

---

# Scaling

Scaling should occur by increasing workers.

Not by making workers more complex.

Preferred.

```
1 Task

↓

Many Simple Workers
```

Avoid.

```
1 Worker

↓

Complex Internal Scheduling
```

Simple workers are easier to understand and easier to replace.

---

# Task Completion

Every completed task ends in one of four states.

```
Completed

Failed

Cancelled

Dead Letter
```

No task should disappear silently.

Every outcome should be observable.

---

# Restart Behaviour

Workers SHOULD be restartable without affecting business correctness.

Because:

- business state belongs elsewhere
- events are immutable
- subscribers are idempotent

Restarting a worker should simply continue processing available work.

This property significantly improves operational resilience.

---

# Worker Metrics

Every worker SHOULD expose:

- tasks processed
- task duration
- queue wait time
- failures
- retries
- cancellations
- utilisation

Worker metrics provide insight into runtime capacity and bottlenecks.

---

# Anti-Patterns

The following practices are prohibited.

## Self-Managing Workers

Workers creating or destroying other workers.

---

## Hidden Goroutines

Workers spawning unmanaged background goroutines.

---

## Ignoring Cancellation

Workers continuing indefinitely after shutdown begins.

---

## Infinite Loops Without Blocking

Workers consuming CPU while waiting for work.

---

## Business Scheduling

Workers deciding when future work should execute.

Scheduling belongs to the runtime.

---

## Permanent Mutable State

Workers retaining business state between tasks.

Business state belongs to capabilities.

---

# Mosaic Guidelines

Within Mosaic:

- Workers MUST remain execution infrastructure.
- Workers MUST honour cancellation.
- Workers MUST release acquired resources.
- Workers SHOULD process one task at a time.
- Worker pools SHOULD be runtime managed.
- Workers MUST expose health and metrics.
- Workers MUST recover gracefully from unexpected failures.
- Workers MUST remain stateless wherever practical.
- Every worker MUST have a clearly defined owner.

---

# Summary

Workers are the execution engine of the Mosaic Runtime.

They provide a predictable, observable and resilient environment in which business behaviour executes.

By separating execution from business logic, the runtime gains the freedom to:

- scale independently
- recover automatically
- evolve scheduling strategies
- improve observability
- optimise resource usage

Business capabilities remain focused on business behaviour.

The runtime remains focused on execution.

That separation is one of the key architectural principles underpinning the Mosaic platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`09-subscribers.md`

**Next File**

`11-scheduling.md`
