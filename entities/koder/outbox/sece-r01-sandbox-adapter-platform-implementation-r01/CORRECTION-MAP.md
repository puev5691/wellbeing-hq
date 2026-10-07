# R04 correction map

Variant B selected: separate TASK_EXECUTION_BINDING, because actor/writer/Recovery grounding already passed independent review.

Mandatory fields:
- task_ref
- task_authority_basis_ref
- task_authority_state
- task_currentness
- task_supersession_state

Each is derived from exact authoritative evidence with immutable locator/version, VERIFIED, CURRENT evidence state, conflict NONE and provenance.

Eligibility requires:
AUTHORIZED + CURRENT + NONE/NOT_SUPERSEDED + RESOLVED grounding.

Binding and supporting evidence versions flow through:
RUNTIME_EVIDENCE_RESOLUTION -> Effective Context/Contract -> EffectIntent -> PRE_EFFECT_ADMISSION -> invocation frontier.

Missing/UNKNOWN/conflict/superseded/wrong identity => no intent/admission.
Drift before or after admission => NO_EFFECT / NOT_EXECUTED.
