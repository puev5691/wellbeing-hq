# SIS → RED: journal-source — reasoning перестал быть ложной тревогой, не став новой дверью

После первого реального Booster-вызова выяснилось, что OpenAI возвращает не только пользовательский текст, но и служебный контейнер reasoning. Старый normalizer воспринимал его как запрещённое действие и останавливал цепочку.

ОПЕРАТОР разрешил очень узкую политику: exact type=reasoning можно игнорировать как metadata, но его содержимое нельзя превращать в результат, команду, tool action или acceptance evidence.

КОДЕР реализовал коррекцию. СИСАДМИН независимо проверил её без нового provider call.

Проверка подтвердила две вещи одновременно:
1. reasoning больше не ломает нормальный assistant/output_text результат;
2. защита не стала шире: function_call, tools/actions, unknown types, aliases metadata/reasoning_summary, non-assistant roles и запрещённые content types всё ещё блокируются.

Это хороший пример того, как проект исправляет не «ошибку вообще», а строго найденную причину, не открывая попутно лишние возможности.

Evidence:
entities/sisadmin/outbox/SIS__booster-reasoning-metadata-normalizer-correction-r01-independent-verify__KOO.md
commit 25c457f661a18a426247c70373d27a3623376ac2
blob 7f86644952608322e700fa3a2ae685c374d85447

status: source_only
project_time: omitted
