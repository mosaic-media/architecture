<!--
File: docs/engineering/guides/meg-008-observability/11-opentelemetry.md
Document: MEG-008
Status: Draft
Version: 0.4
-->

# OpenTelemetry

> *The Runtime should own observability. OpenTelemetry should transport it.*

---

# Purpose

Throughout MEG-008 the platform has defined:

- logs
- metrics
- traces
- health
- diagnostics

These describe **what** the platform observes.

A second question remains.

> **How is that information exported to external observability systems?**

Within Mosaic, the answer is **OpenTelemetry (OTel)**.

OpenTelemetry provides a vendor-neutral telemetry standard allowing Mosaic to integrate with existing operational tooling while remaining independent of any particular observability vendor.

---

# Philosophy

Within Mosaic:

> **Observability belongs to the architecture. OpenTelemetry belongs to the transport layer.**

The Runtime owns:

- telemetry generation
- ownership
- semantics

OpenTelemetry owns:

- encoding
- propagation
- export

The platform should never confuse:

```mermaid
flowchart TD

N1["Observability"]
N2["Architecture"]

N1 --> N2
```

with

```mermaid
flowchart TD

N1["OpenTelemetry"]
N2["Implementation"]

N1 --> N2
```

---

# Why OpenTelemetry?

OpenTelemetry provides:

- vendor neutrality
- standard trace propagation
- metrics export
- structured logging integration
- broad ecosystem support

Using an open standard allows operators to choose:

- Grafana
- Prometheus
- Jaeger
- Tempo
- Honeycomb
- Datadog
- New Relic

without changing Mosaic itself.

The Runtime should remain independent of operational tooling.

---

# Architectural Boundary

OpenTelemetry sits outside the Runtime.

Conceptually.

```mermaid
flowchart TD

N1["Runtime"]
N2["Observability Layer"]
N3["OpenTelemetry"]
N4["Exporter"]
N5["Monitoring Platform"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Runtime should never know which monitoring platform ultimately consumes its telemetry.

---

# Logs

Structured logs SHOULD be exported through OpenTelemetry log pipelines.

The Runtime owns:

```text
Log Event
```

OpenTelemetry transforms that into the appropriate wire format.

The Runtime should never construct exporter-specific log formats.

---

# Metrics

Runtime metrics SHOULD map naturally onto OpenTelemetry metrics.

Examples include:

```text
runtime_workers_active
```

```text
storage_blob_objects_total
```

```text
capability_activation_duration_seconds
```

Metric ownership remains unchanged.

Only transport changes.

---

# Traces

Distributed traces SHOULD use OpenTelemetry trace propagation.

The Runtime generates:

- traces
- spans
- events

OpenTelemetry propagates:

- trace identifiers
- span identifiers
- baggage
- context

Trace ownership remains architectural.

Transport remains infrastructural.

---

# Context Propagation

The Runtime SHOULD propagate trace context across:

- Runtime Events
- worker boundaries
- capability execution
- storage operations

OpenTelemetry provides the propagation mechanism.

The Runtime determines where context should travel.

Propagation policy belongs to the architecture.

Not the library.

---

# Resource Metadata

Every Runtime instance SHOULD expose resource metadata.

Examples include:

```mermaid
flowchart TD

N1["service.name"]
N2["mosaic-runtime"]

N1 --> N2
```

```text
service.version
```

```text
runtime.instance
```

```text
deployment.environment
```

This metadata allows external systems to distinguish:

- Runtime instances
- environments
- deployments

without affecting Runtime behaviour.

---

# Capability Metadata

Capabilities SHOULD expose resource attributes.

Examples include:

```text
capability.name
```

```text
capability.version
```

```text
capability.owner
```

These attributes become available throughout:

- traces
- metrics
- logs

Capabilities remain architecturally visible outside the Runtime.

---

# Runtime Services

Runtime Services SHOULD expose consistent telemetry attributes.

Examples include:

```text
runtime.service=scheduler
```

```text
runtime.service=worker-manager
```

```text
runtime.service=execution-engine
```

Telemetry should reinforce Runtime ownership.

Not implementation packages.

---

# Storage Metadata

Storage telemetry SHOULD identify:

```text
storage.type=postgres
```

```text
storage.type=duckdb
```

```text
storage.type=blob
```

Storage ownership should remain visible across:

- traces
- metrics
- logs

---

# Sampling

Sampling SHOULD remain configurable.

Possible strategies include:

- always sample startup
- always sample failures
- percentage sampling
- adaptive sampling

Sampling policy belongs to operations.

The Runtime should remain independent from exporter configuration.

---

# Exporters

OpenTelemetry exporters SHOULD remain replaceable.

Examples include:

```text
OTLP
```

```text
Prometheus
```

```text
Jaeger
```

```text
Tempo
```

The Runtime should depend only upon OpenTelemetry contracts.

Never exporter implementations.

---

# Correlation

OpenTelemetry should allow correlation between:

- logs
- metrics
- traces

using shared identifiers.

The Runtime generates:

- trace IDs
- span IDs

OpenTelemetry ensures these identifiers remain consistent across exported telemetry.

Operators should move naturally between:

logs

↓

traces

↓

metrics

without manual correlation.

---

# Baggage

Context baggage SHOULD remain minimal.

Examples include:

- capability identifier
- Runtime service
- operation

Avoid:

- user information
- secrets
- payload data

Baggage should describe execution context.

Not business content.

---

# Health

Health SHOULD remain separate from OpenTelemetry.

Health describes:

Operational readiness.

OpenTelemetry transports telemetry.

The Runtime should not attempt to encode health semantics solely through traces or metrics.

Health remains an independent architectural concern.

---

# Diagnostics

Likewise.

Runtime Diagnostics remain Runtime APIs.

They should not become OpenTelemetry resources.

Diagnostics answer:

> **What currently exists?**

Telemetry answers:

> **What happened?**

These responsibilities remain intentionally separate.

---

# Performance

OpenTelemetry integration SHOULD remain lightweight.

Avoid:

- synchronous exporters
- blocking telemetry
- excessive allocations

Telemetry export should never significantly affect Runtime execution.

Observability should remain proportional to operational value.

---

# Privacy

Telemetry exported through OpenTelemetry MUST NOT contain:

- passwords
- API keys
- personal information
- authentication tokens

Sensitive information should remain inside secure platform boundaries.

Observability should remain safe by default.

---

# Testing

OpenTelemetry integration SHOULD be tested.

Typical tests verify:

- trace propagation
- metric export
- log correlation
- resource metadata
- context propagation

Testing should verify transport.

Not business behaviour.

---

# Future Compatibility

OpenTelemetry evolves.

The Runtime should remain insulated from:

- exporter changes
- protocol changes
- backend changes

Observability contracts belong to Mosaic.

OpenTelemetry simply carries them.

This protects the platform from external tooling evolution.

---

# Anti-Patterns

The following practices are prohibited.

## Vendor APIs

Capabilities calling vendor-specific monitoring SDKs.

---

## Exporter Logic

Embedding exporter implementation inside Runtime Services.

---

## Missing Context

Exporting telemetry without trace propagation.

---

## Sensitive Telemetry

Publishing secrets through OpenTelemetry.

---

## Platform Coupling

Designing Runtime architecture around one monitoring vendor.

---

## Diagnostic Replacement

Replacing Runtime diagnostics with external telemetry.

---

# Mosaic Guidelines

Within Mosaic:

- OpenTelemetry MUST remain transport infrastructure.
- Runtime ownership MUST determine telemetry ownership.
- Exporters MUST remain replaceable.
- Trace context MUST propagate across Runtime boundaries.
- Resource metadata SHOULD remain consistent.
- Sensitive information MUST NOT be exported.
- Health and diagnostics MUST remain Runtime concepts.
- OpenTelemetry SHOULD remain vendor neutral.

---

# Relationship to MEG

Debugging defines:

> **How operators investigate the Runtime.**

OpenTelemetry defines:

> **How Runtime telemetry reaches external observability systems.**

The next chapter introduces **Observability Guidelines**, bringing together every observability concept into practical engineering guidance for Runtime and capability developers.

---

# Summary

OpenTelemetry is not Mosaic's observability architecture.

It is the transport protocol through which that architecture reaches external tools.

Within Mosaic:

- the Runtime owns telemetry,
- capabilities own business observability,
- storage owns storage observability,

and OpenTelemetry simply carries those signals safely to whatever operational ecosystem the user chooses.

That separation preserves one of the platform's most important architectural principles:

> **The platform defines observability. External tooling consumes it.**
