# KOO -> KOD: SECE R02 offline combined-runtime evidence handoff

status: PREPARED_FOR_OPERATOR_DECISION_NOT_ACTIVATED
recipient: KOD / КОДЕР current-writer v0.7
scope: OFFLINE_COMBINED_RUNTIME_EVIDENCE_ONLY
project_time: omitted

## OPERATOR decision and limits

OPERATOR explicitly approved:
AUTHORIZE_KOO_PREPARE_KOD_SECE_R02_OFFLINE_RUNTIME_HANDOFF = YES

This authorizes KOO to PREPARE this addressed handoff only. It is not authority to deliver/activate it automatically or execute tests. Before execution a separate explicit OPERATOR authorization, safe runner definition, and KOD fresh Resume-First, writer/currentness, source and task gates are mandatory. No production/live/sandbox target authority is created.

## Exact immutable task basis

Prepared task design:
puev5691/wellbeing-hq@5a0ece95a8955041d3e8fcf45e3c48d21a6cc0da:
entities/koordinator/outbox/KOO__SECE-R02-offline-combined-runtime-task-preparation__OPERATOR.md
blob bafc0e4181b5baa2db868c5adedd0c59fcd016b9

KOO reconciliation:
puev5691/wellbeing-hq@bd23339a2e45265b32a348f87d08645641ed884e:
entities/koordinator/outbox/KOO__SECE-sandbox-implementation-R02-static-rereview-reconciliation__OPERATOR.md
blob 6d3b83e7fe9e6dbb4d9e6a4d73bc5166f77cbb0a

SHD independent static R02 rereview:
puev5691/wellbeing-hq@7bc69dc25a1e6c4646f467710bbe4e00284c097e:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02-rereview-r01__KOO.md
blob 59ba58a2cea3b6ae6cc3dad6cd7b760456555f26
terminal PASS_SHD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R02_REREVIEW_R01
boundary: STATIC_OFFLINE_REVIEW_ONLY

KOD R02 implementation result:
puev5691/wellbeing-hq@36e2d03c17063722c7c0a72ab6ef56f26b1a1d9b:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02__KOO.md
blob bcf282a0e69a2e1272ca885be379798423a76e57

Exact candidate:
puev5691/wellbeing-hq@1752adb514e3bfa772ef22e25804f2b8ef7636b8:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-correction-r02/
tree 65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade
recursive blobs 58

KOD current writer:
entities/koder/current/KOD__replacement-current-writer-v07.md
blob 5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e
status CURRENT_WRITER_ESTABLISHED

KOD external recovery:
puev5691/wellbeing-entity-bootstrap@b3e720a8acfe16e2e15b70cde4c5989e552f756b:
entities/kod/recovery/versions/kod-recovery-v09
tree 7ae634672118887630c7df730525ebac3b659dba

SHD external recovery:
puev5691/wellbeing-entity-bootstrap@ce702f2e01bc2a9a4698f08690cf60548d855e31:
entities/shd/recovery/versions/shd-recovery-r06
tree 6ec5560cdb76d04bab02b7b55390dbc2c70b3fd5

## Proposed bounded task, NOT YET AUTHORIZED FOR EXECUTION

Objective: reproduce the exact R02 pure/mock suite and offline combined R04 runtime + R02 sandbox-wrapper integration, using controlled non-live mock/simulation inputs only. Distinguish KOD's historical recorded 38/38 from newly executed test evidence.

Before execution:
- verify all exact immutable source/blob/tree identities and no supersession;
- verify KOD instance continuity/current writer and applicable execution authority;
- establish and document a safe offline runner, toolchain/dependencies and fixture identities; if safe non-live execution cannot be proven, STOP and return blocker;
- ensure test harness cannot select real sandbox target or mutate a real filesystem object as an effect; permitted temporary runner infrastructure must be separately scoped and controlled, not misreported as a SECE sandbox effect.

When and only when separately authorized, execute bounded reproducible offline mock/simulation tests:
1. Exact R02 pure/mock suite with commands, logs, counts, failures and hashes.
2. Combined runtime binding and positive admission under mock/simulation.
3. Negative fail-closed cases: forged/stale root and binding identities; exact profile/constants mismatch; no-symlink evidence missing; cleanup operation/owner/root/target mismatch; pre-effect admission and invocation revalidation; outcome UNKNOWN/UNRESOLVED, no unsafe retry or destructive cleanup.
4. Check unchanged R04 runtime and baseline core identities; distinguish static assumptions, actual mock observations and untested boundaries.
5. Return one immutable evidence result to KOO, including reproducibility details, exact inputs, observed PASS/NEEDS_REWORK/BLOCKED and unresolved cases. Read back and report commit/blob.

Do not modify candidate; do not activate/deploy; do not select target; do not run real sandbox effect; do not infer combined-runtime PASS from static review or KOD's historical test report. No G4/G5/G6, no production/live action, no automated activation, no historical task replay.

## STOP conditions and next gate

Stop on competing writer/task, changed immutable input, missing safe runner evidence, missing explicit execution authority, actual/non-live boundary ambiguity, or conflicting active sources. Return exact blocker.

This handoff remains PREPARED_NOT_ACTIVATED until a separate OPERATOR decision authorizes KOD execution under verified conditions. No claim of delivery, receipt or acceptance.

terminal: KOD_SECE_R02_OFFLINE_COMBINED_RUNTIME_HANDOFF_PREPARED_ONLY
