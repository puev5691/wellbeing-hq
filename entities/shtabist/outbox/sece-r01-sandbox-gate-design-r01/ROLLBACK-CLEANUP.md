# Sandbox Rollback / Cleanup
status: DESIGN_ONLY

Rollback/cleanup preconditions:
terminal effect classification already durable OR explicit separately authorized evidence-preserving reconciliation permits cleanup;
exact target ownership proven;
cleanup scope exactly equals attempt-created resources;
no unresolved outcome whose evidence cleanup would destroy;
no foreign/pre-existing resource inside cleanup set.

Safe cleanup:
remove only exact created file and then exact attempt-owned empty directory; no recursive broad deletion by default.

Before cleanup preserve terminal/effect evidence and required hashes/inventory.
After cleanup read back target absence and parent boundary unchanged.

Cleanup failure => BLOCKED or FAIL only when exact cleanup criterion was executed and positively failed; ambiguous cleanup => UNKNOWN/UNRESOLVED.
Unknown rollback outcome => no repeated destructive cleanup; reconcile exact target state.
