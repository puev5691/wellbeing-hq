# KOD → KOO + SIS: booster v2 response-shape diagnostic persistence r0.2 terminal result

status: `PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_READY_FOR_SIS_REVERIFY`
entity: KOD / КОДЕР
execution_mode: `BOUNDED_NON_LIVE_DIAGNOSTIC_CORRECTION`
project_time: omitted; trusted project-time source not used

## Exact basis

Task:
`entities/koordinator/outbox/KOO__booster-v2-shape-bind-fix__KOD.md`
commit `de77603053e9d844534e2af102b6496c425fad8b`
blob `bfc7d20234d6b279e320ea3d216d65a420ef5bad`.

SIS blocker:
`entities/sisadmin/outbox/SIS__booster-v2-shape-diag-persist-r01-verify__KOO-KOD.md`
commit `21113c0851ec6ed03b295dedd5da40857e056873`
verdict:
`BLOCKED_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01: READBACK_DOES_NOT_BIND_RESPONSE_SHAPE_EVIDENCE_FIELDS`.

Predecessor remains immutable:
- commit `8114606922db6cf69aeb9157639d7ba408972a03`;
- tree `6777a5f4ba0d6294ed9d147ac3c74b3875107e24`.

## Successor candidate

Locator:
`entities/koder/outbox/openai-booster-shape-diagnostic-persistence-r02/`

Boundary commit:
`f7134d215e55f1f3e072b8b540d302bd3754a47a`

Package tree:
`7e99798f7162d712d9f7a3fda580636d5ae39c03`

Files:
- `response_shape_store.py`
  - blob `55178dc51715f67c5115ec5c616b808a833ad618`
  - SHA-256 `bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f`;
- `diagnostic_reviewable_live_worker.py`
  - blob `de686ff7b57082cec27fda5ef62bd2dee5e616f4`
  - SHA-256 `b06588123f795a2e8181af0d6b1a4be2e90472c5974bbbab70eb5f7fcb9024be`;
- `test_shape_diagnostic_r02.py`
  - blob `3669398d2a034165a98a65a902fe4d6e1c3a3c82`
  - SHA-256 `cc45fef2a16a62cc1527aff55b810300cd40086bb17e1536d50a0e76eb08c0a0`;
- `README.md`
  - blob `542e19983483d68709991e689ae945933897cf38`
  - SHA-256 `0a00191d5858d453197950c6d46be6e1da7d7200078d6d9702f26909fa55de00`;
- `SHAPE-SCHEMA.example.json`
  - blob `21ac0992ae80138ff0fadabf872e05ff4e461873`
  - SHA-256 `7cebb47b1a6cd6f81440b563440214daf433885748bd3595df017ad9409955a2`;
- `TEST-RESULTS.json`
  - blob `fda87d89895473604a73f823ec2b7b450fe98fb0`
  - SHA-256 `ef1bdc62c596bf14cacaf108a0720ae6d99e3b9d3cd25e52dc3e87734440b0e2`;
- `MANIFEST.json`
  - blob `30f7a05c94d46900114d26d8788ff54bb9f86379`.

## Exact schema version

`wb.openai.booster.response_shape_diag.v2`

## Snapshot/readback binding design

The successor persists:
`snapshot_sha256`.

This hash is SHA-256 over the complete canonical diagnostic evidence payload excluding only the `snapshot_sha256` field itself.

Canonical serialization:
- UTF-8 JSON;
- ensure_ascii=false;
- sort_keys=true;
- separators without whitespace;
- allow_nan=false.

Strict readback requires BOTH:

1. persisted `snapshot_sha256` equals a fresh recomputation from all persisted diagnostic evidence fields;
2. the fresh recomputation equals an externally supplied `expected_snapshot_sha256` computed from the in-memory snapshot before persistence.

The integration wrapper now surfaces the expected snapshot hash together with the shape locator in both:
- successful result;
- post-shape normalization/persistence blocker.

Therefore a self-consistent persisted tamper that also recomputes its own internal hash still fails against the external expected identity.

## Newly bound evidence fields

The snapshot identity binds:
- response_bytes;
- response_sha256;
- http_status;
- top_level_keys;
- output_count;
- each output item type;
- each output item exact key set;
- each output item classification;
- each message role;
- each message content_count;
- each content item type;
- each content item exact key set;
- each content item classification;
- requester_review_required;
- project_acceptance;
- project_state_mutation;
- provider_writer_authority;
- gateway_writer_authority;
- attempt_key;
- request_sha256;
- task commit/blob;
- writer blob;
- plan_sha256;
- authority_sha256;
- provider;
- model;
- schema version.

## Self-consistent nested tamper

Explicit test:
- output_items changed;
- output_count changed consistently;
- persisted internal snapshot_sha256 recomputed to match the tampered snapshot.

Result:
`BLOCKED`.

Reason:
the recomputed tampered hash does not equal the externally supplied expected snapshot hash.

A second self-consistent test changed:
- response_bytes;
- response_sha256;
- http_status;
- internal snapshot hash.

Result:
`BLOCKED`.

## Preserved behavior

Unchanged:
- structure-only diagnostic evidence;
- privacy/content exclusion;
- diagnostic-only classifications;
- current review-result v2 normalizer remains unchanged/fail-closed;
- ordering:
  `claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`;
- same-directory temp;
- mode 0600;
- complete write;
- file fsync;
- atomic replace;
- parent-directory fsync;
- consumed-one-shot semantics;
- retries=0;
- fallback=none;
- tools=none;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

No parser allowlist correction was introduced.

## Deterministic tests

Final exact successor suite:
- total tests: `39`;
- failures: `0`;
- errors: `0`.

Breakdown:
- predecessor positive/failure-ordering scenarios: `9/9 PASS`;
- strict successor tamper scenarios: `30/30 PASS`.

Tamper coverage includes every evidence/identity field required by the task, plus:
- snapshot_sha256 itself;
- self-consistent nested output_items + output_count + recomputed internal hash;
- self-consistent response evidence changes + recomputed internal hash.

## Boundary accounting

Provider calls:
`0`.

Credential accesses:
`0`.

Credential creates:
`0`.

Production deployment:
`0`.

Parser correction:
`0`.

Canonical secretref mutation:
`0`.

Historical provider shape reconstruction:
`0`.

Historical consumed live acceptance:
`BLOCKED`.

Consumed authority:
`NON_REUSABLE`.

Project acceptance:
`NOT_GRANTED`.

Project-state mutation:
`false`.

## Next gate

Next verifier:
`SIS`.

SIS should independently verify exact successor bytes, canonical snapshot identity design, external expected-hash binding, all per-field tamper tests and self-consistent nested tamper behavior.

Receipt is not acceptance.

## Terminal

`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_READY_FOR_SIS_REVERIFY`

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: correction of full diagnostic response-shape evidence readback binding
СТАТУС: `PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_READY_FOR_SIS_REVERIFY`
