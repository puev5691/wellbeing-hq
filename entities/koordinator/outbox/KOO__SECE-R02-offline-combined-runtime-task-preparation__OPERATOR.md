# KOO: SECE R02 offline combined-runtime task preparation

status: PREPARED_NOT_AUTHORIZED_FOR_EXECUTION
entity: KOO / КООРДИНАТОР r1.4
scope: OFFLINE_COMBINED_RUNTIME_TASK_DESIGN_ONLY
project_time: omitted

## Exact OPERATOR decision

AUTHORIZE_KOO_PREPARE_SECE_R02_OFFLINE_COMBINED_RUNTIME_TASK = YES

This grants preparation only, not execution, target selection, candidate acceptance, production use, or automatic activation. OPERATOR confirmed KOO r1.4 instance continuity earlier in this conversation.

## Immutable basis

KOO reconciliation:
puev5691/wellbeing-hq@bd23339a2e45265b32a348f87d08645641ed884e:
entities/koordinator/outbox/KOO__SECE-sandbox-implementation-R02-static-rereview-reconciliation__OPERATOR.md
blob: 6d3b83e7fe9e6dbb4d9e6a4d73bc5166f77cbb0a
terminal: PASS_KOO_SECE_R02_STATIC_REREVIEW_RECONCILIATION

SHD independent static rereview:
puev5691/wellbeing-hq@7bc69dc25a1e6c4646f467710bbe4e00284c097e:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02-rereview-r01__KOO.md
blob: 59ba58a2cea3b6ae6cc3dad6cd7b760456555f26
terminal: PASS_SHD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R02_REREVIEW_R01

KOD correction result:
puev5691/wellbeing-hq@36e2d03c17063722c7c0a72ab6ef56f26b1a1d9b:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02__KOO.md
blob: bcf282a0e69a2e1272ca885be379798423a76e57

Immutable R02 candidate:
puev5691/wellbeing-hq@1752adb514e3bfa772ef22e25804f2b8ef7636b8:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-correction-r02/
tree: 65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade
recursive_blob_count: 58

SHD recovery r06:
puev5691/wellbeing-entity-bootstrap@ce702f2e01bc2a9a4698f08690cf60548d855e31:
entities/shd/recovery/versions/shd-recovery-r06
tree: 6ec5560cdb76d04bab02b7b55390dbc2c70b3fd5

KOD recovery v09:
puev5691/wellbeing-entity-bootstrap@b3e720a8acfe16e2e15b70cde4c5989e552f756b:
entities/kod/recovery/versions/kod-recovery-v09
tree: 7ae634672118887630c7df730525ebac3b659dba

## Proposed one-task execution specification (not activated)

Proposed recipient: KOD / КОДЕР, as implementation and test owner, subject to separate authority, writer and recovery/currentness checks. Independent reproduction or review by a distinct authorized specialist is a separate decision, not implied by this task.

Objective: produce reproducible evidence of R02 combined runtime behavior on immutable offline mock/simulation inputs, with the R04 runtime baseline and R02 sandbox wrapper integrated; do not prove or claim real sandbox effects.

Exact scope:
1. Read exact R02 tree and baseline blobs; verify identity before execution. Work in a separately controlled non-live environment only after explicit execution authority. Never modify the immutable candidate.
2. Record toolchain, platform, command lines, dependency versions, fixture identity and deterministic input/output artifacts.
3. Execute the exact R02 pure/mock test suite and combined offline runtime integration scenarios; distinguish existing KOD-declared 38/38 from newly observed results.
4. Cover positive admission and negative/fail-closed cases: forged/stale root and binding IDs; exact profile/constants; no-symlink evidence; cleanup operation/owner/root/target mismatches; pre-effect admission and invocation revalidation; outcome UNKNOWN/UNRESOLVED; no unsafe retry or destructive cleanup.
5. Preserve R04 baseline behavior and ensure non-live boundary, candidate NOT_ACTIVATED, no target selection, no real filesystem effect, no G4/G5/G6.
6. Return one immutable evidence package with commands, outputs, test counts, failures, hashes/locators, observed vs inferred classifications, and PASS/NEEDS_REWORK/BLOCKED. If a test would cross into real sandbox/filesystem effects or need a concrete target, STOP that case rather than silently expanding scope.

Acceptance conditions for this proposed task:
- exact immutable candidate/source set and execution environment recorded;
- reproducible offline mock/simulation run evidence, not only static inspection;
- negative tests actually executed with fail-closed outcomes;
- no real sandbox effect, no activation, no target selection;
- no claim of production suitability or G4/G5/G6 authority;
- distinct runtime claims and limits explicitly stated.

## Authority boundary and next decision

No execution has been authorized or started by this preparation.
No runner/host is selected; feasibility of a strictly non-live environment is not established by this document.
KOD writer and currentness must be checked before any execution handoff.
A separately authorized execution task and safe runner definition are required before the proposed tests can run.
No automatic activation, no historical replay, no canon rewrite.

terminal: SECE_R02_OFFLINE_COMBINED_RUNTIME_TASK_PREPARED_FOR_OPERATOR_DECISION
