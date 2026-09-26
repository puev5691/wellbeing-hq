# KOO: authority for one Commander live proof

status: OPERATOR_AUTHORITY_RECORDED
project_time: omitted

token:
AUTHORIZE_SIS_FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ_ONLY

target_node: burzh
device_id: dd09a197-f716-4dd6-80bb-7f8e5d8260ff
device_name: ruvds-xnqc6
action_id: FIXED_IP_COMMANDER_LIVE_PROOF_R01_BURZH_IDENTITY_READ

exact_command:
hostname && id -un

Authorized only:
- fresh route/device/authority verification;
- one execution of the exact command above;
- read-only result capture;
- immutable result return to KOO.

Not authorized:
- any second command;
- host mutation;
- deployment;
- automatic failover/node switching;
- credentials/provider operations;
- DNS fallback;
- shard WRITE;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

Any mismatch before execution => STOP.
