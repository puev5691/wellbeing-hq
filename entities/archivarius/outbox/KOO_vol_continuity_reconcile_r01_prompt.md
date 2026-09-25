АДРЕСАТ: КООРДИНАТОР / KOO

PROMPT:

Resume-First. Сделай fresh preflight puev5691/wellbeing-hq, загрузи действующие approved Project Sources, проверь KOO current-writer, supersession, receipt/processing evidence и отсутствие более нового competing VOL continuity/recovery result.

Exact ARH terminal result:
puev5691/wellbeing-hq@997fe4b020afe2a14c95313a9bf5c97862be00f5:
entities/archivarius/outbox/ARH__vol-continuity-recovery-triage-r01__KOO.md
blob ff8bff197112ce9e7f4d8a6086dc72b72a7afbde
terminal PASS_ARH_VOL_CONTINUITY_RECOVERY_TRIAGE_R01_WITH_BOUNDARIES.

Ключевые установленные границы:
- last independently verified VOL recovery bytes: preserved/verified;
- old recovery: STALE_FOR_DIRECT_TASK_REPLAY;
- VOL current-writer: UNKNOWN_NOT_VERIFIED;
- VOL writer availability: UNKNOWN;
- new preservation checkpoint: REQUIRED_BEFORE_NORMAL_REPLACEMENT;
- ARH cannot author VOL self-snapshot;
- Library context candidate is NOT_VOL_SELF_SNAPSHOT / NOT_CANONICAL_RECOVERY;
- Memory-layering attempt 3: NOT_AUTHORIZED;
- historical PROMPT/task replay: NONE.

Exact last verified recovery:
puev5691/wellbeing-entity-bootstrap@f6ff070313caff5d7b5d12779d4bb8d8eb0eec01:
entities/vol/recovery/current/VOL_recovery-manifest_VOL.md
blob e2c1547b826fc0f5cae5f58e80838f2a068dcc8b.

Выполни только fresh reconciliation следующего gate.

1. Независимо прочитай exact ARH result и его addressed inbox/dispatch.
2. Зафиксируй receipt только после фактического чтения.
3. Проверь, существует ли теперь проверяемое evidence authoritative current VOL writer и его фактической доступности.
4. Не выводи writer identity из имени чата, Library candidate, старого recovery manifest или поздних VOL outbox-файлов без отдельного writer evidence.
5. Если current VOL writer подтверждён и доступен:
   - подготовь ОПЕРАТОРУ один готовый manual activation PROMPT именно этому VOL writer на создание текущего authoritative self-snapshot/recovery checkpoint;
   - PROMPT должен требовать fresh preflight, доказательство continuity/current-writer, reconciliation всего VOL delta после старого recovery, отсутствие historical replay, exact frontier/open gates/dependencies/failure-state, publication/self-readback и возврат ARH на independent preservation verification;
   - не инициируй replacement сам.
6. Если current VOL writer не подтверждён либо доказанно недоступен:
   - не назначай writer и не инициируй replacement;
   - подготовь ОПЕРАТОРУ один точный decision block для отдельного emergency failover authority;
   - failure-state должен быть доказан и назван точно, например FAILURE_STATE_VOL_CURRENT_WRITER_UNAVAILABLE_OR_UNVERIFIABLE только если это поддерживается fresh evidence;
   - authority должна отдельно разрешать использование старого recovery как stale recovery basis, replacement initiation с fresh delta reconciliation, запрет historical replay и отдельный Writer Gate.
7. Если evidence остаётся недостаточным для обоих вариантов, верни точный BLOCKED и минимальный факт, который должен предоставить/подтвердить ОПЕРАТОР.

Не выполнять:
- VOL self-snapshot за VOL;
- replacement initiation;
- Writer Gate;
- historical task replay;
- recovery mutation;
- host/secrets/provider work;
- automation mutation;
- Project Sources/canon mutation.

Если следующий шаг требует другого Entity-чата и automatic activation exact scope не доказан, верни ОПЕРАТОРУ готовый блок:
АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА.

STOP после одного reconciliation/decision-preparation result.

ДЕЙСТВИЕ ОПЕРАТОРА: открыть чат КООРДИНАТОРА и передать этот PROMPT целиком.
