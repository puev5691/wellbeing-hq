# ARH execution evidence — ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_A1 PROCESSING_STARTED E1

profile_id: CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01
execution_attempt_id: ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_A1
event_id: ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_A1_PROCESSING_STARTED_E1
event_class: PROCESSING_STARTED
processing_started: YES
project_time: omitted

## Exact authority/frontier

authority:
puev5691/wellbeing-hq@3a0292a49d396fc498467e17fe768eaa594b0411:
entities/koordinator/outbox/ARH_SHT_r02_post_writer_external_recovery_R03_authority.md

authority_blob:
3055cad5e47a03be2d6a90d48fa34906896a0fce

frontier:
puev5691/wellbeing-hq@fdeb7a240bcc31da190f8e3aea51e88668ba4157:
entities/koordinator/outbox/ARH_SHT_r02_post_writer_external_recovery_R03_frontier.md

frontier_blob:
041cccc62ba26b022c30027bf1072d782f4fc34b

accepted_state:
INITIAL_NOT_STARTED_V1

## Exact source state

source_snapshot_commit:
f0a49469c6b318df0d1b436c011f1f459df29f47

source_snapshot:
entities/shtabist/outbox/SHT__replacement-r02-post-writer-self-snapshot__KOO-ARH.md

source_snapshot_blob:
6d48804adfb190d211ffea7c20f80fbde0135e64

source_writer_commit:
7ed8b5570d3aa610120ab4a541b4d03ca032cf3b

source_writer:
entities/shtabist/current/SHT__replacement-current-writer-r02.md

source_writer_blob:
591a5c474523f46ad84b5c49c62939832b87b15c

source_writer_generation:
SHT-REPLACEMENT-R02

previous_recovery_ref:
c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5

target_path:
entities/sht/recovery/versions/sht-recovery-r03

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
1dd9b9770f3f8dd2c7335bb6eaef8fa2ca1a9788

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

writer_gate_result:
PASS

previous_recovery_r02:
PASS

target_r03_absent:
PASS

competing_attempt_or_result:
NONE_FOUND

competing_registry:
NONE_FOUND

profile_continuation:
PAUSED_BY_OPERATOR

narrow_rereview:
NOT_AUTHORIZED

## Scope started

EXTERNAL_RECOVERY_PRESERVATION:
STARTED

PROFILE_WORK:
NOT_STARTED

SECE_CONTINUATION:
NOT_STARTED

WRITER_MUTATION:
NOT_STARTED

terminal:
PASS_ARH_SHT_R02_POST_WRITER_EXTERNAL_RECOVERY_R03_PROCESSING_STARTED
