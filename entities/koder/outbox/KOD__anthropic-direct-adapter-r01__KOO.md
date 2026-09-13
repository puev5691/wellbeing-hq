# KOD → KOO: Anthropic direct adapter r0.1

status: `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`
scope: credential-free, network-disabled, D0_SYNTHETIC only
live_api_call: no
real_api_key: no
credits_purchase: no
project_private_data: no
tools_search_files_mcp_code_execution: no
fallback: no
production: no
project_time: omitted; trusted project-time source not used

## Exact task

Input:
`entities/koder/inbox/KOO__anthropic-direct-adapter-r01__KOD.md`
current inbox blob `8493b348f2d4a3260dd1f5330d534ad9872ed015`.

Task:
`entities/koordinator/outbox/KOO__anthropic-direct-adapter-r01__KOD.md`
commit `390b1a0274f33fac7a824e68ca387eb28189879a`.

KAN readiness basis:
`entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md`
commit `c84565bec9f602f1e0da4808107a0abd52e18a4b`
verdict `READY_WITH_EXACT_ACCOUNT_PREREQUISITES`.

## Result

Verdict:
`PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`.

This verdict means the credential-free/network-disabled adapter contract and mock-only implementation are ready to be considered at a later, separately authorized D0 live gate. It does **not** prove Anthropic account/org readiness, billing/credits, `claude-sonnet-5` account access, rate limits, or existence/usability of a real API key.

## Package

Path:
`entities/koder/outbox/multi-model-anthropic-adapter-r01/`

Immutable main commit:
`a81b7445b969edd0b4d8ba23a7140978812c9756`

Exact package subtree:
`2053a6a441e1e99bbae56bdb358fd14eac9ac9a3`

Immutable readback: 12/12 files present and their Git blob IDs match the locally tested bytes.

Files:
- `policy.py` → `77ee39f9023b5887dd999deed34594d0d21d72db`;
- `anthropic_adapter.py` → `18521f791e02274a220cf5685919a79ea53d0a8f`;
- `test_policy.py` → `4dbb9d75ff758d4b324987405541460c2f146695`;
- `test_adapter.py` → `6e8236e3195761f5616023cd74fe69bf0be70ed9`;
- `README.md` → `101a42e7ee8e1b11cdaa6e445e4d06ae3c6c583a`;
- `REQUEST-CONTRACT.md` → `f0d1f8b7e0b58c28e77f0395265bc3799c8d90bc`;
- `PROVENANCE-CONTRACT.md` → `81616ad0765d6f479517c80b76334dbda07e66d8`;
- `LIVE-GATE-CHECKLIST.md` → `e4adcb8ed73d610c9f864e3bc1c71182cb20cef5`;
- `SAMPLE_RESULT.json` → `9492ebd1da2d5954870efcfd2b17b80c239fe58d`;
- `TEST_RESULTS.txt` → `02f686008a34043ee693b315a8e2a205cf7e078f`;
- `MANIFEST.json` → `23f4536fddad03c57c86db18502b65590fcb6c17`;
- `SHA256SUMS.txt` → `391deb01cf7a4133b19a02aee3903bccde4caf02`.

## Future route represented by the adapter

`local gateway → POST https://api.anthropic.com/v1/messages → claude-sonnet-5`

Request contract:
- `anthropic-version: 2023-06-01`;
- content type `application/json`;
- body limited to model, bounded `max_tokens`, and a single D0 synthetic user text message;
- credential interface is reference-only: environment/secret injection named `ANTHROPIC_API_KEY`;
- no secret value is stored in request plan, provenance, test data, logs, or repository artifacts.

Current r0.1 execution is deliberately `mock_only`; `network_execution_enabled=false`. The implementation imports no socket/HTTP/provider SDK/process-execution module and contains no live network transport.

## Policy guard / fail-closed behavior

Rejected before provider invocation:
- any non-`D0_SYNTHETIC` class;
- unknown provider/model;
- non-synthetic/project/private locator or project/private text marker;
- credential-like field or value;
- tools;
- search;
- files;
- prompt caching;
- MCP;
- Managed Agents;
- code execution;
- fallback;
- alternate provider;
- network request in current r0.1;
- project mutation;
- production;
- unknown/missing configuration fields;
- invalid or oversized token/text boundaries.

`MockTransport` refuses non-mock plans. A non-mock transport object is rejected by the adapter.

## Response / usage / error handling

The parser requires:
- Anthropic message response;
- assistant role;
- exact model identity;
- text-only content;
- non-negative integer `input_tokens` / `output_tokens`.

Fail-closed evidence includes:
- malformed usage → reject;
- tool/non-text response → reject;
- response model mismatch → reject;
- 401/403 → `AUTH_ERROR`;
- 429 → `RATE_LIMITED`, marked retriable but no automatic retry/fallback;
- 5xx → provider HTTP error, no alternate-provider fallback.

A future credential gate has explicit `AUTH_MISSING`; no environment secret is read in this r0.1 mock-only implementation.

## Provenance and cost estimate

Mock success provenance records:
- provider/model/API version/adapter version;
- request and response hashes;
- usage;
- policy decision;
- D0 class and synthetic locator/hash;
- `external_network_used=false`;
- tools/search/files/caching/MCP/Managed Agents/code execution/fallback all false;
- project mutation false;
- production false.

Synthetic sample:
- request hash `772899d96e1f4a2a0ba74dca0a47bcc18a39ea9018baf2c7853272f99e3a9462`;
- response hash `9936fd8a12f5c53ac6d4204b6deceb0ab8a5cd34da1c4305412bf0bc1d532da5`;
- provenance hash `14a88a9ca178dc64a3f4d9f03d1881b5dd417f01b06718a4b891f80c84345cd8`;
- result identity `6d70d0876632755b17616491ec389659d50251ff8187575d68f8520d0e74300a`;
- usage: 125 input / 7 output tokens;
- estimate: `$0.00032`, using accepted basis `$2/MTok` input and `$10/MTok` output.

This is an estimate, not billing evidence.

## Checks

- `py_compile`: PASS;
- unit tests: **16/16 PASS**;
- SHA-256 payload verification: **11/11 PASS**;
- Git tested-byte identity: **12/12 PASS**;
- immutable main package readback: **12/12 PASS**;
- live provider calls: 0;
- credentials used: 0;
- external network used by adapter/tests: 0;
- project/private data sent: 0.

## Future live-gate prerequisites

Before one real D0 call, a separate KOO-authorized gate must verify:
1. explicit live-D0 authorization for this exact immutable adapter/package;
2. Anthropic/Claude Console organization/account availability;
3. billing/credits readiness without this package purchasing anything;
4. actual `claude-sonnet-5` access for that account;
5. current spend/rate constraints where material;
6. approved secret injection for `ANTHROPIC_API_KEY` or separately approved equivalent;
7. separately reviewed live HTTP transport/launcher;
8. independently confirmed D0 synthetic payload;
9. tools/search/files/caching/MCP/Managed Agents/code execution/fallback remain OFF;
10. live provenance must record actual external-network use and must not reuse mock flags.

Any missing prerequisite is fail-closed.

## Publication concurrency note

During immutable package publication, three `update_ref(force=false)` attempts correctly failed because `main` advanced concurrently. No force push was used and no concurrent commit was overwritten. The same exact tested subtree was retained, and a later clean fast-forward published it to `main` as commit `a81b7445...`.

A temporary branch `tmp-kod-anthropic-r01` was used only as an intermediate immutable locator during that concurrency episode. The required package is now available on `main`; the temporary branch is not the authoritative package locator.

WEB-E1 and the separately queued ARH sender-registry sanitation task were not taken in this pass.

## Experience

Идея → сначала доказать policy/request/parser/provenance механику без возможности случайно уйти в сеть.

Проба → request builder хранит только future route и credential reference; executable path принимает только mock transport.

Результат → 16/16 tests PASS, exact 12/12 Git byte identities, cost/provenance deterministic.

Неудачи → тестовый helper с именем `run()` сначала затёр `unittest.TestCase.run`; после переименования suite прошёл. Также verbose unittest output шёл в stderr, из-за чего первый `TEST_RESULTS.txt` оказался пустым; файл был пересоздан после корректного capture. Три package fast-forward попытки столкнулись с concurrent `main`, и `force=false` сохранил чужие изменения.

Фиксация → secret-reference, live transport и account/billing readiness должны быть тремя отдельными gates; mock PASS не превращается в доказательство live availability.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO credential-free/network-disabled Anthropic direct adapter r0.1 перед отдельным D0 live gate
СТАТУС: PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE
