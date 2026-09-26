# SIS → KOO: fixed-IP router implementation package authorization handoff r0.1

status: OPERATOR_AUTHORITY_HANDOFF_TO_KOO
scope: ROUTING_ONLY
project_time: omitted

## OPERATOR authority

Direct current OPERATOR decision in SIS chat:

"Разрешаю подготовить implementation package fixed-IP router без установки на серверы"

Interpretation:
- implementation package preparation is authorized;
- server installation/deployment is NOT authorized;
- host/config/service mutation is NOT authorized by this decision;
- automatic failover activation is NOT authorized;
- package should be prepared by the profile owner for code construction.

## Role boundary

Approved role source:
entity-roles-short-v2_4-approved.md
blob:
1772339cb74dae8550bfbd2e33401c34a929e911

KOD profile:
source code, runtime, patch/build/test, implementation-level verification.

SIS profile:
hosts, network, deployment environment, services, monitoring, infrastructure verification.

Therefore SIS does not author the implementation package in this chat.
KOO should route one exact bounded implementation-package task to KOD under the existing OPERATOR authority.

## Exact design basis

SIS fixed-IP routing design:
puev5691/wellbeing-hq@2d61ac65616b7b30e3a11b6c682ec027094e11dd:
entities/sisadmin/outbox/SIS__fixed-ip-administration-routing-design-r01__KOO.md

blob:
399afd89134f877e61d68d0bb2047efd168067dc

terminal:
PASS_SIS_FIXED_IP_ADMINISTRATION_ROUTING_DESIGN_R01_DOCUMENT_ONLY

Measured fixed-IP evidence:
puev5691/wellbeing-hq@4f07ba64212a78d7e18d44089292b5838475649e:
entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-by-ip-r01__KOO.md

blob:
a9285466f6541d347309902d21537d2e3c77a0f4

## Requested KOD package boundaries

Package only.

No:
- installation on burzh/mazhor/erefia;
- host/config/service changes;
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

Expected package should be implementation-ready but non-deployed and should include exact code/config/schema/tests/docs/checksums needed for later independent SIS review.

## Routing

No competing implementation-package KOD task/result was found at SIS fresh reconciliation HEAD:
78999987f1e7e0aa4aea593bdecc2eb3d6086f9c

This file records/routs the direct OPERATOR authority; it does not create new authority and does not activate KOD.

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
