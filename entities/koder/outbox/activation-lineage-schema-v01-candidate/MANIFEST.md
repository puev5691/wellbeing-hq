# Activation-lineage schema v0.1 candidate — manifest

status: `SCHEMA_CANDIDATE_READY_FOR_ORG_REVIEW`
implementation: no
runtime_validator: no
scheduler: no
automation_change: no
production: no
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Exact task basis

Task artifact:
`entities/koordinator/outbox/KOO__activation-lineage-schema-review-v01__KOD.md`
commit `4b8275e94ef3835be62743c71d5b1b3a294aed95`
blob `76b7e673bfed3d23c2914c3de61948ce9005b932`.

Accepted VOL basis:
`entities/volonter/outbox/VOL__activation-lineage-candidate-v02__KOO.md`
commit `d4ad859c1524daa05a89c51fb251c3cf17e565be`
blob `87ca81187635afe3f9fb0014b86b88f686432a58`.

Machine candidate:
`entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl`
commit `6021bd68861843a3e50a4a35cef82803baed3a76`
blob `b25e61a2317290d75078535d546a03ee457bb127`.

SHT contract-fit basis:
`entities/shtabist/outbox/SHT__activation-lineage-contract-fit-review__KOO.md`
commit `d58fa92da7356722b17c21178ce29883635dd53b`
blob `4d4d994f3f6397c639a2664deb8fd74851207ad1`.

KOO corrected-candidate acceptance:
`routes/receipts/VOL__activation-lineage-candidate-v02__KOO.receipt.md`
commit `63c22e0b51b61987ba09f6a04b855f838aca769b`
blob `07c43648484484c0c4297d56dba2ed36aced4c9b`.

## Package files and blobs before manifest commit

- `schema.json` — blob `8bf9e8d4900b4994bdb4a1dd7d78c1c4fa90470f`;
- `CROSS_RECORD_INVARIANTS.md` — blob `f33d512f584a046ffb5092940ec93c1eb6ce32f1`;
- `FIELD-MAP.md` — blob `8f52b57a862e6bef821850dfa2da5b2aa2805213`;
- `TEST-VECTORS.md` — blob `548a64291e9adaa919b726a2169824caf3d52008`.

## Review observations over exact 24-record candidate

- records: `24`;
- semantic records: `8`;
- transport records: `16`;
- `source_relation`: `5 causal_parent`, `16 transport_predecessor`, `3 null`;
- explicit bridge-reference records: `A-EVT-03`, `A-EVT-05`, `A-EVT-06`;
- `acceptance_status`: `2 PROVEN`, `6 UNKNOWN`, `16 NOT_APPLICABLE`;
- all dispatch/inbox/receipt/activation-attempt records: `NOT_APPLICABLE` acceptance with null scope;
- all five activation-attempt records: `activation_failed`, not real processing;
- semantic `event_time`: null throughout v0.2;
- loaded Git timestamps are represented as publication time only;
- no `real_processing_start` event class exists in v0.2.

## Structural JSON Schema boundary

`schema.json` expresses only per-record constraints that JSON Schema can actually enforce, including:
- field types/requiredness;
- observed enum/nullable boundaries;
- explicit relation typing and source/null coupling;
- semantic versus transport field/stage separation;
- `PROVEN` acceptance requiring a non-null bounded scope;
- transport lifecycle forcing `NOT_APPLICABLE` acceptance;
- event-specific transport state constraints;
- `verification_scope=current_event_record_claim_only`;
- Git publication/domain-event time separation for current v0.2 semantics;
- rejection of undeclared fields.

## Explicitly outside JSON Schema

The following are specified only in `CROSS_RECORD_INVARIANTS.md` for a future separate validator layer:
- global `event_id` uniqueness;
- reference target existence and no self-reference;
- causal/transport/bridge target correctness across records;
- experiment/task lineage separation and bridge non-merge semantics;
- append-only/non-retroactive bridge rules;
- evidence propagation prohibition;
- immutable Git artifact/commit/blob correspondence;
- acceptance evidence provenance and scope non-widening;
- prohibition on promotion from activation attempt to real processing;
- semantic time provenance/equivalence.

No validator/runtime/scheduler/automation was written.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: manifest и immutable source boundary candidate package перед организационным review
СТАТУС: SCHEMA_CANDIDATE_READY_FOR_ORG_REVIEW
