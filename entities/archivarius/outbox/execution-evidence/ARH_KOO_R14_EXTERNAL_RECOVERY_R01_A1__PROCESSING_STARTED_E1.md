# ARH KOO recovery r14 — PROCESSING_STARTED

attempt:
ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1

status:
PROCESSING_STARTED

scope:
EXTERNAL_RECOVERY_PRESERVATION_READBACK_AND_COLD_START_PREPARATION_ONLY

project_time:
omitted

## Exact authority and accepted frontier

task:
puev5691/wellbeing-hq@cadb19b2e2e5a4c1db008565330b2d51d1fad420:entities/koordinator/outbox/KOO__ARH-KOO-r14-external-recovery__ARH.md

task_blob:
1b303f63fb4dc08306eb507b84977da14d6845a1

authority:
puev5691/wellbeing-hq@2729c7ad066ad1ba5dc7dc802db2c96fc995a3dc:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_authority.md

authority_blob:
3a92721b8a12ebe3d20632d610130ecccca5cb14

authority_status:
OPERATOR_TASK_AUTHORITY_RECORDED

registry:
puev5691/wellbeing-hq@fd0e8f1a3cfb05fcafc807b902fa50fbf6328e67:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_registry.md

registry_blob:
003e2ea1e282de130961d241031bf4eb760a0987

registry_state:
INITIAL_NOT_STARTED

frontier:
puev5691/wellbeing-hq@026ac6db4b3eec5d2c1263e195147c981a9ed8e6:entities/koordinator/outbox/ARH_KOO_r14_external_recovery_frontier.md

frontier_blob:
3bab160572ffef647c902eff1dddfabf1858fbbd

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven_before_this_artifact:
NO

start_proven_after_this_artifact:
YES

## Current writers and source snapshot

ARH_current_writer:
puev5691/wellbeing-hq@cadb19b2e2e5a4c1db008565330b2d51d1fad420:entities/archivarius/current/ARH__replacement-current-writer-r03.md

ARH_writer_blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

ARH_writer_status:
WRITER_ESTABLISHED

KOO_source_snapshot:
puev5691/wellbeing-hq@5795ac734b4f6af1b948911c6da7f907d9a0427b:entities/koordinator/outbox/koo-planned-handoff-r14/KOO__planned-chat-replacement-self-snapshot-r14.md

source_snapshot_blob:
8a39b17be502cfa4f356e69fb6f6374fdc2b5029

source_snapshot_terminal:
PASS_KOO_R13_SELF_SNAPSHOT_R14_READY_FOR_ARH_PRESERVATION

KOO_current_writer:
puev5691/wellbeing-hq@210cdf8c3268d5bbb31b0fa7b344a4a14edd22dd:entities/koordinator/current/KOO__replacement-current-writer-r13.md

source_writer_blob:
5208fd71173b8258dfc0ef0ccd8dd21f07b6bdb1

source_writer_status:
WRITER_ESTABLISHED

## Previous and target recovery

previous_external_recovery:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:entities/koo/recovery/versions/koo-recovery-r13

previous_recovery_tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

previous_recovery_disposition:
LAST_EXTERNALLY_VERIFIED_KOO_RECOVERY_BUT_STALE_RELATIVE_TO_LATER_KOO_R13_WORK

target_repository:
puev5691/wellbeing-entity-bootstrap

target_path:
entities/koo/recovery/versions/koo-recovery-r14

target_absence_precheck:
PASS

competing_r14_attempt_result_registry_precheck:
PASS

## Fresh pre-write checks

HQ main HEAD:
cadb19b2e2e5a4c1db008565330b2d51d1fad420

Bootstrap main HEAD:
b3e720a8acfe16e2e15b70cde4c5989e552f756b

ARH current-writer exact blob and status:
PASS

No competing ARH current-writer or ARH r14 attempt/result:
PASS

KOO r1.3 current-writer exact blob and status:
PASS

KOO r14 source self-snapshot exact blob and terminal:
PASS

No KOO r1.4 initiation result:
PASS / NOT_FOUND

No KOO r1.4 current-writer:
PASS / NOT_FOUND

No external KOO recovery r14:
PASS / NOT_FOUND

Active Project Sources:
R07 / PASS

Project Core v2.5:
a42f7dca6a7469a54fa2da24aae0da4e549c9d33

Entity Roles v2.4:
1772339cb74dae8550bfbd2e33401c34a929e911

File Work Canon v2.4:
e9c29d62057f34e4f771d6057a36d9b7f72e74c2

Source Loading Policy v2.2:
69eb657f260a019f76e8e707c880ea88c1dfa0bf

Recovery Canon v1.6:
233117e1c9509d730e1f5ec532b1cabe3f786609

Task Conveyor Canon v1.2:
df7896d867eeeffff506319538fedad938856686

Task Conveyor v1.3:
NOT_ACTIVE

Current global profile-task pause:
GLOBAL_PROFILE_TASK_PAUSE_RELEASED

SECE primary priority:
ACTIVE_COORDINATION_DECISION

KOD recovery:
v09 / CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_POST_SANDBOX_IMPLEMENTATION_CORRECTION_R02

KOD R02 candidate:
NOT_ACTIVATED

Real sandbox effect:
NOT_EXECUTED

R02 combined runtime PASS:
NOT_INFERRED

Current SHD writer:
replacement-r0.4 / AUTHORITATIVE_CURRENT_WRITER

Current SHD recovery:
r05 / STALE_RELATIVE_TO_LATER_SHD_R01_IMPLEMENTATION_REVIEW

Prepared SHD preservation tail:
PREPARED_NOT_ACTIVATED

Prepared SHD frontier:
current path blob 81082bc94bf8db76196139626291409bef853f7c

Known internal locator discrepancy:
the prepared SHD task blob e10657752889c84a9c01ed1621aa9ec8b075adda cites frontier blob b16894c2119bbac96f8a49e607ad25b28d950fc0, which is not retrievable; KOO self-snapshot and current HQ path identify 81082bc94bf8db76196139626291409bef853f7c. This subordinate SHD tail remains historical frontier evidence pending fresh reconciliation and MUST NOT be replayed.

SHD prepared-tail start_proven:
NO

SHD PROCESSING_STARTED:
NOT_FOUND

SHD self-snapshot result for this attempt:
NOT_FOUND

SHD recovery r06:
NOT_FOUND

SHD R02 rereview:
NOT_AUTHORIZED / NOT_PERFORMED

G4/G5/G6 authority:
NOT_CREATED

Historical PROMPT/task/queue replay:
FORBIDDEN

## Start boundary

All exact ARH r14 preconditions required before substantive preservation were freshly checked against the current main refs. This artifact is the positive start event for this exact attempt only.

No external recovery content has yet been published by this start record.
No KOO authoritative current-state was mutated.
No Project Source/canon was mutated.
No replacement Initiation Gate or Writer Gate was executed.
No SHD task was activated.
No historical task/PROMPT/queue was replayed.
No sandbox, deployment, provider, API, Telegram, or live effect was performed.

terminal:
PROCESSING_STARTED_ARH_KOO_R14_EXTERNAL_RECOVERY_R01_A1
