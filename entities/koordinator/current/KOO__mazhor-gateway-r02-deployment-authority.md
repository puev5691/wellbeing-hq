# OPERATOR decision — mazhor shard gateway r0.2 bounded VERIFY deployment

status: OPERATOR_DECISION_RECORDED
decision: AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT
project_time: omitted; trusted project-time source not used

## Exact OPERATOR decision

`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

This decision was explicitly issued by OPERATOR in the active KOO conversation.

Decision gate:
`entities/koordinator/outbox/KOO__shard-gateway-r02-mutation-decision__OPERATOR.md`
commit `43123b47f3ff8351820251a2dbd694b46c0e4d32`
blob `015045df71c71415c90c99a87905fa39069f9cee`.

## Exact selected scope

Target:
`mazhor` / `p552203.kvmvps` only.

Selected canonical runtime layout:
`/opt/wb-shard-gateway/`.

Immutable adapter:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`.

Immutable harness:
`puev5691/wellbeing-hq@01c4f6a336d0ca6d9000d42e5966c4e924f82bbd:entities/koder/outbox/shard-gateway-verify-harness-r02`.

SIS rereview PASS:
`ed2974f0f03c12e3dc8dd1364ef6436ad1785bb7`.

## Authority granted

KOO may route SIS to perform exactly the bounded mazhor VERIFY deployment stage described in OPTION A of the decision gate.

Authorized classes:
- create non-login, non-sudo `arh-preserve`;
- create exact new gateway runtime/run/work/audit paths;
- install exact immutable adapter/harness runtime bytes;
- publish/read back exact systemd oneshot unit candidate before installation;
- install that exact unit only after argv equivalence to `INVOCATION.json` is verified;
- create synthetic non-secret request;
- create/use local audit sink;
- run one bounded local VERIFY smoke;
- perform post-smoke readback and bounded rollback if needed.

## Authority explicitly not granted

- burzh mutation/deployment;
- erefia action;
- chmod/chown/ACL/group changes on existing repo/archive roots;
- WRITE/shard-write;
- credential read/provisioning;
- SSH/firewall mutation;
- listener/socket exposure;
- automatic failover/replication;
- repository/archive/shard writes;
- boot enablement/standing service use;
- production acceptance.

## Mandatory fail-closed condition

After `arh-preserve` exists, SIS must verify effective read/traverse access to the exact mazhor repository and archive roots without changing those roots.

If access is insufficient:
STOP.
Do not modify existing root permissions.
Return exact blocker and preserve reversibility of already-created deployment-only state.

## Boundary

This record itself performs no host mutation.
All mutations must occur only under a separately routed exact SIS task referencing this decision.

---
КТО: OPERATOR / recorded by KOO
ДЛЯ ЧЕГО: explicit bounded mazhor VERIFY deployment authority
СТАТУС: OPERATOR_DECISION_RECORDED
