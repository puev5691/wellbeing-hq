# KOO → OPERATOR: execution observability / reasoning / transport notes r0.1

status: `CANDIDATE_FOR_FUTURE_DESIGN`
project_time: omitted; trusted project-time source not used

## Смысл

Эта карточка фиксирует эксплуатационные выводы, возникшие в рабочих диалогах и уже частично подтверждённые практикой. Она не является каноном и не меняет действующие authority/process rules.

## 1. WIP считать по execution-cycle

Слот считается занятым, пока task не получила terminal result либо явный `BLOCKED/WAITING`.

Факт, что чат перестал печатать или ОПЕРАТОР считает задачу «законченной», сам по себе не закрывает цикл.

Промежуточный commit, staged file или partial publication не равны terminal completion.

## 2. Reasoning effort задавать как часть task metadata

Для chat-surface использовать advisory field:
`RECOMMENDED_REASONING: MEDIUM|HIGH|XHIGH`.

Это не переключает ChatGPT автоматически и является инструкцией ОПЕРАТОРУ/launch surface.

Для будущего API-runner поле должно стать машинным параметром provider request.

Рабочая гипотеза для калибровки:
- MEDIUM: штатная профильная работа;
- HIGH: сложный debugging, architecture, reconciliation, конфликтующее evidence;
- XHIGH: редкие критические recovery/audit задачи.

Не считать эту градацию утверждённой нормой до накопления telemetry.

## 3. Latency разложить на этапы

Не использовать одну wall-clock цифру как объяснение «модель тормозит».

Фиксировать события:
- `dispatch_at`
- `activation_at`
- `first_work_at`
- `terminal_result_at`
- `routing_complete_at`

Производные:
- `queue_latency = activation - dispatch`
- `startup_latency = first_work - activation`
- `execution_latency = terminal_result - first_work`
- `routing_latency = routing_complete - terminal_result`
- `wall_latency = routing_complete - dispatch`

Для chat-surface допустимым внешним evidence являются Git commit/event timestamps там, где соответствующее событие действительно отражено GitHub.

Для API-runner нужны собственные monotonic/runtime timestamps.

## 4. Run telemetry

Минимальная запись на execution-cycle:
- `run_id`
- `entity`
- `task_identity`
- `surface`
- `provider/model`
- `reasoning_effort`
- пять lifecycle timestamps
- пять latency values
- tool calls
- GitHub reads/writes
- commits
- retries
- reconciliation count
- operator re-wake count
- terminal status
- usage tokens/cost для API, если доступны

Эти данные нужны для отделения:
- model reasoning cost/latency;
- tool/GitHub latency;
- workflow/reconciliation overhead;
- operator waiting/rewake;
- возможной lifecycle/context degradation.

## 5. Retired-instance research

Исследовательская линия должна оставаться background и не занимать профильный WIP-slot.

Текущий v0.3 использует `CAPTURE_FIRST / COMPACT_TRANSPORT / EXTERNAL_COLLECTOR`.

Полные evidence-простыни не должны передаваться через ОПЕРАТОРА, если достаточно compact SAMPLE_CARD + locator/file.

## 6. Transport principle

Значимый подробный результат хранить файлом/артефактом.

Через чат передавать:
- смысл;
- terminal status;
- immutable locator;
- следующий шаг/stop condition.

Не дублировать содержимое файла многостраничной вставкой в чат без практической необходимости.

## 7. Future orchestrator use

Эти поля должны быть учтены при проектировании API Entity Runner / orchestrator:
- task-class → reasoning-effort policy;
- automatic latency telemetry;
- automatic terminal-cycle detection;
- external canonical state;
- compact operator reporting;
- separation of execution result from routing completion;
- later evidence-based replacement/health decisions.

## 8. Evidence boundary

Эта карточка фиксирует наблюдения и design requirements. Она не доказывает, что рост latency вызван старением контекста, reasoning effort или конкретной причиной.

Такой вывод допустим только после накопления сопоставимых runs/samples.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: не терять эксплуатационные выводы из диалогов и превратить их в input для будущего runner/orchestrator design
СТАТУС: `candidate_for_future_design_r01`
