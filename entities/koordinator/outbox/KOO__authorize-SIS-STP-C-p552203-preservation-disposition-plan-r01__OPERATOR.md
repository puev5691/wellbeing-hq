# KOO record: authorize SIS p552203 preservation/disposition plan r0.1

status: OPERATOR_READ_ONLY_PRESERVATION_DESIGN_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR selected:
DESIGNATE_P552203_STPC_DISPOSABLE_CONDITIONAL_PRESERVATION_FIRST

Exact decision record:
puev5691/wellbeing-hq@020efa139071f5a73b3501d3c00d394daf75c588:
entities/koordinator/outbox/KOO__STP-C-p552203-disposable-designation-selected-r01__OPERATOR.md

Scope:
READ_ONLY_DATA_INVENTORY_AND_PRESERVATION_DISPOSITION_PLAN

Authorized:
- fresh read-only inventory of /data/wellbeing-lab and /opt/wb-shard-gateway;
- classify contents by preserve / discardable / unknown;
- identify project/recovery/live dependency evidence;
- identify secret-bearing paths without exposing secret contents;
- prepare preservation targets/requirements and dependency verification plan;
- identify exact later mutation authority needed.

Not authorized:
- delete/move/copy/modify data;
- expose secret contents;
- create proof roots;
- reset/reimage VM;
- install/run backends;
- execute T01-T20;
- live WRITE/CAS;
- CHECKPOINT_DURABLE.
