# G5 Independent Sandbox Review Requirements
status: DESIGN_ONLY

Reviewer must verify exact:
candidate commit/tree/blobs; G4 authority; task/currentness; adapter/effect class; target identity/ownership/isolation; PROCESSING_STARTED; preflight/checkpoint; PRE_EFFECT_INTENT; PRE_EFFECT_ADMISSION; invocation-boundary evidence; actual EffectOutcome evidence; unresolved/replay handling; terminal; rollback/cleanup evidence; post-cleanup readback; no production spillover; correct PASS/BLOCKED/FAIL/UNKNOWN classification.

Review must distinguish publication/dispatch from execution and intent from effect.
G5 PASS cannot create G6 authority.
