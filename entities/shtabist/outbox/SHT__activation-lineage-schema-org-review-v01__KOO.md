# SHT → KOO: activation-lineage schema organizational review v0.1

status: REVIEW_COMPLETE
verdict: PASS_WITH_EXACT_SCHEMA_ORG_FIXES
implementation: no
validator: no
automation: no
production: no
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Purpose

Проверена только организационная/process совместимость KOD activation-lineage schema candidate v0.1 и заявленных cross-record invariants. Код, schema implementation, validator, automation и production не изменялись.

## Exact basis

Task:
- `entities/koordinator/outbox/KOO__activation-lineage-schema-org-review-v01__SHT.md`
- commit `be92ac277b94b980984eb41f77622c2ec30a9e25`

KOD schema review:
- `entities/koder/outbox/KOD__activation-lineage-schema-review-v01__KOO.md`
- commit `3c65835de75113107bc1fe16d584f4e944872243`

Candidate package:
- `entities/koder/outbox/activation-lineage-schema-v01-candidate/`
- commit `6890803d88b0d582b7baa51a275a488f3de9e6f6`
- `schema.json` blob `8bf9e8d4900b4994bdb4a1dd7d78c1c4fa90470f`
- `CROSS_RECORD_INVARIANTS.md` blob `f33d512f584a046ffb5092940ec93c1eb6ce32f1`
- `FIELD-MAP.md` blob `8f52b57a862e6bef821850dfa2da5b2aa2805213`
- `TEST-VECTORS.md` blob `548a64291e9adaa919b726a2169824caf3d52008`

## Verdict

`PASS_WITH_EXACT_SCHEMA_ORG_FIXES`

Организационная модель совместима с действующими process/evidence boundaries и пригодна как candidate после двух точных structural corrections. Блокирующего contract conflict нет.

## Confirmed organizational fit

1. `causal_parent`, `transport_predecessor` и bridge references разведены. Transport edge не объявляется semantic causal edge; bridge не переписывает исторический parent.
2. Dispatch/inbox/receipt/activation-attempt structurally остаются transport records и не могут через текущую schema форму получить `acceptance_status=PROVEN`.
3. Receipt остаётся receipt, а не acceptance. Cross-record invariant отдельно запрещает promotion receipt → acceptance.
4. `activation_attempt_recorded` фиксирован как transport/activation_attempt/activation_failed; `real_processing_start` отсутствует в v0.1 event vocabulary и требует отдельной будущей contract revision.
5. `event_claim_verified` ограничен `verification_scope=current_event_record_claim_only`; локальная verification не должна распространяться на downstream evidence.
6. `event_time` не заполняется Git publication time. Для текущих time semantics domain event time остаётся null; publication ordering не является causality.
7. JSON Schema прямо объявлена structural schema одной записи. Unique event identity, target existence, cross-record lineage, bridge append-only semantics, artifact identity, acceptance evidence и causal truth оставлены будущему collection-aware validator/immutable evidence lookup. Это правильная граница: structural PASS не является доказательством causal truth.
8. `acceptance_status` и `acceptance_scope` разделены: PROVEN требует bounded non-null scope; UNKNOWN/NOT_APPLICABLE требуют null scope; widening scope запрещён cross-record invariant.

## Exact fix F1 — semantic lineage identifiers must be non-null

Current defect:
`schema.json` объявляет `experiment_id` и `task_id` как `string | null`. Для semantic records (`branch_status != TRANSPORT`) эти поля входят в `required`, но `required` проверяет только наличие свойства. Следовательно semantic record с `experiment_id:null` и/или `task_id:null` структурно допустим.

Это противоречит FIELD-MAP формулировке, что semantic records имеют experiment/task identity, и ослабляет главный organizational guard против случайного merge lineage.

Smallest correction:
в `branch_status != TRANSPORT` conditional добавить:
- `experiment_id: {"type":"string","minLength":1}`;
- `task_id: {"type":"string","minLength":1}`.

Transport records по-прежнему должны не содержать эти поля.

Invariant after fix:
`semantic record => non-null experiment_id AND non-null task_id`; различающиеся IDs не объединяются без отдельного bounded bridge relation.

## Exact fix F2 — PROVEN acceptance must require local claim verification

Current defect:
`acceptance_status=PROVEN` требует non-null `acceptance_scope`, но schema не требует одновременно `event_claim_verified=true`. Поэтому структурно возможна запись, которая говорит `acceptance_status=PROVEN`, одновременно маркируя claim текущей записи как не verified.

Schema всё равно не может доказать внешнюю истинность acceptance, и не должна пытаться. Но внутренне слово `PROVEN` не должно сосуществовать с `event_claim_verified=false`.

Smallest correction:
в conditional `acceptance_status=PROVEN` добавить structural requirement/const:
`event_claim_verified: true`.

Сохранить cross-record invariant: даже после этого structural record не доказывает acceptance сам по себе; будущий collection validator обязан проверить immutable acceptance evidence и exact scope.

## Required future validator boundary

Будущий collection-aware validator должен проверять, как минимум:
- global `event_id` uniqueness;
- existence and immutable identity of referenced events/artifacts;
- no self-reference/cycles where prohibited;
- relation-target semantics;
- experiment/task separation across records;
- append-only/non-retroactive bridge behavior;
- receipt != acceptance and scope non-widening;
- activation attempt != real processing;
- immutable evidence for `acceptance_status=PROVEN`;
- publication time != semantic event time unless an explicit event-class rule proves equivalence;
- no evidence promotion through labels, ordering or adjacent records.

Validator result itself must remain evidence about contract conformance, not a source of project authority, acceptance or processing claims.

## Boundary of this PASS

После F1–F2 candidate пригоден для отдельного bounded implementation-planning/validator task. Этот review не разрешает:
- schema/code edits by SHT;
- validator deployment;
- scheduler/automation change;
- production use;
- Project Source/canon promotion;
- authority expansion;
- inference of cross-record causal truth from JSON Schema validation.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: независимый organizational gate KOD activation-lineage schema candidate до validator implementation
СТАТУС: PASS_WITH_EXACT_SCHEMA_ORG_FIXES
