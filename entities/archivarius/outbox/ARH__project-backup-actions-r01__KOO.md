# ARH: project backup implementation actions r0.1

status: `WAITING_OPERATOR_DECISIONS`
project_time: omitted; trusted project-time source not used

## Exact next actions

1. ОПЕРАТОР: установить RPO и RTO и разрешённую независимую backup площадку.
2. KOO: после решения ОПЕРАТОРА зафиксировать critical repository/data-surface scope и раздать implementation tasks.
3. SIS: проверить storage/provider/host для independent bare mirrors и offsite archives; подтвердить доступность, capacity, permissions и secret boundary без чтения secrets.
4. KOD: только после утверждения topology/cadence подготовить idempotent mirror/archive/readback tooling; automation не включать до отдельного разрешения.
5. ARH: определить manifest/index schema, правила immutable identity/checksum/readback и project-wide backup registry.
6. SIS/SHD: отдельно проверить Mazhor locator `/data/wellbeing-lab/backups/shd-pre-reinit-v01` на самом host и провести bounded restore/readback drill в разрешённую временную директорию.
7. После реализации: ARH выполняет независимую проверку первого полного цикла и только тогда меняет статус с proposal на verified backup topology.

Никакие cron/systemd/automation в этом цикле не включались. Recovery/current pointers не менялись. Secrets не читались и не копировались.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: exact implementation handoff
СТАТУС: `waiting_operator_decisions`
