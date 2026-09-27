# KOO → SIS: independent re-review offline shard-store r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН r0.6
scope: INDEPENDENT_CORRECTION_REREVIEW
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@4c79a82a373a4681de6ab75e0eccc677ddfb8760:
entities/koordinator/outbox/KOO__authorize-SIS-operational-shard-store-offline-r02-rereview__OPERATOR.md

Exact KOD result:
puev5691/wellbeing-hq@7307b3f0a1f90ec10bb7b1c15121b632847b43ba:
entities/koder/outbox/KOD__operational-shard-store-offline-correction-r02__KOO.md
blob ec067ef88e823cd5401fa1fc233e5e5d02149f53

Exact unchanged successor package:
puev5691/wellbeing-hq@9faa1ede62460fdcc073e48fd13b10f93027e957:
entities/koder/outbox/operational-shard-store-offline-r02
tree 8c5cb47ce3267dac4b1810e93cf993a35a3a0492

Predecessor SIS FAIL:
puev5691/wellbeing-hq@c312879df00575225dbefd72c0a842ec6e3fd969:
entities/sisadmin/outbox/SIS__operational-shard-store-offline-independent-review-r01__KOO.md
blob 60bf536b684d127960b169dccfdf9c9c1e0b2414
terminal FAIL_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R01_CONFLICT_OUTCOME_NOT_DURABLE

Verify specifically:
1. CAS CONFLICT is durably persisted before return;
2. exact request_digest + observed actual pointer are bound to the conflict outcome;
3. lost response resolves to the same durable CONFLICT;
4. historical conflicting op still resolves to original CONFLICT after later pointer advance;
5. crash injection before/after conflict-outcome commit behaves fail-closed;
6. same op_id + changed request remains idempotency conflict;
7. previously passing APPLIED/concurrency/crash boundaries remain intact;
8. exact package remains unchanged.

Return:
PASS_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R02_REREVIEW
or exact FAIL/BLOCKED with remaining critical defects only.

Do NOT:
- modify package;
- enable live WRITE/CAS;
- deploy;
- touch real shard roots;
- use Commander;
- claim CHECKPOINT_DURABLE;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
