# ARH recovery registry — KOO recovery r1.3

status: EXTERNALLY_PRESERVED_READBACK_PASS
entity: KOO / КООРДИНАТОР
project_time: omitted

## Source snapshot

source_snapshot:
puev5691/wellbeing-hq@0178dde20cca04fc1d8d5147d9c32addac87b616:
entities/koordinator/outbox/koo-emergency-preparation-r13/KOO__emergency-preparation-self-snapshot-r13.md

source_snapshot_blob:
bf8144c5bd9365f9096c03ea92deee8ea37a8d8b

source_writer:
entities/koordinator/current/KOO__replacement-current-writer-r12.md

source_writer_blob:
b68e1dd2e79781f4ea8fab7e48e7456fada14c80

source_writer_status:
WRITER_ESTABLISHED

global_pause:
puev5691/wellbeing-hq@d15850fee62634a507d3e4473d19e8cfd43b6e31:
entities/koordinator/current/KOO__global-pause-emergency-initiation-preparation-r13.md

global_pause_blob:
10522b06a9f3a58298823a2a251df1b9859e8aad

global_pause_status:
GLOBAL_PROFILE_TASK_PAUSE_ACTIVE

## Recovery lineage

previous_external_recovery:
puev5691/wellbeing-entity-bootstrap@122fcd2172781cc87e2cc15afc46f715193f63db:
entities/koo/recovery/versions/koo-recovery-r12

previous_package_tree:
aee471b4388224842b1d052e6e9951eeb1090eac

new_external_recovery:
puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:
entities/koo/recovery/versions/koo-recovery-r13

external_package_tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

## Composition / integrity

composition:
5/5 PASS

copied source Git blob identity:
3/3 PASS

external immutable readback:
5/5 PASS

Exact external blobs:
- KOO__emergency-preparation-self-snapshot-r13.md — bf8144c5bd9365f9096c03ea92deee8ea37a8d8b
- KOO__global-pause-emergency-initiation-preparation-r13.md — 10522b06a9f3a58298823a2a251df1b9859e8aad
- KOO__human-interface-contract-r02.md — fdea31034c370220dfb961993059500716ccfe20
- KOO__recovery-lineage-r13.md — ef59f6f8ecbe32a99b774f5f67e4a0d55a3315c1
- RECOVERY-MANIFEST.md — f5bced3e27b024cc7e45366c52b5d54ea3ed4e89

## Recoverability / stale notes

r13 is the newest externally preserved KOO recovery successor.

It captures fresher KOO r1.2 durable state after r12, including:
- GLOBAL_PROFILE_TASK_PAUSE_ACTIVE;
- latest SHD rereview terminal NEEDS_REWORK;
- pending KOO R03 decision gate with decision NOT_GIVEN;
- PAUSED_NON_EXECUTABLE disposition;
- no KOD R03 task authority;
- no SIS combined-package execution authority;
- no activation/deployment/live-effect authority.

Historical tasks/prompts/queues remain non-authoritative for execution.

After any future Writer Gate, fresh reconciliation is mandatory.

## Authority boundary

KOO r1.2 freeze/retire:
NOT_PERFORMED

replacement Initiation Gate:
NOT_PERFORMED

replacement Writer Gate:
NOT_PERFORMED

profile work resume:
NOT_PERFORMED

historical replay:
NONE

Project Source/canon mutation:
NONE

cold-start activation:
NOT_PERFORMED
