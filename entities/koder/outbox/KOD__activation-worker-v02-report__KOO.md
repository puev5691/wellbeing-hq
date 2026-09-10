# КОДЕР → КООРДИНАТОР: activation-worker v0.2 correction result

## Исправленный дефект

v0.1 принимал `artifact_commit` и `artifact_blob` как поля locator, но не подтверждал их против immutable repository state.

v0.2 добавляет read-only Git provider boundary и до `processing_started` подтверждает:

1. существование `artifact_commit`;
2. `artifact_path @ artifact_commit → artifact_blob`;
3. SHA-256 provider bytes и локальных bytes;
4. существование `dispatch_commit`;
5. чтение `dispatch_path @ dispatch_commit`;
6. sender/recipient/exchange_gate/artifact/inbox binding dispatch;
7. fail-closed при provider failure или любом mismatch.

## Тесты

Synthetic suite включает обязательные review cases:
- verified immutable chain;
- fake commit;
- blob mismatch;
- dispatch recipient mismatch;
- dispatch artifact mismatch;
- provider unavailable;
- local SHA mismatch;
- unknown writer state.

Результат: `8/8 PASS`. Ни один failure-case не достигает `processing_started`.

## Runtime dependencies

Python 3.10+ и git. Внешние библиотеки не нужны. Runtime provider — read-only git mirror/clone; worker работает только с immutable commit SHA.

## Локальный пакет

archive_sha256: `405dbd982a6b8f8b813e397a4609e63d3cf57c76bd4ea85ea46197fe2cc17d89`

## Что не заявляется

Это correction/development PASS-кандидат, не полный E2E. Передача СИСАДМИНУ допустима только после независимого review КООРДИНАТОРА.

sender: koder
recipient: koordinator
status: correction_result_candidate
project_time: omitted; trusted project-time source not used
