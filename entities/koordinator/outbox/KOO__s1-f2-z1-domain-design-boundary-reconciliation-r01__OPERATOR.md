# KOO → OPERATOR: fresh reconciliation after S1 F2 Z1 design-boundary selection

status: Z1_DESIGN_BOUNDARY_CURRENT_EVIDENCE_PLAN_GATE_REQUIRED
project_time: omitted

## Human meaning

OPERATOR selected Z1 as the first S1 F2 failure-domain design boundary.

The choice is current and not superseded at the checked HQ boundary.

Z1 requires future evidence that two sides relied upon for a positively acknowledged S1 state are not within the same selected provider zone/site failure domain.

The current mazhor inventory cannot prove Z1 because it covers one host only and does not establish provider-zone/site independence.

Therefore the next safe step is not host access. It is one bounded documentary evidence plan defining what must be proven before any multi-zone/site technical verification can be authorized.

## Exact decision

SELECT_S1_F2_DOMAIN_Z1_PROVIDER_ZONE_OR_SITE_DESIGN_ONLY

Decision record:
entities/koordinator/outbox/KOO__select-s1-f2-domain-z1-provider-zone-site-design-only__OPERATOR.md

## Existing evidence

Mazhor scoped read-only inventory:
puev5691/wellbeing-hq@4635cbd8b16ed0d9ca58f19d18c511fc10bb111b:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-f2-mazhor-nonsecret-host-inventory-r01__KOO.md

blob:
177204daf9093688db49c75749a36bec4f5352fd

This evidence proves one scoped host inventory only.

It does NOT prove:
- provider zone/site identity;
- distinct physical sites;
- distinct storage failure domains;
- provider control-plane independence;
- network/power/common-storage independence;
- cross-zone durability.

## Required next evidence-plan content

A bounded SIS document-only plan should define, without performing access:

1. Exact Z1 assertion to prove.
2. Required evidence for provider zone/site identity.
3. Required evidence that two candidate placements are in distinct zones/sites.
4. Common-dependency checks:
   - shared storage;
   - shared physical host/hypervisor where knowable;
   - shared availability zone/site;
   - shared power/network/control plane where relevant and verifiable.
5. Minimum acceptable evidence classes:
   - provider authoritative metadata/documentation;
   - host/provider inventory evidence;
   - immutable config/placement records;
   - independent readback/verification.
6. Evidence that must remain UNKNOWN if provider cannot expose physical/site facts.
7. What can be concluded from VPS names/IP/geography and what cannot.
8. Required evidence before any future runtime cross-zone test.
9. Failure modes that invalidate Z1 proof.
10. Exact stop conditions and privacy/secret boundaries.

The plan must not choose provider/backend/hosts.

## Next authority gate

A SIS task is NOT activated by this reconciliation.

Required separate OPERATOR token:

AUTHORIZE_SIS_S1O2_F2_Z1_EVIDENCE_PLAN_R01_DOCUMENT_ONLY

If authorized, KOO must fresh-reconcile SIS writer/current task/supersession and issue one exact document-only task.

## Preserved boundaries

candidate governance:
CANDIDATE_NOT_ACTIVE

deployed CHECKPOINT_DURABLE:
NOT_ESTABLISHED

deployed RECOVERY_READY:
NOT_ESTABLISHED

failure-domain Z1 runtime proof:
NOT_ESTABLISHED

multi-zone access:
NOT_AUTHORIZED

host/provider access:
NOT_AUTHORIZED

shard WRITE:
NOT_AUTHORIZED

backend selection:
NONE

operational owner:
NOT_APPOINTED

resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

historical PROMPT replay:
NONE

## Terminal

PASS_KOO_S1_F2_Z1_DESIGN_BOUNDARY_RECONCILED_EVIDENCE_PLAN_GATE_REQUIRED_R01
