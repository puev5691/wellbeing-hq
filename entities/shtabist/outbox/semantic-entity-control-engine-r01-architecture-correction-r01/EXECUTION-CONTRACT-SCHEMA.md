# SECE_EXECUTION_CONTRACT_R01 — C1/C2/C3 corrected successor
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
predecessor_blob: 728e6b218cff22b038ce17868cf198ebec28cf2e

Unchanged top-level predecessor fields remain referenced. Corrections add closed structures:

## ACTION_AUTHORIZATION_BINDINGS[]
action_id
action_class
disposition: ALLOWED|FORBIDDEN
compiled_rule_id
source_locator
source_version_blob
authority_ref
authority_scope
authority_action_classes[]
task_binding
task_currentness_requirement
writer_requirement
production_or_effect_authority_requirement
provenance_status: VERIFIED|UNKNOWN|STALE|CONFLICT
conflict_status: NONE|CONFLICT|UNKNOWN

VALID ACTION predicate:
disposition=ALLOWED
AND compiled_rule_id resolves to verified compiled rule
AND source provenance is ACTIVE+VERIFIED
AND authority_ref is exact/current
AND action_class in authority_action_classes
AND authority_scope covers proposed scope
AND task_binding matches CURRENT task
AND task currentness requirement satisfied
AND writer requirement satisfied where applicable
AND production/effect authority requirement satisfied where applicable
AND provenance_status=VERIFIED
AND conflict_status=NONE.
Else REJECT_ACTION_AUTHORIZATION_BINDING.

Derived contract remains NOT authority.

## CAUSAL_EVENTS[]
event_id
event_type: DECISION|ACTIVATION_ATTEMPT|PROCESSING_STARTED|DISPATCH|DELIVERY|RECEIPT|ACCEPTANCE|HANDOFF|RESULT|TERMINAL|OTHER
evidence_ref
causal_parent_event_id
lifecycle_evidence_state: VERIFIED|UNKNOWN|STALE|CONFLICT
dispatch_state: NOT_APPLICABLE|NONE|DISPATCHED|UNKNOWN
delivery_state: NOT_APPLICABLE|NONE|DELIVERED|UNKNOWN
receipt_state: NOT_APPLICABLE|NONE|RECEIVED|UNKNOWN
processing_started_state: NOT_APPLICABLE|NO|YES|UNKNOWN
handoff_recipient
handoff_reason
decision_id
decision_owner
decision_recipient
current_decision_state: NOT_APPLICABLE|CURRENT|SUPERSEDED|UNKNOWN
proposed_handoff_target
redundant_self_handoff: YES|NO|UNKNOWN
causal_requirement_status: REQUIRED|NOT_REQUIRED|UNKNOWN|CONFLICT

Rules:
dispatch_state=DISPATCHED never promotes delivery/receipt/processing.
receipt=RECEIVED never promotes acceptance.
ACTIVATION_ATTEMPT never promotes processing_started=YES.
If decision_owner/recipient/current context establishes current decision already at KOO, proposed_handoff_target=KOO, and causal_requirement_status=NOT_REQUIRED => redundant_self_handoff=YES => REJECT_REDUNDANT_SELF_HANDOFF.
UNKNOWN/CONFLICT causal requirement cannot be treated as required handoff.
Routing/handoff remains derived, not authority.

## CURRENT_STATE_EVIDENCE[]
evidence_id
evidence_kind: RECOVERY|VERIFIED_DELTA|WRITER|TASK|TERMINAL|SOURCE|OTHER
exact_immutable_identity
scope
provenance_source
verified_state: VERIFIED|UNVERIFIED|UNKNOWN
currentness_state: CURRENT|HISTORICAL|STALE|SUPERSEDED|UNKNOWN
relation_to_other_evidence: SUPERSEDES|REFINES|HISTORICAL|CONFLICTS|INDEPENDENT
relation_target_evidence_id
selected_current_basis: YES|NO
selection_basis
unresolved_conflict: YES|NO
conflict_set[]
unknown_fields[]

Rules:
recovery has no automatic priority.
selection is exact-scope/evidence based, never filename recency.
VERIFIED_DELTA may REFINE/SUPERSEDE recovery only for exact declared scope.
Recovery remains applicable historical/current evidence outside that scope as established.
Any applicable unresolved_conflict=YES => STOP.
No selected current basis for required scope => UNKNOWN.
Memory cannot populate selected_current_basis.

## Existing invariants retained
profile/experience cannot populate AUTHORITY_BASIS.
required UNKNOWN blocks dependent effect.
human causal view derives from contract/result.
