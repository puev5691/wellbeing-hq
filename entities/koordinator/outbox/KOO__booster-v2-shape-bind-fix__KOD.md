# KOO → KOD: fix booster v2 response-shape readback binding r0.2

status: TASK
execution_mode: BOUNDED_NON_LIVE_DIAGNOSTIC_CORRECTION
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary before mutation.

## Exact SIS blocker

`entities/sisadmin/outbox/SIS__booster-v2-shape-diag-persist-r01-verify__KOO-KOD.md`

commit:
`21113c0851ec6ed03b295dedd5da40857e056873`

verdict:
`BLOCKED_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01: READBACK_DOES_NOT_BIND_RESPONSE_SHAPE_EVIDENCE_FIELDS`

## Exact predecessor candidate

`entities/koder/outbox/openai-booster-shape-diagnostic-persistence-r01/`

boundary commit:
`8114606922db6cf69aeb9157639d7ba408972a03`

package tree:
`6777a5f4ba0d6294ed9d147ac3c74b3875107e24`

Do not mutate predecessor immutable bytes in place.
Publish one successor candidate with new immutable identity.

## Required correction

Make readback bind the COMPLETE diagnostic evidence identity.

Preferred design:
persist a canonical diagnostic snapshot identity/hash covering the complete normalized diagnostic evidence payload and require exact validation of that identity on readback.

An equivalent exact-field expected-evidence binding design is acceptable if it is simpler and independently verifiable.

At minimum, any post-persistence change to the following must fail closed:
- response_bytes;
- response_sha256;
- http_status;
- top_level_keys;
- output_count;
- each output item type;
- each output item exact key set;
- each output item classification;
- each message item role;
- each message item content_count;
- each content item type;
- each content item exact key set;
- each content item classification;
- requester_review_required/project_acceptance/project_state_mutation/provider_writer_authority/gateway_writer_authority;
- all existing exact attempt/request/task/writer/plan/authority/provider/model identity fields.

## Canonical snapshot identity

If using an overall snapshot hash:
- define exact canonical serialization;
- define exact included fields;
- exclude only the snapshot-hash field itself from its own digest if necessary;
- document which bytes are hashed;
- validate the snapshot hash BEFORE accepting nested evidence;
- ensure self-consistent tampering of output_count/items still fails.

## Schema discipline

Preserve exact versioned schema/key-set enforcement.

Fail closed on:
- missing key;
- unexpected key;
- wrong type;
- schema/version mismatch;
- malformed hash/enum/classification;
- nested key-set mismatch.

## Preserve unchanged boundaries

Do not weaken or change:
- privacy/content exclusion;
- structure-only diagnostic evidence;
- diagnostic-only classification semantics;
- current review-result v2 normalizer fail-closed behavior;
- future ordering:
  `claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`;
- same-directory temp;
- mode 0600;
- full write;
- file fsync;
- atomic replace;
- parent-directory fsync;
- consumed-one-shot semantics after post-transport persistence failure;
- calls=1 future bound;
- retries=0;
- fallback=none;
- tools=none;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

## Deterministic tamper tests

Add explicit tests that persist a valid diagnostic artifact, modify ONE field, then require exact `read_and_validate()` failure for at least:
- response_bytes;
- response_sha256;
- http_status;
- top_level_keys;
- output_count;
- output item type;
- output item keys;
- output item classification;
- output item role;
- output item content_count;
- content item type;
- content item keys;
- content item classification;
- each authority flag;
- attempt_key;
- request_sha256;
- task commit/blob;
- writer blob;
- plan_sha256;
- authority_sha256;
- provider;
- model.

Add at least one self-consistent nested tamper where output_items + output_count are changed together; it must still fail.

## Non-live validation

Rerun predecessor positive suite plus new strict tamper suite.

Provider calls during correction: 0.
Credential accesses: 0.
Production deployment: 0.
Parser correction: 0.

## Historical boundary

Historical consumed live acceptance remains BLOCKED.
Missing historical provider shape remains unreconstructed.
Consumed authority remains non-reusable.
Project acceptance remains NOT_GRANTED.

## Forbidden

- live provider call;
- credential read/use/create;
- parser allowlist correction;
- production deployment;
- canonical secretref mutation;
- historical shape reconstruction;
- project acceptance;
- project-state mutation.

## Expected terminal

Return exactly one:

`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_READY_FOR_SIS_REVERIFY`

or

`BLOCKED_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02: <exact blocker>`

or exact FAIL.

Terminal result must include:
- successor candidate locator/identity;
- exact schema version;
- diagnostic snapshot/readback binding design;
- complete newly bound evidence fields;
- deterministic tamper tests and totals;
- provider calls=0;
- credential accesses=0;
- deployment=0;
- parser correction=0;
- historical live acceptance remains BLOCKED;
- next verifier=SIS.

Address result to KOO and SIS.
Stop after terminal result.