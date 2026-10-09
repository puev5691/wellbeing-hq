# Implementation map

EphemeralFileSandboxEffectAdapterR01:
- sandbox_effect.py
- pre-effect deterministic fail-closed classifier
- exclusive-create primitive plan only; no syscall execution in this candidate
- created-object identity schema and outcome classification

SECE_SANDBOX_CONFINEMENT_PROFILE_R02:
- sandbox_profile.py
- exact basename grammar
- anchored root identity validation
- platform evidence capability validation
- deterministic binding identity

OBJECT_BOUND_CLEANUP_R02:
- sandbox_effect.py
- terminal/outcome/root/parent/current-leaf/ownership/profile rechecks
- cleanup plan is anchored-relative only
- unresolved identity/outcome => UNRESOLVED
- unavailable strong cleanup proof => BLOCKED/UNKNOWN, never weaker fallback

Linux/POSIX profile:
- LINUX-POSIX-PLATFORM-EVIDENCE-PROFILE-R01.json
- private attempt-owned tmpfs mount namespace
- no foreign writer access
- exclusive namespace mutation control
- serialized effect executor
- anchored dirfd
- openat2 + RESOLVE_BENEATH/NO_SYMLINKS/NO_MAGICLINKS/NO_XDEV
- O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC
- retained fd + fstat/statx dev/ino/mount identity
- fd-bound readback/hash
- unlinkat relative to anchored dirfd
- pre-unlink identity revalidation and anchored post-cleanup absence

Runtime integration:
- sandbox_runtime_integration.py wraps exact reviewed R04 EffectIntentEmitter / PreEffectRevalidator / EffectBoundaryVerifier
- sandbox binding ID/profile/adapter/platform identities and supporting evidence versions are added to intent/admission/invocation checks
- R04 source remains unchanged.
