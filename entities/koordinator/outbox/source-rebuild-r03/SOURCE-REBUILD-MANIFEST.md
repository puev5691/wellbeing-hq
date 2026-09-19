# Пересборка базовых Project Sources — conveyor v1, revision r0.3

## Результат

Подготовлен согласованный кандидат нового корпуса из шести базовых управляющих источников. Действующие approved-файлы не изменяются задним числом: этот пакет становится новым active-source set только после решения ОПЕРАТОРА и фактической замены файлов в Project Sources.

## Новая архитектура ответственности

- `project-instructions-core` — общий режим, authority и различение механизмов;
- `entity-roles-short` — кто за что отвечает;
- `file-work-canon-universal` — создание, проверка, упаковка и доставка рабочих артефактов;
- `source-loading-policy` — что загружать и что не тащить в контекст;
- `entity-state-preservation-and-recovery-canon` — состояние, current-writer, preservation/recovery;
- `task-conveyor-canon` — **единственный владелец полного алгоритма передачи управления между Entity-чатами через PROMPT-файлы**.


## Reconciliation KAN K1–K6 в revision r0.3

Эта ревизия подготовлена только как bounded correction после
`KAN__project-sources-conveyor-v1-norm-review__KOO.md`
commit `3753f169063d3531a9455fe7d55ca0cdba9f7c3e`,
verdict `REQUIRES_EDITS_KAN_SOURCE_REBUILD_V1`.

Закрытие замечаний:

- **K1:** recovery candidate больше не конкурирует за target `v1.5`. Новый файл имеет target `v1.6`, интегрирует reviewed Wake/Writer layer r0.4 (`aea341e30d5d5297a491e7320674f2587d66d1e5`) и прямо сохраняет открытый OPERATOR gate `17190f729eef6537f0404af387253c9c11eb3a21` как unresolved lineage gate.
- **K2:** source-loading candidate переведён на `v2.2`, с exact lineage от reviewed v2.1 candidate `59ae5c036151460ca63a0e2ccd37d4aa53c88aaf`; открытый OPERATOR gate `b15a9250e72e7bb5da4efabd027fa4e43386022e` не закрывается и не supersede-ится молча.
- **K3:** task-conveyor canon и entity roles теперь явно фиксируют: conveyor материализует уже существующий authority и не создаёт standing instruction authority KOO; OPERATOR upload не является substantive approval.
- **K4:** task-conveyor, project core, entity roles, source-loading и recovery используют общий automation boundary: technical verification proves capability only; automatic activation требует отдельного standing/explicit automation-authority; `activation != processing_started`.
- **K5:** task-conveyor фиксирует `terminal_result != delivered != received != accepted`; `COMPLETED` зависит от declared terminal criterion и не закрывает parent workflow при незавершённых delivery/receipt/acceptance.
- **K6:** введён source-set activation barrier с exact-set approval/readback, `SOURCE_SET_INCOMPLETE`, fail-closed maintenance transition и rollback rule.

Revision r0.2 не утверждает ни один источник и не выбирает исход открытых OPERATOR gate.

## Что вынесено из существующих источников

### project core

Убрана отдельная нормативная роль `upload-task` из общего минимального документооборота. Добавлено только различение artifact delivery и Entity-chat activation со ссылкой на task-conveyor canon.

### entity roles

Сохранены только устойчивые обязанности ОПЕРАТОРА и KOO. Детали имени PROMPT, Resume-First последовательности, WIP-состояний и failure modes не дублируются.

### file-work canon

Файловый канон больше не изображает общий межчатовый цикл `файл -> запуск ОПЕРАТОРОМ/адресной Сущностью`. `upload-task` оставлен только для реальной ручной доставки рабочего артефакта и прямо исключён из стандартного task-conveyor wake-up. Для PROMPT-файлов введено явное исключение из обычной схемы `sender -> смысл -> recipient`.

### source-loading policy

Удалён собственный упрощённый алгоритм доставки «загрузить файл в адресный чат или зафиксировать невозможность». Вместо него разделены ссылки на file-work canon и task-conveyor canon. Task-conveyor canon добавлен в базовые управляющие источники. Исторические PROMPT-файлы запрещено тащить как постоянные управляющие источники.

### recovery canon

Не содержит алгоритм конвейера. Добавлено только recovery-специфичное правило: сохранять состояние шага, не воспроизводить исторические PROMPT, после Writer Gate fresh-reconcile и при необходимости создать новый PROMPT.

## Главное устранённое противоречие

Прежние источники одновременно говорили:

- не использовать ОПЕРАТОРА как лишний транспорт при доступной межсущностной доставке;
- создавать `upload-task` для ручной физической загрузки;
- считать GitHub/inbox частью маршрута;
- при этом фактическая технология запуска другого Entity-чата требовала от ОПЕРАТОРА загрузить PROMPT-файл.

В новой схеме это разведено:

- **artifact delivery** != **Entity-chat activation**;
- ручной PROMPT-transfer ОПЕРАТОРОМ является текущим механизмом активации интерфейса;
- GitHub остаётся информационным/evidence-контуром и не притворяется механизмом пробуждения чата.


## Reconciliation SHT D1–D3 и новое решение ОПЕРАТОРА в revision r0.3

Основание process-review:

`entities/shtabist/outbox/SHT__source-rebuild-r02-process-review__KOO.md`
commit `021619fd4162cf065054095d21f66fb1cf5fa00b`
blob `ed2ed7bc6bbcd96fbf46d1d1ffc22d3cfecdc75a`
verdict `REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`.

Исправлено только:

- **D1:** состояние теперь принадлежит exact conveyor attempt/PROMPT lineage; replacement требует явного `SUPERSEDED` либо `BLOCKED` predecessor disposition и successor/retry relation; одновременно current transferable/executable PROMPT для одного exact task lineage только один; `activation_failed != processing_failed`; replay без fresh reconciliation запрещён.
- **D2:** task-conveyor canon сужен до inter-chat/PROMPT activation; он baseline для KOO и participating PROMPT/chat instances, но не навязывается всем non-chat recovery-managed instances как постоянный источник.
- **D3:** rollback получил deterministic postcondition: exact previous set фиксируется заранее, все predecessor bytes восстанавливаются, newly introduced sources деактивируются, полный previous set проходит readback и только после этого maintenance завершается.

Дополнительное явное решение ОПЕРАТОРА после SHT review:

> PROMPT activation не требует физической передачи referenced artifacts, если адресная Сущность имеет проверяемый доступ к их exact locator и immutable identity. ОПЕРАТОР передаёт только activation PROMPT. Physical file transfer используется только когда locator недоступен адресату либо задача требует внешний файл, отсутствующий в общем информационном поле.

В r0.3 это реализовано без расширения task authority:
- PROMPT остаётся activation payload;
- PROMPT может быть direct text либо file-form;
- правило 40–50 символов применяется только к file-form PROMPT;
- exact task/input authority по-прежнему обязателен;
- locator-first access не означает delivery/receipt/acceptance;
- automation-authority и `activation != processing_started` сохранены.


## Source-set activation barrier после approval

Эта пересборка является взаимозависимым source-set. Она **не активируется последовательным принципом «часть уже новая, часть ещё старая»**.

Обязательные условия:

1. Решение ОПЕРАТОРА должно идентифицировать exact набор утверждаемых файлов и их SHA-256 как один source-set decision либо явно утвердить иной определённый subset.
2. До активации должны быть отдельно разрешены два открытых lineage-gate:
   - recovery v1.5 r0.4 OPERATOR gate `17190f729eef6537f0404af387253c9c11eb3a21`;
   - source-loading-policy v2.1 OPERATOR gate `b15a9250e72e7bb5da4efabd027fa4e43386022e`.
   Эта r0.2-ревизия не выбирает исход этих gate молча.
3. Частичная замена имеет статус `SOURCE_SET_INCOMPLETE` и **не считается coherent active source-set**.
4. Новый source-set становится authoritative только после того, как:
   - все требуемые новые approved bytes присутствуют;
   - выполнен readback exact identity всех файлов;
   - superseded active sources больше не активны;
   - отсутствует неоднозначный mixed set.
5. Если UI/механизм не позволяет атомарную замену, используется fail-closed maintenance transition:
   - до replacement фиксируется exact identity полного previous approved source-set;
   - профильная работа, зависящая от source-set, не начинается;
   - состояние фиксируется как `SOURCE_SET_MAINTENANCE`;
   - при failure восстанавливаются exact predecessor bytes всех replaced sources;
   - newly introduced sources, отсутствовавшие в previous set, включая task-conveyor canon, должны быть inactive/удалены из active Project Sources;
   - весь previous approved set проходит полный exact readback как единый coherent set;
   - только после PASS полного rollback readback разрешён переход `SOURCE_SET_MAINTENANCE -> previous approved set active`;
   - если любой rollback element не восстановлен/не проверен, состояние остаётся `SOURCE_SET_MAINTENANCE / SOURCE_SET_INCOMPLETE`;
   - partial/mixed set не используется как нормативная база.
6. Пробная cold-start initiation и реальный conveyor test выполняются **только после PASS activation barrier**.
7. Если тест требует ОПЕРАТОРУ заново объяснять механику конвейера или выявляет mixed-authority state, source-set возвращается на review, а не считается активированным по факту частичной загрузки.

Нормативный инвариант:

`package_approved != source_set_activated`

`partial_replacement = SOURCE_SET_INCOMPLETE`

## Статус

`candidate_set_r03_ready_for_sht_narrow_recheck`

## SHA-256 кандидатов revision r0.3

- `task-conveyor-canon-v1-candidate.md` — SHA-256 `7be4a0d30d0e8ad1653f9d3aea50f92ff2ed20a8190b7f9f722ea2b4a83b7644`
- `project-instructions-core-v2_2-candidate.md` — SHA-256 `8c3ed7faa58da334b5b8bc2cff2d2dcbac764c92e0ef7d22f664292e31b79fd2`
- `entity-roles-short-v2_4-candidate.md` — SHA-256 `e9a150d897932e02b123b180bca1939649045538100f652f379d52fd1cd6dcdb`
- `file-work-canon-universal-v2_4-candidate.md` — SHA-256 `04e670583b95880410ec70f42be1b705d3eb068e3fe4bddffeef27d4b5e95e10`
- `source-loading-policy-v2_2-candidate.md` — SHA-256 `081d8737c8e24ef58d9e9e7d17fbfc341c4736a181c584b05e854d298fd3644a`
- `entity-state-preservation-and-recovery-canon-v1_6-candidate.md` — SHA-256 `eead47bfd085e9473c729307c8d4aff06d3a8379283dc1cb91f803d2d592c673`

## Карта замены и SHA-256 действующих исходников

- `project-instructions-core-v2_1-approved(2).md` — SHA-256 `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26` → `project-instructions-core-v2_2-candidate.md`
- `entity-roles-short-v2_3-approved(1).md` — SHA-256 `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a` → `entity-roles-short-v2_4-candidate.md`
- `file-work-canon-universal-v2_3-approved(2).md` — SHA-256 `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5` → `file-work-canon-universal-v2_4-candidate.md`
- active `source-loading-policy-v2-approved(1).md` — SHA-256 `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061` → proposed `source-loading-policy-v2_2-candidate.md`, with reviewed v2.1 candidate/open gate retained as unresolved lineage
- active `entity-state-preservation-and-recovery-canon-v1_4-approved(1).md` — SHA-256 `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda` → proposed `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`, integrating reviewed v1.5 r0.4 and retaining its open OPERATOR gate as unresolved lineage
- новый источник без approved-предшественника → `task-conveyor-canon-v1-candidate.md`

## Review/activation boundary

Следующий предусмотренный профильный review: **SHT narrow recheck** D1–D3 и нового OPERATOR locator-first activation decision именно этой r0.3-ревизии.

До SHT/KAN/ARH review chain и отдельного решения ОПЕРАТОРА:
- package approval = `no`;
- Project Sources activation = `no`;
- open predecessor OPERATOR gates остаются open/unresolved;
- старые candidate-версии сохраняются как provenance и не выбираются/не утверждаются молча.
