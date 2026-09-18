# KOO → KOD: File/Artifact Service MVP r0.1

status: QUEUED_WAITING_ACTIVE_SLOT
priority: HIGH_INFRASTRUCTURE

Do not start until:
- current portal presentation-fix task has a terminal result;
- KOO current queue shows a free KOD slot.

Direction:
`entities/koordinator/outbox/KOO__file-artifact-git-shards-r01__PROJECT.md`
commit `b62896ff271ab0480a4ff1fcecef386a7c65b1b6`.

Goal:
Build an isolated deterministic local File/Artifact Service MVP for repetitive package/seal/hash/manifest/readback work.

Required:
- explicit request schema;
- explicit input file identities;
- deterministic package assembly;
- SHA-256 / size / inventory;
- manifest;
- local readback;
- package diff;
- fail-closed identity mismatch;
- compact machine result;
- no authority/project-state semantics;
- no secrets;
- zero-network default tests;
- optional Git adapter interface kept disabled unless separately authorized.

Do not:
- publish to GitHub in MVP execution path;
- mutate current/writer/acceptance;
- replace GitHub canonical evidence;
- touch Telegram/TERA2/portal source state.

Expected once activated:
`PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`
or exact blocker/fail.
