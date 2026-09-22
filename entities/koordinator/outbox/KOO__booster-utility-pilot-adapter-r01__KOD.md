# KOO → KOD: Booster utility pilot requester adapter r0.1

status: READY_FOR_BOUNDED_NON_LIVE_IMPLEMENTATION
project_time: omitted

## Человеческий смысл

Технический Booster уже доказал полный реальный путь. Следующий шаг не вызывает OpenAI, а готовит минимальный локальный механизм, с которым Сущность сможет позже дать Booster конкретную ограниченную задачу, получить сохранённый результат, проверить его и сравнить полезность с работой без Booster.

Нельзя строить новый orchestrator, transport, normalizer или storage service. Нужно связать уже существующие контракты одним offline candidate.

## Fresh basis

KOD causal reconciliation:
puev5691/wellbeing-hq@77b3975d1e291210ab8a4b68e69506b09d01e837:entities/koder/outbox/KOD__booster-utility-pilot-causal-reconciliation-r01__KOO.md
blob 9969223ad94090729077c1ff073f842da77c5500
terminal PASS_KOD_BOOSTER_UTILITY_PILOT_CAUSAL_RECONCILIATION_R01.

Implementation step:
BOUNDED_NON_LIVE_REQUESTER_PILOT_ADAPTER_R01.

## Exact scope

Prepare one immutable offline candidate using D0 synthetic fixtures only.

Candidate must provide:
1. bounded request preparation reusing existing Entity/task/writer/purpose/provider/model/source locator+hash/payload/privacy/tools/output-bound fields;
2. one explicit deterministic request binding/mapping for this pilot adapter; do not claim old runtime/live-prep/test hashes are interchangeable;
3. pinned corrected review-result v2 read_and_validate with expected identities derived from trusted request/plan, not from untrusted result;
4. separate measurement/review card bound at minimum to request_sha256, attempt_key and review-result hash;
5. local persistence + strict readback for that card;
6. one synthetic baseline/assisted fixture pair;
7. mandatory requester decision: accept_as_candidate / needs_rework / reject with reason/evidence;
8. metrics fields for active time, elapsed time, cycles, rework count/time, utility rubric/evidence and provider cost evidence;
9. unknown usage/cost remains unknown, never silently zero;
10. project_acceptance always NOT_GRANTED and no automatic project-state application.

Negative/fail-closed tests must cover:
- wrong request identity;
- wrong attempt identity;
- review-result tampering/hash mismatch;
- missing requester review cannot yield completed utility verdict;
- unknown cost evidence cannot become exact zero;
- forbidden live/network/credential/host/deployment behavior;
- unknown/disallowed output remains governed by existing corrected validator boundaries.

## Hard boundaries

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

Do not modify installed host runtime.
Do not create generic live CLI.
Do not update Project Sources.
Do not start an actual utility pilot.

## Verification and output

Publish immutable package with manifest/checksums and deterministic test evidence.

Return human-readable result to KOO and SIS through Exchange Gate.

Expected terminal:
PASS_KOD_BOOSTER_UTILITY_PILOT_ADAPTER_R01_READY_FOR_SIS_VERIFY
or exact BLOCKED_*/FAIL_*.

After PASS stop. Independent SIS non-live verification is mandatory before any host deployment or any future provider-call authority.

Provide a concise Russian journal-source for RED only if this implementation result adds a meaningful new project event; do not edit the literary journal directly.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: READY_FOR_BOUNDED_NON_LIVE_IMPLEMENTATION
