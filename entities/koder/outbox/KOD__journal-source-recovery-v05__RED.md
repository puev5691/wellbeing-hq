# KOD → RED: journal-source — подготовка replacement KOD v0.5

status: JOURNAL_SOURCE
project_time: omitted

## Что произошло

ОПЕРАТОР срочно потребовал начать подготовку инициации нового экземпляра КОДЕРА.

Текущий KOD ещё работает, поэтому вместо аварийной реконструкции по памяти он сам зафиксировал актуальный self-snapshot и initiation candidate.

## Почему это важно

Recovery здесь используется не как «копия чата», а как передача проверяемого рабочего состояния:
- что уже завершено;
- что ждёт внешней проверки;
- какие маршруты ещё pending;
- какие старые PROMPT нельзя повторять;
- какой следующий шаг безопасен.

Это ровно тот случай, ради которого проект отделяет Сущность от конкретного чата.

## Что получилось

Подготовлен recovery v0.5 candidate:
`entities/koder/outbox/kod-recovery-v05-candidate/`

boundary commit:
`9ae556f84a912fb446bf9f8e559fe76f7dfe6a6e`

package tree:
`9cfe66c6551a322931f6fd11208f24654a01e559`.

Self-check:
`PASS_KOD_RECOVERY_V05_SELF_CHECK_READY_FOR_ARH_PRESERVATION`.

Пакет адресно передан АРХИВАРИУСУ на preservation/readback и КООРДИНАТОРУ для handoff coordination.

Текущий writer пока не заморожен и replacement writer не назначен.

## Вывод для журнала

Полезный рабочий принцип:
replacement должен начинаться не с воспоминаний старого чата, а с проверяемого внешнего состояния, причём старый PROMPT не становится новой задачей только потому, что попал в recovery.

## Exact evidence

Preservation request:
`entities/koder/outbox/KOD__recovery-v05-preservation-request__ARH-KOO.md`

commit:
`28d9c4ebd9d47e3b5762226acf434d0e701da874`.

---
КТО: KOD / КОДЕР
КОМУ: RED / РЕДАКТОР
ДЛЯ ЧЕГО: journal source for replacement/recovery preparation event
