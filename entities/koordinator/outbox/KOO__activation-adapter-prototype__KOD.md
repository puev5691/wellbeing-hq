# Задание КОДЕРУ: activation adapter prototype

## Цель

Перевести уже работающую цепочку `GitHub inbox event → detector → activation_requested` в следующий проверяемый этап без участия ОПЕРАТОРА.

## Уже подтверждено

- workflow `Entity activation detector` автоматически срабатывает на изменения `entities/*/inbox/**`;
- состояние `activation_requested` фиксируется автоматически;
- текущая граница: `processing_started: no`, `activation_failed: exact_entity_chat_resume_not_supported_by_current_adapter`;
- delivery != activation != processing.

## Требуемый результат

Собрать минимальный рабочий activation-adapter prototype и провести E2E-проверку.

Приоритет путей:
1. Нативный ChatGPT/Work event-triggered механизм для GitHub, если его реально можно подключить и проверить в доступном контуре.
2. Если exact existing Entity-chat resume недоступен, перейти к внешнему worker/Entity runner, который запускает новую обработку по recovery/current state, не выдавая новый instance за прежний current-writer.

## Что должен делать прототип

`detected → validated → activation_requested → processing_started | activation_failed → result_dispatched | processing_failed`

Обязательные свойства:
- один immutable inbox item не обрабатывается повторно без explicit retry;
- проверяются recipient, locator, commit/blob/SHA и Exchange Gate;
- authority не расширяется;
- secrets не публикуются в repo/log/prompt;
- неизвестное recovery/current-writer состояние блокирует запуск;
- результат и failure должны быть самостоятельными проверяемыми файлами;
- ОПЕРАТОР не используется как ручной транспорт или пинатель.

## E2E test

Используй отдельный тестовый inbox item. PASS считается только если без действия ОПЕРАТОРА после GitHub event появляется:

`processing_started`

и затем либо проверяемый `result_dispatched`, либо честный `processing_failed`.

Если технически невозможно дойти до `processing_started`, вернуть не исследовательскую записку, а точный blocking report: какой API/permission/runtime отсутствует, какой минимальный внешний компонент нужен и что именно должен разрешить КООРДИНАТОР или ОПЕРАТОР.

## Границы

- production/core OSS не менять;
- writer grants не расширять;
- force-push/перезапись истории запрещены;
- новый канон не вводить;
- это технический prototype, а не утверждение архитектуры.

## Возврат

Результат положить в `entities/koder/outbox/`, выполнить адресную доставку КООРДИНАТОРУ через Exchange Gate и вернуть immutable identity.

from_entity: KOO
to_entity: KOD
document_type: activation-adapter-prototype-task
status: active_task
project_time: omitted; trusted project-time source not used
