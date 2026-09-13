# KOO → OPERATOR: Telegram Phase 1B exact privilege-path dependency

status: `BLOCKED_WAITING_OPERATOR_AUTHORIZED_EXECUTION_DECISION`
source_result: `entities/sisadmin/outbox/SIS__telegram-phase1b-host-gate-r3-result__KOO.md`
source_result_commit: `1fd4db09e4d6561b5ef1a378c9ac0461a4236451`
koo_receipt: `routes/receipts/SIS__telegram-phase1b-host-gate-r3-result__KOO.receipt.md`
koo_receipt_commit: `a64892c129e399a31e0c410fe13c4c0e8e9f23f0`
host: `ruvds-xnqc6`
production: `no`
mazhor_allowed: `no`

## Exact dependency

SIS completed fresh read-only host-scope checks and found no candidate path/user/unit/port collision. The current authorized remote execution interface refused the privilege probe containing `sudo -n true` before command execution with `Command not allowed`.

The next causal step requires one of these authoritative outcomes from OPERATOR:

1. provide/authorize an execution path on `ruvds-xnqc6` that permits the exact privileged non-production provisioning and readback required by the already-issued SIS host-gate task; or
2. explicitly identify an already-approved mechanism through which SIS may perform that privileged provisioning/readback on the same host.

This task does **not** ask OPERATOR to disclose passwords, tokens, private keys, or other credentials into GitHub. Any credential-bearing action must stay outside the repository and use an approved secret/remote-execution mechanism.

After the dependency is satisfied, SIS must Resume-First and repeat fresh host-scope preflight before any mutation. KOO does not authorize another host, MAZHOR, production, live Telegram send, public webhook, or authority/writer expansion.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: адресовать ОПЕРАТОРУ точную внешнюю зависимость, которую SIS и KOO не вправе выдумывать или обходить
СТАТУС: BLOCKED_WAITING_OPERATOR_AUTHORIZED_EXECUTION_DECISION