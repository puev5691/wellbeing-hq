# KOD → KOO: Entity operational memory / shards convergence design r0.1

Status: PASS_KOD_ENTITY_OPERATIONAL_MEMORY_SHARDS_CONVERGENCE_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW
Class: implementation-ready design candidate; NON-LIVE; no operational authority conferred
Task: puev5691/wellbeing-hq@ff613d74e80a11dc74d15cfcdcd8f1ac122b341e:entities/koordinator/outbox/KOO__entity-operational-memory-shards-convergence-design-r01__KOD.md (blob 023165d79b3d2f7ca6aac0ef62d4529ec31f8a1f)
Writer: KOD v0.5, entities/koder/current/KOD__replacement-current-writer-v05.md (blob cf1c84f9df7c90509703e4885844d0cf871ff412)
Recovered plan: puev5691/wellbeing-hq@f13c4d4665ce0ba2f8b853f2f082b830040a2078:entities/koordinator/current/KOO__entity-operational-memory-shards-recovered-plan-r01.md (blob ffb62995588ed5af83f38465d1b7bfc3ef92cefd)
Preflight: main ff613d74e80a11dc74d15cfcdcd8f1ac122b341e; no newer competing KOD writer or task terminal observed. Approved Project Sources loaded under source-loading policy. This document is a proposal, not a change to those sources.

## 1. Causal basis and present limits

| Existing evidence | What it establishes | Boundary |
|---|---|---|
| KOO Git operational shards priority @87c278e5, blob 5b19033e | Entity → quick operational store → batch/seal/check → canonical GitHub publication/readback | Shard records convey no independent project authority |
| KOO File/Artifact and shards direction @b62896ff, blob a32d248e | Existing package assembly, manifest, SHA, archive, local readback/diff and mechanical shard gateway roles | GitHub remains canonical |
| File/Artifact Service r0.1 @bc0c6c70, tree 1f5f9349 | Candidate `parse_request` / `execute`, deterministic packaging, GitAdapter publish disabled | SHD independently failed r0.1: FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY |
| SHD independent review @b6849cd2, blob deb8c40a | Four exact defects listed below | Self-test 12/12 does not override FAIL |
| SIS shard gateway current @19c360d6, blob da804dfb | r0.3 admitted for bounded READ/VERIFY on mazhor; verify unit disabled/inactive, no listener | WRITE off, no credentials or production acceptance |
| SIS memory isolation feasibility @930e90b3, blob 8325926f | Separate process/address space and bounded broker design feasible | Feasibility is not MAIN continuation proof |
| SIS MAIN attempt 2 @7cfcfb61, blob 028a6257 | Structural verifier created bytecode inside immutable package; integrity blocked before OLD/NEW | Attempt 2 consumed; attempt 3 NOT_AUTHORIZED |
| KOO standing fixed-IP → Commander transport @59848480, blob eec04d24 | Per-action route and device selection possible after currentness/inventory checks | CONTROL_PATH_READY gives no generic host action or shard WRITE authority |

Exact source identifiers above abbreviate commit in the table for readability; full path/commit/blob are in the task's pinned inputs and the evidence section below. No CHECKPOINT_DURABLE, production continuity, or automatic writer-transfer claim follows.

## 2. Six layers and authority

1. **Governance / identity:** approved Project Sources, current-writer, exact task/action authority, immutable publication identities and supersession graph. Read fresh at admission and before any continuation; a shard cannot grant these.
2. **Operational working memory:** short-lived observations, provisional scratch, active cursor drafts and diagnostic traces in an explicitly scoped operational shard. Never authoritative alone; expiry/retention remains policy input, not invented here.
3. **Current task state / checkpoint:** sealed, content-addressed checkpoint: exact task version, completed prefix, causal cursor, last verified result, dependencies, unresolved conflicts, next admissible action reference and hashes of selected working records. A current pointer is CAS/fenced; a published canonical anchor is required for replacement admission.
4. **Experience:** verified reusable lessons with provenance, verdict and scope; candidates stay candidates until the existing experience process accepts them.
5. **Library / durable knowledge:** immutable or versioned documents, source indexes and selective retrieval references; exact bytes/digests pinned. A summary is an index, not a substitute for mandatory source bytes.
6. **Canonical GitHub evidence:** task authority, approved sources, writer state, terminal results, accepted checkpoints, significant decisions and immutable package manifests/results with publication/readback. GitHub is project truth; shard data can be useful operational evidence only under a canonical anchor and exact identity checks.

The distinction is deliberate: frequent operational writes can stay on shards until promotion, but a replacement must STOP if the only claimed last result/current authority exists on a lost or conflicting shard. RPO/RTO and retention are UNKNOWN pending explicit decision; no durability claim is made by naming a checkpoint.

## 3. Record and interface contract

Proposed canonical serialization: UTF-8 JSON with documented canonical key ordering and byte encoding, schema_version, record_kind, record_id, entity_id, task_id, task_version, writer_id, writer_epoch/fence, parent_digest, generation, created_at with timezone or explicit UNKNOWN, source_refs (exact repo/commit/path/blob or content-addressed shard locator), payload_digest SHA-256, payload_size, state (PROVISIONAL/SEALED/PROMOTED/SUPERSEDED), supersedes_refs, authority_ref, expiry_policy_ref and integrity envelope. Compute the record digest over exact canonical bytes excluding its own digest/signature fields; define algorithm/version in the schema. No secrets, visitor content or arbitrary transcript.

- `append_operational(record, expected_parent, fence, idempotency_key)` proposes an immutable object write; acknowledge object digest and byte count. A repeated same key + bytes returns the same receipt; conflicting bytes fail.
- `seal_checkpoint(task, expected_generation, previous_pointer_digest, record_set, authority_refs)` validates chain, evidence and fence and proposes a new immutable checkpoint; separate CAS publishes current pointer. Never infer pointer success from object-write success.
- `verify_exact(locator, expected_digest, size, generation)` independently reads exact bytes and returns verified/missing/mismatch/unavailable, without mutation.
- `publish_canonical(package, manifest, authority)` uses the existing File/Artifact Service after correction and independent review, then exact Git commit/tree/blob readback; a promotion record links shard digest and canonical identities.
- `retrieve_selective(bootstrap_refs, allowed_exact_refs, query, budget)` emits an append-only trace of each exact reference, bytes and reason. Unknown locator, full corpus and checker-private/oracle are denied.

These interfaces are PROPOSED, not claims of deployed API compatibility. r0.3 gateway's exact-root allowlist, bounded Git object READ/VERIFY, no-follow and command-scoped safety are reusable for verifying canonical Git evidence where applicable; its WRITE is disabled. An operational shard writer, CAS/pointer implementation, trust root, binding to exact task authority, retention and failure semantics need separate design, authorization and independent verification. No silent shim may turn r0.3 READ/VERIFY into WRITE.

## 4. File/Artifact Service correction gate

Use a correction-only successor of the existing r0.1 service, preserving package/manifest/readback API where possible. Its independent SHD FAIL requires all four fixes before relying on it:

| Defect | Required correction and negative check |
|---|---|
| Published MANIFEST byte/size mismatch (11/12) | Generate inventory after final bytes are fixed; verify each SHA-256 and size against actual committed blob bytes on immutable readback, fail if any differ. |
| `target_path=MANIFEST.json` collision | Reject generated/reserved names and their normalized aliases before package construction; no overwrite. |
| `prior_manifest_path=../outside.json` escape | Exact safe relative path, root containment and no symlink traversal before access; reject escape/absolute paths. |
| String `create_archive="false"` accepted as truthy | Exact Boolean type; `prior_manifest_path` exact null or safe string; reject coercion and wrong types. |

Independent SHD re-review is a gate. A self-check or rewritten manifest after commit is insufficient. The service can assemble and verify a package, but does not itself authorize GitHub publication, shard WRITE or checkpoint durability.

## 5. Event routing and promotion

| Event class | Initial location | Canonical promotion rule |
|---|---|---|
| Provisional notes, retrieval-cache indexes, local health and timing counters, unverified hypotheses | Shard-only with task/fence/expiry, if separately admitted | No project truth; loss may require recomputation. Do not use as last verified result. |
| Sealed intermediate checkpoint before a replaceable boundary | Shard immutable object and CAS pointer | Publish exact checkpoint/manifest/readback to GitHub before claiming a replacement can recover that boundary. |
| Task authority, writer change, approved source version, supersession/conflict decision | GitHub canonical | Must already be canonical and fresh; shard mirror only. |
| Independently verified result, terminal verdict, accepted reusable experience/knowledge, externally reviewable package | GitHub canonical with exact readback | Mandatory; shard index may reference exact commit/blob. |
| Failed test or diagnostic with causal importance | Bounded shard trace; significant failure summarized with exact provenance | Canonical publication if needed for a new gate, successor task, or preserving why work stopped. Never promote unsupported conclusion. |

Any shard/Git mismatch, divergent pointer generations, missing exact evidence or expired authority yields BLOCKED; never choose a convenient branch by recency alone. If GitHub is temporarily unavailable, collect only explicitly permitted provisional state; do not announce canonical promotion, durable checkpoint or new writer admission.

## 6. Minimal future synthetic E2E pilot (DESIGN ONLY)

Pilot identity `EOM-SHARD-PILOT-R01`, distinct from the consumed memory-layering attempts; no authority is created here. Use an isolated deterministic synthetic multi-step task with frozen input bytes and predeclared rubric, prefix of three steps and remaining suffix. The independent oracle and expected final result live solely in supervisor-private storage; NEW gets neither. The pilot must exercise an operational shard write, File/Artifact packaging and canonical checkpoint anchor, exact readback, selective retrieval and continuation. No real Entity state, production recovery registry or current-writer mutation.

1. **Admission:** pin six approved sources, exact task/input, writer/worker scope, recovery package, corrected File Service and shard interface versions, authorities and bounds. Check no competing writer/result and no stale source. Future execution needs new separate authority; memory-layering attempt 3 remains NOT_AUTHORIZED.
2. **OLD:** separate fresh process runs only prefix, emits evidence and cursor=3; supervisor verifies and freezes OLD. Seal exact checkpoint containing task version, causal cursor, prefix digest, last verified result, dependencies, knowledge/experience refs and next permitted step reference.
3. **Anchor:** independent readback of shard object/pointer and canonical Git package/commit/blob; compare exact digests and generation. A partial object write or unconfirmed CAS is UNKNOWN, not durable. If an anchor is absent, STOP before replacement.
4. **Fresh NEW:** separate address space, explicit allowlisted environment and no inherited transcript, variables, cache, package root, checker-private/oracle, project credentials or writer authority. Bootstraps pinned mandatory sources and exact anchor only through an allowlisted broker; no arbitrary network.
5. **Restore:** structural/integrity verifier runs from a separate read-only projection/tool state, with Python bytecode disabled (e.g. `-B`), no write capability to the immutable package. NEW retrieves only needed exact state, task and knowledge/experience refs, records read/byte budget and submits semantic restoration report before continuing.
6. **Gate:** independent structural PASS and semantic restoration PASS are both required. The report must identify exact task, task version, cursor=3, last verified result, dependency state, selected knowledge/experience, unresolved conflicts and next authorized step. Missing/contradictory evidence yields STOP/BLOCKED.
7. **Continue:** NEW executes suffix only; ledger records step IDs, prior result refs, duplicate-prefix guard and final digest. Independent checker with private oracle verifies final output and ledger. No automatic project acceptance, no automatic writer transfer.

Reuse the existing preparation contract's bounded retrieval pattern (exact allowlist, default minimal refs, max 32 semantic reads, 262144 payload bytes, six mandatory sources separately accounted) as a design constraint subject to fresh version admission; no full-corpus/transcript default. The previous broker sentinel budget=4 versus seven required reads is a known historical correction issue: future admission must prove all required exact reads fit within policy and actual broker loop. Computation deadline <=5 s only if independently feasible for the new exact pilot, not silently widened. No MAIN execution or negative-case execution is authorized by this document.

## 7. Measurements and acceptance boundaries

Instrumentation, with immutable event IDs and monotonic timestamps where available: shard writes/reads, bytes, retries/failed CAS, checkpoint seal/readback latency; GitHub fetch/read and publication counts/bytes, commits/trees/blobs, readback latency; File Service package bytes and verification failures; semantic retrieval count/bytes/reasons; OLD/NEW active and elapsed times; duplicate prefix executions; OPERATOR retelling count (manual task/history restatements required for NEW to continue), decision/authorization touchpoints separately. Report baseline with direct Git operational writes/readbacks under an equal synthetic workload versus converged pilot; disclose cold cache, timing and failures. Target observation is exact restoration and continuation with zero historical OPERATOR retellings and zero repeated completed prefix; traffic reduction is measured, not assumed. A single PASS is one bounded observation, not general Fast Memory or production continuity proof.

Verification matrix for independent reviewers: stale writer/task/source; missing or conflicting shard pointer; object write without CAS and CAS without verified object; Git/shard digest mismatch; lost provisional shard; unknown locator/full corpus/oracle request; expired fence; package mutation attempt by verifier; bytecode generation; seven allowed reads and full 32-read boundary versus 33rd denial; byte limit; duplicate prefix; missing exact last result; unverified experience promoted as accepted; unauthorized writer or host mutation. Expect explicit BLOCKED/FAIL, with separate structural and semantic reports.

## 8. Ordered next gates

1. KOD correction-only File/Artifact Service successor fixing four SHD defects, immutable package and exact committed-byte manifest verification; SHD independent re-review.
2. Separate scoped operational shard store/CAS/fence/trust contract and authority decision; SIS/SHD independent review. r0.3 stays READ/VERIFY-only until separately authorized and proven otherwise.
3. KOD/SIS isolated harness correction: immutable package presented physically read-only to verifier, tool state outside it, bytecode disabled, actual broker request capacity aligned with admitted limits; independent SHT/ARH integrity/preservation review.
4. KOO/OPERATOR decide explicit one-shot synthetic pilot authority after fresh admission. Execute once only in a separate task. Reconcile result and metrics, then decide any production proposal.

**One next implementation step:** correction-only File/Artifact Service r0.1 successor plus independent SHD re-review. It is a prerequisite to trusting package identities; this document does not implement it. No backend, owner, retention, RPO/RTO, generic Commander action or automatic promotion authority is selected.

## Evidence / scope declaration

Pinned inputs: KOO task @ff613d74e80a11dc74d15cfcdcd8f1ac122b341e blob 023165d79b3d2f7ca6aac0ef62d4529ec31f8a1f; plan @f13c4d4665ce0ba2f8b853f2f082b830040a2078 blob ffb62995588ed5af83f38465d1b7bfc3ef92cefd; KOO shard priority @87c278e5d99f102b9c148104a56e5009ab49a005 blob 5b19033eff68f5409992631e38adc9bbd759fa2e; KOO File/Artifact direction @b62896ff271ab0480a4ff1fcecef386a7c65b1b6 blob a32d248e6296ab3a0ba07ca07e6d163bf6d3c0ee; SHD FAIL @b6849cd2aa9d45fea823b06f05d45053d968d2cb blob deb8c40ada7f713a6423dbb9aa83448b0b1f505e; SIS gateway @19c360d694f2274236942b9e8f4b792003a13bcd blob da804dfb646c4da25c431771c0a2f0b2b2c30ea3; SIS isolation @930e90b32dddb33aad133d8303ecaa6b49348f42 blob 8325926f7556aa22612f5bf6ab3952cb6645091a; SIS attempt 2 @7cfcfb611dd9e1a66fcb5dd2ff4e460fb8003a86 blob 028a6257ae96be5b740e5d0d351586fdb6e702f2; standing transport @59848480752f5096d07866e747bf894c3559270a blob eec04d2439b6b866ae07cd3930ceb5013ba4231c.

No implementation, tests, live shard/host/provider call, attempt 3, deployment, production migration, Project Sources/canon/current-writer mutation, automatic writer transfer, or CHECKPOINT_DURABLE claim occurred. Result is ready for independent review, not accepted architecture or execution authority.
