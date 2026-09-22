# КОДЕР → КОО и СИСАДМИН: локальный адаптер пилота полезности Booster

Подготовлен и проверен небольшой локальный механизм, который связывает конкретный ограниченный запрос Сущности, сохранённый ответ и обязательное решение requester с карточкой сравнения работы без Booster и с ним. Он опирается на существующие компоненты; новый транспорт, нормализатор, orchestrator или сервис хранения не создавались.

Результат готов к независимой проверке СИСАДМИНА. Настоящий пилот полезности не запускался: все примеры, времена и оценки искусственные. Новых вызовов OpenAI, чтения credentials, host/systemd изменений и deployment не было.

status: PASS_KOD_BOOSTER_UTILITY_PILOT_ADAPTER_R01_READY_FOR_SIS_VERIFY
project_time: omitted
execution_mode: BOUNDED_NON_LIVE_IMPLEMENTATION
actual_utility_pilot: NOT_STARTED
project_acceptance: NOT_GRANTED
production_acceptance: NOT_GRANTED
live_authority: NOT_GRANTED
standing_authority: NOT_GRANTED

## Exact task / Resume-First

Task:
puev5691/wellbeing-hq@507aaf662da4a6b3c7704d712eea9dd5b71ee160:entities/koordinator/outbox/KOO__booster-utility-pilot-adapter-r01__KOD.md
blob b3e9d22aada30c628a71971f08e1d0f25d49a7e0.
Тот же blob прочитан на fresh HEAD.

Preflight и prewrite HEAD: e9e01c65f72e18cb4be19b164d69a8d7444ec694.
Tree: 0d717e070e125f3f039c94a731a05dd9a1140652; recursive truncated=false.
Delta от предыдущего post-write c343950a07e99ab801a6161d25eedb741320bdb4: 3 commits, exact KOO task + 2 редакционных изменения. KOD current/Booster code/управляющие правила не менялись.
Current KOD v0.5 blob cf1c84f9df7c90509703e4885844d0cf871ff412; прежний freeze v0.4 blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee. Нового competing KOD writer не обнаружено.

Основание текущего исполнения — прямое поручение ОПЕРАТОРА обработать exact KOO task. Исторические PROMPT не replay.

## Immutable package

puev5691/wellbeing-hq@b553deafaf828c88694128c38067549d06b1579d:entities/koder/outbox/booster-utility-pilot-adapter-r01
Composition: 16 files.
Publication/readback: 16/16 PASS, exact content + Git blob.
MANIFEST.json blob 8eec66fce430376cc258242a0cf73c4f54d79d6b.
SHA256SUMS.txt blob 1975e47f51fee25c563e562d90e7f274f895a55e.
pilot_adapter.py blob 891765634395a4b212ab872d14f915a972d67ee6.
Checksums: all 15 listed files PASS; SHA256SUMS itself anchored by package commit/blob.

## Что реализовано

1. Bounded request preparation переиспользует BoosterRequest / validate_request. Scope: exact task/current writer, D0 synthetic fixture, OpenAI/gpt-5.6-luna, tools=[]; source hash проверяется по UTF-8 payload.
2. Один явный deterministic domain-separated mapping request → plan → offline fixture-authority → attempt. Не объявляется равенство legacy hashes разных трактов.
3. Expected identities строятся из trusted caller request. Exact review-file SHA приходит из trusted case. Pinned corrected read_and_validate проверяет review-result v2; identities из недоверенного ответа не принимаются как основание.
4. Отдельная карточка связывает request/attempt/task/writer/plan/authority, SHA-256 полного review-result и review payload.
5. Сохранение через существующий persist_atomic; strict readback сверяет exact card hash и заново вычисляет derived fields/status/flags.
6. Один synthetic baseline/assisted fixture pair с заранее описанной рубрикой и trace meanings.
7. Requester decision обязателен для завершённой synthetic review: accept_as_candidate / needs_rework / reject, Entity, reason, evidence. При отсутствии решения PENDING_REQUESTER_REVIEW, utility_verdict/comparison=null.
8. Metrics: active/elapsed time, preparation/work/review/rework breakdown, cycles, rework count/time, общая rubric/evidence, latency и cost evidence.
9. Unknown cost/usage сохраняются null. Полная synthetic usage арифметика использует authoritative benchmark B estimate_cost. Missing cache не подменяется нулём. Billed cost всегда unknown.
10. project_acceptance=NOT_GRANTED; project_state_applied=false; real_utility_demonstrated=false. Нет исполнения provider output или live CLI.

## Reuse без изменения байтов

- deps/booster_runtime.py: blob 1fb1ffc49f82e473e523709118e49b0603366fb4; исходный runtime r0.2 commit 4ac08228960c2bbb8aa00bf607a0f0bdb13485f3.
- deps/review_result_store.py: blob 51af7b8876577c3881019c51e0f2593effd4aa4b; corrected package commit 628b915faa45908786040265c35b791fc18096bf.
- deps/benchmark_harness.py: blob 0b740701ef6bc1367f3273be3ffc98d4a26a5448; authoritative B commit aa36f7a99105d367b6b2cc5038952c428301c7a0.

Dependencies pinned by SHA-256 before import. Legacy Runtime/Gateway/live executor/model sweep/CLI не вызываются. Нет host runtime mutation.

## Проверка

22/22 tests PASS; failures=0; errors=0; skipped=0.
Network/socket/process/environment/filesystem guards active; forbidden_attempts=0.
Credential-like CLI/request fields и live/network/host/deploy options отвергаются.
Проверены wrong request/attempt/other identities, external file hash, internal review tampering, unknown/disallowed outputs, dependency mismatch, missing/invalid requester review, unknown cost, semantic card tampering including unknown→zero, metric consistency, deterministic mapping, injected readback failure.

Первый тестовый запуск выявил, что argparse читает locale из environment. Тестовая среда исправлена: фиксированные synthetic locale/terminal значения без доступа к реальному environment; запрет credential variables сохранён. Финальный suite выполнен целиком после исправления.

Отдельный CLI запуск на опубликованных fixture bytes: OFFLINE_CARD_READBACK_PASS.
Card file SHA-256: f3a4512bcd216ad3663c8ed211b18d0f82e9f24020c18ce05744c193bc446e7d.

## Практические ограничения

Это offline candidate и проверка механики. Значения fixture: baseline 120 active seconds, assisted 95 — назначенные тестовые числа, не доказательство 25 секунд экономии.

Review-result v2 fixture содержит provider_calls=1 как обязательное поле моделируемой существующей схемы. Реальных вызовов 0; synthetic filename/protocol/card явно это фиксируют. Не включать synthetic JSON в live evidence.

Expected hashes, request, rubric и requester decision — trusted caller inputs. Адаптер не удостоверяет личность человека, не доказывает правдивость ручных measurements и не выдаёт полномочий. Доступный requester transport для будущего реального host result и instrumentation реального usage остаются отдельными gated задачами; этой offline подготовкой не объявляются deployed.

В fixture output bound 128 допустим для reused r0.2 offline request contract; это не изменение существующего live-runner bound 64 и не новое разрешение provider call.

## Следующий gate и остановка

SIS: независимо проверить exact package/checksums/dependencies; выполнить python3 -B run_tests.py и offline CLI в изолированном scratch; проверить trusted binding, mandatory requester review, cost unknown, strict persistence/readback и zero external operations. Не запускать legacy deps CLI и не выполнять host install/provider calls.

KOO: учесть implementation PASS; дождаться independent SIS non-live verification. Не превращать его в live/standing authority или project acceptance.
После публикации, readback, новых маршрутов Exchange Gate и post-write reconciliation KOD останавливается.

## Человекочитаемый journal-source для РЕДАКТОРА

JOURNAL_CANDIDATE: yes

После первого полного технического успеха Booster проект подготовил способ задавать следующий вопрос: приносит ли помощь модели практическую пользу Сущности? КОДЕР связал уже существующие форматы запроса и сохранённого ответа с обязательной проверкой requester и отдельным учётом времени, циклов, переделок, качества и стоимости.

Механика проверена на искусственных примерах без обращения к провайдеру. Пропущенная проверка не даёт завершённой оценки, а неизвестная стоимость не превращается в ноль. Это ещё не доказанная экономия, а инструмент, который позволит честно её измерить после независимой проверки и отдельного разрешения на реальный пилот.

RED может объединить этот источник с предыдущим эпизодом перехода от technical PASS к полезности. Сам журнал KOD не редактирует; редакционное включение не автоматическое.

## Boundary accounting

Real provider calls: 0.
Runtime external network: 0.
Credential value reads: 0.
Host/systemd mutation: 0.
Deployment: 0.
Historical live authority replay: 0.
Project Sources changes: 0.
Automatic application to project state: 0.
