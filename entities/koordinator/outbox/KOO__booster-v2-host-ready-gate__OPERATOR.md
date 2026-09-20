# KOO → OPERATOR: authorize bounded booster v2 host installation/readiness r0.1

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Verified basis

SIS terminal:
`PASS_SIS_BOOSTER_RESULT_V2_INTEGRATION_R01_VERIFY`

commit:
`8b849b3ec1c0cd3d754539c16eb8f51b474ea8be`

Verified candidate:
`entities/koder/outbox/openai-booster-result-v2-integration-r01/`

boundary commit:
`b0779b4215de43ca96888df94835e97e3e15402e`

package tree:
`600f4ba691152db74dc5818c85dc822bba000bc3`

Current state:
- candidate technically verified;
- provider calls during verification = 0;
- credential accesses = 0;
- production deployment = 0;
- candidate unit not installed;
- candidate unit not enabled;
- project_acceptance = NOT_GRANTED.

## Next causal step

Authorize SIS to perform one bounded host installation/readiness step on `ruvds-xnqc6`.

Purpose:
install the exact verified candidate unit/runtime bytes in a non-live, disabled state and independently verify host-level readiness without provider transport.

## Exact allowed actions

SIS may:
- install the exact verified integration candidate bytes to the bounded host runtime location;
- install/register the exact candidate systemd unit;
- keep the unit disabled;
- preserve exact canonical `LoadCredentialEncrypted` mapping and secretref identity;
- create the bounded review-result directory if required;
- verify ownership/modes/write scope/systemd parsing/unit identity;
- run a non-live sentinel/dry verification path only if it provably cannot perform provider transport;
- verify ordinary KOD-triggered invocation boundary if that can be done without live transport;
- verify no legacy TTY path and no scope expansion;
- record exact installed byte identities.

## Explicitly forbidden

- any OpenAI/provider call;
- credential value read/use/exposure;
- enabling persistent/automatic execution;
- starting live mode;
- changing canonical secretref/object identity;
- retries/fallback expansion;
- production acceptance;
- project acceptance;
- project-state mutation outside exact bounded installation/readiness state;
- any second deployment target.

## Required terminal boundary

Provider calls = 0.
Credential value reads/exposure = 0.
Candidate unit remains disabled.
No live provider authority is created.
Project acceptance remains NOT_GRANTED.

## Security caveat

The systemd host credential key remains not located on encrypted media.
No full-disk or host-key compromise protection is claimed.

## Decision requested

`AUTHORIZE_BOOSTER_V2_HOST_INSTALL_READINESS_R01`

## If approved

KOO will create and address one exact SIS task for bounded non-live installation/readiness verification.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED