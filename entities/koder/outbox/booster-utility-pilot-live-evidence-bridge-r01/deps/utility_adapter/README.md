# Локальный адаптер пилота полезности Booster r0.1

Этот candidate связывает ограниченный запрос КОДЕРА, сохранённый ответ и обязательную проверку requester с отдельной карточкой измерений. Он не обращается к провайдеру и не запускает настоящий пилот. Все примеры — искусственные D0 fixtures; их время, качество и экономия не являются измерениями реальной работы.

## Использование без сети

Из каталога пакета:

```sh
python3 -B run_tests.py
python3 -B pilot_adapter.py --case fixtures/case.json --review fixtures/review.synthetic.json --output local-card.json
```

У адаптера нет режима live, параметров credentials, host или deployment. Путь output предназначен только для локального scratch; не указывать системные файлы. Не запускать legacy CLI из deps. Эти immutable dependencies включены для проверки точных байтов; используются только перечисленные ниже функции/структуры, без Gateway/Runtime/LiveWorker.

## Что переиспользовано

| Источник | Используемая часть |
|---|---|
| Entity booster runtime r0.2 | BoosterRequest, Authority(REPLAY_ONLY, false), validate_request |
| Corrected review_result_store.py | read_and_validate, persist_atomic; для генерации synthetic fixture — normalize_openai_result |
| Authoritative benchmark B | Usage и estimate_cost; старые model sweep, live switch и executor не вызываются |

Все три файла deps byte-identical исходникам. При несовпадении SHA-256 import блокируется. Нормализатор, транспорт, общий orchestrator и хранилище не переписаны. Установленный host runtime не изменён.

## Формат и доверенная сторона

case.json содержит ровно request, expected_review_sha256, observations, requester_review. Это доверенный вход, который формирует requester, а не провайдер. В реальном будущем использовании локальный caller должен контролировать этот файл, рубрику и источник expected hash; данный offline adapter не удостоверяет личность человека и не предоставляет live authority.

Request повторяет поля существующего BoosterRequest. Этот candidate ограничен текущим exact KOO task, KOD writer v0.5, OpenAI/gpt-5.6-luna, synthetic_only, tools=[], fixture://utility-r01/. Payload целиком включает синтетические данные и вопрос; source_sha256 = SHA-256 UTF-8 payload. Лимит request reuse берётся из r0.2. Fixture max_output_tokens=128 — только offline параметр, не изменение лимита установленного live runner (64).

Expected identity никогда не извлекается из review-result. prepare(request) детерминированно вычисляет:

1. request_sha256 = hash(domain + полный canonical request);
2. plan_sha256 = hash(domain + request_sha256 + offline plan);
3. authority_sha256 = hash(domain + task/writer + request/plan + NOT_GRANTED);
4. attempt_key = hash(domain + request/plan/fixture-authority).

Canonical JSON: UTF-8, sorted keys, compact separators, no NaN. Domain prefix: wb.booster.utility_pilot.offline.v1. Это отдельное соответствие идентификаторов. Оно не равно legacy Gateway, live-prep или test-runner mapping. authority_sha256 здесь означает identity синтетического разрешения на offline fixture, а не provider authority. Повторная локальная проверка не является replay live one-shot.

Перед чтением review JSON проверяется доверенный exact-file SHA-256. Затем pinned corrected read_and_validate проверяет request/attempt/plan/authority/task/writer/provider/model, структуру и хеши review-result v2. Provider content никогда не исполняется.

## Review и измерения

Карточка связывает полный набор ожидаемых identities, exact review-file SHA-256 и review-payload SHA-256. Фиксируются baseline и assisted:

- active_seconds = preparation + work + requester review + rework;
- elapsed_seconds включает ожидание, не меньше active_seconds;
- cycles: один кандидат → проверка requester → решение;
- rework_count и rework_seconds;
- одна и та же рубрика качества и fixture evidence;
- provider latency и cost evidence отдельно от полного elapsed времени.

requester_review=null сохраняет PENDING_REQUESTER_REVIEW: utility_verdict/comparison отсутствуют. Заполненное решение требует matching Entity, accept_as_candidate / needs_rework / reject, reason и evidence. Даже accept_as_candidate оставляет project_acceptance=NOT_GRANTED, project_state_applied=false, real_utility_demonstrated=false.

Для completed synthetic review карточка выводит baseline-minus-assisted изменения времени, циклов и переделок. Качество остаётся отдельной общей рубрикой: уменьшение времени не означает улучшения при ухудшении качества. N=1 fixture ничего не говорит о реальной эффективности. В будущем до пилота нужно заморозить рубрику/stop criteria и baseline до просмотра ответа; учитывать эффект обучения. Без Booster означает без дополнительного вызова Booster, а не без модели requester.

Cost kind=unknown требует usage/price/evidence/latency=null, estimated/billed cost также null. synthetic_estimate требует полных неотрицательных целочисленных usage, включая cached_input_tokens, согласованного total, fixture price snapshot и evidence. Arithmetic reuse estimate_cost; fixture ставки — произвольные тестовые числа, не реальные тарифы. Billed cost всегда неизвестна. Нет подстановки missing cache=0. Нет финансовых или billing операций.

## Persistence и strict readback

save_card использует существующий persist_atomic, рассчитывает expected exact-file hash и перечитывает карточку. read_card получает hash от доверенного producer/caller, проверяет его и заново строит ожидаемую карточку из request, проверенного review-result и записанных observations/reviewer decision. Изменение derived status/cost/flags/hash блокируется. Сами observations — утверждения requester, не доверенная телеметрия и не автоматически доказанная полезность.

## Fixtures и границы

fixtures/protocol.json определяет искусственные baseline/assisted outputs, рубрику и trace meanings. fixtures/case.json + review.synthetic.json + card.synthetic.json образуют один пример. build_fixture.py воспроизводит первые два файла через существующий corrected normalizer.

Review-result v2 содержит provider_calls=1, поскольку это обязательное поле существующей схемы моделируемого ответа. Это **синтетическое протокольное значение**, а не реальный вызов; fixture filename/protocol/card фиксируют D0_SYNTHETIC_FIXTURE и фактические provider_calls=0. Не использовать этот JSON как live evidence.

run_tests.py запрещает sockets, subprocess, os.system, реальные environment reads и файловый доступ вне пакета/временного scratch (read-only stdlib imports разрешены). Для argparse возвращаются фиксированные не-секретные значения locale/terminal. Число запрещённых попыток проверяется отдельно, чтобы пойманное исключение не скрывало обращение наружу.

Итог candidate — готовность к независимой non-live проверке SIS. Host install, новый provider call, реальные project data и project acceptance требуют отдельных разрешений и не предоставляются этим пакетом.
