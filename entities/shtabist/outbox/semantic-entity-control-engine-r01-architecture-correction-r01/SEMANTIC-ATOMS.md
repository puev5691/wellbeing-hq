# SECE r0.1 — Semantic Atoms local C1/C2 precision
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
predecessor_blob: fa854994a7e2cbe626999f3bae0cf751de26897e

All predecessor atoms unchanged.

Local precision:
ACTION_INTENT now maps to action_id/action_class and requires ACTION_AUTHORIZATION_BINDING before authority-sensitive effect.
HANDOFF maps to explicit CAUSAL_EVENT with recipient/reason/causal requirement.
DELIVERY, RECEIPT, ACCEPTANCE remain distinct explicit event states.
ACTIVATION_ATTEMPT is explicitly not PROCESSING_STARTED.
CURRENT_STATE_EVIDENCE is an evidence structure, not a new semantic authority atom.
