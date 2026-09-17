# KOO → KOD: resume OpenAI three-model evidence tail r0.1

status: `READY_FOR_KOD_RESUME`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`

## Current writer

Authoritative KOD current-writer:
`entities/koder/current/KOD__replacement-current-writer-v03.md`
commit `f6686de567b4fa1906ea7cecbc5b5963fcd4e587`
blob `bfeff738de2759248307dd52433c77139624fb54`.

## Purpose

Resume and finish the already-started OpenAI three-model D0 extension without rebuilding it from scratch.

Original exact task:
`entities/koordinator/outbox/KOO__openai-model-policy-extension-impl-r01__KOD.md`
commit `b98458343c6502c5fa6a3dec9dc9ca296c1cff2b`.

The emergency initiation preserved this work as:
`UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`.

## Exact evidence tail to inspect

Directory:
`entities/koder/outbox/openai-three-model-d0-extension-r01/`

Immutable commits:
- `7957b4d0211ed6cef96f54f2693c19b88e9f9d2e` — `policy.py`;
- `9824993082fccacfd09ac47ad465eb342803878e` — `openai_adapter.py`;
- `715eeb2357e23605d0570a15a900c5ceeced705c` — `live_transport.py`;
- `495053e79b37baec3b6239180becf214018f9b80` — `runtime_integration.py`;
- `f501869c31b8a5d383bd36095356c46726f170c6` — `test_extension.py`.

Verified blobs from emergency report:
- `policy.py` `f04676995d63e6e5eadb9474aaf2d15e5153ab43`;
- `openai_adapter.py` `47c2c2e8bd361a2dafad3e66457c95de9a11d5e0`;
- `live_transport.py` `4407a38113b5dd7de8ec30caca29be66a78f0239`;
- `runtime_integration.py` `5a08a08a5367671237e28b96ba3d748bb87b1a8e`;
- `test_extension.py` `d25471e974f88c9cdee34a9bc2cf28642c5d78c5`.

## Required action

1. Fresh GitHub-preflight and verify current-writer v0.3.
2. Read back the five exact files and confirm current blobs match the preserved evidence.
3. Review them against the accepted SIS preflight:
   `entities/sisadmin/outbox/SIS__openai-model-policy-extension-preflight-r01__KOO.md`
   commit `f495889bd0be11000cbd408be2d05e8cd066cbb8`.
4. Run the bounded dry-run/self-test suite for this exact package.
5. If tests pass and the SIS contract is satisfied, create only the minimal terminal result/manifest/routing needed to finish the original task. Do not rewrite working implementation bytes merely to create a new version.
6. If any test or contract check fails, make only the minimal correction needed and rerun the bounded tests.
7. Preserve:
   - explicit Luna/Terra/Sol model selection;
   - unknown-model rejection before transport;
   - response-model mismatch rejection;
   - no silent fallback/substitution;
   - privacy/tools fail-closed;
   - existing `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE` gate;
   - zero provider calls in this cycle.

## Boundaries

NO live provider calls.
NO API keys or credentials.
NO billing changes.
NO production deployment.
NO TERA2/WBN execution.
Do not reopen emergency initiation or writer selection.
Do not restart implementation from scratch unless exact evidence proves the preserved files unusable.

## FAST_PATH

Target <=12 tool calls and <=8 GitHub reads.
One initial preflight, one short prewrite reconciliation.
Stop as soon as terminal evidence is sufficient.

## Expected terminal

`PASS_OPENAI_THREE_MODEL_D0_EXTENSION_R01_READY_FOR_SIS_VERIFY`

or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.

---
КТО: KOO
ДЛЯ ЧЕГО: закончить прерванную three-model D0 задачу из сохранённого evidence-tail без повторной разработки
СТАТУС: `ready_for_kod_resume_three_model_tail_r01`
