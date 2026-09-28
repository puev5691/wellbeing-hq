# KOO → ARH: preserve planned replacement r1.0

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: ARH / АРХИВАРИУС
scope: EXTERNAL_RECOVERY_PRESERVATION_ONLY
project_time: omitted

Resume-First.

ОПЕРАТОР явно поручил КООРДИНАТОРУ подготовить собственную инициацию/replacement так, чтобы новый экземпляр восстанавливал не только техническую роль, но и человеко-ориентированный способ общения.

Current authoritative KOO writer:

puev5691/wellbeing-hq@59378fc3e06e840b5f46c3b7f10beb0ae69c2995:
entities/koordinator/current/KOO__replacement-current-writer-r09.md

blob:
8659c738f7d0a2f595a6da3e0f88633268bd2b75

Exact planned replacement package at current package commit:

puev5691/wellbeing-hq@8a6e2e1fe8352cf18e7e5203e102f79fb7814ec5:
entities/koordinator/outbox/koo-planned-replacement-r10/

Required files:
- KOO__human-interface-contract-r02.md
- KOO__planned-replacement-self-snapshot-r10.md
- KOO__planned-replacement-initiation-draft-r10.md
- RECOVERY-MANIFEST.md

Existing canonical KOO recovery base:

puev5691/wellbeing-entity-bootstrap@ab4c7ad12db9760fe825d2a93b6467499e1a09f4:
entities/koo/recovery/versions/koo-recovery-r09

Perform only preservation-owner work:

1. verify current-writer provenance;
2. verify exact 4-file package composition;
3. verify package contains no secrets;
4. verify no authority/task/writer state is minted by the package;
5. verify the Human Interface Gate does not conflict with active approved Project Sources;
6. preserve the package in the canonical external KOO recovery contour as the next planned-replacement delta/version;
7. perform immutable readback/integrity verification;
8. return exact external recovery locator/version to KOO/OPERATOR.

Important:
The human-interface contract is a mandatory recovery input for the next KOO initiation, not an optional style note.

Do NOT:
- freeze current KOO;
- initiate replacement KOO;
- perform Writer Gate;
- resume or mutate STP-C/P552203 work;
- replay historical PROMPTs.

Expected terminal:
PASS_ARH_KOO_PLANNED_REPLACEMENT_R10_EXTERNALLY_PRESERVED

or exact BLOCKED_/FAIL_.

After result + exact readback + return KOO, STOP.
