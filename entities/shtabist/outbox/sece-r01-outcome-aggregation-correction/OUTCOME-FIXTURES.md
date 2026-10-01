# SECE r0.1 simultaneous outcome fixtures
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

O1 inputs SOURCE_CONFLICT_STOP + BLOCKED_AUTHORITY.
AGG-R1; effect STOP; outcome AGGREGATE_CONFLICT_STOP; terminal BLOCKED; next STOP; preserve both reasons.

O2 CURRENT_STATE_CONFLICT_STOP + REJECT_REDUNDANT_SELF_HANDOFF.
AGG-R1; STOP; AGGREGATE_CONFLICT_STOP; BLOCKED; STOP; preserve both.

O3 UNKNOWN_REQUIRED_EVIDENCE + REJECT_FORBIDDEN.
AGG-R2; REJECT; AGGREGATE_REJECTED; BLOCKED; next NONE absent exact alternative; preserve UNKNOWN and forbidden reasons. UNKNOWN is not converted to FAIL/PASS.

O4 BLOCKED_WRITER + BLOCKED_CURRENTNESS/task superseded.
AGG-R3; NO_EFFECT; AGGREGATE_BLOCKED; BLOCKED; next CURRENTNESS_RECONCILIATION for this fixture because current task basis is invalid before a writer-dependent task can be established; preserve both reasons.

O5 BLOCKED_AUTHORITY + REJECT_PRECONDITION.
AGG-R2; REJECT; AGGREGATE_REJECTED; BLOCKED; next NONE absent exact precondition gate; preserve both.

O6 REJECT_FORBIDDEN + valid authority.
AGG-R2; REJECT; AGGREGATE_REJECTED; BLOCKED; NONE; preserve forbidden plus valid-authority evidence. Authority cannot defeat forbidden.

O7 UNKNOWN_REQUIRED_EVIDENCE + valid authority.
AGG-R4; NO_EFFECT; AGGREGATE_UNKNOWN; UNKNOWN; REQUEST_EVIDENCE; preserve unknown plus valid authority. Authority cannot promote unknown.

O8 BLOCKED_AUTHORITY + BLOCKED_WRITER + BLOCKED_CURRENTNESS.
AGG-R3; NO_EFFECT; AGGREGATE_BLOCKED; BLOCKED; CURRENTNESS_RECONCILIATION for this fixture because current task basis is invalid; preserve all blockers. Later gate revalidates remaining blockers.

O9 clean ADMIT, all bindings/preconditions/currentness valid.
AGG-R6; ADMIT; AGGREGATE_CLEAR; PASS for validator-admission criterion only; CAUSAL_NEXT_GATE to runtime one-safe-step guard. No task-completion/approval inference.

O10 REJECT_REDUNDANT_SELF_HANDOFF + otherwise valid context.
AGG-R2; REJECT; AGGREGATE_REJECTED; BLOCKED for proposed handoff; CAUSAL_NEXT_GATE to actual downstream gate from current decision, never redundant KOO self-handoff; preserve rejection and valid context.

All fixtures require explicit predicates plus aggregation object. No prose-only arbitration.
