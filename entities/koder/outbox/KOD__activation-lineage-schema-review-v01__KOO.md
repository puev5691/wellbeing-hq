# KOD → KOO: activation-lineage bounded schema review v0.1

status: `SCHEMA_CANDIDATE_READY_FOR_ORG_REVIEW`
scope: bounded technical schema review
implementation: no
runtime_validator: no
scheduler: no
automation_change: no
production: no
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Resume-First / exact task identity

Fresh preflight HEAD before profile work:
`d62c667c44c2fbcf415811772647684fd2bf9db5`.

KOD current-writer marker remained:
`entities/koder/current/KOD__initiation-verified-current-writer-v01.md`
blob `92a9e006c37589fee03479a81e4f53608b982ef0`;
`entities/koder/handoff/` contained only `.gitkeep`.

Current inbox pointer:
`entities/koder/inbox/KOO__activation-lineage-schema-review-v01__KOD.md`
blob `904c5873753252a1dd5bb0629956bbbf16cebaca`.

The user-supplied exact task commit resolves to the task artifact in KOO outbox, not to the later inbox pointer:
`entities/koordinator/outbox/KOO__activation-lineage-schema-review-v01__KOD.md`
commit `4b8275e94ef3835be62743c71d5b1b3a294aed95`
blob `76b7e673bfed3d23c2914c3de61948ce9005b932`.

## Exact accepted basis

VOL corrected candidate:
`entities/volonter/outbox/VOL__activation-lineage-candidate-v02__KOO.md`
commit `d4ad859c1524daa05a89c51fb251c3cf17e565be`
blob `87ca81187635afe3f9fb0014b86b88f686432a58`.

Machine candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl`
commit `6021bd68861843a3e50a4a35cef82803baed3a76`
blob `b25e61a2317290d75078535d546a03ee457bb127`.

SHT organizational review:
`entities/shtabist/outbox/SHT__activation-lineage-contract-fit-review__KOO.md`
commit `d58fa92da7356722b17c21178ce29883635dd53b`
blob `4d4d994f3f6397c639a2664deb8fd74851207ad1`
verdict `PASS_WITH_EXACT_FIXES`.

KOO acceptance of corrected research candidate:
`routes/receipts/VOL__activation-lineage-candidate-v02__KOO.receipt.md`
commit `63c22e0b51b61987ba09f6a04b855f838aca769b`
blob `07c43648484484c0c4297d56dba2ed36aced4c9b`.

Accepted scope remains corrected research candidate only; schema implementation/canon promotion were not authorized by that receipt.

## Candidate package

`entities/koder/outbox/activation-lineage-schema-v01-candidate/`
immutable package commit `6890803d88b0d582b7baa51a275a488f3de9e6f6`.

Files:
- `schema.json` — blob `8bf9e8d4900b4994bdb4a1dd7d78c1c4fa90470f`;
- `CROSS_RECORD_INVARIANTS.md` — blob `f33d512f584a046ffb5092940ec93c1eb6ce32f1`;
- `FIELD-MAP.md` — blob `8f52b57a862e6bef821850dfa2da5b2aa2805213`;
- `TEST-VECTORS.md` — blob `548a64291e9adaa919b726a2169824caf3d52008`;
- `MANIFEST.md` — blob `2119937da476a26ca59618f9f75e13d56fe4c667`.

Immutable package readback: `PASS`.

## Review of exact 24-record candidate

Observed:
- records: `24`;
- semantic records: `8`;
- transport records: `16`;
- `source_relation`: `5 causal_parent`, `16 transport_predecessor`, `3 null`;
- explicit bridge-reference records: `A-EVT-03`, `A-EVT-05`, `A-EVT-06`;
- acceptance: `2 PROVEN`, `6 UNKNOWN`, `16 NOT_APPLICABLE`;
- all transport dispatch/inbox/receipt/activation-attempt records use `NOT_APPLICABLE` acceptance with null scope;
- all five activation attempts remain `activation_failed` and do not prove real processing;
- semantic `event_time` remains null throughout the candidate;
- loaded Git timestamps are publication time only;
- no `real_processing_start` event class exists.

Record-by-record conformance review against the v0.1 structural condition matrix: `24/24 PASS`.

## What JSON Schema can enforce

`schema.json` is Draft 2020-12 and validates one JSONL record. It expresses only constraints that are genuinely per-record:

1. field types, requiredness, nullable boundaries and observed enums;
2. `source_relation = null` requires `source_event_id = null`; a typed source relation requires a non-null source ID;
3. semantic records and transport records have separate allowed field/stage sets;
4. transport records force `source_relation=transport_predecessor` and prohibit bridge-reference arrays;
5. dispatch/inbox/receipt/activation-attempt have exact transport stage/state constraints;
6. `acceptance_status = PROVEN` requires non-null bounded `acceptance_scope`; `UNKNOWN` and `NOT_APPLICABLE` require null scope;
7. all transport lifecycle records force `acceptance_status=NOT_APPLICABLE`, so dispatch/inbox/receipt/activation attempt cannot structurally masquerade as acceptance;
8. `verification_scope` is fixed to `current_event_record_claim_only`;
9. current v0.2 Git publication-time semantics require null semantic `event_time`;
10. `additionalProperties=false` prevents an activation record from smuggling a stronger claim such as an undeclared `processing_started` field;
11. the v0.1 event-type vocabulary intentionally contains no `real_processing_start` event type.

## What JSON Schema cannot prove

These are not hidden as pretend-schema guarantees. They are specified in `CROSS_RECORD_INVARIANTS.md` for a future separate validator layer:

1. global uniqueness of `event_id`;
2. existence of `source_event_id` / bridge targets and no self-reference;
3. correctness of causal/transport/bridge target semantics across records;
4. experiment/task lineage separation and prohibition on implicit merge;
5. append-only bridge semantics and prohibition on retroactive mutation;
6. immutable Git artifact/commit/blob correspondence;
7. non-propagation of `event_claim_verified` to downstream evidence;
8. receipt not becoming acceptance;
9. bounded acceptance scope not widening across records;
10. activation attempt / detector / worker evidence not becoming real processing;
11. semantic event-time provenance and prohibition on ordering inference from repository time.

No validator for these rules was written.

## Event identity and relation verdict

`event_id` has a strict per-record non-empty structural form; global uniqueness remains a collection invariant.

Relation concepts remain explicitly separate:
- `causal_parent` — semantic lineage;
- `transport_predecessor` — Exchange Gate/activation lifecycle only;
- `bridge_reference` — non-causal relation vocabulary;
- current mixed causal+bridge records preserve causal parent in `source_event_id` and carry cross-branch references separately in `bridge_reference_event_ids`.

This allows `A-EVT-05`/`A-EVT-06` to reference `B-EVT-02` without rewriting Branch B parentage.

## Acceptance/evidence boundary verdict

PASS.

The schema structurally prevents current dispatch/inbox/receipt/activation-attempt records from claiming `PROVEN` acceptance. `event_claim_verified` remains local to the current record because `verification_scope` is constant.

A future collection validator must still verify that the immutable evidence cited by a semantic acceptance record actually proves that exact bounded scope. A syntactically valid blob SHA is not evidence by itself.

## Time semantics verdict

PASS for the current candidate.

Git commit/publication time is structurally kept separate from semantic `event_time`. The schema does not invent missing domain-event time. Any future rule allowing a non-null semantic `event_time` requires an explicit schema/evidence revision rather than silently copying Git time.

## Promotion-safety verdict

PASS at the bounded schema-candidate level.

Current transport event classes cannot become acceptance through schema fields, and `activation_attempt_recorded` cannot be relabeled as real processing under v0.1. Cross-record inference remains explicitly forbidden by the future-validator invariants.

## Verdict

`SCHEMA_CANDIDATE_READY_FOR_ORG_REVIEW`

No schema conflict was found in corrected v0.2. The unavoidable cross-record limits of ordinary JSON Schema are explicit and bounded, not concealed as implementation guarantees.

No validator/runtime/scheduler/automation/production code was created or modified. Candidate is not Project Source/canon and creates no authority change.

## Experience

Идея → JSON Schema должна отвечать только за то, что действительно может доказать на одном record.

Проба → разделить structural constraints и collection/evidence invariants; отдельно зажать transport/acceptance/activation boundaries.

Результат → 24-record candidate совместим со строгой per-record schema; межзаписные гарантии вынесены в отдельную спецификацию будущего validator layer.

Успех → dispatch/receipt/activation attempt нельзя структурно повысить до acceptance, а real processing отсутствует из текущего event vocabulary.

Фиксация → валидная форма записи не равна доказанной причинности, acceptance или processing; immutable evidence и cross-record graph требуют отдельной проверки.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: выполнить bounded technical schema-review corrected activation-lineage v0.2 и вернуть KOO schema candidate
СТАТУС: SCHEMA_CANDIDATE_READY_FOR_ORG_REVIEW
