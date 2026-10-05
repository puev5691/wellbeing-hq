# Sandbox Effect Class
status: DESIGN_ONLY

effect_class: SANDBOX_EPHEMERAL_FILE_CREATE
Meaningful real mutation: create one small marker/data file in an isolated disposable sandbox directory and read it back.
Synthetic: authority/task/context/adapter decision inputs may still be controlled test fixtures around the real filesystem mutation; the file creation/readback itself must be real in future G4.

Resource: exact future attempt-owned ephemeral directory, NOT selected here.
Maximum mutation: one new regular file, future G4 bounded size, exact name/path/payload.
Allowed: exclusive create + write + close + readback/stat/hash.
Forbidden: overwrite; delete before terminal evidence; symlink/hardlink traversal; parent mutation; executable bit; subprocess/service/network/provider/API/Telegram; repo/config/current-state/credential access.

Expected reversible state: remove only the exact attempt-owned file then exact attempt-owned directory after terminal evidence and review-preservation requirements.
Isolation proof: target ownership + initial absence/clean snapshot + canonical path containment + no symlink traversal + production deny-list/boundary + post-effect resource inventory.
