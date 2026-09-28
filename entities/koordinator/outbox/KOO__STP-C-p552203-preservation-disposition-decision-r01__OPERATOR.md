# KOO → OPERATOR: p552203 preservation/disposition decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Exact SIS result:
puev5691/wellbeing-hq@cdfcc3186b404584c4d6c2a726dd4f853e73e99b:
entities/sisadmin/outbox/SIS__STP-C-p552203-preservation-disposition-plan-r01__KOO.md
blob 99857883d03bff78a97bd8aea7d1ee20425f7bf0

Proposed exact disposition:

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

SECRETS RULE:
- /data/wellbeing-lab/secrets is currently observed empty but remains secret-bearing.
- At the future mutation boundary it must be rechecked by metadata/count only.
- If still empty: it may be treated as discardable.
- If non-empty: STOP; no publication/copy to public/project Git; require separate secret-capable preservation decision.

GATEWAY RULE:
- /opt/wb-shard-gateway must be preserved before destructive action.
- installed wellbeing-shard-gateway-verify.service and its external runtime paths must be checked/retired by a separate bounded dependency-retirement gate before reset/reimage.
- current inactive/disabled state is not itself retirement authority.

This decision does NOT authorize:
- copy/archive;
- deletion;
- move;
- service removal;
- root creation;
- reset/reimage;
- backend install/run;
- T01-T20;
- CHECKPOINT_DURABLE.

Decision token:

APPROVE_P552203_PRESERVATION_DISPOSITION_R01_PRESERVE_REQUIRED_ACCEPT_DISCARDABLE_SECRETS_FAIL_CLOSED

Alternative:

DEFER_P552203_PRESERVATION_DISPOSITION_R01
