# PROMPT — replacement KOO cold-start v0.8

Проведи replacement cold-start нового физического экземпляра KOO / КООРДИНАТОРА по действующему recovery-канону.

ОПЕРАТОР явно разрешил replacement предыдущего KOO v0.6.

Predecessor authoritative KOO writer:

entities/koordinator/current/KOO__replacement-current-writer-v06.md

blob:
90edff69b20879231fda8b882cbb172173e456f0

establishment commit:
525e5b131472e61b1f55db5ef7307217aea4c4fc

Exact handoff/freeze authority:

entities/archivarius/outbox/ARH__KOO-v06-handoff-freeze-authority-v08__OPERATOR-KOO.md

commit:
41020449328bc65de00bfa3ee83cee21761bce46

blob:
4b07e9815eaae17f79e15d02f2007c2cb708025f

status:
CURRENT_WRITER_HANDOFF_FREEZE_AUTHORIZED

Exact immutable recovery:

puev5691/wellbeing-entity-bootstrap@ef8e2c887fe95b69a99b0a0252027d9ee267ea2b:entities/koo/recovery/versions/koo-recovery-v08

ARH preservation terminal:

PASS_ARH_KOO_RECOVERY_V08_PRESERVED_READY_FOR_HANDOFF

result commit:
d46c77a7f5a685943b0aec732d75cf42c95eed9b

Recovery composition:
8/8 PASS

Required cold-start procedure:

1. fresh-preflight puev5691/wellbeing-hq;
2. load and independently verify current approved Project Sources;
3. verify exact recovery locator, immutable commit, 8-file composition, Git blobs, SHA256SUMS and readback;
4. verify predecessor KOO v0.6 writer and exact OPERATOR handoff/freeze authority above;
5. verify no newer competing valid KOO current-writer/handoff evidence exists;
6. fresh-reconcile KOO current/inbox/outbox/routes/receipts;
7. treat active-queue-r110 as stale evidence, not replay authority;
8. preserve the memory-layering attempt-2 terminal exactly:
   FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION;
9. attempt 3 remains NOT_AUTHORIZED;
10. classify all other work only from fresh repository evidence; UNKNOWN stays unknown;
11. historical PROMPT/tasks are evidence only and must not be replayed;
12. perform initiation only.

Return exactly one of:
- initiation_verified_waiting_writer_gate
- exact BLOCKED_* / FAIL_*.

STOP before Writer Gate and before profile/routing work.

Do not:
- establish a new current-writer in this step;
- resume historical tasks;
- authorize memory-layering attempt 3;
- issue provider/Telegram live authority;
- access credential contents;
- mutate external hosts/services/accounts.
