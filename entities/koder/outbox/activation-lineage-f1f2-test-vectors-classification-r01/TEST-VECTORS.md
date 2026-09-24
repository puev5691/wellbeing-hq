# Activation-lineage v0.1 candidate — test vectors

status: `CANDIDATE_FOR_ORG_REVIEW`
implementation: none
validator: not implemented
project_time: omitted; trusted project-time source not used

Test vectors are specified as mutations of exact v0.2 records. They define expected contract behavior without supplying validator/runtime code.

## Positive structural vectors

The following exact records from `VOL__activation-lineage-events-v02.jsonl` are representative valid cases:

1. `A-EVT-05` — semantic causal parent plus independent cross-branch bridge reference.
2. `A-EVT-06` — semantic acceptance with `acceptance_status=PROVEN` and bounded non-null `acceptance_scope`.
3. `T-DISPATCH-01` — transport dispatch, `NOT_APPLICABLE` acceptance.
4. `T-RECEIPT-01` — receipt remains transport and does not become acceptance.
5. `T-ACT-03` — activation attempt remains transport, state `activation_failed`, no real processing claim.

## Historical compatibility failures after F1

- `A-EVT-01` — historical semantic ROOT with experiment_id=null and task_id=null. F1 rejects it; its null relation, UNKNOWN acceptance, loaded publication time and null domain event time remain historical evidence.
- `A-EVT-02` — historical semantic CONTINUATION with experiment_id=null and task_id=null. F1 rejects it; its causal relation remains historical evidence.

Neither record is a positive structural vector for the successor schema. They are not repaired by guessing identifiers.

Successor result over unchanged 24 exact v0.2 lines: 22 STRUCTURAL_PASS; A-EVT-01 and A-EVT-02 STRUCTURAL_FAIL solely because both historical semantic identifiers are null. The original candidate was 24/24 PASS. Transport records remain 16/16 PASS. No historical record is silently rewritten.

## F1/F2 focused positive/negative vectors

Machine-readable cases with exact base event and mutation are in `TEST-FIXTURES.json`; F1 rejects null and empty semantic identifiers while retaining valid strings. F2 rejects PROVEN with event_claim_verified=false; UNKNOWN and transport remain bounded.

## Negative vectors that JSON Schema MUST reject

Apply each mutation independently to the named successor-valid record. Mutations of historical F1-incompatible records are classified separately below and do not isolate an additional successor rule.

| Vector | Mutation | Expected reason |
|---|---|---|
| S-N01 | `T-DISPATCH-01.acceptance_status = "PROVEN"`, scope non-null | Transport cannot claim acceptance. |
| S-N02 | `T-RECEIPT-01.acceptance_status = "PROVEN"` | Receipt is not acceptance. |
| S-N03 | `T-ACT-03.new_state = "real_processing_start"` | Activation attempt cannot be relabeled as real processing in v0.1. |
| S-N04 | `T-ACT-03.transport_stage = "acceptance"` | Activation attempt event/stage mismatch. |
| S-N05 | `A-EVT-06.acceptance_scope = null` | `PROVEN` requires exact non-empty scope. |
| S-N06 | `A-EVT-04.acceptance_status = "UNKNOWN"` plus non-null scope | Unknown acceptance must have null scope. |
| S-N08 | `T-INBOX-01.bridge_reference_event_ids=["B-EVT-02"]` | Transport record cannot carry semantic bridge references. |
| S-N09 | `T-DISPATCH-01.source_relation="causal_parent"` | Transport must use `transport_predecessor`. |
| S-N10 | any record `verification_scope="verified_result_and_downstream"` | Verification scope is fixed to current record claim only. |
| S-N13 | add undeclared property `processing_started=true` to `T-ACT-03` | `additionalProperties=false`; current activation record cannot smuggle processing proof through an extra field. |
| S-N14 | transport record adds `experiment_id` | Transport lifecycle is separated from semantic experiment/task fields. |

## Historical negative mutations, not isolated successor tests

S-N07 is based on A-EVT-02; S-N11 and S-N12 are based on A-EVT-01. All three starting records already fail successor F1 because experiment_id/task_id are null. These mutations illustrate additional intended constraints in historical evidence; failure of a mutated record alone does not demonstrate that the additional constraint caused rejection. An isolated successor test would require an independently valid starting record and a separate fixture/review, outside this explanatory correction.

| Vector | Historical mutation | Intended additional rule, not isolated by this baseline |
|---|---|---|
| S-N07 | `A-EVT-02.source_relation = null` while retaining `source_event_id="A-EVT-01"` | Null relation requires null source event. |
| S-N11 | `A-EVT-01.event_time = publication_time` | Current Git publication semantic explicitly requires null domain event time. |
| S-N12 | `A-EVT-01.source_commit="abc"` | Commit identity shape invalid. |

## Negative vectors that ordinary per-record JSON Schema CANNOT prove

These are expected to pass or remain undecidable at the single-record schema layer and MUST be rejected/decided by a future collection-aware validator or immutable evidence lookup.

| Vector | Collection mutation | Future invariant |
|---|---|---|
| X-N01 | duplicate `A-EVT-04` with same `event_id` | Global `event_id` uniqueness. |
| X-N02 | set `A-EVT-05.source_event_id="NO-SUCH-EVENT"` | Reference target must exist. |
| X-N03 | set `A-EVT-05.bridge_reference_event_ids=["A-EVT-05"]` | No self-reference. |
| X-N04 | point a `causal_parent` edge from Branch A to Branch B solely because topic is similar | Different experiment/task identities do not merge causal lineage. |
| X-N05 | retroactively edit `B-EVT-02` to reference later `A-EVT-04` | Later bridge must not mutate historical event. |
| X-N06 | infer acceptance of `A-EVT-04` from `T-RECEIPT-01` or another receipt | Receipt does not promote semantic artifact acceptance. |
| X-N07 | infer real processing from detector/worker activation attempt evidence | Activation attempt is not real Entity processing. |
| X-N08 | treat `event_claim_verified=true` on `T-ACT-03` as verification of successful activation | Verification is local to current event claim. |
| X-N09 | populate semantic `event_time` from Git commit order without independent event-time rule | Publication time is not domain event time. |
| X-N10 | claim source artifact bytes are proven merely because commit/blob fields have 40-hex shape | Immutable repository readback is required. |
| X-N11 | widen `A-EVT-06.acceptance_scope` from corroboration-only to package execution or production authority | Acceptance scope cannot widen across records. |
| X-N12 | create a synthetic `real_processing_start` from dispatch+inbox+receipt+activation-attempt sequence | A separate evidence event and explicit schema revision are required. |

## Review expectation

A conforming review must report separately:
- structural vectors evaluated by `schema.json`;
- cross-record/evidence vectors reserved for a future validator layer.

Passing structural validation MUST NOT be described as proof that cross-record invariants hold.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать positive/negative schema и cross-record test vectors без реализации validator
СТАТУС: CANDIDATE_FOR_ORG_REVIEW
