# KOO: OPERATOR decision on delivery-rule conflict

status: OPERATOR_NORMATIVE_DECISION_EFFECTIVE

## Decision

ОПЕРАТОР выбрал:

`Вариант 1`.

Therefore, effective immediately for project routing semantics:

The section 5 wording of `source-loading-policy-v2`, insofar as it makes physical file upload to the addressed chat the only successful terminal delivery mode, is superseded by the newer approved delivery model in:

- `project-instructions-core-v2.1`;
- `file-work-canon-universal-v2.3`.

## Effective routing rule

Addressed delivery may be completed by either:

1. actual file transfer to the addressed recipient; or
2. verified locator-based delivery of an existing artifact.

Locator-based delivery is terminal only when all required conditions are satisfied:

- artifact actually exists;
- concrete recipient is identified;
- addressed dispatch is performed;
- locator is available to the recipient;
- required immutable version identity is verifiable;
- receipt is confirmed where required by the route;
- failure-mode exists for locator unavailability or version mismatch.

Publication alone is not delivery.

Receipt alone is not semantic acceptance.

Physical manual file carrying by OPERATOR is not required when a valid locator-based route is available.

## Scope

This decision resolves the approved-source conflict for current execution now.

It does not silently rewrite the historical bytes of `source-loading-policy-v2`.

KAN is assigned to prepare a harmonized replacement revision so the active source text itself stops carrying the obsolete contradiction.

ARH preservation/provenance should preserve the old source as superseded historical provenance after the harmonized revision is approved and activated.

## Direct consequences

- SHT COOP research conveyor is unblocked and continues the same P1 task.
- Future process/OSS designs may use locator-based delivery as the general project routing model.
- OPERATOR is no longer required as physical file courier where verified locator-based delivery is possible.
- Existing security, authority, secret-handling and acceptance boundaries remain unchanged.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать явное решение ОПЕРАТОРА по конфликту правил адресной доставки
СТАТУС: operator_normative_decision_effective
