# SHD / ШАРДОВИК: lab-01 Mazhor connection preflight

Кратко: выполнена первичная безопасная проверка доступности `Мажор / p552203` как candidate host для `lab-01`. Прямой доступ ChatGPT к самому хосту ещё не установлен: Remote Desktop Commander видит только `ruvds-xnqc6`. Проверка выполнена с уже подключённого устройства `ruvds-xnqc6` как внешний network probe.

## Input

ОПЕРАТОР попросил подключаться к `Мажор`.

Из предыдущей карточки host candidate:

```text
host label: Мажор / mazhor
panel hostname: p552203.kvmvps
IP: 130.49.174.162
OS shown: Ubuntu 24.04
```

## Tool/device state

Remote Desktop Commander visible device list:

```text
online: ruvds-xnqc6
not visible: mazhor / p552203
```

Следовательно прямого Desktop Commander канала к `Мажор` пока нет.

## Network probe

Probe source:

```text
ruvds-xnqc6
```

Target:

```text
130.49.174.162
```

Observed result:

```text
ping: PASS, 3/3 received, 0% loss
rtt: 55.361 / 56.949 / 58.922 ms
tcp/22: open
tcp/2222: closed_or_filtered
```

## Interpretation

`Мажор` reachable from `ruvds-xnqc6`; standard SSH port 22 appears open. This does not prove credentials, OS cleanliness, hostname correctness inside guest, user availability, firewall policy completeness, or root access.

## Required next action

Choose one access path:

```text
A. Install/connect Remote Desktop Commander agent on Мажор.
B. Provide SSH access method through approved safe channel.
```

Recommended route if no valuable data exists on VPS:

```text
1. Reinstall clean Ubuntu 24.04.
2. Enable SSH on port 22.
3. Use key-based access or temporary password handled outside public GitHub/chat artifacts.
4. Let SHD run read-only base readiness checks.
5. Only after report, install lab packages.
```

## Boundary

- No login was performed.
- No password/token/secret was received or stored.
- No production change was made.
- No SIS task was opened.
- No claim of host readiness beyond network reachability is made.

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: зафиксировать безопасную первичную проверку доступности `Мажор` перед подключением  
СТАТУС: network_preflight_pass_waiting_access_method
