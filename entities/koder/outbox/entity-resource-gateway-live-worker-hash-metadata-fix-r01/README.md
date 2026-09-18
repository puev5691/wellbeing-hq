# Live-worker immutable hash metadata fix r0.1

This package corrects immutable SHA-256 metadata only.

Behavioral race blocker is already independently closed by SIS. The worker and test source bytes are intentionally unchanged from the race-fix candidate.

## Exact reused source bytes

- live_worker.py Git blob: `d276de1050fd54e836ed4fc879eb384dba3aa1f1`
  - direct SHA-256 from Git blob API bytes: `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`
- test_live_worker.py Git blob: `e9a0d938e0eb7180fdc8336050a38347a477c2ed`
  - direct SHA-256 from Git blob API bytes: `3eb5f2ff7c664f8a03cd3978636537aa8ab5c776dc44803c56799d779f0c5ad0`

These are the exact bytes independently reverified by SIS.

## Source lineage

Blocked metadata package:
- commit `6880f16459c5424992fcbe2102f0889142fe533a`
- tree `81a23900c6437c8a76ee3f45cb451f319f3fdec2`

Independent blocker:
- commit `75c877679bb2ce2126a2934b50cc9caaddaaca71`
- verdict `BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH`

Exact corrective task:
- commit `628ff93bc70aab8ed77556cc3d216df180cf43fc`
- path `entities/koordinator/outbox/KOO__liveworker-hash-metadata-fix-r01__KOD.md`

## Scope

No worker redesign. No behavior delta. No provider call. No credential read/create. No account/billing mutation. No production deployment.

Final package tests must be rerun from the immutable package after publication. Their evidence is returned in the KOD terminal report and Exchange Gate result.

Expected terminal result:
`PASS_LIVEWORKER_HASH_METADATA_FIX_R01_READY_FOR_REVERIFY`.
