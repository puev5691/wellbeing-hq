# SHD / ШАРДОВИК: lab-01 Mazhor marker + inventory v0.1

Кратко: на `Мажор / p552203.kvmvps` созданы два локальных файла в `/data/wellbeing-lab/reports` и получены их SHA-256. Это подтверждает, что базовый workspace не просто создан, но пригоден для записи проверяемых отчётных файлов.

## Scope

Фиксируется только локальная запись двух файлов и их контрольные суммы.

Не фиксируется:

- стабильный Remote Desktop Commander command-cycle;
- установка Docker/Podman;
- запуск WBN/TERA2;
- изменение firewall;
- работа с секретами;
- участие `ruvds-xnqc6 / Буржуиния`.

## Operator shell evidence

ОПЕРАТОР выполнил команду через SSH на `shd@130.49.174.162`.

Созданы файлы:

```text
/data/wellbeing-lab/reports/LAB01_MARKER.txt
/data/wellbeing-lab/reports/host_inventory.txt
```

Полученные SHA-256:

```text
c1329555ed3e0341cbe3d37fed5e2739774f2195eb4916be0852f37a4f89d64e  /data/wellbeing-lab/reports/LAB01_MARKER.txt
cb1a5728287d23cf7e3d3fa484b6a44d5ef7a2e7937d45dd87d42320349797d3  /data/wellbeing-lab/reports/host_inventory.txt
```

Размеры и права:

```text
-rw-rw-r-- 1 shd shd   26 LAB01_MARKER.txt
-rw-rw-r-- 1 shd shd 1236 host_inventory.txt
```

## Interpretation

`/data/wellbeing-lab/reports` usable by `shd` for report artifacts.

The marker hash provides a simple baseline proof that write/read/hash cycle works in the lab workspace.

The inventory file is local evidence only. It is not yet copied into GitHub and not treated as a full host audit.

## Next allowed step

Next safe step: install only minimal verification tools if missing, then clone or fetch one GitHub repository in `/data/wellbeing-lab/repos` for read-only locator/checksum tests.

Do not yet install or run WBN/TERA2 node.

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: зафиксировать локальный write/hash readiness step на `Мажор / lab-01`  
СТАТУС: local_marker_inventory_created