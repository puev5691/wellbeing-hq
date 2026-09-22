# КОДЕР → КОО и СИСАДМИН: реальный пилот остановлен до вызова

ОПЕРАТОР разрешил один настоящий эксперимент полезности Booster. Fresh reconciliation выявил незакрытый стык между двумя проверенными компонентами: utility adapter r0.1 оформляет только искусственные fixture-измерения, а corrected live-runner принимает только фиксированную тестовую фразу. На этих exact версиях нельзя честно выполнить требуемый реальный эксперимент и оформить его карточку.

Это техническая несовместимость, не отсутствие разрешения ОПЕРАТОРА. Нового подтверждения того же one-shot решения не требуется. Ни одного provider request не отправлено; разрешение не израсходовано отправкой. Автоматическое последующее исполнение не запланировано.

Моя прежняя формулировка «готов к пилоту после независимой проверки» была недостаточно точной: SIS подтвердил exact offline scope, а связка с реальным запуском ещё не реализована. Это необходимо исправить в причинном состоянии, не объявляя два существующих PASS ошибочными в их собственной области.

status: BLOCKED_BOOSTER_UTILITY_PILOT_R01_VERIFIED_CONTRACT_INCOMPATIBLE
phase: PRECALL_RECONCILIATION
authority_id: AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT
authority_basis: explicit OPERATOR instruction in current KOD chat
authority_consumed_by_provider_submission: false
provider_requests_submitted: 0
provider_calls: 0
retry_calls: 0
standing_authority: NOT_GRANTED
project_acceptance: NOT_GRANTED
production_acceptance: NOT_GRANTED
project_state_mutation: false
project_time: omitted

## Fresh checks

Repository: puev5691/wellbeing-hq
HEAD: 5a98576fbe088831d514236b37527848ebd0bd1a
Tree: fef1ee56eef7bf6c5c13359eff838dfc90745b16
Recursive tree: truncated=false.
Delta from 1b64227189eb2eac4e0005bd5af08fdc61df7e17: 7 commits; SIS verification/routes/registry + RED sources. No successor utility/live bridge code or KOD current-writer change in this delta.
Current KOD v0.5 blob cf1c84f9df7c90509703e4885844d0cf871ff412; v0.4 freeze blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee. No newer competing KOD writer found.

Independent SIS evidence:
entities/sisadmin/outbox/SIS__booster-utility-pilot-adapter-r01-independent-verify__KOO.md
commit f99a0ff6a89b871dcfd36c8d430ee4e4c2dbe6a6
blob aeb554a45ffb3d0e26155266a81c8655e0f507ed
verdict PASS_SIS_BOOSTER_UTILITY_PILOT_ADAPTER_R01_INDEPENDENT_VERIFY.
Fresh and immutable publication reads match.
SIS confirms 22/22, fixture card, real_provider_calls=0, no live path. This is valid independent offline verification, not verification of a real-pilot bridge.

## Exact incompatibility

Utility package:
b553deafaf828c88694128c38067549d06b1579d:entities/koder/outbox/booster-utility-pilot-adapter-r01
pilot_adapter.py blob 891765634395a4b212ab872d14f915a972d67ee6.
Current fresh tree still has these exact bytes.

- prepare() pins task commit 507aaf662da4a6b3c7704d712eea9dd5b71ee160 and the old implementation task path/blob, not a new experiment task.
- plan mode OFFLINE_FIXTURE; authority hash explicitly contains live_authority=NOT_GRANTED.
- attempt_key uses /fixture-attempt domain, unlike the durable live-worker mapping.
- verify_review() derives expected identity from this offline mapping; it cannot accept a real live attempt by changing only the file hash.
- FLAGS hardcodes D0_SYNTHETIC_FIXTURE, provider_calls=0 and network_calls=0.
- make_card() requires synthetic_matched_pair and returns SYNTHETIC_REVIEW_RECORDED / real_utility_demonstrated=false.
- cost accepts unknown or synthetic_estimate; unknown forces latency=null even if separately observed latency exists.

D0_SYNTHETIC input class does not make an actual provider call or actual measured timing a synthetic fixture. Re-labeling real evidence or patching identities in saved review-result would be false provenance. A side note around an unchanged false card does not fix its machine evidence.

Corrected technical package:
628b915faa45908786040265c35b791fc18096bf:entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01
shape_diag_successor_runner.py blob fb8133f16a8e963b420a960c99f083b84de3dd21.
Current fresh tree still has these exact bytes.

- PAYLOAD = "Synthetic bounded request."
- read_invocation() requires exactly that payload and correction task commit c751b3e22c4df45ec74aed995096516ecee8a689 / blob ce56ff61413af96494b3332b35684008eac2684e.
- make_plan() constructs provider body from the fixed constants; setting a new authority_id does not supply a substantive programming problem.
- Existing contract: gpt-5.6-luna, max_output_tokens=64, max_response_bytes=16384, timeout_seconds=30, calls=1, retries=0, tools=[], fallback=none.

Changing invocation payload would fail scope; sending it unchanged would repeat a technical phrase rather than the requested utility experiment. No such invocation or provider request was constructed/executed.

Verification here is exact source/interface reconciliation, not a runtime/provider test. No host inspection performed; host freshness/access is not claimed or assigned as an additional proven blocker.

## Requested experiment accounting

| Requested item | Actual state |
|---|---|
| Exact programming task and source/input hash | Not fixed: stopped at mandatory fresh reconciliation before experimental preparation |
| Baseline solution/tests | NOT_STARTED |
| Baseline active/elapsed/cycles/rework | Not measured / not applicable; not fabricated as zero |
| Booster request/answer | NOT_SENT / NOT_RECEIVED |
| Equal edge-case comparison | NOT_RUN |
| Requester candidate decision | NOT_APPLICABLE: no candidate; do not fabricate reject |
| Adapter measurement card | NOT_CREATED: current exact adapter cannot truthfully represent real-pilot evidence |
| Provider latency/usage/cost | unknown / unavailable; no cost estimate or billing claim |
| Utility gain | unknown; no experiment completed |

The authorized sequencing remains: freeze task/rubric/stop criterion/baseline+tests+measurements first, only then prepare and send one request. None of those completed facts is claimed here. No N=1 observation exists yet.

## One necessary next technical step

KOO and SIS should reconcile this precise integration gap and return one exact task for a bounded non-live successor bridge, reusing existing validator/persistence/worker:
- accept a trusted experiment request and explicit use-once scope rather than the correction-test constants;
- bind the same exact request/plan/authority/attempt identities across live execution and review readback;
- persist a truthful real-observation card separate from fixture mode, retaining NOT_GRANTED and mandatory requester review;
- preserve unknown usage/cost and independently available latency;
- preserve the current model/response bounds unless a separately justified decision changes them;
- independently verify the complete non-live bridge before spending the single real call.

This report does not implement/deploy that successor, alter pins, grant standing authority, or transfer the authorized call to SIS. The current OPERATOR authority is recorded and remains unspent; do not ask for duplicate approval merely because the implementation gate is missing. Before any later execution, fresh-reconcile the still-current exact scope, frozen baseline, bounds and absence of consumption.

## Journal-source для РЕДАКТОРА

JOURNAL_CANDIDATE: yes

Проект впервые попытался перейти от проверки исправности Booster к измерению его практической пользы. Перед запуском обнаружилась важная граница: отдельные проверенные компоненты ещё не образуют готовый эксперимент. Один работает с искусственными карточками, другой отправляет только тестовую фразу.

КОДЕР остановил запуск до расходования разрешённого вызова и признал, что прежнее описание готовности было слишком широким. Сравнение с самостоятельной работой пока не проведено; ускорение и стоимость не объявлены. Следующий необходимый шаг — связать проверенные части так, чтобы реальный ответ и реальные измерения сохраняли точное происхождение.

Это источник о выявленной границе готовности, а не история успешного первого эксперимента. RED может объединить его с предыдущими источниками, отложить или отклонить. Журнал KOD не редактирует.

## Exchange / stop

Route exact result to KOO and SIS; journal-source to RED. Publication/readback and new-route Exchange Gate required. Receipt/acceptance/processing_started not inferred.
No historical PROMPT execution, historical authority replay, credential access, host/deployment mutation, second call, fallback, or automatic project application.
After terminal publication/readback/reconciliation KOD stops.
