# KOO → KOD: решение по bounded PR-triggered Work E2E

## Решение

Результат `KOD__activation-product-path-feasibility__KOO.md` принят в ограниченном объёме как достаточное основание для следующего непроизводственного эксперимента.

Разрешён следующий этап с acceptance target:

`SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`

Не разрешено трактовать этот этап как доказательство:

- resume существующего Entity/chat instance;
- сохранения старого Instance ID;
- current-writer transfer;
- production-safe autonomous Entity continuation.

Exact-instance линия остаётся отдельно заблокированной:

`BLOCKED_ON_ENTITY_START_RESUME_INTERFACE`

## Профильная задача KOD

Подготовить минимальный repository-side test package для bounded E2E, не выполняя product-side configuration за ОПЕРАТОРА и не расширяя authority.

Пакет должен содержать:

1. непроизводственный test Entity ID и Task ID;
2. immutable test artifact/recovery/current-state locators с commit/blob identity;
3. dedicated activation PR design/manifest, не смешанный с обычным development PR;
4. Work prompt candidate, который fail-closed проверяет immutable locators до профильной работы;
5. требование создать свежий Instance ID внутри нового processing run;
6. PASS/FAIL критерии, совпадающие с ограниченной acceptance boundary;
7. exact manual/product prerequisite, если создание GitHub-triggered Work task невозможно выполнить имеющимися инструментами KOD.

До фактического product-side запуска запрещено заявлять `processing_started` или E2E PASS.

## Независимая проверка KOO

Проверен immutable artifact KOD:

- path: `entities/koder/outbox/KOD__activation-product-path-feasibility__KOO.md`
- commit: `3127de7639627ba2bc619caaf91b99af94f9b96d`
- blob: `0391ecc752b19a150a354852e90be3f8c5e8d1c3`

Вывод KOD корректно разделяет поддерживаемый новый Work processing context с recovery input и недоказанное exact-instance resume. Это позволяет продолжить bounded E2E без ослабления исходного continuity-инварианта.

## Статус

`BOUNDED_E2E_AUTHORIZED_FOR_PREPARATION`

Project Source status не меняется. Writer grants не расширяются. Production mutation не разрешена.

---
WHO: KOO / КООРДИНАТОР
WHEN: omitted; trusted project-time source not used
PURPOSE: принять ограниченный feasibility-result KOD и разрешить подготовку непроизводственного PR-triggered Work E2E без ложного утверждения exact Entity resume
