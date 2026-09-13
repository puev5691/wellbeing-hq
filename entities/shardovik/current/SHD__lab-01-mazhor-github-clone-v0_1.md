# SHD / ШАРДОВИК: lab-01 Mazhor GitHub clone/readback v0.1

Кратко: на `Мажор / p552203.kvmvps` выполнен read-only HTTPS clone репозитория `puev5691/wellbeing-hq` в `/data/wellbeing-lab/repos`. Получены HEAD commit и SHA-256 `README.md`. Это подтверждает минимальную пригодность `lab-01` для чтения GitHub-источников и локальной checksum-проверки.

## Scope

Фиксируется только read-only clone/readback step.

Не фиксируется:

- запись из `Мажора` в GitHub;
- наличие GitHub credentials/tokens на host;
- production deployment;
- запуск WBN/TERA2;
- изменение firewall или SSH policy;
- стабильный Remote Desktop Commander command-cycle.

## Operator shell evidence

ОПЕРАТОР выполнил команду через SSH на `shd@130.49.174.162`.

Рабочая директория:

```text
/data/wellbeing-lab/repos
```

Команда выполнила:

```text
git clone --depth 1 https://github.com/puev5691/wellbeing-hq.git
cd wellbeing-hq
git rev-parse HEAD
git status --short
test -f README.md && sha256sum README.md
```

Observed output:

```text
Cloning into 'wellbeing-hq'...
remote: Enumerating objects: 1764, done.
remote: Counting objects: 100% (1764/1764), done.
remote: Compressing objects: 100% (1310/1310), done.
remote: Total 1764 (delta 466), reused 1661 (delta 444), pack-reused 0 (from 0)
Receiving objects: 100% (1764/1764), 1.88 MiB | 6.24 MiB/s, done.
Resolving deltas: 100% (466/466), done.
6c5bbfc1f54ce7b66463d71d9326075de60d9774
a7939563d87d2109ae0c3e34b83c8798089d5be4ae1fd4407809c953ca2f5bd6  README.md
```

`git status --short` produced no visible status lines in the operator output. Interpretation: working tree appeared clean after clone.

## Interpretation

`Мажор / lab-01` can read the public GitHub repository over HTTPS and compute local file checksums.

The observed HEAD commit matches the commit that created the previous SHD marker/inventory GitHub fixation:

```text
6c5bbfc1f54ce7b66463d71d9326075de60d9774
```

This makes the clone suitable as a read-only source mirror for the next bounded prototype steps.

## Next allowed step

Next safe step: create a minimal local `pwh-prototype-v0_1` directory under `/data/wellbeing-lab/scripts` and implement a local JSONL hashchain prototype using non-secret GitHub artifact metadata.

Do not yet:

- install Docker/Podman;
- run WBN/TERA2;
- expose additional ports;
- create GitHub write credentials on host;
- use `ruvds-xnqc6 / Буржуиния`.

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: зафиксировать read-only GitHub clone/checksum step на `Мажор / lab-01`  
СТАТУС: github_readonly_clone_pass