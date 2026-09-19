# OPERATOR decision — source rebuild r0.3

status: OPERATOR_DECISION_RECORDED
decision: APPROVE_SOURCE_REBUILD_R03_AND_SELECT_SUCCESSOR_LINEAGE
project_sources_activation: no
project_time: omitted; trusted project-time source not used

## Exact OPERATOR decision

`APPROVE_SOURCE_REBUILD_R03_AND_SELECT_SUCCESSOR_LINEAGE`

This decision was explicitly issued by OPERATOR in the active KOO conversation after the completed KAN/SHT/ARH review chain.

## Exact approved candidate basis

Immutable locator:
`puev5691/wellbeing-hq@316fe7ac638b9ed7bc422f2cbf1a720ca6197b10:entities/koordinator/outbox/source-rebuild-r03`

Boundary commit:
`316fe7ac638b9ed7bc422f2cbf1a720ca6197b10`

Boundary tree:
`e8cd47baec0be6accca0fa2968187aefa75b18ed`

Decision gate:
`entities/koordinator/outbox/KOO__source-rebuild-r03-decision-gate__OPERATOR.md`
commit `a56255c7b0f6e5b93239ed937a8e2ee37dc1bdff`
blob `408517dd797654c9c67b8f5f44000a934841eb58`.

## Effect

OPERATOR approves exactly the six candidate source documents in the reviewed r0.3 source set as the semantic basis for the next approved publication/activation preparation.

OPERATOR explicitly selects:

- recovery v1.6 r0.3 as successor lineage over pending recovery v1.5 r0.4;
- source-loading-policy v2.2 r0.3 as successor lineage over pending source-loading-policy v2.1.

Therefore predecessor gates are resolved by explicit OPERATOR selection, not by KOO inference.

### Recovery predecessor gate resolution

Gate:
`17190f729eef6537f0404af387253c9c11eb3a21`

Resolution:
`SUPERSEDED_BY_OPERATOR_SELECTED_V1_6_R03`

### Source-loading predecessor gate resolution

Gate:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`

Resolution:
`SUPERSEDED_BY_OPERATOR_SELECTED_V2_2_R03`

## Important boundary

This decision is semantic approval and lineage selection.

It does NOT itself:
- mutate Project Sources;
- activate the new source set;
- prove approved publication bytes/readback;
- bypass the source-set activation barrier;
- authorize a partial/mixed set;
- create automation authority.

Next causal step:
prepare exact approved-source publication set + activation/rollback operation from the reviewed r0.3 basis.

---
КТО: OPERATOR / recorded by KOO
ДЛЯ ЧЕГО: explicit approval and successor-lineage selection for source rebuild r0.3
СТАТУС: OPERATOR_DECISION_RECORDED
