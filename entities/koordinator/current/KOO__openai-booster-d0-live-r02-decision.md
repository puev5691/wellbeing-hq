# OPERATOR decision — fresh one-shot OpenAI Entity-booster D0 live authority r0.2

status: OPERATOR_DECISION_RECORDED
decision: AUTHORIZE_OPENAI_ENTITY_BOOSTER_D0_LIVE_R02
project_time: omitted; trusted project-time source not used

## Exact authorized task identity

path: `entities/koordinator/outbox/KOO__openai-booster-d0-live-r01__KOD.md`
commit: `b988066e0e018627cc24b95f409f3ccd0a416990`
blob: `691af722274bc51f87d5eeda6e7054d21ee3c9c3`

## Exact requester/current-writer binding

entity: `KOD`
current_writer_path: `entities/koder/current/KOD__replacement-current-writer-v04.md`
current_writer_blob: `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

## Fresh resolver basis

SIS terminal:
`PASS_SIS_OPENAI_CANONICAL_SECRETREF_RESOLVER_PATH_R01_READY`

Canonical reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

Executable resolver path is the SIS-verified canonical systemd path.
No fallback to legacy TTY injection is authorized.

## Scope

All provider/model/request/privacy/tools/bounds/use-once parameters are inherited only from the exact immutable task bytes.

Maximum provider calls: 1.
Automatic retries: 0.
Fallback: none.
Requester review remains required.
Project acceptance remains NOT_GRANTED.
Project-state mutation remains forbidden.

## Fresh one-shot validity

This authority is separate from all previous live authorities.
It is valid for one manual activation session only.
Runtime expiry must be local monotonic activation-start + 600 seconds.

It expires immediately on the earliest of:
- first durable one-shot claim;
- expiry window reached;
- task identity mismatch;
- current-writer mismatch;
- canonical reference/resolver metadata mismatch;
- explicit revoke or supersession.

No retry or second claim is authorized after any claimed or uncertain attempt.

## Security caveat

The systemd host credential key is not located on encrypted media.
This does not invalidate the current verified resolver/binding PASS.
No protection against full-disk or host-key compromise is claimed.

## Boundaries

No production deployment.
No project acceptance.
No project-state mutation.
Only normal provider-side consumption caused by the single exact authorized call is permitted.