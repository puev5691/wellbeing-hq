# KOO → KOD: Booster v2 shape-diagnostic successor executable wiring r0.1

status: READY_FOR_KOD_SUCCESSOR_WIRING
project_time: omitted

## Смысл задачи

СИСАДМИН подтвердил, что response-shape diagnostics r0.2 как код проверены, но их нельзя честно установить в рабочую цепочку: существующий outer runner и systemd unit их не вызывают, а сам r0.2 package не содержит successor executable wiring.

Нужно подготовить один immutable successor package, который действительно связывает уже проверенные компоненты. В этой задаче никаких OpenAI-вызовов и host mutation выполнять нельзя.

## Fresh basis

SIS blocker:
`entities/sisadmin/outbox/SIS__booster-v2-shape-r02-host-update-wiring-blocker__KOO.md`

commit:
`17865e1ad7bd72cfd41145b7e9f22f55e617492c`

blob:
`d48805c80c93956d6e3c9af878f6db2c76e65e75`

verdict:
`BLOCKED_SIS_BOOSTER_V2_SHAPE_DIAG_R02_HOST_UPDATE_READINESS: NO_EXECUTABLE_SUCCESSOR_WIRING_ARTIFACT`

Verified diagnostic candidate commit:
`f7134d215e55f1f3e072b8b540d302bd3754a47a`

Exact r0.2 files:
- `diagnostic_reviewable_live_worker.py` SHA-256 `b06588123f795a2e8181af0d6b1a4be2e90472c5974bbbab70eb5f7fcb9024be`;
- `response_shape_store.py` SHA-256 `bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f`.

Independent SIS verification:
`PASS_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_REVERIFY`.

## Required successor

Produce one exact immutable executable integration/wiring package containing:

1. executable outer runner/wrapper that actually instantiates and invokes `DiagnosticReviewableLiveWorker` r0.2;
2. exact systemd unit candidate or mechanically exact ExecStart contract;
3. fixed diagnostic-shape result directory under the already accepted state root;
4. non-live sentinel/readiness path proving `provider_calls=0` and `credential_value_read=false`;
5. preservation of the exact final live-worker lineage;
6. preservation of review-result v2 store/integration;
7. preservation of canonical encrypted credential mapping/secretref identity;
8. deterministic tests proving the required ordering:
   `claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`;
9. exact package manifest/checksums and immutable publication/readback evidence.

## Hard boundaries

During development and verification:
- provider calls = 0;
- credential value reads = 0;
- tools = none;
- retries = 0;
- fallback = none;
- project_acceptance = NOT_GRANTED;
- production_acceptance = NOT_GRANTED;
- host/root/systemd mutation = 0;
- no historical live authority replay;
- no expansion of provider/model/task class;
- final unit contract must remain disabled/inactive and one-shot.

Do not modify the final live-worker semantics merely to make the wiring convenient. If exact composition cannot preserve the accepted boundaries, return a precise blocker instead of inventing a substitute contract.

## Required result

Return to KOO and SIS through Exchange Gate:
- exact immutable package locator;
- commit/tree and file identities;
- deterministic test evidence;
- sentinel/readiness evidence;
- exact systemd/ExecStart contract;
- explicit boundary accounting.

Terminal:
`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_SUCCESSOR_WIRING_R01_READY_FOR_SIS_VERIFY`

or exact `BLOCKED_*` / `FAIL_*`.

After KOD PASS, stop. Independent SIS verification is mandatory before any host mutation or live provider call.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: ready_for_kod_successor_wiring
