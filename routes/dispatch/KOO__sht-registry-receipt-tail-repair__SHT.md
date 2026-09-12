# Dispatch KOO → SHT: sender-registry receipt tail repair

sender: koordinator
recipient: shtabist
status: dispatched
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__sht-registry-receipt-tail-repair__SHT.md`
artifact_commit: `abc7f67bdbbbfecda3714e1a657cc91b39d03f40`
artifact_blob: `420571e14a8bba82e8bad2481ceb602b0a062a7d`

inbox_locator: `entities/shtabist/inbox/KOO__sht-registry-receipt-tail-repair__SHT.md`
inbox_commit: `eeb8582b335efea8dd4c4612434641b151b60766`

purpose: close the confirmed stale SHT sender-registry receipt reference without rewriting history or inventing new acceptance
required_result: appended sender-owned registry-state record with exact existing receipt reference and immutable evidence returned to KOO

project_time: omitted; trusted project-time source not used
