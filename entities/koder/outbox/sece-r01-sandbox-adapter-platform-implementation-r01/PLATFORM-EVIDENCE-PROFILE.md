# Linux/POSIX platform evidence profile candidate

profile_id: LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01
profile_version: R01
status: IMPLEMENTATION_CANDIDATE_NOT_ACTIVE

This is a platform evidence model, not a selected target.

Required future evidence includes exact versions/identities proving:
private mount namespace; attempt-owned private tmpfs; no bind exposure; no foreign writer access; exclusive namespace mutation control; serialized effect executor; anchored root dirfd; openat2 relative semantics; RESOLVE_BENEATH; RESOLVE_NO_SYMLINKS; RESOLVE_NO_MAGICLINKS; RESOLVE_NO_XDEV; O_CREAT; O_EXCL; O_NOFOLLOW; O_CLOEXEC; retained created fd; fstat dev/ino; statx mount-id; regular-file proof; link-count/replacement evidence; fd readback/hash; unlinkat dirfd; pre-unlink identity revalidation; anchored post-unlink absence; root/parent identity revalidation; anchored empty-directory proof; no recursive cleanup.

Unsupported, missing, stale, conflicted or unprovable capability => BLOCKED.
No optimistic fallback exists.
