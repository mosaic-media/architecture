<!--
File: docs/engineering/guides/meg-001-go-engineering-standards/10-concurrency.md
Document: MEG-001
Status: Draft
-->

# Concurrency

> *Concurrency is about structuring software to perform multiple tasks independently. Parallelism is merely one possible outcome.*

---

# Purpose

Concurrency is one of Go's defining strengths.

It allows software to perform multiple independent operations without blocking overall progress.

Within Mosaic, concurrency underpins almost every major subsystem.

Examples include:

- Metadata ingestion
- Event processing
- Background indexing
- Cache refresh
- Playback monitoring
- Scheduler execution
- Blob synchronisation
- Docker orchestration
- Module communication

For this reason, concurrency is considered an architectural concern rather than merely a language feature.

---

# Philosophy

Within Mosaic:

> **Concurrency exists to improve responsiveness, not complexity.**

Every goroutine introduces:

- another execution path
- another lifecycle
- another failure mode
- another debugging challenge

Concurrency should therefore be introduced deliberately.

Not automatically.

---

# Concurrency vs Parallelism

These terms are frequently confused.

They describe different concepts.

| Concurrency | Parallelism |
|-------------|-------------|
| Structuring independent work | Executing work simultaneously |
| Improves responsiveness | Improves throughput |
| Language concern | Hardware concern |

A concurrent application is not necessarily parallel.

A parallel application is usually concurrent.

Go provides excellent support for both.

---

# When To Use Concurrency

Concurrency SHOULD be introduced when:

- waiting on I/O
- independent work can proceed simultaneously
- latency can be reduced
- responsiveness improves
- background processing is appropriate

Examples include:

```

Metadata Lookup

+

Artwork Download

+

Subtitle Discovery
```

These operations do not depend upon one another.

Running them concurrently improves overall response time.

---

# When Not To Use Concurrency

Concurrency SHOULD NOT be introduced when:

- operations are dependent
- work is CPU trivial
- sequential execution is easier to understand
- added complexity outweighs performance gains

Poor:

```mermaid
flowchart TD

N1["Validate"]
N2["Spawn Goroutine"]
N3["Wait"]
N4["Continue"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Nothing has been gained.

Sequential execution is clearer.

---

# Goroutine Ownership

Every goroutine MUST have a clearly defined owner.

Ownership answers:

- Who started it?
- Who stops it?
- Who waits for it?
- Who handles failures?
- Who cleans up resources?

If these questions cannot be answered, the goroutine should not exist.

---

# Goroutine Lifecycle

Every goroutine should follow the same lifecycle.

```mermaid
flowchart TD

N1["Created"]
N2["Running"]
N3["Cancellation Requested"]
N4["Cleanup"]
N5["Exit"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

No goroutine should run indefinitely without an explicit architectural reason.

---

# Never Fire And Forget

The following is prohibited.

```go
go process()
```

without:

- lifecycle management
- cancellation
- error handling
- ownership

Every goroutine should be observable.

If work is important enough to execute, it is important enough to manage.

---

# Use errgroup For Related Work

When multiple goroutines contribute towards a single operation, `errgroup` SHOULD be preferred.

Example:

```mermaid
flowchart TD

N1["Metadata"]
N2["Artwork"]
N3["Subtitles"]
N4["Combined Result"]

N1 --> N4
N2 --> N4
N3 --> N4
```

Benefits include:

- automatic cancellation
- error propagation
- coordinated completion

This is simpler than manually coordinating channels and wait groups.

The `errgroup` package is widely recommended for managing groups of related goroutines. ([pkg.go.dev](https://pkg.go.dev/golang.org/x/sync/errgroup))

---

# Worker Pools

Repeated background work SHOULD use worker pools.

Example:

```mermaid
flowchart TD

N1["Queue"]
N2["Worker 1"]
N3["Worker 2"]
N4["Worker 3"]
N5["Completed Tasks"]

N1 --> N2
N1 --> N3
N1 --> N4
N2 --> N5
N3 --> N5
N4 --> N5
```

Worker pools provide:

- predictable resource usage
- backpressure
- easier monitoring
- bounded concurrency

Creating thousands of goroutines for identical work should generally be avoided.

---

# Channels

Channels communicate ownership.

They are not simply queues.

Before introducing a channel ask:

> Does another goroutine genuinely need to communicate?

If not, a normal function call is probably sufficient.

Channels should communicate:

- work
- completion
- cancellation
- events

They should not replace normal data structures.

---

# Channel Direction

Whenever practical, channel direction SHOULD be specified.

Example:

```go
func Publish(events chan<- Event)
```

```go
func Consume(events <-chan Event)
```

Directional channels communicate intent.

The compiler prevents accidental misuse.

---

# Buffered Channels

Buffered channels should have a clearly documented purpose.

Good reasons include:

- absorbing bursts
- smoothing producer / consumer rates
- bounded queues

Poor reason:

```

It fixed a deadlock.
```

Buffer size is an architectural decision.

Not a debugging tool.

---

# Closing Channels

Only the sender closes a channel.

Receivers MUST NOT close channels they do not own.

Closing communicates:

> No more values will ever be sent.

It is not a signal that processing has completed.

---

# Select Statements

Long-running goroutines SHOULD use `select`.

Example:

```go
select {

case <-ctx.Done():

case event := <-events:
}
```

This allows:

- cancellation
- responsiveness
- graceful shutdown

Ignoring `ctx.Done()` in long-running loops is prohibited.

---

# Shared Memory

Go encourages communicating through channels.

However:

Mutexes are entirely appropriate when protecting shared state.

Do not force channel-based designs where simple locking is clearer.

The Go proverb "Do not communicate by sharing memory; instead, share memory by communicating" is guidance rather than an absolute rule. Simpler synchronisation mechanisms should be chosen where they better fit the problem. ([go.dev](https://go.dev/blog/share-memory-by-communicating))

---

# Mutexes

A mutex protects ownership of mutable state.

Example:

```mermaid
flowchart TD

N1["Cache"]
N2["Mutex"]
N3["Read"]
N4["Write"]

N1 --> N2
N2 --> N3
N2 --> N4
```

Mutexes SHOULD remain private.

Callers should never need to understand locking behaviour.

---

# RWMutex

`sync.RWMutex` SHOULD only be introduced when measurements demonstrate significant read contention.

It is not automatically faster than `sync.Mutex`.

Additional complexity requires measurable benefit.

---

# Atomics

Atomic operations SHOULD be reserved for:

- counters
- flags
- metrics
- simple state transitions

If multiple values must remain consistent together, prefer a mutex.

---

# Backpressure

Every concurrent pipeline should have a strategy for overload.

Examples include:

- bounded queues
- worker pools
- rate limiting
- request rejection

Unlimited buffering is prohibited.

Every queue should have a maximum capacity.

---

# Long Running Services

Long-running services should follow a common lifecycle.

```mermaid
flowchart TD

N1["Start"]
N2["Wait"]
N3["Process"]
N4["Cancellation"]
N5["Cleanup"]
N6["Exit"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Every service should honour context cancellation.

Shutdown should be graceful.

---

# Concurrency Patterns

Within Mosaic the following patterns are encouraged.

- Worker Pool
- Fan-Out / Fan-In
- Pipeline
- Event Loop
- Producer / Consumer
- Stale-While-Revalidate
- Background Scheduler

Future specifications explore each pattern individually.

---

# Anti-Patterns

The following practices are prohibited.

## Fire And Forget Goroutines

```go
go process()
```

with no ownership.

---

## Unbounded Goroutines

```

for {

go process()
}
```

---

## Ignoring Context

Long-running goroutines that never observe cancellation.

---

## Closing Someone Else's Channel

Receivers closing channels they did not create.

---

## Channels As Databases

Using channels to permanently store application state.

---

## Shared Mutable State Without Synchronisation

Concurrent access to mutable memory without:

- mutexes
- atomics
- channels

The race detector should never report data races in production code. Running tests with `-race` is an important part of validating concurrent programs. ([go.dev](https://go.dev/doc/articles/race_detector))

---

# Mosaic Guidelines

Within Mosaic:

- Every goroutine MUST have an owner.
- Every goroutine MUST honour cancellation.
- Fire-and-forget goroutines are prohibited.
- Worker pools SHOULD be used for repeated background work.
- `errgroup` SHOULD coordinate related concurrent tasks.
- Shared mutable state MUST be synchronised.
- Queues MUST be bounded.
- Shutdown MUST be graceful.

Concurrency should reduce waiting.

It should never reduce understanding.

---

# Summary

Concurrency is one of Go's greatest strengths.

It is also one of its easiest features to misuse.

Within Mosaic, concurrency is considered successful when:

- ownership is obvious
- cancellation is respected
- resources are bounded
- shutdown is graceful
- debugging remains straightforward

A concurrent system should feel predictable.

Not mysterious.
