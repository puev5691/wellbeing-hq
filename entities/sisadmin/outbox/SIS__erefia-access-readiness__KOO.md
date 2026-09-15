# SIS → KOO: readiness доступа к эРэФии

status: `WAITING_OPERATOR_EXACT_HUMAN_ACTION`
production_mutation: `no`
tera_wbn_mutation: `no`
telegram_phase1b: `PAUSED_BY_HIGHER_CURRENT_PRIORITY`
project_time: omitted; trusted project-time source not used

## Fresh Resume-First boundary

fresh_HQ_HEAD: `b5afbd9d7f50cb53751e55962503c850f1f8dd6e`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
competing_writer: `none_found_at_fresh_boundary`

Exact KOO task:
`entities/koordinator/outbox/KOO__sis-current-priority-erefia-access__SIS.md`
commit `bcaeccfefb992aafab16c3c7b0678d0072c65a5e`
blob `6e0c6e2dde96699c867d197207c872748ceb77b7`.

## Exact host lane

host_label: `эРэФия`
ssh_endpoint: `194.87.107.135:2222`
port_22_as_current_endpoint: `forbidden/not_used`

SHD correction evidence:
`entities/shardovik/outbox/SHD__erefia-ssh2222-correction__SIS.md`
commit `9b257f36c02cde9dcaec680aa4190b2ac7011705`
blob `db749700ca2b4ce8c49bdb0ef54fbe400954dddb`.

## Что реально проверено

1. Remote Desktop Commander `list_devices`:
   - `ruvds-xnqc6` — online;
   - `p552203.kvmvps` — online;
   - `ruvds-ygo0w` — offline, device id `c55d5659-f2c8-416d-8b40-9bac8c80c30d`.
   Связь `ruvds-ygo0w` ↔ эРэФия по текущим проверяемым данным не доказана, поэтому не утверждается.

2. С Буржуинии `ruvds-xnqc6`:
   - TCP `194.87.107.135:2222` — `OPEN`;
   - локальный пользователь — `pev5691`;
   - `~/.ssh/config` отсутствует;
   - batch SSH `pev5691@194.87.107.135:2222` → `Permission denied (publickey,password)`;
   - локальный ssh-agent недоступен;
   - отдельного ключа эРэФии в metadata `~/.ssh` не найдено.

3. С МАЖОРа `p552203.kvmvps`:
   - локальный пользователь — `shd`;
   - batch SSH `shd@194.87.107.135:2222` → `Permission denied (publickey,password)`;
   - отдельного клиентского SSH key для этого lane в `~/.ssh` не обнаружено.

4. SHD ранее подтвердил на exact endpoint:
   - TCP 2222 OPEN;
   - SSH banner `SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.18`;
   - sshd отвечает штатно.

Вывод: сетевой путь и sshd доступны. Текущий blocker — отсутствие подтверждённого работающего административного SSH credential path из доступных SIS-controlled hosts и отсутствие доказанной связи offline Commander device с exact host.

## Commander state

`NOT_READY_ON_EXACT_HOST`.
Ни один online Commander device не доказан как `194.87.107.135`.
Offline `ruvds-ygo0w` не может быть опрошен инструментом в текущем состоянии.

## Exact human action

ОПЕРАТОРУ выполнить ровно одну операцию:

**Войти по SSH на `194.87.107.135:2222` теми действующими административными credentials, которыми он обычно управляет эРэФией, и выполнить:**
`hostname && id -un`

Вернуть SIS только две строки вывода. Пароль, приватный ключ, токен или иные credentials в чат/GitHub не передавать.

После этого SIS сможет доказать host identity/username и продолжить только bounded восстановление Remote Desktop Commander, не касаясь TERA/WBN runtime.

## Boundary

TERA/WBN service, chain identity, DB, DATA, genesis/reward logic, shard.js, const.lst, blockchain ports, nginx, Xray, UFW и DNS не менялись.
Credentials не создавались, не читались и не публиковались.
Telegram Phase1B не возобновлялся и параллельно не исполнялся.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: вернуть проверяемый readiness/blocker exact эРэФия access lane
СТАТУС: waiting_operator_exact_human_action