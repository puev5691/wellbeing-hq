# KOO → SHD: independent technical review of STP-C key storage/recovery r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК
scope: INDEPENDENT_DOCUMENT_ONLY_CROSS_LAYER_TECHNICAL_REVIEW
project_time: omitted

Resume-First.

Current authoritative SHD writer:

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

Writer Gate result:

puev5691/wellbeing-hq@0b18917db27b81994e2de08963988812eff1728f:
entities/shardovik/outbox/SHD__replacement-r04-writer-gate-result__KOO.md

Exact authority:

puev5691/wellbeing-hq@4103001a9bf46bcc9da6d03ec36dc417e1251bfd:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-key-storage-r02-independent-review__OPERATOR.md

Exact candidate:

puev5691/wellbeing-hq@fa10f156589d30a187fa529c3975517d8c1bdbc7:
entities/sisadmin/outbox/SIS__STP-C-per-seat-key-storage-design-r02__KOO.md

blob:
7d9ebcb8069379a4fd068ddb2a9cff1a015929fc

Review only the r0.2 technical/cross-layer consistency.

Check at minimum:

1. Three-host / three-key isolation
- one seat key per host;
- no cross-seat key reuse;
- host/account availability does not become authority;
- shared hosting-account facts are not overstated as full independence.

2. No-private-key-restore recovery
- lost key cannot silently return;
- successor key does not inherit authority without exact public binding + readback + separate activation;
- historical signatures remain attributable.

3. Git canonical public-key history
- local replicas cannot promote themselves to canonical;
- pinned history/currentness semantics are coherent;
- Git publication/readback does not itself mint seat authority.

4. Git-outage degraded mode
- VERIFY and new signing under last verified ACTIVE key-state do not silently become authority expansion;
- no rotation/revocation/successor/seat-binding change during outage;
- outage decisions bind exact local snapshot identity;
- no fail-open from UNKNOWN state.

5. Long outage risk
- examine whether unlimited degraded duration creates an unbounded stale-authority window;
- identify whether this is acceptable only as explicit residual risk or requires a bounded freshness rule before implementation.
Do not choose a timeout unless supported.

6. Post-recovery reconciliation
- exact canonical state is reloaded before normal continuation;
- outage signatures invalidated by canonical state become BLOCKED_PENDING_CONFLICT_REVIEW;
- no silent accept/discard.

7. Disputed-signature review
- disputed seat does not vote on itself;
- two remaining seats review;
- OPERATOR arbitration only on disagreement;
- confirm this does not accidentally create a new quorum/authority path for unrelated decisions.

8. Key state machine
- ACTIVE / DEGRADED_ACTIVE / ROTATION_PENDING / SUPERSEDED / REVOKED / LOST_OR_UNKNOWN / RECOVERY_PENDING transitions are closed and non-circular;
- no state transition creates seat authority by key possession alone.

9. TOCTOU / replay / stale-state boundaries
- identify required future exact binding between decision digest, key_id, seat_id, snapshot identity, currentness and effect boundary;
- flag any missing atomicity/replay requirements.

10. Implementation-readiness boundary
- distinguish what r0.2 already establishes conceptually from what remains mandatory before any implementation design:
  host mapping, algorithm/key format, OS/runtime isolation, API contract, public-key schema, degraded snapshot format, reconciliation state machine, network/access boundary.

Return one terminal:

PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES

or exact FAIL_/BLOCKED_ with only critical defects.

Do NOT:
- modify candidate;
- generate keys;
- handle secret material;
- select algorithms/products by convenience;
- mutate hosts;
- deploy;
- activate Fast Gate/profile;
- live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
