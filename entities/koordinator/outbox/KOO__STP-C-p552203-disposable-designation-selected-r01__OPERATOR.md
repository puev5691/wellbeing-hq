# KOO record: OPERATOR selects conditional disposable designation for p552203

status: OPERATOR_DISPOSABLE_DESIGNATION_RECORDED
project_time: omitted

Exact OPERATOR token:

DESIGNATE_P552203_STPC_DISPOSABLE_CONDITIONAL_PRESERVATION_FIRST

Exact VM:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Meaning:
- this exact VM is designated as the intended future STP-C disposable proof environment;
- designation is CONDITIONAL and PRESERVATION-FIRST;
- designation alone does NOT authorize reset, erase, reimage, storage-root creation, backend install/run, or T01-T20 execution.

Mandatory before any destructive mutation:
1. inventory all existing relevant data under /data/wellbeing-lab and /opt/wb-shard-gateway;
2. classify each item as preserve / discardable / unknown;
3. identify live/recovery/project dependencies;
4. preserve required material to a separately verified safe locator/version before deletion;
5. keep secrets out of public/project artifacts;
6. verify absence of live dependency on this VM;
7. only then request separate exact mutation authority for proof-root creation/reset.

Current M5/M6 effect:
- M5 advances from no-designation blocker to CONDITIONAL_DESIGNATION_ESTABLISHED, but is not yet fully closed as disposable until preservation/dependency checks complete;
- M6 remains BLOCKED / ROOT_NOT_CREATED_AND_NO_ISOLATED_STORAGE_BOUNDARY.

Hard boundary:
- no erase/reset/reimage;
- no root creation;
- no backend install/run;
- no T01-T20;
- no live WRITE/CAS;
- no CHECKPOINT_DURABLE.
