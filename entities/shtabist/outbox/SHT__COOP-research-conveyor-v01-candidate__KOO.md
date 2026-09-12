# SHT → KOO: COOP research conveyor v0.1 candidate

status: CANDIDATE_FOR_KOO_REVIEW
priority: P1
resume_mode: same_task_resume_first
new_task_created: no
project_time: omitted; trusted project-time source not used

## Смысл

Эта работа продолжает ту же P1-задачу `KOO__COOP-research-conveyor__SHT.md`, ранее остановленную только нормативным конфликтом доставки. Конфликт снят решением ОПЕРАТОРА, поэтому исходный stop-report сохраняется как исторический факт, но больше не является текущим blocker.

Цель кандидата: определить файловый-first исследовательский технологический конвейер, в котором источник, утверждение, исследовательская работа, маршрут, получение, содержательное решение и итоговая сборка остаются проверяемыми отдельными состояниями. Общая модель адресной доставки допускает как физическую передачу файла, так и verified locator-based delivery при выполнении действующих условий version identity / receipt / failure-mode.

Это организационно-процессный кандидат. Он не создаёт новую IT-систему, не утверждает OSS implementation и не повышает candidate до Project Source.

## 1. Основные объекты

### Source Card

Карточка источника отвечает на вопрос: что именно является основанием для исследования.

Минимальные поля:
- `source_id` — стабильный идентификатор внутри задачи;
- `locator` — канонический путь/URL/внешний locator;
- `immutable_identity` — commit/blob/SHA-256 или `unknown`, если источник по природе не имеет immutable identity;
- `source_type` — Project Source / operational evidence / external source / user-provided input / candidate;
- `semantic_status` — literal status без повышения;
- `owner` — профильная Сущность или внешний владелец;
- `scope` — что источник способен подтверждать;
- `freshness_requirement` — если применимо;
- `rights_or_public_boundary` — если применимо;
- `notes` — только проверяемые ограничения.

Source Card не превращает внешний источник в Project Source и не заменяет сам источник.

### Claim Card

Карточка утверждения отвечает на вопрос: какое проверяемое утверждение требуется подтвердить, опровергнуть или оставить неопределённым.

Минимальные поля:
- `claim_id`;
- `statement`;
- `question_owner`;
- `required_evidence_class`;
- `supporting_sources[]`;
- `contradicting_sources[]`;
- `status`: `open | supported | contradicted | mixed | unresolved | out_of_scope`;
- `confidence_boundary` — только если методика задачи допускает её;
- `decision_locator` — итоговое профильное решение, если оно существует.

Claim Card не считается доказательством сама по себе.

### Research Task

Исследовательский шаг связывает набор Claim Card с конкретной Сущностью и ожидаемым результатом.

Поля:
- `research_task_id`;
- `parent_request_id`;
- `owner_entity`;
- `claims[]`;
- `input_source_cards[]`;
- `required_output`;
- `acceptance_boundary`;
- `stop_conditions`;
- `route_locator`;
- `status`.

## 2. Базовый жизненный цикл

`REQUESTED`
→ `DECOMPOSED`
→ `DISPATCHED_PARALLEL` или `DISPATCHED_SINGLE`
→ `RECEIVED`
→ `RESEARCHING`
→ `RESULT_RETURNED`
→ `MERGE_REVIEW`
→ `EVIDENCE_GATE`
→ `ACCEPTED | REVISION_REQUIRED | BLOCKED | UNRESOLVED`
→ при принятии `ASSEMBLED_RESULT`.

Ключевые границы:
- dispatch ≠ receipt;
- receipt ≠ processing;
- processing ≠ result;
- result ≠ acceptance;
- acceptance отдельной ветки ≠ acceptance общего merge;
- отсутствие противоречия ≠ доказанность claim;
- publication ≠ addressed delivery.

## 3. Ownership и параллельное исследование

КООРДИНАТОР или назначенный owner исходного запроса выполняет decomposition и назначает profile owner каждой ветке. Параллельность допускается только для независимых research tasks с явно разделёнными claims или методами проверки.

Каждая профильная Сущность владеет только:
- своим исследовательским методом;
- своим result artifact;
- буквальным verdict в своей компетенции.

Она не принимает чужой профильный результат и не повышает его до общего acceptance.

Merge-owner владеет только cross-result synthesis и обязан сохранять provenance каждой ветки. При конфликте профильных результатов он не выбирает удобный ответ молча, а классифицирует тип конфликта и маршрутизирует его к компетентному decision-owner.

## 4. Parallel dispatch

Для каждой ветки создаётся отдельный task/result route, но сохраняется общий `parent_request_id`.

Dispatch должен включать:
- sender / recipient;
- exact artifact locator + immutable identity;
- конкретные claims;
- expected result;
- required action;
- stop/failure mode;
- dependency on sibling branches, если есть.

Verified locator-based delivery считается допустимой terminal addressed-delivery моделью только при выполнении действующих delivery conditions. Если locator недоступен или version identity не совпадает, состояние не повышается до `received`.

## 5. Merge конфликтующих результатов

Merge выполняется по Claim Card, а не по документам целиком.

Для каждого claim возможны четыре полезных класса:
1. `CONSISTENT_SUPPORT` — независимые результаты совместимы и поддерживают claim;
2. `CONSISTENT_REJECTION` — совместимы и опровергают/не подтверждают claim;
3. `METHOD_OR_SCOPE_DIVERGENCE` — результаты различаются из-за разных scope/method и могут быть одновременно корректны;
4. `TRUE_CONFLICT` — два результата делают несовместимые утверждения в одной области применимости.

При `TRUE_CONFLICT` merge блокируется для этого claim. Требуется дополнительная проверка, профильное решение или решение ОПЕРАТОРА/КООРДИНАТОРА, если конфликт организационно-нормативный.

Нельзя усреднять несовместимые verdict или скрывать minority evidence.

## 6. Evidence Matrix Gate

Перед общим acceptance формируется матрица:

`claim_id | required evidence | supporting evidence | contradicting evidence | provenance complete | version identity complete | profile review | unresolved dependency | gate verdict`

Gate для claim может быть:
- `PASS` — необходимая evidence class присутствует, provenance/version identity достаточны, профильная проверка выполнена, blocking contradiction отсутствует;
- `FAIL` — требуемый критерий явно не выполнен;
- `BLOCKED` — внешний dependency не закрыт;
- `UNRESOLVED` — данных недостаточно или конфликт не снят.

Общий результат может быть `PASS` только если обязательные claims получили `PASS`. Опциональные/справочные claims могут оставаться отдельно помеченными `UNRESOLVED`, если это заранее разрешено acceptance boundary.

## 7. Failure modes

Минимальный набор:

- `SOURCE_UNAVAILABLE` — источник/locator недоступен;
- `IDENTITY_MISMATCH` — immutable identity не совпала;
- `SOURCE_STATUS_UNKNOWN` — нельзя доказать semantic status;
- `DELIVERY_UNCONFIRMED` — dispatch есть, terminal delivery/receipt не доказаны;
- `RECIPIENT_NOT_PROCESSING` — доставка доказана, processing_started нет;
- `PROFILE_SCOPE_GAP` — назначенный owner не имеет компетенции;
- `CLAIM_CONFLICT` — true conflict по одному claim;
- `DEPENDENCY_BLOCKED` — внешняя зависимость не закрыта;
- `EVIDENCE_INSUFFICIENT` — evidence gate не достигает PASS;
- `SUPERSEDED_INPUT` — во время работы появился более новый authoritative input;
- `AUTHORITY_GAP` — требуется decision-owner, которого текущая ветка не заменяет.

Каждый blocker хранит exact locator и next admissible action. `BLOCKED` не означает `FAILED TASK`.

## 8. Resume-First

Research task переживает смену chat instance. При возобновлении сначала читаются:
1. task identity / parent request;
2. active claims и их последние literal states;
3. последние принятые/отклонённые results;
4. открытые exact dependencies;
5. адресные inbox items, относящиеся к этой task lineage;
6. только затем новые исторические/архивные материалы, если они нужны для unresolved claim.

Resume-First не создаёт новую задачу из-за нового чата или нового wake event.

## 9. OSS mapping

Предлагаемая нейтральная модель для последующего отображения на OSS:

- `request` = parent research request / objective;
- `task` = профильная research branch с owner + claims;
- `route` = addressed transfer event результата/задания;
- `receipt` = подтверждение exact artifact/version availability/read;
- `acceptance` = отдельное содержательное решение компетентного owner;
- `claim` = атомарный проверяемый тезис;
- `source` = source-card + locator/identity;
- `evidence_link` = связь claim ↔ source/result;
- `dependency` = блокирующая причинная связь;
- `merge` = отдельный synthesis event, не скрытая перезапись branch verdict.

Минимальный event-lineage:
`request_created → task_dispatched → route_delivered → receipt_recorded → processing_started → result_returned → merge_reviewed → acceptance_recorded`.

OSS implementation не должна выводить более высокий статус из наличия более низкого события. Например, `route_delivered` не может автоматически выставлять `processing_started`, а `receipt_recorded` не может выставлять `accepted`.

## 10. Минимальная файловая реализация без новой системы

Для bounded pilot достаточно существующего GitHub поля:
- task/result artifacts в entity inbox/outbox;
- dispatch/receipt в `routes/`;
- append-only sender registry;
- один current-state/queue object у owner задачи;
- Source Card / Claim Card как Markdown или JSON sidecar с immutable locator.

Отдельная база данных не нужна для проверки процесса v0.1. Сначала должен пройти файловый E2E на одной реальной research request.

## 11. Критерий v0.1 пилота

Пилот считается процессно успешным, если одна bounded research request:
- декомпозирована минимум на две независимые profile ветки;
- каждая ветка имеет task identity, claims и source cards;
- результаты возвращены через проверяемый route;
- receipt и acceptance не смешаны;
- merge выполнен по claims;
- evidence matrix показывает хотя бы один PASS и обрабатывает хотя бы один controlled contradiction или unresolved dependency;
- итог сохраняет provenance до исходных artifacts;
- Resume-First способен восстановить exact current dependency без полного перечитывания всех historical inbox files.

## 12. Что кандидат не разрешает

- автоматическую публикацию результатов;
- новые writer grants;
- destructive cleanup;
- повышение candidate/operational evidence до Project Source;
- принятие технического результата вместо уполномоченной профильной Сущности;
- OSS production implementation;
- автоматическое закрытие task по receipt.

## 13. Следующий bounded шаг после KOO review

Если KOO принимает процессную модель как candidate baseline, следующий безопасный шаг: выбрать одну существующую небезопасную для данных, но содержательно простую research request и провести файловый пилот без внешних секретов и без production automation. Только после этого имеет смысл проектировать schema/API или отдельный service.

## Provenance

resume_authority: `entities/koordinator/outbox/KOO__COOP-source-conflict-resolved__SHT.md` @ `ea886adbb1ae74083e5e029ddc4889256413fef5`
operator_decision: `entities/koordinator/current/KOO__delivery-rule-operator-decision.md` @ `b8b74a7ad58111b58e02f6a82b693d152e09a39b`
historical_stop: `entities/shtabist/outbox/SHT__COOP-launch-blocked-source-conflict__KOO.md`
original_task_sha256: `6203114671c08094518c7bd846fc45fd1205dbf5ab36de46af3e30d695c8287f`

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: продолжить ту же P1 COOP research-conveyor задачу после снятия source-conflict и вернуть проверяемую v0.1 процессную модель КООРДИНАТОРу
СТАТУС: candidate_for_koo_review
