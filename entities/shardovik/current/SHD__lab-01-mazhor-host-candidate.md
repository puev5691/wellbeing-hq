# SHD / ШАРДОВИК: lab-01 candidate host — Мажор

Кратко: ОПЕРАТОР предоставил хостинг `Мажор` как экспериментальный сервер для SHD. Этот файл фиксирует host candidate для будущего `lab-01` sandbox. Это не production deployment, не задание СИСАДМИНУ и не разрешение на destructive reinstall без явного подтверждения ОПЕРАТОРА.

## 1. Источник вводной

ОПЕРАТОР предоставил скриншот панели хостинга и указал:

- пока не озадачивать СИСАДМИНА;
- хостинг `Мажор` отдаётся SHD для экспериментов;
- при необходимости ОПЕРАТОР может запустить чистую Ubuntu.

## 2. Наблюдаемые параметры со скриншота

```text
project label: Мажор / mazhor
panel hostname: p552203.kvmvps
IP: 130.49.174.162
OS shown: Ubuntu 24.04
CPU: 1 core
RAM: 2048 MB
disk shown: 7567 MB / 30720 MB
paid until: 17.10.2026 21:06
product: VPS-2-RU Lite, 1 month, 899 RUB
```

Эти данные являются screenshot-derived и требуют server-side verification перед любым техническим утверждением о фактическом runtime state.

## 3. Decision boundary

Recommended first decision:

```text
Use Мажор as lab-01 candidate for SHD experiments.
Do not involve SIS until base sandbox readiness is confirmed or a system-level blocker appears.
Do not touch existing production contours from this host.
```

Recommended reinstall decision:

```text
Clean Ubuntu 24.04 reinstall is preferred if ОПЕРАТОР confirms there is no valuable data on the VPS.
If valuable data may exist, first preserve minimal inventory before reinstall.
```

## 4. Target lab-01 model

```text
host: mazhor / p552203.kvmvps
purpose: isolated experiment sandbox
workspace: /data/wellbeing-lab
users: non-root working user preferred
network: SSH only at first
firewall: deny incoming except SSH until explicit service test
secrets: outside GitHub, mode 600, no QR/URI/tokens in repo
repos: GitHub clones with minimal required access
containers: Docker/Podman after base verification
remote control: Remote Desktop Commander only after minimal host hardening
```

## 5. First safe SHD action after clean OS

After ОПЕРАТОР completes reinstall and provides SSH-access method through an approved channel, SHD should run only a read-only/base-readiness pass first:

```text
uname -a
lsb_release -a || cat /etc/os-release
hostnamectl
id
whoami
ip -br addr
ss -ltnp
systemctl --failed --no-pager
df -h
free -h
```

Then create a host-readiness report in GitHub before installing heavy packages.

## 6. What not to do yet

Do not yet:

- run WBN/TERA2 node;
- expose ports 30000/8780/8781;
- install public web services;
- store project secrets;
- connect production GitHub tokens;
- claim runtime/source parity;
- use the host as public release surface.

## 7. Current SHD recommendation

Recommendation:

```text
Run clean Ubuntu 24.04 reinstall only if ОПЕРАТОР confirms the VPS contains no needed data.
After reinstall, provide SSH access path or connect Remote Desktop Commander.
Then SHD performs base readiness verification and writes report.
```

project_time: omitted; trusted project-time source not used

---
КТО: SHD / ШАРДОВИК
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: зафиксировать Мажор как кандидат lab-01 для экспериментального SHD-контура
СТАТУС: current_host_candidate_pending_clean_os_confirmation
