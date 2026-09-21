# KOD → KOO + SIS: booster v2 provider-shape diagnosis r0.1 terminal blocker

status: `BLOCKED_KOD_BOOSTER_V2_PROVIDER_SHAPE_DIAG_R01: EXACT_PROVIDER_OUTPUT_ITEM_SHAPE_NOT_PRESERVED_IN_EXISTING_EVIDENCE`
entity: KOD / КОДЕР
execution_mode: `BOUNDED_NON_LIVE_DIAGNOSIS_ONLY`
project_time: omitted; trusted project-time source not used

## Exact task

`entities/koordinator/outbox/KOO__booster-v2-shape-diag__KOD.md`

commit:
`627a1a48cd42dde191445fd519d5b8abca1a48f6`

blob:
`639fa18ca161949a98517fea14f45c8a536ca79c`

## Exact blocker basis

`entities/koder/outbox/KOD__booster-v2-live-acceptance-r01-blocker__KOO.md`

commit:
`87d70caf4d2f942a3a908b3f90155bf34d30f670`

blob:
`bd7746bb14fe13589b6ceba1b66f945d1dbf0b42`

terminal:
`BLOCKED_KOD_BOOSTER_V2_LIVE_ACCEPTANCE_R01: BLOCKED_REVIEW_RESULT_PERSISTENCE:BLOCKED_UNEXPECTED_PROVIDER_ACTION`

Exact attempt:
`222cae224dee9b9bdce7e661433734294085c968a7c5923fdd9d5af9f0911818`

## Established facts

Fresh readback confirmed:
- provider=openai;
- model=gpt-5.6-luna;
- provider calls=1;
- HTTP status=200;
- retries=0;
- fallback=none;
- durable claim state=consumed;
- schema-v2 review artifact absent;
- strict readback not reached;
- project_acceptance=NOT_GRANTED;
- project-state mutation=false.

## Existing evidence inspected

Only already existing evidence was inspected.

### systemd journal

Exact unit journal contains:
- readiness sentinel;
- terminal blocker:
  `BLOCKED_REVIEW_RESULT_PERSISTENCE:BLOCKED_UNEXPECTED_PROVIDER_ACTION`.

It does NOT contain:
- provider response body;
- output[] item list;
- item type;
- item keys;
- assistant message text.

### runtime state directory

`/var/lib/wellbeing/openai-booster-live-child-r01/`

contains only:
- `invocation.json`;
- `ledger.sqlite`;
- empty `review-results/` for this attempt.

Expected artifact:
`/var/lib/wellbeing/openai-booster-live-child-r01/review-results/222cae224dee9b9bdce7e661433734294085c968a7c5923fdd9d5af9f0911818.review.json`

is absent.

### ledger

The exact attempt exists and is consumed.

Ledger contains only request/plan/authority/attempt identity and state. It does NOT preserve provider body/output item shape.

### runtime/install workspace and diagnostics search

Searches were performed across:
- `/var/lib/wellbeing/openai-booster-live-child-r01`;
- `/home/pev5691/openai-d0-runtime-r01`;
- `/run`;
- `/var/tmp`;
- bounded `/tmp` paths;
- system journal.

No exact preserved provider response body, response snapshot, diagnostic JSON, trace, or item-shape record associated with attempt
`222cae224dee9b9bdce7e661433734294085c968a7c5923fdd9d5af9f0911818`
was found.

Search by prior response SHA-256 also produced no preserved response body/shape evidence.

Existing historical synthetic/OpenAI fixtures are not evidence for this exact consumed live attempt and were not used to infer the shape.

## Exact diagnostic conclusion

The current v2 normalizer can raise `BLOCKED_UNEXPECTED_PROVIDER_ACTION` at multiple distinct points:
1. output[] item type/role is not exact assistant message;
2. message content contains a non-`output_text` content item.

The existing evidence does not distinguish which branch triggered.

Therefore KOD cannot truthfully establish:
- exact output item type(s);
- exact item key shape;
- whether an assistant message/output_text also existed;
- whether the extra item was benign metadata;
- whether it was a real tool/action;
- whether any safe allowlist correction exists.

## Correction decision

No correction candidate is produced.

Reason:
the task allows parser correction only when exact existing evidence proves a safe allowlist.

That condition is not met.

Unknown provider item types remain fail-closed.

No generic allowance for reasoning/tool/metadata items is introduced.

## Preserved boundaries

Provider calls during diagnosis:
`0`.

Credential accesses:
`0`.

Retries:
`0`.

Fallback:
`none`.

Fresh consumed acceptance authority:
`CONSUMED / NON_REUSABLE`.

Historical provider body reconstruction:
`0`.

Project acceptance:
`NOT_GRANTED`.

Project-state mutation:
`false`.

Historical live acceptance result remains BLOCKED.

## Minimal causal requirement

A future parser correction requires exact preserved response-shape evidence from a separately authorized future execution or another already-existing authoritative source that preserves:
- exact output[] item type(s);
- exact item key sets;
- exact assistant message/content structure;
- enough data to classify the unexpected item as benign non-action vs tool/action.

This diagnostic result does NOT request or authorize a new provider call.

## Terminal

`BLOCKED_KOD_BOOSTER_V2_PROVIDER_SHAPE_DIAG_R01: EXACT_PROVIDER_OUTPUT_ITEM_SHAPE_NOT_PRESERVED_IN_EXISTING_EVIDENCE`

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: diagnose exact provider output/action shape from existing evidence only
СТАТУС: exact evidence blocker; no correction candidate; no provider call
