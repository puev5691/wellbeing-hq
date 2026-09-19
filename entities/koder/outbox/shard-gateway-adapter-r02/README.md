# Shard gateway adapter r0.2 security correction

Successor of immutable r0.1. This package changes only the four defects identified by SIS plus tests/docs/manifest evidence.

## C1 wall-time

Every opcode executes under a real process-local wall deadline. Limits remain: default 10 s, SHA256 60 s, ARCHIVE_LIST 20 s, Git 15 s. Git subprocess timeout remains as a second layer. The candidate is Linux-oriented; a non-main-thread/non-setitimer execution path fails closed instead of silently dropping the deadline.

## C2 no-follow / TOCTOU

Filesystem operations traverse from an allowlisted root directory descriptor using `dir_fd` plus `O_NOFOLLOW`; intermediate components require `O_DIRECTORY`. READ_BOUNDED, SHA256 and ARCHIVE_LIST consume an already-open descriptor, so a post-validation pathname swap cannot redirect bytes to a new symlink target. STAT and LIST_DIR use the same descriptor boundary. A deterministic pre-open symlink-swap test verifies no secret target bytes are read.

## C3 Git ref boundary

One shared `validate_git_ref()` is used by GIT_LS_TREE, GIT_BLOB_META and GIT_BLOB_READ_BOUNDED. It accepts only `HEAD` or a full lowercase 40-hex commit proven by `git merge-base --is-ancestor <commit> HEAD`. Symbolic, malformed and unreachable refs fail as `REF_NOT_ALLOWED`.

## C4 final result size and text decoding

The 1 MiB cap is checked on the final canonical serialized `Result`, not only raw read/subprocess bytes. JSON escaping expansion therefore cannot bypass the boundary. Invalid UTF-8/binary text produces stable `BINARY_TEXT_NOT_ALLOWED`.

## Preserved r0.1 boundaries

Exact VERIFY opcode allowlist and mazhor/burzh root mappings are unchanged. WRITE remains `WRITE_MODE_NOT_AUTHORIZED`. There is no free-form shell, shell interpolation, automatic cross-host failover, deployment, credential access, listener exposure, or repository/archive/shard mutation. Request limit remains 32 KiB, directory/archive entry caps remain, concurrency stays one per host, and audit schema stays `wb.shard_gateway.audit.v1`.

This remains a non-deploying candidate. SIS exact-byte independent re-verification is the next gate. ARH acceptance remains blocked until SIS r0.2 PASS.
