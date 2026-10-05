# R02 D1/D2 dependency plumbing into PRE_EFFECT_ADMISSION
status: DESIGN_ONLY

All R01 admission semantics preserved.

Add mandatory:
confinement_profile_id=SECE_SANDBOX_CONFINEMENT_PROFILE_R02;
confinement_profile_version;
platform_evidence_profile_id/version;
SANDBOX_ROOT_OBJECT_IDENTITY + currentness evidence version;
exact accepted leaf_name;
created_object_identity_requirement=MANDATORY;
cleanup_identity_profile=OBJECT_BOUND_CLEANUP_R02.

Admission is NO_EFFECT_BLOCKED/UNKNOWN unless anchored root identity and platform evidence profile can prove the required confinement semantics.

Invocation revalidates exact anchored root/parent object identity, target/currentness, confinement profile version and platform evidence capability immediately before create.

Same pathname with different root object identity => NOT_EXECUTED.
