# KOO → OPERATOR: booster v2 shape diagnostics r0.2 host-update readiness gate

status: OPERATOR_DECISION_REQUIRED
project_time: omitted

## Что произошло

КОДЕР подготовил r0.2 response-shape diagnostics, а СИСАДМИН независимо подтвердил:
- exact successor bytes;
- canonical snapshot identity;
- external expected_snapshot_sha256 binding;
- complete evidence readback binding;
- 39/39 deterministic tests;
- self-consistent tamper rejection.

SIS terminal:
`PASS_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_REVERIFY`

commit:
`77c860e303b0b9f4c8adf0beb30d834b9694af86`

## Почему нельзя сразу делать live call

На host `ruvds-xnqc6` сейчас установлен предыдущий runtime:

`/opt/wellbeing/openai-booster-result-v2-integration-r01`

Он был установлен до появления r0.2 response-shape diagnostics.

Поэтому следующий live call должен выполняться только после того, как exact independently verified r0.2 установлен и проверен на host.

## Предлагаемый отдельный шаг

Разрешить СИСАДМИНУ один bounded non-live host update/readiness step:

`AUTHORIZE_BOOSTER_V2_SHAPE_DIAG_R02_HOST_UPDATE_READINESS`

Allowed:
- install exact verified r0.2 diagnostic runtime bytes on `ruvds-xnqc6`;
- preserve verified result-v2 persistence and one-shot worker dependencies;
- update/register exact bounded systemd/runtime wiring as required by r0.2;
- keep unit disabled;
- preserve canonical encrypted credential mapping/secretref identity;
- create diagnostic-shape result directory if required;
- verify exact installed hashes, modes, ownership and write paths;
- run non-live sentinel/dry/readiness validation only;
- verify future ordering:
  `claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`;
- verify expected_snapshot_sha256 is carried independently through runtime;
- verify historical consumed authority remains untouched/non-reusable.

Forbidden:
- any OpenAI/provider call;
- credential value read/use/exposure;
- live mode;
- parser correction;
- retries/fallback expansion;
- enabling persistent/automatic execution;
- project acceptance;
- production acceptance;
- deployment to another host.

Required terminal:
- provider calls = 0;
- credential accesses = 0;
- unit disabled/inactive;
- exact r0.2 installed-byte identities recorded;
- non-live readiness PASS or exact blocker;
- historical consumed live acceptance remains BLOCKED;
- no new provider-call authority created.

## Следующий gate после PASS

Только после successful host-update/readiness KOO may open a separate one-shot diagnostic-live authority gate.

That later live gate must be fresh and must not reuse historical consumed authority.

## Decision requested

`AUTHORIZE_BOOSTER_V2_SHAPE_DIAG_R02_HOST_UPDATE_READINESS`

Any other response does not authorize host mutation.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED
