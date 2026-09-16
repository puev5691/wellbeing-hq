# KOD → KOO: OpenAI Responses API D0 adapter/transport r0.1

status: `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`
production: `no`
live_api_call: `no`
real_api_key: `no`
billing_changes: `no`
project_private_data_sent: `no`
tools_search_files_computer_use: `no`
fallback: `no`
tera2: `not_started`
project_time: omitted; trusted project-time source not used

## Exact task

`entities/koordinator/outbox/KOO__openai-responses-d0-adapter-r01__KOD.md`
commit `73a7ccbc2a3728f69c123a3790129343325c4277`
blob `0472f621324885bc0bc6a8c02b69b45c8761def3`.

Fresh Resume-First preflight for continuation:
`42afb12983717e236b69bb11a780fa76e7765024`.

## Official OpenAI contract verification

Current official OpenAI documentation was rechecked before terminal publication. Material provider-doc drift was not found.

Verified official sources:
- `https://developers.openai.com/api/reference/cli/resources/responses/methods/create`
- `https://developers.openai.com/api/docs/models/gpt-5.6-luna`
- `https://developers.openai.com/api/reference/cli`
- `https://developers.openai.com/api/reference/cli/resources/responses/methods/retrieve`

Verified boundary used by the package:
- endpoint: `POST https://api.openai.com/v1/responses`;
- model: `gpt-5.6-luna`;
- runtime credential reference only: `OPENAI_API_KEY`;
- request: text `input`, bounded `max_output_tokens`, `store=false`, `tools=[]`, `tool_choice=none`, `parallel_tool_calls=false`;
- response: `id`, `model`, `status`, `output` message blocks with `output_text` content;
- usage: `input_tokens`, `output_tokens`, `total_tokens`, optional `input_tokens_details.cached_tokens`, optional `input_tokens_details.cache_write_tokens`, optional `output_tokens_details.reasoning_tokens`;
- absent optional usage detail is not invented by normalization.

Verdict: `NO_MATERIAL_PROVIDER_DOC_DRIFT`.

## Immutable package

Path:
`entities/koder/outbox/openai-responses-d0-adapter-r01/`

Package commit:
`4fd2c0bb930e81fd5c9e023f674131f086f0e814`

Package tree:
`79e0701df2582f412a3f7358b3702a26b5ed8763`

Blob identities:
- `D0-SYNTHETIC-CONFIG.example.json` `6c0d1e055599eb94a3957db75263e5487199ca16`
- `LIVE-GATE-CHECKLIST.md` `0d8a0c50518b64705b96b41553b0d790849b74d1`
- `MANIFEST.json` `ab43cbaab05eee249705916b1c3cad7d37d272e2`
- `PROVENANCE-CONTRACT.md` `140a434c62d5c55bb43d6d7bf843050ed17a582c`
- `PROVIDER-DOC-CONTRACT.md` `ce652d8db43b5a995f2b3478ca4abe70f11ee032`
- `README.md` `241bc8932451c5ad0bf9ea48a4130256ccc6ab22`
- `REQUEST-CONTRACT.md` `8e91c9f79d22c55f1504fbb1a6a44eb785cab113`
- `SAMPLE_RESULT.json` `e343f98209029935e356445437176fa21f52e431`
- `SHA256SUMS.txt` `d36ee622d66fe68667c77dea3a1c9284734d57c9`
- `TEST_RESULTS.txt` `ec146085ac94136c9b3be41709e3ad5e2c3f9922`
- `TRANSPORT-CONTRACT.md` `1feaf2d5dcc451b2025406ef29950138846e41c1`
- `live_transport.py` `f34dff943d0dbbff3ece56e64cece1d26cd23c14`
- `openai_adapter.py` `c02ab55725caf43c6117aa793ccaa418b1a60f2f`
- `policy.py` `92c2f3e08597c90d781e48c38f664327284db6d6`
- `test_adapter.py` `44213d1de8551d70541f8bb96e5af6be299c0ff1`
- `test_live_transport.py` `57d6699b9d23243d8cf08d871f3dfcf4a1a20d33`
- `test_policy.py` `5fb07e6832a5b2661c4d82ad2be0d91c343067cc`.

## Verification

Immutable checkout/readback from exact package commit:
- `sha256sum -c SHA256SUMS.txt`: `16/16 PASS`;
- `python3 -m py_compile policy.py openai_adapter.py live_transport.py test_policy.py test_adapter.py test_live_transport.py`: PASS;
- `python3 -m unittest -q`: `25/25 PASS`.

The suite covers valid D0 request/response, model mismatch, malformed usage/content, non-D0 reject before transport, credential-like field/value rejection, tools/search/files/computer-use/fallback/project-mutation rejection, auth/rate-limit/5xx/timeout/network handling, deterministic provenance/result identity, provider-output candidate-only semantics, and default-deny live execution.

A first immutable readback correctly detected publication byte drift in 10 files. Those files were reconciled to the exact tested payload before this terminal package identity was established; the final exact commit above passes the full checksum suite.

## Boundary actually observed

- real OpenAI API calls: `0`;
- real credentials/API keys used or requested: `0`;
- billing changes: `0`;
- project/private data sent externally: `0`;
- tools/search/files/computer-use/code-execution enabled: `0`;
- fallback/alternate provider used: `0`;
- production mutation: `0`;
- TERA2 work: `0`.

## Future live gate prerequisites

This PASS is readiness for a separate account/live gate, not live authority. A later task would require all of the following independently:
- explicit OPERATOR/KOO authorization for exactly one D0 synthetic request;
- verified account/project access to `gpt-5.6-luna`;
- account/billing readiness confirmed outside this task;
- `OPENAI_API_KEY` supplied only by runtime secret injection;
- selected Unix-host outbound HTTPS preflight;
- this exact immutable package/readback still current;
- D0 synthetic input only;
- tools/search/files/computer-use/code/fallback/project-mutation remain disabled;
- explicit live switch `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE` only inside that future gate.

Provider output remains candidate/evidence only and cannot self-declare project acceptance/current/canon state.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO terminal result exact bounded OpenAI Responses D0 adapter/transport task
СТАТУС: `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`
