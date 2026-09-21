# KOO → KOD: Booster reasoning metadata normalizer correction r0.1

status: OPERATOR_POLICY_APPROVED__READY_FOR_NON_LIVE_CORRECTION
project_time: omitted

## Человеческий смысл

ОПЕРАТОР утвердил узкую политику: известный OpenAI output item типа `reasoning` допускается только как игнорируемый служебный контейнер. Он не становится результатом, командой или основанием для изменения состояния проекта.

Пользовательским результатом остаётся только разрешённый `message → assistant → output_text`.

`function_call`, tool calls и неизвестные output-типы по-прежнему должны блокироваться fail-closed.

Эта задача только на non-live исправление и проверку. Новый OpenAI-вызов не разрешён.

## Operator decision

Exact decision:
`APPROVE_BOOSTER_REASONING_AS_IGNORED_METADATA_R01`

## Verified diagnostic basis

KOD diagnostic:
`puev5691/wellbeing-hq@8ac4f80eef7444c9e278e77f887c41a1d0a21c09:entities/koder/outbox/KOD__reasoning-normalizer-diagnostic-r01__KOO.md`

blob:
`06048835c39bd754be20e0ca3569e255f2fff315`

terminal:
`PASS_KOD_REASONING_NORMALIZER_CAUSE_REPRODUCED_R01`

KOO receipt:
`routes/receipts/KOD__reasoning-normalizer-diagnostic-r01__KOO.receipt.md`
commit `83cdc32798b1f931a97a75dea9e1a70c2e6ea7ec`.

## Exact policy

Allowed handling:
1. output item `type=reasoning` may be present before/alongside the allowed assistant message;
2. normalizer ignores reasoning content for review-result production;
3. reasoning content must not be promoted into user-visible result, commands, tool requests, project-state mutations or acceptance evidence;
4. diagnostic shape may record only the already-approved structural classification/metadata needed for evidence;
5. review-result v2 is derived only from allowed `message` with `role=assistant` and allowed `output_text`.

Must remain fail-closed:
- `function_call`;
- tool/action requests;
- unknown output item types;
- non-assistant message roles;
- disallowed content item types;
- ambiguous/multiple result semantics outside the existing accepted contract.

No broader OpenAI response-shape policy is granted.

## KOD task

Produce one immutable non-live successor correction package.

Requirements:
- preserve exact final live-worker lineage;
- preserve response-shape diagnostic persistence-before-normalization;
- preserve review-result v2 store/integration and strict readback;
- implement only the approved reasoning-as-ignored-metadata policy;
- add deterministic positive test for `reasoning + assistant/output_text`;
- retain negative tests proving `function_call`, tools/actions and unknown output types remain blocked;
- include plain assistant-only regression test;
- include persistence/readback ordering tests;
- verify no reasoning content is copied into review-result v2;
- provider calls = 0;
- credential value reads = 0;
- host/systemd mutation = 0;
- deployment = 0;
- retries = 0;
- fallback = none;
- tools = none;
- project_acceptance = NOT_GRANTED;
- production_acceptance = NOT_GRANTED.

Publish exact immutable package with manifest/checksums, deterministic test evidence and human-readable result.

Route result to KOO and SIS through Exchange Gate.

After PASS stop. Independent SIS verification is mandatory before any host mutation.

No live/provider-call authority is created by this task. The previous one-shot authority is consumed and MUST NOT be replayed.

Expected terminal:
`PASS_KOD_BOOSTER_REASONING_METADATA_NORMALIZER_CORRECTION_R01_READY_FOR_SIS_VERIFY`
or exact `BLOCKED_*` / `FAIL_*`.

For a significant result, provide the existing editorial journal-feed with a concise Russian human-readable source rather than raw machine telemetry.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: READY_FOR_NON_LIVE_CORRECTION
