АДРЕСАТ: КООРДИНАТОР / KOO

PROMPT:

Проведи только replacement cold-start нового physical KOO / КООРДИНАТОРА по действующему recovery-канону.

ОПЕРАТОР явно разрешил replacement предыдущего authoritative KOO v0.8.

Predecessor writer:

entities/koordinator/current/KOO__replacement-current-writer-v08.md

establishment commit:
9781aeff09d868ade3f3e1a28f28014d23512386

blob:
ca7ed0ed4e539dcdbe783e122cea409a77ab10cd

Exact handoff/freeze authority:

entities/archivarius/outbox/ARH__KOO-v08-handoff-freeze-authority-r09__OPERATOR-KOO.md

commit:
93ecf356eca736457f1adf69aaa77ff73fc04c00

blob:
621101e1a6480c9f8dce10226731c720c0be5907

status:
CURRENT_WRITER_HANDOFF_FREEZE_AUTHORIZED

Exact immutable recovery:

puev5691/wellbeing-entity-bootstrap@ab4c7ad12db9760fe825d2a93b6467499e1a09f4:
entities/koo/recovery/versions/koo-recovery-r09

ARH preservation result:

puev5691/wellbeing-hq@4e3bafce6e5bf70a426d474ddf5037531bc47552:
entities/archivarius/outbox/ARH__KOO-self-preservation-r09-result__KOO-OPERATOR.md

blob:
018e29fc096254d7c1211afdeab32449f59c25a6

terminal:
PASS_ARH_KOO_SELF_PRESERVATION_R09_EXTERNALLY_PRESERVED

Recovery composition:
5/5 PASS

External readback:
5/5 PASS

Required cold-start procedure:

1. Fresh-preflight puev5691/wellbeing-hq and verify current repository state.
2. Load and independently verify current approved Project Sources under source-loading policy.
3. Verify exact immutable recovery locator above, full 5-file composition, Git blobs, SHA256SUMS and readback.
4. Verify predecessor KOO v0.8 writer identity and exact handoff/freeze authority above.
5. Verify no newer competing valid KOO current-writer, handoff/freeze, recovery successor or superseding initiation authority exists.
6. Fresh-reconcile current/inbox/outbox/routes/receipts and all relevant terminal results newer than the r0.9 self-snapshot boundary.
7. Treat the r0.9 self-snapshot as recovery evidence, not as permission to replay any historical task.
8. Preserve the explicit pause: all other KOO profile tasks remain paused until a later separately authorized transition.
9. Preserve exact memory-layering terminal:
   FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION.
10. Memory-layering attempt 3 remains NOT_AUTHORIZED.
11. UNKNOWN remains UNKNOWN; do not reconstruct missing state from memory, chat context, timestamp or plausibility.
12. Perform initiation only.

Return exactly one of:
- initiation_verified_waiting_writer_gate
- exact BLOCKED_* / FAIL_*.

If initiation passes, publish one immutable initiation-result artifact in puev5691/wellbeing-hq, perform exact readback and return:
- path;
- commit;
- blob;
- status.

STOP before Writer Gate and before profile/routing work.

Do not:
- establish a new current-writer;
- resume any paused/historical task;
- authorize memory-layering attempt 3;
- issue provider/Telegram/host/credential authority;
- mutate external services;
- change automation;
- modify Project Sources or canons.

ДЕЙСТВИЕ ОПЕРАТОРА: создать/открыть новый physical чат КООРДИНАТОРА и передать этот PROMPT целиком.
