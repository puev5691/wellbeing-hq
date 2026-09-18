# KOO current active queue r0.1

## ACTIVE WIP 1 — KOD / boosters

Task:
`entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-r01__KOD.md`

Commit:
`dbe29d49eef74e491ed055e642f1411ff4273bbe`

Goal:
live-worker candidate before first real provider call.

## ACTIVE WIP 2 — RED / public portal

Task:
`entities/koordinator/outbox/KOO__public-info-portal-editorial-review-r01__RED.md`

Commit:
`d95948d979389d61ad9f394fb60f54158996803a`

Goal:
public-facing editorial/public-safe review before static implementation.

## QUEUED NEXT — boosters

After KOD PASS:
SIS independent verify of exact live-worker candidate.

After SIS PASS:
OPERATOR account/credential/model-entitlement gate + exact one-call LIVE_EXECUTION_AUTHORITY + bounded live D0.

## QUEUED NEXT — Telegram facilitator

Accepted:
`PASS_SIS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01`
commit `8d738f6a2eafb84485ab5e11e1961adb60d017ac`.

Next task after a KOD slot is free:
upstream semantic privacy/admission gate for real discussion excerpts → SemanticInput.
No live Telegram ingestion before that gate.

## QUEUED NEXT — public portal

After RED PASS:
KOD deterministic local/static portal build from WEB assembly + RED handoff.

Then:
independent readback/verification before any public-ready decision.

## CLOSED / WAITING EXTERNAL OPERATOR

OpenAI live account gate:
technical runtime ready; waiting exact project/billing/credential/model entitlement and separate one-call authority.

Anthropic live account gate:
adapter technically verified; waiting account/credential/model entitlement and later live authority.

Telegram Phase1B host runtime:
`BLOCKED_PRIVILEGE_REQUIRED` remains infrastructure blocker for exact host runtime.

## POLICY

WIP limit: 2 active profile tasks.
Queued tasks do not start until their dependency and slot are clear.
No historical task replay by inbox presence alone.
