# OpenAI booster result persistence/readback r0.2

Статус: bounded non-live successor candidate.

## Причина successor

SIS независимо воспроизвёл blocker r0.1:
`READBACK_VALIDATION_DOES_NOT_BIND_RESPONSE_IDENTITY_FIELDS`.

В r0.2 readback связывает весь persisted evidence contract, а не только request/task/writer/provider/model и review payload.

## Schema

Schema:
`wb.openai.booster.review_result.v2`.

Top-level key set exact. Missing или unexpected key блокируется.

Обязательные поля:
- schema;
- attempt_key;
- request_sha256;
- task_commit;
- task_blob;
- writer_blob;
- plan_sha256;
- authority_sha256;
- provider;
- model;
- http_status;
- provider_calls;
- retries;
- fallback;
- response_evidence;
- response_bytes;
- response_sha256;
- parser_status;
- review_payload;
- requester_review_required;
- project_acceptance;
- project_state_mutation;
- provider_writer_authority;
- gateway_writer_authority.

Unknown persisted evidence fields silently не игнорируются.

## Response identity semantics

`response_evidence` — exact bounded normalized provider evidence object with exact key set:

`{"model": <exact model>, "output": <normalized assistant message/output_text sequence>}`.

`response_bytes` is the exact byte length of canonical UTF-8 JSON serialization of `response_evidence`.

Canonical serialization:
- ensure_ascii=false;
- sort_keys=true;
- separators=( ",", ":" );
- allow_nan=false.

`response_sha256` is SHA-256 over those same canonical `response_evidence` bytes.

Readback re-canonicalizes `response_evidence` and independently recomputes both fields.

## Parser/review-payload binding

Allowed parser status is exactly:

`NORMALIZED_ASSISTANT_TEXT_EXACT_FROM_RESPONSE_EVIDENCE`.

The readback parser reconstructs review text from exact `response_evidence.output[].content[].output_text`.

`review_payload.text` must equal that reconstructed text exactly.

`review_payload.bytes` is the UTF-8 byte length of that exact text.

`review_payload.sha256` is SHA-256 over the same UTF-8 text bytes.

Unexpected tool/action output fails closed and is not silently discarded.

## External identity bindings

`read_and_validate()` receives exact expected:
- attempt_key;
- request_sha256;
- task commit/blob;
- writer blob;
- plan_sha256;
- authority_sha256;
- provider;
- model.

All must match persisted values exactly.

Hashes use lowercase 64-hex format.
Git commit/blob bindings use lowercase 40-hex format.

## Accepted technical-result semantics

For this bounded D0 contract:
- provider=openai;
- http_status=200;
- provider_calls=1;
- retries=0;
- fallback=none;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false;
- provider_writer_authority=false;
- gateway_writer_authority=false.

Wrong type, enum, schema/version, status or identity blocks readback.

## Persistence semantics preserved

Unchanged from r0.1:
1. same-directory unique temp;
2. mode 0600;
3. complete write;
4. file fsync;
5. atomic replace;
6. parent-directory fsync;
7. exact readback validation.

If transport was already consumed and persistence/readback fails, technical PASS is not returned and the one-shot remains consumed. No retry/replay is granted to recover missing content.

## Reused verified stack

Final live-worker reused unchanged:
- package commit `716637bb0e18319fa8f3151253ed5c71b8c1aad7`;
- blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`;
- SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`;
- SIS PASS `18af0b778d5b30f15c20da989a39006f503dcff3`.

Live-child basis remains:
`PASS_SIS_OPENAI_BOOSTER_LIVE_CHILD_PATH_R01_READY`
commit `5723ef15ecd76f2c5a0c401d262619c634015c96`.

No provider call, credential access, deployment, canonical secretref change or historical R03 reconstruction occurs in this candidate.

## Historical R03 boundary

Unchanged:
- technical correlation PASS;
- requester review BLOCKED;
- project_acceptance NOT_GRANTED;
- missing historical body not reconstructed.
