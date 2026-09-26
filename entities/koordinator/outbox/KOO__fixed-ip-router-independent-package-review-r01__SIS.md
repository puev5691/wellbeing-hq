# KOO → SIS: independent review of fixed-IP router implementation package r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: INDEPENDENT_PACKAGE_ONLY_REVIEW_NO_DEPLOYMENT_NO_LIVE
project_time: omitted

## Purpose

Independently verify the exact KOD implementation package against the approved SIS design and the current infrastructure/security boundary.

This is a package review only.

No installation, host mutation, live node test, automatic failover activation, provider/API access, credentials, DNS change or shard WRITE is authorized.

## Exact KOD result

puev5691/wellbeing-hq@1e7037784830c994cd57f5e41d8a7ec5068ae3a1:
entities/koder/outbox/KOD__fixed-ip-router-implementation-package-r01-result__KOO.md

blob:
8d93497d3252e33c2c1296ae37ef651d67da10e8

terminal:
PASS_KOD_FIXED_IP_ROUTER_IMPLEMENTATION_PACKAGE_R01_READY_FOR_SIS_REVIEW

## Exact package

puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:
entities/koder/outbox/fixed-ip-router-r01

tree:
fc1bb2751cc5d662037a037fdecf3ece69f07adb

KOD-reported package integrity:
- MANIFEST.md blob 83a45b65dfe81a2e8f666105dc40bfffaff31840
- SHA256SUMS.txt blob 2538b84c80f4b27163ea73622d660a56388ee937
- sha256sum -c: 11/11 PASS
- package readback: 12/12 exact bytes/blobs PASS
- python unittest: 17/17 PASS
- deployment/live network probe: 0

Do not trust those PASS claims merely because KOD reported them; independently verify what is checkable from the exact immutable package.

## Exact design basis

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

## Required independent checks

1. Exact package identity:
   - commit/tree;
   - member list;
   - manifest/checksum consistency;
   - no unexpected extra executable/deployment artifacts.

2. Design conformance:
   - fixed-IP transport destination;
   - TLS SNI = chatgpt.com;
   - HTTP Host = chatgpt.com;
   - certificate validation = chatgpt.com;
   - no DNS in normal fixed-IP path;
   - node priority burzh → mazhor → erefia;
   - deterministic same-node IP retry before node failover.

3. Failure classification correctness:
   - TARGET_IP_FAILURE;
   - NODE_FAILURE;
   - TLS_CERTIFICATE_FAILURE;
   - HTTP_APPLICATION_RESPONSE;
   - FIXED_IP_SET_EXHAUSTED.

4. Security boundary:
   - no certificate downgrade;
   - no silent DNS fallback;
   - no hidden credentials/secrets;
   - no provider/API dependency;
   - no undeclared host/service mutation;
   - no automatic IP admission from discovery;
   - no automatic failover activation by package presence alone.

5. Profile/admission model:
   - current measured profile must not silently become operational ADMITTED;
   - stale/successor semantics preserve versioning and explicit admission;
   - current two-IP set is treated as versioned evidence, not permanent truth.

6. Audit:
   - failure class, node, target IP, profile revision and outcome are recordable;
   - no credentials/private request content required.

7. Rollback/deployment readiness boundary:
   - README/pre-state/rollback contract is sufficient as a later deployment prerequisite or identify exact gaps;
   - do not collect live pre-state in this review.

8. Test review:
   - independently inspect the 17 synthetic tests and confirm coverage claims;
   - rerun only in a bounded local/non-host environment if available and permitted by existing tooling;
   - no live network probe.

## Required result

Return one immutable SIS result addressed to KOO with one of:

PASS_SIS_FIXED_IP_ROUTER_INDEPENDENT_PACKAGE_REVIEW_R01_READY_FOR_DEPLOYMENT_GATE

or exact BLOCKED_* / FAIL_*.

PASS means only:
package is ready to reach a separate deployment decision gate.

PASS does NOT authorize:
- installation;
- host/config/service mutation;
- automatic failover activation;
- live node testing;
- provider/API calls;
- DNS changes;
- credentials/secrets;
- shard WRITE;
- automation mutation;
- Project Sources/canon mutation;
- CHECKPOINT_DURABLE;
- resume authority;
- Memory-layering attempt 3.

If any implementation defect is found, identify exact file/behavior and smallest correction needed. Do not repair it in SIS review.

After immutable result + readback + addressed return to KOO, STOP.
