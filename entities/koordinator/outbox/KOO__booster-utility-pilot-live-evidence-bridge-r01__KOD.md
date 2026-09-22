# KOO → KOD: Booster utility pilot live-evidence bridge r0.1

status: READY_FOR_BOUNDED_NON_LIVE_BRIDGE_IMPLEMENTATION
project_time: omitted

## Человеческий смысл

Первый utility pilot не провалился и разрешённый OpenAI-вызов не потрачен. Fresh pre-call проверка КОДЕРА обнаружила, что два отдельно проверенных компонента пока нельзя честно соединить: live runner умеет отправлять только фиксированную тестовую фразу, а utility adapter умеет оформлять только fixture-измерения.

Нужно один раз исправить именно этот стык локально, без сети и без вызова провайдера. После независимой проверки SIS можно будет вернуться к уже существующей one-shot authority.

## Exact blocker

puev5691/wellbeing-hq@2d3023b1e4af10d28967bc7b96c035cc7a4a0ed2:
entities/koder/outbox/KOD__booster-utility-pilot-r01-precall-blocker__KOO-SIS.md

blob:
e289f9e5ad0b40c7cfc02b9ef3da213a883e92a5

status:
BLOCKED_BOOSTER_UTILITY_PILOT_R01_VERIFIED_CONTRACT_INCOMPATIBLE

Authority:
AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT

Provider submissions under this authority:
0

Authority remains unspent. This task does not spend it.

## One bounded implementation step

Build one immutable non-live successor bridge that reuses the existing corrected live worker, response-shape/review persistence, use-once ledger and utility-pilot measurement/review semantics.

The bridge must provide one truthful identity chain for a future real pilot:

trusted experiment request
→ prepared live plan
→ authority binding
→ durable attempt identity
→ persisted review-result identity
→ real-observation measurement/review card.

### Required behavior

1. Accept a trusted D0_SYNTHETIC experiment request with:
   - Entity/requester identity;
   - exact task/writer identities;
   - exact bounded programming-task payload;
   - source/input locator and hash;
   - provider/model;
   - privacy class;
   - tools=[];
   - response bounds;
   - one-shot authority identity.

2. Remove dependence on correction-test fixed payload/task constants only through this new successor bridge. Do not weaken the installed predecessor in place.

3. Define one explicit deterministic request/plan/authority/attempt mapping shared by:
   - future live execution preparation;
   - expected review-result validation;
   - utility observation card.

4. Expected identities must originate from trusted request/plan/authority inputs, never from the untrusted provider result.

5. Preserve:
   - corrected reasoning policy;
   - response-shape persistence before normalization;
   - review-result v2 strict persistence/readback;
   - use-once ledger;
   - calls=1;
   - retries=0;
   - fallback=none;
   - tools=none;
   - current model and existing response/time bounds unless an exact incompatibility makes that impossible;
   - project_acceptance=NOT_GRANTED;
   - project_state_mutation=false.

6. Add a distinct REAL_PILOT observation-card mode. It must not masquerade as OFFLINE_FIXTURE or D0_SYNTHETIC_FIXTURE.

7. Real-pilot card must support:
   - baseline and assisted active/elapsed time;
   - cycles;
   - rework count/time;
   - common quality rubric/evidence;
   - mandatory requester decision and evidence;
   - provider latency when independently evidenced;
   - usage/cost evidence when available;
   - unknown usage/cost remaining unknown/null, never silently zero;
   - billed cost unknown without billing evidence.

8. No completed utility verdict without requester review.

9. No automatic project application or project acceptance.

## Required offline verification

Use synthetic fixtures only. No provider call.

Tests must prove at minimum:
- exact identity mapping is shared across prepared future live plan, expected review validation and REAL_PILOT card;
- wrong request/task/writer/authority/attempt identities fail closed;
- fixture evidence cannot be relabeled as real pilot evidence;
- real-pilot evidence cannot be accepted by fixture-only path;
- review-result tampering fails;
- missing requester review cannot yield completed utility verdict;
- unknown cost remains unknown;
- independently supplied latency may remain present while cost is unknown;
- function/tool/unknown output restrictions remain delegated to the corrected validator;
- second/replayed use-once attempt is rejected;
- no network/provider/credential/host/deployment path is exercised by tests.

Publish immutable package with manifest/checksums and deterministic test evidence.

## Hard boundaries

provider_calls=0
provider_requests_submitted=0
network=0
credential_value_reads=0
host/systemd mutation=0
deployment=0
standing authority=NOT_GRANTED
historical authority replay=0
current utility one-shot authority consumption=0
project_acceptance=NOT_GRANTED
production_acceptance=NOT_GRANTED
automatic project-state mutation=0

Do not start baseline or the actual utility experiment inside this implementation task.
Do not create another provider-call authority.
Do not request duplicate OPERATOR approval for the already unspent one-shot authority.

## Required terminal

PASS_KOD_BOOSTER_UTILITY_PILOT_LIVE_EVIDENCE_BRIDGE_R01_READY_FOR_SIS_VERIFY

or exact BLOCKED_*/FAIL_*.

Route result to KOO and SIS through Exchange Gate.

After KOD PASS stop. SIS must independently verify the exact immutable bridge non-live before any provider submission.

For RED, provide a concise human-readable journal-source only if the implementation adds a meaningful event beyond the already routed pre-call blocker story.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: READY_FOR_BOUNDED_NON_LIVE_BRIDGE_IMPLEMENTATION
