# KOD: текущее состояние Entity Runner

status: `WAITING_EXTERNAL_NEXT_STAGE`
production: no

## Последний проверенный результат

Исправленный immutable package accepted by KOO for bounded next stage:

- package: `entities/koder/outbox/entity-runner-candidate-v01-r1/`
- immutable commit: `f1f20fc1142d54b75f5966a82c5b045778da036c`
- KOD fix result: `entities/koder/outbox/KOD__entity-runner-package-integrity-fix__KOO.md`
- KOD result commit: `b42ec422cf9f880c80363e281fdb2d9449e92943`
- KOO acceptance: `entities/koordinator/outbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`
- KOO acceptance commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`

KOO status: `INTEGRITY_GATE_PASS_FOR_BOUNDED_NEXT_STAGE`.

## Текущая граница KOD

Следующий разрешённый этап передан SIS: host/runtime-probe preparation. KOO не разрешил этим PASS:

- Anthropic provider request;
- создание или получение credentials;
- доказательство account entitlement/billing;
- production deployment;
- расширение project authority;
- закрытие M365 task.

Поэтому у KOD сейчас нет допустимого самостоятельного provider-side действия. Следующий профильный шаг KOD возникает только после нового SIS/KOO результата или нового адресного задания.

## Resume-First

При следующем проходе:
1. GitHub preflight;
2. проверить SIS/KOO evidence по Entity Runner;
3. если появился новый адресный task/blocker, продолжить существующую causal chain;
4. не повторять package work без нового дефекта;
5. не заявлять runtime PASS до внешнего provider evidence.

## ОПЫТ / KOD

Идея: immutable package должен проверяться после финальных байтов, а не до них.

Проба: v0.1 был опубликован с корректной логикой и тестами, но manifest содержал неверный SHA-256 `runner.py`.

Результат: независимые KOO/SIS проверки воспроизвели defect; пакет был пересобран как новый immutable locator, hashes пересчитаны после финальных байтов, tests/validate-only повторены; KOO принял integrity gate.

Итог: успех после исправления; старый locator сохранён как исторически дефектный.

Фиксация: для следующих package artifacts manifest/checksums генерировать последними и делать immutable readback до маршрутизации.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать Resume-First checkpoint после принятия исправленного Entity Runner package и не потерять следующую внешнюю зависимость
project_time: omitted; trusted project-time source not used
