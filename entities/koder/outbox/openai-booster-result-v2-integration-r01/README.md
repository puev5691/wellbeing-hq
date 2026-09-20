# OpenAI booster result-v2 runtime integration r0.1

Статус: bounded non-live, non-production candidate.

## Назначение

Встраивает independently verified review-result persistence/readback v2 в существующий verified OpenAI booster live-child/live-worker путь.

Future runtime flow:

`durable claim → credential resolve → provider transport → normalize → persist schema v2 → strict readback → terminal technical PASS`.

Terminal PASS до durable persistence и strict readback невозможен.

## Reused verified components

Result persistence/readback v2:
- package `entities/koder/outbox/openai-booster-result-persistence-r02/`;
- boundary commit `b76e385c139a1b2b0ccdf2ff6481aa1062c161a1`;
- tree `6fcc2f0325256aab96a9c52c913d53875606070f`;
- SIS PASS `a9b2c084b7e747e66336ff35ed06fcd4f9c76016`.

Exact reused files:
- `review_result_store.py` blob `1f216d9625095d817e4cafb8eea8dacb7cb4b9af`;
- `reviewable_live_worker.py` blob `604f73453ad78fdbc933b1ff7399d5e8c5a0da91`;
- inherited v2 test blob `667be662fe06caf82361c22adad7c5abe32ed368`.

Final one-shot live-worker:
- commit `716637bb0e18319fa8f3151253ed5c71b8c1aad7`;
- tree `2737ae65789e6608ad71631e074cc67602a182ab`;
- blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`;
- SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`;
- SIS PASS `18af0b778d5b30f15c20da989a39006f503dcff3`.

SIS live-child basis:
`PASS_SIS_OPENAI_BOOSTER_LIVE_CHILD_PATH_R01_READY`
commit `5723ef15ecd76f2c5a0c401d262619c634015c96`.

No competing provider/gateway stack is introduced.

## Future runtime contract

Exact future D0 scope remains:
- provider=openai;
- endpoint=https://api.openai.com/v1/responses;
- model=gpt-5.6-luna;
- data class D0_SYNTHETIC;
- privacy synthetic_only;
- tools none;
- calls 1;
- retries 0;
- fallback none;
- max output tokens 64;
- max response bytes 16384;
- timeout 30 s;
- use-once;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

The runner accepts the existing exact invocation contract and constructs the same one-shot WorkerPlan.

## Result path

Candidate runtime result directory:

`/var/lib/wellbeing/openai-booster-live-child-r01/review-results`

This stays under the existing live-child state boundary:

`/var/lib/wellbeing/openai-booster-live-child-r01`.

The candidate systemd unit keeps:
`ReadWritePaths=/var/lib/wellbeing/openai-booster-live-child-r01`.

Individual review artifacts are created mode 0600 by the verified v2 persistence layer.

## Credential boundary

The candidate preserves the existing:
- canonical secretref `secretref:openai:wellbeing-entity-boosters-restricted`;
- systemd `LoadCredentialEncrypted`;
- exact encrypted object;
- no legacy TTY path.

The review artifact contains no credential value, Authorization header, environment value, cookie/token or secretref locator.

## Terminal semantics

Successful future LIVE execution returns:
`PASS_TECHNICAL_RESULT_AFTER_DURABLE_V2_READBACK`

only after:
1. live-worker returned one bounded provider reply;
2. provider response normalized into schema v2 evidence;
3. artifact persisted atomically/durably;
4. strict v2 readback succeeded with exact attempt/request/task/writer/plan/authority/provider/model bindings.

If transport occurred but persistence/readback fails:
- terminal is BLOCKED/FAIL;
- one-shot remains consumed;
- retry/replay/new provider call is not authorized;
- requester-review success is not fabricated.

## Candidate unit

`wellbeing-openai-booster-result-v2.service.candidate`

It is documentation/config candidate only and was not installed.

It preserves:
- User/Group pev5691;
- exact LoadCredentialEncrypted object;
- AF_UNIX/AF_INET/AF_INET6;
- existing state write scope;
- system hardening;
- one-shot service behavior.

## Historical R03

Unchanged:
- technical correlation PASS;
- requester review BLOCKED;
- project_acceptance NOT_GRANTED;
- missing body not reconstructed.

This integration does not reinterpret the historical R03 execution.
