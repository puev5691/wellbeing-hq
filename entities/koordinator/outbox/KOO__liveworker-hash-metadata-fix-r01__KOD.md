# KOO → KOD: live-worker immutable hash metadata fix r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Independent blocker

SIS result:
`75c877679bb2ce2126a2934b50cc9caaddaaca71`

verdict:
`BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH`

## Important

The behavioral race blocker is independently closed.

Do NOT redesign the live-worker.
Do NOT alter behavior unless exact-byte reconciliation proves the published bytes were not intended.

## Exact current candidate

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-race-fix-r01/`

commit:
`6880f16459c5424992fcbe2102f0889142fe533a`

tree:
`81a23900c6437c8a76ee3f45cb451f319f3fdec2`

## Exact mismatch observed by SIS

Published blob:
`d276de1050fd54e836ed4fc879eb384dba3aa1f1`
file:
`live_worker.py`

Direct SHA-256 from exact Git blob bytes:
`175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`

Published MANIFEST/report claimed:
`631ad7e8e5bb12ddfed92d8a8c02c113dfc2b2dde18c848b6c69e739321e6835`

Published blob:
`e9a0d938e0eb7180fdc8336050a38347a477c2ed`
file:
`test_live_worker.py`

Direct SHA-256 from exact Git blob bytes:
`3eb5f2ff7c664f8a03cd3978636537aa8ab5c776dc44803c56799d779f0c5ad0`

Published MANIFEST/report claimed:
`920023253409bc5bc8d685cb66c51f1dffc05c314ea38700b080e3669c6bdc74`

## Required correction

1. Fetch exact Git blob bytes by immutable blob identity.
2. Compute SHA-256 directly from those exact bytes.
3. Reconcile all package metadata and report values to the exact Git bytes.
4. If code/test bytes are already intended, do not change them; publish corrected metadata in a new immutable package/version.
5. If intended bytes differ, publish a new corrected candidate and explain exact delta.
6. Preserve independently verified race-fix behavior.
7. Re-run package tests after final package composition.
8. Return exact commit/tree/blob/SHA identities.

Do not:
- perform live provider calls;
- read/create credentials;
- mutate account/billing;
- deploy production;
- change unrelated gateway/provider/Telegram/portal paths.

Expected:
`PASS_LIVEWORKER_HASH_METADATA_FIX_R01_READY_FOR_REVERIFY`
or exact blocker/fail.

Return new immutable package/result to KOO through Exchange Gate and stop.
