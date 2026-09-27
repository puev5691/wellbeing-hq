# KOO record: OPERATOR authorizes offline shard-store correction r0.2

status: OPERATOR_CORRECTION_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR explicitly instructed KOO to route the smallest correction-only task to KOD after the independent SIS and SHD FAIL results.

Scope:
correct only the two independently verified defects in offline synthetic shard-store r0.1.

SIS FAIL:
puev5691/wellbeing-hq@c312879df00575225dbefd72c0a842ec6e3fd969:
entities/sisadmin/outbox/SIS__operational-shard-store-offline-independent-review-r01__KOO.md
blob 60bf536b684d127960b169dccfdf9c9c1e0b2414
terminal FAIL_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R01_CONFLICT_OUTCOME_NOT_DURABLE

SHD FAIL:
puev5691/wellbeing-hq@f4182c49e9f19fd6925c7e5011743b377a21b96d:
entities/shardovik/outbox/SHD__operational-shard-store-offline-independent-review-r01__KOO.md
terminal FAIL_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R01_LEDGER_RESOLUTION_FAIL_OPEN

Authorized:
- correction-only offline/synthetic implementation;
- regression tests;
- immutable successor package;
- result to KOO.

Not authorized:
- live WRITE/CAS;
- deployment;
- real shard roots;
- Commander;
- trust-root/backend/operator appointment;
- CHECKPOINT_DURABLE;
- EOM pilot;
- memory-layering attempt 3.
