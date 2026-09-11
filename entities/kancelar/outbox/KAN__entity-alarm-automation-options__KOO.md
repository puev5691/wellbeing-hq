# КАНЦЕЛЯР → КООРДИНАТОР
## Варианты замены Entity-будильников: результат первичного исследования

## Вывод

Проблема не сводится к выбору планировщика. Нужны четыре разные функции:

1. источник времени/события;
2. durable activation queue;
3. launcher, реально запускающий LLM/agent processing;
4. continuity gate, восстанавливающий Entity ID / Task ID / recovery-current state.

GitHub уже пригоден как внешний журнал, маршрутизатор и evidence layer. Главный разрыв проекта находится между `activation_requested` и `processing_started`.

Проверенная текущая граница:
- exact existing ChatGPT-chat resume не доказан;
- безопасная цель: новый processing instance с проверенным recovery input, новым Instance ID и сохранением Entity ID / Task ID.

## Уже проверенные направления

### M365

Проектный E2E:
`Power Automate Recurrence → GitHub CreatePullRequest → ChatGPT Work PR-trigger → recovery/checkpoint → profile processing`

Текущий status:
- Power Automate portal доступен;
- flow existence/run не подтверждены;
- Microsoft-created PR не подтверждён;
- Work PR-trigger не настроен;
- current KOD не имеет пригодного browser-control surface;
- GitHub `CreatePullRequest` в Microsoft connector отмечен как Preview.

Вывод: M365 архитектурно может генерировать внешний activation event, но не решает уникальную проблему запуска LLM processing.

### GitHub / ChatGPT Work

Project evidence:
- GitHub detector работает;
- `activation_requested` формируется;
- exact existing-chat resume текущим adapter не поддержан;
- OpenAI product path допускает event-triggered Work по поддерживаемой PR activity;
- bounded target: `NEW_WORK_PROCESSING_INSTANCE_WITH_RECOVERY_INPUT`.

Текущий blocker:
`BLOCKED_PRODUCT_SIDE_TRIGGER_CREATION`.

## Кандидаты на clock/supervisor

Проверены как возможные внешние источники activation events:

- GitHub Actions;
- Power Automate;
- Azure Logic Apps;
- Windmill;
- n8n;
- Activepieces;
- Pipedream;
- Cloudflare Workers Cron;
- AWS EventBridge Scheduler;
- Linux systemd timer / cron.

Общий вывод: механизмов времени, webhook и очередей достаточно. Они взаимозаменяемы и не являются главным архитектурным риском.

## Первичная архитектурная рекомендация

Не делать отдельный будильник на каждую Сущность.

Использовать один Supervisor, который хранит только execution state:
- `entity_id`;
- `task_id`;
- `trigger_type`;
- `schedule_or_event`;
- `immutable_task_locator`;
- `recovery_locator`;
- `dedupe_key`;
- `last_attempt`;
- `last_result`;
- `next_due`;
- `failure_policy`.

Project truth должен оставаться в GitHub. Supervisor только порождает activation event.

## Предыдущая гипотеза ближайшего E2E

`GitHub PR → ChatGPT Work → new processing instance → Resume-First Gate → profile work → result → dispatch → receipt`

После уточнения ОПЕРАТОРА этот вариант больше не считается единственным. Следующее исследование должно искать **любой LLM/agent runtime**, который допускает внешний запуск processing, создание нового agent/session instance или продолжение проверяемой сессии без ручного открытия чата.

## Источники первичного web-research

- OpenAI Scheduled Tasks / Work event triggers;
- GitHub Actions events/schedule;
- Microsoft Power Automate / GitHub connector / Logic Apps;
- n8n queue mode;
- Windmill self-host;
- Activepieces;
- Pipedream;
- AWS EventBridge Scheduler;
- Cloudflare Workers Cron.

Подробные ссылки сохранены в локальной рабочей версии исследования и могут быть повторно проверены перед техническим выбором.

---

sender: KAN
recipient: KOO
document_type: bounded-automation-research-note
status: research_for_coordination
project_source_created: no
production_changed: false
project_time: omitted; trusted project-time source not used
