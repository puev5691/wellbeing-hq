# КОДЕР → КООРДИНАТОР: S1+O2 checkpoint interface / negative matrix r0.1

status: `CANDIDATE_NONLIVE_DOCUMENT_ONLY`
task: `KOD_CHECKPOINT_SYNTH_R01`
CHECKPOINT_DURABLE: `NOT_ESTABLISHED`
memory_layering_attempt_3: `NOT_AUTHORIZED`
project_time: omitted; trusted project-time source not used

## Человеческий вывод

Предложен точный формат одной точки остановки искусственной задачи и правила будущей записи/проверки. Отдельные immutable bytes, текущий pointer, storage commit/ack, независимое readback и право продолжать задачу получают разные доказательства. Существующий mazhor gateway подтверждён только как VERIFY-only: этот документ не создаёт checkpoint-хранилище. Положительный сценарий и 18 отказов ниже — **ожидания проектируемого интерфейса**, ни один тест не запускался.

## Полномочие и прочитанное evidence

Fresh HQ preflight: `puev5691/wellbeing-hq@88c44d0ca5492a7e6b9fbb92aee01e571da22fb2`; tree truncated=false. Current KOD writer v0.5: `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`. v0.4 remains frozen: `entities/koder/current/KOD__current-writer-handoff-freeze-v04.md`, blob `94cc1acb14fdcca623f4596c9a589e9ff42451ee`. No newer KOD writer or competing S1+O2 KOD terminal result found in complete fresh tree.

Direct current OPERATOR authority: `AUTHORIZE_KOD_S1O2_INTERFACE_NEGATIVE_MATRIX_R01_DOCUMENT_ONLY`. KOO exact instruction: `puev5691/wellbeing-hq@88c44d0ca5492a7e6b9fbb92aee01e571da22fb2:entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-interface-negative-matrix-r01__KOD.md`, blob `49bf7b16faf7880a25faef9d67222ba6ef64bf00`. SIS fit-gap: `puev5691/wellbeing-hq@e58e40ca1cf478b95a91f611dd64055d3fb6c50e:entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-storage-profile-fitgap-r01__KOO.md`, blob `cffcd2c9a7531dd0589877d3c31527e94682f33b`; documentary PASS only.

S1+O2 exact proposed scope blob `30a8444646a84cf8eff7a7941c3b1ca5fa0a70e3`; KAN governance candidate blob `33f2e8f832044bbd2c77d810ddaa725ed87de100` is `CANDIDATE_NOT_ACTIVE`; ARH document review blob `740e313ca661063c69d87f9cc00a7db31bfc2234` is PASS with boundaries, not runtime proof. Applied approved sources: recovery v1.6, roles v2.4, source-loading v2.2, file-work v2.4, task-conveyor v1.2, core v2.5. No historic PROMPT replay. Selection S1+O2 grants design only, appoints no storage owner and selects no backend/host.

## Proposed fixture and exact checkpoint format

**VERIFIED_FROM_INPUT_DOCUMENTS, not executed:** exact input UTF-8 bytes `alpha\nbeta\ngamma\n`, specified SHA-256 `4fdbc441ea7b546100e086ac1e4fc5ae6749b7314311c99db05be450eca12996`. Input has three newline-terminated lines; a proposed interruption after processing the first two gives `next_index=2,count=2`. Proposed bounded continuation reads only the third line and ends at `next_index=3,count=3`. Neither task nor fixture is run by this document.

**PROPOSED schema `wb.kod.checkpoint.s1o2.v1`:** one immutable content-addressed object whose logical fields are exactly the following. All fields are required, no additional fields; `null` is forbidden unless explicitly shown. Each `*_ref` is a structured immutable locator `{repository_or_store, version_identity, path_or_key, content_digest}` where the version and digest must be checked independently. No human-readable alias, mutable branch, bare timestamp or free-text guess satisfies a required ref.

| Key in immutable object | Exact proposed type / constraint | What it proves |
|---|---|---|
| `schema` | string exactly `wb.kod.checkpoint.s1o2.v1` | Decoder version only |
| `entity_id` | string exactly `KOD` | Namespace identity, not writer grant |
| `task_id` | string exactly `KOD_CHECKPOINT_SYNTH_R01` | Proposed synthetic task identity |
| `task_revision_ref` | immutable ref, **UNKNOWN until separately authorized task revision exists** | Prevents stale task interpretation |
| `input` | object `{encoding:"utf-8",sha256:"4fdbc441ea7b546100e086ac1e4fc5ae6749b7314311c99db05be450eca12996",bytes_ref:<immutable-ref>}` | Binds fixture identity; fixture bytes not embedded in checkpoint |
| `dependency_refs` | array of unique immutable refs sorted by exact canonical serialized bytes; may be empty **only if** separately established that no other dependencies are mandatory | Manifest of material needed to interpret state |
| `authority_ref` | immutable authorized task/scope decision ref, UNKNOWN for future actual execution | Does not create authority |
| `writer_ref` | immutable current-writer establishment ref revalidated at use, UNKNOWN for future physical instance | Writer provenance only |
| `writer_epoch_ref` | exact issued epoch/fence lineage ref, UNKNOWN issuer/value | Detects stale writers; token does not appoint writer |
| `generation` | nonnegative decimal JSON integer, issued by approved atomic namespace rule; initial and successor value UNKNOWN | Monotonic pointer lineage, not time |
| `parent_digest` | 64 lowercase hex SHA-256 of previous accepted immutable object; genesis represented by exact string `GENESIS` only if separately defined; no implicit genesis | Causal parent |
| `next_index` | JSON integer 0..3; sample stop=2 | Next unread line; prevents replay of prefix |
| `count` | JSON integer 0..3; sample stop=2; for this fixture must equal `next_index` | Completed line count |
| `effect_ledger` | exact object `{mode:"none",records:[]}` for first synthetic scope; any external effect invalidates this fixture class | Asserts no authorized external effects; unknown real effect must be separately reconciled |
| `request_id` | non-empty unique dedupe identifier within namespace+task revision; actual ID UNKNOWN | Correlates uncertain put/ack without blind retry |

**PROPOSED validation:** for this fixture `0 ≤ count = next_index ≤ 3`, and interruption checkpoint candidate must have `next_index=count=2`. Verifier independently checks fixture identity and all refs, including raw fixture bytes when available; the checkpoint alone does not authorize DONE, resume or writer transfer. `task_revision_ref`, `authority_ref`, `writer_ref`, `writer_epoch_ref`, `dependency_refs` content, generation issuer and request ID are **UNKNOWN mandatory inputs**; no fabricated instance values are supplied.

**PROPOSED deterministic hash boundary:** serialize exactly this immutable object (and nothing else) as JSON UTF-8, with object keys sorted by Unicode code point ascending recursively, arrays preserving contract order, no insignificant whitespace, no BOM, no duplicate keys, no NaN/infinity/fractions, JSON integers in plain shortest decimal. All variable string values use ASCII only (code points U+0021..U+007E excluding double quote and backslash); locators with any other character must use canonical percent-encoded UTF-8 before serialization. Slash is not escaped; fixed schema keys and string values are ASCII. Invalid UTF-8, noncanonical percent encodings and values outside this alphabet are rejected. Hash the complete resulting byte sequence with SHA-256: `digest=sha256(canonical_object_bytes)`. `checkpoint_id="sha256:"+lowercase_hex(digest)`. The digest covers task revision, input digest and bytes ref, every dependency ref, authority/writer/epoch refs, generation, parent, cursor, effect ledger and request ID. It **does not** cover storage ack, durable ref, current pointer or readback report: those are separately attested observations after object creation. A future implementation must freeze one precise canonicalizer/Unicode rule and independently compare exact byte fixtures before a live claim; **this design does not calculate a checkpoint digest**.

## Proposed client/storage boundary (not an existing gateway API)

Names below are prospective typed operations. Service, trust domains, principals, retention and backend are UNKNOWN. Current VERIFY-only gateway does not implement any proposed put/commit/CAS.

1. `PutImmutable(namespace, object_bytes, checkpoint_id, request_id, caller_auth)` checks exact caller/task/writer scope, content digest and uniqueness. It may create an immutable object; it **must not** move the current pointer on its own. Response `RECORDED_PENDING | REJECTED | UNKNOWN_OUTCOME` cannot establish durability.
2. `CommitCurrentCAS(namespace, expected={task_revision_ref,writer_epoch_ref,generation,parent_digest}, successor={checkpoint_id,generation,writer_epoch_ref}, request_id)` atomically compares the **complete** expected tuple and one approved fence lineage, advances only on a single winner, persists dedupe result, returns `COMMITTED | CAS_CONFLICT | FENCED | UNKNOWN_OUTCOME`. Generation increases exactly once under the approved issuer rule; timestamps/lease expiry never substitute for writer authority. An orphan object whose pointer was not committed remains non-current evidence. Whether put+CAS share a transaction is **UNKNOWN**, so success of one cannot imply the other.
3. `CommitEvidence/StorageAck` associates checkpoint id + exact committed pointer tuple + transaction token + issuing principal + durable ref + approved durability/failure-domain and retention profile refs + observed placement proof with outcome `COMMITTED | NOT_COMMITTED | UNKNOWN`. An HTTP 200, queue admission, buffer write, signature alone or same-disk copy is insufficient. Actual issuer, persistent commit semantics and failure domains **UNKNOWN**.
4. `ReadByDurableRef(durable_ref, authorized_independent_reader)` after ack reads **stored** exact bytes/metadata via a path demonstrably separate from submitted buffer/cache, recomputes digest and verifies tuple. Emits `ReadbackReport{reader,requested_ref,observed_ref,observed_digest,observed_bytes_digest,profile_ref,result,evidence_ref}`. Independence boundary/reader identity **UNKNOWN**. No boolean `independently_readable=true` is accepted as proof by itself.
5. `ReadCurrent(namespace)` returns pointer tuple and provenance; caller cross-checks source/writer/task authority fresh. `ResolveRequest(request_id)` reconciles a lost ack to exactly `COMMITTED | NOT_COMMITTED | UNKNOWN` using durable state, not by blindly issuing a second write. Dedupe persistence/retention UNKNOWN; same key+same bytes may yield the recorded result without a second effect, same key+different bytes is always conflict.

**PROPOSED fence rule:** an old writer whose epoch is no longer accepted receives `FENCED` even if it is alive, owns credentials or its former lease appears valid. A new epoch requires an independently authorized writer transition; the store cannot create that authority. Different heads with the same generation or divergent epochs remain `BLOCKED_CONFLICT`; no last-write-wins. Any incomplete evidence yields `UNKNOWN/STOP`.

## Expected matrix: one positive and SIS N01–N18

All expected outcomes are **PROPOSED**, not observed PASS. In every row `CHECKPOINT_DURABLE=NOT_ESTABLISHED` for the actual project; the status refers to the proposed future protocol, not an existing service.

| ID | Scenario from SIS | Proposed outcome / forbidden claim | Missing proof or decision |
|---|---|---|---|
| P01 | Valid synthetic input/revision/authority/fence; first two lines checkpointed, object put, pointer CAS wins, durable ack and independent exact-byte readback under approved profile | Then and only then candidate `CHECKPOINT_DURABLE` for that exact tuple; continuation still `WAIT_RESUME_AUTHORITY` | D1–D9 independently verified on actual deployed version; BOUNDED_TASK_RESUME_AUTHORITY separate |
| N01 | Wrong fixture digest or task revision | `REJECT_INPUT` before commit; no current pointer change | Immutable fixture and task revision readback |
| N02 | Wrong expected parent digest | `CAS_CONFLICT`; pointer unchanged; stored object, if any, orphan | Atomic compare evidence |
| N03 | Stale writer epoch/fence | `FENCED`; old availability irrelevant; no pointer advance | Issuer and authoritative writer lineage |
| N04 | Two writers same expected parent | Exactly one CAS winner; loser `CAS_CONFLICT/FENCED`; no duplicate current successor | Concurrency evidence on exact store |
| N05 | Same generation, different digest or parent | `BLOCKED_CONFLICT`; preserve both branches, no pick newest | Conflict provenance/arbiter UNKNOWN |
| N06 | Same request ID, identical bytes | Return persisted duplicate outcome; no second effect | Durable dedupe namespace/retention UNKNOWN |
| N07 | Same request ID, different bytes | `HARD_DEDUPE_CONFLICT`; no pointer change | Exact-byte/digest compare |
| N08 | Commit succeeds, ack lost | `UNKNOWN_OUTCOME` until independent ResolveRequest/readback; no blind retry | Transaction/durable request index UNKNOWN |
| N09 | Ack COMMITTED, durable-ref readback absent or mismatched | `BLOCKED_INTEGRITY`; no CHECKPOINT_DURABLE | Independent exact-byte reader and profile |
| N10 | Partial/orphan object, CAS not committed | Keep orphan evidence only; current pointer unchanged; no resume from orphan | Atomic pointer/read-current evidence |
| N11 | Corrupted payload, manifest or dependency | `BLOCKED_INTEGRITY`; no resume | Hash of bytes + dependency graph |
| N12 | Dependency expires before recoverable interval | `BLOCKED_RECOVERY_ELIGIBILITY` even if object bytes intact | Approved retention for required dependencies UNKNOWN |
| N13 | Shard unavailable | `UNAVAILABLE/STOP`; no reconstructed checkpoint | Storage availability/failure profile UNKNOWN |
| N14 | Partition gives divergent heads | `BLOCKED_CONFLICT`; freeze namespace, preserve both branches | Conflict resolution authority UNKNOWN |
| N15 | Backup yields old epoch/generation | Restore only in isolation; never auto-promote current | Approved backup/restore contract and fence reconciliation UNKNOWN |
| N16 | Restored bytes valid but fence/dedupe lineage absent | `BLOCKED_RESTORE/RECOVERY`; no resume | Independent lineage availability/retention UNKNOWN |
| N17 | Retention expires during promotion delay | `WAIT_RETENTION_DECISION/STOP`; do not silently lose only required copy | Exact hold/extension/alternate-preservation authority UNKNOWN |
| N18 | External side effect outcome unknown | `BLOCKED_EFFECT_RECONCILIATION`; never replay from cursor blindly | External evidence and separate effect decision required |

N18 is outside this no-effect synthetic fixture as an adversarial contract case, not a claim that the fixture performs external effects. N01–N18 mirror the SIS documentary list; their tests have **not** been implemented, run or passed.

## Separate gates and required future evidence

| Claim | Status now | Exact distinct future gate |
|---|---|---|
| Exact serialized checkpoint object | PROPOSED | Freeze schema/canonical bytes, independent review and offline fixtures after separate permission; no object exists now |
| `CHECKPOINT_DURABLE` | BLOCKED / NOT_ESTABLISHED | D1 approved storage/failure/retention owner+contract; D2 caller/task/writer authority; D3 immutable context/dependencies; D4 persistent commit; D5 independent readback; D6 atomic CAS/generation/dedupe/fencing; D7 retention/backup/restore; D8 separately authorized negative runtime checks on deployed version; D9 object-specific current provenance |
| `BOUNDED_TASK_RESUME_AUTHORITY` | BLOCKED / NOT_GRANTED | Separate approved bounded task and resume scope, fresh task/current-writer/authority/supersession check and explicit decision for this checkpoint. Durable bytes alone insufficient |
| `RECOVERY_ELIGIBLE` | BLOCKED | Immutable manifest with required dependencies, approved source versions, freshness, retention/privacy and recovery-contract readback; independent ARH assessment as required. Does not imply completed initiation |
| ARH preservation | NOT_CLAIMED | ARH independently accepts exact package, external publication and post-publication readback with version/checksums; candidate source policy alone insufficient |
| New instance initiation | NOT_PERFORMED | Exact recovery locator/composition/identity verified by that instance under recovery canon; no inherited chat memory |
| Writer Gate | NOT_PERFORMED | Separate permitted writer establishment/freeze/failover authority and proof; storage key/epoch/availability not enough |
| `processing_started` | NOT_PERFORMED | New admitted instance proves first task-specific step after final revalidation; neither checkpoint ack nor publication/inbox/activation suffices |

## One smallest subsequent gate

KOO may separately address **one independent documentary interface and N01–N18 matrix review** to SIS, with ARH preservation input checked by KOO where relevant. Review exact definitions against SIS D1–D9 and the frozen S1 scope; report contradictions/UNKNOWN without selecting service owner, backend, host or retention. Only after that review and a distinct OPERATOR decision may anyone ask for implementation/tests; this document authorizes neither. No further task is automatically activated by this result.

Boundary accounting: code=0; tests (including synthetic task)=0; host/shard/network/credentials/provider calls=0; automation/Project Sources/canon changes=0; operational owner assignment=0; numeric retention/RPO/RTO=UNSET; historical PROMPT replay=0. Publication/dispatch/inbox ≠ receipt/activation/processing_started.
