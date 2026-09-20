# KOO current active queue r0.62

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## SOURCE SET R0.4 — CHECKSUM DECISION RESOLVED

OPERATOR decision:
`ACCEPT_ACTUAL_GIT_BLOB_SHA256_FOR_SOURCE_SET_R04`.

Decision record:
`entities/koordinator/current/KOO__source-set-r04-checksum-decision.md`

commit:
`bfbb04bdc57674f428efa52ee06f502f8ecd37b9`.

Meaning:
- exact successor commits/blobs remain unchanged;
- KAN manifest SHA mismatch is resolved as checksum metadata error caused by final-LF discrepancy;
- actual Git blob SHA-256 values are authoritative for this activation barrier.

## Accepted exact successor identities

### core v2.3

commit:
`6286962c6218072d174f87e2a040687719fbe3a6`

blob:
`e51054d57c583bbbecc79716e1d5543e686efbd8`

SHA-256:
`b115daa61782441e3b336dbedda216e4ea0b088fae12b374681a1069414d258e`

### task-conveyor v1.1

commit:
`6d13d7ffcfb837492ed999c904a5f5bcc210b0a0`

blob:
`0ff3d3f74d5793ea72cc9e84fffc64f01e8455ab`

SHA-256:
`904c4a89a459ab159758a50ae6cc56be25b988514388bd201a9872ad4a56e6d8`

## Four unchanged active sources

Remain unchanged:
- `entity-roles-short-v2_4-approved.md`
- `file-work-canon-universal-v2_4-approved.md`
- `source-loading-policy-v2_2-approved.md`
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`

## CURRENT BARRIER STEP — OPERATOR PROJECT SOURCES UI REPLACEMENT

Exact operation artifact:
`entities/koordinator/outbox/KOO__source-set-r04-ui-replacement__OPERATOR.md`

commit:
`7380a8c73b09e701d237ae96f4cc8f2c0b551226`

blob:
`24c122899619624496d15e456b99ad2bb348dcbd`

OPERATOR inbox:
`43574e8d8e339e38d718530cf1c8e031c668220b`.

Required UI operation:
1. replace/remove active `project-instructions-core-v2_2-approved.md`;
2. add exact `project-instructions-core-v2_3-approved.md`;
3. replace/remove active `task-conveyor-canon-v1-approved.md`;
4. add exact `task-conveyor-canon-v1_1-approved.md`;
5. leave the other four active sources unchanged;
6. complete both replacements before resuming source-dependent normative work.

After UI completion OPERATOR returns exact signal:
`SOURCE_SET_R04_UI_REPLACEMENT_DONE`.

## Effectivity boundary

Until KOO performs post-UI active-payload readback PASS:
- core v2.2 remains authoritative;
- conveyor v1.0 remains authoritative;
- core v2.3 and conveyor v1.1 are approved successors but not yet active;
- supersession is not yet effective;
- partial/mixed set must not be treated as authority.

## NEXT KOO ACTION AFTER SIGNAL

Fresh readback must verify:
- intended active source membership = exactly 6;
- successor core present;
- successor conveyor present;
- predecessor core absent;
- predecessor conveyor absent;
- four unchanged sources present and unchanged;
- exact identities/content match;
- no activation manifest loaded as source;
- no mixed old/new set.

Only then declare:
`SOURCE_SET_R04_ACTIVATED`

and record:
- core v2.2 → v2.3;
- task-conveyor v1.0 → v1.1.

## EXACT NEXT CAUSAL STATE

`SOURCE_SET_R04_WAITING_OPERATOR_UI_REPLACEMENT`

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: state after OPERATOR checksum-resolution decision
СТАТУС: WAITING_OPERATOR_UI_ACTION
