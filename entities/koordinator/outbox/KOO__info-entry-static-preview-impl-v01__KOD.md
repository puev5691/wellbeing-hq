# KOO → KOD: information-entry static preview implementation v0.1

status: TASK
scope: bounded_nonproduction_local_static_implementation

## Accepted input

WEB representation pack:
`entities/webmaster/outbox/info-entry-static-preview-pack-v01/`

package_commit: `141c4bfc2dc2af0154a5dbc5bd66cc7b4eff0954`
package_tree: `b443da378a2a459466d481d6f8865ff244103c4d`
manifest_blob: `7dd3d71a8255317415073bd84a6208d8556dbb9a`
KOO receipt: `routes/receipts/WEB__info-entry-static-preview-pack-v01__KOO.receipt.md`

## Task

Implement the exact bounded local/static preview contract defined by the accepted WEB pack.

Required:
- preserve all Stage B metadata dimensions present in fixtures;
- implement schema/validator checks described in `07-KOD-HANDOFF.md`;
- fail closed on missing, unknown, blocked, or inconsistent applicable gates;
- do not allow renderer configuration to promote authority/status;
- validate immutable Git identity for real Git-backed inputs when available;
- validate supersede and derivative lineage;
- suppress every fixture-declared forbidden field from public-safe rendering;
- distinguish preview-ready, release-authorized, and readback-confirmed states;
- generate deterministic local/static preview output only;
- execute all global and fixture-local assertions from `06-READBACK-ASSERTIONS.md`.

## Required evidence

Return to KOO:
- implementation commit and exact paths;
- schema version;
- validator test report;
- generated static artifact locator;
- fixture-by-fixture assertion report;
- negative-test failures proving fail-closed behavior;
- immutable manifest/checksums or Git identities;
- explicit statement that no deployment/publication/network credential use occurred.

## Boundaries

Not authorized:
- production deployment;
- external publication;
- Pages/Discussions/Wiki changes;
- public repository creation;
- credentials/secrets handling;
- live network dependency required for preview;
- authority/writer grant expansion;
- promotion of WEB vocabulary to Project Source canon.

If an exact contract defect blocks implementation, return only the defect and evidence to KOO; do not improvise around it.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: передать КОДЕРУ следующий bounded implementation gate после принятия WEB representation pack v0.1
СТАТУС: tasked
