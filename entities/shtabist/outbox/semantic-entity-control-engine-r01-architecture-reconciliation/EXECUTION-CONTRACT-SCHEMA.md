# SECE_EXECUTION_CONTRACT_R01
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

Required:
contract_id; schema_version; derived_event_ref;
ENTITY; INSTANCE; ROLE_PROFILE; CAPABILITIES;
CURRENT_STATE {writer_requirement, writer_state, task_currentness, supersession_state, blockers};
TASK_IDENTITY {task_ref, task_version, task_status};
AUTHORITY_BASIS[] {authority_ref, scope, action_classes, currentness};
SOURCE_SET[] {locator, version_blob, active_status, semantic_basis};
INPUTS[] {input_id, exact_identity, required, verified_state};
PROFILE {profile_id, selection_basis};
EXPERIENCE_SET[] {ref, provenance, applicability, freshness, reason_loaded, advisory_only:true};
ALLOWED_ACTIONS[]; FORBIDDEN_ACTIONS[]; REQUIRED_PRECONDITIONS[]; STOP_IF[];
EXPECTED_RESULT; EXPECTED_TERMINAL[]; NEXT_GATE_RULE[]; PROVENANCE[];
VALIDATION_STATE {static_validation, unresolved_unknowns[], conflicts[]};
HUMAN_CAUSAL_VIEW {checked, known, unknown, authorized, forbidden, observed, significance, next_action}.

Invariants:
contract is derived, not authority;
authority-sensitive ALLOWED action traces to active rule + exact authority;
FORBIDDEN defeats helpful proposal;
required UNKNOWN blocks dependent effect;
experience/profile cannot populate AUTHORITY_BASIS;
human view is rendered from contract/result, not parallel truth.
