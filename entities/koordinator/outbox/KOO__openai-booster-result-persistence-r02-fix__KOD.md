# KOO → KOD: correct OpenAI booster result-persistence readback identity r0.2

status: TASK
execution_mode: BOUNDED_NON_LIVE_ENGINEERING_CORRECTION
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary before mutation.

## Exact SIS blocker basis

`entities/sisadmin/outbox/SIS__openai-booster-result-persistence-r01-independent-verify__KOO-KOD.md`

commit:
`fd312d09bb0ee4a16ed85f7f75d86540e87c9b24`

verdict:
`BLOCKED_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01: READBACK_VALIDATION_DOES_NOT_BIND_RESPONSE_IDENTITY_FIELDS`

Independent reproduction:
- exact immutable candidate verified;
- 14 deterministic tests passed;
- provider calls = 0;
- credential accesses = 0;
- tampered persisted `response_sha256` was accepted by exact `read_and_validate()`.

## Exact candidate to correct

`entities/koder/outbox/openai-booster-result-persistence-r01/`

package commit:
`13243aa2a0cf9bc667248c7f8ae7f8e4872898cd`

package tree:
`29fbc01f07f337c1d2488b6f278fdab0a23099f0`

Do not mutate historical immutable bytes in place.
Publish a successor correction candidate with new immutable identity.

## Required correction

Bind the complete persisted review-result evidence contract on readback.

At minimum `read_and_validate()` / underlying validator must validate:
- `response_bytes`;
- `response_sha256`;
- `http_status`;
- `parser_status`;
- `plan_sha256`;
- `authority_sha256`.

Also preserve/validate existing bindings for:
- attempt key;
- request identity;
- task commit/blob;
- writer blob;
- provider;
- model;
- review payload bytes/SHA-256;
- requester_review_required;
- project_acceptance;
- project_state_mutation;
- provider_writer_authority;
- gateway_writer_authority.

## Schema discipline

Prefer exact allowed schema/key-set enforcement for the persisted review-result record.

Requirements:
- missing required key -> BLOCK;
- unexpected extra key -> BLOCK unless explicitly versioned/allowed;
- wrong type -> BLOCK;
- malformed identity/hash/enum/status -> BLOCK;
- schema/version mismatch -> BLOCK.

Do not silently ignore unknown persisted evidence fields.

## Cross-field consistency

Validate cross-field invariants where applicable:
- `response_bytes` matches exact persisted/normalized source length used for review identity;
- `response_sha256` matches exact persisted/normalized source bytes defined by schema;
- `parser_status` is one exact allowed terminal parser state;
- `http_status` is consistent with accepted successful provider result semantics;
- `plan_sha256` matches exact correlated plan identity;
- `authority_sha256` matches exact correlated authority identity;
- normalized review payload identity matches stored payload.

Document precisely which bytes each hash covers.

## Deterministic tamper tests

Add one deterministic tamper test for EACH bound field at minimum:
- response_bytes;
- response_sha256;
- http_status;
- parser_status;
- plan_sha256;
- authority_sha256.

Also add tests for:
- missing required key;
- unexpected extra key;
- wrong type;
- schema/version mismatch;
- review payload tamper;
- task/writer/provider/model correlation tamper.

Every tamper must make exact readback validation fail closed.

## Preserve existing persistence semantics

Do not weaken:
- same-directory temp file;
- mode 0600;
- complete write loop;
- file fsync;
- atomic replace;
- parent-directory fsync;
- readback identity validation;
- consumed-one-shot remains consumed after post-transport persistence failure;
- no retry/replay to reconstruct missing result.

## Boundaries

Provider calls during correction: 0.
Credential accesses: 0.
Credential creates: 0.
Production deployment: 0.
Canonical secretref mutation: 0.
Project acceptance: NOT_GRANTED.
Project-state mutation: false.

Historical R03 requester review remains:
`BLOCKED`.

Historical R03 project acceptance remains:
`NOT_GRANTED`.

Do not reconstruct historical provider body.

## Expected terminal result

Return exactly one:

`PASS_KOD_OPENAI_BOOSTER_RESULT_PERSISTENCE_R02_READY_FOR_SIS_REVERIFY`

or

`BLOCKED_KOD_OPENAI_BOOSTER_RESULT_PERSISTENCE_R02: <exact blocker>`

or exact FAIL.

Terminal result must include:
- successor candidate locator/identity;
- exact schema/key-set rules;
- all newly bound readback fields;
- per-field tamper tests/results;
- total deterministic tests;
- provider calls = 0;
- credential accesses = 0;
- historical R03 requester review remains BLOCKED;
- project_acceptance remains NOT_GRANTED;
- next verifier = SIS.

Address result to KOO and SIS.
Stop after terminal result.