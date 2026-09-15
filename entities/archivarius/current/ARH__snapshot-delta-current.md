# ARH — supplemental current-state delta

status: supplemental_current_state_non_canon
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Этот файл дополняет, но не заменяет `entities/archivarius/current/ARH__snapshot.md`.
Он нужен для Resume-First, когда базовый emergency snapshot остаётся полезным как большой проверенный слепок, но после его последнего refresh появились существенные bounded-состояния, которые нельзя терять между запусками.

Этот supplement не является approval, canon, writer-authority grant или доказательством delivery/processing сам по себе.

## Проверяемая граница

- repository: `puev5691/wellbeing-hq`
- branch: `main`
- base snapshot blob: `8223ea771012d1cf0cc654047e51e87787879bbe`
- previous ARH run boundary: `fdfa35751e137b9cb1ab8d12097531452b1d4bfb`
- pre-profile HEAD: `4397e9cd848eb399b8c702c8c1ac7aabc4caa9a8`
- fresh delta after previous run: `1 commit ahead / 0 behind`
- canonical ARH path checked: `entities/archivarius/`

Invariant remains:
`WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`.
The scan itself is not profile execution.

## Fresh preflight classification

### KOO / KOD recovery initiation runbook v0.2

Fresh commit:
`4397e9cd848eb399b8c702c8c1ac7aabc4caa9a8`

Fresh artifact:
`entities/koordinator/outbox/KOO__KOD-initiation-recovery-runbook-v02__OPERATOR.md`

Verified state:
- status: `INITIATION_RUNBOOK_READY`;
- canon: `no`;
- canonical KOD recovery remains `puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`;
- ARH verification remains `PASS_PUBLISHED_CANONICAL_RECOVERY` at commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`;
- the runbook explicitly records that newer KOD evidence exists after recovery publication, including Static Preview E1 result `1f31bc2b640a456f2f99655620e809ce8eaeaada` and package `434ffc103b620711ab4f784d8c825e17bd91a927`;
- therefore the canonical recovery snapshot must not be treated as exhaustive current state without fresh HQ reconciliation;
- successful initiation alone does not establish a new KOD current-writer; absent an explicit retirement/replacement boundary, the permitted stop state is `initiation_verified / WAITING_OPERATOR_WRITER_DECISION`.

This fresh commit changes KOD recovery-orchestration state but does not create an exact ARH task, does not promote the runbook to canon and does not alter KOD writer authority by itself.

## Delta after the base snapshot

### 1. SIS recovery-pending lifecycle policy gap

Current evidence object:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`

Its verified semantic state says replacement SIS current-writer is established, practical replacement initiation was performed and verified, writer gap is resolved, and recovery-registry reconciliation was completed. The locator still remains under `recovery-pending/`.

ARH therefore classified a structural/lifecycle ambiguity and did not move, rename or delete the object without an exact disposition rule.

Exact ARH dependency artifact:
`entities/archivarius/outbox/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md`
- artifact commit: `2ea877283576a5c14f9a8b19b7331e025a5ecd1f`
- artifact blob: `d3a6f0fece88f94fe5df151e6cf70237ed0f40d0`
- verdict: `BLOCKED_RECOVERY_PENDING_LIFECYCLE_DESTINATION_UNDEFINED`

Exchange Gate remains unresolved at this boundary:
- dispatch: `routes/dispatch/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md`
- receipt: not asserted;
- acceptance: not asserted.

ARH does not relocate the recovery object without exact KOO lifecycle disposition.

### 2. Wake / Resume / Initiation → ARH recovery-operational review routing boundary

KAN authority/terminology review is complete with `PASS_WITH_EXACT_AUTHORITY_FIXES`, but without canon approval, implementation selection, writer-state establishment or production authority.

The intended sequence remains:
`KAN authority/terminology review → ARH recovery-operational review → KOO integration → OPERATOR decision`.

The next ARH review was not materialized as an exact KOO → ARH task. ARH therefore routed the exact gap to KOO in the previous profile pass:

`entities/archivarius/outbox/ARH__recovery-operational-review-routing-gap__KOO.md`

Verified blocker:
`BLOCKED_EXACT_ARH_RECOVERY_OPERATIONAL_TASK_NOT_MATERIALIZED`.

Exchange Gate state:
- artifact commit: `b752ce408a4d3132735ca7ac394f4bef64a4523b`;
- dispatch commit: `e78b8b8aca75c9d1e5617dd1e2380fafeb405165`;
- KOO inbox locator final commit: `372fef233eedbddd2f5ec9632a81b888b2ec9ebe`;
- sender-registry commit: `92ae080c80c95103abe4cf235a8049cd3ff0a0a2`;
- activation detector: `PASS`;
- activation requested: `yes`;
- processing started: `no`;
- activation status: `activation_failed`;
- failure reason: `exact_entity_chat_resume_not_supported_by_current_adapter`;
- operator manual ping required: `yes`;
- exact receipt `routes/receipts/ARH__recovery-operational-review-routing-gap__KOO.receipt.md`: absent at this boundary;
- acceptance: not asserted.

Current state is therefore:
`ARH_RECOVERY_OPERATIONAL_REVIEW_GAP_ROUTED_TO_KOO_WAITING_PROCESSING_EVIDENCE`.

This is **not** `EXECUTING`. ARH must not infer the review scope from the queue or from the routing artifact itself.

### 3. KOD recovery freshness boundary

Canonical KOD recovery remains independently verified and published, but it predates newer HQ evidence. The fresh KOO runbook v0.2 correctly treats recovery as a verified basis plus a mandatory fresh reconciliation step, not as an exhaustive current-state claim.

ARH therefore preserves both facts simultaneously:
- canonical recovery identity and prior ARH verification remain valid within their publication boundary;
- later KOD state/results must be reconciled after recovery before profile execution or writer decisions.

No canonical recovery rewrite or promotion is performed in this pass.

## Still-open ARH service tails

No exact return receipt is asserted for tracked tails unless a file is actually present and identity-checked. Historical sender-registry rows are not rewritten; reconciliations remain append-only.

## Resume rule

A replacement ARH should read in this order:

1. `entities/archivarius/current/ARH__initiation-current.md`
2. `entities/archivarius/current/ARH__snapshot.md`
3. `entities/archivarius/current/ARH__snapshot-delta-current.md`
4. fresh GitHub-preflight from the newest observed boundary before any profile execution.

If this supplement conflicts with later exact evidence, later verified evidence wins. If it conflicts with Project Source/canon, Project Source/canon wins.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить bounded current-state delta поверх большого emergency snapshot без переписывания истории, без повышения authority/canon и без выдуманного processing
СТАТУС: supplemental_current_state_non_canon
