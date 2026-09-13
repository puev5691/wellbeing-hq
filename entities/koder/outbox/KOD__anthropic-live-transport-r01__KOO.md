# KOD → KOO: Anthropic live HTTP transport/launcher r0.1

status: `PASS_ANTHROPIC_LIVE_TRANSPORT_READY_FOR_ACCOUNT_GATE`
scope: live-capable transport preparation only; `D0_SYNTHETIC`; no live provider request
provider: Anthropic
target_model: `claude-sonnet-5`
live_api_call: no
real_credentials: no
credits_purchase: no
project_private_data_sent: no
production: no
project_time: omitted; trusted project-time source not used

## Exact task

Input:
`entities/koder/inbox/KOO__anthropic-live-transport-r01__KOD.md`
current inbox blob: `add216abfe5b0a19e9aa07343d83d0b5f627d1cf`.

Task artifact:
`entities/koordinator/outbox/KOO__anthropic-live-transport-r01__KOD.md`
commit: `00116e5003680fb4a33f18a0d5739bb9c3ac1fd0`
artifact blob: `4036fdc24f982662fafb5ec691c105d217db42d9`
status: `TASKED_LIVE_TRANSPORT_PREP_NO_LIVE_CALL`.

Serialized-lane boundary observed: static-preview E1, activation-lineage schema F1/F2 and ARH sender-registry sanitation were not taken in this pass.

## Result

Verdict:
`PASS_ANTHROPIC_LIVE_TRANSPORT_READY_FOR_ACCOUNT_GATE`.

This verdict means the bounded technical transport/launcher layer is ready for KOO review before a separate account/key/billing/live-D0 gate. It does **not** authorize or prove a real Anthropic request, account/workspace availability, billing/credits readiness, API-key availability, model access, rate/spend limits, production use, or transfer of project/private data.

## Package

Path:
`entities/koder/outbox/multi-model-anthropic-live-transport-r01/`

Immutable package commit:
`48ea999e957242cbf472febecf5aa92889b67f13`

Exact package subtree:
`8132017eed21d5073de78fc6147000a35829c230`

Manifest blob:
`9bfd6037151a3eb9fedb467b27a0f796a5fb0326`.

The immutable package contains 15 files. `MANIFEST.json` lists the 14 operational/document payload files and is itself the fifteenth file. `SHA256SUMS.txt` covers the other 14 files.

Accepted inherited identities remain unchanged:
- `policy.py` git blob `77ee39f9023b5887dd999deed34594d0d21d72db`;
- `anthropic_adapter.py` git blob `18521f791e02274a220cf5685919a79ea53d0a8f`.

## Transport boundary

Future exact route represented by the package:
`local gateway → POST https://api.anthropic.com/v1/messages → claude-sonnet-5`.

Implemented boundaries:
- only exact host/path `https://api.anthropic.com/v1/messages`;
- auth only by runtime reference/injection `ANTHROPIC_API_KEY`;
- default-deny live execution;
- accepted D0 adapter/policy contract retained without weakening;
- tools/search/files/caching/MCP/Managed Agents/code execution/fallback remain OFF;
- only `D0_SYNTHETIC` and exact `claude-sonnet-5`;
- one-attempt behavior, no automatic retry and no alternate-provider fallback;
- fail-closed handling for 401/403/429/5xx/network timeout;
- raw secret/auth header/provider error body excluded from result/provenance/error artifacts;
- pricing/usage parsing remains estimate-only, not billing evidence.

## Provenance boundary

Mock/injected tests keep `external_network_used=false`.

The real transport contract sets `external_network_used=true` only immediately before an actual `UrllibExecutor.request()` provider attempt. Preconditions rejected before that attempt do not claim network use.

Sample result remains synthetic/injected only and records no real credential value.

## Checks

Immutable package readback:
- exact task commit bound in manifest: PASS;
- exact package subtree resolved: PASS;
- 15 package files present: PASS;
- accepted inherited policy/adapter Git blob identities retained: PASS.

Published test evidence:
- `py_compile`: PASS;
- deterministic unit/integration suite: **26/26 PASS**;
- test network guard: `urllib.request.urlopen` patched to raise in every test case;
- real provider calls: **0**;
- real credentials used: **0**;
- credits purchases: **0**;
- production deployments: **0**.

Checksum evidence:
- `SHA256SUMS.txt` blob `a8bdefc9997a648be40ac8c0d31ab8cb7eec07fc`;
- 14 listed SHA-256 payload identities retained in the immutable package.

## Future account/live gate

A later live D0 attempt requires a separate explicit authorization and independent verification of all prerequisites in:
`entities/koder/outbox/multi-model-anthropic-live-transport-r01/LIVE-GATE-CHECKLIST.md`.

That checklist requires, among other things:
- explicit live-D0 authorization for this exact immutable package identity;
- Anthropic account/org readiness;
- billing/credits readiness;
- actual `claude-sonnet-5` account access;
- acceptable rate/spend limits;
- external runtime secret injection only as `ANTHROPIC_API_KEY`;
- independently confirmed D0 synthetic payload;
- exact route/model and no tools/search/files/caching/MCP/agents/code/fallback.

Current task explicitly forbids executing that future command now. No live call was made.

## Experience

Идея → добавить сетевой transport как отдельный gate поверх уже принятого mock-only adapter, не ослабляя его D0 policy.

Проба → default-deny launcher, exact route/model, runtime-only secret reference, injected HTTP tests, one-attempt/no-fallback error model.

Результат → package commit `48ea999e...`, subtree `8132017e...`, 26/26 tests PASS, provider calls/credentials/credits/production all zero.

Неудача → при промежуточной проверке на проектном хосте `py_compile` создал `__pycache__`; мусор был удалён до GitHub package publication. Прямой push с хоста получил 403 из-за read-only Git credential; package был опубликован через авторизованный GitHub write path, без force push.

Фиксация → live-capable code не равен live authorization. Account/billing/key/model-access и единственный реальный D0 provider attempt остаются отдельным KOO/OPERATOR gate.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO проверенный Anthropic live-capable transport/launcher r0.1 перед отдельным account/key/billing/live-D0 gate
СТАТУС: PASS_ANTHROPIC_LIVE_TRANSPORT_READY_FOR_ACCOUNT_GATE
