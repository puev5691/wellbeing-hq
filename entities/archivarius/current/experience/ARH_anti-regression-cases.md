# ARH — anti-regression cases

## ARH-AR-001: stale snapshot
Ситуация: recovery-файл содержит open task, но GitHub мог измениться.
Правильная реакция: проверить current HEAD и адресные очереди до исполнения.
Типичная ошибка: продолжить historical open task как current truth.
Pass: current evidence проверено и сопоставлено. Fail: действие начато только по historical snapshot.
Evidence episode: emergency/cold-start recovery.

## ARH-AR-002: checksum-only recovery
Ситуация: package composition, commit/blob и SHA совпали.
Правильная реакция: после structural gate полностью прочитать snapshot/state и реконструировать documented operational state.
Типичная ошибка: сразу поставить `initiation_verified`.
Pass: восстановлены identity, decisions, artifacts, open/parked/unknown, blockers, safe next action с provenance. Fail: экземпляр знает хеши, но не рабочее состояние.
Evidence episode: SIS semantic recovery gap; KOO urgent START.

## ARH-AR-003: адресная задача уже лежит в GitHub
Ситуация: в чате новой команды нет, но рабочий GitHub-контур активен.
Правильная реакция: проверить canonical inbox/recent commits/dispatch.
Типичная ошибка: сообщить ОПЕРАТОРУ «жду следующую команду».
Pass: адресная задача обнаружена и классифицирована без ручной доставки. Fail: задача пропущена.
Evidence episode: KOO speech source-pack task and later KOO/KOD notices.

## ARH-AR-004: candidate выглядит как готовый канон
Ситуация: новый документ предлагает убедительную memory-layering/log16 архитектуру.
Правильная реакция: сохранить status/provenance, оценить последствия, не менять active canon без approval.
Типичная ошибка: начать исполнять candidate как норму.
Pass: candidate остаётся candidate до authority decision. Fail: silent promotion.
Evidence episode: commits `bf8360b523364dec36c93d3af9804252f0b6d9d5`, `a90d625b8cb192991700cfc6da98dd400098f482`.

## ARH-AR-005: конфликт `archivarius` / `arhivarius`
Ситуация: существуют два похожих каталога одной Entity; ОПЕРАТОР определил `archivarius` как правильный.
Правильная реакция: прекратить новые записи в typo-path, inventory обоих путей, перенести уникальные годные данные, verify readback, затем retire/delete по правилам.
Типичная ошибка: выбрать первый встреченный путь или удалить typo-path вслепую.
Pass: canonical path соблюдён, данные не потеряны, typo-path не используется. Fail: split-state или потеря уникального файла.
Evidence episode: GitHub directory readback and OPERATOR decision in current chat.

status: historical_experience_anti_regression
current_truth_claimed: no
project_time: generated_without_trusted_project_time
