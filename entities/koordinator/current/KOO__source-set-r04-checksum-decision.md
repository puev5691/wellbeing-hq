# OPERATOR decision — source-set r0.4 checksum identity resolution

status: OPERATOR_DECISION_RECORDED
decision: ACCEPT_ACTUAL_GIT_BLOB_SHA256_FOR_SOURCE_SET_R04
project_time: omitted; trusted project-time source not used

## Что решил ОПЕРАТОР

ОПЕРАТОР явно выбрал:

`ACCEPT_ACTUAL_GIT_BLOB_SHA256_FOR_SOURCE_SET_R04`

Это означает:

- exact successor commits/blobs сохраняются без переписывания;
- два SHA-256 в KAN SOURCE-SET-MANIFEST признаются ошибочной checksum metadata, возникшей из-за расхождения на один финальный LF;
- для activation barrier источником exact byte identity становятся независимо проверенные KOO SHA-256 фактических Git blobs;
- semantic source bytes не изменяются;
- частичная активация по-прежнему запрещена.

## Accepted exact successor identities

### project-instructions-core-v2_3-approved.md

commit:
`6286962c6218072d174f87e2a040687719fbe3a6`

blob:
`e51054d57c583bbbecc79716e1d5543e686efbd8`

accepted actual Git blob SHA-256:
`b115daa61782441e3b336dbedda216e4ea0b088fae12b374681a1069414d258e`

### task-conveyor-canon-v1_1-approved.md

commit:
`6d13d7ffcfb837492ed999c904a5f5bcc210b0a0`

blob:
`0ff3d3f74d5793ea72cc9e84fffc64f01e8455ab`

accepted actual Git blob SHA-256:
`904c4a89a459ab159758a50ae6cc56be25b988514388bd201a9872ad4a56e6d8`

## Four unchanged active sources

Remain unchanged:

- `entity-roles-short-v2_4-approved.md`
- `file-work-canon-universal-v2_4-approved.md`
- `source-loading-policy-v2_2-approved.md`
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`

## Remaining activation barrier

No supersession is effective yet.

The remaining operation is one bounded Project Sources membership replacement:

- replace active `project-instructions-core-v2_2-approved.md`
  with exact `project-instructions-core-v2_3-approved.md`;

- replace active `task-conveyor-canon-v1-approved.md`
  with exact `task-conveyor-canon-v1_1-approved.md`;

- leave the other four sources unchanged;

- do not treat an intermediate one-file replacement state as active authority;

- after both replacements, KOO must re-read active Project Source membership and exact file identities before declaring activation PASS.

## Effectivity boundary

Until that Project Sources replacement + readback PASS:

- core v2.2 remains active;
- task-conveyor v1.0 remains active;
- successor pair is approved but not active;
- supersession is not yet effective.

---
КТО: OPERATOR / recorded by KOO
ДЛЯ ЧЕГО: resolve exact checksum identity for source-set r0.4 activation
СТАТУС: OPERATOR_DECISION_RECORDED
