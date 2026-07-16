<!--
File: docs/roadmaps/mrm-001-mosaic-platform-foundation/glossary.md
Document: MRM-001
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

## Mosaic Platform

The core Mosaic runtime authority that provides shared capabilities such as authentication, storage, GraphQL, events, registration, configuration and health.

## Mosaic-Local Authentication

Authentication in which Mosaic owns user credentials, passkeys, recovery and sessions rather than delegating user identity to Apple, Google or another external identity provider.

Mosaic-local authentication does not require email, phone verification or an external notification service.

## Remote Device Sign-In

A short-lived, one-time pairing flow in which a user authenticates on a trusted phone or computer and authorises a limited-input device such as a television.

## Policy Decision Point

The Platform-owned service that evaluates a subject, action, resource and context to return an explainable allow or deny decision.

## Relationship-Based Access Control

Authorisation based on relationships between identities, resources, devices and capabilities, such as ownership or shared-library membership.

## Attribute-Based Access Control

Authorisation based on contextual attributes such as authentication strength, device state, session age and resource classification.

## Mosaic SDK

The supported consumer-facing software development kit derived from Platform contracts.

## Mosaic Shell

The host client experience that renders Mosaic through the client-side Mosaic Design Language and Design System implementation and mounts Module surfaces.

## Mosaic Supervisor

The lifecycle authority that assembles, starts, observes, diagnoses and recovers the Mosaic binary and its managed capabilities.

## Module

A bounded Mosaic extension that provides domain capability through the Platform and SDK contracts without owning core Platform authority.
