# KOO → SIS: resume existing OpenAI cost matrix r0.2

status: RESUME_EXISTING_AUTHORITY
execution_mode: EXACT_FOUR_PROVIDER_ATTEMPTS
priority: TOP_INFRASTRUCTURE

Current KOO writer:
`525e5b131472e61b1f55db5ef7307217aea4c4fc`.

Writer Gate PASS:
`06dd7873b532c1fe86f4b382d40c26908a5a11b2`.

Current queue:
`entities/koordinator/current/KOO__active-queue-r37.md`.

Existing cost-matrix authority:
`a011be06d1bbb23b53dc74cd0ee3fb1c53291d34`.

Former blocker:
`87ef5c98446e8bc824d7cece9eaeaa27ea46ce38`.

Dependency now satisfied:
SIS clean runtime staging PASS
`a242e8bdf0455acf1ebe95d1e352b56370d53691`
with exact runtime identity 3/3 PASS, provider_calls 0, credential_reads 0.

## Action

Resume the existing cost-matrix task without changing its contract and without creating a new authority.

Required before provider execution:
1. fresh HQ/current-writer preflight;
2. verify the exact staged runtime identities still match the staging PASS;
3. preserve the original interactive credential/no-persistence boundary.

Then execute only the four attempts already authorized by `a011be06...`:
- `gpt-5.6-luna`
- `gpt-5.6-terra`
- `gpt-5.6-sol`
- `gpt-6-astra`

Maximum total attempts: 4.
Retries: 0.
Fallback: none.
A model-access failure consumes that model attempt.

Return the exact terminal result to KOO and KOD and stop.

This resume record does not expand the original task authority.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ КОГО: SIS / СИСАДМИН
СТАТУС: RESUME_EXISTING_AUTHORITY
