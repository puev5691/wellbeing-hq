# KOO → KOD: File/Artifact Service correction-only successor r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: CORRECTION_ONLY_NO_DEPLOYMENT
project_time: omitted

## Exact authority

puev5691/wellbeing-hq@3b88b407389da8823a856a5ed6a335e49635a6ac:
entities/koordinator/outbox/KOO__authorize-KOD-file-artifact-service-correction-r02__OPERATOR.md

## Current causal basis

Recovered plan:
puev5691/wellbeing-hq@f13c4d4665ce0ba2f8b853f2f082b830040a2078:
entities/koordinator/current/KOO__entity-operational-memory-shards-recovered-plan-r01.md
blob ffb62995588ed5af83f38465d1b7bfc3ef92cefd

KOD convergence design:
puev5691/wellbeing-hq@e90b9bd65e569d97e7497122c80808759dc4ce9e:
entities/koder/outbox/KOD__entity-operational-memory-shards-convergence-design-r01__KOO.md
blob d760a8289ec14d16059c54f579ffe5172fd3625b

SHT independent review:
puev5691/wellbeing-hq@a9ea81332d2e9164bb836984fe8989567bbfa46d:
entities/shtabist/outbox/SHT__entity-operational-memory-shards-convergence-independent-review-r01__KOO.md
blob 949a7ec8158c20a52c0815aa38c3f1e36566f100

terminal:
BLOCKED_SHT_EOM_SHARD_PILOT_R01_CAUSALLY_OVERLAPS_UNAUTHORIZED_MEMORY_LAYERING_ATTEMPT_3

Important:
this blocker applies to EOM pilot execution lineage.
SHT explicitly found the File/Artifact Service correction gate independently separable.

## Exact failed predecessor

Independent SHD FAIL:

puev5691/wellbeing-hq@b6849cd2aa9d45fea823b06f05d45053d968d2cb:
entities/shardovik/outbox/SHD__file-service-verify-r01__KOO.md

blob:
deb8c40ada7f713a6423dbb9aa83448b0b1f505e

terminal:
FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY

Predecessor candidate:

puev5691/wellbeing-hq@bc0c6c708bdcc70cb25171f94717c0250f4317de:
entities/koder/outbox/file-artifact-service-mvp-r01

tree:
1f5f934975b64e957818c213290c9ee2969301e5

## Correction-only requirements

Fix exactly these four independently proven defects.

### A. Immutable MANIFEST mismatch

Predecessor top-level MANIFEST did not describe immutable committed bytes for 11/12 records.

Required:
- generate/seal inventory only after final bytes are fixed;
- verify SHA-256 and byte size against final successor package bytes;
- after immutable Git publication, read back exact committed blobs and compare;
- mismatch => FAIL/BLOCKED, never rewrite evidence after the fact.

### B. Reserved generated target collision

Predecessor accepted input target:
MANIFEST.json

Required:
- reserve every generated service artifact path;
- reject exact name and normalized aliases before any package write;
- add negative tests proving collision rejection.

### C. prior_manifest_path escape

Predecessor allowed traversal outside source_root.

Required:
- exact null|string contract;
- safe relative path only;
- reject absolute path and any .. component;
- enforce root containment;
- reject symlink traversal/escape before access where applicable;
- add negative tests.

### D. create_archive type closure

Predecessor accepted string "false" as truthy.

Required:
- exact Boolean type only;
- no coercion;
- malformed-type fixtures/tests;
- prior_manifest_path type closure tested as well.

## Preserve predecessor good boundaries

Must remain:
- zero network;
- no credentials;
- Git adapter disabled;
- no GitHub publication primitive from service execution path;
- no writer/current/acceptance/public_ready semantics;
- no authority/project-state semantics;
- deterministic packaging/readback/diff behavior where still valid;
- fail-closed hash/size/missing-source and ordinary source/target path checks.

## Required successor evidence

Produce one immutable successor package with:
- source;
- tests;
- README;
- request/negative fixtures;
- deterministic demo evidence;
- manifest/checksum inventory;
- exact committed-byte readback table;
- predecessor/successor delta;
- result addressed to KOO.

Tests must explicitly cover all four historical defects plus preserved prior boundary tests.

No deployment.

## Next gate

After KOD result, KOO will route the exact immutable successor to SHD for independent re-review.

KOD self-PASS does not replace SHD re-review.

Expected KOD terminal:

PASS_KOD_FILE_ARTIFACT_SERVICE_CORRECTION_R02_READY_FOR_SHD_REVIEW

or exact BLOCKED_* / FAIL_*.

## Hard prohibitions

Do not:
- execute EOM-SHARD-PILOT-R01;
- execute memory-layering attempt 3;
- enable shard WRITE;
- deploy service;
- mutate any host;
- use Commander for host action;
- mutate Project Sources/canon/current-writer;
- claim CHECKPOINT_DURABLE;
- migrate production Entity state.

After immutable successor package + exact readback + result to KOO, STOP.
