# KOO → SIS: OpenAI Terra/Sol model-policy extension preflight r0.1

status: `READY_FOR_SIS_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Purpose

Prepare a bounded dry-run model-policy extension path so the accepted OpenAI runtime/benchmark stack can later evaluate:
- `gpt-5.6-luna`;
- `gpt-5.6-terra`;
- `gpt-5.6-sol`.

Current authoritative benchmark implementation is package B:
commit `aa36f7a99105d367b6b2cc5038952c428301c7a0`.

Accepted runtime integration:
`b212eda0151a5ee07fed8f5cef4299e2b7e3a73f`.

Accepted SIS runtime/secret gate:
`3c282b2d67a699520ccbf7a751616c3e2ee58d5a`.

## Required work

Read-only/dry-run only:
1. identify exact Luna-only policy constraints in accepted OpenAI D0 adapter/runtime;
2. define smallest fail-closed policy extension for Terra/Sol;
3. prove via dry-run/sentinel path that model selection is explicit and no silent fallback exists;
4. preserve existing live switch and secret-injection contract;
5. keep live execution disabled;
6. return exact files/fields KOD would later need to update, or produce a bounded patch candidate if that is within SIS profile authority;
7. no provider call, no entitlement assumption.

## FAST_PATH

Target <=12 tool calls and <=8 GitHub reads.
Do not repeat host inventory already proven.
Stop once extension feasibility and exact dependency are established.

## Hard boundaries

No API keys.
No authenticated/unauthenticated OpenAI provider request.
No billing/account mutation.
No sudo/root.
No production deploy.
No project/private data external send.
No TERA2/WBN.

## Expected result

`PASS_SIS_OPENAI_MODEL_POLICY_EXTENSION_PREFLIGHT_R01`

or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.
