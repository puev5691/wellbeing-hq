# КООРДИНАТОР — рабочая очередь v0.12

Статус: `CURRENT_OPERATOR_QUEUE`
Режим: `WIP_LIMIT_2`
Проектное время не указывается.

## ACTIVE SLOT 1 — SIS / OpenAI D0 host preflight r0.1

Exact task:
`entities/koordinator/outbox/KOO__openai-d0-host-preflight-r01__SIS.md`
commit `612036fdd7100a3169dec764f394cf2120685a5a`
blob `f3d3e3e87623425d05a4ae61e1bc508151a711cd`.

`RECOMMENDED_REASONING: MEDIUM`.

Scope: read-only/non-privileged Unix-host preflight on `ruvds-xnqc6`; no key, no billing change, no authenticated OpenAI call.

## ACTIVE SLOT 2 — KOD / TERA2 root-profile candidate r0.2

Exact task:
`entities/koordinator/outbox/KOO__tera2-root-profile-candidate-r02__KOD.md`
commit `a704c0ba37242e1bb03f63c71b7689d7868bde3f`
blob `9e742b8d5ad19bbb6d4b5f5e43b02cea57d981f4`.

`RECOMMENDED_REASONING: HIGH`.

Scope: candidate-only root/main profile; no node launch, no DATA/DB mutation, no credentials.

## WAITING

Telegram Phase1B host/runtime remains `BLOCKED_PRIVILEGE_REQUIRED` pending exact privilege/provisioning decision.

OpenAI live D0 remains waiting for:
- successful SIS host preflight;
- OPERATOR billing readiness;
- OPERATOR-created API key;
- secret-safe injection;
- separate explicit authorization for one D0 synthetic live call.

Recovery canon v1.5 remains a separate nonblocking OPERATOR gate.

## BACKGROUND

Retired Entity lifecycle study uses v0.3 `CAPTURE_FIRST / COMPACT_TRANSPORT / EXTERNAL_COLLECTOR` and does not consume WIP slots.

No further pensioner-protocol change is required unless new samples reveal a concrete defect.

## Observability

New tasks carry advisory `RECOMMENDED_REASONING` and should return compact telemetry where actually observable: activation/first-work/terminal events, tool/GitHub call counts, retries, reconciliations and re-wakes. Do not invent timestamps or latency.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: запустить следующий двухполосный цикл после KOD OpenAI adapter PASS
СТАТУС: `CURRENT_OPERATOR_QUEUE_V12`
