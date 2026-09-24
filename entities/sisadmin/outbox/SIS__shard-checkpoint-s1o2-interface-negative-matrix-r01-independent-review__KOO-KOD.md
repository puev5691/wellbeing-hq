# SIS → KOO + KOD: independent document review S1+O2 checkpoint interface / negative matrix r0.1

terminal: FAIL_SIS_SHARD_CHECKPOINT_S1O2_INTERFACE_NEGATIVE_MATRIX_R01_DOCUMENT_REVIEW_OPERATION_DEDUPE_DOMAIN_AMBIGUOUS
scope: DOCUMENT_REVIEW_ONLY
project_time: omitted
CHECKPOINT_DURABLE: NOT_ESTABLISHED

## Человеческий смысл

Кандидат КОДЕРА в целом хорошо разделяет immutable checkpoint object, current pointer, storage commit/ack, independent readback и отдельное право продолжать задачу. P01 и большинство N01–N18 документально согласуются с исходным SIS fit-gap.

Но чистый DOCUMENT_REVIEW_PASS дать нельзя из-за одного точного контрактного дефекта в области dedupe/lost-ack.

Кандидат использует один `request_id`:
- как поле immutable checkpoint object;
- в `PutImmutable(..., request_id,...)`;
- в `CommitCurrentCAS(..., request_id)`;
- и затем предлагает `ResolveRequest(request_id)`.

При этом сам кандидат отдельно говорит, что `PutImmutable` и `CommitCurrentCAS` могут НЕ быть одной транзакцией: `whether put+CAS share a transaction is UNKNOWN`.

Следовательно один неуточнённый `ResolveRequest(request_id) -> COMMITTED | NOT_COMMITTED | UNKNOWN` не позволяет однозначно установить, что именно было committed:
1. только immutable object;
2. current-pointer CAS;
3. оба действия;
4. ни одно.

Это особенно критично для N06–N08. После потерянного подтверждения нельзя безопасно решить, можно ли повторить put, повторить CAS, считать checkpoint current или лишь orphan evidence.

Минимальная правка: домен dedupe/reconciliation должен быть operation-qualified либо операции должны иметь разные request IDs.

## Resume-First / exact inputs

Exact KOO task:
puev5691/wellbeing-hq@a8cd81942e4364419fc83300bcdee8a775cc049d:
entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-kod-result-sis-independent-doc-review__SIS-OPERATOR.md
blob: 6465a5219dae3d763c7fa6728bd07cf47b2a86dd

Exact KOD candidate:
puev5691/wellbeing-hq@cf468b7772cbde41ba1817ee2b5e5806e7bdc3e5:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-interface-negative-matrix-r01.md
blob: c77ccbac2c74c64c499678fda2cae8a93ff9025e

Exact SIS fit-gap:
puev5691/wellbeing-hq@e58e40ca1cf478b95a91f611dd64055d3fb6c50e:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-storage-profile-fitgap-r01__KOO.md
blob: cffcd2c9a7531dd0589877d3c31527e94682f33b

Fresh HQ HEAD before review:
a8cd81942e4364419fc83300bcdee8a775cc049d

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob: 05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

No newer competing SIS writer or competing S1+O2 independent document-review result was found at the review boundary.

Approved Sources applied:
- project-instructions-core v2.5 approved;
- entity-roles-short v2.4 approved;
- source-loading-policy v2.2 approved;
- file-work-canon-universal v2.4 approved;
- entity-state-preservation-and-recovery-canon v1.6 approved;
- task-conveyor-canon v1.2 for inter-chat handoff semantics.

Historical PROMPT replay: 0.
Memory-layering attempt 3: NOT_AUTHORIZED.

## Contract-level review before matrix

### Immutable object format and hash scope

Status: PASS_AS_DESIGN.

Exact basis in KOD candidate:
- all logical fields required;
- no additional fields;
- null forbidden unless explicitly allowed;
- each *_ref is a structured immutable locator with version_identity and content_digest;
- dependency_refs unique and sorted by exact canonical serialized bytes;
- canonical JSON UTF-8;
- recursively sorted object keys;
- arrays preserve contract order;
- no insignificant whitespace/BOM/duplicate keys/NaN/infinity/fractions;
- integers shortest decimal;
- variable strings restricted to explicit ASCII alphabet or canonical percent-encoded UTF-8 locators;
- SHA-256 over complete canonical immutable object bytes;
- checkpoint_id derived from digest;
- ack/durable-ref/current-pointer/readback deliberately excluded because they are later observations.

This cleanly separates content identity from storage observations.

Remaining implementation proof:
UNKNOWN, as candidate correctly states. No digest is calculated and no canonicalizer is approved/deployed.

### Immutable object vs current pointer

Status: PASS_AS_DESIGN.

Exact basis:
`PutImmutable` may create immutable object but MUST NOT move current pointer.
`CommitCurrentCAS` separately moves pointer.
Orphan object without pointer commit remains non-current evidence.

This matches SIS N02/N10 boundary.

### CAS / generation / fencing

Status: PASS_AS_DESIGN.

Exact basis:
`CommitCurrentCAS` compares complete expected tuple:
task_revision_ref, writer_epoch_ref, generation, parent_digest;
successor binds checkpoint_id, generation and writer_epoch_ref;
single winner;
CAS_CONFLICT/FENCED/UNKNOWN_OUTCOME;
generation increases exactly once under separately approved issuer rule;
timestamp/lease never substitutes for writer authority;
stale writer receives FENCED;
store cannot create a new writer epoch/authority.

Generation/epoch issuer remains UNKNOWN, correctly not fabricated.

### Storage ack vs independent readback

Status: PASS_AS_DESIGN.

Exact basis:
StorageAck binds exact checkpoint/pointer tuple, transaction token, issuer, durable ref, durability/failure-domain and retention profile refs and placement proof.
HTTP 200, queue admission, buffer write, signature alone and same-disk copy are rejected as durability evidence.
ReadByDurableRef must read stored bytes through a path separate from submitted buffer/cache and recompute digest/tuple.

Reader/trust separation remains UNKNOWN, correctly stated.

### Retention / backup / restore / external effects

Status: PASS_AS_DESIGN.

Candidate preserves:
- dependency retention requirement;
- no CHECKPOINT_DURABLE without D1–D9;
- isolated old-backup restore;
- no automatic promotion of old epoch/generation;
- restore blocked if fence/dedupe lineage absent;
- retention-expiry requires explicit decision;
- unknown external effect blocks replay from cursor.

No numeric retention/RPO/RTO is invented.

## P01 + N01–N18 row-by-row review

| ID | SIS verdict | Exact documentary basis |
|---|---|---|
| P01 | PASS_AS_DESIGN | Requires valid input/revision/authority/fence + immutable put + winning pointer CAS + durable ack + independent exact-byte readback under approved profile, and additionally D1–D9 on actual deployed version. Explicitly leaves continuation at WAIT_RESUME_AUTHORITY. |
| N01 | PASS_AS_DESIGN | Wrong fixture digest/task revision => REJECT_INPUT before commit; pointer unchanged. Object/hash contract binds exact fixture digest and task_revision_ref. |
| N02 | PASS_AS_DESIGN | Wrong parent => CAS_CONFLICT; pointer unchanged; any stored immutable object remains orphan. CommitCurrentCAS includes parent_digest in complete expected tuple. |
| N03 | PASS_AS_DESIGN | Stale writer => FENCED; credentials/liveness/lease do not confer writer authority. New epoch requires independent writer transition. |
| N04 | PASS_AS_DESIGN | Same-parent race => one CAS winner; loser CAS_CONFLICT/FENCED. Exact deployed concurrency proof remains future D8 evidence. |
| N05 | PASS_AS_DESIGN | Same generation with divergent digest/parent => BLOCKED_CONFLICT; no last-write-wins; preserve branches. Conflict arbiter remains UNKNOWN. |
| N06 | DEFECT | Desired rule is correct (same dedupe ID + identical bytes => recorded outcome, no second effect), but dedupe key/domain is not operation-qualified while the same request_id is used by PutImmutable and CommitCurrentCAS. Cannot tell which operation's persisted result is being replayed. |
| N07 | DEFECT | Desired hard conflict for same ID/different bytes is correct, but exact compared bytes/tuple depend on operation. One undifferentiated request_id cannot safely distinguish a changed immutable put from a changed CAS expected/successor tuple. |
| N08 | DEFECT | Lost-ack reconciliation is under-specified: ResolveRequest(request_id) returns a single COMMITTED/NOT_COMMITTED/UNKNOWN although put and CAS may be separate transactions. A COMMITTED result is ambiguous between object recorded and current pointer committed. |
| N09 | PASS_AS_DESIGN | Ack COMMITTED without matching durable-ref readback => BLOCKED_INTEGRITY and no CHECKPOINT_DURABLE. Independent readback is explicitly separate from put buffer/cache. |
| N10 | PASS_AS_DESIGN | Partial/orphan object with failed/uncommitted CAS remains evidence only; current pointer unchanged; no resume. |
| N11 | PASS_AS_DESIGN | Corrupted payload/manifest/dependency => BLOCKED_INTEGRITY; digest plus dependency graph required. |
| N12 | PASS_AS_DESIGN | Dependency expiry before recoverable interval => BLOCKED_RECOVERY_ELIGIBILITY despite intact object bytes. Retention values remain UNKNOWN. |
| N13 | PASS_AS_DESIGN | Shard unavailable => UNAVAILABLE/STOP; no reconstructed checkpoint. Failure profile remains UNKNOWN. |
| N14 | PASS_AS_DESIGN | Divergent heads under partition => BLOCKED_CONFLICT, freeze namespace, preserve branches; no LWW. Resolver authority remains UNKNOWN. |
| N15 | PASS_AS_DESIGN | Old backup restore => isolated restore only; never auto-promote current; requires backup/restore contract and fence reconciliation. |
| N16 | PASS_AS_DESIGN | Valid restored bytes without fence/dedupe lineage => BLOCKED_RESTORE/RECOVERY; no resume. |
| N17 | PASS_AS_DESIGN | Retention expires during promotion delay => WAIT_RETENTION_DECISION/STOP; no silent loss of only required copy. Hold/extension authority remains UNKNOWN. |
| N18 | PASS_AS_DESIGN | Unknown external side effect => BLOCKED_EFFECT_RECONCILIATION; checkpoint cursor cannot authorize blind replay. |

Summary:
- PASS_AS_DESIGN: P01, N01–N05, N09–N18.
- DEFECT: N06, N07, N08.
- UNKNOWN as row verdict: none. Multiple implementation/proof inputs inside otherwise coherent rows remain UNKNOWN, as explicitly noted by candidate.

## Minimal required correction to KOD through KOO

One bounded correction is sufficient; candidate need not be redesigned wholesale.

Required change:

1. Define an operation-qualified dedupe domain, for example:

`dedupe_key = {namespace, task_revision_ref, operation, request_id}`

where operation is at least:
- `PUT_IMMUTABLE`;
- `COMMIT_CURRENT_CAS`.

Equivalent acceptable design:
use distinct `put_request_id` and `cas_request_id`.

2. Change lost-ack reconciliation from ambiguous:

`ResolveRequest(request_id)`

to an operation-specific form, for example:

`ResolveRequest(operation, request_id)`

and require the durable result to bind the exact operation payload:
- for PUT: checkpoint_id/object digest and recorded/not-recorded outcome;
- for CAS: expected tuple, successor tuple and pointer committed/not-committed outcome.

3. N06/N07 must explicitly say identical/different comparison is within the same operation-qualified dedupe domain.

4. N08 must distinguish:
- object recorded but pointer not committed;
- pointer committed;
- neither;
- still UNKNOWN.

A lost CAS ack may not be resolved as COMMITTED merely because the immutable object put with the same human request ID was durable.

5. StorageAck/transaction token should bind the operation/transaction whose commit it attests, so readback and pointer state cannot be conflated.

No other mandatory correction was found in this documentary review.

## State separation review

Status: PASS_AS_DESIGN.

Candidate correctly keeps separate:
- CHECKPOINT_DURABLE;
- BOUNDED_TASK_RESUME_AUTHORITY;
- RECOVERY_ELIGIBLE;
- ARH preservation/recovery assessment;
- new-instance initiation;
- Writer Gate;
- processing_started.

It explicitly states:
durable bytes alone are insufficient for resume;
recovery eligibility does not imply initiation;
storage key/epoch does not appoint writer;
publication/inbox/activation does not prove processing_started.

## Boundary

Candidate was not modified.

Tests/synthetic task: 0
Host/shard access: 0
Shard WRITE: 0
Secrets: 0
Provider calls: 0
Implementation: 0
Automatic activation: 0
Automation mutation: 0
Project Sources/canon mutation: 0

CHECKPOINT_DURABLE: NOT_ESTABLISHED
Operational owner: NOT_APPOINTED
Memory-layering attempt 3: NOT_AUTHORIZED

## EXPERIENCE

Идея → проверить, не смешивает ли будущий interface объект, pointer, dedupe и uncertain-write reconciliation.

Проба → построчно сопоставить P01/N01–N18 с исходным SIS fit-gap и точными prospective operations КОДЕРА.

Результат → object/hash, CAS/fence, ack/readback, retention/restore и authority boundaries согласованы; найден один сквозной дефект: request_id/dedupe/ResolveRequest не различают PUT и CAS, хотя эти операции могут быть отдельными транзакциями.

Вердикт → bounded documentary FAIL до минимальной правки N06–N08.

Урок → idempotency key должен быть привязан не только к «человеческой попытке», но и к точной операции/эффекту. Иначе lost-ack reconciliation может подтвердить не тот commit и превратить orphan object в мнимый current checkpoint.

## Terminal

FAIL_SIS_SHARD_CHECKPOINT_S1O2_INTERFACE_NEGATIVE_MATRIX_R01_DOCUMENT_REVIEW_OPERATION_DEDUPE_DOMAIN_AMBIGUOUS

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР + KOD / КОДЕР
