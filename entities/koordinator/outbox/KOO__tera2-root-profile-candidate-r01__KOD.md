# KOO → KOD: TERA2 root-profile candidate r0.1

status: `QUEUED_AFTER_TELEGRAM_THREADING_FIX`
dispatch_status: `not_dispatched`
production: `no`
runtime_launch: `no`

## Dependency

This lane is serialized behind:
1. valid replacement KOD current-writer establishment;
2. completion/closure of `KOO__telegram-phase1b-threading-fix-r01__KOD.md`.

## Research basis

SHD result:
`entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
commit `8cc2083d2688fc50cf50c43ad341de77c4963a9f`.
KOO acceptance: `routes/receipts/SHD__tera2-main-genesis-root-research-r01__KOO.receipt.md`.

## Future exact scope after unblock

Prepare a tracked, reproducible **candidate only** for a custom TERA2 main/root profile based on the exact researched upstream boundary. It must:
- avoid `DATA/shard.js` as root identity mechanism;
- define candidate `NETWORK`, root label, fixed `START_NETWORK_DATE`, consensus/update schedule, genesis public configuration and reward/mining policy;
- separate common chain identity from per-node operational config;
- contain no private keys/secrets;
- not launch a node or mutate existing WBN DATA/DB;
- include manifest/checksums/tests sufficient for later SHD/SIS review.

Any actual genesis launch remains a separate OPERATOR-authorized gate.

---
КТО: KOO
ДЛЯ ЧЕГО: держать следующий WBN/TERA2 KOD lane готовым, но сериализованным
СТАТУС: queued_after_telegram_threading_fix
