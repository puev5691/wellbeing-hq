# KOO -> ARH: KOO external recovery r14 and replacement cold-start preparation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_READBACK_AND_COLD_START_PREPARATION_ONLY

project_time:
omitted

Resume-First.

Perform ONLY preservation of the exact KOO r1.3 current-writer self-snapshot into one NEW immutable external KOO recovery successor r14, followed by integrity/readback/registry verification and preparation of one cold-start PROMPT for a genuinely NEW KOO r1.4 instance.

The cold-start PROMPT scope is Initiation Gate only.

Do NOT execute replacement Initiation Gate.
Do NOT execute Writer Gate.
Do NOT activate the prepared SHD task.
Do NOT replay historical PROMPT/tasks/queues.
Do NOT mutate KOO authoritative current-state.
Do NOT mutate Project Sources/canons.

## Exact authority

puev5691/wellbeing-hq@2729c7ad066ad1ba5dc7dc802db2c96fc995a3dc:
entities/koordinator/outbox/ARH_KOO_r14_external_recovery_authority.md

blob:
3a92721b8a12ebe3d20632d610130ecccca5cb14

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Registry

puev5691/wellbeing-hq@fd0e8f1a3cfb05fcafc807b902fa50fbf6328e67:
entities/koordinator/outbox/ARH_KOO_r14_external_recovery_registry.md

blob:
003e2ea1e282de130961d241031bf4eb760a0987

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@026ac6db4b3eec5d2c1263e195147c981a9ed8e6:
entities/koordinator/outbox/ARH_KOO_r14_external_recovery_frontier.md

blob:
3bab160572ffef647c902eff1dddfabf1858fbbd

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current ARH writer

entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

status:
WRITER_ESTABLISHED

Fresh-check ARH continuity/currentness before substantive work.

If ARH writer changed/superseded, or competing KOO r14 preservation exists:
STOP with exact blocker.

## Exact authoritative KOO self-snapshot

puev5691/wellbeing-hq@5795ac734b4f6af1b948911c6da7f907d9a0427b:
entities/koordinator/outbox/koo-planned-handoff-r14/KOO__planned-chat-replacement-self-snapshot-r14.md

blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

terminal:
PASS_KOO_R13_SELF_SNAPSHOT_R14_READY_FOR_ARH_PRESERVATION

This is authoritative KOO self-state authored by current KOO r1.3.

Preserve exact bytes.
Do NOT rewrite/reconstruct its substantive KOO state.

## Current KOO writer

puev5691/wellbeing-hq@210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd:
entities/koordinator/current/KOO__replacement-current-writer-r13.md

blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

status:
WRITER_ESTABLISHED

terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R13

## Previous external KOO recovery

puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:
entities/koo/recovery/versions/koo-recovery-r13

tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

ARH registry:

puev5691/wellbeing-hq@f892fadb04a70855a47cfa4f3946303284502586:
entities/archivarius/current/recovery-registry/ARH__KOO-recovery-r13.md

previous status:
EXTERNALLY_PRESERVED_READBACK_PASS

current disposition:
LAST_EXTERNALLY_VERIFIED_KOO_RECOVERY_BUT_STALE_RELATIVE_TO_LATER_KOO_R13_WORK

Do NOT rewrite/delete r13.

## Target successor

Repository:
puev5691/wellbeing-entity-bootstrap

Create exactly one NEW immutable successor at:

entities/koo/recovery/versions/koo-recovery-r14

Before publication verify the target path does NOT already exist.

If r14 or competing r14 result/registry appears:
STOP exact conflict.

## Mandatory human-interface dependency

Preserve exact Human Interface Contract bytes from the last verified KOO recovery lineage:

puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:
entities/koo/recovery/versions/koo-recovery-r13/KOO__human-interface-contract-r02.md

expected blob:
fdea31034c370220dfb961993059500716ccfe20

The new KOO cold-start PROMPT must require loading and passing this Human Interface Gate before any Writer Gate request.

## Active approved Project Sources

source-set:
R07

activation:
entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

activation_blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Required active identities:
- Project Core v2.5: a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- Entity Roles v2.4: 1772339cb74dae8550bfbd2e33401c34a929e911
- File Work Canon v2.4: e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- Source Loading Policy v2.2: 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- Recovery Canon v1.6: 233117e1c9509d730e1f5ec532b1cabe3f786609
- Task Conveyor Canon v1.2: df7896d867eeeffff506319538fedad938856686

Task Conveyor v1.3:
NOT_ACTIVE

## Current KOO control state to preserve

Old global pause:
HISTORICAL / RELEASED

Current pause release:

puev5691/wellbeing-hq@36af73b6dcb4823e3809216a8e5f77437dd03262:
entities/koordinator/current/KOO__global-profile-task-pause-release-r13.md

blob:
de2edddd2dea3ceb956f890326b3dcb2795984d9

status:
GLOBAL_PROFILE_TASK_PAUSE_RELEASED

SECE priority:

entities/koordinator/current/KOO__semantic-entity-control-engine-r01-priority-decision__OPERATOR.md

blob:
d0521905627b306a4888261a9d414148ac64f265

status:
ACTIVE_COORDINATION_DECISION

SEMANTIC_ENTITY_CONTROL_ENGINE_R01_PRIMARY_PRIORITY:
YES

PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE:
YES

Do NOT restore the old global emergency pause as current state.

## Current SECE/recovery tail to preserve

Current KOD recovery:

puev5691/wellbeing-entity-bootstrap@b3e720a8acfe16e2e15b70cde4c5989e552f756b:
entities/kod/recovery/versions/kod-recovery-v09

tree:
7ae634672118887630c7df730525ebac3b659dba

classification:
CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_POST_SANDBOX_IMPLEMENTATION_CORRECTION_R02

KOD R02 result:

puev5691/wellbeing-hq@36e2d03c17063722c7c0a72ab6ef56f26b1a1d9b:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02__KOO.md

blob:
bcf282a0e69a2e1272ca885be379798423a76e57

R02 package tree:
65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade

candidate:
NOT_ACTIVATED

real_sandbox_effect:
NOT_EXECUTED

R02_combined_runtime_PASS:
NOT_INFERRED

Current SHD writer:

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

blob:
34b1b11d3cf2c607a8399e91ce066423ca3277e9

status:
AUTHORITATIVE_CURRENT_WRITER

Current SHD recovery:

puev5691/wellbeing-entity-bootstrap@78cff4d8fc2a7681b9bf10e4cd5f5f014ec2a7e9:
entities/shd/recovery/versions/shd-recovery-r05

tree:
760d44a757a2842b3643306a1fb82272b2032472

disposition:
STALE_RELATIVE_TO_LATER_SHD_R01_IMPLEMENTATION_REVIEW

## Prepared-but-not-started SHD preservation tail

attempt:
SHD_R04_POST_R01_REVIEW_PRE_R02_REREVIEW_SELF_SNAPSHOT_R01_A1

scope:
PRESERVATION_SELF_SNAPSHOT_ONLY

authority:
puev5691/wellbeing-hq@e7045a117a561d6385f17cc5f075f6eecb775283:
entities/koordinator/outbox/SHD_r04_post_R01_review_pre_R02_rereview_snapshot_authority.md

authority_blob:
5eedf84e785368640dde7497e9e3cbeeb27f582b

registry_blob:
cf671dcb723e225cc4a0b18faf6c76c4145e271f

frontier:
puev5691/wellbeing-hq@98012d8062e4c5b3bb174b142f05f702d0eedb7f:
entities/koordinator/outbox/SHD_r04_post_R01_review_pre_R02_rereview_snapshot_frontier.md

frontier_blob:
81082bc94bf8db76196139626291409bef853f7c

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

task:
puev5691/wellbeing-hq@e75cfe8d40732e736a0c213089f1feee281eb5ad:
entities/koordinator/outbox/KOO__SHD-r04-post-R01-review-pre-R02-rereview-self-snapshot__SHD.md

task_blob:
e10657752889c84a9c01ed1621aa9ec8b075adda

task_status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

Current classification for recovery:
PREPARED_NOT_ACTIVATED / HISTORICAL_FRONTIER_EVIDENCE_PENDING_FRESH_RECONCILIATION

Do NOT present this old PROMPT as automatically executable after recovery.

## Current downstream boundaries

SHD_PROCESSING_STARTED_for_pre_rereview_snapshot:
NOT_FOUND

SHD_recovery_r06:
NOT_CREATED

independent_SHD_R02_rereview:
NOT_AUTHORIZED / NOT_PERFORMED

G4_authority:
NOT_CREATED

G4_execution:
NOT_STARTED

G5_authority:
NOT_CREATED

G6_authority:
NOT_CREATED

historical_replay:
FORBIDDEN

hidden_unwritten_KOO_state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check authority/registry/frontier;
2. verify current ARH writer;
3. verify exact KOO self-snapshot;
4. verify current KOO writer;
5. verify r13 exists and r14 absent;
6. verify no competing KOO r14 attempt/result/registry;
7. verify active source-set r07;
8. verify current pause RELEASED, not active;
9. verify SECE priority current;
10. verify KOD v09 and exact KOD R02 state;
11. verify prepared SHD preservation remains start_proven=NO and no result exists;
12. verify no replacement KOO r1.4 initiation/result/writer already exists.

Then create:

entities/archivarius/outbox/execution-evidence/ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1

authority_blob:
3a92721b8a12ebe3d20632d610130ecccca5cb14

frontier_commit:
026ac6db4b3eec5d2c1263e195147c981a9ed8e6

frontier_blob:
3bab160572ffef647c902eff1dddfabf1858fbbd

accepted_state:
INITIAL_NOT_STARTED_V1

source_snapshot_commit:
5795ac734b4f6af1b948911c6da7f907d9a0427b

source_snapshot_blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

source_writer_blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

previous_recovery_ref:
896b33f99551092bf50f7bef2657e3276d850fc3

previous_recovery_tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

target_path:
entities/koo/recovery/versions/koo-recovery-r14

Immutable-readback PROCESSING_STARTED.

Only then perform preservation.

## Required r14 recovery package

Create exactly one standalone immutable package under:

entities/koo/recovery/versions/koo-recovery-r14

Required composition: 9 files.

1. Exact copy:
KOO__planned-chat-replacement-self-snapshot-r14.md

Must equal source snapshot blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

2. Exact copy:
KOO__replacement-current-writer-r13.md

Must equal source writer blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

3. Exact copy:
KOO__human-interface-contract-r02.md

Must equal expected blob:
fdea31034c370220dfb961993059500716ccfe20

4. SOURCES.md

ARH-owned recovery metadata only.
Record exact active source-set r07 and exact six approved blobs.
Do not copy drafts/candidates as active norms.

5. TASK-STATE.md

ARH-owned recovery metadata only.
Must preserve:
- global pause RELEASED;
- SECE primary priority ACTIVE;
- KOD recovery v09 current;
- KOD R02 candidate non-live;
- SHD recovery r05 stale relative to R01 review;
- prepared SHD preservation attempt as PREPARED_NOT_ACTIVATED;
- start_proven NO;
- SHD R02 rereview NOT_AUTHORIZED / NOT_PERFORMED;
- G4/G5/G6 NOT_CREATED;
- historical replay FORBIDDEN;
- replacement KOO must fresh-reconcile before selecting any task.

6. KOO__recovery-initiation-boundary-r14.md

ARH-owned procedural metadata.
Must state:
- new KOO r1.4 is Initiation-required;
- package_present != initiation_verified;
- initiation_verified != current_writer_established;
- Writer Gate requires separate explicit OPERATOR decision;
- historical PROMPT replay forbidden;
- old global pause must not be resurrected;
- prepared SHD PROMPT is not automatically current after recovery.

7. RECOVERY-LINEAGE.md

Bind:
- predecessor r13 locator/tree;
- current KOO r1.3 writer;
- exact self-snapshot r14;
- Human Interface Contract exact blob;
- current control-state.

8. RECOVERY-MANIFEST.md

List exact composition/provenance/blob/SHA-256 as applicable.

9. SHA256SUMS.txt

Cover every non-checksum file from final bytes.

No unrelated reports inside the external package.

## Integrity / publication

Before publication:
- final composition fixed;
- exact source provenance verified;
- SHA-256 computed after final bytes;
- copied source Git blob identities verified;
- no secrets/private keys/credentials.

Publish exactly to:

puev5691/wellbeing-entity-bootstrap:
entities/koo/recovery/versions/koo-recovery-r14

Record:
- publication commit/ref;
- version path;
- package tree;
- 9/9 composition;
- SHA256SUMS coverage 8/8;
- external blobs.

## Immutable readback

After publication independently read back r14 and verify:
- path -> exact tree;
- composition 9/9;
- self-snapshot external equality PASS;
- current KOO writer external equality PASS;
- Human Interface Contract external equality PASS;
- manifest matches actual package;
- independently recomputed SHA256SUMS 8/8 PASS;
- no missing/extra files;
- no state conflict/supersession.

Publication alone is NOT PASS.

## Recovery registry

Create:

entities/archivarius/current/recovery-registry/ARH__KOO-recovery-r14.md

Include:
- source self-snapshot locator/blob;
- current KOO writer locator/blob/status;
- predecessor r13 locator/tree/stale disposition;
- r14 immutable locator/ref/path/tree;
- 9/9 composition;
- checksum/readback results;
- Human Interface Contract identity;
- source-set r07 identities;
- current pause RELEASED state;
- SECE priority state;
- current KOD v09 state;
- prepared SHD preservation frontier and start_proven NO;
- rereview/G4/G5/G6 boundaries;
- current KOO writer mutation NONE;
- replacement initiation NOT_EXECUTED;
- Writer Gate NOT_EXECUTED;
- historical replay NONE.

Fresh-readback registry.

## Success classification

Return:

EXTERNALLY_PRESERVED_READBACK_PASS

only if all required checks pass.

On PASS classify r14 as:

CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOO_R13_PLANNED_CHAT_REPLACEMENT_R14

Do NOT infer KOO r1.4 initiation or writer authority from preservation.

## Cold-start PROMPT for NEW KOO r1.4

Only after r14 PASS/readback, create:

entities/archivarius/outbox/PROMPT__KOO__replacement-r14-cold-start__OPERATOR.md

This PROMPT must address one genuinely NEW KOO / КООРДИНАТОР r1.4 chat/instance.

Scope:
INITIATION_GATE_ONLY

It must require:

1. Initiation-required, NOT Resume-First.
2. Load current approved Project Sources r07.
3. Read exact r14 self-snapshot, current-writer copy, Human Interface Contract, SOURCES, TASK-STATE, initiation boundary, lineage, manifest and checksums.
4. Verify external locator:
   puev5691/wellbeing-entity-bootstrap@<exact-r14-ref>:
   entities/koo/recovery/versions/koo-recovery-r14
5. Verify exact package tree/composition/checksums and copied blob equality.
6. Fresh-check wellbeing-hq for newer KOO writer/recovery/initiation/supersession evidence.
7. Pass Human Interface Gate.
8. Restore role/constraints/current known state, but DO NOT replay the prepared SHD PROMPT.
9. Classify the prepared SHD preservation tail as historical frontier evidence pending fresh reconciliation.
10. Return one initiation result:
    initiation_verified_waiting_writer_gate
    or exact initiation_loaded_external_unverified / initiation_failed.
11. Do NOT establish current-writer.
12. Do NOT execute profile task.
13. Do NOT create Writer Gate authority.
14. Do NOT mutate authoritative KOO current-state except the Initiation Gate result artifact allowed to that new instance.
15. Return exact initiation result locator/commit/blob and a human-language state summary to OPERATOR.

Expected initiation-result path:

entities/koordinator/outbox/KOO__replacement-r14-initiation-result__OPERATOR.md

A PASS initiation result must state:
Writer Gate = NOT_PERFORMED
profile work = NOT_STARTED
historical replay = NONE

## Required ARH standalone result

Create:

entities/archivarius/outbox/ARH__KOO-r14-external-recovery__KOO-OPERATOR.md

Expected PASS terminal:

PASS_ARH_KOO_R14_EXTERNAL_RECOVERY_AND_COLD_START_PREPARED

Include:
- exact attempt;
- authority/registry/frontier;
- PROCESSING_STARTED;
- source snapshot;
- current KOO writer;
- predecessor r13 disposition;
- r14 locator/ref/path/tree;
- composition/checksum/readback;
- registry locator/commit/blob;
- cold-start PROMPT locator/commit/blob;
- replacement Initiation Gate NOT_EXECUTED;
- Writer Gate NOT_EXECUTED;
- prepared SHD tail NOT_ACTIVATED;
- exact boundaries/UNKNOWNs.

## Hard boundaries

Do NOT:
- establish KOO r1.4 writer;
- execute new KOO Initiation Gate;
- activate SHD preservation task;
- perform SHD R02 rereview;
- create G4/G5/G6 authority;
- mutate KOO/SHD/KOD current-state;
- replay historical tasks/prompts;
- mutate Project Sources/canons;
- perform deployment/live/provider/API/Telegram effects;
- automatically continue downstream.

## Mandatory return

After durable result + immutable readback return one final copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO r1.3

Resume-First.

Include:
- ARH attempt;
- result locator/commit/blob;
- terminal;
- PROCESSING_STARTED locator/blob;
- r14 external recovery locator/ref/path/tree;
- 9/9 composition;
- SHA256SUMS 8/8;
- readback verdicts;
- registry locator/commit/blob;
- cold-start PROMPT locator/commit/blob;
- current KOO writer identity;
- replacement initiation status NOT_EXECUTED;
- Writer Gate status NOT_EXECUTED;
- prepared SHD task NOT_ACTIVATED.

Include exact line:

Fresh-reconcile this exact KOO recovery r14 preservation result. If PASS, the only next action is to open a genuinely NEW KOO r1.4 chat and pass the exact cold-start PROMPT. Do not infer Writer Gate or replay the prepared SHD task.

End:
STOP.

After that block add nothing.
