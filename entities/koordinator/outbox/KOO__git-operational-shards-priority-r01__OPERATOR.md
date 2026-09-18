# KOO → OPERATOR: Git operational shards priority r0.1

status: OPERATOR_DIRECTION_RECORDED
priority: HIGH_INFRASTRUCTURE
implementation_authorization: bounded design/pilot only

## Goal

Reduce GitHub tool latency without weakening GitHub as the canonical external immutable evidence layer.

Target architecture:

`Entity → fast local/host file service → batch/seal/check → GitHub canonical publish/readback`

The fast service is an operational shard, not an authoritative source.

## Candidate shard functions

- local staging/worktree;
- package assembly;
- SHA-256 and manifest generation;
- deterministic file inventory;
- batch commit preparation;
- local Git plumbing/checks;
- bare mirror/fetch cache;
- readback comparison;
- restore/readback drills;
- queueing of outbound GitHub writes.

## Non-goals

Do not:
- replace GitHub as project truth;
- let local cache define current/accepted;
- create hidden state that cannot be reproduced;
- bypass version identity, receipt, or recovery rules;
- store secrets in shard repositories/files.

## Order

1. finish booster account/live gate as highest project priority;
2. use existing ARH→SIS bounded host-access pilot on mazhor;
3. obtain physical/readback access and baseline file/Git timings;
4. compare mazhor/burzh/erefia with identical bounded benchmark;
5. select fastest/most reliable host(s) as operational Git/file shards;
6. KOD builds idempotent shard tooling;
7. independent verification;
8. only then route selected repetitive Git/file operations through shard layer.

## Acceptance idea

A shard is operational only if:
- exact inputs/outputs are reproducible;
- canonical GitHub commit/tree/blob identity remains final evidence;
- shard failure cannot silently corrupt project state;
- sync/readback mismatch fails closed;
- no secrets leak into artifacts/logs;
- recovery path exists.

---
KTO: KOO / КООРДИНАТОР
STATUS: GIT_OPERATIONAL_SHARDS_DIRECTION_RECORDED
