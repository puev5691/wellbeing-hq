# KOO → SIS: Telegram Phase 1B resume gate r0.4

status: `TASKED_BOUNDED_NONPRODUCTION_RESUME_GATE`
entity: `SIS / СИСАДМИН`
production: `no`
live_telegram_send: `no`
public_webhook: `no`
real_credentials: `no`
project_time: omitted; trusted project-time source not used

## Current-writer basis

Replacement SIS current-writer artifact:
`entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
commit `2926908f9843a8c325a975dcf5180fa51baef2c5`
blob `6590555d95275d18f4eee4478dad0f80ec9b260f`.

Replacement initiation result:
`entities/sisadmin/outbox/SIS__replacement-initiation-v01-result.md`
commit `551abc81d6950b868d37607643456e0cc5bff982`.

## Preserved Phase 1B state

Historical one-shot was actually attempted once and returned:
`HOST_GATE=FAIL reason=user_collision`
`SCRIPT_RC=1`.

Subsequent SIS evidence observed the expected sandbox user/group/paths/unit already existing.

Resume-aware candidate exists at:
`/home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once-v2.sh`

Expected SHA-256 from preserved SIS state:
`1208ff4e123afcd407115c476c549b7c24730624dc2e01bd0c2751ad448e9d3d`.

The old one-shot command is NOT standing authority and must not be replayed.

## OPERATOR authority carried into this new exact task

OPERATOR previously authorized SIS to find and use any suitable technical path needed to configure the Phase 1B tooling, with OPERATOR participation where a human password/confirmation is actually required.

This task converts that standing direction into a fresh exact bounded resume gate after replacement recovery.

## Task

1. Fresh GitHub-preflight `puev5691/wellbeing-hq`.
2. Confirm exact replacement SIS current-writer identity and no competing writer evidence.
3. Use Remote Desktop Commander or another already authorized read-only path to fresh-check `ruvds-xnqc6` Phase 1B state.
4. Verify current user/group/directories/unit state relevant to the sandbox host gate.
5. Verify whether the resume-aware v2 script still exists and, if present, its exact SHA-256 against the expected value above.
6. Determine whether the host gate is already satisfied without any privileged mutation.
7. If not satisfied and the verified v2 script remains the minimal bounded fix, perform only that exact non-production host-gate step if the authorized execution interface can do so without credential publication or privilege-bypass improvisation.
8. If interactive human sudo/password entry is required, do NOT invent a workaround. Return exactly one short copy-paste Termux block for OPERATOR and stop in `WAITING_OPERATOR_EXACT_HUMAN_ACTION`.
9. After any authorized host-gate execution, read back exact evidence and return PASS or exact blocker.

## Hard boundaries

Do NOT:
- replay the historical v1 one-shot command;
- create permanent sudoers changes, root keys or persistent privileged credentials;
- send live Telegram traffic;
- create/expose bot token or webhook secret;
- enable public webhook;
- deploy production;
- mutate nginx/Xray/TERA2/UFW/DNS;
- touch MAZHOR;
- perform destructive cleanup.

## Required result

`entities/sisadmin/outbox/SIS__telegram-phase1b-resume-gate-r04__KOO.md`

Return one exact verdict:
- `PASS_PHASE1B_NONPRODUCTION_HOST_GATE`
- `WAITING_OPERATOR_EXACT_HUMAN_ACTION`
- `BLOCKED_PHASE1B_RESUME_CONFLICT`.

The result must state observed host state, v2 identity state, whether privileged execution occurred, and the exact next boundary.

Return through Exchange Gate.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: безопасно возобновить Telegram Phase 1B после replacement SIS без replay старого sudo шага
СТАТУС: tasked_bounded_nonproduction_resume_gate
