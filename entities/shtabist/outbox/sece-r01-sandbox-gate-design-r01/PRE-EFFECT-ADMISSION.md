# Sandbox PRE_EFFECT_ADMISSION
status: DESIGN_ONLY

Admission binds:
attempt_id; task binding/evidence versions; candidate commit/tree/path/relevant blobs; EffectIntent id/payload digest; contract/context ids; action/effect class/scope; adapter class; adapter/effect authority; sandbox target identity/current-state digest; actor/writer/Recovery evidence; policy/source dependencies; prior-effect state; exact evidence frontier; rollback boundary identity.

verdict: ADMIT_EFFECT_NOW | NO_EFFECT_UNKNOWN | NO_EFFECT_BLOCKED | NO_EFFECT_STOP | NO_EFFECT_REJECT.

Any missing/mismatch/stale/conflict/supersession => not ADMIT.

Invocation boundary immediately before mutation MUST independently compare current evidence frontier to admission:
task; writer/Recovery; candidate/tree/blobs; adapter authority; target identity/state; policy/currentness; prior-effect state; intent/contract/context.

Any drift => NOT_EXECUTED. Admission alone is insufficient.
No wall-clock freshness proxy. No exactly-once claim.
