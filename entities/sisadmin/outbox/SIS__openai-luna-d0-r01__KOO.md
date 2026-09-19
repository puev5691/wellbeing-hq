# SIS → KOO: OpenAI Luna one-shot D0 r0.1

verdict: `PASS_SIS_OPENAI_LUNA_D0_R01`
execution_mode: `EXACT_ONE_PROVIDER_CALL`
provider_calls: `1`
automatic_retries: `0`
fallback_used: `false`
project_time: omitted; trusted project-time source not used

## Resume-First

fresh_HQ_HEAD: `eacb8f3807c2d7aa11d7c52354e58770ab519d21`
prewrite_reconciliation_HEAD: `eacb8f3807c2d7aa11d7c52354e58770ab519d21`
current_SIS_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__openai-d0-live-r01__SIS.md`
commit `1f987e65e8ef9273ec394c7081c915d5ddc631a9`.

Inbox placement:
commit `3269be0d3c7f1f3bc1d66d082287ce7c878cbc1e`.

Technical gate:
commit `787ec5df1878c7ddb0a5f2928c61e265b40959b0`.

Live-worker final PASS:
commit `18af0b778d5b30f15c20da989a39006f503dcff3`.

## Runtime byte re-verification before call

Runtime:
`/home/pev5691/openai-d0-runtime-r01`

Observed SHA-256:
- `package/policy.py`: `b95edabf6461ce155f48cf08fcec752d7c2c5dd8a7cc94ff4e765575731a83ad`;
- `package/openai_adapter.py`: `e2787a3764eb09a209fcbea5ccbcada55ad32b870b87efbcdd2a225b4fb7d232`;
- `package/live_transport.py`: `6ebad878a82d116aa9f7b21e9cf63bc53c1fac562bd8a9c7a9da86746e446498`;
- `run_live_once.sh`: `0e4d85e0eda92b3b63a064a271cfd16c8150fa5ef6850e6a445a5fcbc2356edb`;
- `package/D0-SYNTHETIC-CONFIG.example.json`: `acdad032f73b9264d0f4ca461ccf459562c982cbc3f30ad128125fa1bbbc7043`.

Wrapper properties re-read:
- exact live switch required;
- pre-set `OPENAI_API_KEY` rejected;
- secret read only by hidden `/dev/tty`;
- EXIT/HUP/INT/TERM trap unsets the key.

No secret-like or log files were observed under the runtime path before call.
No `OPENAI_API_KEY` or `OPENAI_LIVE_D0` was present in the inspected runtime execution environment before launch.

## Exact request boundary

Provider:
`openai`

Model:
`gpt-5.6-luna`

Synthetic prompt:
`Return exactly the word SYNTHETIC.`

Configured:
- `max_output_tokens=64`;
- tools disabled;
- web search disabled;
- file search disabled;
- computer use disabled;
- code execution disabled;
- fallback disabled;
- alternate provider disabled;
- store disabled;
- production false;
- project mutation false.

The API key was entered by OPERATOR only into the hidden TTY prompt. Its value was not copied into GitHub, ChatGPT, result files, or logs.

## Live provider result

Exactly one provider request was executed.

Safe returned metadata:
- provider: `openai`;
- model: `gpt-5.6-luna`;
- response id: `resp_0d54d05ff3b12731016aae3ab9f06087d18f2bf28390c0d07d`;
- response status: `completed`;
- parsed text: `SYNTHETIC`;
- input tokens: `15`;
- cached input tokens: `0`;
- cache write tokens: `0`;
- output tokens: `9`;
- reasoning tokens: `0`;
- total tokens: `24`;
- automatic retry used: `false`;
- fallback used: `false`;
- tools used: `false`;
- web search used: `false`;
- file search used: `false`;
- computer use used: `false`;
- code execution used: `false`;
- credential source: `OPENAI_API_KEY`;
- credential value recorded: `false`;
- external network used: `true`;
- project mutation performed: `false`;
- production: `false`;
- project acceptance: `NOT_GRANTED`.

Model entitlement result:
`PASS` by successful completed response from exact model `gpt-5.6-luna`.

HTTP status code was not exposed by the current safe wrapper output after successful parsing. The provider response status was `completed`. No HTTP code is invented.

Stop/finish reason was not exposed by the current safe parser/result. No value is invented.

Latency was not instrumented reliably for this operator-driven TTY call and is therefore omitted.

## Post-call hygiene

After the call SIS performed only local read-only hygiene checks.

Observed:
- no secret-like files under the runtime path;
- no runtime log files under the runtime path;
- no `OPENAI_API_KEY` or `OPENAI_LIVE_D0` in the inspected post-call process environment;
- wrapper and runtime hashes remained unchanged.

No second provider call was made.

## Boundary

This task does not authorize:
- Terra/Sol/Astra calls;
- automatic retry;
- comparative matrix calls;
- production deployment;
- project acceptance;
- credential persistence;
- account/billing mutation.

The one-call authority is consumed.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: выполнить ровно один bounded synthetic OpenAI Luna D0 live request
СТАТУС: `PASS_SIS_OPENAI_LUNA_D0_R01`
