# SECE r0.1 Collision and Correction
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

Collision classes:
DIRECT_NORM_CONFLICT
SCOPE_OVERLAP_CONFLICT
AUTHORITY_CONFLICT
CURRENT_STATE_CONFLICT
SOURCE_STATUS_CONFLICT
TASK_CURRENTNESS_CONFLICT
EVIDENCE_CONFLICT
PROFILE_CONSTRAINT_CONFLICT
EXPERIENCE_CONFLICT_WITH_RULE
HUMAN_INPUT_CONFLICT_WITH_VERIFIED_EVIDENCE
UNKNOWN_REQUIRED_EVIDENCE
SUPERSESSION_REFINEMENT

Difference in independent scopes is not conflict.

Correction rules:
active-source conflict => STOP/block dependent effect only in exact affected scope;
FORBIDDEN => remove/mark forbidden action in affected action-space;
authority absence => authority-sensitive actions non-executable in exact scope;
verified delta may refine/supersede older evidence only exact scope;
UNKNOWN => preserve uncertainty + evidence requirement;
profile/experience/capability never create authority;
experience conflicting with active rule remains advisory/history but loses for affected decision;
human input cannot overwrite verified state unless itself valid authorized decision/evidence;
unrelated lines remain unchanged.

Each correction records correction_id, collision_id/type, affected_scope, affected_atom/binding ids, transformation, retained facts, provenance, unresolved state.

No correction silently rewrites prior context.
