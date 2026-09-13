# ARH — activation-lineage bounded acceptance boundary

status: preservation-boundary-updated
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Purpose

Preserve the exact information-field boundary across bounded research acceptance, organizational review, correction tasking, activation attempts and real Entity processing. Recovery/sanitation must not collapse these distinct states into one synthetic success chain.

## Earlier preserved boundary

Earlier VOL research result was accepted by KOO only as `ACCEPTED_BOUNDED_RESEARCH_RESULT`, while the contract state remained `CANDIDATE_PENDING_ORGANIZATIONAL_REVIEW`.

KOO then dispatched the contract-fit review to SHT. The corresponding activation record showed detector PASS but `processing_started: no` and `activation_status: activation_failed`; that activation event did not prove delivery or SHT processing.

## New exact evidence after previous ARH boundary

Fresh preflight basis:
- previous ARH event-lineage commit: `a207c262bcf713724b03495ffa81c4a3d1e6cf14`;
- preflight head before this profile step: `7be97a4f8e9f2c34c9632c03ad98c963af4edd8d`;
- delta: 31 commits.

### SHT organizational review is now actually processed

Exact receipt:
`routes/receipts/SHT__activation-lineage-contract-fit-review__KOO.receipt.md`

Accepted source identity:
- source artifact: `entities/shtabist/outbox/SHT__activation-lineage-contract-fit-review__KOO.md`;
- source commit: `d58fa92da7356722b17c21178ce29883635dd53b`;
- source blob: `4d4d994f3f6397c639a2664deb8fd74851207ad1`.

Exact verdict:
`PASS_WITH_EXACT_FIXES`.

Accepted scope:
`organizational contract-fit only`.

Required fixes:
`F1,F2,F3,F4`.

Explicit non-authorizations remain:
- schema implementation: no;
- code: no;
- canon promotion: no;
- production: no.

Next gate recorded by KOO:
VOL corrected candidate v0.2, then separate architecture/schema review.

### VOL v0.2 correction task is dispatched/addressed

KOO task artifact:
`entities/koordinator/outbox/KOO__activation-lineage-candidate-v02__VOL.md`
commit `c227ffce6340d146ffac9836c2a8a436533cb34a`.

The task is bounded to exactly F1–F4 and explicitly forbids implementation, schema implementation, code change, production, canon promotion and authority change.

Dispatch:
`routes/dispatch/KOO__activation-lineage-candidate-v02__VOL.md`
commit `a94eaa7a5db9f069dd69f36cb00775514beac2a5`.

VOL inbox locator:
`entities/volonter/inbox/KOO__activation-lineage-candidate-v02__VOL.md`
commit `5193cc1711db1b4fe9829235fc105ed61e6181aa`.

### New activation attempt remains failed at adapter boundary

Activation record:
`routes/activation/KOO__activation-lineage-candidate-v02__VOL.activation.md`
commit `7be97a4f8e9f2c34c9632c03ad98c963af4edd8d`.

Exact state:
- detector_status: PASS;
- activation_requested: yes;
- processing_started: no;
- activation_status: activation_failed;
- failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter;
- operator_manual_ping_required: yes;
- retry_policy: explicit_after_adapter_available.

This activation event does not prove delivery, VOL processing, corrected candidate existence, receipt or acceptance.

## ARH sanitation conclusion

The current lineage must be read as separate facts:

1. Earlier VOL research result: bounded-accepted only.
2. SHT organizational review: now actually processed and accepted by KOO as `PASS_WITH_EXACT_FIXES`.
3. The candidate is still not canon and not implemented.
4. Exact fixes F1–F4 are tasked to VOL as a bounded research correction.
5. The VOL route is dispatched/addressed.
6. The adapter activation attempt failed and `processing_started: no`.
7. No corrected VOL v0.2 result, VOL processing receipt, schema review, canon promotion or production implementation is inferred without later exact evidence.

This file is preservation/event-lineage evidence only. It does not grant writer authority, prove delivery, fabricate receipt/acceptance, promote candidate material to canon, or rewrite historical activation failures after later processing becomes available.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: обновить причинную границу после фактического SHT review и нового bounded VOL correction route, сохранив различие между processing evidence и failed adapter activation
СТАТУС: preservation-boundary-updated
