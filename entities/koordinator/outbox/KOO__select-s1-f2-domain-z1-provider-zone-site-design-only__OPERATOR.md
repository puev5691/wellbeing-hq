# KOO record: OPERATOR selects S1 F2 Z1 failure-domain design boundary

status: OPERATOR_Z1_DESIGN_BOUNDARY_RECORDED
project_time: omitted

Exact OPERATOR decision:

SELECT_S1_F2_DOMAIN_Z1_PROVIDER_ZONE_OR_SITE_DESIGN_ONLY

Meaning:

For the first S1 F2 design proof, the protected failure domain is one independently verified provider availability zone or physical site, including all hosts/storage in that zone/site.

Required design property:

Loss of the whole selected zone/site must not lose a positively acknowledged S1 checkpoint object's required state, including as applicable:
- acknowledged immutable object;
- current pointer;
- PUT/CAS outcomes;
- dedupe/fence/transaction evidence required by the selected governance scope.

This decision is DESIGN_ONLY.

It does NOT authorize:
- multi-host or multi-zone access;
- provider API access;
- host inventory;
- deployment;
- shard WRITE;
- backend selection;
- operational owner appointment;
- storage purchase/provisioning;
- implementation/runtime tests;
- Project Sources/canon mutation;
- resume authority;
- memory-layering attempt 3.

Exact predecessor gate:

puev5691/wellbeing-hq@5ca5396b16782de58e4d8ae31c9b61133189e858:
entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-f2-mazhor-inventory-receipt-domain-gate-r01__OPERATOR.md

blob:
fd07ef0510a83d9fd15c583a74e64f45c626505f

Fresh taxonomy reconciliation:

puev5691/wellbeing-hq@8ec6ff1b27a480cf128781cf2a99665883d230a1:
entities/koordinator/outbox/KOO__shard-checkpoint-claims-taxonomy-reviews-complete-f2-gate-reconciliation-r01__OPERATOR.md

blob:
2d00113c221b0ccf35522e16f4f1356a121574ec

Historical task/PROMPT replay:
NONE
