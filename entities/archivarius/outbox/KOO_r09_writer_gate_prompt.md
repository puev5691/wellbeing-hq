АДРЕСАТ: КООРДИНАТОР / KOO

PROMPT:

ОПЕРАТОР разрешает выполнить только отдельный Writer Gate replacement KOO r0.9 после успешно завершённой initiation.

Resume-First. Сделай fresh preflight puev5691/wellbeing-hq, загрузи действующие approved Project Sources и проверь:
- exact initiation result r0.9;
- predecessor writer v0.8;
- exact handoff/freeze authority;
- exact immutable recovery r0.9;
- отсутствие более нового competing KOO writer, superseding handoff/freeze, recovery successor или replacement initiation;
- отсутствие более нового terminal result, который делает этот Writer Gate stale.

Exact initiation result:

puev5691/wellbeing-hq@8afcec859c66bf3b3c0f06cf8c9e49bcf0a3c85b:
entities/koordinator/outbox/KOO__replacement-cold-start-r09-initiation-result__OPERATOR.md

blob:
13a32310383ff5e96d23c704c714bc0f2518d4b3

status:
initiation_verified_waiting_writer_gate

Predecessor authoritative writer:

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

ARH preservation terminal:

PASS_ARH_KOO_SELF_PRESERVATION_R09_EXTERNALLY_PRESERVED

ARH result:

puev5691/wellbeing-hq@4e3bafce6e5bf70a426d474ddf5037531bc47552:
entities/archivarius/outbox/ARH__KOO-self-preservation-r09-result__KOO-OPERATOR.md

blob:
018e29fc096254d7c1211afdeab32449f59c25a6

Required action:

1. Выполни fresh Writer Gate reconciliation.
2. Если initiation identity, freeze authority, recovery identity и competing-writer checks PASS, установи текущий physical replacement KOO как authoritative current-writer r0.9.
3. Опубликуй один current-writer artifact:

entities/koordinator/current/KOO__replacement-current-writer-r09.md

4. В artifact явно зафиксируй:
   - status: WRITER_ESTABLISHED;
   - exact initiation result path/commit/blob;
   - predecessor v0.8 identity и frozen disposition;
   - exact handoff/freeze authority;
   - exact recovery r0.9 locator;
   - fresh pre-write HQ HEAD;
   - no competing valid KOO writer;
   - historical PROMPT replay: none;
   - all KOO profile tasks: PAUSED;
   - memory-layering attempt 3: NOT_AUTHORIZED;
   - Writer Gate не создаёт task authority и не возобновляет profile/routing work.
5. Выполни immutable readback current-writer artifact.
6. Сделай fresh post-write reconciliation и проверь, что между pre-write и publication не появился competing writer.
7. Верни exact:
   - path;
   - commit;
   - blob;
   - terminal/status.

Ожидаемый terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R09
или точный BLOCKED_* / FAIL_*.

Не выполнять после Writer Gate:
- Resume profile work;
- routing old tasks;
- historical PROMPT replay;
- memory-layering attempt 3;
- provider/Telegram/host/credential actions;
- external service mutation;
- automation mutation;
- Project Sources/canon mutation.

Все KOO profile tasks остаются PAUSED до отдельного последующего Resume-First и точного разрешённого перехода.

STOP после immutable Writer Gate result.

ДЕЙСТВИЕ ОПЕРАТОРА: открыть новый physical чат КООРДИНАТОРА и передать этот PROMPT целиком.
