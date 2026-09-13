# KOO — сериализованная очередь KOD v0.1

status: ACTIVE_WORKING_QUEUE
project_time: omitted; trusted project-time source not used

## Основание

У KOD одновременно появились три допустимых, но несовместимых как одновременная current-writer работа, хвоста.
KOO выбирает один active KOD lane; остальные сохраняются READY_SERIALIZED.

## Active KOD lane

1. `anthropic-direct-adapter-r01`
   - reason: прямое новое решение ОПЕРАТОРА «работаем с Anthropic»;
   - owner: KOD;
   - state: READY_TO_DISPATCH / затем RUNNING только по факту обработки.

## READY_SERIALIZED после active lane

2. `info-entry-static-preview-E1-evidence-alignment`
   - source: `entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`;
   - WEB verdict: `PASS_WITH_EXACT_REMAINING_FIXES`;
   - remaining defect: E1 — committed readback report не byte-reproducible из exact committed verifier output.

3. `koder-sender-registry-sanitation`
   - source: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap__KOD.md`;
   - ARH finding commit: `81c5f69cb9fc0943b3cc0484e630775ea4bcc66f`;
   - exact scope: append-only reconcile stale receipt state + missing schema-review dispatch row; no history rewrite.

## Rule

- не выполнять эти три KOD-задачи одновременно;
- после каждого KOD result KOO делает fresh preflight и может изменить следующий serialized priority, если появится более сильное событие;
- наличие задачи в inbox не равно RUNNING;
- ARH sanitation finding не закрывать молча и не терять при смене приоритета.

Это рабочая очередь KOO, не Project Source/canon.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: не допустить параллельной мутации одним current-writer KOD и не потерять уже адресованные хвосты
СТАТУС: active_working_queue
