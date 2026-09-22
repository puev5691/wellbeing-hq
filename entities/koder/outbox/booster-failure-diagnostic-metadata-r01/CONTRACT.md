# Exact contract: failure metadata v1

## Порядок и scope

Прежние authority reservation и attempt claim → injected transport → unchanged shape v2 persistence/readback → metadata v1 atomic create/readback → unchanged normalizer → прежний review-result.

Path: STATE/metadata/<attempt_key>.metadata-v1.json. Shape v2 не переписывается новым модулем. Reasoning-only output по-прежнему приводит к BLOCKED_PROVIDER_RESPONSE без review/candidate, metadata остаётся. Metadata write/readback failure останавливает путь до normalizer: BLOCKED_FAILURE_METADATA. Повторная попытка блокируется consumed ledger до транспорта.

Scope ограничен ответами после успешного shape v2 readback. Для timeout, invalid JSON/model, превышения byte bound или shape readback failure metadata не обещается: принятого response/shape нет. Никакие произвольные исключения не превращаются в успешный результат.

## Exact schema

schema: wb.openai.booster.failure_metadata.v1
Canonical UTF-8 JSON: ensure_ascii=False, sorted keys, compact separators, no NaN, завершающий LF. Максимум 16384 bytes. Duplicate JSON keys и non-finite literals отклоняются. Неизвестные record keys запрещены.

Ровно следующие верхние поля:
- schema: literal выше;
- execution_mode: OFFLINE_TEST или REAL_PILOT из admitted prepared mode, не provider body;
- identity: ровно request_sha256, plan_sha256, authority_sha256, attempt_key, response_sha256, native_body_sha256, shape_snapshot_sha256; lowercase hex64 каждый;
- http_status: integer 100..599;
- response_bytes: integer 1..16384;
- fields: ровно 11 dotted paths из таблицы ниже;
- transport_latency_ms: null или finite nonnegative number <= 2^53-1;
- latency_source: null при null latency, иначе transport_boundary_monotonic;
- requester_review_required: true;
- project_acceptance: NOT_GRANTED;
- project_state_mutation: false;
- snapshot_sha256: SHA-256 canonical record без этого поля.

Во всех numeric fields bool запрещён. Strict readback требует independently supplied expected_snapshot_sha256, full expected_identity, expected_mode и проверяет schema/hash/identities/canonical bytes. Hash не подпись: trusted caller хранит ожидаемый digest. response_sha256 вычисляется от original bytes; native_body_sha256 — exact canonical bytes из worker.parse_native, которые переданы transport; остальные identity — из admitted plan/reply и shape. Provider не выбирает identity/mode.

## Allowlist

| Dotted path | Разрешённое value |
|---|---|
| status | completed, failed, in_progress, cancelled, queued, incomplete |
| incomplete_details.reason | max_output_tokens, content_filter |
| error.code | server_error, rate_limit_exceeded, invalid_prompt, invalid_request_error, context_length_exceeded, content_filter, insufficient_quota |
| error.type | server_error, rate_limit_error, invalid_request_error, api_error, authentication_error, permission_error |
| max_output_tokens | integer 0..2^53-1 |
| usage.input_tokens | integer 0..2^53-1 |
| usage.output_tokens | integer 0..2^53-1 |
| usage.total_tokens | integer 0..2^53-1 |
| usage.input_tokens_details.cached_tokens | integer 0..2^53-1 |
| usage.output_tokens_details.reasoning_tokens | integer 0..2^53-1 |
| reasoning.effort | none, minimal, low, medium, high, xhigh, max, ultra |

Enums — закрытый диагностический allowlist, не объявление возможностей модели; не меняют sent effort. Usage — provider-reported counts без исправления сумм, вычисления цены или вывода о причине. Добавление enum требует successor version.

Leaf: ровно {state,value} при state=value, иначе ровно {state}.
- value: валидное typed значение;
- absent: leaf либо промежуточный ключ отсутствует;
- null: конечное значение явно null;
- ancestor_null: промежуточный объект явно null;
- ancestor_invalid: промежуточный объект неверного типа;
- invalid: конечное значение неверного типа/числового диапазона;
- unsupported: строка вне фиксированного enum.

usage=null и usage={} различаются (ancestor_null / absent). Invalid/unsupported values не копируются и не попадают в exceptions; это явно выбранная safe redaction semantics. Дополнительные provider fields игнорируются. Output/content/summary/encrypted_content/arbitrary metadata/headers/error.message не сохраняются. Error code/type также ограничены enum, чтобы не копировать произвольную строку под видом кода.

## Latency и persistence

bridge.MeasuredClient измеряет perf_counter_ns непосредственно вокруг transport.request; latency доступна до normalizer. Это transport-boundary latency, не end-to-end time и не server compute duration. Missing latency=null, не 0. Offline fixtures помечены OFFLINE_TEST.

Writer: private temp O_EXCL/O_NOFOLLOW, fsync data, atomic hard link на новый final path без overwrite, fsync directory, temp cleanup, strict readback O_NOFOLLOW/regular-file check. Existing file/symlink не заменяется. Ошибка любого шага не даёт PASS. Private caller-owned STATE и trusted expected identities — filesystem trust boundary; защиты от привилегированного host attacker не заявляется.

Исторические metadata не реконструируются. Consumed authority/ledger не сбрасываются и не переносятся ради обхода. Схема не создаёт live/standing authority либо acceptance.

## Verification

34 tests: 16 predecessor bridge + 18 новых. Все fixtures synthetic. Сохранены проверки tool/unknown-output rejection, authority/rebind/replay и shape/readback failures. Новые покрывают 12 требований exact KOO task; consumed REAL authority ID проверяется только на synthetic isolated ledger, без реального admission/credential/host access. Полный список в TEST-LOG.txt.

Independent SIS non-live verification обязательна перед host installation. Новый host caller/pins deployment и experiment gate в scope пакета не входят.
