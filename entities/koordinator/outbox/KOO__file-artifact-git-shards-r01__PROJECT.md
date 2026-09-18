# KOO: File/Artifact Service + Git operational shards r0.1

status: INFRASTRUCTURE_DIRECTION_RECORDED
priority: HIGH_AFTER_ACTIVE_WIP
implementation_authorization: bounded design/pilot only

## Goal

Reduce Entity cycle time by moving repetitive file/Git mechanics out of reasoning-heavy profile work while preserving GitHub as canonical immutable project evidence.

Target flow:

`Entity → File/Artifact Service → Git operational shard → GitHub canonical publish/readback`

The service/shards are operational workers only. They do not gain writer, acceptance, routing, or project-state authority.

## Layer 1 — File/Artifact Service

Required bounded functions:
- package assembly from explicit inputs;
- deterministic file inventory;
- SHA-256 generation;
- manifest generation;
- exact size/blob/hash table;
- archive creation where allowed;
- local readback/check;
- diff against prior immutable package;
- fail-closed source mismatch;
- output one compact verified result for the calling Entity.

The service must not:
- decide acceptance;
- promote current/public_ready;
- infer authority;
- store secrets in artifacts/logs;
- silently mutate GitHub/project state.

## Layer 2 — Git operational shards

Candidate shard roles:

### READ
- cached/fresh fetch;
- exact commit/tree/blob lookup;
- bounded search/preflight;
- source identity readback.

### WRITE
- local staging/worktree;
- batch commit preparation;
- bounded multi-file atomic publication where Git backend permits;
- no authority decision.

### VERIFY
- SHA/tree/blob comparison;
- manifest verification;
- package sealing/readback;
- reproducibility checks.

### ROUTE
- mechanical inbox/outbox/pointer/registry preparation;
- never equate publication with delivery, receipt, acceptance or activation.

## Canonical boundary

GitHub remains final canonical external evidence layer.

Shard/local cache is never authoritative by itself.

A shard result is valid only when:
- inputs/outputs are reproducible;
- exact GitHub commit/tree/blob identity is verified for canonical publish;
- mismatch fails closed;
- secrets remain excluded;
- recovery/readback path exists.

## Host selection order

Existing direction:
`87c278e5d99f102b9c148104a56e5009ab49a005`.

Practical sequence:
1. finish current SIS mazhor host-access/readback pilot;
2. collect identical bounded file/Git benchmark on mazhor;
3. repeat on burzh and erefia;
4. compare latency/reliability/permissions/storage boundaries;
5. choose fastest reliable host(s) as operational shards;
6. deploy File/Artifact Service MVP on selected shard;
7. independently verify;
8. route only selected repetitive operations through shard layer;
9. measure cycle-time delta before broader adoption.

## MVP acceptance

File/Artifact Service MVP must demonstrate:
- deterministic package seal from same inputs;
- SHA/manifest exactness;
- batch preparation;
- local readback;
- GitHub canonical readback;
- no secret leakage;
- fail-closed mismatch;
- no authority escalation;
- recovery of service state without affecting project truth.

## Priority relation

1. current active KOD portal-fix and SIS mazhor pilot finish first;
2. portal corrected build gets independent reverify;
3. File/Artifact Service MVP becomes the next KOD infrastructure priority before Telegram semantic-admission implementation;
4. shard benchmark/selection proceeds from SIS host pilot evidence;
5. booster first live call remains blocked only on OPERATOR account/project/model/credential gate and may preempt this lane once inputs are ready.

## Non-goals

Do not:
- replace GitHub;
- create another authoritative state database;
- let caches define current/accepted;
- bypass recovery/routing canon;
- convert @mention into delivery;
- enable broad automation before pilot verification.

---
KTO: KOO / КООРДИНАТОР
STATUS: FILE_ARTIFACT_GIT_SHARDS_DIRECTION_RECORDED
