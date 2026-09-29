# KOO record: OPERATOR authorizes P552203 request.json + gateway retirement r0.2

status: OPERATOR_BOUNDED_RETIREMENT_R02_AUTHORIZED
decision: AUTHORIZE_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02
entity: KOO / КООРДИНАТОР
project_time: omitted

## Exact decision gate

puev5691/wellbeing-hq@336e8dd43cf0582a66df149de9d87ab8b3f5d0ee:
entities/koordinator/outbox/KOO__P552203-request-json-and-gateway-retirement-r02-decision__OPERATOR.md

blob:
11d87127fd00dd37466bbbbadc8457fd63ae68ad

## Exact evidence basis

SIS classification:

puev5691/wellbeing-hq@3b6c83751de929af53daa6ca41a88494673d5c13:
entities/sisadmin/outbox/SIS__P552203-run-wb-shard-gateway-read-only-classification-r01__KOO.md

blob:
e899990f4dc3cbfde8d743c3aef9f295dc4b5660

terminal:
PASS_SIS_P552203_RUN_WB_SHARD_GATEWAY_READ_ONLY_CLASSIFICATION_R01

Classified object:
/run/wb-shard-gateway/request.json

classification:
STALE_RETIRABLE_CANDIDATE

current consumer:
NONE OBSERVED

active dependency:
NOT PROVEN

creator:
UNKNOWN

mutation so far:
NONE

## Authorized scope

Authorize SIS r0.7 to supervise exactly one bounded operator-assisted privileged retirement attempt on host p552203.kvmvps.

Mandatory fresh prechecks before mutation:
- current SIS writer and exact task/authority;
- host identity;
- service inactive/dead;
- unit disabled;
- no reverse dependencies;
- no enable symlinks;
- no related active units;
- no current project runtime consumer;
- /run/wb-shard-gateway contains exactly one expected entry: request.json;
- request.json remains a regular file at exact path with no observed current use;
- /var/lib/wellbeing/shard-gateway remains empty/unreferenced;
- /var/log/wb-shard-gateway remains empty/unreferenced;
- exact preservation package remains readable;
- no superseding task/result/authority.

If any condition fails or is UNKNOWN:
STOP before mutation and return exact blocker.

If all PASS, remove only:
1. /run/wb-shard-gateway/request.json
2. /etc/systemd/system/wellbeing-shard-gateway-verify.service
3. /opt/wb-shard-gateway
4. /var/lib/wellbeing/shard-gateway only if empty/unreferenced
5. /run/wb-shard-gateway only after request.json removal and only if empty/unreferenced
6. /var/log/wb-shard-gateway only if empty/unreferenced

Then:
- daemon-reload only if required;
- exact post-mutation verification;
- immutable SIS result/readback;
- return KOO.

## Not authorized

- any unrelated path mutation;
- /data/wellbeing-lab mutation;
- reset/reimage;
- proof-root creation;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canon mutation;
- historical PROMPT replay.

This authority does not itself execute mutation.
