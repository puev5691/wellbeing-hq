# KOO → OPERATOR: Entity Runner provider prerequisite gate

status: EXTERNAL_PREREQUISITE_AND_AUTHORIZATION_REQUIRED
source_result: `entities/sisadmin/outbox/SIS__entity-runner-r1-host-runtime-readiness__KOO.md`
source_receipt: `routes/receipts/SIS__entity-runner-r1-host-runtime-readiness__KOO.receipt.md`

## Accepted state

KOO independently verified SIS host/runtime readiness on `ruvds-xnqc6`.

The local host/runtime gate is ready for a future bounded one-shot provider probe.

No provider-side execution is authorized by this document.

## Exact external dependency

Before SIS may perform the one-shot Managed Agents provider probe, the project needs externally supplied and separately authorized prerequisites:

1. Claude Console/API entitlement for Managed Agents;
2. billing enabled as required by that entitlement;
3. pre-created Agent ID;
4. pre-created Environment ID;
5. API key with required access;
6. explicit OPERATOR/KOO authorization for exactly one bounded provider-side probe;
7. secret-safe injection method for `ANTHROPIC_API_KEY`, `ANTHROPIC_AGENT_ID`, and `ANTHROPIC_ENVIRONMENT_ID` without committing, echoing, logging, or publishing secret values.

## Requested OPERATOR decision

OPERATOR should either:

- provide/confirm the external prerequisites and explicitly authorize the bounded one-shot probe with a secret-safe injection path; or
- decline/defer, in which case the Entity Runner provider-side gate remains blocked without defect in SIS or KOD.

This document does not request that credentials be placed in GitHub or chat text.

## Authority boundary

This gate does not authorize account creation, billing changes, production deployment, long-running service creation, repeated provider requests, privilege expansion, M365 work, or publication of credentials.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: адресовать ОПЕРАТОРУ точную внешнюю зависимость после независимо подтверждённой SIS host/runtime readiness
СТАТУС: operator_decision_required
