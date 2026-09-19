# KOO → KOD: shard gateway adapter r0.2 bounded security correction

status: TASK
execution_mode: BOUNDED_NON_DEPLOYING_CODE_CORRECTION
deployment_authority: no
host_mutation_authority: no
credential_authority: no
project_time: omitted; trusted project-time source not used

## Current authority

KOD current-writer:
`entities/koder/current/KOD__replacement-current-writer-v04.md`

Writer establishment commit:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

Writer blob:
`ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

KOD must fresh-verify current-writer and task state before editing.

## Exact causal input

SIS independent verification result:
`entities/sisadmin/outbox/SIS__shard-gateway-adapter-r01-independent-verify__KOO-KOD.md`

Result commit:
`294564fe0d25d6c8e33d51975c62a00823fe2cd7`

Result blob:
`33c7ccb07ec599507df5c7f8faae1ddd59ed3543`

Verdict:
`REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`

SIS already addressed this result to KOD:
`entities/koder/inbox/SIS__shard-gateway-adapter-r01-independent-verify__KOO-KOD.md`

Address commit:
`5b9cb3dd0d7d52746d11a7caca024d8b10e0d5d7`

That result is evidence/input only. This KOO task is the exact correction authority.

## Exact r0.1 immutable basis

Locator:
`puev5691/wellbeing-hq@84c7225e8073beeda86491c1f27f371c4f532a2d:entities/koder/outbox/shard-gateway-adapter-r01`

Boundary commit:
`84c7225e8073beeda86491c1f27f371c4f532a2d`

Package subtree:
`ab976b7e627cebd62f8aa9c0d86ea91ef341fcb4`

Read exact r0.1 bytes directly from the shared GitHub information field. Do not require OPERATOR to transfer candidate files.

SIS identity verification:
`PASS_EXACT_IMMUTABLE_CANDIDATE_5_OF_5`

SIS deterministic rerun:
15 tests, 0 failures, 0 errors.

## Exact correction scope

Create one successor package:
`entities/koder/outbox/shard-gateway-adapter-r02/`

Do not mutate or replace the immutable r0.1 package.

Correct only the four SIS defects below plus tests/documentation/manifest changes strictly required by those corrections.

### C1 — enforce wall-time for every opcode

SIS finding:
TIMEOUTS are enforced only through the Git/subprocess `_run()` path.

Required behavior:
- default non-special operation deadline: 10 s;
- SHA256: 60 s;
- ARCHIVE_LIST: 20 s;
- Git operations: 15 s;
- STAT, LIST_DIR, READ_BOUNDED, SHA256 and ARCHIVE_LIST must have actual fail-closed wall-time/deadline enforcement, not declarations only.

Add deterministic tests for:
- SHA256 timeout/deadline;
- at least one ARCHIVE_LIST or other non-Git timeout path.

Do not implement cancellation semantics that permit a timed-out worker to continue mutating anything. Candidate remains read-only.

### C2 — race-safe no-follow / TOCTOU boundary

SIS finding:
lexical/lstat validation occurs before later pathname-based open/tar/stat operations; target can be swapped after validation.

Required behavior:
- file-bearing operations must use descriptor-relative/no-follow semantics, or an equivalent fail-closed primitive preventing a newly substituted symlink from being followed before bytes are read;
- READ_BOUNDED and SHA256 must not read attacker-swapped target bytes before detection;
- ARCHIVE_LIST must have equivalent race-safe protection;
- directory/stat handling must preserve the same no-follow policy where applicable;
- fail closed on race/identity mismatch.

Add a real deterministic symlink/target-swap race test, not merely post-read identity-change simulation.

Keep the existing denied-target and traversal policy.

### C3 — one validated Git ref boundary for tree + blob operations

SIS finding:
GIT_LS_TREE validates ref, but GIT_BLOB_META and GIT_BLOB_READ_BOUNDED accept `req.git_ref` without the same rule.

Required behavior:
- factor one shared Git ref validator;
- apply it to GIT_LS_TREE, GIT_BLOB_META and GIT_BLOB_READ_BOUNDED;
- accept only:
  - `HEAD`; or
  - full 40-hex commit;
- non-HEAD exact commit must satisfy the approved reachability/ancestor rule against HEAD;
- reject symbolic/non-approved/unreachable refs consistently.

Add deterministic tests for rejected symbolic and unreachable/non-approved refs in both blob meta and blob read paths.

### C4 — final serialized result-size + stable binary-read error

SIS finding:
raw bytes are bounded before JSON/text wrapping; final serialized result can exceed the configured result cap due to escaping/framing. Invalid UTF-8 may escape as `UnicodeDecodeError`.

Required behavior:
- enforce 1 MiB cap on final serialized/canonical result payload for every opcode;
- do not rely only on pre-serialization raw byte limits;
- define a stable fail-closed GatewayError code for invalid UTF-8 / binary content on text read operations;
- preserve deterministic error serialization without leaking raw binary.

Add deterministic tests for:
- JSON escaping expansion crossing final cap;
- invalid UTF-8/binary read;
- final serialized cap enforcement.

## Preserve all r0.1 PASS boundaries

Do not regress:

- exact VERIFY opcode allowlist;
- mazhor repository + approved archive root;
- burzh repository only;
- no burzh archive root;
- erefia absent/deferred;
- hard-coded `VERIFY`;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- no free-form shell;
- direct argv/no shell interpolation;
- traversal and denied-target rules;
- request-size 32 KiB;
- directory/archive entry bounds;
- per-host concurrency = 1;
- no automatic cross-host failover;
- audit schema `wb.shard_gateway.audit.v1`;
- non-deploying status.

## Hard boundaries

Do NOT:
- deploy to any host;
- mutate mazhor/burzh/erefia;
- SSH for mutation;
- create/modify users, groups, ACLs, firewall, systemd, services or packages;
- read/provision credentials;
- enable WRITE;
- expose a listener;
- mutate repository/archive/shard content;
- reuse historical Entity Resource Gateway implementation unless the exact correction itself requires a small independently reviewed primitive and provenance is explicit.

## Required output

Publish one new immutable r0.2 package under:
`entities/koder/outbox/shard-gateway-adapter-r02/`

Required package content:
- corrected implementation;
- updated tests;
- updated README/security boundary;
- deterministic TEST-RESULTS;
- deployment/non-deployment manifest with exact hashes/blobs/tree after final publication.

Run the full test suite from exact final bytes.

Terminal result must include:
- exact package locator;
- boundary commit/tree;
- per-file blob/SHA identities;
- total tests/failures/errors;
- explicit closure status C1–C4;
- deployment/host mutation/credential access = 0;
- explicit next gate: SIS independent re-verification on exact r0.2 bytes;
- ARH acceptance review must remain blocked until SIS r0.2 re-verify PASS.

## Expected terminal result

Return exactly one:

`PASS_KOD_SHARD_GATEWAY_ADAPTER_R02_READY_FOR_SIS_REVERIFY`

or

`BLOCKED_KOD_SHARD_GATEWAY_ADAPTER_R02: <exact blocker>`

or exact FAIL.

Address terminal result to KOO and SIS.
Stop after terminal result.
