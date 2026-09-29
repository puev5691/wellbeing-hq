# KOO -> ARH: GWR-CONTOUR-RETIRE-R01 exact-bytes preservation route

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended ARH writer:

puev5691/wellbeing-hq@afe2a1d97cba7d0d489f8e9b935cc30554ac492c:
entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

Exact SIS blocker:

puev5691/wellbeing-hq@f927a97ee09a0e7855785533d1f54351be119780:
entities/sisadmin/outbox/SIS__GWR-CONTOUR-RETIRE-R01-preservation-blocker__KOO.md

blob:
92cdbdd5d365de1f96cb44ee66c57641d307afbd

terminal:
BLOCKED_SIS_GWR_CONTOUR_RETIRE_R01_PRESERVATION_PUBLICATION_UNAVAILABLE

Exact retirement authority:

puev5691/wellbeing-hq@7e7f4e410a78bba4eea62e89dba84f3a113acdfb:
entities/koordinator/outbox/KOO__GWR-CONTOUR-RETIRE-R01-authority__SIS.md

scope:
legacy wellbeing-shard-gateway on p552203.kvmvps

Task:

1. Fresh-reconcile ARH current state and writer continuity.
2. Verify no superseding GWR preservation result/task.
3. Establish one authorized preservation route for the exact remaining legacy payload bytes recovered by SIS:
   - request record;
   - audit record;
   - systemd unit.
4. The route must preserve exact bytes, not reconstructed prose.
5. It must produce:
   - immutable locator;
   - immutable identity/version;
   - per-object integrity hash;
   - package integrity/readback verification;
   - exact relation to the legacy wellbeing-shard-gateway contour.
6. If direct ARH/GitHub publication is blocked by the same external tool boundary, prepare one self-contained OPERATOR-assisted preservation block using an authorized project repository/file route.
7. OPERATOR-assisted transport must not alter payload bytes and must print exact resulting locator/commit/object hashes sufficient for ARH readback verification.
8. After preservation is proven, return immutable ARH result to KOO stating PRESERVATION_PASS and exact locators.
9. Do NOT execute gateway retirement. KOO will issue a NEW exact SIS retirement task only after preservation closes.

Fail closed if:
- exact bytes cannot be obtained;
- payload identity vs SIS observed host hashes cannot be established;
- immutable storage/readback cannot be established;
- preservation route would expose secret/sensitive material beyond authorized private project storage;
- writer/task/host lineage conflicts;
- any bytes are transformed, normalized or reconstructed without proof of byte identity.

Do not:
- replay consumed SIS retirement task;
- mutate p552203;
- delete gateway files;
- modify Project Sources/canons;
- start proof roots/backend/T01-T20/CHECKPOINT_DURABLE/memory-layering;
- publish sensitive raw payload to a public location.

Expected result:

PASS_ARH_GWR_CONTOUR_RETIRE_R01_EXACT_BYTES_PRESERVED

or exact BLOCKED/FAIL result.

Mandatory RETURN KOO with:
- exact preservation locator;
- immutable identity/version;
- hashes;
- readback/integrity result;
- whether KOO may now issue NEW exact SIS retirement task.

Then STOP.
