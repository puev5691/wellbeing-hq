# KOO → SHT: lifecycle convention for completed recovery records r0.1

status: `TASKED_PROCESS_DESIGN`
canon_change_authority: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Exact problem

ARH reported a verified structural ambiguity:
`entities/archivarius/outbox/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md`
commit `2ea877283576a5c14f9a8b19b7331e025a5ecd1f`.

A record under:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`
now semantically records completed verified recovery/current-writer reconciliation.

No approved convention currently defines whether completed recovery-state records remain under `recovery-pending/`, move elsewhere, or how provenance/old locators are preserved.

## Task

Design one bounded reusable organizational/process convention for recovery-record lifecycle states.

Check:
1. pending vs verified/completed vs superseded/historical semantics;
2. whether path relocation is necessary or whether semantic status is sufficient;
3. if relocation is recommended, exact minimal directory/state model;
4. preservation of old locators and provenance;
5. no authority/canon implication from a move/rename;
6. interaction with ARH recovery registry and immutable external recovery locators;
7. failure mode for interrupted moves or competing current-state updates;
8. whether one-record-specific repair should be avoided in favor of a reusable rule.

Do not move/delete/rename files. Do not change recovery/current-writer authority. Do not approve a canon change.

Required result:
`entities/shtabist/outbox/SHT__recovery-record-lifecycle-convention-r01__KOO.md`

Verdict exactly one of:
- `PASS_REUSABLE_LIFECYCLE_CONVENTION_PROPOSED`
- `PASS_KEEP_IN_PLACE_WITH_STATUS_RULE`
- `FAIL_PROCESS_RULE_REQUIRES_CANON_DECISION`

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: снять структурную двусмысленность completed recovery records без самовольного изменения файлового канона
СТАТУС: tasked_process_design
