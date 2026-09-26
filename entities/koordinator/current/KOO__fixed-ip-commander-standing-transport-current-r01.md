# KOO current state: fixed-IP → Commander standing transport r0.1

status: STANDING_TRANSPORT_ACTIVE_PER_ACTION_AUTHORITY_REQUIRED
project_time: omitted

Authority:
puev5691/wellbeing-hq@e58b964f0f8c490f2ee228faa8b9581dcfe20013:
entities/koordinator/outbox/KOO__authorize-fixed-ip-commander-standing-transport-r01__OPERATOR.md

Standing use allowed:
- fresh route/currentness verification;
- exact router/profile identity verification;
- fresh Commander inventory/device availability verification;
- explicit logical node/device selection;
- CONTROL_PATH_READY selection result.

Current mapping:
- burzh -> ruvds-xnqc6 -> dd09a197-f716-4dd6-80bb-7f8e5d8260ff
- mazhor -> p552203.kvmvps -> 830038a0-232b-4d83-b52d-0e9973126165
- erefia -> ruvds-ygo0w -> c55d5659-f2c8-416d-8b40-9bac8c80c30d

Current node policy:
burzh -> mazhor -> erefia

Every actual Commander host action still requires separate exact task/action authority with exact action_id, node, device_id, scope/currentness and required operator confirmation.

Missing or mismatched authority => STOP.

Not granted:
- generic host-command authority;
- standing host mutation;
- automatic failover;
- autonomous node switching;
- automatic IP discovery/admission;
- DNS fallback;
- provider/credential authority;
- shard WRITE;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

Live proof basis:
puev5691/wellbeing-hq@c732d3df298418f302bec67f5efda4bdbabaa0f9:
entities/sisadmin/outbox/SIS__fixed-ip-commander-live-proof-r01__KOO.md
blob c8057e6c868bbbd93757bdc6acf5c0d47305732a

terminal: PASS_KOO_FIXED_IP_COMMANDER_STANDING_TRANSPORT_R01_ACTIVE_PER_ACTION_AUTHORITY_REQUIRED
