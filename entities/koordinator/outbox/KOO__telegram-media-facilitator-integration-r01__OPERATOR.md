# КОО → ОПЕРАТОР: практическая интеграция методологического фасилитатора в Telegram-медиаконтур r0.1

status: `PROPOSAL_FOR_OPERATOR_DECISION`
entity: `KOO / КООРДИНАТОР`
production: `no`
project_time: omitted; trusted project-time source not used

## Смысл

Материал полезен для проекта не как готовое ТЗ отдельного «методологического бота», а как расширение существующего медиаконтура: Telegram-бот может стать входным шлюзом коллективного обсуждения, а отдельный фасилитационный слой — превращать разрешённый поток сообщений в проверяемое состояние обсуждения, открытые вопросы, разногласия и кандидаты задач.

Это не должно создавать второй Telegram-контур и не должно смешивать транспорт, LLM-анализ, решение группы и адресную постановку задач.

Целевая формула:

`Telegram event → privacy/validation gate → normalized discussion event → discussion-state processor → candidate insight/question/task → moderator/operator gate → dispatch → receipt`

ИИ не принимает решение вместо участников. Он классифицирует, суммирует, связывает выводы с допустимым происхождением и предлагает следующий шаг.

## Что принимаем как проектные принципы

1. Telegram остаётся заменяемым транспортом, а не местом основной логики.
2. LLM остаётся за provider-интерфейсом и не привязывает Telegram-слой к OpenAI/Anthropic/Google.
3. Сначала надёжно принимается допустимое событие, затем оно обрабатывается; отказ LLM не должен уничтожать вход.
4. Производный результат должен иметь provenance: источник → нормализованное событие → processing job → model result → решение человека → dispatch → receipt.
5. Анализ, согласие группы, право публикации и право постановки задачи — разные состояния.
6. Система должна различать хотя бы: проблему, понятия/термины, факты, цели, критерии, средства и процедуру. Семь уровней не объявляются каноном, но полезны как первая аналитическая модель.
7. Результат фасилитации должен быть машинно-проверяемым: тема, позиции, предполагаемые согласия, разногласия, открытые вопросы, следующий шаг и кандидаты задач.
8. Исторические решения не считаются подтверждёнными только потому, что модель их сформулировала.

## Критическая граница privacy

Исходное ТЗ фасилитатора предполагает долговременное сохранение исходного текста и идентификаторов. Для текущей Phase 1B это НЕ принимается автоматически.

Текущий принятый Telegram-контур использует privacy-профиль `aggregate_only`; persistent raw Telegram updates, audience identity и raw comment text не должны появляться в application/debug/retry logs или постоянном хранилище без отдельного решения.

Поэтому первый проектный вариант должен разделять:

- краткоживущий допустимый processing buffer, если он вообще нужен для анализа;
- persistent normalized/derived state без полного сырого сообщения;
- provenance locator/минимальный идентификатор, достаточный для проверки, но не копию пользовательского содержимого «на всякий случай»;
- отдельную retention/delete policy.

До изменения privacy-контракта нельзя переносить правило «сохранять исходный текст без изменения» из исходного ТЗ.

## Предлагаемый новый функциональный слой

Рабочее название: `Discussion Facilitation / Task Synthesis Layer`.

Он располагается после validation/privacy gate и normalized event, но до approval/dispatch.

Минимальные внутренние объекты:

| Объект | Назначение |
| --- | --- |
| `normalized_event` | допустимое событие без лишних Telegram-данных |
| `discussion_state` | текущая тема, проблема, позиции, вопросы, provisional agreements |
| `disagreement` | тип разногласия: facts/concepts/goals/criteria/means/procedure/other |
| `candidate_question` | вопрос группе для снятия неопределённости |
| `candidate_task` | кандидат задачи, ещё не адресная задача проекта |
| `candidate_summary` | краткая сводка обсуждения |
| `decision_record` | решение moderator/operator: approve/reject/defer |
| `dispatch_record` | адресная передача подтверждённого объекта |

Кандидат задачи должен содержать минимум: тема/проблема, основание, ожидаемый результат, кому предположительно адресовать, какие вопросы ещё не закрыты, provenance и статус `candidate_only`.

Никакой `candidate_task` не становится проектной задачей Сущности автоматически.

## Как это встраивается в существующую Phase 1B

Текущий Telegram runtime уже имеет принятый threading/runtime candidate и отдельный host contract. Последний host/runtime gate остановлен на `BLOCKED_PRIVILEGE_REQUIRED`: точные `/opt`, `/etc`, `/var/lib` и systemd boundary требуют отдельно разрешённого privilege/provisioning шага. Этот blocker не связан с фасилитацией и не должен обходиться новым пользовательским runtime.

Поэтому развитие делится на две независимые оси:

**Ось транспорта:** завершить существующий bounded Phase 1B runtime/privacy gate по уже принятому contract, не меняя paths и privacy semantics.

**Ось фасилитации:** спроектировать чистый library/domain слой без Telegram API, systemd, credentials и production storage. Его можно тестировать полностью синтетическими `normalized_event` fixtures ещё до разблокировки host runtime.

Так мы не тормозим методологическую разработку из-за sudo-блокера и одновременно не создаём конкурирующий runtime.

## Минимальная полезная версия фасилитации

Для первого этапа достаточно одного сценария:

`серия synthetic normalized_event → discussion_state → disagreement/open questions → candidate_task + candidate_question → human approval/rejection`

Без Telegram send, без live API, без автоматической постановки задачи, без persistent raw text.

Приёмка: после нескольких сообщений система должна показать, что обсуждение касается одной темы, где именно разногласие, чего не хватает для решения и какой следующий вопрос/кандидат задачи следует вынести человеку. После отказа/подтверждения состояние должно быть воспроизводимо и не выдавать machine inference за решение группы.

## Рекомендуемый порядок работ

A. Не менять принятую Phase 1B архитектуру транспорта.

B. КОО/КОДЕР формализуют `normalized_event`, `discussion_state`, `candidate_task` и `decision_record` как provider-neutral schemas.

C. RED участвует только в содержательной форме сводок, вопросов, протоколов и читаемости task candidate, но не определяет state-machine или privacy policy.

D. КОДЕР реализует чистый facilitator core и synthetic tests без Telegram/network.

E. СИСАДМИН проверяет, что новый слой не расширяет persistent privacy footprint, secret/log surface и recovery requirements.

F. После PASS domain-layer подключается к существующей Phase 1B state machine как новый processing policy, а не как новый бот.

G. Только потом вводятся реальные обсуждения в bounded sandbox и по одному разрешённому классу действий: сначала summary/question, затем candidate_task; автоматическая публикация или постановка задач остаются за отдельным решением.

## Что НЕ следует принимать сейчас

- DeepSeek как обязательного provider;
- SQLite как обязательную архитектурную БД;
- aiogram как неизменяемый transport framework;
- полный raw message archive;
- постоянное хранение Telegram user_id/username;
- весь набор slash-команд исходного ТЗ;
- семь методологических уровней как жёсткий канон;
- автоматическое признание model agreement настоящим согласием группы;
- автоматическую постановку задач Сущностям по одному model output.

## Предлагаемое решение ОПЕРАТОРА

Принять материал как `design input` для расширения медиаконтура и разрешить проектирование отдельного provider-neutral `Discussion Facilitation / Task Synthesis Layer` без изменения действующего Phase 1B runtime/privacy contract.

Первый профильный результат после такого решения: schema/specification r0.1 для `normalized_event`, `discussion_state`, `candidate_task`, human approval boundary и retention classes. Реализация — только после отдельной проверки этой схемы.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: интегрировать идеи методологического фасилитатора в существующий Telegram-медиаконтур без второго runtime и без нарушения privacy/authority boundary
СТАТУС: `PROPOSAL_FOR_OPERATOR_DECISION`
