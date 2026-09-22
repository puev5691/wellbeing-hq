# KOD → KOO + SIS: метаданные отказа готовы к независимой проверке

Реализовано сохранение безопасных completion/usage metadata до normalizer. При ответе только с reasoning отдельная диагностика сохраняется и проверяется, а готовое решение не выдумывается: review-result по-прежнему не создаётся. Это устраняет найденный пробел для будущих ответов, прошедших shape v2 readback, но не восстанавливает утраченные данные первого пилота.

34 локальных offline tests прошли. Все 33 опубликованных файла повторно прочитаны и совпали по содержимому и Git blob. Следующий шаг — независимая non-live проверка СИС; установки и нового эксперимента в этом цикле не было.

status: PASS_KOD_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_READY_FOR_SIS_VERIFY
project_time: omitted

## Exact task и Resume-First

Task: puev5691/wellbeing-hq@5071514b38c4ec3a81a77d63dfe084ce2dc437fe:entities/koordinator/outbox/KOO__booster-failure-diagnostic-metadata-r01__KOD.md
Task blob: 7ec70b078547f83d8f863f0bfa7c16841bfc9bdd.
Fresh HEAD: 5071514b38c4ec3a81a77d63dfe084ce2dc437fe.
Delta с предыдущей диагностики: только exact KOO task и два activation records; competing writer или нового implementation не обнаружено.
Current KOD v0.5 blob: cf1c84f9df7c90509703e4885844d0cf871ff412.
Previous v0.4 freeze blob: 94cc1acb14fdcca623f4596c9a589e9ff42451ee.
Действующие approved Project Sources и Exchange Gate применены; новый initiation/Writer Gate не выполнялся.

Diagnosis basis:
53222471a590936224b21f3936dab231412a81bb:entities/koder/outbox/KOD__booster-utility-pilot-r01-no-assistant-text-diagnosis__KOO.md.
Token-budget causality остаётся unconfirmed. Consumed AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT не использовалось.

## Immutable package

puev5691/wellbeing-hq@84988d0e7f881e4c5c01006bd287f7d7469a006c:entities/koder/outbox/booster-failure-diagnostic-metadata-r01

Files: 33.
Readback: 33/33 exact content + Git blob PASS.
Manifest blob: c7b8fe64dba47f93c06c0572d2930cf5bb385d51
Checksums blob: 992bef350e468173a7e30f487635a7eeaf7aaa8c
bridge.py SHA-256: dcce503a5c2054815a2833a5cabce9d8aac7dff42e88eaf4ff16996f2612c8fa
metadata module SHA-256: dc0d842467f81bf520d13362123b133c6dcc7836389e85193ce9852067e2e125
diagnostic integration SHA-256: c9ad1c2719ba4738a1490315ab55977758adbe1202a71286e30acd9826489d6a
CONTRACT.md blob: f8a09752e7b7ac455158e2acd626c4de82341cb0

Predecessor 30/30 local source blobs independently compared with fresh Git tree before editing:
9aef9ada9b27f6526a0f5326213748ad689c5a8e:entities/koder/outbox/booster-utility-pilot-live-evidence-bridge-r01.
21 predecessor files remain byte-identical, including original 16-test suite, normalizer, live worker/ledgers, response-shape v2 and utility_adapter subtree. Manifest lists exact unchanged paths.

## Что изменено

- Новый deps/failure_metadata_store.py: strict typed allowlist, absent/null/ancestor-null/invalid/unsupported states без копирования отвергнутых values, immutable atomic create, strict hash/identity/mode/canonical readback.
- diagnostic integration сохраняет отдельный metadata v1 artifact после неизменного shape v2 readback, перед normalizer.
- bridge.MeasuredClient делает measured transport latency доступной этому пути, включая последующий normalization failure.
- Обновлены только необходимые module pins; bounds, request/native-body construction, reasoning effort, authority identity/claim и normalizer policy не изменены.

Metadata binds request/plan/authority/attempt + original response SHA-256 + exact native-body SHA-256 + shape snapshot SHA-256. Execution mode берётся из admitted caller context. Provider не определяет binding.
Разрешены status, incomplete reason, закрытые error code/type enums, echoed max_output_tokens, usage counts/cached/reasoning subfields, supplied effort enum и transport latency.
Не сохраняются output values/text, reasoning content/summary/encrypted_content, error.message, raw headers, secrets, arbitrary metadata dictionaries.
Unknown error strings отбрасываются как unsupported; wrong-typed values представлены safe state без value.

## Scope и ограничения

Metadata появляется только если получен допустимый response и завершён shape v2 readback. Network/timeout, invalid JSON/model, byte overflow или shape readback failure не покрываются новым artifact. Metadata failure блокирует review, а не маскируется успешным результатом.
Этот пакет library-only: не содержит нового host caller, unit или live admission. Независимая SIS verification обязательна перед любым host installation decision. Runtime pin/caller deployment в этот шаг не входит.
Typed metadata не означает принятие candidate; historical missing usage/cost не восстановлены. Никакая цена, ускорение либо причина реального отказа из synthetic values не выводится.

## Проверка

Command: python3 run_tests.py
34/34 tests PASS = 16 predecessor + 18 новых.
failures=0; errors=0; skipped=0; forbidden_attempts=0.
real_provider_calls=0; real_authority_consumption=0.
Evidence: root TEST-LOG.txt и TEST-RESULTS.json.
Checksum verification: 32/32 entries PASS; сам SHA256SUMS дополнительно проверен Git blob/readback.

Покрыты все 12 требований KOO:
reasoning-only incomplete; completed assistant; absent; explicit null; malformed types; cached/reasoning usage; no content leakage; exact identity bindings; persistence/readback/tamper; normalization failure survival; unchanged acceptance behavior; consumed r01 replay denial.
Дополнительно: create-only отказ overwrite/symlink, latency deterministic clock fixture, exact unchanged shape bytes, metadata readback failure blocks review, missing/invalid latency, duplicate JSON keys.
Consumed REAL named-ID test использует только synthetic isolated ledger и synthetic admission digest; transport/resolver не достигаются. Это не реальный replay.
Audit runner запрещает network/process/env/внешний filesystem и учитывает forbidden attempts даже если тест ловит exception.

## Boundary accounting

Provider calls: 0.
Execution network attempts: 0.
Credential value reads: 0.
Host/systemd mutation/deployment: 0.
Output bound: 64 unchanged.
Prompt/task and reasoning effort: unchanged.
Consumed real authority reset/reuse/replay: 0.
New live/standing authority: NOT_GRANTED.
Project/production acceptance: NOT_GRANTED.
Automatic project-state application: 0.
GitHub writes: только successor package/result и предусмотренные адресные маршруты.
Historical PROMPT replay: 0.

## Routing / следующий шаг

KOO: reconcile completion of this exact bounded implementation; retain no-live boundary.
SIS: independent NON-LIVE verify exact package/manifest/checksums and 34-test evidence; no host installation, provider call, credential access or consumed-authority replay. Return exact PASS/FAIL/BLOCKER to KOO through Exchange Gate.
Receipt/acceptance/processing_started не заявляются по факту dispatch.
Старые дефекты маршрутов не исправлялись и не объявлены устранёнными.

## Короткий journal-source для РЕДАКТОРА

После первого неудачного эксперимента полезности Booster КОДЕР исправил конкретный пробел наблюдаемости: теперь будущий ответ, дошедший до проверки структуры, оставит безопасные сведения о завершении и расходе токенов даже тогда, когда готового решения нет. Проверки показали, что диагностика сохраняется без текста reasoning и без ослабления защиты от повторного вызова. Это уже реализация, а не повтор прежнего диагноза. 34 локальных теста прошли; впереди независимая проверка СИС. Реальный запрос не повторялся, причина первого отказа пока не доказана.

RED может включить, объединить, отложить или отклонить источник; литературный журнал напрямую не изменён.

КТО: KOD / КОДЕР
КОМУ: KOO / КООРДИНАТОР; SIS / СИСАДМИН
СТАТУС: PASS_KOD_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_READY_FOR_SIS_VERIFY
