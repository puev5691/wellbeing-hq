# КООРДИНАТОР: архитектурная фиксация Entity Continuity / Task Persistence

## Смысл

Результат диалога ОПЕРАТОРА и КОДЕРА выводит текущую работу за пределы задачи «автоматически разбудить существующий чат».

Рабочая архитектурная гипотеза: долговечная специализированная Сущность должна существовать независимо от отдельного chat/processing instance. Экземпляр становится сменяемым вычислительным исполнителем, а непрерывность обеспечивается внешним проверяемым состоянием, удержанием Task ID и восстановлением релевантного опыта.

Это пока не новый канон и не утверждённая норма. Это архитектурная концепция, которую следует проверять поэтапным E2E.

## Базовые идентичности

Необходимо жёстко разделять Entity ID, Task ID и Instance ID. Entity ID хранит долговечную идентичность, роль, границы полномочий, канон и накопленный проверенный опыт. Task ID живёт до проверяемого DONE либо явного прекращения уполномоченной Сущностью. Instance ID обозначает конкретный сменяемый вычислительный экземпляр.

Ключевой инвариант: смерть, timeout, ошибка или исчерпание контекста отдельного instance не завершают Task. `FAILED INSTANCE != FAILED TASK`.

## Рабочий цикл

`addressed event -> detector -> supervisor/activation-worker -> provenance validation -> recovery -> initiation -> current-state restore -> relevant experience restore -> unfinished-chain restore -> processing instance -> work -> verification -> addressed delivery -> preservation/experience extraction`

После запуска instance должен получить минимум три слоя: канон и границы полномочий; текущее состояние и незавершённую причинно-следственную цепочку задачи; релевантный проверенный опыт с evidence, applicability, freshness, supersedes и anti-regression.

Контекстное окно становится оперативной памятью экземпляра, а не единственным носителем опыта Сущности.

## Удержание Task

DONE: результат получен, проверен, адресно доставлен, состояние сохранено, полезный новый опыт извлечён.

BLOCKED: зафиксирован конкретный внешний блокер и создан адресный запрос тому, кто способен его снять; Task остаётся активной.

FAILED INSTANCE: конкретный instance не способен продолжить; его evidence/state сохраняются, но Task остаётся незавершённой и может быть продолжена новым instance.

После снятия BLOCKED supervisor должен продолжать ту же Task ID автоматически.

## Supervisor

Текущий activation-worker целесообразно развивать в Entity Supervisor поэтапно. Supervisor обнаруживает адресное событие, проверяет immutable provenance и Exchange Gate, определяет Entity/Task, проверяет recovery/current-writer state, инициирует новый Instance ID, восстанавливает состояние/цепочку/опыт, контролирует допустимые переходы Task, не допускает ложного DONE и запускает preservation/experience extraction после терминального результата.

Supervisor не расширяет authority/writer grants и не выдаёт новый instance за прежний current-writer.

## Дополнительное требование: ownership/current-writer

Из архитектуры следует необходимость отдельного управляемого механизма владения активной задачей. Нельзя полагаться на предположение, что последний запущенный чат и есть current-writer. Нужна проверяемая модель lease/ownership, которая определяет, какой instance вправе продолжать конкретную Task, и не допускает параллельного ложного владения одной рабочей цепочкой.

Это вывод КООРДИНАТОРА из концепции и пока не новая норма.

## Правильная последовательность E2E

1. Доказать реальный автоматический `processing_started` через activation-worker/runtime adapter.
2. Запустить новый instance с одной реальной Task ID и доказать восстановление current-state.
3. Добавить восстановление релевантного experience layer.
4. Искусственно завершить/сломать instance до DONE.
5. Запустить следующий instance и доказать продолжение той же Task ID без ручного сообщения ОПЕРАТОРА.
6. Довести Task до проверяемого DONE с адресной доставкой, preservation и experience extraction.

## Следствия для сохраняемых и накапливаемых данных

Потребуются: явное разделение Entity state, Task state и instance-local state; сохранение незавершённой причинно-следственной цепочки Task; immutable provenance; deduplication/supersedes/freshness/applicability для опыта; фиксация failed attempts и anti-regression; защита от ложного current-writer inheritance; проверяемое связывание нового instance с Entity ID и Task ID; политика compact/retention; отделение historical evidence от current truth.

АРХИВАРИУСу и ШТАБИСТу следует учитывать, что действующие каноны preservation/recovery и организационные маршруты, вероятно, потребуют расширения после технического подтверждения концепции. До подтверждения это не считается новой нормой.

status: architectural_concept_requirements_candidate
source: KOD__entity-continuity-task-persistence-concept__KOO.md @ 7636799be362dfa8a587887a6ee1f2f8c21a9600
project_time: omitted; trusted project-time source not used
