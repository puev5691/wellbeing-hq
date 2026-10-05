# EphemeralFileSandboxEffectAdapterR01 — R02 corrected design
status: DESIGN_CANDIDATE_NOT_AUTHORITY
implementation: NOT_IMPLEMENTED
effect_class: SANDBOX_EPHEMERAL_FILE_CREATE

R01 authority/effect containment unchanged.

New mandatory confinement binding:
SECE_SANDBOX_CONFINEMENT_PROFILE_R02.

Adapter accepts only one exact admitted basename component and an anchored SANDBOX_ROOT_OBJECT_IDENTITY.

Creation must satisfy profile race-safe semantics and return CREATED_SANDBOX_OBJECT_IDENTITY from the actual created/open object.

Adapter must keep same-object continuity through write/stat/readback/hash/outcome. No unanchored path fallback.

If confinement cannot be proved before mutation => NOT_EXECUTED/BLOCKED.
If continuity is lost after mutation may have occurred => UNRESOLVED.

Cleanup is not adapter free-form behavior; it must obey OBJECT_BOUND_CLEANUP_R02.
