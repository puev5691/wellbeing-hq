# KOO → KOD: emergency replacement initiation v0.3

status: `PREPARED_FOR_NEW_KOD_INSTANCE`
THIS_IS_NOT_A_PROFILE_TASK: `true`
production: `no`
project_time: omitted; trusted project-time source not used

## Authority

Emergency failover authority:
`entities/koordinator/outbox/KOO__KOD-emergency-failover-v03__OPERATOR.md`
commit `0ef6727698cdadbd6c5c2015fdf6e585a824b862`.

The previous KOD current-writer is retired for new mutations by explicit OPERATOR emergency decision. Do not rely on the old chat instance.

## Canonical recovery

Repository:
`puev5691/wellbeing-entity-bootstrap`

Immutable recovery locator:
`f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Exact initiation file:
`f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current/KOD__initiation-current__KOD.md`

Independent ARH verification in HQ:
`entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`
verdict `PASS_PUBLISHED_CANONICAL_RECOVERY`.

## Mandatory recovery-first sequence

1. Load the current approved Project Sources:
   - `project-instructions-core-v2_1-approved.md`;
   - `entity-roles-short-v2_3-approved.md`;
   - `file-work-canon-universal-v2_3-approved.md`;
   - `source-loading-policy-v2-approved.md`;
   - `entity-state-preservation-and-recovery-canon-v1_4-approved.md`.
2. Resolve the immutable recovery locator above.
3. Verify package composition and `sha256sums.txt` / immutable identities by external readback before trusting snapshot state.
4. Read initiation, snapshot, manifest, sources and experience files in the recovery package.
5. Set exact initiation status only as one of:
   - `initiation_verified`;
   - `initiation_loaded_external_unverified`;
   - `initiation_failed`.
6. Do a fresh preflight of `puev5691/wellbeing-hq`.
7. Reconcile KOD delta since recovery publication. Do not automatically resume historical inbox tasks.
8. Verify the former writer boundary:
   `entities/koder/current/KOD__replacement-current-writer-v02.md`
   commit `56db550005d6ed6956ba1bf753f3cb24ca295cc3`
   blob `23f20f04504c65497c154c099d8090cde11fba83`.
9. Verify emergency decision commit `0ef6727698cdadbd6c5c2015fdf6e585a824b862` and check that no newer competing KOD current-writer has appeared.
10. If and only if initiation is verified and no newer competing writer exists, establish one new immutable replacement current-writer marker v0.3 using the explicit emergency decision as authority.
11. Stop after writer establishment and return the initiation/writer result to KOO. Do not start profile work in the same step.

## Unfinished evidence tail to preserve, not trust blindly

Current unfinished task:
`entities/koordinator/outbox/KOO__openai-model-policy-extension-impl-r01__KOD.md`
commit `b98458343c6502c5fa6a3dec9dc9ca296c1cff2b`.

Partial commits:
- `7957b4d0211ed6cef96f54f2693c19b88e9f9d2e` — policy;
- `9824993082fccacfd09ac47ad465eb342803878e` — adapter;
- `715eeb2357e23605d0570a15a900c5ceeced705c` — live transport validation;
- `495053e79b37baec3b6239180becf214018f9b80` — runtime integration;
- `f501869c31b8a5d383bd36095356c46726f170c6` — tests.

Classification:
`UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`.

There is no verified terminal result for this task. After replacement-writer establishment, a separate Resume-First cycle may inspect and finish/reject/supersede this tail. Presence of code or tests is not PASS.

## Hard boundaries

Before initiation verification: read-only except initiation evidence/reporting.

This initiation does not authorize live provider calls, API keys, billing changes, production deployment, external project/private data transfer, TERA2/WBN execution, or automatic acceptance of partial implementation.

Expected first terminal result:
`PASS_KOD_EMERGENCY_INITIATION_V03_WRITER_ESTABLISHED`

or exact `BLOCKED_* / FAIL_*` with evidence.

Return result to KOO through the current Exchange Gate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: аварийно восстановить новый экземпляр KOD из проверенного recovery и свежего HQ evidence
СТАТУС: `prepared_for_operator_launch_into_new_kod_chat`
