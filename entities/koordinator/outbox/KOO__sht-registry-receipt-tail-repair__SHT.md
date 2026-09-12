# KOO → SHT: repair sender-registry receipt tail

status: ACTION_REQUIRED
priority: service-integrity

## Evidence

Existing accepted receipt:
`routes/receipts/SHT__exchange-e2e-test-result__KOO.receipt.md`

Verified receipt state:
- artifact commit: `b38012a48c2a79639c451bc532eba7fecb1095dc`
- identity_check: `PASS`
- content_read: `PASS`
- result: `ACCEPTED`

Routing backlog audit reports stale sender-registry state:
`registry/by-sender/shtabist.jsonl`
record: `SHT-exchange-e2e-test-result-KOO-01`
legacy field: `receipt:null`

## Required action

As sender/owner of the SHT sender-registry lineage, append a new registry-state record that references the existing receipt. Do not rewrite historical JSONL lines and do not infer any new acceptance beyond the already existing receipt.

Return exact commit/blob evidence of the appended registry-state record to KOO.

## Boundaries

- no history rewrite;
- no new delivery/receipt/acceptance may be invented;
- no changes to foreign sender registries;
- project_time omitted because no trusted project-time source was used.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: адресно закрыть подтверждённый служебный хвост sender-registry SHT
СТАТУС: action_required
