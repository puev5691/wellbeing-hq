# KOO → SHD: independent review STP-C anti-replay / TOCTOU / effect-binding r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК
scope: INDEPENDENT_DOCUMENT_ONLY_CROSS_LAYER_SECURITY_REVIEW
project_time: omitted

Resume-First.

Current authoritative SHD writer:

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

Writer Gate result:

puev5691/wellbeing-hq@0b18917db27b81994e2de08963988812eff1728f:
entities/shardovik/outbox/SHD__replacement-r04-writer-gate-result__KOO.md

Exact authority:

puev5691/wellbeing-hq@e8c6106e34171206eb17c107591fe704c82d406a:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-anti-replay-effect-binding-independent-review-r01__OPERATOR.md

Exact candidate:

puev5691/wellbeing-hq@f8091f94ec31f4b9937d9cd41096e4b1a255fde4:
entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md

blob:
3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8

Exact freshness/currentness boundary:

puev5691/wellbeing-hq@ca13d99e6bfe385d184f2e5ebfbe40309bd35e2f:
entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r02__KOO.md

blob:
ecbeeda215fd3418503bdf947f79ddc8bbc7c3a8

Prior SHD key-storage review:

puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md

Review only. Do not modify candidate.

Check at minimum:

1. Closed-schema completeness
- authority/effect-changing fields are all inside signed/hashed scope;
- no mutable semantic field can alter effect outside decision_digest/request_digest/effect_boundary;
- unknown fields/types fail closed.

2. Request identity / replay
- identical request replay is deterministic/idempotent;
- same request_id with different bound content => conflict;
- nonce/operation reuse cannot create a second effect;
- request/result ledger semantics survive lost response/retry.

3. Preparation/admission/signature chain
- pre-sign admission does not become effect authority;
- no circular identity dependency;
- SIGNATURE verification binds exact final request and prior admission evidence.

4. Quorum binding
- quorum binds deterministic exact set of signature-verification identities;
- current REJECT/conflict remains blocking;
- valid quorum != effect authority;
- disputed-signature two-seat review cannot be replayed as general quorum.

5. Recovery-driven currentness
- every authority-bearing interaction under unavailable/uncertain canonical state preserves SIS r0.2 recovery-first rule;
- failed recovery does not refresh currentness;
- local snapshot cannot self-renew;
- DEGRADED_CURRENT cannot silently become CURRENT.

6. PRE_EFFECT / TOCTOU
- authority/currentness is revalidated at effect boundary;
- accepted decision cannot survive later revocation/supersession without applicable revalidation;
- no unchecked gap between PRE_EFFECT validity and actual irreversible effect.

7. Effect binding
- exact effect payload equals bound arguments/effect boundary;
- hidden/unhashed parameters cannot influence effect;
- maximum effect identity/scope prevents widening;
- signature validity != effect authority.

8. Irreversible effects
- require CURRENT plus separately valid effect authority;
- degraded quorum/signatures cannot self-promote to irreversible AUTHORIZED state.

9. Idempotent effect execution
- operation_id/idempotency_key semantics prevent duplicate external effects;
- distinguish:
  decision accepted
  effect authorized
  effect attempted
  effect completed
  effect result unknown
- lost response must not fabricate a second effect.

10. Ledger durability boundary
- identify what must be atomically/durably persisted before implementation can claim replay protection;
- do not assume CHECKPOINT_DURABLE;
- document-only candidate must remain explicit about persistence/runtime requirements.

11. Canonical recovery conflict
- after Git recovery, stale/degraded decisions invalidated by canonical key/currentness state become blocked/reviewed;
- already irreversible effects must not be retroactively called valid merely because a signature existed.

12. State machine
- verify no circular convenience transition or authority-by-possession;
- UNKNOWN/CONFLICT/STALE states remain fail-closed.

13. Negative cases
At minimum examine:
- same request ID / different digest;
- same operation ID / different effect;
- nonce replay;
- stale snapshot;
- revoked key after decision before effect;
- profile/quorum-policy revision changes before effect;
- degraded signature replay after canonical recovery;
- dispute-review result replayed into ordinary governance;
- duplicate effect after lost response;
- hidden argument mutation after signing.

14. Implementation-readiness
Return exact remaining mandatory gaps before code implementation/review.
Do not turn a document PASS into implementation authority.

Expected terminal:

PASS_SHD_STP_C_ANTI_REPLAY_EFFECT_BINDING_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES

or exact FAIL_/BLOCKED_ with critical defects only.

Do NOT:
- implement code;
- generate keys;
- touch secret material;
- choose libraries/products by convenience;
- mutate hosts;
- deploy;
- activate Fast Gate/profile;
- live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
