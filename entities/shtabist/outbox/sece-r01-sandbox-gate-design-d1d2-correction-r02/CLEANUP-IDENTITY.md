# D2 Object-bound Cleanup R02
status: DESIGN_ONLY

Cleanup eligibility:
required terminal/effect evidence durable;
effect outcome != UNRESOLVED;
exact anchored root identity current;
CREATED_SANDBOX_OBJECT_IDENTITY available;
attempt ownership proven;
cleanup scope separately bound;
confinement profile exact version bound.
Otherwise NO AUTOMATIC CLEANUP.

Immediately before file removal revalidate:
anchored root identity == admitted/current root identity;
expected parent identity unchanged;
current leaf object identity == CREATED_SANDBOX_OBJECT_IDENTITY;
leaf still regular file;
no symlink/reparse substitution;
attempt ownership matches;
operation_key exact match;
no unresolved effect/outcome;
platform evidence profile still sufficient.

Mismatch/ambiguity => NO DELETE.
Known unmet precondition => BLOCKED.
Missing evidence => UNKNOWN.
Possible post-mutation identity/outcome ambiguity => UNRESOLVED.

Removal semantics:
remove/unlink exact leaf relative to the same anchored root/parent object using platform-equivalent object-bound primitive.
No destructive re-resolution from absolute pathname.
No recursive fallback.
No wildcard.
No removal outside exact attempt-owned leaf.
If platform cannot bind deletion to the verified object strongly enough, cleanup is BLOCKED/UNKNOWN; do not substitute a weaker path-only delete.

Directory cleanup:
before removing attempt-owned sandbox directory require exact directory object identity; exact owner_attempt_id; expected parent object identity; directory empty proof through anchored/object-bound observation; no foreign entry; no unresolved object/effect; no identity drift.
Non-empty/ambiguous => no recursive cleanup; BLOCKED/UNKNOWN.

Post-cleanup:
through same anchored boundary prove exact leaf absent; if authorized, exact attempt directory absent; parent/root object identity unchanged; no unexpected sibling/parent mutation within declared observation scope.
Path text alone insufficient.

Ambiguous cleanup command/transport:
do not retry destructively;
preserve all evidence;
cleanup_outcome=UNKNOWN;
require separately authorized read-only reconciliation;
no clean-state claim until proved.
