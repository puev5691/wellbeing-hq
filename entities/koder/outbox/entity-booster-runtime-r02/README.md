# Entity booster runtime r0.2

Статус: bounded non-live candidate.

## Назначение

Один Entity-facing runtime связывает:

`Entity bounded request → authority/policy gate → verified Resource Gateway → pinned provider-neutral orchestrator/provider adapter → replay-only bounded result → Entity review`.

В r0.2 никакого live provider execution нет. External model остаётся ресурсом, а не writer/authority.

## Entry point

`booster_runtime.py`

CLI:

`python3 -I -B booster_runtime.py --gateway <verified-gateway.py> --live-worker <verified-live_worker.py> --deps <pinned-deps-dir> --ledger <one-shot-ledger.sqlite> --request <request.json>`

Input содержит ровно три объекта:
- `request`;
- `authority`;
- `replay`.

Любое дополнительное поле, включая credential/live shortcut, отклоняется.

## Binding

Request и authority явно связывают:
- Entity id + role;
- exact task path/commit/blob;
- exact writer path/commit/blob;
- provider;
- model;
- privacy class;
- tools;
- bounded payload/source identity;
- output cap.

Текущий authority mode только `REPLAY_ONLY`.
`live_execution_authorized` обязан быть `false`.

## Reused verified components

### Entity Resource Gateway MVP

Independent PASS:
`fd49601948827cc43e46331ae98ab1f680101c0a`.

Package:
`entities/koder/outbox/entity-resource-gateway-mvp-r01/`
commit `f4807a5f2e3231fda3e4ba0f258de647b055c6e4`
tree `0160558fc173b52b20ac055e81112910091a2fd1`.

Runtime:
`gateway.py` blob `e93ac320468dfeed84a7342b4e9dc5c597f48fc2`,
SHA-256 `703f9e4a72ab043063ff74f636ec6c3fa85de1a8fc8b89ac1859623f46a17d7a`.

That gateway pins and uses:
- orchestrator MVP blob `55939b2e4c91f7af1159a60b2f4ee8fa961196f2`;
- OpenAI policy blob `f04676995d63e6e5eadb9474aaf2d15e5153ab43`;
- OpenAI adapter blob `47c2c2e8bd361a2dafad3e66457c95de9a11d5e0`;
- Anthropic adapter blob `985746909772900d9c72257dc53478aa34861d91`.

These bytes were independently verified as one gateway dependency set. r0.2 intentionally reuses that exact verified set rather than silently upgrading provider bytes.

### Live-worker safety component

Independent final PASS:
`18af0b778d5b30f15c20da989a39006f503dcff3`.

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/`
commit `716637bb0e18319fa8f3151253ed5c71b8c1aad7`
tree `2737ae65789e6608ad71631e074cc67602a182ab`.

Runtime:
`live_worker.py` blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`,
SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`.

r0.2 reuses its durable one-shot ledger and final ResourceResult authority guard. It does not instantiate the live HTTP worker or credential resolver.

## One-shot and safety

Only after request/authority/privacy/tools binding succeeds, r0.2 lazily opens the verified durable SQLite ledger and claims:
`authority identity + request identity + replay plan identity`.

Thus invalid authority does not create a ledger.

The reused live-worker contract retains:
- exactly one claimant;
- retries=0;
- max calls=1;
- hard timeout contract;
- response bound;
- redirect fail-closed;
- secret-reference-only credential interface for any separately authorized future live path;
- no provider/gateway writer authority.

The r0.2 replay entrypoint contains no credential input/resolver and makes no network call.

## Result contract

`wb.entity_booster.result.v2`

Always preserves:
- `project_acceptance=NOT_GRANTED`;
- `review_required=true`;
- caller writer unchanged;
- gateway/provider writer authority false;
- project state application false;
- external dispatch false;
- live provider calls = 0;
- credential reads = 0.

A successful technical result therefore still requires requesting Entity review. Receipt is not project acceptance.

## No fallback

Only the explicitly requested provider/model is passed into the verified Resource Gateway. Provider/model mismatch or unavailable paths fail closed. No alternate provider is selected.

## Boundaries

This package does not:
- call OpenAI or Anthropic live;
- read/create credentials;
- mutate billing/accounts;
- deploy to production;
- start automation;
- modify Project Sources;
- perform portal/Telegram/memory work;
- grant project acceptance or writer authority.
