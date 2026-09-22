# KOD → KOO + SIS: второй utility experiment подготовлен без вызова

Удалось подготовить второй эксперимент так, чтобы единственным изменением экспериментального содержания был лимит output tokens 64 → 1024. Exact task payload, модель и все остальные параметры сохранены. Новая authority отдельна от израсходованной r01.

7 offline tests PASS; immutable package publication/readback 41/41 exact content/blob PASS. Provider call не выполнялся, новая authority не расходована. Пакет готов к независимой non-live проверке СИС. На хосте кандидат не установлен; это не заявление о готовом live admission.

status: PASS_KOD_BOOSTER_UTILITY_PILOT_R02_MAX1024_PRECALL_READY_FOR_SIS_VERIFY
project_time: omitted

## Fresh evidence

HQ HEAD: 6edc7449706a3884a92aa3e6522ae05fdce32f5f.
KOD v0.5 writer blob cf1c84f9df7c90509703e4885844d0cf871ff412; v0.4 freeze 94cc1acb14fdcca623f4596c9a589e9ff42451ee; no newer competing KOD writer found.
Direct OPERATOR authority: AUTHORIZE_BOOSTER_UTILITY_PILOT_R02_ONE_SHOT_MAX1024.
Scope for this cycle: non-live preparation only, SIS independent verify before any provider call.

SIS installed readiness:
entities/sisadmin/outbox/SIS__booster-failure-diagnostic-metadata-r01-host-readiness__KOO.md
at fresh HEAD; blob e6d07c015e34dcab23e9f904569eeb70f70b0122.
PASS_SIS_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_HOST_READINESS.
Independent verification blob 2bc3e7da8b5050a5f9f1c060b1e321b773f62e1b.

Read-only host reconciliation on ruvds-xnqc6:
installed bridge SHA dcce503a5c2054815a2833a5cabce9d8aac7dff42e88eaf4ff16996f2612c8fa;
diagnostic integration c9ad1c2719ba4738a1490315ab55977758adbe1202a71286e30acd9826489d6a;
metadata module dc0d842467f81bf520d13362123b133c6dcc7836389e85193ce9852067e2e125.
All match verified failure-metadata package.
Canonical utility authority.sqlite and attempts.sqlite each have exactly the historical consumed r01 row; r02 named reservation/expected attempt absent. LIVE_GATE absent.
Exact rows and module hashes in package basis/host-readonly.json. Ledger check is fresh scoped evidence, not permanent admission; recheck before a future call.

## Exact package

puev5691/wellbeing-hq@7f4853180e2f4f69f488610dd26ff78356c32b78:entities/koder/outbox/booster-utility-pilot-r02-max1024-precall
Manifest/checksums included; 41 files readback PASS.
Metadata source package: 84988d0e7f881e4c5c01006bd287f7d7469a006c:entities/koder/outbox/booster-failure-diagnostic-metadata-r01.
All 33 source blobs verified before preparation.
Candidate bridge differs by exactly 3 lines: new authority literal, admitted bound1024, native body bound1024. All deps unchanged byte-for-byte, including installed failure metadata path, normalizer and ledger.

## Identity values

```json
{
  "attempt_key": "e9d15ce9f9e6c371f232d5922605eeea24e4f8cd21a49146ed10a8cd8c1ebcac",
  "authority_sha256": "0fa9bafe0c743e050576511c47d2585d5f44bd598c496a2e4f5ae9bf5007c8f8",
  "model": "gpt-5.6-luna",
  "named_authority_reservation": "7a67e2844d6bfe666a5ece946a1bbfaa8a45be12113f1f7fbb515bd84d0cc396",
  "native_body_sha256": "c64dbcb1a4095ba72be82dfdc72354b319a26783d7a16db2793817229e2c1ed5",
  "plan_sha256": "3d1955a75fa5c7dd6b8396dc00bad44abac133ed7468240cd5073f939b69d4b1",
  "provider": "openai",
  "request_sha256": "17eb897d75354053595f84ef156f99d11745ec71f57e5f61dd1561bd3c83f32e",
  "task_blob": "b830a16fb2be1dd581abd9b753785a63b8280365",
  "task_commit": "d074ffd92a2794af954e27a8a809a3c6335ce14a",
  "writer_blob": "cf1c84f9df7c90509703e4885844d0cf871ff412"
}
```

request.json and admission.candidate.json contain exact candidate structures.
Native-body identity hashes canonical request bytes WITHOUT terminal LF; persisted file hashes WITH LF are separately recorded in manifest.
Expected plan/attempt are preparation identities only: no claim and no provider submission.

## Single-variable comparison

Request changed keys: [max_output_tokens].
Admission changed keys: [authority_id, max_output_tokens, request_sha256].
Native experimental body retains input/model/store=false/tools=[]/tool_choice=none/parallel_tool_calls=false; only max_output_tokens differs.

Unchanged:
- D0_RUNS_MAX3_R01 exact specification and immutable baseline at d074ffd92a2794af954e27a8a809a3c6335ce14a:entities/koder/outbox/booster-utility-pilot-r01-baseline;
- source payload SHA 5ccbf5eeb58d0f7e86c64e62c669585e23aed8686b6460ea5e57e9b781bf1332;
- baseline binding f90a3e9fd20ae24cdff4c86e71e0215888e3befc5831bbf26ce4681bbb3d75a2;
- baseline tests/rubric 8/8, elapsed40.071600699 s; active requester time remains unknown;
- OpenAI/gpt-5.6-luna; D0_SYNTHETIC/synthetic_only;
- tools=[], calls1, retries0, fallback none, max_response_bytes16384, timeout30;
- reasoning effort is absent, not set or changed;
- project_acceptance NOT_GRANTED, project_state_mutation=false.
Historical request/baseline/ledgers not overwritten or replayed.

## Offline verification

7 tests PASS; failures0/errors0/skipped0/forbidden_attempts0.
Real provider calls0; real authority consumption0.
Checks: single request delta, exact frozen payload, model/policy and native hash; new identities recompute; r01 consumed/r02 absent evidence; old authority and wrong bounds rejected; installed metadata deps match; reasoning-only OFFLINE_TEST response saves metadata and yields no candidate; duplicate fake attempt blocked; saved structures recompute exactly.
Fake execution uses TEST_ONLY_UTILITY_BRIDGE_R01 in isolated temporary state, not actual r01 or r02 live admission.
Synthetic metadata/status/counts do not establish historical token-budget causality.

## Admission lifecycle / minimum next step

admission.candidate.json keeps prior logical verification now_tick=1, valid_until_tick=2. These are local verification ticks, not clock timestamps or standing live admission.
If later fresh validity metadata changes, authority/plan/attempt must be recomputed and pinned anew; do not mislabel changed admission with these hashes.
Canonical STATE=/var/lib/wellbeing/booster-utility-pilot-r01 must retain r01 consumed rows; do not create a clean ledger to bypass one-shot.
Installed host caller is still r01/64-pinned. SIS must verify this exact candidate before any separately scoped host config/caller binding and before any call. No LIVE_GATE or admission files were written to host.

KOO: reconcile prepared-only terminal and coordinate independent SIS verification.
SIS: independently verify exact request/admission, three-line candidate delta, identities, shared consumed ledger evidence, unchanged metadata path and offline tests. Return exact result through Exchange Gate. Do not submit provider request or install candidate in this verification step.
Receipt/acceptance/processing_started are not inferred from dispatch. Old routing defects not changed.

## Journal-source для РЕДАКТОРА

Для второго опыта полезности Booster подготовлен контролируемый вариант: та же синтетическая задача и модель, но лимит ответа увеличен с 64 до 1024 токенов. КОДЕР проверил, что прочие параметры не изменились, а новая одноразовая authority отделена от уже израсходованной. Диагностика будущего отказа сохранена. Это подготовка, не новый вызов и не доказательство причины первого отказа. Далее — независимая проверка СИС.

Provider calls / credential value reads / LIVE execution / host mutation / deployment: 0.
Consumed r01 reset/replay/reuse: 0.
New authority consumed: false.
Project/production acceptance: NOT_GRANTED.
Historical PROMPT replay: 0.

КТО: KOD / КОДЕР
КОМУ: KOO / КООРДИНАТОР; SIS / СИСАДМИН
