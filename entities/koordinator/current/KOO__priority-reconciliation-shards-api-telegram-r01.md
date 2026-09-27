# KOO current priorities: shards / LLM API / Telegram r0.1

status: CURRENT_PRIORITY_DIRECTION
project_time: omitted

OPERATOR decision:
- pause ПКТБ autonomous governance/source package review/activation;
- finish operational shards;
- finish OpenAI / Anthropic / Gemini API interaction contour;
- finish Telegram channel interaction contour.

ПКТБ candidate:
puev5691/wellbeing-hq@2978b4d48c8c251963bbe4ea8e90e516ee76ab02:
entities/koordinator/outbox/KOO__PKTB-autonomous-governance-source-package-r01-candidate__PRO-OPERATOR.md

Disposition:
PAUSED_NOT_ACTIVE_NOT_REJECTED.

Fresh reconciliation:

SHARDS
- design candidate:
  wellbeing-hq@dc0e458fd8950fc5cc7fbb08034e7695630f7a77
- SIS review:
  wellbeing-hq@1ba484e9cc819f3514afdefe7476b6403b17a494
  PASS_SIS_OPERATIONAL_SHARD_STORE_DESIGN_R01_WITH_BOUNDARIES
- SHD review:
  wellbeing-hq@4515391b10b0f59af2052fb8171f5a86adea43ce
  PASS_SHD_OPERATIONAL_SHARD_STORE_DESIGN_R01_WITH_BOUNDARIES
- runtime store: NOT_ESTABLISHED
- WRITE/CAS: NOT_AUTHORIZED
- next causal class from design/reviews:
  separately authorized offline implementation/test candidate only.

LLM API
- Anthropic has accepted/verified transport/provider-compatible work in HQ history.
- OpenAI has verified live/booster/resolver/persistence work in HQ history.
- no fresh Gemini implementation/result lineage found in current reconciliation.
- requires separate fresh multi-provider reconciliation before choosing exact next implementation task.

TELEGRAM
- historical Phase1B line exists;
- later facilitator/normalized-event bridge work exists;
- newest fresh line includes read-only Bot API bridge and A+B identity/attestation design on 2026-09-25;
- requires fresh reconciliation of exact latest terminal/blocker before issuing new runtime task.

Priority ordering for next single-step execution:
1. operational shards offline implementation/test gate;
2. multi-provider API reconciliation (OpenAI/Anthropic/Gemini);
3. Telegram latest bridge/runtime reconciliation.

No automatic activation of 2/3 from this record.
