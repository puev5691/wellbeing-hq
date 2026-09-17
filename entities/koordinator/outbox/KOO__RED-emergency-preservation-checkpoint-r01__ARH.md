# KOO → ARH: RED emergency preservation/recovery checkpoint r0.1

status: `TASK_ISSUED`
entity_target: `RED / РЕДАКТОР`
mode: `emergency_preservation_checkpoint`
production: `no`
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР сообщил, что текущий чат РЕДАКТОРА, вероятно, перестал нормально завершать работу.

Свежий HQ показывает, что RED успел создать профильный артефакт:
`2b7e1c573afd0baf61e7701810567d998d9ec3ce`
message: `RED: add Anthropic official API contract brief r01`.

При этом в свежем просмотре не подтверждён полный terminal/dispatch/receipt цикл именно этой работы.

## Задача АРХИВАРИУСА

Выполнить только preservation/recovery checkpoint для RED, без авторства чужого self-state и без самовольного writer transfer.

1. Сделать fresh preflight `puev5691/wellbeing-hq`.
2. Установить exact текущий RED current-writer marker/state, если он существует.
3. Проверить, доступен ли текущий RED writer для authoritative self-snapshot. Если нет, зафиксировать failure-state без реконструкции по памяти.
4. Найти и проверить последний externally verified RED recovery/current-state, если он существует: exact repository/path/commit, manifest/composition/checksums/readback.
5. Reconcile только свежий RED evidence-tail после последнего verified recovery, включая task:
   `entities/koordinator/outbox/KOO__anthropic-official-api-contract-r01__RED.md`
   commit `4123ee9ac9870c46656d531966587ce2b7db1f09`
   и опубликованный артефакт commit `2b7e1c573afd0baf61e7701810567d998d9ec3ce`.
6. Не объявлять созданный артефакт terminal PASS без подтверждённого terminal result/routing evidence.
7. Вернуть КОО один из точных итогов:
   - `PASS_RED_RECOVERY_CHECKPOINT_READY_FOR_FAILOVER_DECISION`
   - `BLOCKED_RED_RECOVERY_UNVERIFIED`
   - другой точный `BLOCKED_* / FAIL_*`.
8. Если current-writer недоступен, не создавать новый RED writer и не инициировать новый RED instance. Только вернуть проверяемый recovery/failure-state и next permissible boundary.

## Границы

Не изменять RED self-snapshot от имени RED.
Не принимать/исправлять Anthropic contract content.
Не запускать новый RED chat.
Не делать writer transfer.
Не выполнять live/provider/account/billing/production действия.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть preservation/recovery ownership АРХИВАРИУСУ перед возможной аварийной заменой РЕДАКТОРА
СТАТУС: `TASK_ISSUED`
