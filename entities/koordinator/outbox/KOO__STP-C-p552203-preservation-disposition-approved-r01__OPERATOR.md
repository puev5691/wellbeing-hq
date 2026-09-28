# KOO record: OPERATOR approves p552203 preservation/disposition r0.1

status: OPERATOR_PRESERVATION_DISPOSITION_APPROVED
project_time: omitted

Exact OPERATOR token:

APPROVE_P552203_PRESERVATION_DISPOSITION_R01_PRESERVE_REQUIRED_ACCEPT_DISCARDABLE_SECRETS_FAIL_CLOSED

Exact SIS plan:
puev5691/wellbeing-hq@cdfcc3186b404584c4d6c2a726dd4f853e73e99b:
entities/sisadmin/outbox/SIS__STP-C-p552203-preservation-disposition-plan-r01__KOO.md
blob 99857883d03bff78a97bd8aea7d1ee20425f7bf0

Approved disposition:

PRESERVE_REQUIRED:
- /data/wellbeing-lab/backups/shd-pre-reinit-v01
- /data/wellbeing-lab/reports
- /opt/wb-shard-gateway

ACCEPT_AS_DISCARDABLE_AFTER_PRESERVATION:
- /data/wellbeing-lab/repos/wellbeing-hq
- /data/wellbeing-lab/tmp/shd-emergency-failover-v02-readback
- empty /data/wellbeing-lab/artifacts
- empty /data/wellbeing-lab/logs
- empty /data/wellbeing-lab/scripts

SECRETS_FAIL_CLOSED:
- /data/wellbeing-lab/secrets was observed empty;
- future mutation boundary must recheck only existence/count/metadata;
- if still empty, it may be treated as discardable;
- if non-empty, STOP and require separate secret-capable preservation decision;
- no secret content may be published to project/public Git or echoed into chat/logs.

GATEWAY_DEPENDENCY:
- /opt/wb-shard-gateway must be preserved before destructive action;
- installed wellbeing-shard-gateway-verify.service and related runtime paths require a separate dependency-retirement gate before reset/reimage.

This decision does NOT authorize:
- copy/archive;
- move/delete;
- service removal;
- proof-root creation;
- reset/reimage;
- backend install/run;
- T01-T20 execution;
- live WRITE/CAS;
- CHECKPOINT_DURABLE.
