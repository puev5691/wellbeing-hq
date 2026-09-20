# OPERATOR decision — authorize one bounded OpenAI Entity-booster D0 live call r0.1

status: OPERATOR_DECISION_RECORDED
decision: AUTHORIZE_OPENAI_ENTITY_BOOSTER_D0_LIVE_R01
project_time: omitted; trusted project-time source not used

## Exact authorized task identity

path: `entities/koordinator/outbox/KOO__openai-booster-d0-live-r01__KOD.md`
commit: `b988066e0e018627cc24b95f409f3ccd0a416990`
blob: `691af722274bc51f87d5eeda6e7054d21ee3c9c3`

All provider/model/request/bounds/reference/security parameters are inherited ONLY from these exact immutable task bytes.

## Exact requester writer binding

entity: `KOD`
writer_blob: `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

## One-shot validity

Maximum provider calls: 1.
Automatic retries: 0.
Fallback: none.
Authority is valid for one manual activation session only.
Runtime expiry must be local monotonic activation-start + 600 seconds.

Authority expires immediately on the earliest of:
- first durable one-shot claim;
- expiry window reached;
- exact task identity mismatch;
- current-writer mismatch;
- exact reference metadata mismatch;
- explicit revoke or supersession.

No retry or second claim is authorized after a claimed or uncertain live attempt.

## Security caveat

The verified host binding has a known storage-hardening caveat documented in the SIS PASS.
This decision does not claim protection against full-disk or host-key compromise.

## Boundaries

No production deployment.
No project acceptance.
No project-state mutation.
Requester review remains required after the technical result.
Only normal provider-side consumption caused by the single exact authorized call is permitted.