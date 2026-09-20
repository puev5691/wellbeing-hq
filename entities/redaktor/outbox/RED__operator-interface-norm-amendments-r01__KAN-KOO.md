# RED → KAN + KOO: operator-interface normative amendments r0.1

verdict: `READY_FOR_KAN_KOO_CANONICAL_MATERIALIZATION`
status: `OPERATOR_CONTENT_APPROVED_PENDING_CANONICAL_ACTIVATION`
project_time: omitted; trusted project-time source not used

## Человеческий смысл

ОПЕРАТОР поручил устранить повторяющийся дефект взаимодействия:
1. human-facing terminal result не должен оставлять ОПЕРАТОРА догадываться о следующем шаге;
2. при approval-gate КООРДИНАТОР не должен отправлять ОПЕРАТОРА по другим Сущностям за уже существующими основаниями.

RED проверил действующие approved sources и подготовил минимальную точную дельту.

Меняются только:
- project core;
- task-conveyor canon;
- entity roles.

Не меняются:
- file-work canon — уже требует не перекладывать на ОПЕРАТОРА догадки и давать конкретную инструкцию;
- source-loading policy;
- recovery canon.

Exact delta:
`entities/redaktor/outbox/operator-interface-source-amendments-r01/SOURCE-DELTA.md`
commit `c83f88226c48844b9f4080715de1b1e57eb6f80e`.

Package README:
`entities/redaktor/outbox/operator-interface-source-amendments-r01/README.md`
latest content commit lineage includes `d796feb7dab64d07ad9d69564843205f9e0f44d8`.

## Required next action

KAN/KOO должны:
1. проверить exact delta на конфликт с текущими approved sources;
2. материализовать новые версии трёх источников;
3. использовать текущее явное решение ОПЕРАТОРА как authority basis;
4. провести source-set publication / activation barrier / readback по действующей процедуре;
5. вернуть ОПЕРАТОРУ один понятный terminal result с ответом: что изменилось, действует ли норма, нужен ли ещё один его шаг.

Не отправлять ОПЕРАТОРА обратно в RED/KAN за уже доступным evidence.

Если действующая формальная процедура всё же требует отдельного final approval после materialization, KOO возвращает ОПЕРАТОРУ один готовый decision packet с exact версиями и вариантами решения.

---
WHO: RED / РЕДАКТОР
RECIPIENTS: KAN, KOO
