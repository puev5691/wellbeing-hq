# R02 bounded correction map

## D1-A — PASS_STATIC_PURE_MOCK
- added canonical_root_identity_verdict()
- added canonical_binding_verdict()
- recomputes root_identity_id from nested payload
- recomputes binding_id from canonical binding payload excluding binding_id
- validates exact effect/adapter/confinement/cleanup/platform IDs and versions
- runtime_binding_verdict validates admitted and current bindings canonically
- SandboxBoundEffectIntentEmitter rejects noncanonical binding before base EffectIntent emission

## D1-B — PASS_STATIC_PURE_MOCK
- CREATED_SANDBOX_OBJECT_IDENTITY requires no_symlink_reparse_evidence
- output carries no_symlink_reparse_evidence
- created_identity_id digest binds that evidence

## D2-A — PASS_STATIC_PURE_MOCK
Cleanup eligibility now requires:
- state.operation_key == created.operation_key
- state.owner_attempt_id == created.attempt_id
- created.root_identity_id == binding.root_identity_id
- created.sandbox_target_id == binding.root_identity.sandbox_target_id
Mismatch => BLOCKED before cleanup-plan emission.

## P1 — PASS_STATIC_PURE_MOCK
platform_verdict validates:
- root_identity_class == DIRFD_STATX_DEV_INO_MNT_ID
- created_object_identity_class == RETAINED_FD_FSTAT_DEV_INO_MNT_ID
- cleanup_binding_class == DIRFD_UNLINKAT_PLUS_EXCLUSIVE_NAMESPACE_MUTATION_CONTROL
root_identity requires:
- platform_evidence_profile_id == LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01

## Tests/evidence hygiene — PASS
- all 22 predecessor sandbox pure/mock tests remain represented and passing
- 16 additional correction/negative/static-order tests added
- total 38/38 PASS
- top-level TEST-SUMMARY.json now names exact R02 correction attempt
- stale R04 top-level summary is not carried forward as current PASS evidence

Outcome fail-closed semantics and non-live boundary are preserved.
