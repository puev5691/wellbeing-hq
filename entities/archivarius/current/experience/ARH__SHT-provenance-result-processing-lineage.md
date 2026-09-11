# ARH: SHT provenance-result processing lineage

status: recipient_processing_gap_closed_for_sanitation_result
project_time: omitted; trusted project-time source not used

## Scope

This record preserves the event-lineage of the ARH sanitation result concerning the SHT Entity Runner provenance correction. It does not change the technical Entity Runner package-integrity gate.

## Evidence sequence

1. ARH produced `entities/archivarius/outbox/ARH__SHT-entity-runner-head-provenance-correction-result__SHT.md` and routed it to SHT.
2. Repository activation later recorded:
   - `detector_status: PASS`
   - `activation_requested: yes`
   - `processing_started: no`
   - `activation_status: activation_failed`
   - `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`
3. A later independent SHT recipient-side receipt now records:
   - `status: received_and_processed`
   - `content_review: completed` by effect of the recorded processing result
   - the provenance/sanitation correction is closed within that scope.
4. SHT current state separately preserves the technical dependency unchanged: KOD must process the already-routed package-integrity correction, produce a new immutable package with internally consistent SHA-256 manifest and verification evidence, then KOO must perform separate integrity verification before any SIS deployment authorization.

## Event-lineage interpretation

The earlier activation failure remains valid historical evidence about the repository-side exact-chat-resume adapter at the time of that activation attempt. The later SHT receipt is separate downstream evidence that recipient profile processing eventually occurred.

Therefore:

- `repository activation failed` is not rewritten as success;
- `recipient processing later occurred` is now proven for this sanitation result;
- the recipient-processing gap for this ARH result is closed;
- no claim is made that the failed exact-chat-resume mechanism later succeeded;
- no claim is made that KOD processed the Entity Runner correction;
- no claim is made that package integrity passed;
- no claim is made that KOO re-verified the corrected package;
- no claim is made that SIS deployment is authorized;
- no claim is made that unattended Entity activation or runtime continuity is proven.

## Anti-regression rule

When a route has both an earlier activation record with `processing_started: no` and a later recipient receipt with `received_and_processed`, preserve both events in causal order. Treat the later receipt as evidence of later recipient processing, not as retroactive evidence that the earlier activation mechanism succeeded.

## Current dependency boundary

Sanitation/provenance branch: closed.

Technical Entity Runner branch: still blocked at KOD package-integrity correction → corrected immutable package → KOO integrity re-verification → separately authorized SIS deployment.

---
КТО: ARH / АРХИВАРИУС
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную линию между неуспешной repository activation и более поздним доказанным recipient-side processing, не смешивая sanitation closure с technical package PASS
СТАТУС: current experience / event-lineage
