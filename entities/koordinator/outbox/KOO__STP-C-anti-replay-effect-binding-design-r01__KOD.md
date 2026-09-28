# KOO → KOD: STP-C anti-replay / TOCTOU / effect-binding contract design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: DOCUMENT_ONLY_PROTOCOL_CONTRACT_DESIGN
project_time: omitted

Resume-First.

Current authoritative KOD writer:

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

writer_gate_outcome:
WRITER_ESTABLISHED

Exact authority:

puev5691/wellbeing-hq@f04e541d0357d72046708571f2e55b58c28d5650:
entities/koordinator/outbox/KOO__authorize-KOD-STP-C-anti-replay-effect-binding-design-r01__OPERATOR.md

Exact freshness/currentness policy:

puev5691/wellbeing-hq@ca13d99e6bfe385d184f2e5ebfbe40309bd35e2f:
entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r02__KOO.md
blob ecbeeda215fd3418503bdf947f79ddc8bbc7c3a8

Exact SHD review basis:

puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md

Design only the exact anti-replay / TOCTOU / effect-binding contract.

## Required binding

Every authority-bearing decision/signing request must bind at minimum:

- request_id / operation_id;
- decision_digest;
- seat_id;
- key_id;
- exact public-key-state snapshot identity;
- currentness state;
- recovery-attempt result identity where applicable;
- normal/degraded mode;
- task/decision scope;
- intended effect class/boundary;
- quorum-policy identity/revision;
- profile identity/revision;
- unique anti-replay nonce or monotonic operation identity;
- verification result identity;
- canonical/local snapshot provenance.

Do not use wall-clock time as trusted authority evidence unless a separately approved trusted-time source exists.

## Required semantics

Define exact outcomes for:

1. duplicate identical request:
- same request_id + same bound content;
- must return same prior result or explicit idempotent replay result.

2. request_id collision:
- same request_id + different digest/key/snapshot/effect/scope;
- must be CONFLICT and fail closed.

3. stale snapshot:
- must not be silently accepted after canonical recovery or known invalidation.

4. replayed signature:
- valid cryptographic signature alone must not authorize a new effect.

5. TOCTOU:
- decision accepted under currentness X but effect executed after authority/currentness changed;
- effect must revalidate applicable authority/currentness at effect boundary.

6. irreversible effect:
- require CURRENT and separately valid effect-authority condition unless a later exact policy says otherwise.

7. degraded mode:
- bind exact last verified snapshot and exact recovery-attempt result for this interaction;
- failed recovery must not refresh currentness;
- degraded signature/quorum may be pending but not self-upgrade to irreversible effect authority.

8. quorum:
- valid signatures + valid quorum != effect authority;
- current REJECT/conflict semantics remain preserved.

9. disputed outage signature:
- bind the dispute review scope so its two-seat review cannot be replayed as general governance authority.

10. idempotent effect execution:
- define requirement for effect dedupe / exactly-once-or-provably-idempotent semantics;
- distinguish decision acceptance from effect execution result.

## Required contract artifacts

Produce one standalone design candidate containing:

A. closed request schema candidate;
B. closed verification-result schema candidate;
C. effect-authorization record candidate;
D. replay/idempotency ledger semantics;
E. conflict taxonomy;
F. state transition diagram/table;
G. negative test matrix;
H. explicit implementation-readiness gaps.

## Hard invariants

- signature validity != authority;
- quorum validity != effect authority;
- request identity collision fails closed;
- UNKNOWN currentness never becomes allow;
- local snapshot never renews itself;
- effect execution requires exact bound decision/evidence;
- no mutable field may be left outside the signed/hashed decision scope if it changes authority/effect semantics;
- key possession does not create seat authority;
- Git publication does not create effect authority.

## Do not implement

No code.
No keys.
No credentials.
No host mutation.
No deployment.
No product/library selection by convenience.

Expected terminal:

PASS_KOD_STP_C_ANTI_REPLAY_EFFECT_BINDING_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

After immutable result + exact readback + return KOO, STOP.
