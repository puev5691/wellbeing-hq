# КОДЕР → КООРДИНАТОР: автономный конвейер Сущностей, сквозная спецификация r0.1

status: `NON_LIVE_SPEC_CANDIDATE_FOR_KOO_REVIEW`
scope: design/spec only; implementation=0; provider_calls=0; host_mutation=0; secrets=0
project_time: omitted; trusted project-time source not used

## Человеческий смысл

Желаемый конвейер хранит оперативный ход задачи в быстром внешнем контуре, создаёт новый вычислительный экземпляр по разрешённому событию и продолжает ту же задачу после проверенного восстановления. В GitHub сохраняются отобранные долговечные результаты и доказательства, а ОПЕРАТОР получает вопрос только там, где меняется цель, возникает конфликт или требуется отдельное решение. Это целевая спецификация, не существующая сквозная система.

Сейчас доказаны отдельные части: GitHub inbox detector фиксирует событие, activation-worker v0.2 прошёл изолированные тесты проверки immutable входов, shard gateway на mazhor ограниченно подтверждён как VERIFY-only, layered memory имеет концепцию L0–L5 и синтетический пакет. Entity Runner r1 — non-production candidate; provider-side запуск не доказан. MAIN memory-layering attempt 2 завершён до OLD-01 из-за integrity failure, attempt 3 NOT_AUTHORIZED. GitHub событие и synthetic PASS не доказывают новый живой processing instance.

## Fresh authority / source basis

- HQ preflight before specification: `puev5691/wellbeing-hq@25e25cb397035f5cac217c4a9f8ff31b101635b2`; complete tree 5177 entries, truncated=false; no competing KOD current-writer or existing terminal for this new spec scope found.
- Current KOD writer: `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`; v0.4 freeze blob `94cc1acb14fdcca623f4596c9a589e9ff42451ee`.
- Exact task authority: direct current OPERATOR instruction in this chat, bounded to a non-live specification, immutable publication and KOO result. It does not authorize a new implementation or any runtime operation.
- Approved governing set loaded: recovery v1.6, roles v2.4, source-loading v2.2, file-work v2.4, task-conveyor v1.2, core v2.5. Project Sources attachment names alone do not grant authority to alter them.
- Recent HQ commits before this task concern independent F1/F2 engine review; no superseding autonomous-conveyor terminal found. Historical activation/product attempts remain evidence, not executable PROMPT.

## Existing components and exact boundary

| Link | Evidence and actual scope | State |
|---|---|---|
| GitHub inbox detector | `.github/workflows/entity-activation-detector.yml` blob `f6a3f2eb8bd2e65d7b09f733a66d7da9489770a0`; KOD activation E2E result blob `072cf12e596abf286e241350969188d2dc72a50e`. GitHub push detected; emitted activation_failed and processing_started=no. | VERIFIED detector; BLOCKED real processing |
| Activation worker v0.2 | README blob `6889ef0d4b6ac613cbbb351ebe85c6fdb55edeb0`; SIS isolated E2E blob `1c215a3e21e4cfb336678c6e53193545b9fb96dd`, 8/8 PASS. Verifies exact commit/blob, provider/local bytes and dispatch binding against read-only mirror. | VERIFIED isolated only; integration CANDIDATE |
| Shard gateway | r0.3 adapter README blob `bec51bb593fe6a428dbab866234dd6abe97f751d`; SIS mazhor current readback blob `da804dfb646c4da25c431771c0a2f0b2b2c30ea3`. Oneshot VERIFY-only, no observed listener, WRITE rejected. | VERIFIED bounded read-only host state; BLOCKED operational write |
| Layered memory | KOD L0–L5 concept blob `a6cf322eb7db02208457b09d71ea3204dbc39f09`; synthetic design blob `b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0`; SIS attempt-2 result blob `028a6257ae96be5b740e5d0d351586fdb6e702f2`. | CANDIDATE architecture; BLOCKED real E2E; attempt 3 NOT_AUTHORIZED |
| Entity Runner | r1 README blob `7243bcca017385b51d04c50eb0f6c8b31fb4f7ab`; SIS host readiness blob `5d4ade030ed9b413145ad822936ae9f1b85c4560`; KOO provider gate blob `669d01c6c9b3d87bc3707d410b431c488ad87782`. Package selected one provider for its own historic experiment, not this architecture. | CANDIDATE; provider execution BLOCKED |
| Event/approval glue | No evidenced single transaction joining checkpoint → archive/recovery → task authority → spawn → start-ack → continuation → result/receipt. | UNKNOWN |

This spec neither reuses historic one-shot authority nor selects Claude, OpenAI or another provider. Existing provider-specific package is evidence of one candidate interface only.

## Proposed interfaces (no implementation claim)

Shared immutable envelope `EntityEvent`:
`schema_version, event_id, entity_id, task_id, task_version_ref, instance_id?, writer_scope, worker_scope, authority_ref, source_ref, causal_parent_ids, event_type, checkpoint_ref?, recovery_ref?, artifact_ref?, body_digest, sequence, project_time_source|unknown`.
Producer signs/attests provenance according to separately chosen trust boundary; consumer checks immutable identities and monotonic per-task sequence. `event_id` + `task_id` + `sequence` are dedupe keys. A duplicate with different digest stops as conflict. This is a proposed contract, not an assertion about deployed formats.

1. **Task admission** `TaskIntent{task_id, revision, recipient, exact_authority, objective, constraints, stop_conditions, input_refs, decision_gates}` → `TASK_ADMITTED | WAIT_AUTHORITY | BLOCKED_CONFLICT`. KOO may choose only a task whose authority already exists. Objective drift creates `OPERATOR_GOAL_REVIEW_REQUESTED`, never silent reinterpretation.
2. **Operational checkpoint** `CheckpointPut{task_id, revision, cursor, L1_ref, L0/L2 causal refs, current_writer_ref, previous_checkpoint_digest, event_id}` → `CheckpointAck{durable_ref, digest, generation, independently_readable}`. Proposed shard write API requires explicit authority, authenticated caller, compare-and-swap generation, stable failure semantics, and preservation/retention decision. Existing mazhor VERIFY-only gateway does **not** implement this put or durable ack.
3. **Promotion for long-lived GitHub** `PromoteCandidate{verified_task_result_ref, provenance, class, redaction_review, preservation_policy_ref, expected_blob_hashes}` → `PROMOTED_COMMIT_READBACK | REJECTED | WAIT_REVIEW`. Only a verified result/decision, approved source/current-state version, recovery snapshot with manifest/checksums, or compact provenance index meeting its approved preservation rule may be promoted. Raw prompts, transient retries, secrets, private data, unreviewed hypotheses, and high-frequency operational checkpoints do not become GitHub project authority merely by being present. ARH owns preservation checks; current writer owns its self-state. Promotion policy, reviewer and retention are UNKNOWN pending exact approval.
4. **Activation request** `ActivationRequest{task_id, task_revision, exact_authority, recovery_locator+version, current_writer_ref, desired_worker_scope, spawn_bounds, provider_selector_unset, request_id}` → `ADMISSION_DENIED | WAIT_OPERATOR | SPAWN_ACCEPTED{attempt_id}`. Detector only proposes intent; KOO/supervisor validates supersession, writer/worker boundary and one-use/standing authority before any create call. Provider selection requires explicit capability/price/privacy/authorization decision; none is default here.
5. **Runner binding** `SpawnAccepted{attempt_id, provider_run_id?, fresh_instance_id, provider_contract_ref}` → `BootstrapVerified{manifest, source_versions, checkpoint_digest, recovery_readback, isolation_evidence}`. A new process cannot claim continuation of exact prior chat, inherit writer authority, or receive oracle/secrets by default. Reader fetches mandatory approved sources, verifies exact recovery and L5/L1, then retrieves only task-relevant L4/L3/L2/L0 under budget.
6. **Actual start proof** `ProcessingStartAck{attempt_id, task_id, fresh_instance_id, authority_ref, validated_checkpoint_digest, first_allowed_work_step_ref, observed_runner_state_ref}`. Supervisor correlates provider/service evidence of running computation **and** first authorized task-specific work step after final revalidation. An HTTP accepted response, queued task, detector PASS, session ID alone, or GitHub dispatch cannot set `processing_started=yes`. Provider-independent readback semantics must be proven on chosen runtime.
7. **Continuation/terminal** `Progress{checkpoint_generation, cursor, evidence_refs}` and `Terminal{PASS|FAIL|BLOCKED, objective_review, result_ref, worker_scope, resource_usage}`. Resume at recorded cursor; no prefix replay. Requester review, independent verification when required, and separate project acceptance remain distinct. Result is immutable-published/read back then addressed with explicit receipt.

## State machine and human gate

`DETECTED → TASK_ADMITTED → CHECKPOINT_DURABLE → ACTIVATION_REQUESTED → SPAWN_ACCEPTED → BOOTSTRAP_VERIFIED → PROCESSING_STARTED → RESULT_PUBLISHED → RESULT_RECEIVED → REVIEWED/ACCEPTED`.

Every arrow has event ID, actor, exact authority, readback or observed evidence and retry/timeout policy. `WAIT_OPERATOR`, `BLOCKED_CONFLICT` and `ACTIVATION_FAILED` are explicit branches. No transition inferred from mere file creation.

OPERATOR gate fires when: task goal/priorities conflict or drift; approved sources conflict; supersession/writer conflict cannot be resolved; new provider/account/billing/privacy scope; missing standing authority; high-impact host/production mutation; acceptance reserved for human. KOO packages one concrete decision with alternatives/evidence; OPERATOR is not a mandatory transport for every routine handoff once a technically proven, exactly scoped automatic activation authority exists.

Artifact lifecycle is independent of run lifecycle:
`created → published → addressed dispatch → recipient receipt → acknowledgement → substantive acceptance`.
Instance lifecycle is `wake_detected → wake_routed → activated → processing_started → task_completed`.
A receipt means version access, not approval. GitHub inbox/dispatch is neither chat activation nor runner processing. Both lifecycles must be cross-referenced by exact event/attempt IDs.

## Failure and recovery

- Crash before durable checkpoint ack: reject unacknowledged cursor and resume only from last externally read-back verified checkpoint; pending work may need human reconciliation. Never synthesize missing state.
- Crash after ack before start: dedupe `request_id`, reconcile whether provider run exists, do not issue another provider call without authority and retry allowance. If provider state unavailable, `BLOCKED_UNKNOWN_ATTEMPT`.
- Crash during run: compare durable checkpoint generation and run/lease state; old worker must be fenced before new one writes. Lease expiry by itself cannot establish writer transfer.
- Shard unreachable/corrupt: stop continuation, consult last independently preserved recovery, label freshness/staleness; no promotion of unverified transient state to authoritative state.
- GitHub publication fails: checkpoint remains operational only, result not claimed externally preserved. If promotion succeeded but readback fails, state `PUBLISHED_UNVERIFIED`; no recoverability claim.
- Conflicting task revisions or competing writers: stop, require exact authority resolution; no commit-time last-write-wins. Missing mandatory source or supersedes evidence → BLOCKED.
- Rate limits, deadlines, network failures and retries: bounded by separately authorized contract. No invisible repeated provider invocation. Emergency failover follows existing recovery canon and distinct writer gate, never automatic from worker availability.

## GitHub as project truth: clarification gate

Current approved recovery v1.6 explicitly allows GitHub as an external versioned contour but says it is **not the sole or final file field**. Task conveyor v1.2 defines an information field including GitHub, approved Project Sources **and other authorized sources**. Thus there is no verified rule here that all transient project truth must already be committed to GitHub. Proposed fast shard checkpoints can be evidence of operational state only if integrity, visibility, retention, authority and recoverability are approved and verified. They cannot silently supersede approved sources, immutable GitHub decisions/current-writer, or ARH registry.

The unresolved governance detail is precise: who may approve a shard checkpoint as operationally authoritative; how shard state and GitHub conflict/supersede; which results must be promoted; how long raw operational events live; what to do during split-brain/unreachable shard. KOO must route that policy choice to the competent approved decision process; this specification changes no canon or Project Source.

## Per-link next gate matrix

| Link | Missing authority / evidence | Minimal bounded verification |
|---|---|---|
| Shard operational writes | Write mode disabled; no approved durable checkpoint ownership/retention | Separate design and authorization for authenticated CAS put/ack/readback; isolated synthetic test, no production write |
| Layered memory → shard | Concept, but no exact serialized production L0–L5/schema/index and privacy/retention contract | One schema/interface alignment and negative-case test against current approved preservation |
| Detector → worker | Detector PASS and isolated worker PASS, but no proven live trigger-to-worker invocation | Authorized isolated event → real worker start trace with exact event/attempt IDs, no provider |
| Worker → Runner | Package candidate; entitlement/credentials and one-shot provider permission missing; provider unchosen for this architecture | Provider-neutral adapter selection + bounded runtime admission design; later separate live gate |
| Runner → processing_started | No proved provider-neutral event/correlated task-first-step evidence | One separately authorized isolated end-to-end test with provider/service readback; fail closed |
| Restoration → same task | Synthetic MAIN attempt 2 failed pre OLD-01; attempt 3 absent | Independent resolution of harness cause and separate future authority; do not run attempt 3 here |
| Result → GitHub/receipt | Git publication/readback and dispatch exist individually; automatic promotion, privacy filter, reviewer and receipt are not integrated | Offline promotion decision table and route-state negative tests; independent review |
| Operator goal checkpoint | No approved scope for unattended goal changes or general standing automation | KOO/OPERATOR define exact delegated routine scope and human decision boundary before runtime |

## Next causal gate

KOO should independently review this one non-live interface specification against existing component owners (SIS runtime/gateway boundary, ARH preservation boundary, SHT cross-stage/task continuity) and choose **one** separately bounded first interface verification. Do not infer permission for shard write, provider call, auto-spawn or production from this document. No implementation, host change, secrets, provider selection/call, Project Source/canon mutation or memory-layering attempt 3 occurred.
