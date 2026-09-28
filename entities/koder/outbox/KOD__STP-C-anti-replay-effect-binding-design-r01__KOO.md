# KOD → KOO: STP-C anti-replay / TOCTOU / effect-binding contract r0.1

terminal: PASS_KOD_STP_C_ANTI_REPLAY_EFFECT_BINDING_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW
status: DOCUMENT_ONLY_CANDIDATE_NOT_ACTIVE
project_time: omitted

## Человеческий смысл

Этот кандидат описывает, как не принять старую или повторно предъявленную подпись за разрешение нового действия. Точное решение, состав подписантов, версия ключей, проверенное состояние и допустимый эффект связываются одной проверяемой цепочкой. Перед фактическим эффектом состояние полномочий проверяется ещё раз; изменение между голосованием и применением останавливает действие. Повтор запроса возвращает прежний результат, а совпавший ID с иным содержимым блокируется.

Это проект протокола, а не действующее разрешение, реализация или выбор алгоритма/хранилища. SIS r0.2 — документальный кандидат политики currentness, а SHD PASS концептуален и содержит границы. Политика эффекта, trust roots и атомарный исполнитель требуют отдельных решений и проверки.

## Проверенные основания и область

- KOD current writer v0.5: `puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`, `WRITER_ESTABLISHED`.
- Authority: `puev5691/wellbeing-hq@f04e541d0357d72046708571f2e55b58c28d5650:entities/koordinator/outbox/KOO__authorize-KOD-STP-C-anti-replay-effect-binding-design-r01__OPERATOR.md`, blob `7783ad10a8fbe116edadb3d30b4016eb810abb1f`.
- Task: `puev5691/wellbeing-hq@899d987aa7b8c2d84be16e319af508513a08160e:entities/koordinator/outbox/KOO__STP-C-anti-replay-effect-binding-design-r01__KOD.md`, blob `c82de86f96ef65c2021ad241541d2922c33d7059`.
- SIS recovery-driven currentness r0.2: `puev5691/wellbeing-hq@ca13d99e6bfe385d184f2e5ebfbe40309bd35e2f:entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r02__KOO.md`, blob `ecbeeda215fd3418503bdf947f79ddc8bbc7c3a8`.
- SHD conceptual review: `puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md`, blob `6efd2cb71d8ff6be248f1c2abc33ac39ccb4f6fa`.

All schemas and transitions below are **PROPOSED**, with strict rejection of unknown fields, wrong types, ambiguous serialization, absent required evidence or unapproved revisions. `identity(X)` means a domain-separated digest of exact canonical bytes of X under a future approved encoding/hash profile; algorithm and canonicalization profile are UNKNOWN and must be pinned before implementation. A locator alone is never an identity. No wall-clock value establishes authority absent a separately approved trusted-time source.

Candidate type grammar: `Id`, `Ref` and `Digest` are nonempty bounded UTF-8 strings in distinct tagged domains; `Digest` is a lowercase fixed-length value only after the digest profile is approved. `Revision` is a positive integer, never a float or numeric string. `NullableDigest` permits explicit null only at the stated phase. `EffectBoundary` is exactly `{effect_class, target_id, arguments_digest, maximum_effect_identity}` with `effect_class` from the closed classes below and the other values typed `Id`, `Digest`, `Digest`; no hidden arguments may influence effect semantics. `SnapshotProvenance` is exactly one tagged alternative: `{kind:CANONICAL,repository:Id,commit:Digest,blob:Digest,readback_identity:Digest}` or `{kind:LOCAL_VERIFIED,last_canonical_identity:Digest,local_bytes_identity:Digest,last_successful_verification_identity:Digest}`. `Binding[]` is a strictly ordered, duplicate-free array of exact `{seat_id:Id,key_id:Id,snapshot_identity:Digest,currentness_state:Id,recovery_attempt_result_identity:Digest,mode:Id}`. `Digest[]` is ordered and duplicate-free. These types are candidate semantics; numeric sizes and concrete encoding are deliberately not selected.

## A. Closed authority-bearing request candidate

`STPC_REQUEST_V1` has exactly the following keys. No implicit defaults, field omission, extension or null-as-unknown conversion. All `*_id`/`*_digest`/`*_ref` values are nonempty, typed, length-bounded under a future encoding profile; enumerations are closed. `request_id` is unique in its namespace and the operation ID is unique per intended effect. The entire object, including every authority-changing field, belongs to the signed/hashed domain `STPC_REQUEST_V1`.

Request types: `schema` literal string; `request_id`, `operation_id`, `nonce`, `seat_id`, `key_id`, `task_scope`, `decision_scope`, `intended_effect_class`, `quorum_policy_identity`, `profile_identity` are `Id` (effect class further restricted to the enum); `decision_digest`, `public_key_snapshot_identity`, `recovery_attempt_result_identity`, `admission_verification_result_identity`, `request_digest` are `Digest`; `decision_ref` is `Ref`; `snapshot_provenance` is `SnapshotProvenance`; `effect_boundary` is `EffectBoundary`; `quorum_policy_revision`, `profile_revision` are `Revision`; `currentness_state` and `mode` are closed enum strings. The `effect_boundary.effect_class` must equal `intended_effect_class`.

| Field | Exact meaning / type |
|---|---|
| `schema`, `request_id`, `operation_id`, `nonce` | Literal `STPC_REQUEST_V1`; bounded opaque identifiers; nonce unique in the request namespace or operation identity monotonic under a verified issuer/ledger. Uniqueness issuance is not inferred from a random-looking value. |
| `decision_digest`, `decision_ref` | Exact immutable decision bytes identity and locator; ref must resolve to those bytes. |
| `seat_id`, `key_id` | Exact seat and key binding; possession alone proves neither seat authority nor key ACTIVE state. |
| `public_key_snapshot_identity`, `snapshot_provenance` | Exact immutable public-key-state snapshot identity; provenance closed union `CANONICAL{repository,commit,blob,readback_identity}` or `LOCAL_VERIFIED{last_canonical_identity,local_bytes_identity,last_successful_verification_identity}`. Local evidence cannot update its own canonical identity. |
| `currentness_state`, `recovery_attempt_result_identity`, `mode` | Closed states `CURRENT` / `DEGRADED_CURRENT`; mode `NORMAL` / `DEGRADED` respectively. In NORMAL the recovery result is exact successful canonical verification identity. In DEGRADED it is the failed recovery attempt identity **for this request**; no null and no reused previous interaction result. UNKNOWN, conflict, expired or recovery-required cannot sign. |
| `task_scope`, `decision_scope`, `intended_effect_class`, `effect_boundary` | Exact immutable scope identifiers and allowed operation class, target, arguments digest and maximum effect boundary; `NONE`, `REVERSIBLE`, `IRREVERSIBLE`, `KEY_GOVERNANCE`, `DISPUTE_REVIEW` are distinct classes, not substitutable. |
| `quorum_policy_identity`, `quorum_policy_revision`, `profile_identity`, `profile_revision` | Exact independently admitted policy/profile revisions; publication alone does not activate them. |
| `admission_verification_result_identity` | Identity of a **prior** closed admission check, bound to this request's immutable preparation digest and snapshot; not the result of verifying the signature generated by this request. |
| `request_digest` | Domain-separated identity of the exact preceding fields, excluding only this derived field. A signature covers the whole finalized request including this digest. Recompute and compare on every consumption. |

To avoid a circular hash: pre-sign admission result binds a `preparation_digest` of all request fields except its own result identity and `request_digest`; it is persisted before the final request. The final request binds that admission-result identity; the subsequent signature-verification result binds the final request digest and signature identity. Quorum and effect records bind those later verification identities. Any mutation creates a different request digest and cannot inherit the old ID. The pre-sign admission result does not grant effect authority.

For `DISPUTE_REVIEW`, `decision_scope` includes exact disputed signature/request identity, contested seat/key, dispute case ID and allowed resolution operation; two non-disputed seats' approvals have this domain only. They cannot satisfy general quorum or effect class. Current canonical REJECT or unresolved conflict remains blocking regardless of two signatures.

## B. Closed verification-result candidate

`STPC_VERIFY_V1` has exactly: `schema`, `verification_id`, `phase` (`ADMISSION` / `SIGNATURE` / `QUORUM` / `PRE_EFFECT`), `request_id`, `operation_id`, `request_digest` (or `preparation_digest` only for ADMISSION), `decision_digest`, `seat_id`, `key_id`, `signature_identity` (null only for ADMISSION), `public_key_snapshot_identity`, `snapshot_provenance`, `currentness_state`, `recovery_attempt_result_identity`, `mode`, `task_scope`, `decision_scope`, `intended_effect_class`, `effect_boundary`, `quorum_policy_identity`, `quorum_policy_revision`, `profile_identity`, `profile_revision`, `prior_verification_id` (null only for ADMISSION), `observed_authority_identity`, `result`, `reason`, `result_identity`.

Verification types: `schema` literal; `verification_id`, `request_id`, `operation_id`, `seat_id`, `key_id`, `task_scope`, `decision_scope`, `intended_effect_class`, `quorum_policy_identity`, `profile_identity` are `Id`; `request_digest`/`preparation_digest`, `decision_digest`, `public_key_snapshot_identity`, `recovery_attempt_result_identity`, `observed_authority_identity`, `result_identity` are `Digest`; `signature_identity`, `prior_verification_id` are `NullableDigest` with null only at the phase stated; `snapshot_provenance` and `effect_boundary` use the closed types above; revisions are `Revision`; phase/currentness/mode/result/reason are closed enum strings. ADMISSION uses an explicit `preparation_digest` in place of `request_digest`; the two names never coexist. `reason` uses one of the E taxonomy codes or `NONE` for a valid phase.

`result` is one of `VALID_FOR_PHASE`, `REJECT`, `CONFLICT`, `STALE`, `UNKNOWN`; `reason` is a closed reason code. `result_identity` derives from all preceding fields under `STPC_VERIFY_V1`. ADMISSION binds the preparation digest before signing; SIGNATURE binds final request/signature/admission; QUORUM binds a deterministic ordered set of SIGNATURE result identities additionally in `observed_authority_identity`; PRE_EFFECT binds the quorum result, live applicable currentness/authority evidence, and intended effect. An implementation must define that aggregate encoding; until then no effect record can be issued. Result `VALID_FOR_PHASE` is never a generic authority grant. A failed canonical recovery attempt retains the last successful snapshot provenance and cannot renew freshness. Every new authority-bearing phase/interaction first performs canonical recovery if canonical currentness is unavailable or uncertain.

## C. Closed effect-authorization record candidate

`STPC_EFFECT_AUTH_V1` has exactly: `schema`, `effect_auth_id`, `operation_id`, `request_id`, `request_digest`, `decision_digest`, `task_scope`, `decision_scope`, `intended_effect_class`, `effect_boundary`, `effect_payload_digest`, `quorum_result_identity`, `ordered_signature_verification_identities`, `pre_effect_verification_identity`, `seat_key_snapshot_bindings`, `quorum_policy_identity`, `quorum_policy_revision`, `profile_identity`, `profile_revision`, `mode`, `currentness_state`, `public_key_snapshot_identity`, `snapshot_provenance`, `recovery_attempt_result_identity`, `effect_authority_basis_identity`, `idempotency_key`, `authorization_result`, `effect_auth_identity`.

Effect-record types: `schema` literal; `effect_auth_id`, `operation_id`, `request_id`, `task_scope`, `decision_scope`, `intended_effect_class`, `quorum_policy_identity`, `profile_identity`, `idempotency_key` are `Id`; `request_digest`, `decision_digest`, `effect_payload_digest`, `quorum_result_identity`, `pre_effect_verification_identity`, `public_key_snapshot_identity`, `recovery_attempt_result_identity`, `effect_authority_basis_identity`, `effect_auth_identity` are `Digest`; `ordered_signature_verification_identities` is `Digest[]`; `seat_key_snapshot_bindings` is `Binding[]`; revisions are `Revision`; `effect_boundary` and `snapshot_provenance` use closed types; mode/currentness/authorization result are closed enums. All identities are recomputed from exact referenced evidence. No receipt, result, signature or object may substitute merely because its name matches.

All fields have exact typed/closed encoding and domain-separated identity over preceding fields. `seat_key_snapshot_bindings` is an exact ordered set of the seat/key/snapshot/currentness/recovery/mode tuples for *each* signature, not only an aggregate. `authorization_result` is one of `AUTHORIZED`, `PENDING_RECONCILIATION`, `REJECTED`, `BLOCKED_CONFLICT`, `UNKNOWN`; only `AUTHORIZED` can be consumed by an executor. It requires current applicable task authority, policy/profile, no REJECT/conflict, signature validity, valid scoped quorum, PRE_EFFECT verification, exact effect authority, and an unused or exactly idempotent operation key. `effect_payload_digest` must equal the exact arguments digest inside the signed `effect_boundary`. For IRREVERSIBLE, `CURRENT` and separate valid effect authority are mandatory. DEGRADED signatures/quorum may yield `PENDING_RECONCILIATION`, never an irreversible `AUTHORIZED` record. `KEY_GOVERNANCE` is blocked during outage. Dispute resolution creates only its dispute-scoped outcome, not general effect authorization. A verifier must independently rederive every identity and reject any mismatch or unsupported policy revision.

## D. Replay, TOCTOU and effect ledger

1. On receipt, atomically reserve `(scope_namespace, request_id)` with exact `request_digest`, operation ID and nonce; reserve `(scope_namespace, operation_id)` with exact intended effect and idempotency key. Duplicate identical request returns the exact stored terminal result or explicit `IDEMPOTENT_REPLAY` referencing it; it never signs again or executes a second effect. An in-progress/uncertain result returns `PENDING/UNKNOWN`, not a fabricated success. Same ID with changed bytes/digest/seat/key/snapshot/scope/effect/policy/profile → `REQUEST_ID_COLLISION`, fail closed. Nonce reuse with a different request → `NONCE_REPLAY`; monotonic ID rollback/gap inconsistent with issuer policy → block. The operation ledger is recoverable and protected against conflicting concurrent writers; mechanism/back end remains UNKNOWN.
2. For each new seat decision and quorum phase, attempt canonical recovery if currentness is unavailable/uncertain. Bind success to exact canonical readback or failure to this phase's recovery result and last previously verified local snapshot. Failed retry does not extend freshness. On canonical recovery/invalidation, compare exact snapshot and key/seat authority; conflicting or REJECT decision becomes `BLOCKED_CONFLICT_REVIEW`, never silently accepted. A signature valid under an older snapshot can remain historical evidence, not new effect authority.
3. Before an effect, reserve exact effect operation and **recheck applicable currentness and authority** against a new PRE_EFFECT result at the effect boundary. If anything changed since admission/quorum, invalidate the candidate authorization, classify `STALE/CONFLICT`, and require a new admissible decision path; do not rewrite or reuse old signed bytes. Signing and quorum never by themselves authorize effect. A valid replayed signature cannot create a second effect or broaden the signed effect boundary.
4. Effect executor atomically claims `(effect-domain, idempotency_key)` against the exact `effect_auth_identity`, payload digest and target. Same identity may return previously committed effect outcome. Different identity/content with same key fails closed. Before an irreversible external call, require the downstream effect to accept and enforce this idempotency key with verifiable result, or an independently proven exactly-once protocol covering uncertain responses/crash. If neither exists, **BLOCKED_EFFECT_EXECUTION**; no speculative retry. Separate durable states `AUTHORIZED`, `CLAIMED`, `COMMITTED`, `OUTCOME_UNKNOWN`, `REJECTED`; claiming is not completion. After an uncertain response, query/reconcile by exact key and receipt; never issue a second irreversible effect while outcome unknown. Do not assert atomicity between Git and an external system without proof.
5. `request_id` identifies a decision attempt, `operation_id` one logical intended effect, `effect_auth_identity` a verified authorization version. Changes to currentness or policy can invalidate a previously authorized but unexecuted effect. A completed effect's immutable receipt remains historical even if later authority changes; it does not grant new effect authority. Ledger provenance and retention policy are implementation gaps; no wall-clock-based expiry is invented.

## E. Conflict taxonomy

| Code | Trigger | Fail-closed outcome |
|---|---|---|
| `REQUEST_ID_COLLISION` / `OPERATION_ID_COLLISION` | Same ID, different exact bound bytes or effect | CONFLICT; preserve both identities; no new signature/effect. |
| `NONCE_REPLAY` / `MONOTONIC_ID_INVALID` | Reused nonce for another request or invalid issuer sequence | REJECT; no authority. |
| `SNAPSHOT_STALE` / `CANONICAL_CONFLICT` | Recovered canonical successor/invalidation conflicts with local or decision | STALE / BLOCKED_CONFLICT_REVIEW. |
| `RECOVERY_EVIDENCE_MISSING` / `CURRENTNESS_UNKNOWN` | No exact per-interaction result or admissible last verified snapshot | UNKNOWN; fail closed. |
| `SEAT_KEY_MISMATCH` / `KEY_STATE_REJECT` | Key possessed but seat/key not ACTIVE/authorized, or current REJECT | REJECT. |
| `SCOPE_EFFECT_MISMATCH` / `DISPUTE_SCOPE_REPLAY` | Signature/quorum reused for different task/effect or general quorum | CONFLICT / REJECT. |
| `POLICY_REVISION_MISMATCH` / `PROFILE_REVISION_MISMATCH` | Unknown or changed applicable policy/profile | STALE; fresh admission. |
| `TOCTOU_AUTHORITY_CHANGED` | Applicable authority/currentness changed before effect | STALE; no effect. |
| `EFFECT_KEY_COLLISION` / `EFFECT_OUTCOME_UNKNOWN` | Effect key with different content or uncertain downstream outcome | CONFLICT or BLOCKED until exact reconciliation. |
| `CANONICALIZATION_AMBIGUOUS` / `EVIDENCE_UNAVAILABLE` | Non-canonical bytes, unknown fields, missing exact readback | UNKNOWN; fail closed. |

## F. State transitions

| From → to | Required evidence / condition | Forbidden shortcut |
|---|---|---|
| NEW → RESERVED | Exact closed request digest, unique IDs/nonce or identical prior reservation | ID collision → signed. |
| RESERVED → ADMITTED | Prior admission result, per-interaction recovery/currentness and seat/key/policy checks | Local snapshot self-renewal. |
| ADMITTED → SIGNED → VERIFIED | Signature over finalized request; exact signature verification result | Valid signature → effect. |
| VERIFIED → QUORUM_PENDING / QUORUM_VALID | Scoped set of non-conflicting signature results, current REJECT checked | Two-seat dispute → general quorum. |
| QUORUM_VALID → PENDING_RECONCILIATION | Degraded decision where selected policy allows pending only | Degraded → irreversible effect. |
| QUORUM_VALID → EFFECT_CHECKED | New PRE_EFFECT currentness/authority verification; exact effect scope and policy | Reuse old currentness after change. |
| EFFECT_CHECKED → AUTHORIZED | CURRENT for irreversible, separate effect authority, exact effect-auth record | Quorum alone → AUTHORIZED. |
| AUTHORIZED → CLAIMED → COMMITTED | Atomic dedupe claim, idempotent/exactly-once downstream proof, exact effect receipt | UNKNOWN response → retry effect. |
| Any uncommitted → BLOCKED/CONFLICT/STALE | Missing or conflicting evidence, canonical recovery/invalidation, unknown outcome | Silent promotion or historical rewrite. |

Only a separately governed reconciliation may move a pending degraded decision into a *new* effect check; an old pending signature is never automatically promoted. `COMMITTED` is terminal for that exact operation, not general standing authority.

## G. Negative verification matrix (design expectations, NOT executed tests)

| Case | Mutation / fault | Expected result |
|---|---|---|
| N01 | Same request ID and exact bytes after completed outcome | Same stored result / explicit idempotent replay; no new sign/effect. |
| N02 | Same request ID, different digest/key/snapshot/effect/scope | `REQUEST_ID_COLLISION`; no effect. |
| N03 | Same operation ID, different payload or effect boundary | `OPERATION_ID_COLLISION`; no effect. |
| N04 | Reused nonce with new ID; monotonic identity rollback | `NONCE_REPLAY` / `MONOTONIC_ID_INVALID`. |
| N05 | Replayed valid signature under new effect class/target | `SCOPE_EFFECT_MISMATCH`; reject. |
| N06 | Canonical revocation between quorum and effect | `TOCTOU_AUTHORITY_CHANGED`; no effect. |
| N07 | Local snapshot conflicts with recovered canonical state | `CANONICAL_CONFLICT`; affected decisions blocked. |
| N08 | Failed recovery attempt reused from prior interaction | `RECOVERY_EVIDENCE_MISSING`; no degraded authority. |
| N09 | Repeated failed recovery claimed to refresh snapshot | `SNAPSHOT_STALE`/UNKNOWN under applicable policy. |
| N10 | UNKNOWN currentness, syntactically valid signatures and quorum | No authorization. |
| N11 | Degraded pending quorum asks irreversible effect | Block until CURRENT and separate effect authority. |
| N12 | Current explicit REJECT mixed with valid quorum | REJECT survives; no effect. |
| N13 | Disputed seat votes on own signature, or two reviewers act outside dispute | `DISPUTE_SCOPE_REPLAY`; block. |
| N14 | Unknown/changed policy or profile revision | STALE / UNKNOWN; fresh admission. |
| N15 | Valid key signature but no active seat binding | `SEAT_KEY_MISMATCH`; reject. |
| N16 | Signature result identity tampered; admission result circular or absent | `EVIDENCE_UNAVAILABLE`; block. |
| N17 | Duplicate effect key with different authorization/content | `EFFECT_KEY_COLLISION`; no execution. |
| N18 | External effect response lost after claim, no query/idempotency proof | `EFFECT_OUTCOME_UNKNOWN`; no retry. |
| N19 | Git publication/readback exists without separate effect authority | No effect. |
| N20 | Untrusted wall-clock timestamp used as currentness proof | `CURRENTNESS_UNKNOWN`; no effect. |
| N21 | Canonical bytes ambiguous, unknown field or mutable effect argument outside signed scope | `CANONICALIZATION_AMBIGUOUS`; reject. |
| P01 | Exact CURRENT request, active seat/key, valid scoped quorum, independent effect authority, unchanged pre-effect check and idempotent executor | One bounded authorized effect and one receipt; duplicate exact request returns same outcome. |

## H. Implementation-readiness gaps and next review

This is an interface contract candidate, **not implementation-ready approval**. Independent review must settle: exact canonical encoding/hash/signing profile and domain separation; key-state schema and authentic canonical readback; seat/key/policy/profile authority and revisions; trusted issuer of nonce/operation identities; atomic and durable ledger consistency/concurrency/recovery; typed representation and verification of per-interaction recovery attempts; provenance and currentness policy selection including residual stale-authority exposure; complete key-state transition/reconciliation rules; exact quorum aggregation encoding and REJECT precedence; admission-result preparation binding; actual effect-authority issuer; downstream effect idempotency/uncertain-outcome reconciliation; evidence retention and unavailable-store behavior; negative test harness and runtime isolation. Host/account topology and service APIs remain separate boundaries from SHD review. No numeric TTL or trusted time is selected.

Next gate: KOO fresh reconciliation and independent SIS/SHD (and governance scope review where KOO determines) of this immutable design against SIS r0.2 and SHD review, before any separate implementation authority. Earlier conceptual PASS does not activate this candidate.

No code, keys, credentials, host mutation, deployment, Fast Gate/profile activation, live WRITE/CAS, Project Source activation or EOM pilot. `CHECKPOINT_DURABLE` not established; memory-layering attempt 3 NOT_AUTHORIZED.

## EXPERIENCE

Идея → отделить проверку подписи от разрешения конкретного эффекта.
Проба → связать request, snapshot, recovery, quorum и pre-effect проверку неизменяемыми идентичностями и отдельным ledger.
Результат → получен проверяемый документальный контракт с закрытыми схемами и отрицательными случаями, без исполнения.
Вердикт → кандидат для независимой проверки.
Урок → повтор старой подписи и успешный quorum не заменяют новую проверку полномочий непосредственно перед эффектом.
