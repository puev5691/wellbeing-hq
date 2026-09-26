# KOO record: OPERATOR authorizes reusable fixed-IP → Commander transport r0.1

status: OPERATOR_AUTHORITY_RECORDED
project_time: omitted

Exact OPERATOR token:

AUTHORIZE_FIXED_IP_COMMANDER_STANDING_TRANSPORT_R01_PER_ACTION_AUTHORITY_REQUIRED

Meaning:
the verified fixed-IP → Commander path may be reused as an operator-assisted transport/selection mechanism for future exact project tasks.

This authority is standing only for:
- route/currentness verification;
- fresh Commander inventory/device identity verification;
- explicit node/device selection;
- returning CONTROL_PATH_READY for an exact selected device.

Each actual Commander host action still requires its own exact task/action authority.

No host command may execute merely because transport is ready.

Current logical mapping:
- burzh -> ruvds-xnqc6 -> dd09a197-f716-4dd6-80bb-7f8e5d8260ff
- mazhor -> p552203.kvmvps -> 830038a0-232b-4d83-b52d-0e9973126165
- erefia -> ruvds-ygo0w -> c55d5659-f2c8-416d-8b40-9bac8c80c30d

Current node policy:
burzh -> mazhor -> erefia

Required before every future use:
1. fresh fixed-IP route/currentness check;
2. exact router/profile identity check;
3. fresh Commander device identity and availability check;
4. explicit node selection;
5. exact per-action task authority;
6. exact action_id/node/device binding;
7. explicit operator confirmation where required by the task.

Preserved prohibitions:
- no generic host-command authority;
- no standing host mutation authority;
- no automatic failover;
- no autonomous node switching;
- no automatic IP discovery/admission;
- no DNS fallback;
- no provider/credential authority;
- no shard WRITE;
- no CHECKPOINT_DURABLE claim;
- no resume authority;
- Memory-layering attempt 3 remains NOT_AUTHORIZED.

Basis:
puev5691/wellbeing-hq@c732d3df298418f302bec67f5efda4bdbabaa0f9:
entities/sisadmin/outbox/SIS__fixed-ip-commander-live-proof-r01__KOO.md
blob c8057e6c868bbbd93757bdc6acf5c0d47305732a
terminal PASS_SIS_FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ_ONLY
