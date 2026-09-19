# KOO current active queue r0.59

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## SOURCE SET R0.3

State:
`SOURCE_SET_ACTIVATED`.

## MAZHOR SHARD GATEWAY R0.3

SIS bounded deployment PASS:
`47120c2375b50112134212e6edab4c8fd5b2c5d9`
verdict:
`PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`.

OPERATOR acceptance decision:
`ACCEPT_MAZHOR_SHARD_GATEWAY_R03_FOR_BOUNDED_STANDING_VERIFY_USE`.

Acceptance record:
`entities/koordinator/current/KOO__mazhor-gateway-r03-standing-verify-acceptance.md`

acceptance commit:
`c09f0658663c97028c46c871da2a41ec4232cf05`.

## Accepted operational state

Target:
`mazhor / p552203.kvmvps`.

Use class:
`BOUNDED_STANDING_VERIFY_USE`.

Runtime:
- adapter r0.3;
- harness r0.3;
- service identity `arh-preserve`;
- unit `wellbeing-shard-gateway-verify.service`.

Unit state retained:
- disabled at boot;
- inactive between one-shot invocations;
- no timer;
- no socket;
- no listener;
- no daemon.

Production acceptance:
`YES_FOR_BOUNDED_STANDING_VERIFY_USE_ONLY`.

## Per-invocation authority rule

Every operational invocation requires a separate exact authoritative task/request binding:
- requester entity;
- immutable authority_ref;
- mazhor host;
- exact allowlisted root;
- exact allowlisted VERIFY opcode;
- bounded target;
- applicable limits.

The previous synthetic smoke request is consumed evidence and is not reusable authority.

## Standing boundaries

Still NOT authorized:
- boot enablement;
- automatic scheduling;
- persistent service;
- network listener;
- credentials;
- WRITE / shard-write;
- existing repo/archive permission mutation;
- burzh deployment;
- erefia deployment;
- automatic failover/replication;
- arbitrary requests without exact authority.

Every invocation must retain:
- VERIFY-only;
- arh-preserve;
- command-scoped exact-root Git safe.directory;
- minimal environment;
- fail-closed audit;
- credential access = 0;
- network/listener authority = 0;
- WRITE = 0;
- repo/archive/shard mutation = 0.

## ACTIVE SLOT

`NONE`.

No additional Entity activation is required merely to record production acceptance.

## EXACT NEXT CAUSAL STATE

`MAZHOR_GATEWAY_R03_ACCEPTED_READY_FOR_EXACT_BOUNDED_VERIFY_TASKS`

A future caller must present/create one exact bounded VERIFY task before runtime invocation.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: state after OPERATOR standing-use acceptance
СТАТУС: CURRENT_QUEUE
