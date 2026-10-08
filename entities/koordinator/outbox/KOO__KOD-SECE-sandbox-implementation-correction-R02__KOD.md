# KOO -> KOD v0.7: bounded sandbox implementation correction R02

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
KOD / КОДЕР v0.7 current writer

attempt:
KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02_A1

scope:
BOUNDED_OFFLINE_SANDBOX_IMPLEMENTATION_CORRECTION_ONLY

project_time:
omitted

Resume-First.

Perform ONLY one NEW immutable correction successor of exact R01 candidate.

Do NOT mutate R01 in place.
Do NOT execute a real sandbox effect.
Do NOT select a concrete sandbox target.
Do NOT create G4/G5/G6 authority.
Do NOT activate/deploy.
Do NOT mutate Project Sources/canons.
Do NOT replay historical tasks/prompts.

## Exact authority

puev5691/wellbeing-hq@0efd64027cb4bb10f68c91a2233091eab6b10b32:
entities/koordinator/outbox/KOD_SECE_sandbox_impl_correction_R02_authority.md

blob:
65a810b1b3c2093aeeb948ec18fd26ac5955d454

decision:
AUTHORIZE_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02 = YES

## Registry

entities/koordinator/outbox/KOD_SECE_sandbox_impl_correction_R02_registry.md

blob:
4cfd08bf27cbd60bc6f1fa89593d51cd9b58470e

state:
INITIAL_NOT_STARTED

## Accepted frontier

entities/koordinator/outbox/KOD_SECE_sandbox_impl_correction_R02_frontier.md

blob:
6e893e79a96018cbe881fc735babe9e75ade8ec5

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current KOD writer / recovery

current writer:
entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

current external recovery:
puev5691/wellbeing-entity-bootstrap@63429caedcf4dd454a4de1f72aa50517fd8d2c42:
entities/kod/recovery/versions/kod-recovery-v08

tree:
5d88470c8b1cf9ea5a1bcc790baab1c52e649105

classification:
CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_POST_SANDBOX_IMPL_REVIEW_PRE_CORRECTION

If writer/recovery changed, superseded, or conflicts:
STOP with exact blocker.

## Exact R01 predecessor

KOD result:
puev5691/wellbeing-hq@c7979afefeb7dc7c33ab24d84039aa374112954e:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-r01__KOO.md

blob:
69a24ea931db365089393c75d13f1ac151593def

R01 candidate:
puev5691/wellbeing-hq@27134205e21ebc44308606de4cb59f7b3b3ed577:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-r01/

tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

candidate:
NOT_ACTIVATED

real_sandbox_effect:
NOT_EXECUTED

R01 is immutable predecessor provenance.
Do NOT rewrite it.

## Exact SHD review basis

puev5691/wellbeing-hq@ab128ba972282ea10ed3ebef51e64bab067036b4:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-adapter-platform-implementation-r01-review-r01__KOO.md

blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

terminal:
NEEDS_REWORK_SHD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_REVIEW_R01

final_verdict:
NEEDS_REWORK_SANDBOX_IMPLEMENTATION_R01

Preserved PASS:
- CANDIDATE_INTEGRITY = PASS;
- OUTCOME_FAIL_CLOSED = PASS;
- NON_LIVE_BOUNDARY = PRESERVED;
- accepted D1/D2 architecture remains valid.

## Bounded correction requirements

Correct ONLY the following classes.

### D1-A canonical binding/root integrity

Implement fail-closed canonical validation that:
- recomputes admitted/current binding_id from canonical payload excluding binding_id;
- recomputes admitted/current nested root_identity_id from nested root payload;
- validates exact effect/adapter/confinement/cleanup/platform IDs and versions against exact constants;
- rejects any mismatch before EffectIntent emission;
- preserves revalidation/invocation checks so stale or forged matching IDs cannot pass.

Add negative tests for:
- forged binding payload + stale matching binding_id;
- nested root mutation + unchanged root_identity_id;
- wrong exact adapter/effect/confinement/cleanup/platform constant.

### D1-B created object identity

CREATED_SANDBOX_OBJECT_IDENTITY must:
- require no_symlink_reparse_evidence;
- carry it in output;
- bind it into created_identity_id.

Add a negative test proving missing evidence is rejected.

### D2-A cleanup identity chain

ObjectBoundCleanupR02 eligibility must require:
- state.operation_key == created.operation_key;
- state.owner_attempt_id == created.attempt_id;
- created.root_identity_id == binding.root_identity_id;
- created.sandbox_target_id == binding.root_identity.sandbox_target_id.

Any mismatch must fail closed before cleanup plan emission.

Add negative tests for each mismatch.

### P1 Linux/POSIX platform profile binding

Validate exact:
- root_identity_class;
- created_object_identity_class;
- cleanup_binding_class;
- root.platform_evidence_profile_id == LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01.

Add negative tests for all mismatches.

### Tests / evidence hygiene

Add all missing negative coverage above.

Top-level TEST-SUMMARY.json:
- either replace with accurate R02 correction summary;
- or clearly namespace/move predecessor R04 metadata so it cannot be mistaken for R02 PASS evidence.

Do not delete immutable predecessor evidence from R01. New R02 package must make provenance clear.

## Must preserve

Exact reviewed R04 runtime/core bytes must remain unchanged:

runtime_integration.py:
e0626e3088b7f364604d1fb5e12c2b2b511c3987

reviewed baseline core:
e7b89c948c4e672c5b682408ce790670dfcdad5c

Accepted D1/D2 design semantics remain unchanged.

Outcome fail-closed semantics remain unchanged unless a change is strictly necessary to preserve or strengthen them.

Non-live boundary remains:
candidate NOT_ACTIVATED
real sandbox effect NOT_EXECUTED
sandbox target UNKNOWN / NOT_SELECTED
G4/G5/G6 authority NOT_CREATED

## Required successor

Create one NEW immutable successor package under a new KOD outbox path, not by mutating R01.

Suggested path:

entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-correction-r02/

Record exact commit/tree/file count/key blobs.

Include manifest/correction map/test evidence/checksums as appropriate.

## Mandatory PROCESSING_STARTED

Before substantive correction:

1. fresh-check exact authority/registry/frontier;
2. verify current KOD writer and recovery v08;
3. verify exact R01 tree;
4. verify exact SHD review blob/result;
5. verify no competing R02 correction attempt/result exists;
6. verify no superseding candidate exists;
7. verify G4/G5/G6 authority remains NOT_CREATED;
8. verify active Project Sources remain current.

Then create:

entities/koder/outbox/execution-evidence/KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02_A1

authority_commit:
0efd64027cb4bb10f68c91a2233091eab6b10b32

authority_blob:
65a810b1b3c2093aeeb948ec18fd26ac5955d454

registry_blob:
4cfd08bf27cbd60bc6f1fa89593d51cd9b58470e

frontier_blob:
6e893e79a96018cbe881fc735babe9e75ade8ec5

accepted_state:
INITIAL_NOT_STARTED_V1

KOD_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

KOD_recovery_ref:
63429caedcf4dd454a4de1f72aa50517fd8d2c42

KOD_recovery_tree:
5d88470c8b1cf9ea5a1bcc790baab1c52e649105

R01_candidate_tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

SHD_review_blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

Immutable-readback PROCESSING_STARTED.

Only then implement correction.

## Verification

At minimum:
- syntax/static checks PASS;
- all predecessor relevant pure/mock tests still PASS;
- new negative tests PASS;
- forged/stale canonical identity cases fail closed;
- cleanup mismatch cases fail closed;
- platform identity-class/profile mismatch cases fail closed;
- exact R04 runtime/core blobs unchanged;
- R01 tree unchanged;
- R02 package immutable-readback PASS.

Do not infer real target behavior from static/mock tests.

## Required standalone result

Create:

entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02__KOO.md

Include:
- attempt;
- authority/registry/frontier;
- PROCESSING_STARTED;
- current KOD writer/recovery;
- exact R01 predecessor;
- exact SHD review;
- R02 successor locator/commit/tree;
- changed files/key blobs;
- D1-A/D1-B/D2-A/P1 correction verdicts;
- test/evidence-hygiene verdict;
- regression verification;
- R04 unchanged proof;
- R01 immutable proof;
- candidate status;
- real effect status;
- G4/G5/G6 status;
- exact terminal.

PASS terminal:

PASS_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02_READY_FOR_INDEPENDENT_REREVIEW

Alternative:
BLOCKED_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02

if exact bounded requirements cannot be faithfully satisfied.

## Hard boundaries

NOT AUTHORIZED:
- real sandbox effect;
- concrete target selection;
- G4/G5/G6 authority or execution;
- activation/deployment;
- R01 mutation;
- Project Source/canon mutation;
- historical replay;
- automatic downstream continuation.

After result:
return to KOO.
Independent SHD rereview requires a separate future authority.

## Mandatory return

Return one final copy-paste block:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include attempt, result locator/commit/blob, terminal, PROCESSING_STARTED, R02 package locator/commit/tree, correction verdicts, test verdict, candidate NOT_ACTIVATED, real effect NOT_EXECUTED, G4/G5/G6 NOT_CREATED, exact blockers/UNKNOWNs.

Fresh-reconcile this exact KOD sandbox implementation correction R02 result. Do not infer SHD rereview or G4/G5/G6 authority.

STOP.
