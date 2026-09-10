# Activation Worker Prototype v0.2

Исправление v0.1: до `processing_started` теперь проверяется не только SHA локального файла, но и immutable provenance через read-only Git provider.

## Проверяемая цепочка

`artifact_commit exists → artifact_path@commit → artifact_blob → provider bytes SHA → local bytes SHA → dispatch_commit exists → dispatch_path@commit → sender/recipient/exchange_gate/artifact/inbox binding → recovery/current-writer → processing_started`

Любой mismatch или недоступность provider даёт `activation_failed`.

## Provider boundary

Runtime provider v0.2: локальный read-only Git repository, проверяемый командами `git cat-file`, `git ls-tree`, `git show`.

Это намеренно уже и проверяемее, чем сетевой API внутри worker. СИСАДМИН может обновлять mirror/clone отдельным механизмом, но worker принимает решение только по immutable commit SHA.

## Запуск тестов

```bash
python3 test_activation_worker.py
```

Зависимости: Python 3.10+, git. Внешние Python packages не нужны.

## Runtime deployment

Worker запускается непривилегированным service account с:
- read-only доступом к git mirror репозитория;
- read-only recovery/current-state;
- private writable state/evidence dir;
- отдельным handler/Entity runner.

Secrets в repo, locator, stdout/stderr и package не нужны и не включены.

## Ограничение

v0.2 закрывает defect immutable identity/provenance validation. Это всё ещё development package. Полный E2E PASS требует фактического runtime evidence запуска реального processing instance.
