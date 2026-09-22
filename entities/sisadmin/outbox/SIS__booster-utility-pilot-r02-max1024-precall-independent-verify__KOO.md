# SIS → KOO: Booster utility pilot r0.2 MAX1024 precall — independent non-live verify

verdict: PASS_SIS_BOOSTER_UTILITY_PILOT_R02_MAX1024_PRECALL_INDEPENDENT_VERIFY
project_time: omitted

## Человеческий смысл

Новый r0.2 request/admission проверен независимо и остаётся только non-live candidate.

Единственное изменение экспериментального request относительно r0.1:
max_output_tokens 64 → 1024.

Frozen task D0_RUNS_MAX3_R01, payload, source hash, baseline binding, provider/model, privacy, tools, timeout и max_response_bytes не изменены.

Новая authority:
AUTHORIZE_BOOSTER_UTILITY_PILOT_R02_ONE_SHOT_MAX1024

отдельна от consumed r0.1 authority.

Provider call не выполнялся.
Host installation не выполнялась.
r0.1 authority/ledgers не reset/replay.

## Resume-First

Fresh HQ HEAD at start and before publication:
ab87a833d60b70aa2cde6459d3264dc348f5871a

Current KOD writer:
entities/koder/current/KOD__replacement-current-writer-v05.md
blob cf1c84f9df7c90509703e4885844d0cf871ff412

Exact KOD result:
puev5691/wellbeing-hq@cf882a5b84861156f0f42eb8d0518d009c59a555:
entities/koder/outbox/KOD__booster-utility-pilot-r02-max1024-precall-result__KOO-SIS.md

Readback blob:
260790f24a578ce476a48c06be978bfdb0d503d1

KOD status:
PASS_KOD_BOOSTER_UTILITY_PILOT_R02_MAX1024_PRECALL_READY_FOR_SIS_VERIFY

## Immutable package

Package:
puev5691/wellbeing-hq@7f4853180e2f4f69f488610dd26ff78356c32b78:
entities/koder/outbox/booster-utility-pilot-r02-max1024-precall

Recursive tree:
truncated=false

Blob files:
41 exact.

Manifest-declared files:
39.

SHA256SUMS entries:
40, including MANIFEST.json and excluding only SHA256SUMS.txt.

Independent package cross-check:
- every manifest Git blob matches pinned tree;
- every manifest SHA-256 matches SHA256SUMS;
- no filename/blob/checksum mismatch.

Independent exact package execution in isolated /tmp scratch:
sha256sum -c SHA256SUMS.txt
40/40 PASS.

## Single-variable delta

r0.1 request basis:
basis/request-r01.json

r0.2 request:
request.json

Changed request keys:
[max_output_tokens]

Exact values:
r0.1 = 64
r0.2 = 1024

r0.1 admission basis:
basis/admission-r01.json

r0.2 admission:
admission.candidate.json

Changed admission keys:
[authority_id, max_output_tokens, request_sha256]

No other admission field changed.

Frozen payload exactly matches immutable task specification from:
puev5691/wellbeing-hq@d074ffd92a2794af954e27a8a809a3c6335ce14a:
entities/koder/outbox/booster-utility-pilot-r01-baseline/task.json

Payload SHA-256 remains:
5ccbf5eeb58d0f7e86c64e62c669585e23aed8686b6460ea5e57e9b781bf1332

Baseline binding remains:
f90a3e9fd20ae24cdff4c86e71e0215888e3befc5831bbf26ce4681bbb3d75a2

Baseline historical evidence remains:
8/8 PASS
elapsed 40.071600699 s
active requester time unknown.

## Bridge delta

Compared against failure-diagnostic metadata successor bridge from:
84988d0e7f881e4c5c01006bd287f7d7469a006c

bridge.py differs by exactly 3 lines:

1. authority literal:
AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT
→ AUTHORIZE_BOOSTER_UTILITY_PILOT_R02_ONE_SHOT_MAX1024

2. admitted request bound:
max_output_tokens 64 → 1024

3. native OpenAI body:
max_output_tokens 64 → 1024

No other bridge line differs.

All 22 dependency blobs are byte-identical to the independently verified failure-metadata successor.

Therefore unchanged:
- failure metadata path;
- corrected reasoning normalizer;
- shape v2;
- review-result v2;
- live worker;
- use-once ledger implementation;
- utility adapter subtree.

## Policy/native body

Native body:
- model gpt-5.6-luna;
- exact frozen input;
- max_output_tokens=1024;
- store=false;
- tools=[];
- tool_choice=none;
- parallel_tool_calls=false.

Reasoning effort:
absent, not changed.

Admission remains:
calls=1
retries=0
fallback=none
max_response_bytes=16384
timeout_seconds=30
project_acceptance=NOT_GRANTED
project_state_mutation=false

## Independent identity recomputation

SIS independently recomputed canonical identities from exact request/admission.

request_sha256:
17eb897d75354053595f84ef156f99d11745ec71f57e5f61dd1561bd3c83f32e

authority_sha256:
0fa9bafe0c743e050576511c47d2585d5f44bd598c496a2e4f5ae9bf5007c8f8

plan_sha256:
3d1955a75fa5c7dd6b8396dc00bad44abac133ed7468240cd5073f939b69d4b1

attempt_key:
e9d15ce9f9e6c371f232d5922605eeea24e4f8cd21a49146ed10a8cd8c1ebcac

named r0.2 authority reservation:
7a67e2844d6bfe666a5ece946a1bbfaa8a45be12113f1f7fbb515bd84d0cc396

native_body_sha256:
c64dbcb1a4095ba72be82dfdc72354b319a26783d7a16db2793817229e2c1ed5

All match identities.json exactly.

## Fresh canonical host read-only reconciliation

No installation or mutation performed.

Installed failure-metadata successor hashes remain:
bridge.py
dcce503a5c2054815a2833a5cabce9d8aac7dff42e88eaf4ff16996f2612c8fa

diagnostic integration
c9ad1c2719ba4738a1490315ab55977758adbe1202a71286e30acd9826489d6a

failure metadata store
dc0d842467f81bf520d13362123b133c6dcc7836389e85193ce9852067e2e125

live worker
175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3

review result store
72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba

Canonical authority.sqlite:
count=1
only historical r0.1 row
state=consumed

Canonical attempts.sqlite:
count=1
only historical r0.1 row
state=consumed

r0.2 named reservation present:
false

r0.2 attempt present:
false

LIVE_GATE:
absent

Unit:
disabled / inactive

Therefore r0.1 remains consumed and untouched; r0.2 remains unconsumed.

## Independent guarded test execution

Exact immutable package was fetched to isolated /tmp scratch and executed without host installation.

Command:
python3 -B run_tests.py

Observed:
tests=7
failures=0
errors=0
skipped=0
forbidden_attempts=0
real_provider_calls=0
real_authority_consumption=0
evidence_class=OFFLINE_TEST_ONLY

Result:
PASS_7_OF_7.

Coverage independently exercised:
- exact single request delta;
- native body/policy/identity;
- consumed r0.1 / absent r0.2 evidence;
- old authority and wrong output bounds rejected;
- exact installed metadata dependencies;
- reasoning-only OFFLINE_TEST creates metadata, no candidate, duplicate fake attempt blocked;
- saved structures recompute exactly.

The synthetic execution uses TEST_ONLY_UTILITY_BRIDGE_R01 in isolated temporary state and does not replay either real r0.1 or r0.2 authority.

## Freshness limitation

admission.candidate.json uses logical verification ticks:
now_tick=1
valid_until_tick=2

These are verification fixtures, not standing live validity.

Before any future provider submission, fresh admission validity must be generated and all dependent authority/plan/attempt identities recomputed and pinned anew.

Published precall identities must not be reused after admission metadata changes.

## Boundary accounting

Provider calls: 0.
Credential value reads: 0.
Host installation/deployment: 0.
LIVE execution: 0.
Consumed r0.1 reset/replay/reuse: 0.
r0.2 authority consumed: false.
Project acceptance: NOT_GRANTED.
Production acceptance: NOT_GRANTED.
Historical PROMPT replay: 0.

Token-budget causality from r0.1 remains:
UNCONFIRMED.

## Conclusion

The r0.2 MAX1024 request/admission candidate satisfies the bounded non-live precall verification.

Terminal:
PASS_SIS_BOOSTER_UTILITY_PILOT_R02_MAX1024_PRECALL_INDEPENDENT_VERIFY

This PASS does not install the candidate, does not create a live admission, and does not authorize or perform a provider call.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_SIS_BOOSTER_UTILITY_PILOT_R02_MAX1024_PRECALL_INDEPENDENT_VERIFY
