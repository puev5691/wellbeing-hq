# R02 Rollback/Cleanup
status: DESIGN_ONLY

R01 cleanup safety retained and replaced where necessary by OBJECT_BOUND_CLEANUP_R02.

File removal requires immediate root/parent and CREATED_SANDBOX_OBJECT_IDENTITY revalidation, regular-file/no-reparse proof, ownership, operation-key match and resolved effect state.

Deletion is relative/object-bound to anchored parent/root or platform-equivalent; no absolute re-resolution, wildcard, recursive fallback or weaker pathname-only substitute.

Directory removal requires exact directory identity/ownership/parent identity + empty/no-foreign-entry proof.

Post-cleanup absence is proven through the same anchored boundary and parent/root identity is reverified.

Ambiguous cleanup => UNKNOWN, preserve evidence, no destructive retry.
