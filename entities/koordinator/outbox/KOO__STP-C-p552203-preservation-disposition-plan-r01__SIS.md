# KOO → SIS: p552203 preservation/disposition plan r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: READ_ONLY_DATA_INVENTORY_AND_PRESERVATION_DISPOSITION_PLAN
project_time: omitted

Resume-First.

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Exact authority:

puev5691/wellbeing-hq@2e22f2eaf1107aad789fff58ff45419bda502e34:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-p552203-preservation-disposition-plan-r01__OPERATOR.md

Exact designation:

puev5691/wellbeing-hq@020efa139071f5a73b3501d3c00d394daf75c588:
entities/koordinator/outbox/KOO__STP-C-p552203-disposable-designation-selected-r01__OPERATOR.md

Exact VM:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Do only fresh read-only inventory and preservation/disposition planning.

Inspect:
- /data/wellbeing-lab
- /opt/wb-shard-gateway

Required result:

1. inventory top-level and materially relevant nested content;
2. classify each meaningful item:
   PRESERVE_REQUIRED
   DISCARDABLE_CANDIDATE
   UNKNOWN_NEEDS_DECISION
3. identify evidence of live/runtime/project/recovery dependency;
4. identify secret-bearing paths by locator/name only; do NOT reveal secret contents;
5. identify what must be preserved before any destructive action;
6. propose safe preservation destination classes/requirements without copying yet;
7. state whether any current dependency prevents disposable conversion;
8. state exact later mutation authority needed for:
   - preservation copy/move if required;
   - proof-root creation;
   - cleanup/reset/reimage.

Do NOT:
- delete;
- move;
- copy;
- edit;
- expose secret values;
- create directories;
- create proof roots;
- stop/start services;
- mutate network/storage;
- install/run backend;
- execute T01-T20.

Expected terminal:

PASS_SIS_STP_C_P552203_PRESERVATION_DISPOSITION_PLAN_R01_READY_FOR_OPERATOR_DECISION

or exact BLOCKED_/FAIL_.

After immutable result + exact readback + return KOO, STOP.
