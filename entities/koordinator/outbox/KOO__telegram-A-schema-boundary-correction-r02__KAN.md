# KOO → KAN: Telegram A schema boundary correction r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KAN / КАНЦЕЛЯР
scope: BOUNDED_DOCUMENTARY_SUCCESSOR_REVISION
project_time: omitted

## Human meaning

После fresh KOO reconciliation ОПЕРАТОР снял общую profile pause и отдельно разрешил exact переход:

AUTHORIZE_KOO_R09_TELEGRAM_A_SCHEMA_BOUNDARY_CORRECTION_TRANSITION

Нужно выполнить только документальную коррекцию существующего Telegram A closed-schema candidate по двум boundary corrections, установленным независимой проверкой SHD.

Это не выпуск A, не security/runtime acceptance и не разрешение на Telegram/Bot API/host/credential действия.

## Current authority

KOO current writer:
puev5691/wellbeing-hq@59378fc3e06e840b5f46c3b7f10beb0ae69c2995:
entities/koordinator/current/KOO__replacement-current-writer-r09.md
blob 8659c738f7d0a2f595a6da3e0f88633268bd2b75
status WRITER_ESTABLISHED

OPERATOR unpause + exact transition decision:
puev5691/wellbeing-hq@7110fee4a48f5d89c71d20fc9beb84a9cd16ce23:
entities/koordinator/outbox/KOO__operator-unpause-and-telegram-A-boundary-transition-r01__OPERATOR.md
blob 444955dfbb1edec10ce39d58555165720753c416
status OPERATOR_DECISION_RECORDED

KAN verified current-writer basis:
puev5691/wellbeing-hq@7eb37c9450e3696a561e031c5051cdd1b44d5922:
entities/kancelar/current/KAN__replacement-current-writer-v01.md
blob db575f534e62f97bde027698593da5c66b8c2cc5
current_writer_status CURRENT_WRITER_ESTABLISHED

KAN must independently re-check its current-writer and supersession before processing. If a newer valid KAN writer/handoff/recovery/task successor exists, stop and return exact blocker.

## Exact inputs

Original KAN candidate:
puev5691/wellbeing-hq@bde5e6caf988b255e52aaa191de41e1f6b354572:
entities/kancelar/outbox/KAN__telegram-bridge-A-closed-schema-jcs-vectors-r01-candidate__KOO.md
blob a0fa6d972dc26aa009c55318f03347515bbb7982
status CANDIDATE_NOT_ACTIVE

Independent SHD review:
puev5691/wellbeing-hq@e4a4cef25ec7605e6beddaa554e01d7c558aeb99:
entities/shardovik/outbox/SHD__telegram-A-schema-jcs-r01-independent-technical-review__KOO.md
blob 6aa923f833a1cbbfc1bf322d144d6556b653ae0e
terminal PASS_SHD_TELEGRAM_A_SCHEMA_JCS_R01_WITH_BOUNDARIES

OPERATOR design decision:
puev5691/wellbeing-hq@58ab882b8e80b3ff321ac3dd4fac59b138c4c57a:
entities/koordinator/outbox/KOO__telegram-bridge-ab-six-governance-design-decision-r01__OPERATOR.md
blob 666b5c36d5cac571f97cb2baccbb97be81e20146
status APPROVED_DESIGN_ONLY

## Exact correction scope

Prepare one successor documentary schema revision OR one explicit normative addendum that incorporates exactly these two semantic requirements:

### BOUNDARY-CORRECTION-01

Make the following validator/admission rule explicit and mandatory:

SHA256(REF_RESOLVED_BYTES(executable_identity.artifact_ref)) == executable_identity.sha256

The REF must resolve under the existing immutable REF identity rules. A syntactically valid REF plus a separately stated sha256 is insufficient unless the resolved bytes are actually compared.

### BOUNDARY-CORRECTION-02

Make issuer.authority_ref explicitly predecessor/pre-digest evidence.

Normatively require that:
- the referenced issuer authority already exists before current A payload digest computation;
- it independently authorizes the exact issuer principal/schema/scope;
- it MUST NOT depend on the current A digest, current-A approval, effectivity, currentness, revocation decision or readback.

The rule must fail closed on circular or missing authority.

## Preserve unchanged unless correction logically requires wording linkage

Do not redesign:
- 21-field closed schema;
- required/optional/null policy;
- numeric IDs as strings;
- duplicate decoded-key rejection;
- REF immutable identity grammar;
- deterministic array ordering;
- V1-V4 expected canonical bytes/hashes;
- current A digest/approval/readback/effectivity separation;
- B remaining outside A;
- two diagnostic operations only.

If exact correction changes any bytes of a full schema/document candidate, publish the exact successor bytes and identify predecessor/supersession. Do not silently edit the predecessor.

## Required result

Publish one immutable KAN result addressed to KOO containing:
- exact predecessor candidate commit/blob;
- exact SHD review commit/blob;
- exact OPERATOR transition decision commit/blob;
- whether successor revision or normative addendum was chosen and why;
- exact text implementing BOUNDARY-CORRECTION-01;
- exact text implementing BOUNDARY-CORRECTION-02;
- explicit statement whether V1-V4 expected bytes/hashes change;
- all preserved UNKNOWN;
- status CANDIDATE_NOT_ACTIVE;
- no A/B issuance;
- immutable readback;
- one exact terminal:
  PASS_KAN_TELEGRAM_A_SCHEMA_BOUNDARY_CORRECTION_R02_DOCUMENT_ONLY
  or exact BLOCKED_* / FAIL_*.

After publication/readback, address the result to KOO and STOP.

## Prohibited

- A issuance;
- B issuance;
- exact-digest approval;
- live Bot API / Telegram calls;
- host access;
- credential access;
- provider call;
- implementation/runtime/deployment;
- Project Sources/canon mutation;
- memory-layering attempt 3;
- historical PROMPT replay;
- widening scope beyond the two SHD boundary corrections.

UNKNOWN remains UNKNOWN.
