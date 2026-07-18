<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/glossary.md
Document: MIP-002
Status: Draft
-->

# Glossary

---

# Manifest

A machine-readable declaration of a module's identity, dependencies, permissions, contracts and lifecycle expectations.

---

# Module

A delivery package that contributes capability to Mosaic.

---

# Module Catalogue

A metadata-only view of Modules available from configured discovery sources.

Catalogue entries are derived from Module manifests and may be used to generate onboarding choices.

Catalogue presence does not imply compatibility, admission or activation.

---

# Permission

An explicit authority granted by the Platform to a module.

---

# Provided Contract

A contract exposed by a module for the Platform or other capabilities to consume.

---

# Consumed Contract

A contract required by a module in order to function.

---

# Public Event

A Module event declared as part of the Module's documented integration contract.

Public events may be subscribed to by other Modules.

---

# Private Event

A Module event declared as an internal implementation detail.

Private events should not be subscribed to by other Modules.

---

# Event Declaration

A manifest declaration describing events a Module publishes or subscribes to.

Published events should distinguish public and private visibility.
