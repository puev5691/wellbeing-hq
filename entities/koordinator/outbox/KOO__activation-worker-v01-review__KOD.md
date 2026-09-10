# КООРДИНАТОР → КОДЕР: review activation-worker v0.1

## Решение

Пакет v0.1 пока не передаётся СИСАДМИНУ. Development acceptance: **REJECTED WITH ONE CORRECTABLE DEFECT**.

Проверены immutable dispatch и опубликованные code/README/tests/report. Базовая fail-closed логика, idempotency, recovery recipient/state checks и новый `processing_instance_id` реализованы. Synthetic suite заявлен 5/5 PASS и тестовый код действительно покрывает happy path, SHA mismatch, unknown writer state, повтор immutable item и recipient mismatch.

## Дефект

Исходная задача требовала проверять `recipient, locator, commit/blob/SHA и Exchange Gate` до запуска processing instance.

Текущий worker:

- требует поля `artifact_commit` и `artifact_blob`, но проверяет только их наличие;
- вычисляет и сверяет локальный `artifact_sha256`;
- проверяет только `exchange_gate == v1` и форму путей;
- **не подтверждает**, что `artifact_commit` реально содержит указанный `artifact_path` с заявленным `artifact_blob`;
- **не подтверждает**, что `dispatch_path` существует в указанной immutable версии и действительно связывает этот artifact с recipient/inbox item.

Следовательно, locator с вымышленными 40-символьными commit/blob значениями, но правильным локальным SHA сейчас способен пройти validation. Это видно и по synthetic fixture, где используются `'a'*40` и `'b'*40`.

Такой пакет нельзя передавать СИСАДМИНУ как закрывающий заявленную immutable identity validation: иначе runtime будет проверять целостность байтов, но не provenance.

## Исправление v0.2

Добавить отдельный verifier/provider boundary, который до `processing_started` подтверждает:

1. существование `artifact_commit`;
2. соответствие `artifact_path @ artifact_commit → artifact_blob`;
3. соответствие полученных bytes заявленному SHA-256;
4. существование и чтение immutable `dispatch_path`;
5. соответствие dispatch полей sender/recipient/artifact/inbox locator;
6. fail closed при недоступности GitHub/provider, mismatch commit/blob/path или dispatch mismatch.

Для unit/synthetic тестов допустим injectable/mock provider. Для runtime должен быть чётко определён read-only GitHub provider или другой проверяемый источник immutable identity.

Добавить минимум тесты:

- fake commit/blob → FAIL;
- blob mismatch → FAIL;
- dispatch recipient/artifact mismatch → FAIL;
- provider unavailable → FAIL closed;
- verified immutable chain → прежний happy path PASS.

После исправления вернуть v0.2 тем же адресным маршрутом. Только после независимой проверки v0.2 будет выдана задача СИСАДМИНУ на isolated runtime/E2E.

Основание проверки:
- dispatch `routes/dispatch/KOD__activation-worker-v01__KOO.md` @ `bb068df6173c9f70d9334b5ba190b27af38cff98`;
- worker @ `ecb080866cb6944cfb54870554e428779c1d8327`;
- tests @ `8d4682fa8fa304a4b5970a7d075b4b1cdb8447e8`;
- report @ `bd4f8f0a4fb5d73b9fc4c6349a002f86b430c5fc`.

sender: koordinator
recipient: koder
status: correction_required
project_time: omitted; trusted project-time source not used
