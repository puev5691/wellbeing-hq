# KOO → SIS: fixed-IP router deployment-readiness r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: BOUNDED_DEPLOYMENT_READINESS_NO_AUTO_ACTIVATION
project_time: omitted

## Exact authority

puev5691/wellbeing-hq@3325856954f2d323fe0a9fbfca75b1c6fa80b9b4:
entities/koordinator/outbox/KOO__authorize-SIS-fixed-ip-router-deployment-readiness-r01__OPERATOR.md

token:
AUTHORIZE_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_BOUNDED_NO_AUTO_ACTIVATION

## Exact reviewed package

puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01

tree:
fc1bb2751cc5d662037a037fdecf3ece69f07adb

## Independent review basis

puev5691/wellbeing-hq@d4b2afc3bd9fa05ddade9d2e8a273d18a69badd4:
entities/sisadmin/outbox/SIS__fixed-ip-router-independent-package-review-r01__KOO.md

blob:
63ff89a3116e377ecb68c56a181a86ff94308f6e

terminal:
PASS_SIS_FIXED_IP_ROUTER_INDEPENDENT_PACKAGE_REVIEW_R01_READY_FOR_DEPLOYMENT_GATE

## Current SIS writer basis

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:

puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md

terminal:
writer_gate_pass_replacement_sis_r06_authoritative

SIS must Resume-First and re-check current writer, task supersession, exact package identity and authority before touching any host.

## Nodes

1. burzh / ruvds-xnqc6
2. mazhor / p552203.kvmvps
3. erefia / ruvds-ygo0w

## Phase 1 — pre-state capture

For each exact node, capture only the minimum relevant current state needed for safe staging/rollback:
- exact target staging directory candidate;
- whether package-related files/directories already exist;
- relevant service/config/listener state;
- checksums for anything that would be touched later;
- Python runtime/version;
- Python SSL/OpenSSL/trust-store readiness;
- available non-secret execution identity/context;
- exact existing state needed to prove rollback boundary.

No mutation in Phase 1.

## Phase 2 — non-active staging

Stage only the exact reviewed package bytes in a non-active location.

Requirements:
- no production-path replacement;
- no service enable/start/reload;
- no automatic execution;
- no PATH hijack;
- no cron/systemd/autostart;
- no credentials;
- verify exact tree/member set and checksums after staging.

If exact reviewed package identity cannot be established on a node, STOP that node and report blocker.

## Phase 3 — bounded node-local verification

On each node:
- run the package synthetic test suite locally;
- record exact result count;
- do not treat KOD's prior 17/17 as local-node evidence.

Then perform bounded live HTTPS probe only to the currently validated fixed IP set:
- 104.18.32.47
- 172.64.155.209
- transport destination = fixed numeric IPv4;
- TLS SNI = chatgpt.com;
- HTTP Host = chatgpt.com;
- certificate validation = chatgpt.com;
- no DNS fallback.

Purpose:
prove node-local runtime/trust/network compatibility only.

HTTP application responses such as 403/429/5xx are not automatically transport failure.

## Phase 4 — rollback/readback evidence

Because staging is non-active:
- remove or revert only what this task staged if rollback verification is part of the chosen bounded method;
- or preserve staged bytes only if the task explicitly records that they remain inert and separately identifies them.

In either case, return exact post-state/readback and show that no production route/service was activated or replaced.

Do not claim rollback readiness beyond what was actually checked.

## Required result

Return one immutable SIS result addressed to KOO containing:

- exact node identities;
- pre-state summary per node;
- staged package identity/checksums per node;
- local synthetic test result per node;
- live fixed-IP HTTPS verification result per IP/per node;
- TLS identity verification outcome;
- exact mutations performed, if any, limited to non-active staging;
- rollback/post-state evidence;
- blockers;
- explicit statement whether a separate activation decision gate can be opened.

Expected terminal on full bounded success:

PASS_SIS_FIXED_IP_ROUTER_DEPLOYMENT_READINESS_R01_READY_FOR_ACTIVATION_GATE

or exact BLOCKED_* / FAIL_*.

## Hard prohibitions

NOT AUTHORIZED:
- automatic failover activation;
- production-path replacement;
- production service enable/start/reload;
- provider/API calls;
- credentials/secrets;
- DNS changes;
- DNS fallback;
- shard WRITE;
- automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE claim;
- resume authority;
- Memory-layering attempt 3.

After immutable result + readback + addressed return to KOO, STOP.
