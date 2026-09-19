# KOO current active queue r0.48

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## OPERATOR decision

Decision:
`APPROVE_SOURCE_REBUILD_R03_AND_SELECT_SUCCESSOR_LINEAGE`.

Decision record:
`entities/koordinator/current/KOO__source-rebuild-r03-operator-decision.md`
commit `c1e44243eb57ef0e667d0b9c4e93c1991cbf1899`.

## Predecessor gates resolved

Recovery v1.5 r0.4 gate:
`17190f729eef6537f0404af387253c9c11eb3a21`
resolution:
`SUPERSEDED_BY_OPERATOR_SELECTED_V1_6_R03`
resolution commit:
`d07a843f57f962a02c5ee34ba8713ad08e4ef416`.

Source-loading v2.1 gate:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`
resolution:
`SUPERSEDED_BY_OPERATOR_SELECTED_V2_2_R03`
resolution commit:
`2fda0a3a6752f1170aee3b5968b5f493d39befc5`.

Both historical candidates remain provenance only.

## Exact approved publication set

Locator:
`puev5691/wellbeing-hq@fd8476883939aa4365c7dc3c5cbbfbc21752a620:entities/koordinator/outbox/source-set-r03-approved`

Boundary commit:
`fd8476883939aa4365c7dc3c5cbbfbc21752a620`

Boundary tree:
`ff97d2dca96c74aaa5faa75937bba0f56bfb676e`

Publication result:
`entities/koordinator/outbox/KOO__source-set-r03-approved-publication__OPERATOR.md`
commit `bfa7f3e96ca0fcd79d4dc6c9a95fe7ae0b7839d2`
verdict `PASS_KOO_SOURCE_SET_R03_APPROVED_PUBLICATION_READY_FOR_ACTIVATION`.

Approved set:
- project-instructions-core v2.2
- entity-roles v2.4
- file-work canon v2.4
- source-loading policy v2.2
- recovery canon v1.6
- task-conveyor canon v1

Project Sources activation:
`NO`.

## ACTIVE SLOT 1 — OPERATOR / PROJECT SOURCES UI REPLACEMENT

State:
`SOURCE_SET_R03_APPROVED_WAITING_OPERATOR_UI_REPLACEMENT`.

Barrier state during UI mutation:
`SOURCE_SET_MAINTENANCE`.

Required OPERATOR action:
- remove/deactivate the five predecessor Project Sources;
- upload exactly the six approved r0.3 source files;
- do not upload the activation manifest as a Project Source;
- return `SOURCE_SET_R03_UI_REPLACEMENT_DONE`.

Rollback:
if UI replacement is incomplete or uncertain, restore the previous complete five-source approved set and return `SOURCE_SET_R03_ROLLBACK_DONE`.

KOO must verify actual Project Source membership/identities after OPERATOR reports completion before declaring activation PASS.

## PENDING AFTER UI REPLACEMENT

1. verify complete six-source membership;
2. verify five predecessor sources are inactive;
3. verify exact identities where available;
4. confirm no mixed set;
5. declare `SOURCE_SET_ACTIVATED` only after barrier PASS;
6. then run cold-start/source-loading + task-conveyor smoke checks.

## PENDING PARALLEL

KOD shard gateway adapter independent verify remains:
`CURRENT_PENDING_NOT_ACTIVE`.

Do not mix it into the source-set activation barrier.

## EXACT NEXT CAUSAL STATE

`SOURCE_SET_R03_APPROVED_WAITING_OPERATOR_UI_REPLACEMENT`

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: current state after OPERATOR approval and exact approved-source publication
СТАТУС: WAITING_OPERATOR_UI_REPLACEMENT
