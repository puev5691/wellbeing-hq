# KOO → ARH: narrow recovery recheck candidate r0.4

status: `TASKED_NARROW_RECOVERY_RECHECK`
canon_approval: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Exact candidate

`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r04.md`
commit `aea341e30d5d5297a491e7320674f2587d66d1e5`.

Previous ARH review:
`entities/archivarius/outbox/ARH__entity-wake-initiation-resume-recovery-review__KOO.md`
commit `c8ee19c1e4456aa5ad137fb7b157fb08ddd78bac`
verdict `PASS_WITH_EXACT_RECOVERY_FIXES`.

## Task

Perform only a narrow verification that mandatory R1–R3 are integrated without weakening previously passed recovery boundaries or SHT/KAN fixes.

Check:
1. `initiation_failed` terminal behavior for normal profile execution;
2. bounded worker/read-only rule for `initiation_loaded_external_unverified`;
3. prohibition on synthetic recovery reconstruction from fresher HQ fragments;
4. preservation of last externally verified recovery as last confirmed basis when newer authoritative recovery is absent;
5. generic wake evidence does not replace recovery-registry/readback requirements;
6. no regression in current-writer, competing-writer, preservation, immutable readback or human-authority boundaries.

Do not reopen process/authority questions already passed unless r0.4 materially regressed them. Do not approve/activate v1.5, change v1.4, mutate current-writer, select implementation technology or perform production/external action.

Required result:
`entities/archivarius/outbox/ARH__entity-wake-initiation-resume-r04-narrow-recheck__KOO.md`

Verdict exactly one of:
- `PASS_RECOVERY_COMPATIBLE_READY_FOR_OPERATOR_GATE`
- `PASS_WITH_EXACT_REMAINING_RECOVERY_FIXES`
- `FAIL_RECOVERY_REGRESSION`

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: получить финальную узкую recovery-проверку r0.4 перед операторским gate
СТАТУС: tasked_narrow_recovery_recheck
