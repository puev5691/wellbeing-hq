# KOO → SIS: STP-C degraded freshness/currentness design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: DOCUMENT_ONLY_SECURITY_POLICY_DESIGN
project_time: omitted

Resume-First.

Current SIS writer:
puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Exact authority:
puev5691/wellbeing-hq@c0d6c157c7d1ebb9ba7b304d10def6f8fb48ade4:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-degraded-freshness-currentness-design-r01__OPERATOR.md

Exact SHD review:
puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md
blob 6efd2cb71d8ff6be248f1c2abc33ac39ccb4f6fa

Exact reviewed SIS candidate:
puev5691/wellbeing-hq@fa10f156589d30a187fa529c3975517d8c1bdbc7:
entities/sisadmin/outbox/SIS__STP-C-per-seat-key-storage-design-r02__KOO.md
blob 7d9ebcb8069379a4fd068ddb2a9cff1a015929fc

Design only the unresolved freshness/currentness policy for prolonged Git outage.

Current candidate allows degraded signing from the last verified ACTIVE local key-state until Git returns.
SHD found this conceptually coherent but implementation-incomplete because it creates an unbounded stale-authority window.

Required analysis:

1. Identify the exact risk:
- revocation/supersession may exist canonically while isolated signer cannot see it;
- post-recovery reconciliation cannot undo irreversible side effects already executed.

2. Compare bounded policy families without selecting arbitrary numbers:
- F1: hard freshness TTL/window, after which new signing stops;
- F2: degraded signing may continue, but only for reversible/non-effecting decisions until reconciliation;
- F3: hybrid policy, with shorter/stricter rules for effect-producing actions and broader VERIFY-only allowance;
- F4: explicit OPERATOR acceptance of indefinite degraded signing with a strict no-irreversible-effect boundary.

You may propose a reviewed derivative if needed.

3. For each family state:
- availability impact;
- stale-authority risk;
- what remains allowed after freshness expires;
- what is blocked;
- whether OPERATOR intervention is required;
- what evidence is needed before choosing any numeric interval.

4. Define currentness states, at minimum:
CURRENT
DEGRADED_CURRENT
FRESHNESS_EXPIRED
CURRENTNESS_UNKNOWN
CANONICAL_CONFLICT
and their effect on:
- VERIFY;
- new seat signing;
- quorum counting;
- effect execution;
- rotation/revocation/successor activation.

5. Hard invariants:
- UNKNOWN never becomes allow;
- expired freshness never silently resets;
- no local replica can extend its own validity;
- no new key-governance changes during Git outage;
- signature validity != effect authority;
- irreversible effects require separately valid effect/currentness conditions.

6. Do not choose a numeric timeout unless current project evidence supports one.
If no evidence supports a number, say NUMERIC_FRESHNESS_INTERVAL_UNKNOWN and specify what runtime/availability evidence would be needed.

7. Produce one bounded OPERATOR decision table:
policy family -> consequence -> evidence needed -> residual risk.

Do not design the anti-replay/TOCTOU/effect-binding contract in this task beyond identifying its dependency on the chosen currentness policy.

Expected terminal:
PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R01_READY_FOR_OPERATOR_DECISION
or exact BLOCKED_/FAIL_.

Do NOT:
- generate keys;
- create credentials;
- mutate hosts;
- deploy;
- activate Fast Gate/profile;
- live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
