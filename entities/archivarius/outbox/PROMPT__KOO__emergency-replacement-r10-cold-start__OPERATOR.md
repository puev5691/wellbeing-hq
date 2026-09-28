АДРЕСАТ: НОВЫЙ КООРДИНАТОР / KOO

Emergency replacement / Initiation-required.

ОПЕРАТОР подтверждает:

PREVIOUS_KOO_R09_TECHNICALLY_UNAVAILABLE = YES

Предыдущий authoritative KOO r0.9 технически недоступен и не способен самостоятельно выполнить новый handoff/freeze.

ОПЕРАТОР явно разрешает только emergency replacement cold-start initiation нового KOO instance.

Это разрешение:
- не является Writer Gate;
- не устанавливает current-writer;
- не возобновляет старые задачи;
- не разрешает historical PROMPT replay;
- не разрешает профильную/routing работу до завершения Initiation Gate и отдельного Writer Gate.

Сделай fresh GitHub-preflight puev5691/wellbeing-hq.

Загрузи текущие approved Project Sources согласно source-loading-policy, включая действующие:
- Project Core v2.5;
- Entity Roles v2.4;
- Source Loading Policy v2.2;
- Recovery Canon v1.6;
- File Work Canon v2.4;
- Task Conveyor Canon v1.2.

Проверь exact authoritative predecessor:

puev5691/wellbeing-hq@59378fc3e06e840b5f46c3b7f10beb0ae69c2995:
entities/koordinator/current/KOO__replacement-current-writer-r09.md

blob:
8659c738f7d0a2f595a6da3e0f88633268bd2b75

status:
WRITER_ESTABLISHED

Не выдумывай отсутствующий predecessor self-freeze artifact.

Загрузи и проверь двухслойную recovery basis.

BASE:

puev5691/wellbeing-entity-bootstrap@ab4c7ad12db9760fe825d2a93b6467499e1a09f4:
entities/koo/recovery/versions/koo-recovery-r09

composition/readback:
5/5 PASS

DELTA / latest independently preserved planned replacement recovery:

puev5691/wellbeing-entity-bootstrap@e07047dfce0684638e2164d1712dee06ac313cfc:
entities/koo/recovery/versions/koo-recovery-r10

composition/readback:
4/4 PASS

ARH preservation result:

puev5691/wellbeing-hq@15f411bbebe3f96c7ac9516b4aa7b6dc07f65815:
entities/archivarius/outbox/ARH__KOO-emergency-replacement-r10-prep__OPERATOR.md

blob:
10c0113519627c012999d73e69e5a1422b649989

Подготовительная проверка ARH установила:
- r0.9 остаётся последним доказанным authoritative KOO writer;
- r1.0 является последним independently preserved KOO recovery successor;
- r1.0 — delta поверх r0.9 base, а не отдельная замена base;
- после r1.0 self-snapshot не найдено более нового KOO current-state/profile mutation;
- KOO r1.0 initiation result не существует;
- KOO r1.0 current-writer не существует;
- competing replacement attempt не найден;
- newer recovery successor после r1.0 не найден.

IMPORTANT STALE BOUNDARY:

Recovery r1.0 не является полным transcript или автоматической current task queue.

После загрузки r0.9 base + r1.0 delta обязательно fresh-reconcile:
- entities/koordinator/current/
- entities/koordinator/inbox/
- entities/koordinator/outbox/
- routes/dispatch/
- routes/receipts/
- registry/by-sender/koordinator.jsonl
- relevant handoff/freeze/replacement evidence.

Не replay historical tasks/PROMPT.

MANDATORY HUMAN INTERFACE GATE:

Exact contract:

puev5691/wellbeing-entity-bootstrap@e07047dfce0684638e2164d1712dee06ac313cfc:
entities/koo/recovery/versions/koo-recovery-r10/KOO__human-interface-contract-r02.md

blob:
fdea31034c370220dfb961993059500716ccfe20

До terminal initiation_verified_waiting_writer_gate явно проверь H1-H8:

H1. Exact human-interface contract загружен.
H2. ОПЕРАТОР понимается как живой человек в чате и как роль полномочия в governance.
H3. Человеческое объяснение и машинное evidence — разные слои ответа.
H4. Чат по умолчанию — связный русский текст, а не protocol dump.
H5. Exact prompts/tasks остаются полными и удобными для копирования.
H6. Historical prompts не replay ради имитации continuity.
H7. Технические детали, не нужные человеку для действия, остаются в информационном поле.
H8. Новый instance способен связно объяснить текущую причинную цепочку до любой профильной работы.

Если H1-H8 PASS, дай короткое русскоязычное объяснение причинной цепочки:
- что пытался делать predecessor;
- что было сохранено;
- где оборвалась continuity;
- почему cold-start допустим;
- что остаётся запрещённым до Writer Gate.

Выполни ТОЛЬКО INITIATION GATE.

Проверь:
1. exact r0.9 base identity/integrity;
2. exact r1.0 delta identity/integrity;
3. predecessor r0.9 identity/status;
4. OPERATOR failure-state;
5. отсутствие newer valid KOO current-writer;
6. отсутствие competing replacement attempt;
7. отсутствие newer freeze/handoff/replacement conflict;
8. отсутствие superseding recovery/initiation;
9. current approved Project Sources;
10. fresh external evidence после r1.0 snapshot;
11. Human Interface Gate H1-H8.

Если всё PASS, верни:

initiation_verified_waiting_writer_gate

Если Human Interface Gate не доказан:

HUMAN_INTERFACE_GATE_NOT_VERIFIED

Если recovery загружен, но обязательная integrity boundary независимо не доказана:

initiation_loaded_external_unverified

Если package/version/composition не совпадает:

initiation_failed

Не выполнять Writer Gate в этом же шаге.

НЕ:
- создавать current-writer;
- возобновлять STP-C/P552203;
- возобновлять active queue автоматически;
- replay historical PROMPT;
- выполнять profile/routing work;
- изменять Project Sources/canon;
- изменять foreign current-state;
- запускать automation;
- использовать publication/dispatch/inbox как receipt/acceptance/processing proof.

Human-first terminal response:

1. ЧЕЛОВЕЧЕСКИЙ ИТОГ
   Что восстановлено, что доказано и что осталось неизвестным.

2. HUMAN INTERFACE GATE
   H1-H8 с кратким результатом.

3. ПРИЧИННАЯ ЦЕПОЧКА
   Коротко и по-русски.

4. ТЕХНОЛОГИЧЕСКАЯ ФИКСАЦИЯ
   Exact recovery identities, initiation result path / commit / blob / readback.

5. СЛЕДУЮЩИЙ GATE
   Явно:
   Writer Gate NOT YET PERFORMED.

6. АДРЕСАТ
   ОПЕРАТОР.

7. ГОТОВЫЙ PROMPT
   Один полный блок только для следующего Writer Gate, если initiation PASS.

8. ДЕЙСТВИЕ ОПЕРАТОРА
   Одно конкретное действие.

После immutable Initiation Gate result — STOP.
