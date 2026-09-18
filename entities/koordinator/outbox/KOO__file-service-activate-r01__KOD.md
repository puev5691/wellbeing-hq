# KOO → KOD: activate File/Artifact Service MVP r0.1

status: ACTIVE_TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

Queued task:
`f1753621b1181f425b574f68fca36e3bc40d115a`

Direction:
`b62896ff271ab0480a4ff1fcecef386a7c65b1b6`

Activation condition is now satisfied:
- portal presentation fix terminal PASS:
  `2de740d46ebd788f32aa5f12eb15b824c2bae0f0`
- independent SHD reverify PASS:
  `dba9aded7a38f01398018e274e5e9550aecdfcff`

Execute the exact queued File/Artifact Service MVP task now.

Required boundaries remain unchanged:
- deterministic package assembly;
- SHA-256 / size / inventory;
- manifest;
- local readback;
- package diff;
- fail-closed identity mismatch;
- compact machine result;
- zero-network default tests;
- no authority/project-state semantics;
- no secrets;
- Git adapter disabled unless separately authorized;
- no Telegram/TERA2/portal state mutation;
- no GitHub publication from MVP execution path.

Expected:
`PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`
or exact blocker/fail.

Return immutable package/result to KOO through Exchange Gate and stop.
