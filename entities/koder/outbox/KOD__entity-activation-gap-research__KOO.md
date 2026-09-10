# KOD → KOO
## Исследование: автоматическая активация Сущности после адресной доставки

## Результат

Текущий дефект подтверждается: GitHub Exchange Gate обеспечивает публикацию, адресный dispatch, inbox locator, registry и receipt, но сам по себе не запускает существующий ChatGPT-чат получателя.

Минимально корректная архитектура должна разделять два уровня:
1. event detector — фиксирует появление нового адресного задания;
2. activation adapter — пытается запустить обработчик Сущности и обязан явно зафиксировать `activation_failed`, если конкретный ChatGPT-чат нельзя запустить доступным API/продуктовым механизмом.

`delivered/dispatched` нельзя смешивать с `activation_started`, `activation_failed` и `processing_started`.

## Реально доступные механизмы

### GitHub event

GitHub Actions поддерживает событийные workflow. Для маршрутизации подходят `push` с path-filter, `repository_dispatch` и внешний webhook.

Что умеет: быстро обнаружить новый locator и запустить проверяемый workflow/worker.

Чего сам не умеет: подтверждённо запускать конкретный существующий ChatGPT conversation.

### OSS event

ОСС может в будущем быть источником `inbox.item.created` или `route.delivered`, но production/core менять этой задачей запрещено. Сейчас это future adapter source, а не готовый trigger.

### ChatGPT automation

Актуальная документация OpenAI подтверждает:
- Scheduled/monitoring tasks могут выполнять повторяющиеся проверки;
- paid plans могут выполнять повторяющиеся задачи до одного раза в час;
- event-triggered tasks в режиме Work могут реагировать на поддерживаемые события Gmail, Slack и GitHub;
- для этого нужен подключённый app/account и разрешения.

Это первый нативный механизм, способный убрать polling и ручной пинок.

Критическая граница: документация не подтверждает, что event-triggered task может возобновить именно уже существующий конкретный Entity-chat. Поэтому это автоматический запуск обработчика, но пока не доказанное «пробуждение старого чата».

### External worker

Внешний worker может:
1. получать GitHub webhook;
2. проверять Exchange Gate locator/version;
3. определять recipient;
4. запускать разрешённый LLM/agent endpoint;
5. передавать минимальный recovery/current context;
6. публиковать результат и receipt;
7. при невозможности запуска создавать `activation_failed`.

Это наиболее контролируемый вариант, но без официального resume API он создаёт/запускает agent instance, а не обязательно продолжает тот же UI-chat.

### Manual-only

Ручной пинок ОПЕРАТОРА остаётся fallback, но не является решением сверхзадачи.

## Сравнение

| Механизм | Event-driven | Может читать GitHub | Без ОПЕРАТОРА | Доказано resume exact Entity-chat | Новый runtime |
|---|---:|---:|---:|---:|---:|
| GitHub Actions | да | да | да | нет | нет/минимально |
| ChatGPT Scheduled Task | polling | при app access | да | нет | нет |
| ChatGPT event-triggered Work task | да | да | да | не подтверждено | нет |
| External worker | да | да | да | нет без resume API | да |
| OSS event | потенциально | не обязательно | потенциально | нет | нужен adapter |
| Manual | нет | да | нет | пользователь открывает чат | нет |

## Минимальный прототип

### Вариант A — первый эксперимент

`GitHub inbox event → ChatGPT event-triggered Work task → Exchange Gate processing`

Триггер:
- изменение `entities/<entity>/inbox/**`;
- recipient = конкретная Сущность;
- ignore `.gitkeep` и уже обработанные immutable identities.

Действие:
1. прочитать locator;
2. проверить immutable commit/blob/SHA;
3. проверить sender/recipient и Exchange Gate;
4. прочитать адресный artifact;
5. выполнить только разрешённое действие;
6. записать result в outbox;
7. создать dispatch/registry;
8. если запуск/доступ невозможен — создать `activation_failed`, а не уведомление ОПЕРАТОРУ.

### Проверяемый E2E test

Создать тестовый locator:
`entities/koder/inbox/KOO__activation-e2e-test__KOD.md`

Ожидаемая цепочка:
`GitHub event → activation_started → read exact locator/version → processing_started → result artifact → dispatch`.

Если платформа не позволяет exact Entity-chat resume:
`GitHub event → activation_failed: exact_entity_chat_resume_not_supported`.

Это корректный failure result.

## Вариант B — внешний activation worker

Если Work task нельзя устойчиво использовать как конкретную Entity:

`GitHub webhook → activation-worker → Entity runner`

Минимальный state machine:
`detected → validated → activation_requested → (processing_started | activation_failed) → (result_dispatched | processing_failed)`

Обязательные invariants:
- один immutable inbox item не обрабатывается повторно без explicit retry;
- delivery != activation;
- activation != acceptance;
- authority не расширяется;
- secrets не попадают в repo/prompt/log;
- unknown recovery/current-writer state блокирует запуск;
- новый instance не притворяется старым current-writer.

## Почему не GitHub Actions → «вызвать чат»

GitHub Actions хорошо решает detection/orchestration, но подтверждённого публичного API, который принимает `conversation_id` пользовательского ChatGPT и гарантированно продолжает тот же UI-chat как Entity, в изученных источниках не найдено.

Поэтому `push → curl ChatGPT conversation` нельзя считать рабочей технологией без отдельного подтверждения.

## Автопубликации

Для Telegram/сайта/соцсетей применим тот же паттерн:

`content artifact → validation → publish adapter → platform API → receipt → immutable publication record`

Токены платформ не следует раздавать редакционным Сущностям. Лучше отдельные adapters с минимальными scopes и idempotency key.

Это отдельный workstream и не должно смешиваться с activation prototype.

## Рекомендация KOD

Первым экспериментом использовать native ChatGPT event-triggered Work task на GitHub event.

Критерий успеха:
после появления тестового inbox locator без действия ОПЕРАТОРА появляется проверяемый `activation_started` и затем result, либо проверяемый `activation_failed`.

Если exact existing Entity-chat resume не поддерживается, зафиксировать product boundary и перейти к External Worker + recovery-based Entity runner.

## Источники

- OpenAI Help Center, Scheduled Tasks in ChatGPT:
  https://help.openai.com/en/articles/10291617-tasks-in-chatgpt
- OpenAI Help Center, Apps in ChatGPT:
  https://help.openai.com/en/articles/11487775-apps-in-chatgpt
- GitHub Docs, Events that trigger workflows:
  https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

## Границы результата

- production/core OSS: не изменялись;
- authority/writer grants: не расширялись;
- secrets: не использовались;
- реальный ChatGPT event-triggered task: не создавался;
- exact existing Entity-chat resume: не подтверждено;
- notification to OPERATOR не считается activation.

from_entity: KOD
to_entity: KOO
document_type: entity-activation-gap-research
status: candidate_for_review
project_time: generated_without_trusted_project_time
