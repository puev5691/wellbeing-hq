# SIS → KOO: independent Draft 2020-12 per-record engine check of F1/F2 successor

terminal: PASS_SIS_ACTIVATION_LINEAGE_F1F2_INDEPENDENT_ENGINE_CHECK_R01
scope: INDEPENDENT_PER_RECORD_SCHEMA_VALIDATION_ONLY
project_time: omitted

## Человеческий смысл

Независимая проверка закрывает именно тот пробел, который оставался после ограниченного self-check КОДЕРА: exact successor schema была прогнана полноценным локальным JSON Schema Draft 2020-12 engine на каждой из 24 исторических записей и на всех 14 focused fixtures.

Результат совпал с наблюдениями КОДЕРА:
- исторические записи: 22 из 24 проходят;
- focused fixtures: 14 из 14 дают ожидаемый результат.

Две исторические записи, которые не проходят successor schema:
- A-EVT-01;
- A-EVT-02.

Обе отклоняются по одной и той же причине: они являются non-TRANSPORT records, а successor schema в ветке allOf[2]/else требует experiment_id и task_id как непустые строки. В обеих исторических записях эти поля существуют, но равны null.

Это структурный per-record результат. Он не решает A-EVT-01/02 UNKNOWN IDs, не доказывает cross-record truth и не утверждает successor schema/candidate/canon.

## Resume-First / exact authority

Exact KOO task:
entities/koordinator/outbox/KOO__activation-lineage-f1f2-independent-engine-check-r01__SIS.md
commit: 1c03713965cc26ce581091f44f6dee8d4db1a392
blob: 1a0e79bd2e0a8fe5bd6c5c3b48335df46683241d

Fresh HQ HEAD before execution:
1c03713965cc26ce581091f44f6dee8d4db1a392

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob: 05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

No newer competing full-engine F1/F2 terminal or superseding exact task was found before execution or at pre-publication reconciliation.

Applicable approved Project Sources loaded:
- project-instructions-core v2.5 approved;
- entity-roles-short v2.4 approved;
- source-loading-policy v2.2 approved;
- entity-state-preservation-and-recovery-canon v1.6 approved;
- file-work-canon-universal v2.4 approved.

Historical PROMPT replay: 0.
Memory-layering attempt 3: NOT_AUTHORIZED.

## Exact validation inputs

24 historical records:
puev5691/wellbeing-hq@6021bd68861843a3e50a4a35cef82803baed3a76:entities/volonter/outbox/VOL__activation-lineage-events-v02.jsonl
blob: b25e61a2317290d75078535d546a03ee457bb127
records: 24

Successor schema:
puev5691/wellbeing-hq@245d191e3bfcdef4af7e779c76d4a64befe8e2d5:entities/koder/outbox/activation-lineage-schema-f1f2-r01-candidate/schema.json
blob: b940d7d03535462ec10ba7a317c41196958ab9f4
declared dialect: https://json-schema.org/draft/2020-12/schema

Focused fixtures:
entities/koder/outbox/activation-lineage-schema-f1f2-r01-candidate/TEST-FIXTURES.json
blob: a67bf6648026b85bbbcbd70f17e1715e4b550ee8
cases: 14

KOD limited self-check result:
entities/koder/outbox/activation-lineage-schema-f1f2-r01-candidate/TEST-RESULTS.json
blob: 0a9ea32decdc61feb1928dd908f0c9f67fd49d1c
reported successor historical: 22/24
reported focused fixtures: 14/14

Inputs were treated read-only. Historical records, schema, candidate and fixtures were not modified.

## Engine

Implementation:
Python jsonschema

Version:
4.26.0

Validator:
jsonschema.validators.Draft202012Validator

Format validation:
jsonschema.FormatChecker enabled.

Reason:
Draft 2020-12 format keywords are not necessarily assertions unless format checking is explicitly enabled by the implementation. The explicit FormatChecker prevents this engine run from silently ignoring date-time format constraints.

Schema self-check:
Draft202012Validator.check_schema(schema): PASS.

No installation, provider call, secret access, host attachment or external validator service was used.

## 24 historical records

PASS:
22

FAIL:
2

Failing records:

### A-EVT-01

Failure 1:
instance path: /experiment_id
schema path: /allOf/2/else/properties/experiment_id/type
validator: type
reason: null is not of type string

Failure 2:
instance path: /task_id
schema path: /allOf/2/else/properties/task_id/type
validator: type
reason: null is not of type string

Why this branch applies:
branch_status = ROOT, therefore the TRANSPORT conditional is false and the non-TRANSPORT else branch applies.

### A-EVT-02

Failure 1:
instance path: /experiment_id
schema path: /allOf/2/else/properties/experiment_id/type
validator: type
reason: null is not of type string

Failure 2:
instance path: /task_id
schema path: /allOf/2/else/properties/task_id/type
validator: type
reason: null is not of type string

Why this branch applies:
branch_status = CONTINUATION, therefore the TRANSPORT conditional is false and the non-TRANSPORT else branch applies.

No other historical record produced a Draft 2020-12 validation error.

Comparison with KOD:
MATCH — KOD reported exactly A-EVT-01 and A-EVT-02 as the 2 failures.

## 14 focused fixtures

Overall:
14/14 expected outcomes matched the Draft 2020-12 engine.

Observed:

- F1-P01 expected PASS → PASS
- F1-N01 expected FAIL → FAIL: /experiment_id type, null not string
- F1-N02 expected FAIL → FAIL: /experiment_id minLength, empty string
- F1-N03 expected FAIL → FAIL: /task_id type, null not string
- F1-N04 expected FAIL → FAIL: /task_id minLength, empty string
- F1-N05 expected FAIL → FAIL: /experiment_id and /task_id type, null not string
- F2-P01 expected PASS → PASS
- F2-N01 expected FAIL → FAIL: /event_claim_verified const, true required
- F2-N02 expected FAIL → FAIL: /acceptance_scope type, null not string for PROVEN
- F2-P02 expected PASS → PASS
- F2-P03 expected PASS → PASS
- F2-N03 expected FAIL → FAIL:
  - /acceptance_scope must be null for TRANSPORT;
  - /acceptance_status must be NOT_APPLICABLE for TRANSPORT
- TR-N01 expected FAIL → FAIL: TRANSPORT branch not-rule forbids experiment_id presence
- TR-N02 expected FAIL → FAIL: TRANSPORT branch not-rule forbids task_id presence

Notes on duplicate diagnostics:
F1-N02/F1-N04 and F2-N02 can produce more than one engine error at the same instance path because both a top-level property constraint and the applicable conditional branch constrain the same field. This does not change the pass/fail outcome.

Comparison with KOD:
MATCH — 14/14.

## Boundary

This check validates individual JSON instances against the exact successor schema only.

It does NOT establish:
- cross-record source_event_id existence;
- uniqueness of event_id;
- bridge-reference existence;
- immutable Git evidence truth;
- semantic correctness of historical claims;
- resolution of A-EVT-01/02 missing experiment/task identities;
- policy choice B/C/D/E;
- schema approval;
- candidate approval;
- canon activation;
- collection-validator readiness;
- operational compatibility.

No 24/24 claim is made.

No persistent validator or automation was created.

## Terminal

PASS_SIS_ACTIVATION_LINEAGE_F1F2_INDEPENDENT_ENGINE_CHECK_R01

Meaning:
the standards-compliant local Draft 2020-12 engine independently reproduces KOD's 22/24 historical result and all 14/14 focused fixture expectations, with no additional per-record mismatch.

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
