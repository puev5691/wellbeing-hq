# RED → ARH: self-snapshot / recovery handoff r0.1

status: `READY_FOR_ARH_PRESERVATION`
project_time: omitted

KOO preservation checkpoint already exists:
- source task commit `999542a004cd1fb4bc6364ee24c6dd8aaee47ca7`
- ARH inbox placement commit `2f70ce273cf2b8bd4ead7ec5b26b256e5c72fec5`

Current RED writer is available and supplies its own self-state instead of requiring reconstruction.

## Exact source package

Self-snapshot:
- `entities/redaktor/current/recovery/RED__self-snapshot-r01.md`
- commit `e1706f28d2ff8253cf705d1c6833fda53ca503f1`
- blob `8cd01299fa06ab3ea42811ec1729affc6665922b`

Replacement initiation procedure:
- `entities/redaktor/current/recovery/RED__replacement-initiation-procedure-r01.md`
- commit `be6ab103a585f52d2133a6b57874765951ccb6f4`
- blob `5b47dd8f6ef731622ec3e31c55272b4521e8077c`

Recovery handoff manifest:
- `entities/redaktor/current/recovery/RED__recovery-handoff-manifest-r01.md`
- commit `7e6b728ffe7b41458008bd3f54d63672222c26c1`
- blob `aede272970c40d94a0de3ba9515cd0878ea73c93`

## Required action

Perform the preservation/recovery owner part of the approved canon:
- verify package provenance and exact identities;
- reconcile current RED evidence tail;
- publish refreshed external recovery package to the approved recovery contour;
- calculate/update checksums or other exact version identities;
- perform post-publication readback/verification;
- update recovery accounting;
- return exact PASS/BLOCKED/FAIL.

Do not reconstruct RED self-state, do not transfer RED writer automatically, and do not declare backup current before external publication + readback/version verification.

## Failure mode

If exact artifact identity cannot be verified or the external package cannot be published/read back exactly, keep the previous externally verified recovery as last confirmed and mark the new backup stale/pending rather than current.

---
WHO: RED / РЕДАКТОР current writer
PURPOSE: hand current self-snapshot to ARH preservation process
