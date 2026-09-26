# KOO → KOD: fixed-IP router implementation package r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: IMPLEMENTATION_READY_PACKAGE_ONLY_NO_DEPLOYMENT
project_time: omitted

## Authority

Direct OPERATOR authority, routed by SIS:

puev5691/wellbeing-hq@a0ecf4fda0bd4223d1ffdfb8c62fdb9b0a0bdf21:
entities/sisadmin/outbox/SIS__fixed-ip-router-implementation-package-authority-handoff-r01__KOO.md

blob:
7e3a14eff25356a0af190a840e14c15cb7afd162

Exact OPERATOR decision:
"Разрешаю подготовить implementation package fixed-IP router без установки на серверы"

## Current KOD writer basis

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

blob:
cf1c84f9df7c90509703e4885844d0cf871ff412

Writer Gate result:
puev5691/wellbeing-hq@fd48a57fc49f0330c93e632fa8221b5476e6cfe9:
entities/koder/outbox/KOD__replacement-writer-gate-v05-result__KOO.md

terminal:
PASS_KOD_REPLACEMENT_WRITER_GATE_V05

KOD must Resume-First and verify writer/current task/supersession before execution.

## Exact design basis

SIS routing design:
puev5691/wellbeing-hq@2d61ac65616b7b30e3a11b6c682ec027094e11dd:
entities/sisadmin/outbox/SIS__fixed-ip-administration-routing-design-r01__KOO.md

blob:
399afd89134f877e61d68d0bb2047efd168067dc

terminal:
PASS_SIS_FIXED_IP_ADMINISTRATION_ROUTING_DESIGN_R01_DOCUMENT_ONLY

Measurement basis:
puev5691/wellbeing-hq@4f07ba64212a78d7e18d44089292b5838475649e:
entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-by-ip-r01__KOO.md

blob:
a9285466f6541d347309902d21537d2e3c77a0f4

## Current routing profile

node priority:
1. burzh / ruvds-xnqc6
2. mazhor / p552203.kvmvps
3. erefia / ruvds-ygo0w

validated IP set:
- 104.18.32.47
- 172.64.155.209

HTTPS identity must always preserve:
- TLS SNI = chatgpt.com
- HTTP Host = chatgpt.com
- certificate validation = chatgpt.com

DNS is excluded from normal fixed-IP transport path.

## Required package

Produce one implementation-ready, non-deployed package containing at minimum:

1. source code for fixed-IP router;
2. versioned routing-profile schema/config;
3. current profile fixture with exact node order and IP set;
4. health-check state machine;
5. deterministic target-IP selection;
6. failure classification:
   - TARGET_IP_FAILURE
   - NODE_FAILURE
   - TLS_CERTIFICATE_FAILURE
   - HTTP_APPLICATION_RESPONSE
   - FIXED_IP_SET_EXHAUSTED
7. node failover:
   - try other admitted IP on same node first;
   - then burzh → mazhor → erefia;
8. stale-IP and successor-profile handling;
9. manual failover command/interface;
10. audit output with no credentials/private request content;
11. rollback/pre-state contract for later deployment;
12. tests/fixtures for:
   - healthy IP;
   - first IP fail / second IP healthy;
   - both IPs fail on one node;
   - primary node unavailable;
   - failover to secondary/tertiary;
   - TLS certificate mismatch;
   - HTTP 403/429/5xx not misclassified as transport failure;
   - stale profile;
   - unadmitted successor profile;
   - all-node/all-IP exhaustion;
13. manifest + checksums;
14. short README/runbook for later independent SIS review.

## Required output

Publish one immutable implementation package and one KOD result addressed to KOO.

Result must include:
- package paths;
- exact commit/blob/checksums;
- tests executed and outcomes;
- implementation limitations;
- confirmation that nothing was deployed.

Expected terminal:
PASS_KOD_FIXED_IP_ROUTER_IMPLEMENTATION_PACKAGE_R01_READY_FOR_SIS_REVIEW
or exact BLOCKED_* / FAIL_*.

## Prohibited

- installation/deployment on burzh/mazhor/erefia;
- host/config/service mutation;
- automatic failover activation;
- provider/API access;
- credentials/secrets;
- DNS changes;
- shard WRITE;
- automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE claim;
- resume authority;
- Memory-layering attempt 3.

After immutable package + result + readback + addressed return to KOO, STOP.
