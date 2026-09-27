# KOO → SHD: independent offline shard-store implementation review r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК r0.4
scope: INDEPENDENT_OFFLINE_STORAGE_INTEGRITY_REVIEW
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@b968b757d1ff0ae2f1f3e7f803c8ffb872d9b950:
entities/koordinator/outbox/KOO__authorize-SIS-SHD-operational-shard-store-offline-reviews-r01__OPERATOR.md

Exact KOD result:
puev5691/wellbeing-hq@6dee3d7b9df07769f48047cd5039a3b9a4b1d16b:
entities/koder/outbox/KOD__operational-shard-store-offline-implementation-test-r01__KOO.md
blob 1331db036213729bbca389183dac721123765143

Exact unchanged package:
puev5691/wellbeing-hq@a972227813ba2e2e495ea1e9d37f86a0028492d7:
entities/koder/outbox/operational-shard-store-offline-r01
tree d70d1eeff3843674ee31e75b86e2b2220e119614

Review only.

Focus:
- canonical OperationalRecordV1 bytes and identity;
- namespace/entity/task/version binding;
- PUT idempotency;
- CAS exact prior-pointer semantics;
- generation/parent invariants;
- fence rollover/stale-writer rejection;
- object/pointer/ledger consistency;
- orphan object vs broken pointer behavior;
- historical CAS resolution after later pointer advance;
- synthetic Git-anchor mismatch behavior;
- malformed identity/path handling;
- whether tests match the reviewed design without authority expansion.

Return:
PASS_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R01_WITH_BOUNDARIES
or exact BLOCKED_* / FAIL_* with critical issues only.

Do NOT:
- modify package;
- enable live WRITE/CAS;
- deploy;
- touch real shard roots;
- resume TERA/Telegram;
- claim CHECKPOINT_DURABLE;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result/readback to KOO, STOP.
