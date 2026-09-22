# Канон конвейера задач проекта «БЛАГОПОЛУЧИЕ» — v1.2 approved

Кратко: конвейер задач связывает отдельные Entity-чаты через адресные PROMPT-активации. КООРДИНАТОР читает проверяемое состояние, выбирает следующий допустимый уже авторизованный шаг и формирует PROMPT; адресная Сущность после активации выполняет Resume-First, сама получает требуемые материалы из информационного поля по exact locator, проверяет immutable identity, исполняет задачу в заданных границах и возвращает проверяемый terminal result.

Этот документ регулирует именно **активацию и передачу управления между отдельными Entity-чатами**. Он не заменяет файловый канон, recovery-канон и правила адресной доставки артефактов. PROMPT может быть материализован как файл или как прямой текстовый activation payload; file-form является формой интерфейса, а не обязательной физической упаковкой входных артефактов.

## 1. Назначение и граница

Конвейер нужен там, где следующий рабочий шаг должен выполнить другой существующий Entity-чат, а проверенного автоматического механизма, способного гарантированно возобновить именно этот чат, нет.

В текущей технологии:

- GitHub и другие разрешённые внешние контуры дают проверяемое информационное поле, версии, результаты и evidence;
- PROMPT передаёт управление конкретному Entity-чату;
- PROMPT содержит exact locator и immutable identity значимых входов вместо обязательного физического переноса этих входных файлов;
- если адресная Сущность имеет проверяемый доступ к exact locator, ОПЕРАТОР не переносит referenced artifacts вручную;
- physical artifact transfer используется только когда locator недоступен адресату либо сама задача требует внешний файл, отсутствующий в общем информационном поле;
- сама публикация task/result в GitHub, `inbox`, `dispatch` или registry **не считается активацией Entity-чата**.

Технически проверенный автоматический адаптер может заменить ручной перенос PROMPT-файла только если для точного scope существует **отдельно утверждённое standing или explicit authority на автоматическую активацию**. Техническая проверка доказывает capability, но не создаёт task authority, writer authority, approval, production authority или `processing_started`.

Инвариант:

`verified_automation_capability != automation_authority`

и отдельно:

`activation != processing_started`.

## 2. Термины

**Шаг конвейера** — одна конкретная задача одной адресной Сущности с проверяемым результатом или точным blocker.

**PROMPT** — адресный activation payload с достаточной для безопасного начала работы инструкцией. Он может быть передан прямым текстом либо материализован как Markdown PROMPT-файл. Значимые входы не обязаны физически вкладываться в PROMPT: если они доступны в информационном поле, PROMPT указывает exact locator + требуемую immutable identity.

**PROMPT-файл** — файловая форма PROMPT для интерфейсов/сценариев, где удобна или требуется передача самостоятельного файла. Он не является контейнером обязательных копий referenced artifacts.

**Активация Entity-чата** — фактическая передача актуального PROMPT в правильный чат адресной Сущности либо работа технически проверенного автоматического адаптера, **для которого отдельно существует применимое automation-authority на этот exact scope**. Активация означает запуск интерфейсного цикла, но сама по себе не доказывает `processing_started` и не создаёт substantive task authority.

**Terminal result** — проверяемый результат, PASS/FAIL/BLOCKER или другой явно предусмотренный конечный факт шага.

**Информационное поле** — внешнее проверяемое состояние проекта: GitHub, approved Project Sources и другие разрешённые источники истины. Информационное поле само по себе не заменяет активацию Entity-чата.

## 3. Базовая формула

    terminal result / новое проверяемое событие
    -> KOO fresh reconciliation
    -> классификация current / completed / blocked / superseded
    -> выбор следующего допустимого шага
    -> создание адресного PROMPT
    -> фиксация exact locator/identity входов
    -> проверка содержимого и, для file-form, имени
    -> передача PROMPT в адресный Entity-чат
    -> referenced artifacts читаются адресатом из информационного поля по locator
    -> адресная Сущность выполняет Resume-First
    -> исполнение
    -> terminal result
    -> новый цикл

Нельзя подменять этот цикл формулой `опубликовал в GitHub -> значит Сущность работает`.

### Инвариант authority конвейера

Task conveyor **материализует и переносит уже разрешённый шаг, но не создаёт task authority**.

KOO может выбирать последовательность и формировать PROMPT только для шага, authority которого уже существует в одном из допустимых оснований:

- профильная роль адресата + действующий approved process;
- standing delegation;
- exact decision/instruction уполномоченного источника;
- иной явно проверяемый authority basis, допустимый действующими approved-нормами.

Если для следующего шага требуется новое approval/instruction, конвейер останавливается на соответствующем gate. Сам факт того, что task-conveyor canon является approved process, не превращает KOO в общий источник поручений.

Передача PROMPT ОПЕРАТОРОМ является **activation/transport**, а не содержательным approval PROMPT-а, если ОПЕРАТОР отдельно и явно не принимает такое решение. Передача PROMPT не требует физической передачи referenced artifacts, доступных адресату по exact locator.

Инвариант:

`conveyor_step_materialization != task_authority`


## 4. Роли

### ОПЕРАТОР

ОПЕРАТОР:

- принимает человеческие решения и приоритеты, которые требуют его authority;
- получает от КООРДИНАТОРА готовый PROMPT либо file-form PROMPT;
- передаёт его в указанный Entity-чат, если применимого automatic activation authority нет;
- не обязан переносить referenced artifacts, если адресная Сущность может получить их по exact locator;
- не обязан самостоятельно реконструировать задачу из GitHub, очереди или набора locator;
- возвращает управление КООРДИНАТОРУ после появления terminal result либо сообщает о фактической невозможности активации.

Ручная загрузка PROMPT-файла в адресный чат является **активацией рабочего интерфейса**, а не обычной межсущностной доставкой результата. Поэтому запрет использовать ОПЕРАТОРА как лишний транспорт артефактов к этому шагу не применяется.

### КООРДИНАТОР / KOO

КООРДИНАТОР:

1. выполняет свежий preflight информационного поля;
2. читает terminal results и актуальную очередь;
3. не восстанавливает статус по памяти старого чата;
4. классифицирует задачи как `current / completed / blocked / superseded`;
5. соблюдает действующий WIP и не создаёт дубли;
6. выбирает следующий допустимый шаг;
7. создаёт один готовый PROMPT для конкретной адресной Сущности;
8. указывает exact locator + immutable identity требуемых входов, доступных в информационном поле;
9. проверяет содержимое, границы authority и, для file-form, имя;
10. после нового результата снова читает информационное поле и формирует следующий шаг.

KOO не должен заменять PROMPT:

- одним только GitHub locator без инструкции;
- файлом `inbox`;
- dispatch-записью;
- сообщением «продолжай работу» без точной инструкции.

Но сам PROMPT **может ссылаться** на exact locator входов вместо физического копирования этих входов в чат.

### Адресная Сущность

Получив PROMPT-файл, Сущность:

1. считает файл текущим поручением только после проверки адресата и свежего Resume-First;
2. выполняет указанный preflight;
3. проверяет current-writer/recovery boundary, если это требуется её режимом;
4. проверяет exact task, входы и immutable identities;
5. исполняет только разрешённый объём;
6. при stale/conflict/mismatch останавливается с точным blocker;
7. формирует проверяемый terminal result;
8. если после terminal result работа должна продолжиться в другом Entity-чате и automatic activation для exact scope отсутствует, включает в human-facing ответ готовый manual activation handoff по §10;
9. маршрутизирует результат предусмотренным способом;
10. останавливается после terminal result, если PROMPT не содержит иной явно разрешённой последовательности.

## 5. Имя PROMPT-файла

Этот раздел применяется только когда PROMPT материализован как файл.

Полное имя файла **включая расширение** должно содержать от **40 до 50 символов**.

Имя строится так:

    <КОД_АДРЕСНОЙ_СУЩНОСТИ>_<тема>_<этап>_prompt.md

Обязательные правила:

- имя начинается с кода адресной Сущности;
- сразу после кода идёт тема задачи;
- используются короткие смысловые латинобуквенные технические обозначения;
- используются одинарные `_`;
- не добавляется код КООРДИНАТОРА в начало;
- не используется бессодержательное `task`, `new`, `final`, `latest` вместо темы;
- при выходе за диапазон 40–50 символов имя перерабатывается **до передачи ОПЕРАТОРУ**.

Примеры корректных имён:

- `SIS_openai_cost_matrix_r02_resume_prompt.md` — 43 символа;
- `SHD_telegram_live_ingest_verify_prompt.md` — 41 символ;
- `KOD_resource_gateway_worker_build_prompt.md` — 43 символа;
- `RED_project_history_r02_review_prompt.md` — 40 символов.

Правила именования обычных маршрутизируемых артефактов из файлового канона на PROMPT-файлы конвейера не распространяются.

## 6. Обязательное содержимое PROMPT-файла

PROMPT должен быть самодостаточным для адресного чата, но не превращаться в копию всего проекта.

Он содержит, насколько применимо:

1. **Адресата и тему.** Кто исполняет и что является текущей задачей.
2. **Resume-First.** Требование начать со свежего preflight соответствующего информационного поля.
3. **Authoritative current-state.** Exact current-writer / Writer Gate / recovery boundary, если они важны для задачи.
4. **Exact task.** Commit, locator, файл или иной однозначный идентификатор поручения.
5. **Exact task authority.** Если authority не выводится однозначно из уже approved standing process + роли адресата, PROMPT обязан содержать exact authority basis/decision/delegation. Отсутствие такого basis является stop condition.
6. **Необходимые входы.** Только те артефакты и результаты, без которых текущий шаг нельзя проверить. По умолчанию указываются exact locator + immutable identity; физическая передача referenced artifact не требуется, если адресат может получить и проверить его из информационного поля.
7. **Требуемое действие.** Что именно сделать сейчас.
8. **Границы authority.** Что разрешено и что не разрешено этим PROMPT.
9. **Stop conditions.** При каких несовпадениях или недостатке данных исполнение прекращается.
10. **Критерий результата.** Какой PASS/FAIL/BLOCKER или файл считается terminal result.
11. **Возврат результата.** Кому и каким проверяемым способом вернуть terminal result.
12. **Stop after result.** Если следующая задача не входит в тот же явно разрешённый шаг, Сущность после результата останавливается.

PROMPT не должен заставлять Сущность читать весь архив «для сведения».

## 7. Resume-First в конвейере

До профильного действия адресная Сущность обязана:

- сделать свежий preflight указанного источника истины;
- убедиться, что PROMPT не superseded;
- проверить отсутствие конфликтующего current-writer/authority, если это относится к задаче;
- проверить exact inputs и dependencies;
- проверить terminal results, которые могли появиться после формирования PROMPT;
- при обнаружении нового terminal result не выполнять устаревший шаг повторно.

PROMPT является **материализованной формой уже существующего поручения/authority basis**, но сам по себе authority не создаёт и не разрешает игнорировать более свежую проверяемую реальность.

## 8. WIP, attempt lineage и дубли

Состояние конвейера относится к **конкретному conveyor attempt / PROMPT lineage**, а не одновременно и неоднозначно к task, PROMPT artifact и execution attempt.

Для одного exact task lineage одновременно transferable/executable может быть только **один current PROMPT attempt**.

KOO обязан различать как минимум:

- `READY_FOR_PROMPT`;
- `PROMPT_PREPARED`;
- `AWAITING_OPERATOR_TRANSFER`;
- `AWAITING_ENTITY_RESULT`;
- `BLOCKED`;
- `COMPLETED`;
- `SUPERSEDED`.

Минимальная transition model:

- `READY_FOR_PROMPT -> PROMPT_PREPARED`;
- `PROMPT_PREPARED -> AWAITING_OPERATOR_TRANSFER` после materialization/validation;
- `AWAITING_OPERATOR_TRANSFER -> AWAITING_ENTITY_RESULT` только после доказанной activation attempt;
- любой open attempt -> `BLOCKED`, если продолжение требует недостающего external fact/authority;
- любой open attempt -> `SUPERSEDED`, если появился current successor либо изменились authoritative inputs;
- `AWAITING_ENTITY_RESULT -> COMPLETED` только по declared terminal criterion.

Перед созданием replacement PROMPT старый open attempt обязан получить non-executable disposition:

- `SUPERSEDED` с exact successor relation; либо
- `BLOCKED` с явным retry/successor relation.

`activation_failed != processing_failed`.

Activation failure не разрешает replay автоматически. Replacement допускается только после fresh reconciliation exact task identity, authority, inputs и processing evidence.

Manual и automated activation используют одну transition rule. Stale/superseded predecessor не может снова стать executable без нового явно авторизованного перехода.

Эти состояния не обязаны порождать отдельный документ на каждый переход; достаточно текущей проверяемой очереди и фактических артефактов, если successor/predecessor relation остаётся однозначно проверяемой.

### Terminal result и `COMPLETED`

Terminal result закрывает **исполнительную попытку/шаг** в пределах его declared terminal criterion. Он не является delivery, receipt, acknowledgement или substantive acceptance.

Инвариант:

`terminal_result != delivered != received != accepted`

Статус `COMPLETED` допустим только если выполнен именно declared terminal criterion шага. Если критерий требует адресной доставки результата, receipt или substantive acceptance, эти факты проверяются отдельно до перевода соответствующего workflow/parent step в `COMPLETED`.

`PASS` результата не может молча закрыть родительскую задачу, которая ещё ждёт delivery/receipt/acceptance.

## 9. GitHub и адресная доставка результатов

GitHub может хранить:

- current queue;
- exact tasks;
- результаты;
- immutable identities;
- evidence;
- dispatch/receipt для межсущностных артефактов.

Но GitHub не считается доказательством, что конкретный Entity-чат проснулся и начал исполнение.

PROMPT можно дополнительно публиковать в GitHub для provenance, если это практически нужно. Такая публикация **не обязательна только ради запуска шага**.

Referenced inputs, уже находящиеся в доступном информационном поле, не переносятся в чат повторно: адресат читает exact locator и проверяет immutable identity. Physical transfer используется только как fallback при недоступном locator либо для внешнего файла, которого нет в общем информационном поле.

Terminal result и значимые рабочие артефакты после исполнения маршрутизируются по файловому канону. Это отдельная процедура от активации Entity-чата.

## 10. Manual activation handoff после terminal result

Пока exact scope не покрыт утверждённым и фактически работающим automatic chat-resume/orchestrator, каждый human-facing terminal result, после которого работа должна продолжиться в другом Entity-чате, содержит готовый блок:

    АДРЕСАТ: <точное имя Сущности>
    PROMPT: <готовый activation payload, который ОПЕРАТОР может целиком передать в адресный чат>
    ДЕЙСТВИЕ ОПЕРАТОРА: открыть чат указанной Сущности и передать PROMPT.

PROMPT обязан содержать все уже доступные exact locator + immutable identity, необходимые адресату. ОПЕРАТОР не обязан собирать PROMPT из нескольких сообщений, реконструировать задачу из GitHub/очереди/locator или переносить referenced artifacts, если адресная Сущность может получить и проверить их из информационного поля.

Если исполнившая Сущность не имеет authority определить следующий профильный шаг, она не придумывает его. В human-facing terminal result используется безопасный fallback:

    АДРЕСАТ: КООРДИНАТОР
    PROMPT: Выполни fresh Resume-First reconciliation информационного поля после terminal result <exact locator + immutable identity>. Определи следующий допустимый уже авторизованный шаг. Если нужен другой Entity-чат и automatic activation для exact scope отсутствует, верни ОПЕРАТОРУ готовый блок АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА. Не проси ОПЕРАТОРА реконструировать задачу или собирать уже доступные основания вручную.
    ДЕЙСТВИЕ ОПЕРАТОРА: открыть чат КООРДИНАТОРА и передать PROMPT.

Publication, inbox, dispatch, receipt, сообщение «результат маршрутизирован» или факт создания PROMPT не заменяют manual activation handoff и не доказывают фактический запуск адресного Entity-чата.

Когда следующий шаг определяет КООРДИНАТОР, его нормальный human-facing ответ использует тот же блок `АДРЕСАТ / PROMPT / ДЕЙСТВИЕ ОПЕРАТОРА`. File-form PROMPT допустим, если ОПЕРАТОР получает точный адрес и готовое действие без самостоятельной реконструкции.

### Редакционный сигнал значимого события для литературного журнала

`JOURNAL_CANDIDATE` — необязательный положительный post-terminal signal для события, которое имеет явную историческую или редакционную ценность для литературного журнала проекта.

Signal допустим, если terminal result или подтверждённое им событие, например:

- меняет архитектуру, правило или существенное направление проекта;
- фиксирует серьёзную неудачу вместе с новым практическим выводом;
- закрывает первый либо иной заметный реальный рубеж;
- создаёт новую устойчивую практику;
- содержит важный человеческий контекст, характерный или смешной эпизод, полезный для будущей истории проекта.

Для routine result signal не создаётся. Поле `JOURNAL_CANDIDATE: no` не требуется.

Если событие отмечается как candidate, **тот же terminal result artifact** может после основной человекочитаемой части содержать компактный блок:

    JOURNAL_CANDIDATE: yes
    СМЫСЛ: <1–3 предложения, почему событие исторически или редакционно важно>
    EVIDENCE: <exact locator + immutable identity события/основания, если они уже известны>

Отдельный artifact только ради `JOURNAL_CANDIDATE` не создаётся.

Если immutable identity самого terminal result становится известна только после публикации, исполнившая Сущность не переписывает результат и не создаёт второй файл ради самоссылки. KOO при fresh reconciliation связывает signal с уже проверенной immutable identity маршрутизированного terminal result из информационного поля. Поле `EVIDENCE` может указывать на более раннее exact основание события, если оно уже существует.

Наличие или отсутствие `JOURNAL_CANDIDATE`:

- не является task authority;
- не является delivery, receipt, acknowledgement или acceptance;
- не является public/release approval;
- не является обязательным критерием завершения исходной задачи;
- не означает автоматическое включение материала в литературный журнал.

KOO при fresh reconciliation замечает новые положительные signals и **не создаёт отдельную RED-задачу на каждый signal**. Обычно KOO объединяет 1–3 содержательных кандидата в один bounded `RED journal-sweep` step. Один кандидат может быть передан отдельно, если есть проверяемый риск потерять существенный человеческий контекст при ожидании batch.

RED получает exact evidence кандидатов, проверяет его и остаётся единственным редакторским фильтром журнала: может включить, объединить, отложить или отклонить candidate как routine/duplicate/неподходящий материал.

Если для RED sweep требуется другой Entity-chat и exact automatic activation отсутствует, KOO использует действующий manual activation handoff. Signal сам по себе не доказывает активацию RED и не разрешает automatic chat resume.

Из этой нормы запрещено выводить:

- journal entry после каждого task;
- обязательное `JOURNAL_CANDIDATE: no`;
- отдельный journal/feed artifact на routine result;
- cron, scheduler или другую automation;
- automatic journal inclusion;
- второй technical log;
- full transcript ingestion;
- обязанность ОПЕРАТОРА быть ручным литературным диспетчером.

Отсутствие signal означает только отсутствие явной отметки в этом terminal result. Оно не запрещает RED позднее обнаружить значимое событие своим bounded editorial delta-review.

## 11. Failure modes

### PROMPT/file-form недоступен

KOO повторно материализует актуальный PROMPT после fresh reconciliation. Referenced artifacts не копируются заново, если их exact locator остаётся доступен.

### Файл попал не в тот чат

Не выполнять. ОПЕРАТОР переносит тот же проверенный файл в правильный адресный чат либо KOO создаёт новый, если состояние успело измениться.

### PROMPT устарел до исполнения

Адресная Сущность после Resume-First возвращает `STALE_OR_SUPERSEDED` с точным новым evidence. Старый шаг не исполняется.

### GitHub activation detector увидел файл, но чат не запущен

Фиксируется только технический факт detector/activation failure. Нельзя объявлять Entity execution или delivery PROMPT-а в чат без фактического подтверждения.

### Обнаружены два конкурирующих PROMPT одной задачи

Исполнение останавливается до fresh reconciliation КООРДИНАТОРОМ.

## 12. Recovery и смена КООРДИНАТОРА

Recovery сохраняет **состояние конвейера**, а не обязанность повторно исполнить старые PROMPT-файлы.

При восстановлении KOO должны быть известны:

- текущая очередь;
- какие задачи completed/blocked/current/superseded;
- какой последний terminal result подтверждён;
- какие PROMPT были подготовлены или переданы, но не имеют terminal result;
- какие activation failures известны.

После Writer Gate replacement KOO выполняет fresh reconciliation и только затем создаёт **новый актуальный PROMPT**, если задача действительно остаётся current.

`historical prompt != current execution authority`.

Автоматическое воспроизведение исторических задач запрещено.

## 13. Проверка качества PROMPT перед выдачей

Перед передачей PROMPT ОПЕРАТОРУ KOO проверяет:

- адресат правильный;
- для file-form: имя начинается с кода адресата;
- для file-form: длина полного имени 40–50 символов;
- для file-form: тема читается из имени;
- materialized PROMPT действительно доступен;
- внутри есть Resume-First;
- exact task/input однозначны;
- authority не расширена молча;
- stop conditions заданы;
- terminal result определён;
- способ возврата результата определён;
- нет секретов;
- нет автоматического replay исторических задач;
- нет второго активного PROMPT той же задачи без причины.

Если хотя бы один обязательный пункт не проходит, файл не передаётся ОПЕРАТОРУ.

## 14. Нормативный шаблон PROMPT

    # <ENTITY> — <тема>

    Продолжай выполнение текущих задач по Resume-First.

    Сначала сделай свежий preflight <источник истины>.

    Current authority / writer:
    <exact identity>

    Exact task:
    <exact identity>

    Exact task authority:
    <approved process / standing delegation / exact authorized decision or instruction>

    Required inputs:
    <минимальный набор>

    Выполни:
    <одно конкретное действие или bounded sequence>

    Ограничения:
    <authority / safety / attempts / forbidden actions>

    Stop conditions:
    <точные условия остановки>

    Expected terminal result:
    <PASS/FAIL/BLOCKER/file>

    Верни результат:
    <адресат и маршрут>

    После terminal result остановись.

Этот шаблон является формой, а не поводом копировать ненужные поля в каждую задачу. Поле включается, если оно помогает однозначно и безопасно исполнить текущий шаг.

## 15. Разделение канонов

- **project core** задаёт общую модель работы и authority;
- **entity roles** задаёт устойчивые роли;
- **file-work canon** регулирует создание, проверку, упаковку и доставку артефактов;
- **task-conveyor canon** регулирует передачу управления между Entity-чатами через PROMPT-файлы;
- **source-loading policy** определяет, какие источники загружать;
- **recovery canon** регулирует сохранение и восстановление состояния и current-writer.

Ни один из этих документов не должен повторять полный алгоритм другого.

---

## Служебная карточка

document_type: task-conveyor-canon
version: v1.2
status: approved
scope: inter-chat/PROMPT activation conveyor; mandatory for KOO and participating PROMPT/chat instances
source: task-conveyor-canon-v1_1-approved.md
supersedes_after_activation_barrier_pass: task-conveyor-canon-v1_1-approved.md
changed_sections: literary-journal candidate feed; служебная карточка
approval_status: operator_approved
effectivity_rule: active_only_after_complete_source_set_activation_barrier_pass
responsibility_boundary: optional positive JOURNAL_CANDIDATE signal + KOO batching + RED editorial filter; no per-task reporting, no automation, no automatic journal inclusion; preserves manual activation handoff and does not replace file-work or recovery canon

approval_decision: `APPROVE_TASK_CONVEYOR_CANON_V1_2_JOURNAL_FEED`; KOO decision gate `entities/koordinator/outbox/KOO__task-conveyor-v1_2-gate__OPERATOR.md@3281974e97d57c87d50e06b5dcbefe9f6c4ef01e`
change_basis: `entities/kancelar/outbox/KAN__task-conveyor-v1_2-journal-feed-delta-candidate__KOO.md@6f27acf12c9a2dc112f2a16c7a84dcc10b5654e2`; normative review `entities/kancelar/outbox/KAN__literary-journal-feed-norm-review-r01__KOO.md@f4b8725d3dda4c8145cb80641b539d0992e760d4`
