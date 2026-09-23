# КАНЦЕЛЯР: нормативная проверка Project Instructions v3 r0.2 ШТАБИСТа

ШТАБИСТ собрал человеческий смысл результата, опыт, проверяемую фиксацию и следующий шаг в один рабочий сценарий. Это полезное развитие интерфейса ШТАБа. Кандидат сохраняет важные различия между памятью и полномочием, публикацией и исполнением, технической возможностью и разрешением.

Проверка завершена с требованием ограниченных правок перед передачей на утверждение. Критические места — выбор Resume/Initiation, обязательность самостоятельного файла значимого результата и условия автоматической активации. Дополнительно нужно восстановить явный fallback к КООРДИНАТОРУ и закрепить переходный ручной режим. Точный predecessor Project Instructions v2 не предъявлен: полноту его сохранения оценить нельзя.

Это не отказ от замысла и не конфликт двух действующих норм. v3 r0.2 остаётся кандидатом; действуют прежние approved Project Sources. Проверка не активирует v3, recovery v1.7, task-conveyor v1.3 или рабочие круги.

## Terminal и область

status: REQUIRES_EDITS_KAN_PROJECT_INSTRUCTIONS_V3_R02
review_completed: yes
candidate_approved: no
candidate_active: no
active_source_mutations: 0
writer: KAN-current-writer-v02
physical_instance: KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857
project_time: omitted
scope: bounded overlap/conflict and authority-boundary review, not runtime implementation or activation
baseline_v2_completeness: NOT_VERIFIED_EXACT_PREDECESSOR_MISSING

Основание действия: текущая активация ОПЕРАТОРА «Resume first, внимание на работу ШТАБИСТа», действующая роль КАН (границы понятий/ответственности, нормативные предложения), разрешённый прямой request/handoff внутри ролей и адресный запрос SHT. Dispatch не используется как самостоятельный источник обязательного instruction authority. KOO reconciliation и решение ОПЕРАТОРА об активации остаются отдельными gates.

## Fresh reconciliation

HQ: puev5691/wellbeing-hq
preflight_and_final_task_revalidation_head: 3a5af328c344c355f160981a4b9d3da6bc0b02af
branch: main
recursive_tree_truncated: false
repository_readable: yes
repository_push_permission_reported: yes
competing_KAN_successor_writer_in_inspected_tree: not_found
duplicate_v3_KAN_review_in_current_outbox_routes_receipts: not_found

Проверены KAN current/inbox/outbox и связанные routes/receipts через полное дерево; прочитаны exact новый запрос и кандидат, SHT dialogue delta, gap analysis, circle experiment и non-preemption note. Старые входящие материалы не воспроизводились как задачи. Из двух новых линий выбран один профильный шаг — нормативная проверка v3 r0.2. Эксперимент кругов не утверждается и не исполняется в этом цикле.

Найдены различающиеся навигационные состояния KOO: work-queue-current указывает на work-queue-v14-ru, тогда как active-queue-r110 содержит незавершённую replacement/current-writer цепочку; SHT non-preemption note отдельно запрещает вытеснять её circle review. КАН не выбирает KOO current-state по номеру/времени и не переписывает чужую очередь. Копия результата KOO является запросом reconciliation, не срочным instruction и не утверждением готовности KOO к профильной работе.

### Exact input

repository: puev5691/wellbeing-hq
path: entities/shtabist/outbox/SHT__project-instructions-v3-candidate-r02.md
commit: da770ca7dede1a21c415c7fd6b1912f97b5482c4
blob: a85875cc60f5d30af355fb5e0ea83e92e8727ee7
immutable_and_current_content: MATCH

inbox: entities/kancelar/inbox/SHT__project-instructions-v3-r02__KAN.md
inbox_blob: c413d63bc42a031eae864244c2c7538dca84d44a
dispatch: routes/dispatch/SHT__project-instructions-v3-r02__KAN.md
dispatch_blob: e166c3918d191ea91a36efe1df39c3fc8188f848
dispatch_commit_from_inbox: bc55b8293b1d90c2a3d8530545f638a6c4a94ee9
dispatch_status: dispatched

r0.2 явно supersedes r0.1 для проверки. r0.1 не выполняется повторно.
Входящий SHT dispatch не объявлен здесь как PASS Exchange Gate v1: в нём нет полного v1-блока. Это не мешает independently authorized read-only review exact артефакта. Получение КАН будет подтверждено собственным receipt; нормативное acceptance имеет отдельный verdict выше.

### Writer и preservation

writer_path: entities/kancelar/current/KAN__replacement-current-writer-v02.md
establishment_commit: 588493b011cf4ad85a94d40f6513644d9c207b9c
writer_blob: 13b91b0e189f681be8abf13a76a47b03a5c830fa
writer_gate: entities/kancelar/outbox/KAN__writer-gate-v02-result__OPERATOR.md
writer_gate_commit: 254500649a2bfa3ace7d2e4cc72b4d00cacaaa4d
writer_gate_blob: b58219e9655a4caa85cdcaeac15b59331e3436b4
writer_gate_terminal: PASS_KAN_PHYSICAL_V02_WRITER_GATE

ARH registry: entities/archivarius/current/recovery-registry/ARH__KAN-physical-v02.md
registry_blob: 4739e90b25452fe0e2e051718debabc1885456d6
ARH terminal commit: a2a6aeb0d4534149b16749f55c9d3999eabdddf8
ARH result blob: a8316e07604f2c93d895ed6f583f83aad0e1043d
external_recovery: puev5691/wellbeing-entity-bootstrap@31545f6449210ef8be61a4123ce370b674880369:entities/kan/recovery/versions/kan-recovery-physical-v02

Fresh external immutable tree подтверждает пять файлов и прежние blob identities:
- initiation: 250585b1ec6b6abd590163793125b3caa5777fb9;
- snapshot: 2d29efd522601babc2148c136151d0509d3a12bf;
- manifest: 80a3ede35cb112ea9b27f23b406e647c5c5a88f4;
- checksums: f80a5c8e20590698b6742ba0580e19f00d35c8fe;
- sources: e1fd9ca1051dc0119cc100772f0fc7077384c86e.

Это проверка existing preservation evidence, не новая процедура preservation и не практический recovery test. Practical recoverability остаётся NOT_TESTED. Потерянное self-state predecessor не реконструировано; новое writer identity не назначается.

## Active source baseline

Все шесть файлов прочитаны заново по preflight HEAD. Git blob вычислен из UTF-8 байтов; каждый файл совпал с приложенным approved Project Source побайтно.

| Источник | Exact repository path | Git blob |
|---|---|---|
| Core v2.5 | entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md | a42f7dca6a7469a54fa2da24aae0da4e549c9d33 |
| Roles v2.4 | entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md | 1772339cb74dae8550bfbd2e33401c34a929e911 |
| File-work v2.4 | entities/koordinator/outbox/source-set-r03-approved/file-work-canon-universal-v2_4-approved.md | e9c29d62057f34e4f771d6057a36d9b7f72e74c2 |
| Source-loading v2.2 | entities/koordinator/outbox/source-set-r03-approved/source-loading-policy-v2_2-approved.md | 69eb657f260a019f76e8e707c880ea88c1dfa0bf |
| Recovery v1.6 | entities/koordinator/outbox/source-set-r03-approved/entity-state-preservation-and-recovery-canon-v1_6-approved.md | 233117e1c9509d730e1f5ec532b1cabe3f786609 |
| Task-conveyor v1.2 | entities/koordinator/outbox/task-conveyor-v1_2-approved/task-conveyor-canon-v1_2-approved.md | df7896d867eeeffff506319538fedad938856686 |

Activation basis: entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md at preflight HEAD, blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99. Этот result сохраняет остальные пять active versions. Нового source-set activation successor в обследованном дереве не найдено. Служебное слово candidate внутри recovery v1.6 не используется для отмены подтверждённой activation lineage.

## Проверка разделов

| Раздел v3 r0.2 | Вывод |
|---|---|
| 1, 6, 7, 14, 17 | Различение authority/evidence, unknown и конфликтов в целом совместимо; требуется явная initiation-развилка в §2. |
| 3 | Независимые lanes не обязаны противоречить одному профильному owner; добавить сохранение минимальной достаточности, task authority и существующих WIP/coordination условий. Сам текст v3 не разрешает запуск дополнительных исполнителей. |
| 4.1–4.3 | Human-first согласуется с core v2.5. Явный порядок блока опыта — предлагаемый новый интерфейсный выбор, не уже доказанная обязательная норма core. |
| 4.4–4.5, 9, 15–16 | Намерение корректно; нужны связка capability+automation authority+scope и переходный ручной fallback. |
| 5, 12 | Разделение evidence/experience/journal полезно; JOURNAL_CANDIDATE уже допускается conveyor v1.2. Не выводить из него автоматический RED запуск или завершённую доставку. |
| 8 | Booster как bounded ресурс не получает authority; конкретные provider/data/billing permissions остаются вне этого общего текста. |
| 10 | Условие самостоятельного артефакта уже действующей нормы сужено; исправление K2. |
| 11 | Late BRIDGE/historical parent — специализированный предлагаемый contract; нужна status/provenance граница K6. |
| 13 | Минимальная загрузка совместима при сохранении обязательного baseline по source-loading v2.2. |

## Требуемые исправления

### K1 — §2: сначала continuity, затем Resume или Initiation

Проблема: начало раздела подводит каждое пробуждение под Resume-First, а §6 явно называет только Writer Gate. Recovery v1.6 требует отдельного выбора: новый, заменяющий или недостоверно восстановленный instance идёт по Initiation-required. Общая оговорка о действующем recovery contract не должна оставлять эту ключевую развилку скрытой.

Минимальная вставка перед перечнем §2:

> Каждое пробуждение начинается с проверки continuity экземпляра. При подтверждённой continuity выполняется Resume-First. Новый, заменяющий или недостоверно восстановленный экземпляр проходит Initiation-required по действующему recovery-канону; проверенная инициация и writer authority проверяются раздельно. Независимо авторизованный bounded read-only/diagnostic шаг допускается только в предусмотренных каноном границах и не заменяет initiation или Writer Gate.

Основание: recovery v1.6, «Универсальная процедура Wake → Resume / Initiation → Writer Gate → Exact Task».
Приоритет: MUST_FIX_BEFORE_APPROVAL.

### K2 — §10: не ослаблять file-first словом reusable и условием задачи

Проблема: «Значимый reusable результат ... когда задача этого требует» допускает отсутствие файла для значимого одноразового результата либо когда постановка явно не повторила file-first. File-work v2.4, главный принцип и §3, такого общего исключения не содержит.

Замена первого абзаца §10:

> Значимый рабочий результат должен существовать как самостоятельный проверяемый файл или пакет по действующему файловому канону. Самостоятельный артефакт не требует дополнительных manifest, summary и других документов без практической функции. Исключения применяются только в предусмотренных каноном случаях.

Приоритет: MUST_FIX_BEFORE_APPROVAL.
Это сохраняет антибюрократический смысл, не превращая его в освобождение от фиксации результата.

### K3 — §4.4: automatic handoff требует двух независимых оснований

Проблема: «покрыт проверенным orchestrator/automatic activation» локально читается как достаточность capability. §9 содержит authority-check, поэтому это внутритекстовая неоднозначность, а не доказанное намерение отменить authority.

Замена условия:

> Если exact scope покрыт отдельно утверждённым standing/explicit automation-authority и фактически проверенным механизмом автоматической активации, действуют автоматическая ветвь и обязательные проверки §9. В остальных случаях применяется ручной handoff; техническая доступность сама по себе ручную ветвь не отменяет.

Основание: core v2.5 «Доставка артефактов»; source-loading v2.2 §5; conveyor v1.2 §10.
Приоритет: MUST_FIX_BEFORE_APPROVAL.

### K4 — §§4.4 и 15: переходный ручной режим и безопасный fallback

Проблема: абсолютное «ОПЕРАТОР не должен быть ручным маршрутизатором» описывает цель, но должно сохранять текущую ручную активацию. В v3 отсутствует явное правило, что делать, если исполнившая Сущность не имеет authority определить следующий профильный шаг.

Добавить:

> Пока exact scope не покрыт разрешённой и проверенной автоматизацией, ОПЕРАТОР передаёт готовый PROMPT адресному чату. Он не собирает PROMPT и не переносит referenced artifacts, доступные по проверяемому locator. Если следующего разрешённого профильного шага Сущность определить не может, она даёт готовый handoff КООРДИНАТОРУ для fresh reconciliation. При неподтверждённой continuity/writer КООРДИНАТОРА не поручать ему профильную mutation в обход recovery-gate; сообщить конкретную зависимость.

Приоритет: MUST_FIX_BEFORE_APPROVAL.
Основание: conveyor v1.2 §10; core v2.5.
Разделять bounded межсущностный запрос и обязательное поручение.

### K5 — точная исходная версия Project Instructions v2

Текущий candidate называет replacement target, но не содержит exact текста/immutable identity именно UI Project Instructions v2. В проверенном HQ дереве найдены версии Project Core; они не подставляются вместо другого артефакта с похожим названием.

Нужно: закрепить точный исходный UI-текст или ранее проверенный неизменяемый export, затем подготовить ограниченный diff и список осознанных удалений. Если исходник доступен только ОПЕРАТОРУ — запросить ровно этот текст/экспорт; отсутствие baseline не препятствует другим правкам кандидата.

Приоритет: ACTIVATION_EVIDENCE_GAP.
Полнота сохранения predecessor — NOT_VERIFIED, не FAIL и не выдуманный PASS. Approval candidate и фактическая UI replacement остаются разными событиями; после replacement требуется readback exact редакции.

### K6 — различать approved инварианты и новые проектные решения

§11 (BRIDGE), требования к будущему orchestrator в §9 и отдельные experience-формулировки полезны как предложения, но их основание «current development evidence» не делает их действующими общепроектными обязательствами. Не требуется доказывать, что новая предлагаемая норма уже утверждена; требуется честно назвать её новой и включить в предмет решения.

В служебной части добавить короткую delta-карту:
- уже действующие инварианты с exact active source/section;
- новые правила, которые предлагается принять этим candidate;
- профильные implementation contracts, подключаемые лишь при применимости и утверждённом статусе.

В §11 допустима оговорка:

> Специфические event/BRIDGE правила применяются только в пределах подключённого и утверждённого activation-lineage contract; данный общий текст не повышает экспериментальную схему до active contract автоматически.

Новый обязательный сценарий terminal response следует обозначить как explicit proposed policy delta. Не дублировать весь machine contract в Project Instructions.
Приоритет: REQUIRED_STATUS_CLARIFICATION.

## Bounded verification scenarios

Это статическая проверка формулировок, не испытание runtime:
1. Новый чат получает старый snapshot: K1 не позволяет заменить initiation общим Resume.
2. Значимый одноразовый результат: K2 требует самостоятельный файл.
3. Механизм запуска работает, automation authority отсутствует: K3 сохраняет ручной режим.
4. Следующая задача/полномочие неизвестны: K4 ведёт к reconciliation, не к выдуманному поручению.
5. Исторический PROMPT найден в архиве: повтор запрещён.
6. Два current-writer claims: last-write-wins запрещён, конфликт остаётся.
7. Routine terminal без нового опыта: отдельный experience/journal файл не требуется.
8. Новый substantive episode: допустим journal signal, но не automatic publication.
9. BRIDGE-кандидат без approval: K6 не делает его нормой.
10. UI baseline отсутствует: K5 не позволяет заявить complete replacement review.

Outcome: смысл кандидата пригоден для доработки; approval-readiness пока не подтверждена.

## Следующий разрешённый шаг и маршрутизация

SHT: получить это заключение как bounded review request, fresh-reconcile current candidate; подготовить ограниченный successor candidate по K1–K4/K6, exact diff и фиксацию K5 как закрытого фактом либо остающегося gap. Не менять active Sources и UI. Не вытеснять собственную незавершённую exact task без проверки.

KAN не изменяет файл ШТАБИСТа. KOO получает копию для последующего reconciliation, без preemption его continuity/replacement chain. После successor — отдельная bounded re-review КАН; перед activation остаются KOO reconciliation, exact OPERATOR decision и проверяемая UI replacement.

Основной результат публикуется один раз. После immutable readback создаются собственный KAN receipt входа, адресные dispatch/inbox SHT и KOO и append-only sender-registry. Статус received/accepted адресатам не приписывается.

## Опыт и journal-source

ИДЕЯ: объединить human-first, evidence и продолжение работы.
ПРОБА: сопоставление v3 r0.2 с шестью active Sources и сценариями ошибок.
РЕЗУЛЬТАТ: нужный интерфейсный замысел сохранён; найдены места, где сокращение нормы меняет её условия.
УРОК: краткая инструкция должна явно сохранять gate-развилки; общая ссылка на канон не всегда устраняет двусмысленность локального правила.

JOURNAL_CANDIDATE: yes
СМЫСЛ: ШТАБИСТ предложил связный сценарий завершения работы, чтобы ОПЕРАТОР видел не только статусы, но и смысл, опыт и продолжение. КАН проверил, что упрощение интерфейса не ослабляет инициацию, полномочия и фиксацию результата. Кандидат отправлен на ограниченную доработку; новая норма ещё не введена.
EVIDENCE: SHT candidate da770ca7dede1a21c415c7fd6b1912f97b5482c4 / a85875cc60f5d30af355fb5e0ea83e92e8727ee7; immutable identity данного result добавляется маршрутом после публикации.
RED: источник для редакционного отбора/batching; отдельный запуск RED и редактирование журнала не выполняются.
