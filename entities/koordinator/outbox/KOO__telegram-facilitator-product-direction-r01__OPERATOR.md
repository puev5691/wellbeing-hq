# КОО → ОПЕРАТОР: утверждённое направление развития Telegram-медиаконтура r0.1

status: `OPERATOR_APPROVED_PRODUCT_DIRECTION`

## Решение ОПЕРАТОРА

Концепция интеграции методологического фасилитатора в Telegram-медиаконтур утверждена.

Разрешено немедленно включать в разработку те элементы, которые не ломают уже принятые Phase 1B transport/runtime/privacy решения.

Целевое развитие продукта: инструмент, способный выступать организационным конвейером формирования задач для локальных/автономных групп участников, кооперирующихся для решения собственных проблем.

## Неприкосновенные границы текущей разработки

Не ломать и не переписывать существующий Telegram transport/runtime Phase 1B.
Не ослаблять privacy-minimization / aggregate-only границу без отдельного решения.
Не переносить автоматически полный raw Telegram archive, постоянные user_id/username, DeepSeek, SQLite, aiogram или весь исходный slash-command набор.
Не превращать model output автоматически в проектную задачу, согласие группы или разрешение на публикацию.

## Разрешённый новый слой

Вводится отдельный provider-neutral domain layer:

`Discussion Facilitation / Task Synthesis Layer`.

Он должен работать после privacy/validation + normalization и до approval/dispatch.

Целевая логика:

`allowed event → normalized event → discussion state → disagreement/open questions → candidate question/summary/task → human/group decision gate → dispatch → receipt`

## Ближайший инкремент

До подключения live Telegram разрешено реализовать изолированное ядро на synthetic normalized events:
- schemas `normalized_event`, `discussion_state`, `candidate_task`, `decision_record`;
- optional `candidate_question`, `candidate_summary`, `disagreement`;
- explicit provenance references;
- retention/privacy class fields;
- deterministic state transition rules;
- fail-closed authority boundary: candidate != approved task;
- synthetic tests.

Никакие Telegram API calls, credentials, systemd, production DB, live provider calls или privileged host changes этим решением не разрешаются.

## Дальнейшее развитие

После доказанной устойчивости ядра продукт может поэтапно расширяться до организационного конвейера локальных/автономных групп:
1. структурирование обсуждения;
2. фиксация проблем, целей, критериев и открытых вопросов;
3. формирование candidate tasks;
4. group/moderator approval;
5. decomposition/routing candidates;
6. dispatch/receipt tracking;
7. feedback/result ingestion;
8. обновление discussion/task state;
9. повторный цикл до закрытия проблемы.

Каждый новый класс автономности вводится отдельно после privacy, authority, failure-mode и rollback проверки.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать явное решение ОПЕРАТОРА о включении безопасной фасилитационной функциональности и дальнейшем развитии продукта
СТАТУС: `OPERATOR_APPROVED_PRODUCT_DIRECTION`
