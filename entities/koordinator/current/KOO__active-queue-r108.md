# KOO current active queue r1.08

status: CURRENT_QUEUE
project_time: omitted

## Приоритет 1 — Бустер

КОДЕР закончил исправление full-bound response-shape diagnostics r0.2.
Следующий шаг уже адресован СИСАДМИНУ: независимая non-live reverify.
Automatic exact-chat activation не поддерживается, поэтому требуется ручной запуск SIS.

## Приоритет 2 — Быстрая память

Рабочая ветка: layered Entity memory / memory-layering E2E.
Последнее доказанное состояние: design task уже находится в KOD inbox, но профильная обработка тогда не стартовала из-за невозможности автоматического exact-chat resume.
Перед возобновлением требуется fresh reconciliation этой старой ветки; слепо переиспользовать старый manual activation нельзя.

## Приоритет 3 — Telegram-фасилитатор

Уже независимо проверены:
- facilitator core;
- normalized-event bridge;
- semantic-input contract.

Semantic-input contract подтверждён как bounded candidate-only контур:
никаких Telegram API calls, provider calls, credential use, DB/systemd deployment или execution authority.
Следующий шаг требует fresh reconciliation более поздней facilitator цепочки, а не повторной разработки ядра.

## Отдельные нормативные хвосты

Task-conveyor v1.3 decision gate остаётся pending и не считается активным.
Project Core v2.5 rollout выполнен нормативно; Project Sources заменены ОПЕРАТОРОМ.

## Порядок работы

1. Закрыть текущую SIS reverify бустера.
2. Fresh-reconcile memory-layering и восстановить ближайший допустимый шаг.
3. Fresh-reconcile Telegram facilitator и продолжить с последнего independently verified boundary.
