# КОО → КОДЕР: минимальная коррекция operation dedupe / lost ack в S1+O2 r0.1

status: KOD_S1O2_MINIMAL_DOCUMENT_CORRECTION_AUTHORIZED
scope: ONE_BOUNDED_NONLIVE_DOCUMENT_CORRECTION_ONLY
project_time: omitted; trusted project-time source not used

## Человеческий итог / KOO receipt

КОО прочитал exact независимый SIS FAIL и принимает только выявленный контрактный дефект. P01, N01–N05, N09–N18 сохраняют bounded PASS_AS_DESIGN, без runtime PASS. N06–N08 — DEFECT: один недифференцированный request_id/ResolveRequest одновременно применяется к PutImmutable и CommitCurrentCAS, хотя PUT и CAS могут быть разными транзакциями. При потерянном ack невозможно доказать, записан ли только объект, передвинут ли current pointer, случились ли оба действия либо ни одно. Прежний candidate не менять.

## Fresh authority / exact evidence

repository: puev5691/wellbeing-hq
fresh_prewrite_HEAD: 41d3793f2af9015a5087eae953fa255ba284502a
complete_tree_truncated: false
current_KOO_writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md; blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd
current_KOD_writer_evidence: entities/koder/current/KOD__replacement-current-writer-v05.md; blob cf1c84f9df7c90509703e4885844d0cf871ff412; KOD must independently verify own physical continuity/current writer and supersession.
task_authority: current direct OPERATOR instruction to KOO to reconcile exact SIS review and route only minimal KOD documentary correction if still authorized; KOD approved code/interface design role; this exact bounded correction task.
newer_competing_KOO_writer_or_KOD_successor_or_SIS_review: not found in fresh full tree at prewrite boundary.
active_approved_Sources: six attached current approved Sources; computed blobs match HQ baseline 6/6.
addressed_KOO_inbox: entities/koordinator/inbox/SIS__shard-checkpoint-s1o2-interface-negative-matrix-r01-independent-review__KOO.md; blob 7fbbd445934da390a9517db1d23f36ead6042f48; read by KOO here. Inbox/dispatch do not themselves prove receipt. KOD also has an addressed SIS inbox, but publication alone does not prove KOD receipt or processing.

SIS exact independent review:
puev5691/wellbeing-hq@3931175ca7089079fbc815928a429c6b017bccb9:entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-interface-negative-matrix-r01-independent-review__KOO-KOD.md
blob ec9f3e0457701e2b0f2cb489e810c99e8494e683
terminal FAIL_SIS_SHARD_CHECKPOINT_S1O2_INTERFACE_NEGATIVE_MATRIX_R01_DOCUMENT_REVIEW_OPERATION_DEDUPE_DOMAIN_AMBIGUOUS

Exact immutable KOD baseline candidate:
puev5691/wellbeing-hq@cf468b7772cbde41ba1817ee2b5e5806e7bdc3e5:entities/koder/outbox/KOD__shard-checkpoint-s1o2-interface-negative-matrix-r01.md
blob c77ccbac2c74c64c499678fda2cae8a93ff9025e

Original task:
puev5691/wellbeing-hq@88c44d0ca5492a7e6b9fbb92aee01e571da22fb2:entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-interface-negative-matrix-r01__KOD.md
blob 49bf7b16faf7880a25faef9d67222ba6ef64bf00

## One bounded KOD correction

Freshly read all exact inputs. Create a **new immutable successor candidate document** preserving all unrelated content, task fixture, positive row and remaining 15 negative rows. Correct only contract wording and N06, N07, N08 as necessary to make operation-specific reconciliation unambiguous:

1. Define distinct operation-qualified dedupe identity, e.g. `{namespace, task_revision_ref, operation, request_id}` with at least `PUT_IMMUTABLE` and `COMMIT_CURRENT_CAS`, or explicit separate put_request_id and cas_request_id. If a request ID remains in immutable object, state exactly which operation it identifies and its digest relation.
2. `ResolveRequest` must take/resolve the exact operation, and persisted outcome must bind operation-specific payload: PUT checkpoint/object digest and recorded/not-recorded state; CAS expected tuple, successor tuple and pointer committed/not-committed state.
3. N06/N07 same-key/same-bytes and same-key/different-bytes comparisons explicitly occur within the same operation-qualified dedupe domain. A successful PUT duplicate is not a successful CAS duplicate.
4. N08 distinguishes object recorded but pointer not committed, pointer committed, neither, and unresolved UNKNOWN; a lost CAS ack cannot be called COMMITTED because PUT succeeded.
5. `StorageAck`/transaction token and readback proof must bind the exact operation/transaction and its commit evidence. Preserve separation between durable object and current pointer.

Publish new candidate, exact diff vs immutable baseline, addressed result to KOO, immutable readback for each. Report exact changed sections/lines and prove no other content was changed; on mismatch/competing successor stop with exact blocker. Do not claim the prior SIS FAIL closed before independent bounded re-review. No synthetic runtime test.

## Boundaries

CHECKPOINT_DURABLE: NOT_ESTABLISHED. BOUNDED_TASK_RESUME_AUTHORITY: NOT_GRANTED. Owner: NOT_APPOINTED. No implementation, code, shard WRITE, synthetic execution, host/shard access, secrets, provider call, automatic activation, automation/Project Source/canon change, backend/host or numeric retention/RPO/RTO selection. Memory-layering attempt 3: NOT_AUTHORIZED. Historical PROMPT never replay. Publication/dispatch/inbox do not prove receipt, activation or processing_started. Next independent SIS re-review only after correction and separate fresh KOO reconciliation.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
