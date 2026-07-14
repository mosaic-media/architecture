<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/index.md
Document: MIP-002
Status: Draft
Version: 0.4
-->

# MIP-002 — Module Manifest Protocol

> *Before the Platform executes a module, it should understand the module's identity, authority and contracts.*

---

# Purpose

MIP-002 defines the canonical manifest contract for Mosaic modules.

MEG-006 explains how engineers build module support.

MIP-002 defines the protocol that makes module admission safe and repeatable.

---

# Protocol Statement

Within Mosaic:

> **The manifest is the contract. The implementation is one possible fulfilment of that contract.**

A module does not participate in the Platform until its manifest has been discovered, validated and accepted.

The manifest is the Supervisor's primary source of truth for Module selection and build-time composition.

---

# Scope

This protocol defines manifest responsibilities for:

- identity
- metadata
- dependencies
- permissions
- provided contracts
- consumed contracts
- lifecycle
- compatibility
- SDK compatibility
- capability support declarations
- event declarations

It does not define module implementation, SDK shape or Build Pipeline internals.
