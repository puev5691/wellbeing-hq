# KOO → SIS: OpenAI comparative cost matrix r0.1

status: TASK
priority: TOP_INFRASTRUCTURE

Basis:
- OpenAI bounded-live gate PASS `04a9633d7657afcf37f2ea9b4fb936ae1789e88f`
- Luna live D0 PASS `28f92b1a72b96fefcb991d1ecccfd57752330301`

Run one identical bounded project-neutral inference attempt for each exact model:
- `gpt-5.6-luna`
- `gpt-5.6-terra`
- `gpt-5.6-sol`
- `gpt-6-astra`

Maximum four provider attempts total. No retries. No fallback.

Same exact prompt and output limit for every model. No tools, files, web or private content.

For each model record only safe result metadata: status/error, token usage, reliable latency, response id if available, output byte length and SHA-256, entitlement result.

Use the already verified operator-interactive live mechanism from Luna D0. Preserve the same secret-handling boundary and leave no persistent secret/log artifact.

Return:
`PASS_SIS_OPENAI_COST_MATRIX_R01`
or exact partial/blocker/fail.
