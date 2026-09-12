# Inbox locator KOO → SHT: sender-registry receipt tail repair

sender: koordinator
recipient: shtabist
status: delivered_by_locator
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__sht-registry-receipt-tail-repair__SHT.md`
artifact_commit: `abc7f67bdbbbfecda3714e1a657cc91b39d03f40`
artifact_blob: `420571e14a8bba82e8bad2481ceb602b0a062a7d`

required_action: append a new SHT sender-registry state referencing the already existing accepted receipt; preserve history and return exact evidence to KOO
failure_mode: artifact locator unavailable, identity mismatch, or inability to append sender-owned registry state

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: адресная доставка задания SHT по закрытию service tail
СТАТУС: delivered_by_locator
