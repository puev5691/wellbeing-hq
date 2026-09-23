# SIS → RED: journal-source — MAIN memory-layering остановлен до одноразовой попытки

Перед единственным synthetic MAIN обнаружен дефект уже допущенной runtime-конфигурации.

Изоляция p552203 работает, package и authority актуальны, но semantic broker был закреплён в readiness-режиме: он физически завершает работу после четырёх запросов. Для обязательного восстановления NEW-01 по design нужно семь точных retrieval reads.

Поэтому MAIN не запускался и одноразовая authority не израсходована. Исправлять broker на месте нельзя: изменится identity уже admitted runtime.

Событие полезно тем, что одноразовый эксперимент снова сохранён от ложного старта. Следующий шаг — узкая коррекция broker lifecycle, независимая проверка и обновлённый runtime admission.

Evidence:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-preclaim-broker-blocker__KOO-SHT-ARH.md
machine:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-preclaim-broker-blocker.json

status: source_only
project_time: omitted
