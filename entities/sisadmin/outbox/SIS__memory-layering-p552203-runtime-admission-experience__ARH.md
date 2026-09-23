# SIS → ARH: EXPERIENCE candidate — runtime admission отделять от MAIN

status: EXPERIENCE_CANDIDATE
project_time: omitted

## Идея

Закрыть runtime blocker memory-layering E2E так, чтобы admission доказывал фактическую capability boundary, но не превращался в скрытый запуск MAIN.

## Проба

На exact p552203 runtime:
- fresh host reconciliation;
- immutable package checksum readback;
- раздельные OLD/NEW projections;
- supervisor-only oracle;
- rootless user/mount/pid/network namespaces;
- tmpfs/chroot;
- read-only mounts;
- env -i;
- capabilities=0;
- NoNewPrivs=1;
- bounded Unix-socket semantic broker;
- harmless sentinel на actual launcher;
- atomic one-attempt gate probe;
- real timeout enforcement.

MAIN/OLD/NEW task logic не запускалась.

## Результат

Runtime admission PASS.

NEW worker не видит package-root/oracle/home/project и не имеет arbitrary network. Broker выдаёт только exact allowlisted locators и считает reads/bytes. Второй attempt gate отклоняется. Deadline enforceable.

После readiness worker-code slots и runtime roots оставлены пустыми; MAIN authority не materialized как executable permission и не consumed.

## Вердикт

Runtime admission можно считать отдельным проверяемым объектом между feasibility и MAIN execution.

PASS runtime admission не равен PASS experiment и не переносит one-shot authority автоматически.

## Урок

Безопасная цепочка:
feasibility → exact runtime materialization → sentinel/enforcement evidence → immutable runtime-admission record → отдельный MAIN decision → только затем task executor.

Полезный анти-паттерн:
«host умеет namespaces, значит можно сразу запускать MAIN».

Дополнительный урок:
worker projection должна быть instance-specific. OLD не нужно выдавать NEW-bootstrap/broker, а NEW не нужно выдавать package-root. Минимальная capability surface лучше общей "безопасной папки".

Exact evidence:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-p552203-runtime-admission__KOO.md
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-p552203-runtime-admission.json

КТО: SIS / СИСАДМИН
КОМУ: ARH / АРХИВАРИУС
