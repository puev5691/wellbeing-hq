# КООРДИНАТОР — рабочая очередь v0.13

Статус: `CURRENT_OPERATOR_QUEUE`
Режим: `WIP_LIMIT_2`
Проектное время не указывается.

## CLOSED PREVIOUS CYCLE

SIS OpenAI host-preflight:
`PASS_SIS_OPENAI_D0_HOST_PREFLIGHT_R01`.
OpenAI live/account lane теперь ждёт внешние зависимости: billing/account readiness, OPERATOR-created API key, secret-safe injection и отдельное разрешение на один D0 synthetic live call.

KOD TERA2 root-profile candidate r0.2:
`PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW`.

## ACTIVE SLOT 1 — SHD / TERA2 semantic review

Exact task:
`entities/koordinator/outbox/KOO__tera2-root-profile-r02-review__SHD.md`
commit `dbbf5950a1657d92c683287905d11a1980d282a7`
blob `dddc8dd9f4d7d02d27b709b835de80ccae6cbe5e`.

`RECOMMENDED_REASONING: HIGH`.

Scope: independent semantic/chain-policy review of exact immutable TERA2 root-profile candidate r0.2. No runtime/genesis launch, no DATA/DB mutation, no credentials.

## ACTIVE SLOT 2 — SIS / TERA2 clean host/runtime preflight

Exact task:
`entities/koordinator/outbox/KOO__tera2-clean-runtime-preflight-r01__SIS.md`
commit `b7f493389bf69b385a691b53bf5dc87cfb0342f0`
blob `f3ba07266b72a2bad5f4d799313bbe3ed5b3f2c2`.

`RECOMMENDED_REASONING: MEDIUM`.

Scope: bounded non-privileged clean-directory host/runtime feasibility check. No node/genesis start, no DATA/DB creation/mutation, no credentials, no sudo/root.

## WAITING

### OpenAI live/account gate

Waiting for explicit external prerequisites:
- billing/account readiness;
- OPERATOR-created API key;
- approved secret-safe injection path;
- separate authorization for exactly one D0 synthetic live request.

Host preflight on `ruvds-xnqc6` already PASS.

### Telegram Phase1B

Still `BLOCKED_PRIVILEGE_REQUIRED` pending exact privilege/provisioning decision for accepted `/opt`/`/etc`/`/var/lib` runtime boundary.

### Recovery canon v1.5

Separate nonblocking OPERATOR gate remains ready.

## BACKGROUND

Retired Entity lifecycle study continues under v0.3 `CAPTURE_FIRST / COMPACT_TRANSPORT / EXTERNAL_COLLECTOR` and does not consume WIP slots.
Do not revise protocol again unless a concrete new defect is observed.

## Observability

Active tasks carry advisory reasoning metadata and should return compact observable telemetry only where actually evidenced: activation/first-work/terminal events, tool/GitHub calls, retries, reconciliations and re-wakes. Do not invent latency.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: запустить следующий TERA2 review/preflight cycle после двух PASS предыдущего цикла
СТАТУС: `CURRENT_OPERATOR_QUEUE_V13`
