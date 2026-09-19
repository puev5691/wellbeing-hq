# KOO → OPERATOR: mazhor shard gateway r0.3 standing-use / production-acceptance decision gate

status: OPERATOR_DECISION_REQUIRED
decision_executes_runtime_use: no
host_mutation_from_this_gate: no
production_acceptance_before_decision: no
project_time: omitted; trusted project-time source not used

## Why this gate exists

SIS completed the explicitly authorized bounded mazhor VERIFY deployment and one exact smoke:

`entities/sisadmin/outbox/SIS__mazhor-shard-gateway-r02-bounded-verify-deployment__KOO.md`
commit `47120c2375b50112134212e6edab4c8fd5b2c5d9`
verdict `PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`.

The deployed runtime is the corrected successor:
- adapter r0.3;
- harness r0.3.

The PASS explicitly states:
`production_acceptance: no`.

Therefore no standing operational use may be inferred from the successful smoke.

## Verified deployed state

Target:
`mazhor / p552203.kvmvps`.

Service identity:
`arh-preserve`
uid `999`, gid `988`, group `arh-preserve` only, shell `/usr/sbin/nologin`.

Installed runtime layout:
`/opt/wb-shard-gateway/`.

Installed exact runtime hashes after smoke:

- `gateway.py`
  SHA-256 `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`;

- `harness.py`
  SHA-256 `6dbf10acd41105e2491262d6745f4ac9574742ca6a11eb09f933dcaf80ec4465`;

- `audit_sink.py`
  SHA-256 `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;

- `INVOCATION.json`
  SHA-256 `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

Installed unit:
`wellbeing-shard-gateway-verify.service`.

Unit artifact:
`entities/sisadmin/outbox/mazhor-gateway-r03-deploy/SIS__wellbeing-shard-gateway-verify.service`
commit `f5316cacccdae55c8fefab9f27d164dec7cb0f7e`
blob `505cbbb6a155efe3c4c59073ddc8f79001e65313`.

Unit state after smoke:
- enabled: `disabled`;
- active: `inactive`;
- no timer;
- no socket;
- no standing service.

Smoke:
- exactly 1 attempt;
- automatic retries: 0;
- systemd result: success;
- canonical `GIT_HEAD` result matched expected HEAD;
- audit delta: +1;
- audit schema: `wb.shard_gateway.audit.v1`;
- executed as `arh-preserve`;
- runtime hashes remained exact 4/4;
- credentials: 0;
- listener exposure: 0;
- WRITE: 0;
- repository/archive/shard mutation: 0.

## Important operational boundary

The verified runtime is a local one-shot VERIFY executor.

It is NOT:
- a network service;
- a persistent daemon;
- an automatically scheduled service;
- a WRITE gateway;
- a credentialed gateway;
- an automatically authorized Entity action surface.

The unit consumes an exact local request file:
`/run/wb-shard-gateway/request.json`.

Therefore production acceptance must not silently create generic request authority.

Every operational request still requires an immutable task/authority reference appropriate to the caller and operation.

## OPTION A — accept mazhor gateway for bounded standing VERIFY use

Decision text:

`ACCEPT_MAZHOR_SHARD_GATEWAY_R03_FOR_BOUNDED_STANDING_VERIFY_USE`

Meaning:

1. Accept the exact installed mazhor adapter r0.3 + harness r0.3 + unit as the current production-approved **read-only VERIFY runtime**.

2. Preserve the current execution model:
   - unit remains `disabled` at boot;
   - no timer/socket/listener;
   - no daemon;
   - no automatic retries;
   - no automatic cross-host failover;
   - local one-shot execution only.

3. Standing use is allowed only when an exact separately authoritative task/request supplies:
   - requester entity;
   - immutable `authority_ref`;
   - host/root/opcode;
   - bounded target;
   - existing VERIFY-only operation from the allowlist.

4. Each invocation must:
   - use the existing exact service identity `arh-preserve`;
   - preserve command-scoped exact-root Git `safe.directory`;
   - write one fail-closed audit event;
   - keep credential access = 0;
   - keep network/listener = 0;
   - keep WRITE = 0.

5. This acceptance does NOT authorize:
   - boot enablement;
   - timer/socket activation;
   - network exposure;
   - credentials;
   - WRITE / `shard-write`;
   - repo/archive permission changes;
   - burzh deployment;
   - erefia deployment;
   - replication/failover;
   - arbitrary requests without exact task authority.

6. The existing smoke request is consumed test evidence and is not reusable operational authority.

Consequence:

The mazhor gateway becomes an accepted local read-only project runtime that KOO/authorized Entities may invoke only through separately authoritative bounded VERIFY tasks.

No new host mutation is required merely to record this acceptance.

## OPTION B — preserve deployment but do not grant standing use

Decision text:

`PRESERVE_MAZHOR_SHARD_GATEWAY_R03_DEPLOYED_NOT_PRODUCTION_ACCEPTED`

Meaning:
- leave exact installed runtime/unit on mazhor;
- unit remains disabled/inactive;
- no operational request may use it except under a future separately authorized test/review task;
- no rollback is requested;
- production acceptance remains NO.

Consequence:
deployment evidence is retained, but the gateway is not yet an ordinary project runtime.

## OPTION C — require another acceptance review before standing use

Decision text:

`REQUIRE_FINAL_SHARD_GATEWAY_R03_ACCEPTANCE_REVIEW`

Meaning:
- no standing use yet;
- KOO routes one bounded final acceptance review of installed mazhor state, exact hashes, audit behavior and authority boundary;
- no new host mutation unless separately authorized.

Consequence:
adds one review gate before human production acceptance.

## OPTION D — withdraw deployed runtime

Decision text:

`WITHDRAW_MAZHOR_SHARD_GATEWAY_R03_DEPLOYMENT`

Meaning:
- standing use not accepted;
- KOO must form a separate exact rollback task under the prior bounded deployment rollback boundary;
- this decision itself does not mutate the host.

## Boundaries common to every option

This decision gate itself:
- performs no host mutation;
- performs no gateway invocation;
- accesses no credential;
- enables no WRITE;
- creates no listener;
- changes no burzh/erefia state.

Until OPERATOR explicitly selects OPTION A:
`production_acceptance = no`.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: exact separately authorized standing-use / production-acceptance decision after successful bounded mazhor VERIFY deployment
СТАТУС: OPERATOR_DECISION_REQUIRED
