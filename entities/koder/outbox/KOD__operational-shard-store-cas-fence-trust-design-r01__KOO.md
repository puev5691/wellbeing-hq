# KOD → KOO: operational shard store / CAS / fence / trust contract r0.1

terminal: PASS_KOD_OPERATIONAL_SHARD_STORE_CAS_FENCE_TRUST_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW
status: DESIGN_CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY
project_time: omitted
authority_semantics: none
project_state_semantics: none

## 0. Основания и граница

Exact task: puev5691/wellbeing-hq@49a73057dff76ce5a86dedb9bd91fa0cd671a25a:entities/koordinator/outbox/KOO__operational-shard-store-cas-fence-trust-design-r01__KOD.md; blob `99f6ce36542e5f6928f1fd0f34585d6e14146398`.

Exact authority: puev5691/wellbeing-hq@5d9916df3f3e3c320a64e7396db6e6640f39eae8:entities/koordinator/outbox/KOO__authorize-KOD-operational-shard-store-design-r01__OPERATOR.md; blob `d5fcf6b04901818a1c1fce6dd09d2cc5af8be7c3`. Writer: `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`. Fresh HQ preflight: `49a73057dff76ce5a86dedb9bd91fa0cd671a25a`, tree `7a6b487dfb1ba8ea3751f6e4e381fa0bc6f54bb6`; no later competing KOD writer/task terminal at this preflight. Six attached approved Project Sources loaded according to source-loading policy.

Causal inputs:
- Recovered plan @f13c4d4665ce0ba2f8b853f2f082b830040a2078, blob `ffb62995588ed5af83f38465d1b7bfc3ef92cefd`: GitHub significant canonical evidence; shard is operational memory.
- Convergence design @e90b9bd65e569d97e7497122c80808759dc4ce9e, blob `d760a8289ec14d16059c54f579ffe5172fd3625b`: six layers, promotion, selective retrieval, proposed store boundary.
- SHT review @a9ea81332d2e9164bb836984fe8989567bbfa46d, blob `949a7ec8158c20a52c0815aa38c3f1e36566f100`: `BLOCKED_SHT_EOM_SHARD_PILOT_R01_CAUSALLY_OVERLAPS_UNAUTHORIZED_MEMORY_LAYERING_ATTEMPT_3`. EOM execution remains blocked; this store design cannot reclassify an attempt by naming it differently.
- File/Artifact Service r0.2 package @b5218dc8c074108b80d7e97f537fe5faf0d9a8e2, tree `b7214594e63303533ade103bf9e627d0cce69504`; independent SHD reverify @d5e9ee10d89fe3e498529824cd7354a469ce99e5, blob `7b57aa4afd7f030b4b3b0f123333b5b6631f850e`, `PASS_SHD_FILE_ARTIFACT_SERVICE_R02_INDEPENDENT_REVERIFY`. This clears four predecessor defects for this bounded component, not store/deployment authority.
- SIS gateway state @19c360d694f2274236942b9e8f4b792003a13bcd, blob `da804dfb646c4da25c431771c0a2f0b2b2c30ea3`: installed r0.3 bounded READ/VERIFY on mazhor, disabled/inactive verify unit, no listener, WRITE off, no credentials, no production acceptance.

The contract below is PROPOSED. Neither operational shard store nor CAS/fence trust service is verified or authorized for implementation. `CHECKPOINT_DURABLE` is NOT_ESTABLISHED.

## 1. Objects, bytes and identity

Namespace is the exact tuple `(entity_id, task_id, task_version, stream_id)`. A task version is an immutable task artifact identity, not a human title. Every locator is scoped to that tuple and to an admitted store/profile version; cross-task or cross-Entity reads/writes are denied.

`OperationalRecordV1` immutable envelope has exactly:
- `schema="operational-record-v1"`, `record_kind` from a closed set `WORKING_NOTE|STEP_EVIDENCE|CHECKPOINT_CANDIDATE|PROMOTION_RECEIPT|CONFLICT_EVIDENCE`;
- `entity_id`, `task_id`, `task_version` (exact repo/commit/path/blob or equivalent immutable reference), `stream_id`;
- `writer_id`, `writer_epoch` (opaque externally attested monotonic fence identity), `authority_ref`, `trust_profile_ref`, `approved_sources_ref`;
- `generation` positive integer, `parent_digest` (null only genesis), `payload_sha256`, `payload_bytes`, `payload_media_type`;
- `state_class` from `PROVISIONAL|SEALED_CANDIDATE|PROMOTION_EVIDENCE`; `source_refs` exact locators, `supersedes_refs` exact digests, `policy_ref` and `expiry_class` with no invented duration.

No secret, credential, private visitor content, transcript, oracle or unrestricted filesystem path in envelope or payload. Provisional hypotheses explicitly marked unverified; content cannot assert writer authority or acceptance. Unknown source/ref stays UNKNOWN and cannot be silently reconstructed. The record ID is `sha256:<hex(SHA256(exact envelope bytes))>`; payload digest binds raw exact payload bytes. The digest is computed over a closed envelope without a self-digest field. For interoperable first implementation, prescribe UTF-8 JSON, no BOM, sorted keys by Unicode scalar value, compact separators, one final LF, integer-only numbers, reject duplicate keys/NaN/floats and unknown keys; serialize and reparse to compare canonical bytes. This is a **proposed versioned byte contract**, not an assertion that an existing runtime implements it. If a different cross-language canonicalization is chosen in independent review, version the schema and vectors before any WRITE.

Immutable object locator: `store_id/namespace/schema_version/record_id` with path components encoded/allowlisted, never directly taken from arbitrary input. `PUT_IMMUTABLE` accepts exact bytes, content digest, size and a scoped operation ID; same ID + same bytes returns the first receipt; same ID + different bytes is `IDEMPOTENCY_CONFLICT`. The object is written atomically or the operation remains UNKNOWN; a successful receipt proves only object persistence/readback within the admitted local store contract, not CAS, Git publication or durability under failure. A returned receipt binds operation ID, namespace, record ID, bytes, digest, store profile and verification evidence.

## 2. Current pointer and CAS

Pointer key: exact `(entity_id, task_id, task_version, stream_id)`. Value: `{generation, record_id, parent_record_id, writer_epoch, fence_ref, task_authority_ref, profile_ref}`. Immutable object and mutable pointer are separate operations. Initial pointer is explicit ABSENT generation 0. `COMMIT_CURRENT_CAS` inputs include scoped operation ID; exact expected full prior pointer or ABSENT; proposed record ID; new generation = expected generation + 1; current externally verified fence; task/source/writer evidence refs. Before atomic commit, VERIFY object bytes/digest/namespace/parent/generation and fresh authority; reject if any mismatch. Compare full prior value atomically, never last-write-wins or recency selection. Pointer receipt binds request digest and actual poststate.

Dedupe is **operation-specific**: a repeated `PUT_IMMUTABLE` checks object request/bytes; a repeated `COMMIT_CURRENT_CAS` checks full expected prior pointer, proposed pointer and authority/fence request. Same operation ID with altered data fails; a different operation ID does not inherit another operation's success. If response is lost, `RESOLVE_OPERATION` reads that exact operation's durable outcome plus exact object/pointer poststate. It returns APPLIED, NOT_APPLIED, CONFLICT or UNKNOWN; UNKNOWN never implies retry success or a right to continue. A record without pointer is an orphan candidate, safe to inspect/GC only after policy; a pointer without verified object is BLOCKED_INTEGRITY. Object write and CAS are not falsely described as one atomic action. A lost CAS response must not be guessed from current pointer alone if a later writer has advanced it: retain an operation-bound ledger or answer UNKNOWN.

Concurrent writers reading generation N: only one CAS can commit N+1. The loser receives `CAS_CONFLICT`, reconciles exact current pointer and obtains fresh authority before any new proposal; no automatic winner by timestamp. Divergent forks are preserved as evidence, not merged by the store. A task-version supersession or competing current writer invalidates old writers even when their numeric generation was plausible.

## 3. Fence and trust root

The shard **verifies** externally established authority and can enforce a fence; it cannot issue task authority, writer status, approved source status or a writer handoff. Admission inputs:
1. exact immutable current-writer and freeze/handoff evidence from canonical project field;
2. exact current task authority and its recipient/scope, task version and supersession check;
3. exact approved source-set identity and recovery/currentness when applicable;
4. a separately approved, versioned `SupervisorTrustProfile` mapping trusted Git provenance, authorized attestor identity/key/verification method, store namespace, allowed operations, scope and revocation rules;
5. a `WriterFenceAttestation` binding entity/task/version, writer instance, monotonic epoch, authority/profile/source refs, validity/revocation evidence and signature/MAC checked under that trust profile.

The profile must be authenticated by a root **outside the shard**; a Git mirror path, shard file, request-supplied public key, or unsigned JSON cannot declare itself trusted. Replacement requires canonical Writer Gate/handoff plus a new externally attested epoch strictly above stored high-water mark. Freeze/revocation invalidates prior epoch; store atomically persists high-water fence alongside CAS guard and rejects any lower/equal incompatible writer epoch. Same writer/epoch with a differing attested identity is conflict, not renewal. If canonical authority cannot be freshly checked, the profile is stale, the attestor cannot be authenticated, or source versions changed: fail closed before mutation.

**UNKNOWN requiring explicit decision:** owner/issuer of SupervisorTrustProfile, attestor and root key custody, epoch issuer and revocation channel, trustworthy freshness bound and availability behavior, and the authorized store operator/backend/host. KOD does not appoint them. Before implementation/admission, OPERATOR/KOO must record those owners and exact authority, then SIS/SHD independently verify trust-root and fence implementation. Without an authentic monotonic fence and trustworthy Git currentness, `WRITE/CAS = BLOCKED_TRUST_ROOT`.

## 4. Operations and gateway compatibility

| Operation | Proposed successor store behavior | Existing r0.3 gateway |
|---|---|---|
| READ_EXACT | Scope/locator allowlist; return exact bytes, digest, size, object/pointer generation and provenance; missing is distinct from unavailable. No full-corpus default. | Existing bounded Git object READ may verify canonical refs where exact root/opcode allowlist admits them; it does **not** read a new store automatically. |
| VERIFY_EXACT | Independent digest/size, namespace, parent chain, CAS pointer and trusted canonical anchor comparison; verifier uses read-only capability and separate state. | Existing Git READ/VERIFY safety properties are reusable at its admitted scope; not a checkpoint durability proof. |
| PUT_IMMUTABLE / COMMIT_CURRENT_CAS | Requires separate successor component, trust profile, scoped write authority, isolated store and independent review. | WRITE disabled. No conversion of READ/VERIFY into WRITE by configuration inference. |
| ROUTE | Select exact admitted locator/node/profile; outcome is addressability, not permission to run a command or switch authority. | Gateway r0.3 must not be treated as an arbitrary routing or host-command service. Standing fixed-IP→Commander transport requires per-action authority and does not grant store mutation. |

Trust domains remain distinct: Entity requester, supervisor/attestor, store mutation process, read-only verifier, File/Artifact Service, GitHub publisher. No shared mutable package access for an independent verifier; read-only projection and tool state outside checked bytes. No arbitrary network or filesystem locator expansion. Deny unknown path, symlink traversal, full corpus, checker-private/oracle, credential-bearing records and unadmitted backend profile. No hidden GitHub publication in service execution path.

## 5. Lifecycle, loss and canonical promotion

`PROVISIONAL` notes/telemetry may remain shard-only within an explicit task/policy scope; loss is disclosed and recomputation may be possible. They cannot support a replacement's last verified result or authority. `SEALED_CANDIDATE` requires exact object chain, CAS receipt and independent readback, but is still not a canonical checkpoint or `CHECKPOINT_DURABLE`. An intended replacement boundary, verified terminal result, current task/writer/authority/source change, significant decision or reusable accepted knowledge requires GitHub canonical publication and exact committed-byte readback under the existing file-work/preservation rules. The shard may retain a `PROMOTION_RECEIPT` linking exact commit/tree/blob and content digest; it cannot manufacture Git acceptance.

Promotion handoff:
1. Freeze a consistent exact snapshot of selected record bytes and pointer/fence/operation receipts into an isolated read-only staging root; re-verify chain and bytes before packaging.
2. Submit the existing r0.2 File/Artifact Service **request schema r0.1**: `schema,request_id,package_id,inputs[]` with each `source_id,source_path,target_path,sha256,size`; `prior_manifest_path=null` or safe relative verified path; `create_archive` exact Boolean; `git_adapter_enabled=false`. Each input is a staged exact byte object, never arbitrary original shard path. Reject reserved `MANIFEST.json` and normalized aliases.
3. Service returns local `package/MANIFEST.json`, `readback.json`, `diff.json`, `result.json` and optional deterministic archive. Check source/input and output SHA/size and manifest consistency. Service has `authority_semantics=none`, `project_state_semantics=none`; GitAdapter is disabled. This is package sealing/readback, not publication.
4. A separately authorized publisher commits bounded significant artifacts to GitHub and reads exact committed blobs back; record commit/tree/blob identities and compare with staged package. No readback → `PUBLICATION_UNVERIFIED`. Publication ≠ dispatch ≠ receipt ≠ substantive acceptance/current-writer transfer.
5. The independently verified Git anchor and current canonical governance are prerequisites for a replacement boundary. Shard loss before promotion may lose provisional work; shard loss after promotion can recover only up to the exact Git anchor and must disclose any later unknown work. Never assert RPO/RTO or `CHECKPOINT_DURABLE` from this sequence alone.

If shard and Git claim different versions, block replacement/current pointer advancement until supersession is externally resolved. If Git unavailable, only separately admitted provisional operations may continue; no canonical result/promotion/replacement claim. If pointer is missing but object exists, preserve orphan and reconcile; if pointer exists but object missing/corrupt, STOP and recover only from independently verified canonical anchor under separate authority. Object-only or ambiguous CAS never grants continuation. Exact failure result includes operation IDs, namespace, expected/actual digests, generation and nonsecret provenance, without raw sensitive payload.

## 6. Policy fields left open

Each record and namespace references `retention_policy_id/version`, `expiry_class`, `hold_refs`, `garbage_collection_eligibility`, `canonical_anchor_ref` and `deletion_receipt` where relevant. GC cannot remove a referenced pointer head, unresolved CAS evidence, a held record or an unpromoted recovery dependency. Expiry is not authority revocation; writer fence still checked independently. Missing policy, uncertain hold or unknown reachability blocks deletion. Numerical retention, RPO, RTO, freshness windows, quota and storage failure model are UNKNOWN; separate responsible decision and tests are required. No default host/backend/owner is selected.

## 7. Independent review matrix (design expectations)

| Case | Expected decision and evidence |
|---|---|
| Valid exact writer, task, sources, object and expected pointer | PUT receipt; independent VERIFY; CAS N→N+1 receipt with bound operation IDs; no Git/current acceptance implied. |
| Same PUT op ID, identical bytes | Same immutable object/receipt; no second object. |
| Same PUT op ID, conflicting bytes | IDEMPOTENCY_CONFLICT before mutation. |
| Same CAS op ID, identical full request | Exact prior outcome/reconciliation, no second generation. |
| Same CAS op ID, changed pointer/fence/task | IDEMPOTENCY_CONFLICT, no mutation. |
| Two valid concurrent writers at generation N | At most one CAS succeeds; other CAS_CONFLICT, fork evidence retained. |
| Frozen or superseded writer, lower epoch | STALE_WRITER_FENCE before PUT/CAS; canonical freeze provenance logged. |
| New writer with only technical access but no Writer Gate | TASK_AUTHORITY_MISSING / BLOCKED_TRUST_ROOT. |
| Forged trust profile or mirror, request-supplied key | BLOCKED_TRUST_ROOT; cannot self-certify. |
| Revoked/stale attestation, unavailable canonical currentness | BLOCKED_TRUST_ROOT, no fail-open cache. |
| Task version superseded or wrong entity namespace | TASK_VERSION_CONFLICT / NAMESPACE_MISMATCH. |
| Duplicate record ID with different bytes | DIGEST_OR_IDENTITY_CONFLICT. |
| Missing pointer, orphan object | No current state claim; reconcile operation ledger/anchor. |
| Pointer references missing/corrupt object | BLOCKED_INTEGRITY; no continuation. |
| Lost PUT response / lost CAS response | RESOLVE_OPERATION bound to exact request; UNKNOWN is not APPLIED. |
| Shard unavailable or partial write | BLOCKED_UNAVAILABLE/UNKNOWN; no durability claim. |
| Object byte/hash, parent chain or generation mismatch | BLOCKED_INTEGRITY/CONFLICT. |
| Git/shard anchor divergence or stale Git result | BLOCKED_CANONICAL_MISMATCH; no recency choice. |
| No canonical anchor at replacement boundary | BLOCKED_REPLACEMENT_ANCHOR; provisional state cannot authorize NEW. |
| Missing retention policy, unresolved hold | BLOCKED_GC; no guessed duration. |
| Unknown locator, symlink escape, full corpus or oracle path | DENY; no bytes emitted. |
| Gateway r0.3 WRITE/CAS request | DENY_UNSUPPORTED; remains READ/VERIFY only. |
| File Service package locally PASS but Git publication/readback absent | PACKAGE_ONLY/PUBLICATION_UNVERIFIED; no accepted state. |
| EOM-SHARD-PILOT-R01 or memory-layering attempt 3 request | BLOCKED_AUTHORITY; no execution. |

Review should require deterministic vectors for serialization, object identity, operation-specific dedupe, CAS concurrency/linearization, fence rollover/revocation, crash injection between object/ledger/pointer writes, package/readback integrity and exact Git anchor reconciliation. Mere contract text does not prove runtime atomicity or failure recovery.

## 8. Minimal separately authorized implementation sequence

1. **First implementation gate:** versioned offline schema/serialization and operation/CAS/fence state-machine candidate with deterministic synthetic vectors and crash/idempotency tests; no host deployment or shard WRITE. KOD implementation task requires a new exact authority. SIS reviews isolation/atomicity feasibility, SHD reviews storage/integrity semantics, SHT reviews writer/authority/supersession boundaries.
2. After explicit OPERATOR decisions on trust root/profile issuer, epoch attestor, owner/backend, retention and freshness policy, build an isolated store prototype and separate read-only verifier. Independent SIS/SHD verification must show real atomic CAS/fence enforcement, persistent operation ledger, fail-closed loss and no privileged cross-capability path. This also requires new authority.
3. Only after independent PASS and separately scoped operational authority consider bounded host admission/write and File Service/Git integration. No automatic deployment or promotion from design.
4. EOM pilot execution is still BLOCKED by SHT's causal overlap with unauthorized memory-layering attempt 3. Resolve that lineage by separate OPERATOR decision before any OLD→NEW test; this document neither redesigns nor runs it.

Success criterion of this **document** is exact interface/failure/review contract ready for SIS+SHD independent review. It is not proof of operational store, durable checkpoint, general Entity continuity or traffic reduction.

## EXPERIENCE

Идея → отделить быстрые immutable shard objects от канонических решений и права writer.
Проба → задать отдельные PUT, CAS, fence, operation-bound resolution и Git promotion gates на проверенных компонентах.
Результат → контракт описывает проверяемые отказы и неизвестные trust/policy решения без включения WRITE.
Вердикт → design candidate ready for independent review; EOM execution remains blocked.
Урок → точный хеш записи и CAS не создают доверенного writer, durable checkpoint или права на продолжение без внешнего authority и canonical readback.
