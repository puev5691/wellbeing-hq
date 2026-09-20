# OpenAI Entity booster live-path preparation r0.1

Статус: non-live live-capable candidate.

## Что подготовлено

Candidate связывает independently verified Entity booster runtime r0.2 и independently verified final live-worker с отдельным explicit use-once OpenAI live authority contract.

Целевая цепочка:

`Entity booster authority → live execution gate → verified live-worker → OpenAI /v1/responses → bounded result → requesting Entity review`.

Никакого второго gateway/orchestrator не создано.

## Exact reused basis

Entity booster runtime r0.2:
- independent SIS PASS: `b0b858d18ef518fa336d3eea9441b392922697c3`;
- package commit: `4ac08228960c2bbb8aa00bf607a0f0bdb13485f3`;
- package tree: `9f0c6f660fa9a1628e526246bb0b108f4c3c27d3`;
- runtime blob: `1fb1ffc49f82e473e523709118e49b0603366fb4`;
- runtime SHA-256: `c0b64fd44879c6c2395c02f66ee79c641a36c768372513ed35d149289ff2d941`.

Final live-worker:
- independent SIS PASS: `18af0b778d5b30f15c20da989a39006f503dcff3`;
- package commit: `716637bb0e18319fa8f3151253ed5c71b8c1aad7`;
- package tree: `2737ae65789e6608ad71631e074cc67602a182ab`;
- runtime blob: `d276de1050fd54e836ed4fc879eb384dba3aa1f1`;
- runtime SHA-256: `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`.

OpenAI readiness:
- dedicated project/account/prepaid + restricted credential provisioned outside project artifacts: `04a9633d7657afcf37f2ea9b4fb936ae1789e88f`;
- Luna/Terra/Sol/Astra entitlement matrix PASS: `4744028f96d6453abaf4a7987a6328ad43b619d8`.

These records prove readiness facts, not authority for this task to perform a live call.

## Live authority contract

`LiveAuthority` binds:
- Entity;
- exact task commit;
- exact writer blob;
- provider = `openai`;
- exact model;
- privacy class;
- data class = `D0_SYNTHETIC`;
- tools = none;
- one call;
- retries = 0;
- fallback = none;
- max output tokens;
- max response bytes;
- hard timeout;
- use-once;
- valid-until tick;
- restricted credential reference identifier.

Credential value is never part of the contract.

Any mismatch blocks in `prepare()` before worker invocation, credential resolution or transport.

## Credential boundary

This package contains no real credential and does not read one.

The candidate accepts only a reference matching:

`secretref:openai:<identifier>`

The exact project credential reference identifier is not asserted by this package because HQ evidence records that the credential was provisioned outside project artifacts but does not expose an exact reference locator. A future live authority must supply a separately verified reference identifier without exposing the value.

Tests use only a synthetic resolver value and sentinel client.

## Worker boundary

Prepared plan is converted to the already verified `WorkerPlan`.

The reused live-worker enforces:
- durable one-shot ledger;
- exactly-one claimant;
- credential resolution after ledger claim;
- max calls = 1;
- automatic retries = 0;
- hard timeout;
- bounded response;
- redirect fail-closed;
- exact OpenAI `/v1/responses` binding.

The candidate itself does not instantiate `BoundedUrllibClient` in tests and performs no live network operation.

## Result boundary

Sentinel result preserves:
- `project_acceptance=NOT_GRANTED`;
- `review_required=true`;
- no gateway/provider writer authority;
- no project-state application;
- no external dispatch.

Technical completion is not substantive acceptance.

## Future D0 profile

See `FUTURE-D0-PROFILE.json`.

Luna is selected because fresh HQ evidence confirms entitlement and it is the smallest already-proven OpenAI option for the first bounded D0 path. This preparation does not authorize execution.

## Hard boundary

No live provider call, credential read/use/create, billing/account mutation, production deployment, automation, Project Sources change or project acceptance occurs in this candidate.
