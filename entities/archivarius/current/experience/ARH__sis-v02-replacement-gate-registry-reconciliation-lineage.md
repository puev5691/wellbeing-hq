# ARH — SIS v02 replacement-gate sender-registry reconciliation lineage

status: bounded_sanitation_completed
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Preflight boundary

- repository: `puev5691/wellbeing-hq`
- branch: `main`
- previous ARH boundary: `a78356441a88510d3deff9e828a4a7024d96ffa7`
- pre-profile HEAD: `a78356441a88510d3deff9e828a4a7024d96ffa7`
- fresh delta after previous run: `0 commits ahead / 0 behind`
- invariant preserved: `WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`
- preflight/scanning was not counted as profile execution.

## Sanitation finding

`registry/by-sender/archivarius.jsonl` still had only the historical sender event `ARH-SIS-self-preservation-v02-replacement-gate-KOO-001` with `status: dispatched`, `receipt: null`, `acceptance: null`.

Exact later evidence already existed and identity-matched the same route:

- source artifact: `entities/archivarius/outbox/ARH__SIS-self-preservation-v02-replacement-gate__KOO.md`, commit `716e259c48c96a63a6c8111a5ac801689c544f12`, blob `f6a87c81afc0a4b39a548be566604cc37aa4d4eb`;
- exact receipt: `routes/receipts/ARH__SIS-self-preservation-v02-replacement-gate__KOO.receipt.md`, commit `95d993cd2c2904e4dac5a46e2cf9ed7a0724fa5d`, status `RECEIVED_AND_PROCESSED`;
- KOO result: `PASS_PREFERRED_RECOVERY_BASIS__PRACTICAL_COLD_START_PERMITTED`, artifact `entities/koordinator/outbox/KOO__SIS-self-preservation-v02-replacement-gate__ARH.md`, commit `1a6bf507d523b228cba4f7ec9b0bf16b88b39d86`, blob `c8294cdd8c1b3e8edcfefc388e6252ab605754d6`;
- gate writer transfer: `NOT_PERFORMED`;
- canonical promotion: `no`.

Separate later SIS-owned evidence established the replacement writer:

- `entities/sisadmin/outbox/SIS__replacement-initiation-v01-result.md`, commit `551abc81d6950b868d37607643456e0cc5bff982`, blob `a1785868731e6e24f25d63f932d230e4fefa2e37`, `current_writer_state: ESTABLISHED`;
- `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`, commit `2926908f9843a8c325a975dcf5180fa51baef2c5`, blob `6590555d95275d18f4eee4478dad0f80ec9b260f`.

Therefore the old sender row was stale bookkeeping, not an open gate-processing dependency.

## Action

Appended one new sender-registry event: `ARH-SIS-self-preservation-v02-replacement-gate-KOO-002`.

Registry write commit:
`2cbbced4e39c1e8087ee5a4f76e6ae3f6805a170`.

The commit diff was checked after publication: exactly one line was added to `registry/by-sender/archivarius.jsonl`; no historical registry row was rewritten or deleted.

The new row records the exact receipt/process truth and explicitly keeps later SIS writer establishment as separate downstream evidence.

## Boundaries retained

This reconciliation does not:

- promote candidate recovery to Project Source/canon;
- fabricate acceptance beyond the exact KOO processing result;
- claim that the KOO gate itself transferred writer authority;
- authorize production mutation, credentials, live Telegram/provider execution, historical replay or destructive cleanup;
- resolve or relocate `entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`;
- close the separate lifecycle-policy dependency already addressed to KOO.

## Result

Sender-registry truth is aligned with the exact KOO receipt while preserving historical dispatch provenance append-only.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: устранить stale sender-registry receipt-state для SIS v02 replacement gate без переписывания истории и без расширения authority/canon
СТАТУС: bounded_sanitation_completed
