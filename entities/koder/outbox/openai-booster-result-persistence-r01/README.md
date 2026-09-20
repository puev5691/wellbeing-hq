# OpenAI booster result persistence/reviewability r0.1

Статус: bounded non-live candidate.

## Назначение

Исправляет только будущую persistence/reviewability bounded live-result. Исторический R03 provider response body не реконструируется и не переоценивается.

Цепочка будущего результата:

`verified live-worker reply → exact parser/model/action checks → bounded normalized assistant text → atomic durable review artifact → later requester review with provider_calls=0`.

## Reused verified stack

Final live-worker:
- package commit `716637bb0e18319fa8f3151253ed5c71b8c1aad7`;
- `live_worker.py` blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`;
- SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`;
- SIS final PASS `18af0b778d5b30f15c20da989a39006f503dcff3`.

SIS-verified live-child lineage:
- terminal `PASS_SIS_OPENAI_BOOSTER_LIVE_CHILD_PATH_R01_READY`;
- commit `5723ef15ecd76f2c5a0c401d262619c634015c96`.

No provider call, credential access or production deployment occurs in this candidate.

## Persisted review-result schema

Schema:
`wb.openai.booster.review_result.v1`.

Persisted fields include:
- exact attempt key;
- request SHA-256;
- task commit/blob;
- writer blob;
- plan SHA-256;
- authority SHA-256;
- provider/model;
- HTTP status;
- provider call count;
- retries/fallback;
- provider response byte count and SHA-256;
- parser status;
- bounded normalized assistant text with its own byte count/SHA-256;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false;
- provider/gateway writer authority=false.

The normalized review payload is the ordered concatenation of every assistant `output_text` item from exact provider `output[].content[]`.

For this D0 review purpose the parser fails closed if:
- model differs;
- response is malformed;
- response/body exceeds bound;
- output is empty;
- output contains non-message actions;
- assistant content contains anything other than `output_text`.

Thus a persisted normalized text is review-equivalent for the bounded D0 assistant-text purpose; unexpected tool/action output is not normalized away.

## Secret exclusion

The review artifact does not contain:
- credential values;
- Authorization headers;
- secretref locators;
- environment values;
- cookies/tokens;
- request headers.

Credential resolution remains inside the reused live-worker boundary.

## Atomic/durable persistence

`persist_atomic()` writes to a unique same-directory temporary file with mode 0600, performs full-write loop, fsyncs the file, atomically replaces the target, then fsyncs the parent directory.

Failures in write/fsync/rename/serialization/readback/identity validation return a blocker and must not produce technical PASS.

If a provider call already occurred and persistence then fails, the one-shot ledger remains consumed. No retry/replay is permitted to reconstruct missing content.

## Preserved execution boundaries

Unchanged:
- durable claim before credential resolution/provider transport;
- calls=1;
- retries=0;
- fallback=none;
- hard timeout and response limit from final live-worker;
- redirect fail-closed;
- exact provider/model binding;
- canonical secretref path;
- no legacy TTY fallback;
- requester review required;
- project_acceptance=NOT_GRANTED;
- no project-state mutation;
- no provider/gateway writer authority.

## Historical R03

Historical R03 remains:
- technical correlation PASS;
- requester review BLOCKED because response body was not persisted;
- project_acceptance NOT_GRANTED.

This candidate does not reconstruct or upgrade that historical result.
