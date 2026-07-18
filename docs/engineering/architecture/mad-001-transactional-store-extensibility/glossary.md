<!--
File: docs/engineering/architecture/mad-001-transactional-store-extensibility/glossary.md
Document: MAD-001
Status: Draft
-->

# Glossary

---

| Term | Meaning |
|------|---------|
| Transaction scope (`Tx`) | An opaque handle marking one Platform transaction. It exposes no fixed list of stores. |
| `UnitOfWork` | The contract that opens a transaction scope and runs work within it. |
| Uniform store resolution | Obtaining any store — Core Platform or capability — through one typed accessor bound to the transaction scope, rather than through named methods. |
| Storage adapter | A port that provides the `UnitOfWork` and binds resolved stores to the live transaction. The built-in PostgreSQL module implements it; SQLite is a candidate replacement. |
| Core Platform store | A store owned by Core Platform, such as the user, session or outbox store. |
| Capability store | A store owned by a first-party capability, resolved the same way as a Core Platform store. |
| Content-agnostic object model | A Platform-owned data model general enough that a new content type maps onto existing storage rather than requiring new schema. |
