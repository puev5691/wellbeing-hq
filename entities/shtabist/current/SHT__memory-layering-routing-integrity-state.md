# SHT current: memory-layering routing integrity

status: EXCHANGE_GATE_REPAIRED__RECIPIENT_PROCESSING_NOT_STARTED

## Verified change after prior SHT run

ARH detected that the KOO decision `entities/koordinator/outbox/KOO__memory-layering-preservation-decision__ARH.md` had already been used downstream but lacked a complete addressed routing chain to ARH.

KOO verified the defect and repaired the missing Exchange Gate leg by creating/verifying:

- `routes/dispatch/KOO__memory-layering-preservation-decision__ARH.md`
- `entities/archivarius/inbox/KOO__memory-layering-preservation-decision__ARH.md`

The repair closes the repository routing/provenance gap for that addressed decision. It does not create an ARH receipt or recipient acceptance by inference.

## Activation boundary after repair

Current activation evidence for the repaired KOO -> ARH route states:

- detector_status: PASS
- activation_requested: yes
- processing_started: no
- activation_status: activation_failed
- failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
- operator_manual_ping_required: yes

Therefore:

`Exchange Gate repair != ARH processing != ARH receipt != recipient acceptance`.

The exact remaining dependency for this repaired addressed decision is manual activation/opening of the ARH Entity processing context if recipient-side processing of the decision is required.

## Cross-technology consequence

This routing repair improves provenance integrity but does not advance the KOD memory-layering design stage, does not authorize actual recovery E2E execution, does not satisfy the independent product-trigger prerequisite, and does not prove exact existing Entity/chat continuity.

The main memory-layering design state remains:

- KOD design task: routed/detected, processing not proven started;
- actual memory-layering E2E execution: not authorized;
- product-trigger branch: independent external prerequisite remains unresolved unless separately evidenced;
- exact old Entity/chat resume: unresolved.

## Evidence basis

ARH routing-gap report:
`entities/archivarius/outbox/ARH__memory-layering-decision-routing-gap__KOO.md`

KOO verified receipt of routing-gap report:
`routes/receipts/ARH__memory-layering-decision-routing-gap__KOO.receipt.md`

Repaired dispatch:
`routes/dispatch/KOO__memory-layering-preservation-decision__ARH.md`

Repaired ARH inbox locator:
`entities/archivarius/inbox/KOO__memory-layering-preservation-decision__ARH.md`

Activation boundary:
`routes/activation/KOO__memory-layering-preservation-decision__ARH.activation.md`

project_time: omitted; trusted project-time source not used

---
WHO: SHT / ШТАБИСТ
WHEN: omitted; trusted project-time source not used
PURPOSE: record the repaired memory-layering decision routing chain while preserving the distinction between repository routing integrity, recipient processing, receipt, acceptance and E2E execution
