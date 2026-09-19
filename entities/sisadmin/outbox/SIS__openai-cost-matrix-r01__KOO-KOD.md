# SIS → KOO + KOD: OpenAI comparative cost matrix r0.1 blocker

verdict: `BLOCKED_OPENAI_COST_MATRIX_ASTRA_NOT_IN_VERIFIED_RUNTIME_ALLOWLIST`
execution_mode: `PRECALL_STOP`
provider_calls: `0`
automatic_retries: `0`
fallback_used: `false`
credential_read: `false`
project_time: omitted; trusted project-time source not used

## Resume-First

fresh_HQ_HEAD: `5ce554d7654c5ac21233440ebdfb0a4ef4ac5bb3`
current_SIS_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
current_writer_match: `PASS`

Exact task:
`entities/koordinator/outbox/KOO__openai-cost-matrix-r01__SIS.md`
commit `512cad6059a4911ee16fb6012a9e05366dc3b547`.

Basis:
- bounded-live gate PASS `04a9633d7657afcf37f2ea9b4fb936ae1789e88f`;
- Luna D0 PASS `28f92b1a72b96fefcb991d1ecccfd57752330301`.

## Required matrix

Task requires one identical bounded provider inference attempt for each exact model:
- `gpt-5.6-luna`;
- `gpt-5.6-terra`;
- `gpt-5.6-sol`;
- `gpt-6-astra`.

Maximum four provider attempts total.
Retries = 0.
Fallback = none.
Same prompt/output cap.
Use the already verified operator-interactive Luna D0 live mechanism.

## Fresh runtime verification

Runtime:
`/home/pev5691/openai-d0-runtime-r01`

Current verified policy contains exactly:
`MODELS=frozenset({"gpt-5.6-luna","gpt-5.6-terra","gpt-5.6-sol"})`

Observed enforcement points:
- `policy.py`: model outside `MODELS` -> `PolicyViolation("unknown_model")`;
- `openai_adapter.py`: model outside `MODELS` -> `PolicyViolation("unknown_model")`;
- `live_transport.py`: model outside `MODELS` -> `PolicyViolation("live_model_forbidden")`;
- success parser requires expected model in `MODELS`.

No staged four-model/cost-matrix runtime file was found under the verified runtime path.
No secret-like/log files were found under that path during this preflight.

## Exact blocker

`gpt-6-astra` is not present in the verified runtime allowlist.

Therefore the existing verified mechanism cannot perform an identical provider attempt for all four exact task models.

Executing Luna/Terra/Sol now and leaving Astra locally blocked would produce a deliberately incomplete matrix and consume three live attempts before the common mechanism is corrected. That would violate the task's requirement for a four-model identical comparison and weaken comparability.

SIS therefore stopped before hidden TTY entry and before any provider call.

## Minimum unblock

KOD should provide an exact immutable runtime update/package that:
1. adds only `gpt-6-astra` to the existing model allowlist;
2. preserves the exact existing request shape, D0 synthetic prompt, output cap, no-tools/no-web/no-files boundary, retries=0 and fallback=none;
3. preserves hidden `/dev/tty` secret handling and no-persistence boundary;
4. updates tests/manifest/SHA identities;
5. passes independent verification before live execution.

Alternatively, KOO/OPERATOR may issue a different exact execution contract if Astra is intentionally to be tested outside the existing verified runtime, but SIS will not invent such an exception.

## Boundary

Provider attempts: `0`.
API key was not requested/read.
No runtime bytes were changed.
No credential/log artifact was created.
No Luna/Terra/Sol/Astra provider request was executed.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: остановить comparative live matrix до первого provider call из-за несоответствия exact verified runtime четырёхмодельной задаче
СТАТУС: `BLOCKED_OPENAI_COST_MATRIX_ASTRA_NOT_IN_VERIFIED_RUNTIME_ALLOWLIST`
