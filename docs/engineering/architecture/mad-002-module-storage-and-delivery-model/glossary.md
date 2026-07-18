<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/glossary.md
Document: MAD-002
Status: Draft
-->

# Glossary

---

| Term | Meaning |
|------|---------|
| Module | An ordinary Go library the Supervisor compiles into the Platform Binary at build time. Not a runtime plugin. |
| Essential Module | A Module that ships in the Platform repository, is pulled with the Platform and cannot be deselected. Required for a valid Generation. |
| Community Module | A Module that lives in its own repository and is selected by the user; the Supervisor fetches and compiles it into the binary. |
| Generation | A composed, activated Platform Binary produced by the Supervisor from the Platform and its selected Modules ([MIP-006](../../protocols/mip-006-generation-composition-protocol/index.md)). |
| Content-agnostic object model | A Platform-owned data model general enough that a new content type maps onto existing structure rather than requiring new tables or schema. |
| Analytical processing port | A Platform-owned contract for analytical work (recommendations, correlation, reporting, popularity, search candidates), satisfied by PostgreSQL today and by additional engines later if needed. |
