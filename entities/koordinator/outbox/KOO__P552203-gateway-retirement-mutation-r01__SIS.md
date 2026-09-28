# KOO → SIS: P552203 gateway retirement mutation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН r0.7
scope: BOUNDED_GATEWAY_RETIREMENT_MUTATION_ONLY
project_time: omitted

Resume-First.

Exact authority:
puev5691/wellbeing-hq@573c9c15abe38bca79e159c265b013199f3d0fea:
entities/koordinator/outbox/KOO__authorize-SIS-P552203-gateway-retirement-mutation-r01__OPERATOR.md

Exact retirement decision:
puev5691/wellbeing-hq@74c92d0c745e35ee4393e22b6db36a286b0f9bae:
entities/koordinator/outbox/KOO__P552203-gateway-retirement-approved-r01__OPERATOR.md

Exact prior read-only review:
puev5691/wellbeing-hq@3792fa046a99f4dded9d91fdc4706e76caaa9e9b:
entities/sisadmin/outbox/SIS__P552203-gateway-dependency-retirement-review-r01__KOO-OPERATOR.md

Exact preservation package:
puev5691/wellbeing-hq@2f58bb83e43e6443335830e3e779cc4c6c38d0b6:
entities/sisadmin/outbox/p552203-stpc-preservation-r01/
tree:
9cf168ce696395872e57b81ea1bab64941006011

Exact host:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Before mutation, fresh-check:
- service inactive/dead;
- unit disabled;
- no reverse dependencies;
- no enable symlinks;
- no related active units;
- no current project runtime consumer;
- /var/lib/wellbeing/shard-gateway empty;
- /run/wb-shard-gateway empty;
- /var/log/wb-shard-gateway empty;
- exact preservation package still readable.

If any check fails or changed:
STOP and return exact blocker.

If all pass, remove only:
- /etc/systemd/system/wellbeing-shard-gateway-verify.service
- /opt/wb-shard-gateway
- the three runtime directories above, only if still empty and unreferenced.

Run systemd daemon-reload only if needed after unit removal.

Then verify:
- unit absent/not loadable from removed path;
- /opt/wb-shard-gateway absent;
- approved runtime paths absent;
- no unrelated path changed;
- no project dependency newly observed.

Do NOT:
- touch /data/wellbeing-lab preservation source paths;
- reset/reimage host;
- create STP-C proof roots;
- install/run backend;
- execute T01-T20;
- claim CHECKPOINT_DURABLE;
- run memory-layering attempt 3.

Expected terminal:
PASS_SIS_P552203_GATEWAY_RETIREMENT_MUTATION_R01_COMPLETE

or exact BLOCKED_/FAIL_.

After immutable result + exact readback + return KOO, STOP.
