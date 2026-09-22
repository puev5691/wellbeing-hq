# KOD → KOO: почему utility pilot не дал текста решения

Запрос с синтетической задачей дошёл до проверенного технического тракта без обнаруженной подмены. OpenAI вернул HTTP 200, но единственным элементом output был reasoning. Готового текста решения не было; нормализатор правильно остановил обработку, не выдав reasoning за candidate.

Наиболее предметная гипотеза — недостаточный общий лимит 64 output tokens. Однако причина завершения и usage не сохранены в текущем диагностическом формате. Поэтому исчерпание token budget для этой конкретной попытки НЕ ДОКАЗАНО. Подтверждена причина локального отказа и выявлен пробел наблюдаемости, мешающий установить причину на стороне провайдера.

status: DIAGNOSED_KOD_BOOSTER_UTILITY_PILOT_R01_NO_ASSISTANT_TEXT_CAUSE_UNCONFIRMED
scope: bounded_non_live_diagnostic_only
provider_calls_this_cycle: 0
historical_authority_replay: 0
host_configuration_changes: 0
credential_value_reads: 0
reasoning_content_access_or_reconstruction: 0
project_acceptance: NOT_GRANTED
project_time: omitted

## Fresh reconciliation

HQ HEAD: f69c544e138fc528a6404142acff741df9b97158.
Fresh current directory: v0.5 writer blob cf1c84f9df7c90509703e4885844d0cf871ff412 unchanged; v0.4 freeze blob 94cc1acb14fdcca623f4596c9a589e9ff42451ee unchanged; no newer competing KOD writer found.

SIS terminal:
entities/sisadmin/outbox/SIS__booster-utility-pilot-r01-one-shot-live-terminal__KOO.md
at HEAD above, blob aa3d4fc03202a093ea565190ec62a72531a3862b.
verdict BLOCKED_SIS_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT_LIVE_NO_ASSISTANT_TEXT.

SIS host-readiness:
entities/sisadmin/outbox/SIS__booster-utility-pilot-bridge-r01-host-readiness__KOO.md
at HEAD above, blob 5b329b9521017707af6def5bc6d3d867929f9123.
Previous KOD host-not-wired blocker is superseded by this host-readiness and subsequent actual attempt. It is not the present cause.

AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT is CONSUMED.
Read-only SQLite inspection on ruvds-xnqc6 confirmed one consumed row in each utility authority/attempt ledger, bound to the identities below. LIVE_GATE absent. No admission, service start, retry or provider request executed in this cycle.

## Exact request and body

Config path /etc/wellbeing/booster-utility-pilot-r01/request.json.
File SHA-256 13ec391f25ab8a5e524e933c61f72dcc30248066daa1babecc22ba8923d8382a matches host caller pin.
Host caller SHA-256 de844e82268243812b86d9fe76a39165dccecde4e98cbe9f6f1e1e20eada40d4 matches SIS readiness.

Payload equals specification from immutable baseline:
puev5691/wellbeing-hq@d074ffd92a2794af954e27a8a809a3c6335ce14a:entities/koder/outbox/booster-utility-pilot-r01-baseline/task.json
blob b830a16fb2be1dd581abd9b753785a63b8280365.
Payload UTF-8 SHA-256 5ccbf5eeb58d0f7e86c64e62c669585e23aed8686b6460ea5e57e9b781bf1332.

Exact frozen request:
```json
{"baseline_sha256":"f90a3e9fd20ae24cdff4c86e71e0215888e3befc5831bbf26ce4681bbb3d75a2","data_class":"D0_SYNTHETIC","entity":"KOD","max_output_tokens":64,"max_response_bytes":16384,"model":"gpt-5.6-luna","payload":"Implement Python runs(s) for a str s. Return a list of (character, count) tuples in input order. Each tuple represents a nonempty maximal consecutive run, split greedily into chunks of at most 3. Characters mean Python Unicode code points. Preserve every character exactly; empty input returns []. Input is always str; no type validation required. No imports, tools, network or project data.","privacy_class":"synthetic_only","provider":"openai","purpose":"D0_RUNS_MAX3_R01 bounded utility pilot assisted variant","role":"koder","source":{"locator":"github://puev5691/wellbeing-hq@d074ffd92a2794af954e27a8a809a3c6335ce14a/entities/koder/outbox/booster-utility-pilot-r01-baseline/task.json#specification","sha256":"5ccbf5eeb58d0f7e86c64e62c669585e23aed8686b6460ea5e57e9b781bf1332"},"task":{"blob":"b830a16fb2be1dd581abd9b753785a63b8280365","commit":"d074ffd92a2794af954e27a8a809a3c6335ce14a","path":"entities/koder/outbox/booster-utility-pilot-r01-baseline/task.json","repository":"puev5691/wellbeing-hq"},"timeout_seconds":30,"tools":[],"writer":{"blob":"cf1c84f9df7c90509703e4885844d0cf871ff412","commit":"df92a8bfcce29294332f6e4de3391a3e7966adfd","path":"entities/koder/current/KOD__replacement-current-writer-v05.md","repository":"puev5691/wellbeing-hq"}}
```

Native body deterministically derived from verified bridge.prepare and live_worker.parse_native:
```json
{"input":"Implement Python runs(s) for a str s. Return a list of (character, count) tuples in input order. Each tuple represents a nonempty maximal consecutive run, split greedily into chunks of at most 3. Characters mean Python Unicode code points. Preserve every character exactly; empty input returns []. Input is always str; no type validation required. No imports, tools, network or project data.","max_output_tokens":64,"model":"gpt-5.6-luna","parallel_tool_calls":false,"store":false,"tool_choice":"none","tools":[]}
```

POST https://api.openai.com/v1/responses.
Canonical UTF-8 native body: 523 bytes; SHA-256 6c4dd049b5feb49b79fae3519a98347c1e3909a28a7dbfa146bc44c125a9eea6.
This is a verified deterministic body derivation, not a separately captured on-wire packet. No authorization header/credential was read or persisted.

request_sha256: 45dfd35e5ef9888caaf9a7b8d4b48d3ff5f66aede354eca94f5562b369ba5bc2
plan_sha256: 4fa2a4b48c233be8c550bf5a5516ab29e9fd2cff080a6427599733c2653893d7
authority_sha256: 1feb7252b8382931280b17c9b96784ca3799f08a1002d7ffd67d38eb6f047b7b
attempt_key: c615ca63da17b9accd8de757c3c89177aa502a6473dd422a1fa67482f4644ca4
named_authority_reservation: 95e2853c6bdafdda9a69517a3f8efc6bc5a0b8281c78c26d4897d8dd2c285c26

Request and plan hashes recomputed without invoking runtime; both match persisted shape and consumed ledger.
max_output_tokens=64 is hardcoded in request admission AND native body construction.
No explicit reasoning.effort was sent; the actual provider default is not established from persisted evidence. No effort value is assumed.
tools=[], tool_choice=none, parallel_tool_calls=false, store=false.
timeout_seconds=30; max_response_bytes=16384.

## Persisted response-shape

Read directly, read-only, on ruvds-xnqc6:
 /var/lib/wellbeing/booster-utility-pilot-r01/shapes/c615ca63da17b9accd8de757c3c89177aa502a6473dd422a1fa67482f4644ca4.shape.json

Shape file SHA-256: 04b084c9a44e220d48374ba37d7cef818ee66e8f25c94bbcc93e3943b6c323f0.
Canonical snapshot SHA-256 recomputed and matched: 07278de02484e0fe2c14dcddc7dbe9e4ec093981f885769eaf4eedb590cdb40f.

Exact structural evidence (no reasoning values):
```json
{"attempt_key":"c615ca63da17b9accd8de757c3c89177aa502a6473dd422a1fa67482f4644ca4","authority_sha256":"1feb7252b8382931280b17c9b96784ca3799f08a1002d7ffd67d38eb6f047b7b","gateway_writer_authority":false,"http_status":200,"model":"gpt-5.6-luna","output_count":1,"output_items":[{"classification":"benign_metadata_or_reasoning_container","content_count":null,"content_items":[],"index":0,"keys":["content","encrypted_content","id","summary","type"],"role":null,"type":"reasoning"}],"plan_sha256":"4fa2a4b48c233be8c550bf5a5516ab29e9fd2cff080a6427599733c2653893d7","project_acceptance":"NOT_GRANTED","project_state_mutation":false,"provider":"openai","provider_writer_authority":false,"request_sha256":"45dfd35e5ef9888caaf9a7b8d4b48d3ff5f66aede354eca94f5562b369ba5bc2","requester_review_required":true,"response_bytes":3495,"response_sha256":"55ffdaabf8e2ec0e35497408631c36064383d89119f8b787b6770c70b6d264ab","schema":"wb.openai.booster.response_shape_diag.v2","snapshot_sha256":"07278de02484e0fe2c14dcddc7dbe9e4ec093981f885769eaf4eedb590cdb40f","task_blob":"b830a16fb2be1dd581abd9b753785a63b8280365","task_commit":"d074ffd92a2794af954e27a8a809a3c6335ce14a","top_level_keys":["background","billing","completed_at","created_at","error","frequency_penalty","id","incomplete_details","instructions","max_output_tokens","max_tool_calls","metadata","model","moderation","object","output","parallel_tool_calls","presence_penalty","previous_response_id","prompt_cache_key","prompt_cache_retention","reasoning","safety_identifier","service_tier","status","store","temperature","text","tool_choice","tool_usage","tools","top_logprobs","top_p","truncation","usage","user"],"writer_blob":"cf1c84f9df7c90509703e4885844d0cf871ff412"}
```

HTTP200; response_bytes=3495 below 16384; output_count=1; exact type=reasoning.
No message/assistant/output_text container is present in output.
reasoning.content_count=null is an intentional structural-schema omission for non-message items, not evidence that reasoning content was empty.
Keys content/encrypted_content/summary are names only. Their values were not retrieved, decoded or reconstructed.

The top_level_keys list includes status, incomplete_details, error, usage, max_output_tokens and reasoning. Their VALUES are unavailable in this snapshot. Presence of a key does not establish non-null contents or status=incomplete.
No raw provider response, review-result or execution.json was found in the inspected canonical utility state root. This is a scoped finding, not a claim about every possible host/provider log.
The last 60 unit journal records were filtered to known host-readiness schema and allowlisted fields: READY and BLOCKED records agree with SIS and the shape; no missing provider usage/status values were recovered.

## One causal diagnosis

Confirmed chain:
frozen task → bound native body with 64-token cap → HTTP200 reasoning-only output → shape saved → normalizer skips exact reasoning → normalized assistant list empty → BLOCKED_PROVIDER_RESPONSE → no review/candidate/common-test result/card.

The wrapper label BLOCKED_REVIEW_RESULT_PERSISTENCE_AFTER_SHAPE_SAVED is broader than the actual failure. Here normalization fails before persist_atomic(review); this is not evidence of a disk-write failure. No regression that discards an existing assistant message is demonstrated.

Code lineage:
9aef9ada9b27f6526a0f5326213748ad689c5a8e:entities/koder/outbox/booster-utility-pilot-live-evidence-bridge-r01
Installed SHA-256 values checked against pinned source:
- bridge.py 0c54e6f40f62c9dc2aaa06dd99dc9d9f9a7c4ffdf882528321210ea72e128d9b
- deps/live_worker.py 175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3
- deps/response_shape_store.py bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f
- deps/review_result_store.py 72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba
- deps/diagnostic_reviewable_live_worker.py ab9e254a34151ed53e36160c4d63ff0b361774f8340bbfc34c56594e550b0deb

Confirmed observability gap:
response_shape_store.structural_snapshot retains top-level key names, not completion/usage values. bridge.execute records measured latency only after successful normalization/readback; on this exception the in-memory latency does not reach execution.json. HTTP200 therefore proves transport success, not completed useful generation.

Hypothesis:
64 total generated tokens may have been exhausted before visible text. Official OpenAI documentation explains that max_output_tokens includes reasoning and visible output, and an incomplete response may occur before visible output.
Source: https://developers.openai.com/api/docs/guides/reasoning#allocating-space-for-reasoning
This documents the mechanism, not the actual cause of this attempt. Missing response.status, incomplete_details.reason and usage prevent confirmation. Do not assert that exactly 64 reasoning tokens were used, that increasing the cap guarantees success, or that this proves a model-wide defect.
Usage, provider latency and cost remain unknown. No completed baseline-versus-assisted utility comparison exists.

## Minimal next correction / experiment gate

ONE next implementation step for KOO to admit: bounded NON-LIVE successor for failure-path diagnostic metadata preservation. No provider call is part of it.

Preserve before normalization, with strict typed allowlist and explicit absent/null handling:
response status; incomplete_details.reason; error.code/type only; echoed max_output_tokens; usage input/output/total plus cached/reasoning token counts when supplied; reasoning.effort enum when supplied; transport latency. Bind to original response hash, request/plan/attempt identities and exact native-body hash. Exclude output values, reasoning content/summary/encrypted_content, raw headers and arbitrary error messages. Keep original v2 evidence immutable; version/hash/readback successor evidence. Failure still produces no candidate or acceptance.

Offline admission checks: synthetic incomplete/max_output_tokens with reasoning-only output; completed assistant text; missing/null metadata; malformed fields; no content leakage; fail-closed normalizer unchanged; failure-path metadata survives; consumed authority cannot be reset/reused. Do not claim these successor checks already passed: no implementation was performed this cycle.

Only AFTER independent verification of that correction may KOO propose a separate experiment gate:
- new explicit OPERATOR one-shot authority with a NEW authority identifier, never reuse/reset the consumed r01 identifier or ledgers;
- same frozen D0 task/model/prompt, no simultaneous reasoning-effort/prompt changes;
- explicitly approved larger finite output cap (candidate 1024, hypothesis-testing value, not guaranteed sufficient), compatible byte/time limits, exact new request/body/plan identities;
- update hardcoded 64 and named-authority admission through a reviewed successor contract, never direct config bypass;
- one call, zero retries/fallback/tools; capture diagnostic metadata on every terminal; stop even if no text;
- requester review and same tests only if an admissible candidate exists; project acceptance remains NOT_GRANTED.
This is a proposed future gate, not a grant of implementation/deployment/live authority. Current task ends with this diagnosis.

## Journal-source для РЕДАКТОРА

Первый эксперимент практической полезности Booster дошёл до реального запроса, но решения не дал: сервис ответил успешно на уровне HTTP, а текста программы в ответе не оказалось. КОДЕР проверил сохранённые данные и установил, что задание не потерялось, а защита правильно отказалась считать служебный reasoning готовым результатом. Малый лимит ответа — обоснованная, но пока не доказанная причина. Выяснилось, что для таких отказов не сохраняются значения причины завершения и расхода токенов. Следующий шаг — исправить эту диагностику без нового вызова. История показывает: технический ответ сервиса ещё не означает полезный результат, а причину сбоя нельзя подменять догадкой.

КТО: KOD / КОДЕР
КОМУ: KOO / КООРДИНАТОР; journal-source для RED
