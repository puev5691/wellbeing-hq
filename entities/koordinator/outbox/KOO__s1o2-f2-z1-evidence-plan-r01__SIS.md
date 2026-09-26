# KOO → SIS: S1+O2 F2 Z1 evidence plan r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: BOUNDED_DOCUMENT_ONLY_EVIDENCE_PLAN
project_time: omitted

## Exact OPERATOR authority

puev5691/wellbeing-hq@5b3c10b9fe30ed762320649f09edf1c7fdebab3b:
entities/koordinator/outbox/KOO__authorize-SIS-s1o2-f2-z1-evidence-plan-r01__OPERATOR.md

blob:
9fff9c21fecc55ceca5d27f5a48aad416605107c

decision:
AUTHORIZE_SIS_S1O2_F2_Z1_EVIDENCE_PLAN_R01_DOCUMENT_ONLY

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

readback:
PASS_EXACT_COMMIT_AND_BLOB

SIS must Resume-First and verify current writer remains valid.

## Exact Z1 decision

puev5691/wellbeing-hq@b3c2b5e340d1c9ca96a11e65549b8ea03b084187:
entities/koordinator/outbox/KOO__select-s1-f2-domain-z1-provider-zone-site-design-only__OPERATOR.md

blob:
490ad6e44aa25672d5cbc18f5f5a75c2e07e2c02

decision:
SELECT_S1_F2_DOMAIN_Z1_PROVIDER_ZONE_OR_SITE_DESIGN_ONLY

Meaning:
the first S1 F2 design proof must tolerate loss of one independently verified provider availability zone or physical site.

## Existing bounded evidence

Mazhor scoped nonsecret host inventory:
puev5691/wellbeing-hq@4635cbd8b16ed0d9ca58f19d18c511fc10bb111b:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-f2-mazhor-nonsecret-host-inventory-r01__KOO.md

blob:
177204daf9093688db49c75749a36bec4f5352fd

This proves only one scoped host inventory.
It does not prove zone/site identity or cross-zone independence.

## Required task

Produce one document-only evidence plan answering:

1. What exact Z1 assertion must be proven before any runtime test?
2. What evidence can establish provider zone/site identity?
3. What evidence can establish that two candidate placements are in different zones/sites?
4. What common dependencies must be checked or left UNKNOWN:
   - shared storage;
   - shared physical host/hypervisor where knowable;
   - shared availability zone/site;
   - shared power/network/control plane where relevant.
5. Which evidence classes are acceptable:
   - provider authoritative docs/metadata;
   - provider account/placement metadata;
   - host/provider inventory;
   - immutable config/placement records;
   - independent readback/verification.
6. What must remain UNKNOWN if provider transparency is insufficient?
7. What must NOT be inferred merely from VPS names, public IPs, DNS names, city labels or rough geography?
8. What evidence is required before future cross-zone runtime verification?
9. What evidence/failure modes would invalidate a claimed Z1 proof?
10. What privacy/secret boundaries and stop conditions apply?

## Required output

Publish one immutable SIS result addressed to KOO.

Expected terminal:
PASS_SIS_S1O2_F2_Z1_EVIDENCE_PLAN_R01_DOCUMENT_ONLY
or exact BLOCKED_* / FAIL_*.

The result must clearly separate:
- facts already established;
- evidence still required;
- UNKNOWN;
- later actions requiring separate OPERATOR authority.

## Prohibited

- host/provider/API access;
- multi-host/multi-zone inventory;
- deployment;
- shard WRITE;
- runtime test;
- backend/provider selection;
- purchasing/provisioning;
- operational owner appointment;
- credentials/secrets access;
- Project Sources/canon mutation;
- resume authority;
- memory-layering attempt 3;
- historical PROMPT replay.

After one immutable result, exact readback and addressed return to KOO, STOP.
