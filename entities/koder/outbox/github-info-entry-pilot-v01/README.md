# Bounded GitHub information-entry pilot v0.1

Status: candidate / pilot only. Production: no.

This package implements a minimal Stage B state-model verifier:
- explicit machine-readable schema;
- fail-closed validator;
- one positive synthetic fixture;
- four negative fixtures: candidate/unknown, blocked, superseded, secret-like;
- static local preview;
- reproducible tests.

Boundary: preview/rendering/indexing cannot upgrade any missing, blocked, unknown, superseded, secret-sensitive, or unauthorized dimension into `public_ready=true`.

No repository settings, Pages/DNS, public release authority, Project Sources, credentials, or other Entities' current/recovery are modified.
