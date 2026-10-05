# Candidate Sandbox EffectAdapter
status: DESIGN_CANDIDATE_NOT_AUTHORITY
implementation: NOT_IMPLEMENTED

class_id: EphemeralFileSandboxEffectAdapterR01
accepted_intent_class: SANDBOX_FILE_MARKER_CREATE_R01
effect_class: SANDBOX_EPHEMERAL_FILE_CREATE
allowed_scope: one exact attempt-owned sandbox target + one exact relative file name.

Input:
exact EffectIntent; PRE_EFFECT_ADMISSION; invocation evidence frontier; target identity; exact UTF-8 payload digest/bytes bounded by future G4 authority.

Adapter authority must separately bind class_id, effect_class, target_id, attempt_id, candidate/tree and maximum mutation.

Operation: exclusive create of one previously absent regular file under exact sandbox root. No overwrite, append, delete, chmod/chown, symlink following, command execution, network, service or repository mutation.

Output: EffectOutcome carrier only.

Idempotency/replay:
operation key = attempt_id + target_id + relative_path + payload_digest.
No blind retry.
If same key already has evidenced success, no second mutation.
If target file exists without matching evidenced outcome => UNRESOLVED/STOP.
Overlapping unresolved effect => replay prohibited.
