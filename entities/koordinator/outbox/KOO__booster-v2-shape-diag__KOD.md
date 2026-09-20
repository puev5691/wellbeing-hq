# KOO → KOD: diagnose booster v2 unexpected provider output r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_DIAGNOSIS_AND_CORRECTION_PREP
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary.

## Exact blocker

`entities/koder/outbox/KOD__booster-v2-live-acceptance-r01-blocker__KOO.md`

commit:
`87d70caf4d2f942a3a908b3f90155bf34d30f670`

blob:
`bd7746bb14fe13589b6ceba1b66f945d1dbf0b42`

terminal:
`BLOCKED_KOD_BOOSTER_V2_LIVE_ACCEPTANCE_R01: BLOCKED_REVIEW_RESULT_PERSISTENCE:BLOCKED_UNEXPECTED_PROVIDER_ACTION`

## Established facts

- provider=openai;
- model=gpt-5.6-luna;
- provider calls=1;
- HTTP 200;
- durable claim=consumed;
- retries=0;
- fallback=none;
- acceptance authority consumed/non-reusable;
- schema-v2 artifact absent;
- strict readback not reached;
- project_acceptance=NOT_GRANTED;
- project-state mutation=false.

## Exact parser behavior

Current verified v2 normalizer only accepts provider `output[]` items shaped as assistant `message` with `output_text` content.
Any other output item/action fails closed with `BLOCKED_UNEXPECTED_PROVIDER_ACTION`.

## Goal

Determine from existing local runtime/host evidence exactly which provider response output/action shape caused the blocker, without any new provider call.

If exact evidence is sufficient, prepare one minimal non-live parser-contract correction candidate.
If exact evidence is insufficient to identify the provider item safely, stop with an exact blocker and do not guess.

## Required diagnosis

Inspect only already existing evidence associated with exact attempt:
`222cae224dee9b9bdce7e661433734294085c968a7c5923fdd9d5af9f0911818`

Use, as available:
- systemd journal for exact unit/attempt;
- bounded runtime diagnostics;
- existing invocation/ledger/result metadata;
- installed runtime code;
- any already persisted provider-response diagnostic evidence;
- GitHub terminal artifacts.

Do not access credentials.
Do not call OpenAI.

Establish, if evidence supports it:
- exact `output[]` item type(s);
- exact item key shape relevant to parser compatibility;
- whether assistant `message/output_text` also existed;
- whether the extra item is semantically non-action metadata (for example provider reasoning metadata) or an actual tool/action/output that must remain rejected;
- whether safely ignoring/excluding that exact item for requester-review normalization preserves the no-tools/no-actions contract.

Do not infer an item type merely from common OpenAI API behavior.

## Correction rule

A correction candidate is allowed only if exact local evidence proves the extra item can be excluded from review normalization without:
- hiding an actual tool/action;
- changing provider/model/task semantics;
- weakening tools=none;
- weakening fail-closed handling of unknown future item types;
- changing one-shot/retry/fallback boundaries.

If corrected, use an explicit allowlist for the exact observed benign item type(s).
Unknown item types must remain fail-closed.

## Deterministic tests if correction is possible

Add tests proving:
- exact observed benign item + assistant message normalizes successfully;
- assistant review text is preserved exactly;
- observed benign item is not treated as review text;
- tool/action items still fail closed;
- unknown item types still fail closed;
- message/output_text-only response still passes;
- schema-v2 persistence/readback/tamper protections remain intact;
- provider calls=0;
- credential accesses=0.

## Historical/authority boundary

The consumed live acceptance attempt remains BLOCKED.
Do not retroactively create a review artifact for it unless exact provider body already exists and current authority/process explicitly permits deterministic local normalization from preserved evidence; otherwise do not reconstruct it.

Fresh live acceptance authority is consumed and non-reusable.
No retry/replay/new provider call is authorized.

## Forbidden

- provider call;
- retry;
- replay against provider;
- credential read/use;
- guessing response shape;
- production deployment;
- project acceptance;
- project-state mutation;
- weakening unknown-action fail-closed behavior.

## Expected terminal

Return exactly one:

`PASS_KOD_BOOSTER_V2_PROVIDER_SHAPE_DIAG_R01_READY_FOR_SIS_VERIFY`

or

`BLOCKED_KOD_BOOSTER_V2_PROVIDER_SHAPE_DIAG_R01: <exact blocker>`

or exact FAIL.

If PASS, include:
- exact evidence source for observed provider item shape;
- exact observed item type/key shape;
- correction candidate locator/identity;
- explicit allowlist behavior;
- deterministic test results;
- provider calls=0;
- credential accesses=0;
- next verifier=SIS.

Address terminal result to KOO and SIS.
Stop after terminal result.