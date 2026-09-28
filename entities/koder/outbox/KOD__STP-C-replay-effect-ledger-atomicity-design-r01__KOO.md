# KOD → KOO: STP-C replay/effect ledger atomicity r0.1

terminal: PASS_KOD_STP_C_REPLAY_EFFECT_LEDGER_ATOMICITY_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW
status: DOCUMENT_ONLY_CANDIDATE_NOT_ACTIVE
project_time: omitted

## Человеческий итог

Этот контракт описывает память защитного контура: как сохранить, что именно уже запрошено, подписано, разрешено и применено, чтобы повтор сообщения или сбой не вызвал второе действие. Одинаковый запрос получает прежний результат; совпавший ID с другим содержимым блокируется. После внешнего вызова с потерянным ответом система не угадывает успех и не повторяет действие до сверки с внешним исполнителем. Журнал обязан переживать сбой и конкуренцию процессов, но сам по себе не выдаёт полномочия.

Это document-only кандидат. Он не выбирает storage backend, не доказывает его реальную стойкость и не устанавливает `CHECKPOINT_DURABLE`.

## Exact basis

- KOD writer v0.5: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`.
- Authority: `puev5691/wellbeing-hq@c0e761ed684fa1d05f93b29542b342a5d31b7e6f:entities/koordinator/outbox/KOO__authorize-KOD-STP-C-replay-effect-ledger-atomicity-design-r01__OPERATOR.md`, blob `b5dffb64786a2eb6c2c5d8354debaffaf009c702`.
- Task: `puev5691/wellbeing-hq@775b17657ac5a7c819dfc961aeca4af6581d6464:entities/koordinator/outbox/KOO__STP-C-replay-effect-ledger-atomicity-design-r01__KOD.md`, blob `afcfebd9472a587d4568fe457f34453260dbad8a`.
- SHD review: `puev5691/wellbeing-hq@a28686b60c6cac48f1a4145162a1eb3977089108:entities/shardovik/outbox/SHD__STP-C-anti-replay-effect-binding-r01-independent-review__KOO.md`, blob `e5d821771133a8aeedf822af193f113b774de7e6`, conceptual PASS with durable ledger gap.
- Reviewed request/effect binding: `puev5691/wellbeing-hq@f8091f94ec31f4b9937d9cd41096e4b1a255fde4:entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md`, blob `3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8`.
- SIS recovery-first currentness r0.2 remains an external admission condition: `puev5691/wellbeing-hq@ca13d99e6bfe385d184f2e5ebfbe40309bd35e2f:entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r02__KOO.md`, blob `ecbeeda215fd3418503bdf947f79ddc8bbc7c3a8`.

All following rules are PROPOSED. Exact canonical serialization, digest/signature profile, policy activation, trusted issuer, downstream effect protocol and concrete durable backend remain UNKNOWN. No wall-clock lease or expiry confers authority without separately approved trusted time.

## 1. Logical keys and durable record

One ledger namespace is bound to exact governance domain, task/decision scope and effect domain; namespace aliasing is rejected. Two unique indexes/serializable predicates must cover `(namespace, request_id)` and `(namespace, operation_id)`; a third covers `(namespace, nonce_or_monotonic_identity)` and an effect index covers `(effect_domain, idempotency_key)`. These are *logical* unique constraints, not a backend choice. Unknown field, corrupt/noncanonical record, unverified digest or missing linked evidence → `LEDGER_CORRUPT`/`LEDGER_UNAVAILABLE`, never ALLOW.

Closed minimum durable record candidate `STPC_LEDGER_V1` (one logical aggregate, storage may decompose it only with equivalent atomicity):

| Field | Binding / evidence |
|---|---|
| `namespace`, `request_id`, `request_digest`, `operation_id`, `nonce_identity` | Exact identities from closed request, with canonical bytes identity and issuer/sequence provenance. |
| `decision_digest`, `effect_class`, `effect_boundary_identity`, `effect_target_id`, `effect_payload_digest`, `idempotency_key` | Exact intended effect. No later substitution of target, arguments or scope. |
| `request_evidence_identity`, `current_state`, `state_revision`, `last_transition_identity`, `process_fence` | Linked immutable request, state and monotonic transition version; writer/process must hold admitted fence. |
| `admission_result_identity`, `signature_result_identity`, `quorum_result_identity`, `pre_effect_result_identity` | Nullable until corresponding phase; non-null only after exact evidence and state transition persist. |
| `effect_auth_identity`, `effect_authority_basis_identity`, `currentness_evidence_identity` | Exact effect authorization and last applicable CURRENT/PRE_EFFECT evidence; null until authorization. |
| `claim_identity`, `claim_fence`, `invocation_identity`, `external_idempotency_key` | Exact claim and external invocation, nullable until begun. Same claim may be resumed only by its fenced owner or independently reconciled successor. |
| `external_receipt_identity`, `external_query_evidence_identity`, `reconciliation_state`, `terminal_result_identity` | Exact downstream outcome/query and final ledger result; nullable when unknown. UNKNOWN must remain explicit. |
| `record_integrity_identity`, `prior_transition_identity` | Canonical/closed record identity and transition chain; readback detects mismatch or missing predecessor. |

Persist a single reservation transaction before any signing: both request and operation indexes, nonce reservation, exact digests/effect/idempotency key, initial `RESERVED` state and revision. If any predicate collides differently, neither reservation is partly visible. A later phase transition atomically checks prior revision/fence and persists its own evidence identity, next state, operation outcome and transition link before exposing a success response. An actual signature must not be released before the corresponding SIGNED result is recoverably persisted; if signer and ledger cannot make that safe, an uncertain signing outcome blocks re-sign and needs a separately designed signer resolution protocol.

Durability means completed commits survive the specified failure model and become visible to all competing processes at one coherent revision. Uncommitted partial records must not masquerade as committed. Exact claim cannot be inferred from log text or a process memory variable.

## 2. State machine and transition guards

`NEW` is conceptual absence, not a persisted permission. `CONFLICT`, `REJECTED`, `STALE`, `QUORUM_BLOCKED`, `COMMITTED` are immutable terminal outcomes for the exact request revision. A new admissible decision uses a **new** request identity; history remains readable. `OUTCOME_UNKNOWN` is blocking but not a fabricated terminal success. `PENDING_RECONCILIATION` cannot auto-promote.

| Source → destination | Atomic evidence and gate | Forbidden shortcut |
|---|---|---|
| NEW → RESERVED | Simultaneous unique request/operation/nonce reservation and state revision commit | Partial request-only reservation; signing first. |
| RESERVED → ADMITTED | Closed admission evidence, fresh applicable currentness and active seat/key/task scope from external policy | Ledger existence → authority. |
| ADMITTED → SIGNED | Exact signed request/signature identity and signer outcome recoverably linked before release | Retry uncertain signing or release unpersisted signature. |
| SIGNED → VERIFIED | Closed signature verification result and prior state compare | Signature validity → effect. |
| VERIFIED → QUORUM_VALID / QUORUM_BLOCKED | Exact scoped quorum evidence; REJECT/conflict precedence | Generalize dispute-only review. |
| QUORUM_VALID → PENDING_RECONCILIATION | Applicable degraded policy allows only pending decision; bind failed recovery attempt and last verified local snapshot | Pending → AUTHORIZED. |
| QUORUM_VALID → PRE_EFFECT_VALID | Fresh applicable CURRENT/authority evidence and exact effect binding | Reuse admission-time snapshot. |
| PRE_EFFECT_VALID → AUTHORIZED | Separately valid effect authority; for irreversible effect CURRENT required; exact effect-auth identity stored | Quorum or ledger state alone grants authority. |
| AUTHORIZED → CLAIMED | Atomic unique effect key compare, final applicable authority/currentness check and fenced claim at one state revision | Competing claim or stale process starts effect. |
| CLAIMED → COMMITTED | Only externally confirmed matching effect receipt plus exact claim/authorization/target/payload; persist terminal before response | Call return without durable receipt → success. |
| CLAIMED → OUTCOME_UNKNOWN | Invocation may have occurred and confirmation is absent/ambiguous | Automatic second external call. |
| OUTCOME_UNKNOWN → COMMITTED / REJECTED | Authenticated exact-key query/reconciliation proves happened / did not happen, recorded with provenance; absence alone is not proof of non-execution | Timeout → REJECTED or retry. |
| Any uncommitted state → REJECTED / CONFLICT / STALE / QUORUM_BLOCKED | Persist exact reason and evidence in same transition transaction | Reverse into valid path under same identity. |
| PENDING_RECONCILIATION → STALE / CONFLICT / REJECTED | Canonical reconciliation invalidates pending decision | Silent discard. |

If canonical reconciliation validates a pending decision, no direct promotion: separately governed **new** currentness/effect check and a new authorization revision/identity are required; only if exact policy permits may this be linked to a new request. `SIGNED`/`VERIFIED` may remain historical even if later stale. `CLAIMED` cannot become ordinary STALE until external invocation is conclusively resolved; preserve uncertain effect evidence. `COMMITTED` never reverses or grants reusable authority. No `AUTHORIZED → QUORUM_VALID`, `CLAIMED → AUTHORIZED`, `OUTCOME_UNKNOWN → CLAIMED`, terminal → active, or revision rollback.

## 3. Idempotency and exact outcomes

| Input | Ledger response / behavior |
|---|---|
| Same request ID + exact digest/bytes, terminal | Exact prior result or `IDEMPOTENT_REPLAY` containing prior result identity; no signing/effect. |
| Same request ID + exact bytes, nonterminal | `IN_PROGRESS` with state/revision; no duplicate work except fenced continuation of the same operation after exact recovery. |
| Same operation ID + same exact intended effect and request binding | Same operation history/state; if different request ID, explicit aliasing is forbidden by default: `OPERATION_ID_COLLISION` until an approved alias rule exists. |
| Same request ID with changed digest/key/snapshot/scope/effect | `REQUEST_ID_COLLISION`; durable conflict evidence, no partial reservation. |
| Same operation ID with changed effect/idempotency key | `OPERATION_ID_COLLISION`; no effect. |
| Nonce reused on different request | `NONCE_REPLAY`; no signing/effect. |
| Lost response after durable COMMITTED | `RESOLVE_OPERATION` reads exact prior `COMMITTED` receipt, returns same result; no second call. |
| Replay after terminal REJECT/CONFLICT/STALE | Same immutable terminal result; no re-admission under old ID. |
| Ledger cannot be read or integrity fails | `LEDGER_UNAVAILABLE` / `LEDGER_CORRUPT`; no claim/effect or unverified replay response. |
| Transition compare loses to concurrent revision | `LEDGER_CONFLICT`; reload exact state; never overwrite newer evidence. |
| External outcome unresolved | `EFFECT_OUTCOME_UNKNOWN`; query/reconcile with exact idempotency key, no blind retry. |
| Executor lacks proven idempotency or exact-once reconciliation | `BLOCKED_EFFECT_EXECUTION` before invocation. |

`IN_PROGRESS` and `IDEMPOTENT_REPLAY` are response classifications, not permission to progress. Collision outcomes must be durable or recoverably derived from both exact committed identities. `RESOLVE_OPERATION(kind, namespace, id, exact_digest)` has closed response fields `status, operation_id, request_id, request_digest, state_revision, result_identity, evidence_identity`; mismatched digest returns CONFLICT, unavailable/corrupt ledger returns UNKNOWN/blocking, absent exact row returns NOT_APPLIED only if lookup/read integrity is proven. It must not infer NOT_APPLIED from an unavailable replica. An in-flight externally issued request cannot be retried as a new operation under another ID.

## 4. Concurrency and logical linearization

One atomic durable commit of both unique reservations is the request/operation reservation linearization point. Two concurrent same-ID exact requests: one commits reservation, other observes that exact commit and returns its state/result. Changed bytes: loser gets collision; neither overwrites. Two different request IDs competing for one operation ID: at most one commits; second conflicts even if payload appears equal unless explicit alias policy is separately adopted. Nonce race behaves similarly.

Every state advance is linearized by durable compare of `(namespace, operation_id, state_revision, process_fence)` and commit of new state plus linked evidence/outcome. A stale process holding an older revision/fence cannot publish a signature result, quorum, authorization or effect claim after a successor advances. Stale reads are diagnostic only. Unique effect claim is linearized by durable compare of effect key plus exact effect-auth/target/payload, applicable authority/currentness evidence and state revision in one commit. Two claimants: at most one claim wins; identical loser observes `IN_PROGRESS` or exact committed result; changed binding gets `EFFECT_KEY_COLLISION`. The backend must provide serializable-equivalent predicate/unique constraint behavior, not only last-write-wins or a per-process lock.

There is **no** common linearization point for a generic external effect and this ledger. The ledger claim and the external system must use a verifiable idempotency/query protocol or separately proven exactly-once effect protocol. If an authority/currentness change can occur after PRE_EFFECT/claim but before invocation, the executor must revalidate at the last enforceable boundary and have a downstream fence or equivalent contract that prevents an invalidated stale claim from executing. If such a boundary cannot be proven, execution is BLOCKED, especially for irreversible effects. No local transaction makes Git plus arbitrary external system atomic by assertion.

## 5. Crash and recovery matrix

| Crash point | Recoverable state/evidence | Retry allowed | Forbidden |
|---|---|---|---|
| Before reservation commit | No committed reservation; exact integrity read yields NOT_APPLIED | Same exact request may attempt first reservation again | Treat uncommitted intent as signed or effectful. |
| After reservation before signing | RESERVED with both IDs/nonce/effect bound | Fenced continuation after fresh admission/currentness; duplicate client gets IN_PROGRESS | Allocate new effect key or sign based solely on old admission. |
| After signer produces signature before SIGNED persist | ADMITTED plus potentially escaped/unknown signature | Only signer-specific exact outcome query/reconciliation if available | Re-sign or release first signature without recoverable identity; block if unresolved. |
| After SIGNED before quorum persist | SIGNED and exact signature identity; no QUORUM_VALID evidence | Recompute/check quorum with fresh applicable currentness and persist one transition | Assert quorum from in-memory votes or execute effect. |
| After PRE_EFFECT_VALID before CLAIMED | PRE_EFFECT_VALID/AUTHORIZED evidence, no claim | Revalidate currentness/authority and atomically claim exact effect key | Reuse stale PRE_EFFECT as indefinite permission. |
| After CLAIMED before external call | CLAIMED, call occurrence not intrinsically proven absent by ledger alone | Query downstream exact key; if provably never invoked and still authorized, controlled fenced continuation under protocol | Automatic second claim or assume never called on process crash. |
| After external call before COMMITTED receipt | CLAIMED or OUTCOME_UNKNOWN; external effect possibly happened | Exact idempotency-key query/reconciliation; persist confirmed result | Blind effect retry or infer NOT_APPLIED from missing local receipt. |
| After COMMITTED before client response | COMMITTED + exact external receipt and terminal result | RESOLVE returns identical committed result | Second external effect or rewrite receipt. |

For crash after claim and before possible invocation, process-local evidence cannot prove the external call did not happen. An invocation-intent transition may narrow diagnosis but cannot bridge the external transaction gap. On recovery classify unknown unless exact downstream query or independently proven atomic effect protocol distinguishes it. If query returns a signed/verified absence guarantee and the downstream idempotency key remains reserved, a fenced continuation may follow applicable policy; absent such guarantee, block. External response without durable local commit is never automatic success, even if client saw it; the exact downstream receipt must be reconciled.

## 6. Backend-neutral guarantees and integrity

Required capability profile, independently proven for the selected failure model: atomic multi-key reservation or equivalent serializable transaction; unique-key predicate enforcement under concurrency; conditional revision/fence transition; durable commit/read-after-crash and cross-process visibility; immutable outcome history and recoverable operation lookup; fail-closed detection of missing/torn/corrupt semantic records and mismatched request/effect/receipt identities; readback of exact bytes/evidence; protected external query credentials if later authorized; defined failure behavior under unavailable or partitioned ledger. No backend is appointed. Replica lag must not answer an authority-bearing lookup or NOT_APPLIED. Forked/conflicting histories yield `LEDGER_CONFLICT`, not a winning guess.

Durable evidence minimum includes exact request bytes/digest, scope/seat/key/snapshot provenance and per-interaction recovery result identities, request/operation/nonce reservation, state/revision/fence, transition reason/outcome, signature/quorum/PRE_EFFECT/effect-authority identities, target/payload/idempotency key, claim/invocation identity, downstream receipt or query evidence, reconciliation status and terminal result. Every authority-changing identity must match the reviewed r0.1 signed/hash scope. Garbage collection/retention cannot erase dedupe/conflict evidence while an exact operation or its external effect may be replayed; numeric retention and owner remain UNKNOWN.

## 7. Future negative, crash and concurrency verification matrix (not executed)

| ID | Setup / injection | Required assertion |
|---|---|---|
| C01 | Two concurrent exact requests, same ID | One reservation, same observed record/outcome. |
| C02 | Two same-ID requests with different digest | One winner; other REQUEST_ID_COLLISION; no partial operation/nonce row. |
| C03 | Two request IDs, same operation ID | One winner; other OPERATION_ID_COLLISION. |
| C04 | Two concurrent claims for one key | One claim; loser IN_PROGRESS or EFFECT_KEY_COLLISION; one external invocation max under protocol. |
| C05 | Stale process attempts revision/fence advance after successor | LEDGER_CONFLICT; no overwritten result. |
| N01 | Duplicate exact terminal request | Exact prior result/IDEMPOTENT_REPLAY; no sign/effect. |
| N02 | Duplicate exact in-progress request | IN_PROGRESS; no second signer/executor. |
| N03 | Reused nonce with different request | NONCE_REPLAY. |
| N04 | Same effect key with changed target/payload/effect-auth | EFFECT_KEY_COLLISION; no invocation. |
| N05 | Semantically corrupt but valid encoded ledger/receipt | LEDGER_CORRUPT; never COMMITTED/AUTHORIZED. |
| N06 | Unavailable ledger/lagged replica claims absent operation | LEDGER_UNAVAILABLE; not NOT_APPLIED. |
| N07 | Valid signature/quorum without CURRENT/PRE_EFFECT/effect authority | BLOCKED_EFFECT_EXECUTION. |
| N08 | Recovered canonical revocation after PRE_EFFECT | STALE/CONFLICT; no invocation. |
| N09 | Dispute-scoped two-seat evidence used as ordinary effect | REJECT; no claim. |
| F01 | Crash before reservation commit | No half reservation; exact retry permitted. |
| F02 | Crash after reservation before sign | RESERVED; same fenced continuation only. |
| F03 | Crash between signature generation and ledger persist | Uncertain sign blocks replay unless exact signer resolution. |
| F04 | Crash after SIGNED before quorum persistence | SIGNED retained; no phantom quorum. |
| F05 | Crash after PRE_EFFECT before claim | Recheck currentness before claim. |
| F06 | Crash after claim before possible external call | UNKNOWN until exact downstream proof; no blind retry. |
| F07 | Crash after external call before COMMITTED | OUTCOME_UNKNOWN; exact-key reconciliation; no duplicate irreversible effect. |
| F08 | Crash after COMMITTED before response | Same receipt returned after restart; invocation count unchanged. |
| F09 | Corrupt one side of request/operation/nonce reservation | LEDGER_CORRUPT/CONFLICT; no sign/effect. |

Tests must use a concrete candidate backend only after separate authority and cover process restart, concurrent processes, injected lost responses and externally observable invocation count. This matrix is design expectation, not a claim that any test ran.

## 8. Readiness gaps and boundary

Independent review should challenge: exact schema/canonical encoding; atomic multi-key constraint and revision protocol; signer-result recovery; process fence issuer/revocation; durable commit and corruption model; external idempotency/query/absence guarantees; downstream receipt authentication; final currentness fence between claim and call; exact reconciliation authority; ledger recovery after fork/partition; retention/GC and unavailable-store policy; precise behavior for reversible effects versus irreversible; test oracle and fault model. If any cannot be proven for a selected backend/executor, implementation admission blocks that effect class. No existing storage package, including the separate offline shard-store candidate, is automatically selected or promoted for STP-C.

Valid ledger state != task authority. Valid signature/quorum != effect authority. `CURRENT`, recovery-first and PRE_EFFECT rules are external conditions. A ledger can record and enforce evidence-bound transitions but cannot create seat, writer, project or effect authority. Git publication/readback is evidence, never effect authority.

No code, backend selection, keys, credentials, host mutation, deployment, live WRITE/CAS, Fast Gate/profile or Project Source activation, EOM pilot or memory-layering attempt 3. `CHECKPOINT_DURABLE` remains NOT_ESTABLISHED.

Next gate: KOO fresh reconciliation and independent technical/security review of this pinned document against SHD r0.1 and the previous KOD binding contract, before any implementation proposal.

## EXPERIENCE

Идея → фиксировать и проверять каждую заявку и попытку эффекта как одну причинную историю.
Проба → разобрать конкуренцию и сбои по обе стороны внешнего вызова, не приписывая журналу возможности атомарно управлять внешней системой.
Результат → документальный контракт с точками фиксации, блокирующими исходами и матрицей будущих проверок.
Вердикт → кандидат для независимой проверки, без реализации.
Урок → при неизвестном исходе внешнего действия повтор опаснее паузы; сначала нужна проверка по тому же ключу операции.
