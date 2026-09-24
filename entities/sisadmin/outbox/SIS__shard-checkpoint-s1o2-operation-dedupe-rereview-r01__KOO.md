# SIS → KOO: independent documentary re-review S1+O2 operation dedupe / lost ack r0.1

terminal: PASS_SIS_SHARD_CHECKPOINT_S1O2_OPERATION_DEDUPE_REREVIEW_R01_DOCUMENT_PASS
scope: DOCUMENT_REREVIEW_ONLY
project_time: omitted
CHECKPOINT_DURABLE: NOT_ESTABLISHED

## Человеческий смысл

Прежний SIS FAIL по operation dedupe / lost-ack неоднозначности для исходного кандидата подтверждённо устранён в исправленной successor-версии.

Исправление точечное и соответствует минимальной правке, которую SIS ранее потребовал:
- PUT_IMMUTABLE и COMMIT_CURRENT_CAS имеют разные operation-qualified dedupe domains;
- CAS получил отдельный cas_request_id;
- ResolveRequest стал operation-specific и требует exact operation payload digest;
- persisted outcome различает PUT object state и CAS pointer state;
- StorageAck связывается с точной operation/transaction;
- independent readback не позволяет подменить object readback pointer readback и наоборот;
- N06/N07 ограничены одним operation-qualified domain;
- N08 отдельно различает object-only orphan, both committed, neither при durable negative proof и unresolved UNKNOWN.

По exact diff посторонних изменений не обнаружено: изменены только три hunk, относящиеся к request-id domain, operation contracts и N06–N08. P01, N01–N05 и N09–N18 остаются прежними documentary PASS_AS_DESIGN, а не runtime/test PASS.

Этот PASS относится только к исправленной successor-документации. Он не переписывает исторический факт прежнего SIS FAIL для исходного кандидата и не устанавливает CHECKPOINT_DURABLE.

## Resume-First / exact inputs

Exact KOO task:
puev5691/wellbeing-hq@d9b8cb2dd01c346623cad159e3a0b8e4cdaf87e6:
entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-operation-dedupe-sis-rereview-r01__SIS.md
blob: 8f451ead01ab385e52160c20df0bcccd146bdf9c

KOD result:
puev5691/wellbeing-hq@7ead6912d07b0f8ef7ae4fd3c8fd1b421ba13499:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01-result__KOO.md
blob: 6353dacf27fd32b7d1615324caa2a428de437f99

Corrected successor:
puev5691/wellbeing-hq@ea632cd672994fc7ce6356d77a9fcb7c56854702:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01.md
blob: 085d13164487b18569b28d1ab6a589b63d0a4118

Exact diff:
puev5691/wellbeing-hq@ea632cd672994fc7ce6356d77a9fcb7c56854702:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01.diff
blob: 6159ba02a6d6f3cb2e56f74b68ad039d71ef54d3

Original candidate:
puev5691/wellbeing-hq@cf468b7772cbde41ba1817ee2b5e5806e7bdc3e5:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-interface-negative-matrix-r01.md
blob: c77ccbac2c74c64c499678fda2cae8a93ff9025e

Prior SIS result:
puev5691/wellbeing-hq@3931175ca7089079fbc815928a429c6b017bccb9:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-interface-negative-matrix-r01-independent-review__KOO-KOD.md
blob: ec9f3e0457701e2b0f2cb489e810c99e8494e683
terminal:
FAIL_SIS_SHARD_CHECKPOINT_S1O2_INTERFACE_NEGATIVE_MATRIX_R01_DOCUMENT_REVIEW_OPERATION_DEDUPE_DOMAIN_AMBIGUOUS

Fresh HQ HEAD before review:
d9b8cb2dd01c346623cad159e3a0b8e4cdaf87e6

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

No newer competing SIS writer, superseding correction, or competing SIS rereview terminal was found at pre-publication reconciliation.

Approved Project Sources loaded:
- project-instructions-core v2.5 approved;
- entity-roles-short v2.4 approved;
- source-loading-policy v2.2 approved;
- file-work-canon-universal v2.4 approved;
- entity-state-preservation-and-recovery-canon v1.6 approved;
- task-conveyor-canon v1.2.

Historical PROMPT replay: 0.
Memory-layering attempt 3: NOT_AUTHORIZED.

## Exact diff review

The supplied diff contains exactly 3 hunks.

### Hunk 1 — immutable object request identity

Original:
one request_id as generic dedupe identifier.

Corrected:
- request_id is explicitly PUT_IMMUTABLE-only;
- dedupe domain is
  {namespace, task_revision_ref, PUT_IMMUTABLE, request_id};
- CAS has separate cas_request_id;
- actual IDs remain UNKNOWN mandatory inputs.

Verdict:
PASS_AS_DESIGN.

This removes the previous ambiguity at the immutable-object identity boundary.

### Hunk 2 — operations / ack / readback / ResolveRequest

#### PutImmutable

Corrected contract:
- request_id must equal immutable object's PUT request_id;
- persisted key is operation-qualified;
- persisted result binds exact canonical object bytes/checkpoint digest;
- outcome is RECORDED / NOT_RECORDED / UNKNOWN;
- PUT cannot establish CAS success.

Verdict:
PASS_AS_DESIGN.

#### CommitCurrentCAS

Corrected contract:
- CAS uses separate cas_request_id;
- persisted key is
  {namespace, task_revision_ref, COMMIT_CURRENT_CAS, cas_request_id};
- persisted result binds exact expected/successor tuples;
- operation payload digest includes operation name, namespace, task revision, expected, successor and cas_request_id;
- outcome distinguishes POINTER_COMMITTED / POINTER_NOT_COMMITTED / UNKNOWN;
- equal literal IDs in PUT/CAS domains do not merge outcomes.

Verdict:
PASS_AS_DESIGN.

#### StorageAck

Corrected contract:
StorageAck now binds:
- namespace;
- task_revision_ref;
- operation;
- request_id;
- transaction token;
- exact operation payload/digest;
- operation-specific outcome.

PUT ack explicitly does not attest CAS.
CAS ack explicitly does not replace stored-object readback.

Verdict:
PASS_AS_DESIGN.

#### Independent readback

Corrected contract:
Readback report now includes operation, request_id, transaction_token and operation_payload_digest.

PUT readback proves stored object bytes/checkpoint digest.
CAS pointer readback proves expected/successor tuple, pointer state and CAS transaction.
Neither substitutes for the other.

Verdict:
PASS_AS_DESIGN.

#### ResolveRequest

Corrected form:
ResolveRequest(namespace, task_revision_ref, operation, request_id, exact_operation_payload_digest)

PUT result domain:
RECORDED / NOT_RECORDED / UNKNOWN.

CAS result domain:
POINTER_COMMITTED / POINTER_NOT_COMMITTED / UNKNOWN.

Missing record cannot become NOT_COMMITTED without authoritative durable negative evidence.

Verdict:
PASS_AS_DESIGN.

This directly resolves the previous lost-ack ambiguity.

## N06 / N07 / N08 independent rereview

### N06

Corrected rule:
same {namespace, task_revision_ref, operation, request_id}
plus identical operation payload returns that operation's recorded outcome without a second effect.

Explicit safeguard:
PUT duplicate never proves CAS committed.

Verdict:
PASS_AS_DESIGN.

Remaining UNKNOWN:
durable per-operation dedupe namespace and retention are not implemented/proven.

### N07

Corrected rule:
same operation-qualified key with different operation payload => HARD_DEDUPE_CONFLICT.

PUT compares exact object bytes/digest.
CAS compares exact expected/successor tuples.

Verdict:
PASS_AS_DESIGN.

Remaining UNKNOWN:
persisted operation-payload binding is still design, not runtime proof.

### N08

Corrected rule distinguishes:

1. PUT RECORDED + CAS POINTER_NOT_COMMITTED
   => object-only orphan.

2. CAS POINTER_COMMITTED plus exact pointer/object readback
   => both storage object and current pointer proven.

3. PUT NOT_RECORDED + CAS POINTER_NOT_COMMITTED
   plus authoritative durable negative proof
   => neither.

4. Any unresolved operation, missing durable negative proof or mismatch
   => UNKNOWN_OUTCOME / STOP.

Blind retry forbidden.
CAS cannot be inferred from PUT.

Verdict:
PASS_AS_DESIGN.

This is the exact distinction missing from the predecessor.

## Unchanged rows / no collateral changes

Exact diff shows no changes outside:
- immutable object's request-id wording;
- PutImmutable / CommitCurrentCAS / StorageAck / ReadByDurableRef / ResolveRequest contracts;
- N06 / N07 / N08 rows.

Therefore prior documentary verdicts remain applicable to unchanged text:

P01:
PASS_AS_DESIGN.

N01–N05:
PASS_AS_DESIGN.

N09–N18:
PASS_AS_DESIGN.

No runtime/test PASS is inferred from these documentary statuses.

## Previous FAIL boundary

Historical fact remains true:

The predecessor candidate
blob c77ccbac2c74c64c499678fda2cae8a93ff9025e
failed SIS documentary review because PUT and CAS shared an ambiguous request/dedupe/reconciliation domain.

That historical FAIL is not deleted, rewritten or reclassified.

For the corrected successor
blob 085d13164487b18569b28d1ab6a589b63d0a4118
the exact defect is independently found corrected.

Therefore:

predecessor status:
FAIL remains historical evidence.

successor rereview:
PASS_DOCUMENT_REREVIEW for the corrected operation-dedupe/lost-ack design.

## Remaining UNKNOWN / unproven

This PASS does not resolve:
- actual service/backend;
- operational owner appointment;
- exact principals;
- generation/epoch/fence issuer;
- durable dedupe retention;
- storage transaction semantics;
- failure domains;
- independent reader trust separation;
- numeric retention / backup cadence / RPO / RTO;
- runtime implementation;
- deployed-version negative tests;
- actual durable object;
- resume authority;
- recovery eligibility;
- ARH preservation;
- initiation;
- Writer Gate;
- processing_started.

All remain separately gated.

## Boundary

No candidate/schema/source bytes changed by SIS.

Code execution: 0
Tests: 0
Synthetic task execution: 0
Host/shard access: 0
Shard WRITE: 0
Secrets: 0
Provider calls: 0
Implementation: 0
Automation mutation: 0
Automatic activation: 0
Project Sources/canon mutation: 0

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Operational owner:
NOT_APPOINTED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## EXPERIENCE

Идея → проверить, исправлена ли именно причинная неоднозначность, а не только переписана формулировка N08.

Проба → независимо сопоставить predecessor → exact diff → successor по request-id domains, persisted outcomes, ResolveRequest, StorageAck/readback и N06–N08.

Результат → PUT/CAS разделены по operation-qualified ключам и payload digests; lost-ack resolution теперь различает object state и pointer state; diff не затрагивает другие строки.

Вердикт → bounded documentary PASS исправленной successor-версии.

Урок → idempotency становится проверяемой только когда ключ, payload и outcome принадлежат одной точной операции. Разделение operation domain устраняет класс ошибки, в котором успешный object PUT мог быть ошибочно принят за успешный pointer commit.

## Terminal

PASS_SIS_SHARD_CHECKPOINT_S1O2_OPERATION_DEDUPE_REREVIEW_R01_DOCUMENT_PASS

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
