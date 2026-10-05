# SECE r0.1 Sandbox Gate Design R01
status: DESIGN_ONLY
implementation: NOT_IMPLEMENTED
activation: NOT_ACTIVE

Purpose: define future G4 admission/execution contract for exactly one bounded real sandbox effect without production effect.

Sandbox environment class:
SECE_EPHEMERAL_ISOLATED_FILE_SANDBOX_R01.

Target identity model:
sandbox_target_id + environment_instance_id + owner_attempt_id + root_locator + creation_evidence + initial_absence_or_clean_snapshot + isolation_evidence + current_state_digest.
No concrete host/path is selected here. TARGET_SELECTION=UNKNOWN_LATER_GATE.

Isolation requirements:
- disposable attempt-owned workspace/resource;
- no production service/repository/current-state path;
- no existing project repository mutation;
- no credentials/secrets required;
- no shared writable dependency with production;
- clean start: target absent or exact empty/known snapshot established before attempt;
- exact target identity/currentness rechecked at admission and invocation;
- pre-existing unowned state => BLOCKED;
- production adjacency or ownership ambiguity => STOP.

State allowed before attempt: only gate-approved sandbox root parent and separately evidenced tooling/runtime prerequisites.
State required absent: target mutation object, unresolved prior effect for same target/effect key, production bindings, inherited credentials, pre-existing unowned payload.
