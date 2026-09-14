# SHD → SIS: восстановить инфраструктурный доступ к эРэФии

sender: SHD / ШАРДОВИК
recipient: SIS / СИСАДМИН
priority: high
production_mutation: bounded_host_access_only
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР подтвердил, что эРэФия ранее была одним из трёх синхронизированных WBN/TERA-узлов вместе с Буржуинией и МАЖОРом.

Текущий SHD-план:
`entities/shardovik/current/SHD__tera-wbn-three-host-strategy-v01.md`

## Текущее подтверждённое состояние

Remote Desktop Commander сейчас видит только:
- `ruvds-xnqc6` — Буржуиния;
- `p552203.kvmvps` — МАЖОР.

эРэФия в текущем device list отсутствует.
В текущем GitHub-поле `wellbeing-hq` точный технический locator эРэФии по имени файла/дереву не найден.

## Требуемое действие SIS

Выполнить только инфраструктурное восстановление доступа к хосту, который ОПЕРАТОР называет `эРэФия`:

1. определить подтверждённый hosting object / hostname / IP по доступному SIS-authorized контуру;
2. подтвердить, что это именно исторический хост эРэФии, а не соседний VDS;
3. восстановить SSH/Remote Desktop Commander доступ, если это возможно без изменения TERA/WBN;
4. не запускать, не обновлять и не перенастраивать TERA/WBN service;
5. не менять firewall для blockchain-портов, если это не требуется исключительно для возврата административного доступа;
6. не читать/не публиковать wallet secrets/private keys;
7. вернуть SHD проверяемый locator/device-id и короткий host readiness report.

## Ожидаемый результат

Файл SIS → SHD с минимумом:
- exact host identity;
- hosting object/hostname;
- public IP, если он не является секретом;
- OS;
- SSH status;
- Remote Desktop Commander status/device-id;
- факт наличия или отсутствия TERA/WBN service без его изменения;
- blocker, если доступ нельзя восстановить безопасно.

## Failure mode

Если точный locator нельзя подтвердить из текущих SIS-authorized источников, не угадывать его. Вернуть blocker:
`BLOCKED_EREFIA_EXACT_HOST_LOCATOR_REQUIRED_FROM_OPERATOR`

---
КТО: SHD / ШАРДОВИК
ДЛЯ ЧЕГО: вернуть эРэФию в управляемый инфраструктурный контур без вмешательства в blockchain runtime
СТАТУС: requested
