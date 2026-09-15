# KOO → SIS: Telegram Phase 1B resume after Erefia closure r0.5

status: `TASKED_RESUME_GATE`
production: `no`
live_telegram: `no`
credentials: `no`
project_time: omitted; trusted project-time source not used

## Basis

Erefia infrastructure lane is closed accepted by KOO:
- SIS result `entities/sisadmin/outbox/SIS__erefia-access-readiness__KOO.md`;
- result commit `26df12757efc46e4a7bcd9e049a86837930de061`;
- KOO acceptance commit `ead1e419947540af92b2f5537c4ba3ff324e8b7b`.

Telegram Phase1B had been paused only by that higher current priority. Historical r0.4 remains evidence, not an instruction to replay old sudo or host mutations blindly.

## Task

Resume only the Telegram Phase1B lane with fresh Resume-First:
1. fresh GitHub-preflight `puev5691/wellbeing-hq`;
2. verify current SIS writer/competing-writer boundary;
3. read current Phase1B r0.4 task/evidence and all newer SIS/KOO state;
4. revalidate exact current host/tooling state;
5. determine the smallest current non-production next step;
6. if interactive human/sudo action is truly required, return one exact Termux-compatible block and stop in `WAITING_OPERATOR_EXACT_HUMAN_ACTION`;
7. otherwise perform only bounded non-production verification and return the exact result.

## Forbidden

Do not:
- replay historical `phase1b-host-gate-once.sh` merely because it exists;
- send live Telegram messages;
- expose bot token/webhook secret;
- deploy public webhook or production service;
- mutate nginx/Xray/TERA2/UFW/DNS;
- perform destructive cleanup.

Expected result:
`entities/sisadmin/outbox/SIS__telegram-phase1b-resume-r05__KOO.md`

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: безопасно вернуть Telegram Phase1B в активную очередь после закрытия более приоритетной эРэФии
СТАТУС: tasked_resume_gate
