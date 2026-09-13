# Provenance Display Rules

## Show when safe

owner/profile; artifact/content class; canonical/provenance locators; semantic status; immutable identity; source repo/path/commit/blob when applicable; supersede lineage; derivative parent/type; public-safe review locators.

## Synthetic handling

Use `source_repository=synthetic`, `source_commit/source_blob=not_applicable`, and `immutable_identity.scheme=synthetic-fixture`. Always show SYNTHETIC.

## Never show publicly

secret values; tokens/session material; raw private user identifiers; raw audience comment DB; credential-bearing runtime paths; private security notes; policy-forbidden moderator/admin identity.

## Fail closed

For real Git-backed objects, missing available commit/blob or immutable mismatch blocks public-ready rendering.

---
created_by: WEB
project_time: omitted; trusted project-time source not used
