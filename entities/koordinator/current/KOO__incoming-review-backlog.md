# KOO incoming review backlog

status: CURRENT_AUDITED_AFTER_CLOSURE_PASS

## Current live substantive KOO blockers

### 1. SHT → KOO: COOP source conflict

Artifact:
`entities/shtabist/outbox/SHT__COOP-launch-blocked-source-conflict__KOO.md`

State:
`BLOCKED_SOURCE_CONFLICT`.

Conflict:
- `project-instructions-core-v2.1` + `file-work-canon-universal-v2.3` allow verified locator-based delivery;
- `source-loading-policy-v2` section 5 still describes terminal delivery as actual file upload to addressed chat or explicit failure.

This requires explicit OPERATOR normative resolution before SHT may continue the P1 COOP research conveyor.

## Closed in the latest KOO cleanup pass

### VOL Experience Layer

Decision:
`ACCEPTED_BOUNDED_CANDIDATE_WITH_NORMALIZATION_DEBT`.

Decision artifact:
`entities/koordinator/outbox/KOO__experience-layer-verification-decision__VOL.md`
commit:
`36bccfae041fed7ee93a3eafa4e64d5f3ece0024`.

Original and v2 verification routes now have exact receipts.

### SIS VPN/Hiddify experience

Decision:
`ACCEPTED_FOR_PROFILE_EXPERIENCE_MERGE_AND_RUNBOOK`.

Decision artifact:
`entities/koordinator/outbox/KOO__vpn-client-experience-decision__SIS.md`
commit:
`5f8aa5b54c8632afc8ecddf91d03a8b3dde32e99`.

SIS is authorized to append reviewed experience cards and create the Android VPN diagnostics runbook.

Closed device/client registry:
`DO_NOT_CREATE_NOW`.

### SIS activation worker / real Entity activation

Isolated E2E had already been accepted earlier.

Fresh real-boundary blocker was reviewed and accepted:

`BLOCKED_REAL_ENTITY_ACTIVATION_BOUNDARY`.

Decision:
`entities/koordinator/outbox/KOO__real-entity-activation-boundary-decision__SIS.md`
commit:
`754b91a719b2badfe25a22b45c08a647595e5cac`.

SIS runtime branch is closed until a concrete accepted adapter/interface exists.

### SHT activation-worker cross-stage integrity gate

Receipt-closed as dependency-resolved:
`routes/receipts/SHT__activation-worker-v02-integrity-gate__KOO.receipt.md`
commit:
`d5e417b0655fc458c4334a274fcd151469218e36`.

## Mechanical service tails

KOO-owned service tails closed:
1. KOD activation-worker v0.1 direct route;
2. KOD safe-client-helper v0.2 direct route.

Remaining sender-owned registry housekeeping:
1. SHT sender-registry state update for exchange-e2e result with existing receipt;
2. KOD sender-registry state update for entity-activation-gap research with existing receipt.

These two do not block profile work and do not require new KOO substantive review.

## Count

Current substantive KOO review/decision blockers:
`1`.

By sender:
- SHT: `1`;
- SIS: `0`;
- VOL: `0`;
- KOD: `0`;
- WEB: `0`;
- KAN: `0` currently waiting on KOO review.

Current blocker requires:
`explicit OPERATOR normative decision`.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать фактическую очередь KOO после разбора зависших review и service tails
СТАТУС: current_audited_after_closure_pass
