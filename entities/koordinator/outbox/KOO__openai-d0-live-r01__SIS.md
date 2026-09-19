# KOO → SIS: OpenAI one-shot live D0 r0.1

status: LIVE_EXECUTION_AUTHORIZED_AFTER_OPERATOR_TTY_ENTRY
execution_mode: EXACT_ONE_PROVIDER_CALL
priority: TOP_INFRASTRUCTURE

## Verified basis

Technical gate PASS:
`787ec5df1878c7ddb0a5f2928c61e265b40959b0`

Final live-worker PASS:
`18af0b778d5b30f15c20da989a39006f503dcff3`

Runtime:
`/home/pev5691/openai-d0-runtime-r01/package/`

Current wrapper properties previously verified:
- requires `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE`;
- rejects pre-set `OPENAI_API_KEY`;
- reads secret only via hidden `/dev/tty` with `read -r -s OPENAI_API_KEY`;
- no secret-like files/logs under runtime path.

## Operator account facts confirmed in current session

- dedicated API project created: `wellbeing-entity-boosters`;
- prepaid API balance is positive ($5 observed by OPERATOR);
- auto-reload is OFF;
- dedicated restricted project key created;
- key permissions configured for `List models: Read` and `Responses (/v1/responses): Write`; other visible capabilities left None.

The secret value itself must NOT be placed in GitHub, ChatGPT, project files or SIS result artifacts.

## Goal

Prepare and execute exactly one bounded synthetic Luna D0 request using the existing verified runtime and direct OPERATOR hidden TTY entry of the project key.

Exact model:
`gpt-5.6-luna`

No fallback or substitution.

## Required sequence

1. fresh HQ preflight and SIS writer check;
2. verify runtime bytes still match accepted identities;
3. verify no credential file exists in runtime path;
4. provide OPERATOR one exact command/path to launch the verified wrapper interactively so the secret is entered only into hidden `/dev/tty`;
5. after OPERATOR performs hidden key entry, execute exactly one synthetic project-neutral request;
6. retries = 0;
7. tools/web/files = none;
8. no private/project-secret content in prompt;
9. capture only safe metadata:
   - provider/model;
   - request id;
   - HTTP/provider status;
   - input/cached/output/reasoning token usage as reported;
   - stop/finish reason;
   - latency if reliably measurable;
   - model entitlement result;
10. do not log or persist the API key;
11. after call, unset key from process environment;
12. verify no credential/log artifact remains;
13. return:
   `PASS_SIS_OPENAI_LUNA_D0_R01`
   or exact blocker/fail.

This authority covers exactly one provider request after one hidden TTY secret entry. No automatic retry and no Terra/Sol/Astra calls in this task.

After PASS, KOO will authorize the comparative cost-probe matrix separately.
