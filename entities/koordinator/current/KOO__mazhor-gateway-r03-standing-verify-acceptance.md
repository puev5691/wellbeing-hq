# OPERATOR acceptance — mazhor shard gateway r0.3 bounded standing VERIFY use

status: OPERATOR_ACCEPTANCE_RECORDED
decision: ACCEPT_MAZHOR_SHARD_GATEWAY_R03_FOR_BOUNDED_STANDING_VERIFY_USE
project_time: omitted; trusted project-time source not used

## Exact OPERATOR decision

`ACCEPT_MAZHOR_SHARD_GATEWAY_R03_FOR_BOUNDED_STANDING_VERIFY_USE`

This decision was explicitly issued by OPERATOR in the active KOO conversation.

Decision gate:
`entities/koordinator/outbox/KOO__mazhor-gateway-r03-acceptance-decision__OPERATOR.md`

gate commit:
`f69526656805bafdc698a0eeb382eaf91902a47b`

gate blob:
`321faeb5d3dfe9c03f65a45e6d9cfa641d05fbf6`.

SIS bounded deployment PASS:
`entities/sisadmin/outbox/SIS__mazhor-shard-gateway-r02-bounded-verify-deployment__KOO.md`

PASS commit:
`47120c2375b50112134212e6edab4c8fd5b2c5d9`.

## Accepted runtime

Target:
`mazhor / p552203.kvmvps`.

Accepted use class:
`BOUNDED_STANDING_VERIFY_USE`.

Service identity:
`arh-preserve`.

Runtime layout:
`/opt/wb-shard-gateway/`.

Installed unit:
`wellbeing-shard-gateway-verify.service`.

Unit remains:
- disabled at boot;
- inactive between one-shot invocations;
- no timer;
- no socket;
- no listener;
- no daemon.

## Accepted exact runtime lineage

Adapter successor:
`shard-gateway-adapter-r03`.

Adapter package commit:
`9140d2ffe2b2ab983ce4a607447b5cc20f44ec6f`.

Installed `gateway.py` SHA-256:
`9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`.

Harness successor:
`shard-gateway-verify-harness-r03`.

Harness package commit:
`1f4c8218734ccb2e081e491b92195bf7bedaf1d8`.

Installed runtime hashes accepted:
- `harness.py`
  `6dbf10acd41105e2491262d6745f4ac9574742ca6a11eb09f933dcaf80ec4465`;
- `audit_sink.py`
  `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;
- `INVOCATION.json`
  `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

## Standing-use authority

The exact installed runtime is accepted as the current local production-approved read-only VERIFY runtime on mazhor.

Every operational invocation still requires a separate exact authoritative task/request binding at minimum:
- requester entity;
- immutable `authority_ref`;
- `host_id=mazhor`;
- exact allowlisted `root_id`;
- exact allowlisted VERIFY opcode;
- bounded target/relative path;
- applicable output/request limits.

The previous synthetic smoke request is consumed evidence only and cannot be replayed as operational authority.

## Preserved runtime boundaries

Standing acceptance does NOT authorize:

- boot enablement;
- automatic scheduling;
- timer/socket creation;
- persistent daemon;
- network listener;
- outbound network behavior;
- credentials;
- WRITE;
- `shard-write`;
- chmod/chown/ACL/group changes on existing repo/archive roots;
- burzh deployment;
- erefia deployment;
- automatic failover/replication;
- arbitrary requests without exact authority.

Each invocation must preserve:
- `VERIFY` only;
- service identity `arh-preserve`;
- command-scoped exact-root Git `safe.directory`;
- minimal environment;
- one fail-closed `wb.shard_gateway.audit.v1` event;
- credential access = 0;
- listener/network authority = 0;
- WRITE = 0;
- repository/archive/shard mutation = 0.

## Operational meaning

This acceptance authorizes **use of the already installed bounded VERIFY runtime** when a separately authorized task requests a permitted read-only operation.

It does not create a free-running service and does not create generic Entity authority.

No additional host mutation is required merely to record this acceptance.

---
КТО: OPERATOR / recorded by KOO
ДЛЯ ЧЕГО: production acceptance of exact mazhor bounded standing VERIFY runtime
СТАТУС: ACCEPT_MAZHOR_SHARD_GATEWAY_R03_FOR_BOUNDED_STANDING_VERIFY_USE
