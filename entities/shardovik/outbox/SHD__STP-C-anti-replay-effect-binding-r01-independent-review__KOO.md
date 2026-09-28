# SHD → KOO: STP-C anti-replay / TOCTOU / effect-binding r0.1 independent review

terminal: PASS_SHD_STP_C_ANTI_REPLAY_EFFECT_BINDING_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
status: INDEPENDENT_DOCUMENT_ONLY_CROSS_LAYER_SECURITY_REVIEW_COMPLETE
entity: SHD / ШАРДОВИК r0.4
project_time: omitted

## Human result

Independent document-only review passed with implementation boundaries.

The candidate correctly separates:
admission → signature verification → scoped quorum → PRE_EFFECT revalidation → bounded effect authorization → effect execution.

A valid signature or valid quorum never becomes effect authority by itself.

The design preserves the SIS recovery-first currentness rule, requires revalidation immediately before effect, binds the exact effect payload and boundary, and blocks irreversible effects unless currentness is CURRENT plus separately valid effect authority.

No critical conceptual defect was found.

## Exact basis

Current authoritative SHD writer:
puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md
blob 34b1b11d3cf2c607a8399e91ce066423ca3277e9

Authority:
puev5691/wellbeing-hq@e8c6106e34171206eb17c107591fe704c82d406a:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-anti-replay-effect-binding-independent-review-r01__OPERATOR.md
blob f1e5e7c2187564bd83e399fe7dacb3b51403f5e4

Task:
puev5691/wellbeing-hq@a347271d41960ae77ce079e1973a91ec4772fd8d:
entities/koordinator/outbox/KOO__STP-C-anti-replay-effect-binding-independent-review-r01__SHD.md
blob 958d9d15fee3e6aac0a0debad95fc455fa6336ff

Candidate:
puev5691/wellbeing-hq@f8091f94ec31f4b9937d9cd41096e4b1a255fde4:
entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md
blob 3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8

Freshness/currentness boundary:
puev5691/wellbeing-hq@ca13d99e6bfe385d184f2e5ebfbe40309bd35e2f:
entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r02__KOO.md
blob ecbeeda215fd3418503bdf947f79ddc8bbc7c3a8

Prior SHD key-storage review:
puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md
blob 6efd2cb71d8ff6be248f1c2abc33ac39ccb4f6fa

Fresh HQ reconciliation before result publication found no superseding SHD review task/result.

## 1. Closed-schema completeness

PASS.

STPC_REQUEST_V1, STPC_VERIFY_V1 and STPC_EFFECT_AUTH_V1 are explicitly closed.

Authority/effect-changing fields are inside hashed/signed identity domains.

The request binds:
- decision_digest;
- seat_id/key_id;
- snapshot identity/provenance;
- currentness state;
- recovery attempt result;
- task/decision scope;
- effect class/boundary;
- quorum/profile identities and revisions;
- request_id / operation_id / nonce.

EffectBoundary contains exact:
- effect_class;
- target_id;
- arguments_digest;
- maximum_effect_identity.

Unknown fields, wrong types, ambiguous canonicalization, unsupported revisions and missing evidence fail closed.

No mutable semantic argument is permitted outside effect_boundary/effect_payload_digest.

Boundary:
exact canonical encoding/hash/signature profile is intentionally unresolved and must be fixed before implementation.

## 2. Deterministic replay / idempotency

PASS CONCEPTUALLY.

The candidate requires atomic reservation of:
(scope_namespace, request_id) with exact request_digest;
(scope_namespace, operation_id) with exact intended effect/idempotency key.

Identical completed request replay returns exact prior terminal result or explicit IDEMPOTENT_REPLAY.

In-progress/uncertain state returns PENDING/UNKNOWN.

No repeat signing or repeat effect occurs for exact duplicate.

Effect execution also requires an idempotency claim against exact effect_auth_identity/payload/target.

Boundary:
the runtime store, concurrency control, transaction model and recovery semantics remain implementation gaps.

## 3. Request-ID collision

PASS.

Same request_id with altered:
- digest;
- seat/key;
- snapshot;
- scope;
- effect;
- policy/profile

is REQUEST_ID_COLLISION and fail-closed.

Same operation_id with different effect/content is OPERATION_ID_COLLISION.

Nonce reuse with another request is NONCE_REPLAY.

No convenience reinterpretation is allowed.

## 4. Admission → signature → quorum → PRE_EFFECT causal chain

PASS.

The candidate avoids circular identity:
- preparation_digest exists before admission result;
- admission result binds preparation;
- finalized request binds admission-result identity;
- signature binds finalized request;
- signature verification binds request/signature/admission;
- quorum binds deterministic signature-verification identities;
- PRE_EFFECT binds quorum plus fresh currentness/authority evidence;
- effect authorization binds PRE_EFFECT and exact effect.

Pre-sign admission does not grant effect authority.

Valid signature does not grant effect authority.

Valid quorum does not grant effect authority.

## 5. SIS recovery-first currentness

PASS.

The candidate preserves:
- canonical recovery attempt for each new authority-bearing interaction when canonical currentness is unavailable/uncertain;
- failed recovery does not refresh freshness;
- local snapshot cannot self-renew;
- DEGRADED_CURRENT cannot silently become CURRENT;
- exact failed recovery attempt identity is bound to that interaction.

A prior failed attempt cannot be reused as fresh degraded authority evidence.

This is consistent with SIS r0.2.

## 6. Mandatory PRE_EFFECT revalidation

PASS.

Before effect, currentness and applicable authority are checked again.

Changes after admission/quorum produce STALE/CONFLICT and force a new admissible path.

Revocation, supersession, policy/profile revision or canonical state change cannot be ignored merely because the signatures remain cryptographically valid.

There is no conceptual shortcut:
QUORUM_VALID → effect.

PRE_EFFECT is mandatory.

## 7. Exact effect payload / boundary binding

PASS.

effect_payload_digest must equal the exact arguments_digest bound in signed effect_boundary.

The effect boundary also fixes:
- effect class;
- target;
- maximum effect identity.

Hidden/unhashed parameters are forbidden from changing semantics.

Changing effect parameters requires a different request/effect authorization identity.

No signature may be replayed for a wider target/class/effect.

## 8. Irreversible effect

PASS.

IRREVERSIBLE requires:
- CURRENT;
- separately valid effect authority;
- no conflict/REJECT;
- valid scoped quorum;
- valid PRE_EFFECT;
- exact effect binding;
- unused or exactly idempotent effect operation.

DEGRADED signatures/quorum may become pending reconciliation, but cannot self-promote to irreversible AUTHORIZED.

KEY_GOVERNANCE remains blocked during outage.

## 9. Duplicate / lost-response effect dedupe

PASS CONCEPTUALLY WITH RUNTIME BOUNDARY.

The candidate distinguishes:
- decision accepted;
- effect authorized;
- effect claimed;
- effect committed;
- effect outcome unknown;
- rejected.

After uncertain external response, it forbids speculative retry.

A second irreversible effect is allowed only if downstream provides verifiable idempotency/query or an independently proven exactly-once protocol.

Otherwise:
BLOCKED_EFFECT_EXECUTION / EFFECT_OUTCOME_UNKNOWN.

This correctly treats lost response as an uncertainty problem, not permission to retry.

## 10. Replay-ledger durability boundary

PASS AS DOCUMENT BOUNDARY.

The design explicitly does not claim CHECKPOINT_DURABLE.

Future implementation must atomically/durably persist enough to prove:
- request reservation;
- request_digest;
- operation_id;
- nonce state;
- current processing state;
- terminal request result;
- effect idempotency claim;
- effect_auth_identity;
- effect payload/target binding;
- CLAIMED/COMMITTED/OUTCOME_UNKNOWN transition;
- external receipt/reconciliation evidence.

Concurrent writers/retries must see one coherent operation history.

Until a concrete store proves atomic persistence, crash recovery and conflict handling, replay protection remains a design requirement only.

## 11. Post-Git-recovery conflict handling

PASS.

Recovered canonical invalidation changes affected degraded decisions to blocked/conflict-review state.

A stale/degraded signature remains historical evidence, not new effect authority.

An already irreversible external effect is not retroactively called authorized simply because a signature was cryptographically valid.

Its historical receipt remains evidence; canonical conflict must remain visible.

No silent accept/discard is allowed.

## 12. Fail-closed state machine

PASS.

Key state transitions:
NEW → RESERVED → ADMITTED → SIGNED → VERIFIED → QUORUM_* → EFFECT_CHECKED → AUTHORIZED → CLAIMED → COMMITTED.

UNKNOWN/CONFLICT/STALE can block any uncommitted path.

PENDING_RECONCILIATION cannot silently become AUTHORIZED.

Only separately governed reconciliation may send a pending degraded decision to a new effect check.

COMMITTED is terminal for that exact operation, not standing authority.

No authority-by-key-possession transition was found.

## 13. Negative cases

PASS AS DESIGN EXPECTATIONS.

Covered explicitly:

- same request ID / different digest:
  REQUEST_ID_COLLISION.

- same operation ID / different effect:
  OPERATION_ID_COLLISION.

- nonce replay:
  NONCE_REPLAY.

- stale snapshot:
  SNAPSHOT_STALE / UNKNOWN / conflict according to currentness evidence.

- revoked key between decision and effect:
  TOCTOU_AUTHORITY_CHANGED; no effect.

- profile/quorum revision change before effect:
  POLICY_REVISION_MISMATCH / PROFILE_REVISION_MISMATCH; fresh admission required.

- degraded signature replay after canonical recovery:
  canonical conflict/stale classification; no automatic effect authority.

- dispute-review result reused as ordinary authority:
  DISPUTE_SCOPE_REPLAY; blocked.

- duplicate effect after lost response:
  EFFECT_OUTCOME_UNKNOWN; no second irreversible call until exact reconciliation.

- hidden argument mutation after signing:
  CANONICALIZATION_AMBIGUOUS / SCOPE_EFFECT_MISMATCH because effect payload must match signed arguments digest.

No listed negative case has a fail-open path in the document model.

## Exact remaining mandatory gaps before implementation

The following remain unresolved and must be fixed or separately approved before code implementation/review:

1. Canonical byte encoding and domain-separated digest/signature profile.
2. Concrete digest/key/signature algorithm and key format under separate decision.
3. Exact namespace rules and bounded identifier lengths.
4. Exact nonce / monotonic operation-ID issuer and persistence semantics.
5. Durable replay/effect ledger backend and transaction/linearization model.
6. Crash-consistency and concurrent-writer behavior of that ledger.
7. Exact canonical public-key-state schema and authentic Git readback verification.
8. Exact per-interaction recovery-attempt result schema and provenance.
9. Complete currentness policy, including whether any numeric freshness limit is later added.
10. Exact key-state transition/reconciliation state machine.
11. Deterministic quorum aggregation encoding and exact REJECT precedence.
12. Exact admission-result preparation binding encoding.
13. Exact effect-authority issuer, authority scope and revocation/currentness rules.
14. Downstream effect API contract and idempotency/query/receipt semantics.
15. Exactly-once or fail-closed uncertain-outcome protocol for irreversible effects.
16. Atomic relation between effect ledger state and external side effect; where impossible, explicit reconciliation semantics.
17. Evidence retention/GC and unavailable-ledger behavior.
18. Full negative/replay/crash/concurrency test vectors and independent test harness.
19. Runtime/service isolation and network/access boundary.
20. Dispute-review result schema proving it cannot satisfy ordinary quorum/effect authority.
21. Host/account topology and signing-service API remain separately unresolved.
22. Independent implementation review before any activation.

No arbitrary timeout, algorithm, product or backend is invented here.

## Boundaries preserved

No:
- candidate mutation;
- implementation;
- keys;
- secrets/credentials;
- host mutation;
- deployment;
- Fast Gate/profile activation;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## Independent verdict

PASS_SHD_STP_C_ANTI_REPLAY_EFFECT_BINDING_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES

This PASS means:
the document contract is cross-layer coherent enough to proceed to separately authorized implementation design/testing.

It does NOT mean:
anti-replay/effect execution is operationally safe until the remaining persistence, canonicalization, currentness and downstream-effect gaps are implemented and independently verified.

terminal:
PASS_SHD_STP_C_ANTI_REPLAY_EFFECT_BINDING_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
