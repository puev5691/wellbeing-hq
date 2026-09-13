# SHD / ШАРДОВИК: lab-01 Mazhor workspace v0.1

Кратко: на `Мажор / p552203.kvmvps` создан базовый рабочий каталог `/data/wellbeing-lab` для SHD-экспериментов. Это пустая лабораторная структура, не production deployment и не запуск WBN/TERA2.

## Scope

Этот файл фиксирует только создание каталогов лабораторного workspace.

Не фиксируется:

- запуск blockchain/node/runtime;
- изменение firewall;
- изменение production services;
- подключение secret material;
- участие `Буржуинии`;
- готовность Remote Desktop Commander как стабильного канала управления.

## Operator shell evidence

ОПЕРАТОР выполнил команду через SSH на `shd@130.49.174.162` и прислал вывод `find /data/wellbeing-lab -maxdepth 2 -type d -printf ...`.

Подтверждённая структура:

```text
drwxr-xr-x shd:shd /data/wellbeing-lab
drwx------ shd:shd /data/wellbeing-lab/secrets
drwxr-xr-x shd:shd /data/wellbeing-lab/scripts
drwxr-xr-x shd:shd /data/wellbeing-lab/artifacts
drwxr-xr-x shd:shd /data/wellbeing-lab/reports
drwxr-xr-x shd:shd /data/wellbeing-lab/repos
drwxr-xr-x shd:shd /data/wellbeing-lab/logs
drwxr-xr-x shd:shd /data/wellbeing-lab/tmp
```

## Interpretation

`/data/wellbeing-lab` now exists and is owned by `shd:shd`.

`/data/wellbeing-lab/secrets` has restricted mode `700`. This is acceptable as an initial filesystem boundary, but it is not yet an approved secret-management model.

## Next allowed step

Next safe step: create one minimal local marker file and one inventory file under `/data/wellbeing-lab/reports`, then verify their paths and hashes.

Do not yet install Docker/Podman, WBN/TERA2, databases, web services, or expose additional ports.

## Boundary

- No production mutation was made.
- No credentials were published.
- No secrets were written to GitHub.
- No route through `ruvds-xnqc6 / Буржуиния` was used.
- No SIS task was opened.

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: зафиксировать создание базовой структуры `/data/wellbeing-lab` на `Мажор / lab-01`  
СТАТУС: workspace_created_partial_lab_ready
