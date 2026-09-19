# SIS → KOO + KOD: OpenAI four-model cost matrix r0.2 terminal result

verdict: `PASS_SIS_OPENAI_COST_MATRIX_R02`
provider_attempts: 4
retries: 0
fallback: none
project_time: omitted; trusted project-time source not used

## Execution basis

Authoritative task:
`a011be06d1bbb23b53dc74cd0ee3fb1c53291d34`.

Current SIS writer:
`3ca813a7addb711eb8bf2e017b39517268fa31f0`.

Clean runtime staging PASS:
`a242e8bdf0455acf1ebe95d1e352b56370d53691`.

Fresh pre-call runtime identity:
`3_OF_3_PASS`.

Prompt SHA-256:
`1d4d31ce8fbbfc167b302ec0e6cb99984972dacd7af8d79e58d72887cf9dbd91`.

Output cap:
`64`.

Credential handling:
interactive hidden entry; no persistence.

## Provider results

### gpt-5.6-luna

- entitlement: PASS
- response id: `resp_020aa3a54ec4aa01016aae7057029887d19a3bcb61b566eb91`
- status: completed
- latency: 2.387152 s
- input tokens: 15
- cached input tokens: 0
- output tokens: 9
- reasoning tokens: 0
- total tokens: 24
- output bytes: 9
- output SHA-256: `6ffbbe12c3d609cbd5297aa4418f8371ce1ee554ce8b6919fee54d90398d44db`
- provider calls: 1
- documented standard list price: $0.20 / 1M input, $1.20 / 1M output
- estimated list-price cost for this call: $0.0000138

### gpt-5.6-terra

- entitlement: PASS
- response id: `resp_0be36a6215ef000f016aae70587c7087d1be6a608eb3be0b7c`
- status: completed
- latency: 1.331757 s
- input tokens: 15
- cached input tokens: 0
- output tokens: 9
- reasoning tokens: 0
- total tokens: 24
- output bytes: 9
- output SHA-256: `6ffbbe12c3d609cbd5297aa4418f8371ce1ee554ce8b6919fee54d90398d44db`
- provider calls: 1
- documented standard list price: $2.00 / 1M input, $12.00 / 1M output
- estimated list-price cost for this call: $0.000138

### gpt-5.6-sol

- entitlement: PASS
- response id: `resp_0e572a516ae946d5016aae7059d48487d19aa1d36ae60d3177`
- status: completed
- latency: 1.132133 s
- input tokens: 15
- cached input tokens: 0
- output tokens: 9
- reasoning tokens: 0
- total tokens: 24
- output bytes: 9
- output SHA-256: `6ffbbe12c3d609cbd5297aa4418f8371ce1ee554ce8b6919fee54d90398d44db`
- provider calls: 1
- documented standard list price: $4.00 / 1M input, $20.00 / 1M output
- estimated list-price cost for this call: $0.000240

### gpt-6-astra

- entitlement: PASS
- response id: `resp_0d50361a82348e6f016aae705aef9887d1ab6e7f8169044bc7`
- status: completed
- latency: 1.295611 s
- input tokens: 15
- cached input tokens: 0
- output tokens: 9
- reasoning tokens: 0
- total tokens: 24
- output bytes: 9
- output SHA-256: `6ffbbe12c3d609cbd5297aa4418f8371ce1ee554ce8b6919fee54d90398d44db`
- provider calls: 1
- documented standard list price: $10.00 / 1M input, $50.00 / 1M output
- estimated list-price cost for this call: $0.000600

## Matrix summary

All four exact models returned completed responses under the same bounded prompt/output-cap contract.

Entitlement:
- Luna PASS
- Terra PASS
- Sol PASS
- Astra PASS

Total provider attempts: 4/4.
Retries: 0.
Fallback: none.
Total input tokens: 60.
Total cached input tokens: 0.
Total output tokens: 36.
Total reasoning tokens: 0.
Total tokens: 96.

Documented standard list-price estimate across all four calls:
`$0.0009918`.

This estimate is calculated from public OpenAI list prices and observed token usage; it is not provider billing metadata and does not assert the account's final billed amount.

Pricing references:
- https://developers.openai.com/api/docs/models/gpt-5.6-luna
- https://developers.openai.com/api/docs/models/gpt-5.6-terra
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/models/gpt-6-astra

## Boundary

No tools/web/files/computer/code execution were used inside provider requests.
No project/private/secret content was sent in provider prompts.
Credential value was not recorded.
No automatic retry was used.
No fallback was used.

## Terminal result

`PASS_SIS_OPENAI_COST_MATRIX_R02`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: terminal four-model OpenAI entitlement/usage/cost matrix result
СТАТУС: `PASS_SIS_OPENAI_COST_MATRIX_R02`
