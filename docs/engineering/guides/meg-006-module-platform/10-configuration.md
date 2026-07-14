<!--
File: docs/engineering/guides/meg-006-module-platform/10-configuration.md
Document: MEG-006
Status: Draft
Version: 0.2
-->

# Configuration

> *Capabilities should declare what they need. The Runtime should decide how that configuration is provided.*

---

# Purpose

Every capability requires configuration.

Examples include:

- API credentials
- refresh intervals
- feature flags
- provider selection
- storage locations
- execution limits

Capabilities should never concern themselves with:

- configuration files
- environment variables
- databases
- secrets management

Those are Runtime responsibilities.

This document defines how capabilities declare, receive and consume configuration within the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Capabilities define configuration. The Runtime supplies configuration.**

The capability declares:

> **What configuration exists.**

The Runtime determines:

> **Where it comes from.**

This separation protects capabilities from deployment concerns.

---

# Configuration Model

Configuration follows a simple lifecycle.

```
Capability Manifest

↓

Configuration Schema

↓

Runtime Validation

↓

Runtime Injection

↓

Capability Execution
```

The capability never reads configuration directly from external sources.

---

# Configuration Before Execution

Configuration must be validated before activation.

```
Discovery

↓

Registration

↓

Configuration

↓

Activation

↓

Execution
```

Capabilities should never begin execution with invalid configuration.

Fail fast.

Not later.

---

# Configuration Schema

Every capability SHOULD define its configuration schema.

Example.

```yaml
configuration:

  provider:

    type: string

    required: true

  refreshInterval:

    type: duration

    default: 24h

  language:

    type: string

    default: en
```

The schema becomes part of the capability manifest.

It is not implementation.

It is contract.

Schema-first configuration is a common approach because it allows validation before components begin execution. ([json-schema.org](https://json-schema.org/))

---

# Configuration Ownership

Configuration ownership is intentionally divided.

Capability owns:

- schema
- defaults
- meaning

Runtime owns:

- storage
- validation
- injection
- lifecycle

Neither should assume the responsibilities of the other.

---

# Configuration Sources

The Runtime MAY assemble configuration from multiple sources.

Examples include:

```
System Defaults
```

↓

```
Capability Defaults
```

↓

```
Configuration File
```

↓

```
Environment Variables
```

↓

```
Secrets Manager
```

↓

```
Administrative Overrides
```

The Runtime owns precedence.

Capabilities simply consume the final validated configuration.

---

# Runtime Injection

Capabilities receive configuration through the SDK.

Example.

```go
cfg := ctx.Configuration()
```

The capability should not know whether configuration originated from:

- YAML
- JSON
- PostgreSQL
- Vault
- Kubernetes
- Docker

Configuration origin remains an infrastructure concern.

---

# Typed Configuration

Configuration SHOULD be strongly typed.

Poor.

```go
cfg["refreshInterval"]
```

Preferred.

```go
cfg.RefreshInterval
```

Strong typing improves:

- readability
- validation
- tooling
- refactoring

The Runtime should transform raw configuration into typed capability configuration before injection.

---

# Default Values

Capabilities MAY declare defaults.

Example.

```yaml
refreshInterval:

  default: 24h
```

The Runtime applies defaults before validation completes.

Defaults should represent sensible operational behaviour.

Not placeholders.

---

# Required Configuration

Capabilities SHOULD explicitly identify required configuration.

Example.

```yaml
tmdbApiKey:

  required: true
```

If required configuration is missing:

Activation must fail.

Capabilities should never attempt to execute without mandatory configuration.

---

# Secrets

Sensitive configuration should remain Runtime managed.

Examples include:

- API keys
- OAuth secrets
- database credentials
- tokens

Capabilities should receive:

```
Secret Value
```

The Runtime should own:

- retrieval
- storage
- rotation
- protection

Capabilities should never discover secrets independently.

---

# Validation

The Runtime validates configuration before activation.

Examples include:

- required values
- type validation
- ranges
- enums
- formats

Capabilities should assume:

Received configuration is valid.

Business validation remains inside the capability.

Configuration validation remains inside the Runtime.

---

# Configuration Versioning

Configuration schemas SHOULD evolve alongside capabilities.

Example.

```
Metadata 1.0

↓

Schema V1
```

Later.

```
Metadata 2.0

↓

Schema V2
```

The Runtime should understand which schema version belongs to which capability version.

Schema evolution should remain explicit.

---

# Live Configuration

The Runtime MAY support live configuration updates.

Lifecycle.

```
Configuration Updated

↓

Validation

↓

Capability Notification

↓

Apply
```

Capabilities should decide:

Whether configuration can be applied dynamically.

Some configuration may require restart.

The Runtime should support both models.

---

# Immutable Configuration

Configuration SHOULD remain immutable during execution unless explicitly refreshed by the Runtime.

Capabilities should avoid modifying configuration internally.

Configuration belongs to the Runtime.

Business state belongs to the capability.

---

# Configuration Scope

Configuration exists at several scopes.

Examples include:

```
Platform
```

↓

```
Capability
```

↓

```
Instance
```

Capabilities should consume only their own configuration.

Platform configuration remains a Runtime concern.

---

# Configuration Diagnostics

The Runtime SHOULD expose:

- loaded configuration
- schema version
- validation failures
- configuration source

Sensitive values MUST remain redacted.

Operators should understand configuration without exposing secrets.

---

# Marketplace

Marketplace tooling SHOULD expose configuration requirements before installation.

Example.

```
Metadata Capability

↓

Requires TMDB API Key
```

Operators should understand configuration requirements before activation.

Installation should not become trial and error.

---

# Runtime Independence

Capabilities should never depend upon:

- YAML parsers
- JSON parsers
- environment variables
- secret managers

The SDK provides configuration.

Nothing more.

This keeps capabilities completely deployment agnostic.

---

# Anti-Patterns

The following practices are prohibited.

## Environment Variables

Capabilities reading:

```go
os.Getenv(...)
```

---

## Configuration Files

Capabilities parsing YAML or JSON directly.

---

## Runtime Discovery

Capabilities searching for configuration sources.

---

## Mutable Configuration

Capabilities modifying Runtime configuration.

---

## Secrets In Code

Embedding API keys or credentials inside capability implementations.

---

## Duplicate Validation

Performing schema validation inside both the Runtime and the capability.

Schema validation belongs to the Runtime.

Business validation belongs to the capability.

---

# Mosaic Guidelines

Within Mosaic:

- Capabilities MUST declare configuration schemas.
- The Runtime MUST validate configuration before activation.
- Configuration MUST be injected through the SDK.
- Secrets MUST remain Runtime managed.
- Configuration SHOULD remain strongly typed.
- Required configuration MUST prevent activation when absent.
- Configuration diagnostics SHOULD remain observable.
- Capabilities MUST remain independent of configuration storage.

---

# Relationship to MEG

Permissions define:

> **What a capability may do.**

Configuration defines:

> **How that capability should operate.**

The next chapter introduces **Versioning**, defining how capabilities, manifests and SDK contracts evolve together while preserving Runtime compatibility.

---

# Summary

Configuration is an agreement between a capability and the Runtime.

The capability declares:

- what it requires
- what defaults exist
- what validation applies

The Runtime determines:

- where values come from
- whether they are valid
- how they are delivered

By separating configuration from configuration storage, the Mosaic platform allows capabilities to remain completely independent of deployment environments while preserving a consistent operational experience across every Runtime.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`09-permissions.md`

**Next File**

`11-versioning.md`
