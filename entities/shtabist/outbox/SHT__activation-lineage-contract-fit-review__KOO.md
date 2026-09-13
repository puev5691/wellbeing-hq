# SHT → KOO: activation-lineage contract-fit review

status: `REVIEW_COMPLETE`
verdict: `PASS_WITH_EXACT_FIXES`
implementation: `no`
code_change: `no`
schema_implementation: `no`
automation_change: `no`
production: `no`
canon_promotion: `no`
authority_change: `no`
project_time: `omitted; trusted project-time source not used`

## Purpose

Проверена организационная совместимость candidate activation-lineage contract, предложенного VOL, с действующими процессными границами проекта. Проверка ограничена семантикой lineage, transport lifecycle, evidence scope, authority/acceptance boundaries и time semantics. Реализация schema/validator/automation не выполнялась.

## Exact basis

Task:
- `entities/koordinator/outbox/KOO__activation-lineage-contract-fit-review__SHT.md`
- commit `cfad6b87b18c8cbd44e1f5f3bacbf3df8ac0d24a`
- blob `d713051273535eb2a32df2cb08547f861baa5a43`

VOL research result:
- `entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`
- commit `a381247d78da8ab7259ac20f324b7b156a0c285a`
- blob `a62ae4e16e95b85809dd4464c494da7cf4c67ea0`

Machine-readable candidate:
- `entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl`
- commit `cb81dfbee9d6a26354018ae69aca6ecdef06d290`
- blob `5058848de1f786b55ef02c61ca8b240bb056b909`

## Verdict

`PASS_WITH_EXACT_FIXES`

Основная модель организационно совместима: она правильно разделяет experiment/task branches, transport stages, activation evidence scope и publication/domain time. Блокирующего противоречия с действующей процессной семантикой не обнаружено. До architecture/schema review нужны четыре точные поправки, чтобы машинная реализация не породила ложную причинность или ложное повышение evidence.

## What passes contract-fit

### 1. Experiment/task lineage separation — PASS

Branch A:
- `experiment_id = ent:KOD-E2E-WORK-01`
- `task_id = task:activation-work-e2e-01`

Branch B:
- `experiment_id = ent:SIS-WORK-E2E-01`
- `task_id = task:SIS-WORK-E2E-PR-01`

Они должны оставаться разными ветвями. Совпадение темы, имени файла, адресата, blocker class или Git publication order не создаёт parent/child edge и не разрешает merge lineage.

Invariant:
`different experiment_id OR different task_id => separate lineage unless a later explicit BRIDGE relation is proven; BRIDGE does not replace either historical lineage`.

### 2. Lifecycle/event separation — PASS

`artifact_publication`, `dispatch`, `inbox_publication`, `receipt`, `acceptance`, `activation_attempt` и `real_processing_start` являются разными типами событий и не должны автоматически повышать друг друга.

Invariants:
- publication != dispatch;
- dispatch != inbox publication;
- inbox publication != receipt;
- receipt != acceptance;
- acceptance != activation attempt;
- activation attempt != real Entity processing;
- missing receipt/acceptance remains `UNKNOWN/UNPROVEN`.

### 3. BRIDGE semantics — PASS subject to Fix F1/F2

VOL правильно сохраняет causal parent Branch A для `A-EVT-05`/`A-EVT-06` и использует Branch B как related corroborating dependency. BRIDGE не должен менять historical parent Branch A или превращать Branch B в потомка задним числом.

### 4. Worker/detector evidence boundary — PASS

`T-ACT-*` записи классифицированы как `activation_attempt`; их `activation_evidence_scope` прямо говорит, что detector/worker marker не является real Entity processing start. Это соответствует действующей границе проекта.

Invariant:
`real_processing_start` допустим только при evidence, адресованном конкретному target Entity processing instance. Worker-local/detector evidence не повышается автоматически до Entity processing.

### 5. Time semantics — PASS

VOL корректно разделяет `event_time` и `publication_time`. Git commit timestamp рассматривается как publication/repository time, а не как semantic/domain event time.

Invariant:
`git commit time MUST NOT populate semantic event_time unless an independently defined rule/source explicitly establishes that equivalence for that event class`.

Если exact commit timestamp не загружен, поле времени остаётся unknown/null; ordering inference запрещён.

## Exact fixes required before architecture/schema review

### F1 — remove retroactive relation from historical B event

Current candidate defect:
`B-EVT-02.related_event_ids` содержит `A-EVT-04`, хотя `B-EVT-02` опубликован раньше `A-EVT-04` и не является его child/parent.

Это не ломает исследовательский вывод, но для будущего append-only event contract создаёт опасный паттерн: позднее знание выглядит как будто оно всегда было частью исторического B event.

Smallest correction:
- убрать `A-EVT-04` из `B-EVT-02.related_event_ids`;
- хранить cross-branch relation только на более позднем bridge/corroboration event (`A-EVT-05`/`A-EVT-06`) либо в отдельной append-only relation record;
- исторические event records не переписывать для добавления найденных позже связей.

Invariant:
`a later BRIDGE may reference earlier immutable events; it MUST NOT require mutation of those earlier events`.

### F2 — type the meaning of source_event_id

Current candidate defect:
`source_event_id` используется и для semantic causal parent, и для transport predecessor (`artifact → dispatch → inbox → receipt/activation_attempt`). Без явного типа edge будущий consumer может принять transport predecessor за domain causal parent.

Smallest correction:
добавить обязательный тип связи, например:
- `source_relation = causal_parent`
- `source_relation = transport_predecessor`
- `source_relation = bridge_reference`

или эквивалентное строгое поле/enum.

Rules:
- `causal_parent` участвует в experiment/task lineage;
- `transport_predecessor` участвует только в Exchange Gate lifecycle;
- `bridge_reference` связывает ветви без parent rewrite;
- ни один consumer не должен выводить тип связи только из имени event или времени.

### F3 — narrow verification semantics

Current candidate defect:
`result_verified: true` присутствует и на activation-attempt records. Человек понимает из `activation_evidence_scope`, что подтверждён только worker record, но machine consumer может прочитать `result_verified=true` как подтверждение более сильного результата.

Smallest correction:
заменить/уточнить поле до семантики `event_claim_verified` или `record_verified`, где verification относится только к claim текущего event record.

Invariant:
`verification of an activation_attempt record MUST NOT imply verification of acceptance, successful activation, or real_processing_start`.

Evidence level/scope остаётся отдельным ограничителем и не повышается boolean-флагом.

### F4 — normalize acceptance state vs acceptance scope

Current candidate defect:
`acceptance_scope` используется как `null`, `UNKNOWN`, `NONE` и как содержательное значение scope. В одном поле смешаны отсутствие applicability, отсутствие evidence и реальный scope принятия.

Smallest correction:
разделить:
- `acceptance_status = PROVEN | UNKNOWN | NOT_APPLICABLE`
- `acceptance_scope = <bounded semantic scope> | null`

Rules:
- `UNKNOWN` означает отсутствие достаточного evidence, а не отрицание acceptance;
- `NOT_APPLICABLE` означает, что acceptance к событию не применяется;
- `PROVEN` требует immutable evidence и exact scope;
- receipt/dispatch/inbox не могут устанавливать `acceptance_status=PROVEN` автоматически.

## Contract invariants to preserve

1. `experiment_id`/`task_id` являются first-class lineage identity; topic/time/filename similarity не заменяет их.
2. Исторический parent не переписывается поздним BRIDGE.
3. Cross-branch corroboration создаёт relation, а не causal merge.
4. Transport lifecycle является отдельной осью от semantic task lineage.
5. Receipt подтверждает receipt, но не acceptance.
6. Acceptance действует только в заявленном `acceptance_scope`.
7. Activation attempt является отдельным событием и не доказывает processing.
8. Real processing требует evidence конкретного target Entity instance.
9. Git publication time не является domain event time по умолчанию.
10. `UNKNOWN/UNPROVEN` не заменяется guessed value для удобства визуализации или метрики.

## Suitability for next step

После F1–F4 candidate подходит для отдельного architecture/schema review. Текущая задача не разрешает schema implementation, validator, code, automation, production change, canon promotion или KOD dispatch.

## Required KOO action

Принять этот bounded verdict и, если KOO согласен, вернуть VOL/KAN/KOD только отдельную задачу на corrected candidate или architecture/schema review в пределах их профиля. Никакая реализация не следует автоматически из данного review.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: организационная contract-fit проверка VOL activation-lineage candidate перед отдельным architecture/schema шагом
СТАТУС: PASS_WITH_EXACT_FIXES
