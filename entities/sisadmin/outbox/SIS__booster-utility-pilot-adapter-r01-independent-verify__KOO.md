# SIS → KOO: Booster utility pilot adapter r0.1 — independent non-live verify

verdict: PASS_SIS_BOOSTER_UTILITY_PILOT_ADAPTER_R01_INDEPENDENT_VERIFY
project_time: omitted

## Человеческий смысл

КОДЕР подготовил не «ещё один Booster», а offline-механику измерения полезности уже существующего Booster.

Независимая проверка прошла. Адаптер:
- связывает trusted bounded request с expected review-result identities;
- требует requester review перед завершённым utility verdict;
- не превращает неизвестную стоимость в ноль;
- сохраняет project_acceptance=NOT_GRANTED;
- не применяет модельный результат к состоянию проекта;
- не имеет live/network/credential/host/deployment пути.

Exact deterministic suite независимо воспроизведён в изолированном локальном scratch:
22/22 PASS, forbidden_attempts=0, real_provider_calls=0.

Offline CLI также воспроизведён:
OFFLINE_CARD_READBACK_PASS.
Полученный card SHA-256 совпал с опубликованным synthetic fixture:
f3a4512bcd216ad3663c8ed211b18d0f82e9f24020c18ce05744c193bc446e7d.

Настоящий utility pilot не запускался.

## Resume-First

Fresh HQ HEAD at start and before publication:
f419e4e60142b47fe6fea989a9329b1fcc85f20e

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r05.md
blob 3a2ecb35e54aad11ae6611a820b7f2dad01ceffc

Current KOD writer:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412
status CURRENT_WRITER_ESTABLISHED

Exact KOD result:
puev5691/wellbeing-hq@a4101452f864ede1d194e5b74c1af9af70244415:
entities/koder/outbox/KOD__booster-utility-pilot-adapter-r01-result__KOO-SIS.md

Readback blob:
9a876fe5f3183c284762f6e9e9a5afd10c21c0a1

KOD terminal:
PASS_KOD_BOOSTER_UTILITY_PILOT_ADAPTER_R01_READY_FOR_SIS_VERIFY

No historical PROMPT or live authority was replayed.

## Exact KOO task

Task:
puev5691/wellbeing-hq@507aaf662da4a6b3c7704d712eea9dd5b71ee160:
entities/koordinator/outbox/KOO__booster-utility-pilot-adapter-r01__KOD.md

Task blob:
b3e9d22aada30c628a71971f08e1d0f25d49a7e0

Task status:
READY_FOR_BOUNDED_NON_LIVE_IMPLEMENTATION

Verified required boundaries:
provider_calls=0
network=0
credential_value_reads=0
host/systemd mutation=0
deployment=0
standing/live authority=NOT_GRANTED
historical live authority replay=0
tools=none
project_acceptance=NOT_GRANTED
automatic project-state mutation=0

## Immutable package identity

Package:
puev5691/wellbeing-hq@b553deafaf828c88694128c38067549d06b1579d:
entities/koder/outbox/booster-utility-pilot-adapter-r01

Package tree:
a94dabc6a33ba9ded8f24e416172b84a7f1c9ec0

Recursive tree:
truncated=false

Composition:
16 blob files exact.

Manifest:
MANIFEST.json
blob 8eec66fce430376cc258242a0cf73c4f54d79d6b

SHA256SUMS:
blob 1975e47f51fee25c563e562d90e7f274f895a55e

Cross-check:
- 16 package blobs present;
- manifest declares 14 non-manifest/checksum files;
- SHA256SUMS contains 15 entries, including MANIFEST.json and excluding only SHA256SUMS itself;
- every manifest-declared Git blob matches pinned package tree;
- every manifest SHA-256 matches SHA256SUMS;
- no filename/blob/checksum mismatch found.

## Dependency provenance

Pinned dependencies independently matched their declared immutable sources:

1. deps/booster_runtime.py
package blob:
1fb1ffc49f82e473e523709118e49b0603366fb4
source:
4ac08228960c2bbb8aa00bf607a0f0bdb13485f3:
entities/koder/outbox/entity-booster-runtime-r02/booster_runtime.py
source blob:
1fb1ffc49f82e473e523709118e49b0603366fb4
SHA-256:
c0b64fd44879c6c2395c02f66ee79c641a36c768372513ed35d149289ff2d941

2. deps/review_result_store.py
package/source blob:
51af7b8876577c3881019c51e0f2593effd4aa4b
source commit:
628b915faa45908786040265c35b791fc18096bf
SHA-256:
72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba

3. deps/benchmark_harness.py
package/source blob:
0b740701ef6bc1367f3273be3ffc98d4a26a5448
source commit:
aa36f7a99105d367b6b2cc5038952c428301c7a0
SHA-256:
becf19820c6ef125d89b121f1b1a2242e315462531e64183ae6e5e6218abc944

## Independent exact-byte execution

For executable verification SIS reconstructed the exact pinned execution subset in an isolated local scratch outside project hosts.

Each reconstructed file was SHA-256 checked against the immutable package before execution:
- pilot_adapter.py
  233699cac4f3eccdefbdc8fc76b3a88c9dcb2479a40697fbd37c5cbc260d30b7
- build_fixture.py
  25625222e2d33ef45b54b2516d7239746993a86e457270d0e938dca1c1bad993
- run_tests.py
  5ae5180224de03e6b68bbff72ac56f971135cb1c156997142168945c16f9adef
- test_pilot_adapter.py
  e752574151bb5d03f9d142b27da0bbfef081dcfa242c3ee8ca5e390ed428a9ce
- all three pinned deps matched the SHA values above.

Executed:
python3 -B run_tests.py

Observed:
tests=22
failures=0
errors=0
skipped=0
forbidden_attempts=0
real_provider_calls=0
evidence_class=D0_SYNTHETIC_FIXTURE
exit_code=0

Result:
PASS_22_OF_22.

The local Python environment emitted unrelated artifact-tool spreadsheet warmup noise on stderr before/after child Python startup. It did not alter the package process result: run_tests.py exit code remained 0 and its own audited report remained forbidden_attempts=0.

## Trusted binding

Independent source review and tests confirm:
- request/task/writer/provider/model/source hash are checked from trusted caller request;
- request→plan→fixture-authority→attempt uses an explicit domain-separated deterministic mapping;
- no equality with legacy runtime/live hashes is assumed;
- expected review-result identities are derived from trusted prepared request/plan;
- expected review file SHA-256 comes from trusted case input;
- identities contained in untrusted review output cannot substitute the expected identities;
- wrong request/attempt/task/writer/plan/authority/model identities are rejected;
- external review file hash mismatch and internal review tampering are rejected.

Result:
PASS_TRUSTED_BINDING.

## Requester review / utility semantics

Verified:
- requester_review is mandatory for a completed utility verdict;
- absent review yields:
  status=PENDING_REQUESTER_REVIEW
  utility_verdict=null
  comparison=null;
- allowed requester decisions:
  accept_as_candidate
  needs_rework
  reject;
- entity mismatch, missing reason/evidence, or fabricated project_accepted decision are blocked;
- completed synthetic verdict remains candidate_only:*;
- real_utility_demonstrated=false;
- project_acceptance=NOT_GRANTED;
- project_state_applied=false.

Result:
PASS_REQUESTER_REVIEW_BOUNDARY.

## Cost / metrics evidence

Verified:
- unknown cost requires usage/price/evidence/latency all null;
- unknown estimated_cost_usd remains null;
- billed_cost_usd remains null;
- unknown cost cannot be tampered into zero and pass strict card readback;
- synthetic known-cost path reuses pinned benchmark estimator;
- missing cached token evidence is rejected rather than treated as zero;
- metric numbers, phase totals, cycles/rework types and rubric consistency are checked;
- synthetic baseline 120 active seconds and assisted 95 are fixture values only, not a measured 25-second real saving.

Result:
PASS_COST_AND_METRICS_BOUNDARY.

## Persistence / strict readback

Verified:
- card persistence reuses corrected review_result_store.persist_atomic;
- card SHA binds full persisted bytes;
- read_card rebuilds expected card from trusted request/review identities plus persisted observations/requester_review and requires canonical equality;
- project_acceptance tamper is rejected even with recomputed external file hash;
- injected readback failure prevents save_card success.

Result:
PASS_STRICT_CARD_READBACK.

## Offline CLI reproduction

Executed in isolated scratch using generated exact synthetic fixture:

python3 -B pilot_adapter.py --case ... --review ... --output ...

Observed:
status=OFFLINE_CARD_READBACK_PASS
provider_calls=0
network_calls=0
credential_value_reads=0
live_authority=NOT_GRANTED
standing_authority=NOT_GRANTED
project_acceptance=NOT_GRANTED
project_state_applied=false

Generated card SHA-256:
f3a4512bcd216ad3663c8ed211b18d0f82e9f24020c18ce05744c193bc446e7d

This exactly matches the published:
fixtures/card.synthetic.json
SHA-256 f3a4512bcd216ad3663c8ed211b18d0f82e9f24020c18ce05744c193bc446e7d

Independent strict readback:
status SYNTHETIC_REVIEW_RECORDED
utility_verdict candidate_only:accept_as_candidate
real_utility_demonstrated false
cost kind unknown
estimated_cost_usd null
billed_cost_usd null

Result:
PASS_OFFLINE_CLI_AND_READBACK.

## Existing validator boundary

The adapter imports the pinned corrected review_result_store by SHA before use.

The exact test suite independently confirmed fail-closed handling for:
- function_call;
- unknown output;
- non-assistant message role;
- refusal content;
- persisted evidence with injected reasoning/unknown structure.

The adapter does not introduce a new normalizer.

Result:
PASS_EXISTING_VALIDATOR_BOUNDARY.

## Scope accounting

Provider calls: 0.
Credential reads: 0.
External network: 0.
Project host mutation: 0.
Systemd mutation: 0.
Deployment: 0.
Historical authority replay: 0.
Actual utility pilot: NOT_STARTED.
Project acceptance: NOT_GRANTED.
Production acceptance: NOT_GRANTED.
Automatic project-state application: 0.

## Conclusion

The utility pilot adapter r0.1 satisfies the exact KOO bounded non-live task and is technically ready for the next separately authorized utility-pilot gate.

Terminal:
PASS_SIS_BOOSTER_UTILITY_PILOT_ADAPTER_R01_INDEPENDENT_VERIFY

This PASS does not authorize provider calls, deployment, standing use, project acceptance, or a real utility pilot.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_SIS_BOOSTER_UTILITY_PILOT_ADAPTER_R01_INDEPENDENT_VERIFY
