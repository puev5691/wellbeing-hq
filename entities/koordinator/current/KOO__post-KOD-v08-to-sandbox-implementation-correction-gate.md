# KOO r1.3 — post-ARH KOD recovery v08 to sandbox implementation correction gate

status:
WAITING_OPERATOR_DECISION

terminal:
PASS_KOO_R13_KOD_V08_RECOVERY_RECONCILED_TO_SANDBOX_IMPLEMENTATION_CORRECTION_GATE

project_time:
omitted

## Exact ARH recovery PASS

puev5691/wellbeing-hq@0df0e1d91ab996d9a371a71a440e428531d2ff4b:
entities/archivarius/outbox/ARH__KOD-v08-external-recovery__KOO-KOD.md

blob:
25657e704b06ed8b8760b6cc1128607837742ebd

terminal:
PASS_ARH_KOD_V08_EXTERNAL_RECOVERY

Current external recovery:
puev5691/wellbeing-entity-bootstrap@63429caedcf4dd454a4de1f72aa50517fd8d2c42:
entities/kod/recovery/versions/kod-recovery-v08

tree:
5d88470c8b1cf9ea5a1bcc790baab1c52e649105

composition:
9/9 PASS

checksum coverage:
8/8 PASS

immutable readback:
9/9 PASS

registry:
puev5691/wellbeing-hq@b0dc24077d32c896681c75db4aeb773c4f9d29da:
entities/archivarius/current/recovery-registry/ARH__KOD-recovery-v08.md

registry_blob:
23b1bdcae896f698722d5730d6fd3f2ed6c31bf7

registry_readback:
PASS

## Current KOD writer

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

## Exact implementation candidate / SHD review

candidate_tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

candidate:
NOT_ACTIVATED

real_sandbox_effect:
NOT_EXECUTED

SHD review:
puev5691/wellbeing-hq@ab128ba972282ea10ed3ebef51e64bab067036b4:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-adapter-platform-implementation-r01-review-r01__KOO.md

blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

terminal:
NEEDS_REWORK_SHD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_REVIEW_R01

final_verdict:
NEEDS_REWORK_SANDBOX_IMPLEMENTATION_R01

## Preserved PASS

candidate_integrity:
PASS

outcome_fail_closed:
PASS

non_live_boundary:
PRESERVED

accepted_D1_D2_architecture:
VALID / NOT_REOPENED

## Exact bounded correction scope

D1-A:
canonical sandbox/root binding validation:
- recompute/validate binding_id;
- recompute/validate nested root_identity_id;
- validate exact adapter/effect/confinement/cleanup/platform IDs and versions;
- fail closed before EffectIntent/admission/invocation.

D1-B:
CREATED_SANDBOX_OBJECT_IDENTITY:
- require no_symlink_reparse_evidence;
- include it in object identity;
- bind it into created_identity_id.

D2-A:
cleanup eligibility exact comparisons:
- state.operation_key == created.operation_key;
- state.owner_attempt_id == created.attempt_id;
- created.root_identity_id == binding.root_identity_id;
- created.sandbox_target_id == binding.root_identity.sandbox_target_id.

P1:
Linux/POSIX platform validation:
- validate root_identity_class;
- validate created_object_identity_class;
- validate cleanup_binding_class;
- require root platform_evidence_profile_id == LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01.

Tests/evidence hygiene:
- add negative forgery/mismatch tests for all above;
- correct or clearly namespace stale top-level TEST-SUMMARY.json.

## Currentness

Fresh checks:
- correction implementation authority: NOT_FOUND;
- correction task/result: NOT_FOUND;
- competing correction attempt: NOT_FOUND;
- candidate successor superseding af63918a...: NOT_FOUND;
- G4/G5/G6 authority: NOT_CREATED;
- KOD writer/recovery conflict: NONE_FOUND.

## Proposed correction attempt

KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02_A1

scope:
BOUNDED_OFFLINE_SANDBOX_IMPLEMENTATION_CORRECTION_ONLY

Allowed if separately approved:
- create one NEW immutable successor candidate from exact R01 tree;
- change only files/evidence/tests needed to close D1-A, D1-B, D2-A, P1 and test/evidence hygiene;
- preserve reviewed R04 baseline/core bytes;
- preserve accepted D1/D2 design semantics;
- add static/pure/mock tests;
- return BLOCKED rather than weaken requirements.

Not authorized by this reconciliation:
- correction implementation;
- real sandbox effect;
- target selection;
- G4/G5/G6 authority;
- activation/deployment;
- Project Source/canon mutation;
- historical replay.

Exact OPERATOR decision required before materialization.

STOP at OPERATOR decision.
