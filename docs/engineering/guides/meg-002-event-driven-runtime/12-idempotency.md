<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/12-idempotency.md
Document: MEG-002
Status: Draft
-->

# Idempotency

> *Every event should be safe to process more than once. Correctness should never depend upon perfect delivery.*

---

# Purpose

The Mosaic Runtime guarantees **at-least-once delivery**, which means every subscriber must assume an event may be delivered:

- once
- multiple times
- after a delay
- after a retry
- during replay

Without idempotency, duplicate delivery produces duplicate side effects. This document therefore defines how capabilities ensure repeated event processing always converges on the same final state.

---

# Philosophy

Within Mosaic:

> **Processing an event twice should produce the same final business state as processing it once.**

Idempotency is not an optimisation.

It is a fundamental property of every event subscriber, because correctness must never depend upon receiving an event exactly once.

---

# Why Idempotency Exists

Consider a `media.imported` event delivered to a Metadata Subscriber that writes to a Metadata Database. Suppose the subscriber:

- downloads metadata
- stores metadata
- crashes before acknowledging the event

The runtime retries. Without idempotency the subscriber downloads and stores, and then downloads and stores a second time, producing duplicate work and potentially duplicate state.

Idempotency prevents this.

---

# At-Least-Once Delivery

The Mosaic Runtime deliberately provides a model in which an event is published, delivered one or more times, and then acknowledged, rather than one in which it is delivered exactly once. Exactly-once delivery generally requires distributed coordination between the event bus, storage engine and subscriber, introducing significant complexity. Mosaic instead adopts the more common architectural approach of at-least-once delivery with idempotent consumers. ([microservices.io](https://microservices.io/post/microservices/patterns/2020/10/16/idempotent-consumer.html))

---

# Idempotent Behaviour

An operation is idempotent when executing it leaves the system in State A, and executing it again leaves the system in State A. The final state remains identical, so repeated execution produces no additional business effect.

---

# Business State

Idempotency concerns business state rather than implementation. A poor statement of the property describes the handler — that the handler executed twice — whereas a good one describes the business outcome, that the library contains one media item. The implementation may execute multiple times, but the business result should remain correct.

---

# Event Identity

Every event contains a unique Event ID, and subscribers should use this identifier when determining whether work has already been completed. On receiving an event a subscriber asks whether that Event ID has been seen before; if the answer is yes it ignores the event, and if the answer is no it processes the event and then records the Event ID.

The Event ID represents one occurrence of a business fact.

---

# Natural Idempotency

Some operations are naturally idempotent. Setting Status = Completed is one such operation, because running it repeatedly still produces Completed and no additional work occurs.

Prefer naturally idempotent business operations wherever practical.

---

# Artificial Idempotency

Other operations require explicit tracking, because they have no naturally convergent result. Sending an email is the clearest example: running it twice sends two emails. Such a subscriber must instead receive the event, ask whether the email has already been sent, send it only where it has not, and record completion afterwards. Artificial idempotency introduces explicit duplicate detection.

---

# Business Keys

Sometimes Event IDs are insufficient, because the identity that matters belongs to the business rather than to the delivery — a Library entry keyed by Media ID rather than by the event that announced it. If only one metadata record should ever exist per media item, the subscriber can take the Media ID, ask whether metadata exists, and skip the work where it does.

Business identifiers frequently provide stronger guarantees than event identifiers alone.

---

# Database Constraints

Whenever possible, correctness should be enforced by persistence rather than by the subscriber alone. Examples include:

- unique constraints
- primary keys
- upserts

An INSERT that meets a conflict becomes an update rather than a duplicate row. Database constraints therefore provide an additional layer of protection against duplicate processing, because business correctness should not rely solely upon application code.

---

# Upserts

Prefer an insert-or-update to an insert that meets a duplicate and fails. Upserts naturally support idempotent behaviour, and they simplify subscriber implementation.

---

# Event Recording

Subscribers may maintain a processed-event store, taking the Event ID of each incoming event, asking whether it has already been processed, executing only where it has not, and recording the outcome afterwards. This approach is particularly useful for side-effect-heavy operations. The runtime does not require a specific implementation, only the resulting behaviour.

---

# Side Effects

Special care is required for external side effects, because they escape the boundary within which the platform can correct itself. Examples include:

- email
- notifications
- webhooks
- external APIs

Repeated execution may produce:

- duplicate emails
- duplicate notifications
- duplicate API calls

Subscribers should therefore verify whether the side effect has already occurred before repeating it.

---

# Event Replay

Replay intentionally delivers historical events again, so delivering a historical event to a subscriber should leave current state correct. Replay should never corrupt business state, and this property depends entirely upon idempotent subscribers.

---

# Retries

Retries become trivial when subscribers are idempotent, because a failure followed by a retry, a further failure, a further retry and eventual success leaves the same business state as success at the first attempt. Subscribers do not need to distinguish between:

- original delivery
- retry
- replay

They simply process events safely.

---

# Event Ordering

Idempotency should not rely upon ordering. Suppose PlaybackCompleted arrives before `playback.started`: subscribers should validate current business state rather than assuming chronological delivery. Ordering guarantees belong elsewhere, and idempotency remains independent of them.

---

# Compensating Events

Business state should never be "rolled back" by replay. Instead a MetadataImported fact is superseded by a later MetadataCorrected fact, because new facts supersede previous facts. History remains intact, and subscribers simply converge upon current truth.

---

# Stateless Subscribers

Stateless subscribers naturally encourage idempotency, because durable state lives outside the subscriber in:

- repositories
- databases
- projections

State does not accumulate in subscriber instances, which is why restarting a subscriber should not affect correctness.

---

# Observability

Duplicate processing should remain observable, because operational visibility helps identify architectural problems before they affect users. Useful metrics include:

- duplicate events ignored
- replayed events processed
- idempotency failures
- constraint violations

---

# Anti-Patterns

The following practices are prohibited.

## Assuming Exactly Once

Treating an event as something the subscriber will receive, execute and then never see again. Subscribers must always assume duplicate delivery.

## Side Effects Before Validation

Sending an email and only afterwards checking whether it is a duplicate. Validation should always precede external effects.

## Mutable Event History

Changing historical events to avoid duplicate processing. History remains immutable, so subscribers adapt to it rather than the reverse.

## Runtime-Owned Idempotency

The runtime should not decide business correctness, because subscribers own idempotent behaviour.

## Ignoring Duplicate Delivery

Assuming retries will never occur. Duplicate delivery is expected rather than exceptional.

---

# Mosaic Guidelines

Within Mosaic:

- Every subscriber must be idempotent.
- Duplicate event delivery must produce the same business state.
- Business correctness must not depend upon exactly-once delivery.
- Event IDs should support duplicate detection.
- Database constraints should reinforce idempotency.
- External side effects must be protected against duplication.
- Replay must remain safe.
- Retries must assume duplicate execution.

---

# Relationship to the Runtime

Idempotency is one of the architectural properties that allows the Mosaic Runtime to remain simple. Because subscribers are idempotent:

- retries become inexpensive
- worker crashes become recoverable
- replay becomes possible
- rolling deployments become safer
- runtime coordination becomes dramatically simpler

Rather than building an increasingly complicated runtime attempting to prevent duplicates, Mosaic accepts duplicate delivery and requires subscribers to handle it correctly, which significantly improves resilience while reducing runtime complexity.

---

# Summary

Idempotency is not about preventing duplicate execution; it is about ensuring duplicate execution produces correct behaviour. Within the Mosaic Runtime, correctness is achieved through:

- immutable events
- idempotent subscribers
- durable business state
- explicit ownership

When these principles are followed, retries, replay and recovery become natural properties of the platform rather than exceptional situations requiring special handling.
