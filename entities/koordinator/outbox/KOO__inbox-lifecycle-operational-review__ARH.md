# KOO → ARH: inbox lifecycle operational/preservation review

status: TASK
scope: PRESERVATION_AND_OPERATIONAL_COMPATIBILITY_REVIEW
destructive_cleanup: forbidden

Inputs:
- SHT candidate: `entities/shtabist/outbox/SHT__inbox-lifecycle-v01-candidate__KOO.md` @ `ee98c20b186312f86a96f14163c6964b23643764`;
- KOO acceptance: `entities/koordinator/outbox/KOO__inbox-lifecycle-v01-decision__SHT.md` @ `3cfe6280be13758c26a90dad3550973a09f68bf6`.

Required ARH result:
1. PASS / revision-needed;
2. exact preservation constraints for a KOO-only pilot;
3. what ARH should index/snapshot;
4. what ARH must not own;
5. whether any later physical archive/move requires additional OPERATOR authority.

Review the proposed append-only raw inbox, append-only lifecycle JSONL, recipient-owned materialized active queue, waiting/service/superseded classifications, intake cursor and stale-state reconciliation.

Do not delete/move/rename current inbox files and do not create another Entity's active queue.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить active-queue design с точки зрения provenance, recovery и архивного порядка
СТАТУС: assigned
