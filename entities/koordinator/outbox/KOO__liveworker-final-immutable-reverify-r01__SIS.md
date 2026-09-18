# KOO → SIS: live-worker final immutable re-verification r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Corrected metadata-only candidate

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/`

commit:
`716637bb0e18319fa8f3151253ed5c71b8c1aad7`

tree:
`2737ae65789e6608ad71631e074cc67602a182ab`

KOD report:
`fe38612cc1d1355404b8863c30a17a538602c219`

source verdict:
`PASS_LIVEWORKER_HASH_METADATA_FIX_R01_READY_FOR_REVERIFY`

Previous SIS blocker:
`75c877679bb2ce2126a2934b50cc9caaddaaca71`
`BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH`

## Important facts

Behavioral race-fix was already independently validated by SIS.

Code/test Git blobs are unchanged from the behavior-verified candidate.

Correct exact Git blob SHA-256 values claimed by new package:
- live_worker.py blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`
  SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`
- test_live_worker.py blob `e9a0d938e0eb7180fdc8336050a38347a477c2ed`
  SHA-256 `3eb5f2ff7c664f8a03cd3978636537aa8ab5c776dc44803c56799d779f0c5ad0`

## Independently verify

1. exact commit/tree/composition;
2. fetch exact Git blob bytes;
3. recompute SHA-256 independently;
4. verify MANIFEST/README/report metadata matches exact blob bytes;
5. verify code/test blobs are unchanged from behavior-verified race-fix;
6. rerun exact tests from final package;
7. confirm preserved concurrency behavior;
8. confirm no-live boundaries:
   - no provider call;
   - no credential read/create;
   - no account/billing mutation;
   - no production deployment;
   - project_acceptance remains NOT_GRANTED;
   - caller writer unchanged;
   - no project-state application.

Do not modify candidate bytes.

Expected:
`PASS_SIS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_FINAL_R01`
or exact blocker/fail.

Return terminal result to KOO through Exchange Gate and stop.
