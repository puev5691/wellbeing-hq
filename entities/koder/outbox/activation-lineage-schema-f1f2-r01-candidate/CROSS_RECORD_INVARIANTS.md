# Activation-lineage v0.1 candidate — cross-record invariants

status: `CANDIDATE_FOR_ORG_REVIEW`
scope: cross-record rules intentionally not claimed as JSON Schema guarantees
runtime_validator: not implemented
scheduler: not implemented
automation: not changed
production: no
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Boundary

`schema.json` validates one JSONL record structurally. The rules below require a future collection-aware validator and/or immutable repository evidence lookup. This file is specification only; no validator is implemented by this package.

## Required future validator invariants

1. **Unique event identity.** `event_id` MUST be unique across the candidate/event set. JSON Schema for an individual JSONL record cannot prove property uniqueness across records.

2. **Referenced event existence.** Every non-null `source_event_id` and every value in `bridge_reference_event_ids` MUST resolve to an existing immutable event record in the same governed event set or an explicitly allowed external lineage set.

3. **No self-reference.** An event MUST NOT reference its own `event_id` through `source_event_id` or `bridge_reference_event_ids`.

4. **Relation-target semantics.** `causal_parent`, `transport_predecessor`, and `bridge_reference` are not interchangeable. A future validator MUST verify the target event is used according to the declared relation, not infer relation type from filename, topic, timestamp, recipient, or apparent ordering.

5. **Semantic lineage versus transport lifecycle.** `causal_parent` contributes to semantic experiment/task lineage. `transport_predecessor` contributes only to Exchange Gate lifecycle. A transport edge MUST NOT become a semantic parent edge merely because both records refer to the same artifact or object.

6. **Bridge is append-only and non-retroactive.** A later bridge/corroboration event MAY reference an earlier immutable record. It MUST NOT require mutation of the earlier record and MUST NOT rewrite historical parentage. In particular, a Branch A bridge to a Branch B event does not turn Branch B into a child of Branch A.

7. **Experiment/task separation.** Different non-null `experiment_id` or `task_id` values remain separate lineages unless a later explicit bridge event proves a bounded relation. A bridge relates lineages; it does not merge or replace their identities.

8. **Acceptance evidence is separate.** `dispatch`, `inbox_publication`, `receipt`, and `activation_attempt` MUST NOT create or infer acceptance. `acceptance_status=PROVEN` requires a separate immutable evidence event and exact bounded `acceptance_scope`.

9. **Receipt is not acceptance.** A receipt proves only the receipt claim of that record. It MUST NOT upgrade the underlying semantic result, package, task, or blocker to accepted unless separate acceptance evidence exists.

10. **Activation attempt is not real processing.** An `activation_attempt_recorded` event, worker marker, detector PASS, delivery marker, or `activation_requested` state MUST NOT be promoted to `real_processing_start`. Real processing requires separate evidence addressed to a concrete target Entity processing instance.

11. **`event_claim_verified` is local.** `event_claim_verified=true` proves only the claim made by the current event record under `verification_scope=current_event_record_claim_only`. Verification MUST NOT propagate through parent, transport, bridge, acceptance, or activation edges.

12. **Artifact identity must be checked externally.** `source_artifact`, `source_commit`, and `source_blob` have structural forms in `schema.json`, but their actual repository identity and byte correspondence require immutable Git readback. A 40-hex string is not evidence by itself, because apparently humans needed that sentence written down.

13. **Publication time is not semantic event time.** Git commit/publication timestamps MUST NOT populate or imply `event_time` unless an independently defined evidence rule establishes equivalence for that event class. Missing time stays unknown/null; ordering inference from null or repository order is forbidden.

14. **Publication order is not causality.** Earlier Git publication does not automatically establish causal parentage; later publication does not automatically establish a bridge.

15. **Acceptance scope does not widen.** A proven bounded scope such as `preparation_only` or corroboration-only acceptance MUST NOT be generalized to execution, processing, deployment, authority, or production acceptance.

16. **No evidence promotion by state labels.** `previous_state`, `new_state`, `result_class`, `branch_status`, or `transport_stage` labels are claims attached to the current record. They do not independently prove a stronger external event.

17. **Future real-processing event class requires explicit contract change.** The v0.1 structural schema intentionally contains no `real_processing_start` event type. Adding one requires an explicit schema revision plus evidence rules; consumers MUST NOT synthesize such an event from current transport records.

## Current v0.2 candidate observations

- 24 records.
- `source_relation`: 5 `causal_parent`, 16 `transport_predecessor`, 3 null; bridge references are carried separately in `bridge_reference_event_ids` on later records.
- `acceptance_status`: 2 `PROVEN`, 6 `UNKNOWN`, 16 `NOT_APPLICABLE`.
- Dispatch/inbox/receipt/activation-attempt records use `NOT_APPLICABLE` and null `acceptance_scope`.
- All activation-attempt records report `activation_failed`; none proves real Entity processing.
- All semantic `event_time` values remain null; loaded Git times are publication time only.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: отделить cross-record invariants от реально выражаемых JSON Schema ограничений
СТАТУС: CANDIDATE_FOR_ORG_REVIEW
