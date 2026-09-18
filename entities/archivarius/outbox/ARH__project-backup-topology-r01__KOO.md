# ARH: project backup topology / cadence proposal r0.1

status: `PROPOSAL_READY_FOR_OPERATOR_DECISION`
project_time: omitted; trusted project-time source not used

## Предлагаемая топология

### Layer 1 — primary Git

Рабочие repositories остаются primary authoritative surfaces. Git commit/blob identity используется как version identity, но primary provider не считается backup самому себе.

### Layer 2 — independent repository mirror

Для каждого critical repository: независимый bare/mirror clone на другом storage/provider/host. Mirror должен сохранять refs и Git object database. После обновления фиксируется exact source HEAD и mirror readback.

### Layer 3 — local/offsite archive

Периодический non-secret archive checkpoint критичных repositories и разрешённых non-Git данных. Архив получает manifest + SHA-256 + locator + immutable/archive identity. Хотя бы одна копия должна быть независима от primary Git provider и от host, потеря которого инициирует recovery.

### Layer 4 — entity recovery packages

Существующие recovery/current, immutable versions и preservation packages сохраняются как continuity layer Сущностей. Они дополняют repository backup, но не заменяют его.

### Layer 5 — host/lab archive

Для runtime/lab hosts сохраняются только необходимые non-secret state, scripts, reports, artifacts и воспроизводимые inventories. Большие/изменяемые data directories включаются только после профильной классификации SIS/SHD. Secrets не копируются этим механизмом.

## Cadence proposal, automation NOT enabled

- milestone: preservation после major accepted milestone / writer handoff / перед destructive or replacement operation;
- repository mirror: регулярно, с периодом не длиннее будущего OPERATOR-approved RPO;
- archive checkpoint: периодически и после существенных infrastructure milestones;
- readback: после каждой новой immutable/archive publication;
- restore drill: периодически на отдельную временную площадку, с проверкой manifest, checksum, Git fsck/refs и способности открыть recovery package.

## Acceptance evidence

Backup считается подтверждённым только при наличии:
source identity → destination locator → immutable/version identity → checksum/structural verification → readback receipt.

Restore-ready требует отдельного drill evidence. Успешный backup readback не равен успешному restore drill.

## OPERATOR decisions

1. RPO: сколько последних изменений допустимо потерять при аварии.
2. RTO: сколько времени допустимо восстанавливать critical contour.
3. Какая независимая площадка разрешена для mirror/offsite archive.
4. Какие repositories считаются critical и входят в первую волну.
5. Какие host/lab datasets, кроме Git, действительно требуют backup.
6. Каким отдельным механизмом обеспечивается disaster recovery secrets/credentials; обычные ARH archives должны оставаться secret-free.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: topology/cadence proposal без включения automation
СТАТУС: `proposal_only`
