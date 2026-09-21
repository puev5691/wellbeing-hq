# OpenAI booster response-shape diagnostic persistence r0.2

Статус: bounded non-live successor candidate.

## Причина successor

SIS независимо подтвердил, что predecessor r0.1 сохранял корректную структуру, но strict readback не связывал полный diagnostic evidence contract. Post-persistence tamper response_bytes, response_sha256, http_status, top_level_keys и self-consistent output_count/output_items мог оставаться принятым.

r0.2 не меняет predecessor bytes и не реконструирует historical provider response.

## Schema

Exact schema:

`wb.openai.booster.response_shape_diag.v2`

Top-level key set exact.

Добавлены:
- `snapshot_sha256`;
- `requester_review_required=true`;
- `provider_writer_authority=false`;
- `gateway_writer_authority=false`.

## Snapshot binding

`snapshot_sha256` = SHA-256 canonical diagnostic evidence bytes.

Canonical diagnostic evidence:
- включает все persisted diagnostic поля кроме самого `snapshot_sha256`;
- UTF-8 JSON;
- ensure_ascii=false;
- sort_keys=true;
- separators without whitespace;
- allow_nan=false.

Strict readback выполняет две независимые проверки:

1. пересчитывает hash persisted evidence и требует:
   `persisted snapshot_sha256 == recomputed hash`;

2. требует:
   `recomputed hash == externally supplied expected_snapshot_sha256`.

Внешний expected hash вычисляется из in-memory snapshot ДО persistence.

Поэтому:
- простая подмена evidence блокируется recomputation;
- подмена evidence вместе с пересчитанным persisted hash блокируется external expected hash.

Integration wrapper выводит expected snapshot hash в terminal result или blocker вместе с shape locator, чтобы subsequent diagnosis имел независимый immutable correlation anchor.

## Bound evidence

Snapshot identity покрывает весь persisted diagnostic evidence contract:
- response_bytes;
- response_sha256;
- http_status;
- top_level_keys;
- output_count;
- each output item type/key-set/classification/role/content_count;
- each content item type/key-set/classification;
- requester_review_required;
- project_acceptance;
- project_state_mutation;
- provider_writer_authority;
- gateway_writer_authority;
- attempt_key;
- request_sha256;
- task commit/blob;
- writer blob;
- plan_sha256;
- authority_sha256;
- provider;
- model;
- schema version.

Self-consistent nested mutation is therefore also externally detectable.

## Preserved privacy/content boundary

Unchanged:
- structure-only diagnostic evidence;
- no raw output_text;
- no raw tool arguments;
- no unrestricted raw provider body;
- no credential values;
- no Authorization headers;
- no environment values;
- no cookies/tokens;
- no canonical secretref locator.

Classification remains diagnostic-only.

Current review-result v2 normalizer remains unchanged and fail-closed.

## Preserved ordering

`claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`

If diagnostic persistence/readback fails after transport:
- one-shot remains consumed;
- terminal BLOCKED/FAIL;
- retry/replay/second provider call prohibited.

If normalization fails after shape persistence:
- shape artifact remains;
- review-result may be absent;
- technical PASS prohibited.

## Atomic persistence

Preserved:
- same-directory unique temp;
- mode 0600;
- complete write;
- file fsync;
- atomic replace;
- parent-directory fsync;
- strict readback.

## Reused verified dependencies

Final live-worker unchanged:
`175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`.

Review-result v2 store/integration unchanged:
- `review_result_store.py` SHA-256 `cd01972b7045d4f84583fb5470d4c0012e09c12b954ea65221107eaa01385d7e`;
- `reviewable_live_worker.py` SHA-256 `6a81a0c08ffd961e3b22d2d1de4948ebce780555cfe40b8c669e96e47cb07751`.

No parser allowlist correction is introduced.

## Historical boundary

Historical consumed live acceptance remains BLOCKED.
Historical provider shape is not reconstructed.
Consumed authority remains non-reusable.
Project acceptance remains NOT_GRANTED.
