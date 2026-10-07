# ARH execution evidence — ARH_KOD_V07_EXTERNAL_RECOVERY_R01_A1 PROCESSING_STARTED E1

profile_id: CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01
execution_attempt_id: ARH_KOD_V07_EXTERNAL_RECOVERY_R01_A1
event_id: ARH_KOD_V07_EXTERNAL_RECOVERY_R01_A1_PROCESSING_STARTED_E1
event_class: PROCESSING_STARTED
processing_started: YES
project_time: omitted

## Exact authority/frontier

authority:
puev5691/wellbeing-hq@2a5080d2cd736670bf06ea594cf5b3d336b61f41:
entities/koordinator/outbox/ARH_KOD_v07_external_recovery_authority.md

authority_blob:
3d0a47c93cff551322240fa7503090a35f168efc

frontier:
puev5691/wellbeing-hq@c7bff8dd4a77ed62689ce6bf3298fe6167dc25bb:
entities/koordinator/outbox/ARH_KOD_v07_external_recovery_frontier.md

frontier_blob:
34c863899cfd621899f82c3a040470b9bba595f1

accepted_state:
INITIAL_NOT_STARTED_V1

## Exact source state

source_snapshot_commit:
84b468944a569eef7d2411366f4773c714d86de6

source_snapshot:
entities/koder/outbox/KOD__v07-pre-sandbox-implementation-self-snapshot__KOO-ARH.md

source_snapshot_blob:
c7ed1f606e87b843149732f4601edcffa559a4b8

source_writer:
entities/koder/current/KOD__replacement-current-writer-v07.md

source_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

source_writer_status:
CURRENT_WRITER_ESTABLISHED

previous_recovery_ref:
51704f5eb7a4bf43210c9760905f486a2e58b5ce

target_path:
entities/kod/recovery/versions/kod-recovery-v07

## Actor

actor_entity:
ARH / АРХИВАРИУС

ARH_writer:
entities/archivarius/current/ARH__replacement-current-writer-r03.md

ARH_writer_blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

ARH_writer_status:
WRITER_ESTABLISHED

## Fresh pre-start checks

HQ_HEAD:
d8dc287c29784b8d3c0654de8e86bcd83117abcc

authority:
PASS

registry:
PASS

frontier:
PASS

source_snapshot:
PASS

source_writer:
PASS

previous_recovery_v06:
PASS

target_v07_absent:
PASS

competing_attempt_result_registry:
NONE_FOUND

source_set_r07:
PASS

KOD_R04_identity:
PASS

SHD_R04_identity:
PASS

SIS_R07_identity:
PASS

SHD_D1D2_identity:
PASS

sandbox_implementation:
NOT_CREATED

G4_authority:
NOT_CREATED

G5_authority:
NOT_CREATED

G6_authority:
NOT_CREATED

## Scope started

EXTERNAL_RECOVERY_PRESERVATION:
STARTED

SANDBOX_IMPLEMENTATION:
NOT_STARTED

G4_G5_G6:
NOT_STARTED

WRITER_MUTATION:
NOT_STARTED

terminal:
PASS_ARH_KOD_V07_EXTERNAL_RECOVERY_R01_PROCESSING_STARTED
