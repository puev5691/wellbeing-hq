# Booster utility live-evidence bridge r0.1

Связка устраняет две несовместимости predecessor: фиксированный correction-test запрос и карточку, рассчитанную только на fixtures. Это отдельный non-live candidate. Установленный runtime и его ограничения не изменены. Реальный пилот и baseline в этой задаче не запускались.

## Проверка

```sh
python3 -B run_tests.py
```

Python 3.12 / Linux. Тесты работают в временном scratch, с fake client/resolver и OFFLINE_TEST authority. Тест REAL_PILOT card является чистой проверкой схемы на искусственно заданном доверенном receipt: он не вызывает execute в реальном режиме и не публикует искусственный receipt как реальное evidence.

## Переиспользование

deps содержит неизменённые exact bytes:

- final live_worker.py: existing bounded HTTP worker, hard deadline и DurableOneShotLedger;
- corrected diagnostic_reviewable_live_worker.py: shape persist/readback перед normalization, затем review v2 persist/readback;
- corrected response_shape_store.py, review_result_store.py, reviewable_live_worker.py;
- весь independently verified utility_adapter r0.1: переиспользуются metrics/rubric/phase checks и versioned cost estimator. Fixture-only path сохранён отдельно и не принимает реальные identities.

Новый bridge.py не содержит собственного HTTP transport, credential resolver, общего orchestrator или storage service. persist_atomic и strict review readback переиспользованы. Реальный вызов не является default: модуль не имеет live CLI, main или автоматического запуска; execute требует явно переданных trusted host capabilities.

## Доверенные входы и API

request_hash(request) проверяет request schema и вычисляет deterministic digest. Полный request включает Entity/role, exact Git task/writer, purpose, bounded payload, source locator/hash, provider/model, D0_SYNTHETIC/synthetic_only, tools=[], bounds, baseline_sha256. Payload включает вопрос и синтетические исходные данные, поэтому source hash = SHA-256 всего UTF-8 payload. Здесь нет correction-test task/payload constants. Writer ограничен действующим KOD v0.5.

prepare(request, authority, now_tick, trusted_authority_sha256, verify_ref) принимает independently admitted authority digest и callback точной Git проверки task/writer. Caller обязан получить эти доверенные значения из управляющего контура; брать их из provider output запрещено. verify_ref — проверка exact task и действующего writer, а не разрешение на network. Authority связывает полный request hash, task/writer, baseline hash, provider/model, privacy/tools/bounds, expiry и имя one-shot разрешения.

Для REAL_PILOT допускается только уже выданное AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT; код не выдаёт новое разрешение. Для тестового исполнения — отдельное TEST_ONLY_UTILITY_BRIDGE_R01. Формирование плана ничего не claim-ит и не расходует.

Сохранены exact limits: OpenAI/gpt-5.6-luna; output tokens=64; response bytes=16384; timeout=30; calls=1; retries=0; fallback=none; tools=[]; store=false. При недостаточном response bound будущий experiment должен завершиться фактическим failure/needs_rework без повторного вызова; этот candidate не повышает лимиты молча.

## Identity mapping

Canonical JSON = UTF-8, sorted keys, compact separators, no NaN.

1. Request hash: domain wb.booster.utility_bridge.v1/request + полный request.
2. Authority hash: полный independently admitted authority document.
3. Plan hash: domain /plan + request hash + native plan + authority hash + response/time bounds.
4. Attempt key: SHA-256 canonical {authority: authority_sha256, request: request_sha256, plan: plan_sha256}. Это **exact алгоритм существующего live_worker**, не отдельная fixture-формула.

Prepared WorkerPlan, corrected persisted review expected identities и observation card используют один identity object. Provider result не определяет expected identities. Исполняющий вызов prepare выполняется заново из trusted inputs: готовый изменённый dict не считается admission.

## Execute и use-once

execute требует trusted verifier, resolver, client, attest_execution(mode,client,resolver) и один канонический durable directory. Устанавливающий host caller должен подтвердить происхождение транспорта: REAL_PILOT только с admitted реальным клиентом; OFFLINE_TEST только с fake. Callback является доверенной границей host интеграции, не самосертификацией provider или полем запроса. В комплект не включена фиктивная функция «всегда разрешить» для реального host. Наличие API не означает host deployment/readiness.

Перед обращением к worker дополнительная reservation в authority.sqlite использует **существующий** DurableOneShotLedger и key от имени authority. Это не позволяет повторить тот же one-shot с другим request/plan при общем каноническом directory. Затем existing worker claim-ит attempt в attempts.sqlite, разрешает secret reference и обращается к переданному клиенту. Canonical resolver для будущего host остаётся на стороне существующей SIS integration; secret value в inputs/plan/receipt не помещается.

Reservation сохраняется при любом последующем исключении, включая resolver failure до отправки. Это консервативный execution guard, а не утверждение, что request уже отправлен: число actual submissions и причина отказа должны сверяться отдельно. Автоматического release/retry нет. Удалять ledger или менять directory ради повторного вызова нельзя. Тесты используют только временные TEST_ONLY ledgers, не текущую live authority.

Существующий corrected diagnostic worker сохраняет shape до нормализации и review v2 после; bridge проверяет attempt и exact review hash. Receipt сохраняет execution mode, identity, baseline hash, review hash, shape snapshot hash, submissions и latency от монотонного таймера вокруг transport boundary. Latency не включает baseline/request preparation/reviewer time.

## REAL_PILOT measurement card

make_card получает trusted receipt digest из verified producer/readback, request/authority admission inputs и original admission now_tick. Для анализа после истечения authority используется сохранённый admission tick, не новая execution admission. Receipt сам по себе не источник своего доверенного хеша.

REAL_PILOT требует совпадения execution provenance, receipt hash и полного identity. Card mode=REAL_PILOT, evidence_class=REAL_OBSERVATION, provider_calls=1. OFFLINE_TEST имеет TEST_FIXTURE/provider_calls=0/simulated_submissions=1. Смена метки в fixture разрушает trusted hash или admission mode и блокируется. Если контролирующий caller фальсифицирует одновременно trusted admission, attestation и trusted receipt digest, это выход за модель доверия: модуль не заменяет аутентификацию хоста или криптографическое удостоверение человека.

Baseline/assisted metrics сохраняют active time, elapsed time, cycles, rework count/time, phase totals, общую рубрику и evidence locator+hash. Вызов legacy metrics получает временный fixture placeholder лишь для URI-проверки; записанные реальные evidence не переименовываются. Baseline publication/freeze до отправки обеспечивает trusted orchestrating caller, request/authority/receipt/card связывают его exact hash.

Cost usage может быть partial/null. Без полной usage и price evidence estimated cost=null. Missing cached_input не считается 0. Latency остаётся в карточке независимо от неизвестной стоимости. Billed USD допускается только с отдельным billing evidence; иначе null. Источники и их содержательная достаточность — ответственность requester, не самооценка модели; tests используют искусственные тарифы. Никаких billing операций модуль не делает.

Requester review обязателен: matching Entity, accept_as_candidate/needs_rework/reject, reason, evidence. Без него utility_verdict/comparison=null. Любое решение сохраняет project/production acceptance=NOT_GRANTED, project_state_mutation=false, standing authority=NOT_GRANTED. N=1 не доказывает общего ускорения.

save_card/read_card повторно строят ожидаемую карточку из trusted inputs и проверяют exact bytes/hash. Candidate response никогда не исполняется и не применяется к проекту.

## Что ещё требует проверки

Следующий шаг — independent SIS non-live verification этого exact пакета. Затем fresh reconciliation существующего one-shot решения, реального host caller/transport attestation/канонических ledgers и доступности exact receipt для requester. Этот result не объявляет host integration установленной или проверенной и не расходует provider call.
