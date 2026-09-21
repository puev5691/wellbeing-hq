# OpenAI booster response-shape diagnostic persistence r0.1

Статус: bounded non-live diagnostic architecture candidate.

## Purpose

Сохраняет безопасный структурный snapshot provider response после успешного transport/JSON parse, но до review-result normalization.

Future ordering:

`claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`.

Если shape persistence после transport падает:
- one-shot остаётся consumed;
- terminal BLOCKED/FAIL;
- retry/replay/second provider call запрещены.

Если normalizer падает:
- diagnostic shape artifact остаётся;
- review-result может отсутствовать;
- technical PASS запрещён.

## Diagnostic schema

Schema:
`wb.openai.booster.response_shape_diag.v1`.

Persisted:
- provider/model;
- attempt key;
- request/task/writer/plan/authority identities;
- HTTP status;
- raw provider response byte count + SHA-256;
- exact top-level key set;
- output[] count;
- each output item: exact type, exact key set, bounded classification;
- message item: exact role, content count;
- each content item: exact type, exact key set, bounded classification;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

No unrestricted provider body or message text is persisted.

## Classification

Bounded classifications:
- assistant_text;
- benign_metadata_or_reasoning_container;
- tool_action_request;
- tool_action_output;
- unknown.

Classification is diagnostic only.

It does NOT relax the normal review-result v2 parser.

Unknown/tool/action items remain fail-closed until a separately verified correction is approved.

## Privacy boundary

Diagnostic artifact intentionally excludes:
- credential values;
- Authorization headers;
- environment variables;
- cookies/tokens;
- secretref locator;
- raw output_text;
- raw tool arguments;
- unrestricted provider response body.

Only structural key/type/count/classification evidence is persisted.

## Atomic persistence

Same-directory unique temp file.
Mode 0600.
Complete write.
File fsync.
Atomic replace.
Parent-directory fsync.
Strict readback identity/schema validation.

## Reused verified components

Final live-worker:
- commit `716637bb0e18319fa8f3151253ed5c71b8c1aad7`;
- blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`;
- SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`.

Review-result persistence/readback v2 reused unchanged:
- commit `b76e385c139a1b2b0ccdf2ff6481aa1062c161a1`;
- tree `6fcc2f0325256aab96a9c52c913d53875606070f`;
- `review_result_store.py` blob `1f216d9625095d817e4cafb8eea8dacb7cb4b9af`;
- `reviewable_live_worker.py` blob `604f73453ad78fdbc933b1ff7399d5e8c5a0da91`.

Existing v2 normalizer remains unchanged.

## Historical boundary

Historical consumed live acceptance remains BLOCKED.
Its missing provider body/output shape is not reconstructed.
Consumed authority is not reused.
