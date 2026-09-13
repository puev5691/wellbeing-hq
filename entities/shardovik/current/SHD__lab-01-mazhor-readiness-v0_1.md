# SHD / ШАРДОВИК: lab-01 Mazhor readiness v0.1

Кратко: `Мажор / p552203.kvmvps` подтверждён как рабочий кандидат `lab-01` для SHD-экспериментов. Базовая ОС, пользователь `shd`, sudo и Remote Desktop Commander agent проверены по выводу ОПЕРАТОРА и частичному tool evidence. Канал Remote Desktop Commander нестабилен по heartbeat, но агент сам восстанавливает channel и один ping от ChatGPT уже был обработан.

## 1. Scope

Это readiness-файл для текущей ручной настройки SHD sandbox. Это не production deployment, не acceptance будущей WBN/TERA2 архитектуры, не разрешение трогать `Буржуинию`, не задача СИСАДМИНУ.

## 2. Подтверждённые параметры host

Source: operator shell output from `Мажор`.

```text
hostname: p552203.kvmvps
os: Ubuntu 24.04.1 LTS
kernel: Linux 6.8.0-51-generic
virtualization: microsoft
ip: 130.49.174.162/24 on eth0
ssh: LISTEN *:22
failed systemd units: 0
disk root fs: 30G total, 3.1G used, 25G available
memory: 1.9GiB total, 1.4GiB available
swap: 0B
```

## 3. Подтверждённый working user

Source: operator shell output.

```text
user: shd
home: /home/shd
uid: 1000
gid: 1000
groups: shd,sudo,users
sudo -n whoami: root
```

Interpretation: `shd` is a valid non-root working user with passwordless sudo for the lab setup. This is acceptable for the temporary isolated sandbox phase, but not a production security model.

## 4. Remote Desktop Commander state

Source: operator shell output from `tmux capture-pane`; account/email and nonessential identifiers intentionally redacted from this public project file.

```text
tmux session: desktop-commander active
node: /home/shd/.nvm/versions/node/v22.23.2/bin/node
agent: @wonderwhy-er/desktop-commander remote
state observed: Device ready
name observed: p552203.kvmvps
presence observed: visible as online
chatgpt ping observed in agent log: completed with pong
channel issue: repeated heartbeat timeout / offline / online cycles
self-heal observed: channel subscribed after reconnect attempts
```

Interpretation: Remote Desktop Commander is installed and running under `shd`. The channel is not fully stable, but it is operational enough to have processed one ChatGPT-origin ping. Further automated work must use one calm tool check per step and tolerate reconnect lag.

## 5. Current blockers

```text
BLOCKER-1: ChatGPT-side tool availability is intermittent in the current chat.
BLOCKER-2: Remote Desktop Commander channel on Mazhor shows heartbeat timeout cycles.
BLOCKER-3: No stable end-to-end command execution cycle has yet been recorded after the successful ping.
```

## 6. Explicit prohibitions after incident

Do not:

- touch `ruvds-xnqc6 / Буржуиния` for Mazhor setup;
- create SSH bridges through production-like hosts;
- run repeated list/ping checks without waiting for lag;
- use nested quoted shell blocks in Android/mobile terminal instructions;
- install WBN/TERA2 or expose extra ports before base lab workspace is created and verified;
- publish passwords, private keys, tokens, full auth logs, or account email in public GitHub.

## 7. Next safe step

When Remote Desktop Commander is available again, perform exactly one direct check on `p552203.kvmvps`:

```text
list_devices -> confirm p552203.kvmvps online
ping device -> confirm pong
start_process on p552203 only -> one read-only whoami/pwd/id check
```

If the tool remains unavailable, continue by operator shell, one simple block at a time.

## 8. Experience note

Идея -> подключить `Мажор` как отдельный SHD sandbox host.
Проба -> root login, user `shd`, nvm/node/tmux/Desktop Commander remote agent.
Результат -> host base verified; agent running; ping once processed; channel heartbeat unstable.
Успех/неудача -> partial success; process discipline failure occurred due to rushed checks and side-route via `Буржуиния`.
Фиксация -> continue only with single-step calm checks; no Burzh route; no nested mobile shell blocks.

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: зафиксировать readiness v0.1 `Мажор / lab-01` после ручной настройки и дисциплинарной коррекции  
СТАТУС: readiness_partial_pass_waiting_stable_rdc_cycle