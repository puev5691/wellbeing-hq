# KOO record: authorize SIS bounded P552203 gateway retirement mutation r0.1

status: OPERATOR_BOUNDED_GATEWAY_RETIREMENT_MUTATION_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR approved:
APPROVE_P552203_GATEWAY_RETIREMENT_R01

Exact decision record:
puev5691/wellbeing-hq@74c92d0c745e35ee4393e22b6db36a286b0f9bae:
entities/koordinator/outbox/KOO__P552203-gateway-retirement-approved-r01__OPERATOR.md

Exact host:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Authorized mutation scope only after fresh precheck:
- remove /etc/systemd/system/wellbeing-shard-gateway-verify.service;
- remove /opt/wb-shard-gateway;
- remove only these runtime paths if they are still empty and unreferenced:
  /var/lib/wellbeing/shard-gateway
  /run/wb-shard-gateway
  /var/log/wb-shard-gateway;
- perform daemon-reload if required after unit removal;
- verify post-mutation absence and no new dependency.

Mandatory precheck:
- service still inactive/dead;
- unit still disabled;
- no reverse dependencies;
- no enable symlinks;
- no related active units;
- no current project runtime consumer;
- runtime paths still empty;
- preservation package exact identity still available.

STOP if any condition changed.

Not authorized:
- delete/move any other path;
- reset/reimage;
- proof-root creation;
- backend install/run;
- T01-T20 execution;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3.
