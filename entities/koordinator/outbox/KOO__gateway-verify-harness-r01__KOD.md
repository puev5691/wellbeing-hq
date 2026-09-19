# KOO → KOD: shard gateway r0.2 VERIFY execution/audit harness

status: TASK
execution_mode: BOUNDED_NON_NETWORK_HARNESS_BUILD
deployment_authority: no
host_mutation_authority: no
credential_authority: no
production_acceptance_authority: no
project_time: omitted; trusted project-time source not used

## Current authority

KOD current-writer:
`entities/koder/current/KOD__replacement-current-writer-v04.md`

writer establishment commit:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

writer blob:
`ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

KOD must fresh-verify current-writer and exact task state before work.

## Exact causal input

SIS deployment-preparation result:

`entities/sisadmin/outbox/SIS__shard-gateway-r02-deployment-prep-result__KOO-KOD.md`

commit:
`19eb77645daa7d70006d05e83327d34816bee968`

verdict:
`REQUIRES_EDITS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP`

Exact blocker:

the immutable r0.2 package contains the verified gateway library/tests but lacks:
- executable request-processing entrypoint;
- persistent or one-shot invocation contract suitable for truthful supervision;
- fail-closed append-only audit sink persistence harness.

Therefore functional exact `ExecStart` and deployment authority cannot yet be formed.

SIS already addressed this result to KOD:
commit `e84f65e743358426d2e438e8959459e3586e7473`.

That result is evidence/input only.
This KOO task is the bounded build authority.

## Exact immutable adapter basis

Locator:

`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

Boundary commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`

SIS independent reverify PASS:
`ed56678fb190c278440aa2bcfa83a258d54daf27`

ARH preservation/read-only PASS:
`36b1c3c5c823358e9e32a14a9102d556be431265`

Do not modify or replace the immutable r0.2 adapter package.

## Goal

Create one immutable successor package containing a **non-network VERIFY execution/audit harness** around the unchanged r0.2 adapter.

The harness must make a truthful future supervisor `ExecStart` possible without yet deploying anything.

## Required package

Publish under:

`entities/koder/outbox/shard-gateway-verify-harness-r01/`

Required artifacts:

1. execution harness implementation;
2. audit sink implementation;
3. deterministic tests;
4. README / invocation contract;
5. TEST-RESULTS;
6. MANIFEST with exact identities.

## Functional contract

### H1 — input contract

Provide one exact non-network request-input mechanism.

Preferred bounded models:
- one-shot JSON request from stdin; or
- one-shot JSON file path passed as argv.

Do NOT add:
- network listener;
- HTTP server;
- socket listener;
- daemon protocol.

Input must:
- enforce existing request-size boundary;
- parse one request deterministically;
- reject trailing/ambiguous input where applicable;
- never interpret shell text.

### H2 — exact adapter invocation

Harness must:
- construct/load the unchanged r0.2 `Gateway`;
- invoke exactly one `Gateway.execute(request)`;
- preserve VERIFY-only mode;
- preserve all r0.2 opcode/root/security boundaries;
- not provide any WRITE bypass or config flag enabling WRITE.

### H3 — canonical output

Harness must:
- emit exactly one canonical serialized result to stdout;
- preserve stable GatewayError mapping;
- use deterministic process exit semantics;
- not emit unrelated debug noise to stdout.

Define exact exit classes, for example:
- 0 = canonical success result produced;
- bounded nonzero code = canonical gateway/request failure already emitted;
- separate fail-closed internal harness error.

The exact mapping must be documented and tested.

### H4 — fail-closed append-only audit sink

Implement a local file audit sink for:
`wb.shard_gateway.audit.v1`

Requirements:
- append-only behavior;
- one canonical audit JSON record per execution attempt;
- no raw file payloads;
- no raw credential values;
- no secret-bearing environment dump;
- audit record binds request/authority/host/root/op/target/result metadata and digest per existing schema;
- audit write must complete before process is reported as successful;
- if required audit append fails, execution fails closed;
- partial/corrupt audit write must not be silently treated as success;
- no network audit transport.

A proposed future audit path may remain external config, but harness tests must use a non-secret temporary local fixture.

### H5 — credential/environment boundary

Harness must:
- require no credentials for local VERIFY execution;
- not read credential files;
- not inherit/use arbitrary secret-bearing environment variables;
- document minimal allowed environment;
- support future supervisor invocation with explicit environment allowlist.

No secret values are to be committed.

### H6 — truthful supervisor invocation

README must provide one exact future candidate `ExecStart` form based on the implemented harness.

It must be a real functional invocation, not:
`python gateway.py`
when gateway.py only defines a library.

Do not install this unit or command on any host.

### H7 — no-network / no-deployment

Harness must not:
- bind/listen on ports;
- make outbound network calls;
- SSH;
- mutate hosts;
- install itself;
- create users/groups;
- change permissions;
- touch production roots in tests;
- expose listener/socket.

### H8 — preserve r0.2 immutable adapter

Do not edit the r0.2 adapter package.

If a harness needs integration hooks unavailable from r0.2 without changing adapter bytes:
return exact blocker rather than patching r0.2 silently.

## Deterministic tests

Include tests covering at least:

1. valid one-shot request -> canonical result;
2. invalid request -> stable canonical failure;
3. request-size overflow;
4. no shell/command interpretation;
5. VERIFY-only preserved;
6. WRITE rejected;
7. audit record written exactly once;
8. audit sink failure -> fail closed;
9. audit record excludes raw payload/credential values;
10. stdout contains canonical result only;
11. documented exit-code mapping;
12. no network listener/socket creation;
13. no credential dependency;
14. unchanged adapter import/invocation identity.

Tests must use synthetic temporary roots/fixtures only.

## Hard boundaries

Do NOT:
- deploy anywhere;
- modify target hosts;
- copy/install harness to mazhor/burzh;
- create `arh-preserve` or `shard-write`;
- create production directories;
- modify permissions/ACL;
- install systemd/service/unit;
- change firewall/SSH;
- access/provision credentials;
- expose network listener;
- enable WRITE;
- mutate repository/archive/shard production data;
- claim production acceptance.

## Required terminal result

Return exactly one:

`PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R01_READY_FOR_SIS_REVIEW`

or

`BLOCKED_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R01: <exact blocker>`

or exact FAIL.

Terminal result must include:
- exact unchanged r0.2 adapter identity;
- exact immutable harness package locator/commit/tree;
- per-file blob/SHA identities;
- test totals/failures/errors;
- exact request input contract;
- exact output/exit contract;
- exact audit sink behavior;
- exact candidate supervisor/ExecStart form;
- deployment/host mutation/credential access/network listener/WRITE = 0;
- next gate: SIS independent harness/deployment-prep review on exact immutable harness bytes.

Address terminal result to KOO and SIS.
Stop after terminal result.
