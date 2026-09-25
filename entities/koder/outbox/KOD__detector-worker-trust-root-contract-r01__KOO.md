# DetectorEventAndSupervisorTrustRootContract r0.1 — кандидат КОДЕРА для КОО

status: DOCUMENT_CANDIDATE_READY_FOR_OPERATOR_TRUST_ROOT_DECISION
scope: DESIGN_ONLY; NOT_APPROVED; NOT_EXECUTABLE; NO_PRODUCTION_ADMISSION

## Основание и граница

Точное поручение: `puev5691/wellbeing-hq@1f91efff2d0e5b258fcc958228cbaa28108ba622:entities/koordinator/outbox/KOO__detector-worker-trust-root-contract-r01__KOD.md`, blob `9e67b778b06c119cef4c476284001eae7b10a67c`. Independent SIS review: `puev5691/wellbeing-hq@4cf2a81c114e076b42e7824e479c96a40735519a:entities/sisadmin/outbox/SIS__detector-worker-admission-r02-independent-review__KOO.md`, blob `3d2b5e6e7ffac13c5c58b24ba6dd286336a539cd`, terminal `PASS_SIS_DETECTOR_WORKER_ADMISSION_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES`. SIS independently reconstructed code and checked semantics, but did not independently rerun 25 Python cases. The existing workflow does not issue this envelope or invoke the worker.

Fresh preflight HEAD `1f91efff2d0e5b258fcc958228cbaa28108ba622`, tree `61dc528ba26b24b280dd340bdd4a619959d97621`, not truncated. KOD current-writer v0.5 blob `cf1c84f9df7c90509703e4885844d0cf871ff412` remains present, prior v0.4 freeze blob `94cc1acb14fdcca623f4596c9a589e9ff42451ee`. No competing result of this exact documentary task or newer KOD writer at prewrite scan. Six attached approved Project Sources loaded; their Git blob values match SIS review: recovery `233117e1c9509d730e1f5ec532b1cabe3f786609`, roles `1772339cb74dae8550bfbd2e33401c34a929e911`, source-loading `69eb657f260a019f76e8e707c880ea88c1dfa0bf`, file-work `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`, task-conveyor `df7896d867eeeffff506319538fedad938856686`, core `a42f7dca6a7469a54fa2da24aae0da4e549c9d33`.

This is a **new file**. Exact documentary diff to a nonexistent predecessor is addition of this whole file (`/dev/null → KOD__detector-worker-trust-root-contract-r01__KOO.md`); the r0.2 code candidate, workflow, canons and sources are unchanged.

## Actors and decisions

| Responsibility | Proposed contract | Established owner/authority now |
|---|---|---|
| Event producer | A bounded detector adapter must observe an authenticated repository event and issue a versioned envelope only after immutable inbox/dispatch/artifact readback. | UNKNOWN. Current workflow records `activation_failed` and issues no r0.2 envelope. |
| Envelope attestor | Independently verifiable platform event/run identity or a signature anchored to a separately approved issuer; unkeyed SHA-256 remains only a consistency check. | UNKNOWN: no approved issuer/anchor/method. |
| Trust-profile issuer | A supervisor distinct from request initiator and handler confirms task authority, applicable source set, recovery and writer from authoritative current records, then issues one versioned scoped profile. | UNKNOWN: KOO may coordinate; its role does not appoint an operational issuer or approve new norms. |
| Trust anchor custodian | Controls accepted issuer identity/key or independent platform proof, repository identity and profile distribution; initiator/handler cannot alter it. | UNKNOWN; storage access alone gives no such authority. |
| Admission verifier | Validates provenance, exact refs, freshness and local bytes before handler, using a read-only trusted view. | PROPOSED role only; isolated r0.2 worker checks internal consistency with caller-supplied CLI trust/repo. |
| Task authority and writer authority | Must originate from their actual approved decision / Writer Gate, each under its own existing role and process. | Existing decisions govern individual tasks/writers; a standing profile-issuance power is NOT established. |
| Approved source-set authority | Operator approved set/effectivity barrier plus source-loading policy determine applicable versions; optional task-specific sources need separate approved basis. | Existing approved set is identifiable, but no automated current-set attestor is established. |

The OPERATOR must explicitly decide: **who may issue and attest the detector envelope; who may issue/revoke the supervisor trust profile; what independent anchor authenticates each and the Git repository; which authoritative ordered currentness source and revocation rule each verifier must consult; where profile issuance is recorded and which process can read it.** This candidate does not select a provider, key store, service owner or deployment mechanism. Until that decision and independent implementation verification: `TRUST_ROOT_ISSUER=UNKNOWN`, `PRODUCTION_ADMISSION=BLOCKED`.

## Contract A: event envelope and repository binding (PROPOSED)

1. Canonical bytes are versioned and domain separated (`detector-event/r01`); specify exact serialization before implementation. Include repository immutable identity, delivery/event ID, workflow identity/version, run ID and attempt, source commit, inbox path/blob, recipient, artifact path/commit/blob and dispatch path/commit, task ID and authority ref, plus payload digest. An ID must be scoped to the authenticated repository and producer; a digest alone does not authenticate its author.
2. The verifier first authenticates producer and event/run provenance against an anchor **outside** caller-supplied envelope, trust file and repository mirror. A signature with an approved pinned issuer key or an independently fetched platform attestation are candidate mechanisms, subject to OPERATOR choice and independent verification. Self-consistent fields or an unkeyed hash never count as provenance.
3. Independent read-only Git evidence verifies source commit and inbox blob; inbox exact bytes bind recipient, task, artifact and dispatch identities. The event source is checked against actual changed inbox path and authenticated event/run identity, not merely a reachable arbitrary commit. Missing run evidence, mismatched attempt, changed workflow, force/branch ambiguity or unavailable independent evidence => STOP/UNKNOWN, never handler.
4. Persistent replay key is `(repository_identity, producer_identity, event_id)`; accepted digest is committed with it. Same ID/same digest after terminal => no second handler; same ID/different digest => conflict and STOP. A reserved, partial, corrupt or unavailable record => UNKNOWN and explicit reconciliation. No automatic retry and no inference of durable exactly-once side effects.

## Contract B: supervisor trust profile (PROPOSED)

1. Profile fields: version, scope, task ID/recipient, exact authority decision ref, effective approved source-set identity and exact refs, recovery ref and exact bytes digest, writer establishment/freeze refs, repository identity, event producer anchor, issuer/anchor identity, issue generation, expiry or explicit revalidation condition, revocation/supersession pointer, and bounded handler identity. Subject to authoritative approval; merely naming these fields grants nothing.
2. Issuer authenticates the profile through an independently pinned key or attested platform channel, and immutable publication/readback pins its exact bytes. Verifier's approved anchor and repository identity come from an independently protected supervisor configuration, **never** from `--admission-trust`, `--git-repo`, the event, handler parameters or an untrusted mirror. Profile signature/authentication, audience and scope are verified before any Git fact is accepted. Issuer identity, root rotation and revocation must have a separately approved decision. Caller-controlled alternative profile/repo => STOP.
3. At admission time, issuer/verifier consult an authoritative current pointer or ordered event log with immutable readback and a monotonic generation/epoch. Confirm task decision remains executable, writer establishment remains current and predecessor freeze intact, source-set effectivity remains active. The old record's `superseded=false` is insufficient; absence of newer competing evidence must be proven from the accepted current view. Race between check and handler requires a fenced generation or revalidation at the boundary; unresolved race/conflict/outage => STOP/UNKNOWN. This is design only; no current production currentness service or fencing is claimed.
4. Source policy is applied per task: mandatory five base sources; task-conveyor canon additionally for participating chat/PROMPT tasks. Record why each topical source is required, effective approval and exact bytes. A draft or an arbitrary Git file is not approved. Source-set change invalidates old profile until a fresh independently issued generation.
5. Local recovery is read as raw bytes, not only parsed identity. Verify exact Git `commit:path → blob → raw bytes`, SHA-256 over those bytes, and `local_bytes == trusted_git_bytes` byte for byte before parsing. A matching `recovery_identity` with changed local bytes fails. If a production recovery package is a directory, the existing recovery manifest/composition/readback contract must be checked separately; one JSON ID cannot substitute for it.
6. Restrict initiator to submitting task/event locator; handler receives only admitted scoped inputs. It cannot set/replace trust profile or Git mirror. Worker executable/version, launch arguments and handler identity are themselves pinned by supervisor; otherwise a fake worker or handler can bypass admission. Technical capability does not create writer or task authority.

## Independent evidence needed before implementation acceptance

Exact OPERATOR authority decision and issuer/anchor assignment; producer event provenance from actual GitHub event/run; immutable profile bytes and independent issuer authentication; trusted repository identity and mirror sync/readback attestation; fresh authority/writer/source currentness including negative supersession evidence; exact recovery Git and local byte equality; event replay/fencing evidence. Structural file checks, source approval, task authority, external Entity processing and durable checkpoint remain distinct gates. F2 storage durability/domain HOLD remains unchanged.

## Negative documentary matrix (no tests executed)

| Case | Checker / immutable evidence required | Expected disposition; future verification |
|---|---|---|
| Forged but internally consistent event | Independent producer anchor + authenticated platform event/run and exact inbox Git bytes | `BLOCKED_UNAUTHENTICATED_EVENT`; adversarial envelope with valid recomputed SHA but absent issuer proof. |
| Valid issuer, wrong run attempt/source commit | Authenticated run ID/attempt/source commit and matching changed-path evidence | `BLOCKED_EVENT_RUN_MISMATCH`; independent run cross-check. |
| Same event ID, changed digest | Scoped persistent event-ID ledger and both exact envelope bytes | `BLOCKED_EVENT_ID_DIGEST_CONFLICT`; no second handler. |
| Forged profile with internally consistent mirror | Independent issuer root and authenticated profile bytes | `BLOCKED_UNTRUSTED_PROFILE`; test caller-controlled profile and repo together. |
| Initiator substitutes profile, repo or handler | Pinned supervisor launch config, profile identity, repo identity and handler identity | `BLOCKED_SUBSTITUTION`; verify CLI input cannot override supervisor pins. |
| Profile issued for another task/recipient or stale generation | Exact audience/scope, authoritative current pointer or ordered event-log generation | `BLOCKED_PROFILE_SCOPE_OR_STALE`; old `superseded=false` alone is insufficient. |
| Later competing authority or writer | Authoritative current view and freeze/establishment lineage at admission | `BLOCKED_SUPERSESSION_CONFLICT`; if order cannot be proven, `UNKNOWN_STOP`. |
| Source-set omitted, draft promoted by filename, or approved set changed | Approval/effectivity decision, applicable source-policy classification and exact refs | `BLOCKED_SOURCE_APPROVAL_OR_EFFECTIVITY`; reissue profile after change. |
| Wrong Git mirror with otherwise matching local profile | Independently anchored repository identity, exact object readback and sync proof | `BLOCKED_REPOSITORY_IDENTITY`; mirror failure => `UNKNOWN_STOP`. |
| Local recovery same identity, different bytes | Trusted commit/path/blob, SHA-256 Git bytes and local raw byte comparison | `BLOCKED_RECOVERY_BYTE_MISMATCH`; no normalization or identity-only acceptance. |
| Profile/repository/revocation source unavailable | Independent anchor and currentness evidence | `UNKNOWN_STOP`; no cached-profile standing grant or fallback. |
| Damaged/incomplete reservation | Scoped immutable event ledger, reservation state and independent integrity check | `UNKNOWN_STOP_RECONCILIATION_REQUIRED`; no blind retry. F2 durability still UNKNOWN. |
| Outage after handler side effect, before terminal record | External side-effect receipt/idempotency evidence plus persistent generation | `UNKNOWN_STOP`; no claim exactly-once or second attempt without explicit reconciliation. |
| Fake local marker without external Entity | External instance-specific processing evidence | `PROCESSING_STARTED_NOT_ESTABLISHED`; marker remains local evidence only. |

Each row is `DESIGN_ONLY / NOT_EXECUTED` in this task. Expected codes are proposed contract outcomes, **not** observed worker behavior. Current r0.2 worker does not implement origin authentication, trusted mirror/profile anchor or local recovery byte equality. No code, test or runtime claim is added by this document.

## Decision and STOP

Document result: `PASS_KOD_DETECTOR_WORKER_TRUST_ROOT_CONTRACT_R01_DOCUMENT_READY_FOR_KOO_REVIEW`.

Operational blocker: `BLOCKED_DETECTOR_WORKER_TRUST_ROOT_ISSUER_ANCHOR_CURRENTNESS_UNDECIDED`. KOO may review dependencies and present the above exact questions to the OPERATOR; neither this candidate nor KOO's routing creates the missing authority. The next gate is an explicit OPERATOR decision on issuer, anchors, currentness authority and revocation semantics, then independent review of the approved contract before implementation authority.

Historical PROMPT replay: no. Tests, worker/workflow edits, host/shard/provider operations, secret reads and actual Entity activation: none. Memory-layering attempt 3: `NOT_AUTHORIZED`. Existing Exchange Gate defects: `NOT_CLOSED`. Receipt, acceptance and `processing_started` do not follow from publication or dispatch.

from_entity: koder
to_entity: koordinator
project_time: omitted; trusted source not used
