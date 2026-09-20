# KOO → OPERATOR: exact one-call OpenAI Entity-booster D0 live decision

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Что готово

SIS verified:
- OpenAI booster live-path preparation PASS;
- durable canonical credential reference PASS;
- exact canonical reference `secretref:openai:wellbeing-entity-boosters-restricted`;
- credential value exposure/read by SIS = 0;
- provider calls = 0.

## Exact task to authorize

Task:
`entities/koordinator/outbox/KOO__openai-booster-d0-live-r01__KOD.md`

task commit:
`b988066e0e018627cc24b95f409f3ccd0a416990`

task blob: `691af722274bc51f87d5eeda6e7054d21ee3c9c3`

Requester binding:
- Entity: `KOD`;
- current writer path: `entities/koder/current/KOD__replacement-current-writer-v04.md`;
- current writer blob: `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

Provider scope:
- provider: `openai`;
- model: `gpt-5.6-luna`;
- data class: `D0_SYNTHETIC`;
- privacy: `synthetic_only`;
- payload: `Synthetic bounded request.`;
- tools: none;
- calls: 1;
- retries: 0;
- fallback: none;
- max output tokens: 64;
- max response bytes: 16384;
- timeout: 30 seconds;
- store: false;
- use-once: true;
- requester review required;
- project_acceptance: `NOT_GRANTED`;
- project-state mutation: false.

Credential reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

## Security caveat

The systemd host credential key is not on encrypted media.
This does not invalidate the current verified binding PASS.
It also must not be interpreted as protection against full-disk or host-key compromise.

## Decision requested

Authorize exactly one execution of the exact task above.

Decision token:
`AUTHORIZE_OPENAI_ENTITY_BOOSTER_D0_LIVE_R01`

## Effect if approved

KOO will address this exact already-prepared task to KOD and provide the manual activation PROMPT.
KOD may perform exactly one provider call under the exact bound scope.
Any task/writer/provider/model/privacy/tools/bounds/secretref/expiry/use-once mismatch must block before transport.

## What approval does NOT authorize

- a second provider call;
- retries;
- provider/model fallback;
- Anthropic;
- other payloads/tools/models;
- credential disclosure;
- billing/account mutation beyond normal cost of the single authorized API call;
- production deployment;
- project acceptance;
- project-state mutation.

## If rejected

No provider call occurs and the prepared task remains non-authorized.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED