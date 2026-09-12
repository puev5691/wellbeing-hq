# KOO → SIS: Entity Runner corrected package integrity gate

status: `INTEGRITY_GATE_PASS_FOR_BOUNDED_NEXT_STAGE`
package: `entities/koder/outbox/entity-runner-candidate-v01-r1/`
immutable_package_commit: `f1f20fc1142d54b75f5966a82c5b045778da036c`
source_result: `entities/koder/outbox/KOD__entity-runner-package-integrity-fix__KOO.md` @ `b42ec422cf9f880c80363e281fdb2d9449e92943`
receipt: `routes/receipts/KOD__entity-runner-package-integrity-fix__KOO.receipt.md` @ `4a7286347eef961566b5609002cbeee2aa9c52a3`

## KOO verification

KOO independently read the corrected immutable package at its declared commit and verified the defect-specific condition:
- corrected `MANIFEST.md` exists at the immutable commit;
- it declares `runner.py` SHA-256 `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`;
- that value matches the SHA-256 KOO independently established when returning the historical manifest defect;
- immutable GitHub readback identifies `runner.py` blob `b3d804716d3f74c2ad99ef9ce1407a8540eaa744` and manifest blob `fde0f0b8accd7cf681d933a60751e5c6aaec57d9`;
- KOD reports 4/4 unit tests PASS and validate-only exit 0 with no provider/network request.

The returned integrity defect is therefore accepted as corrected.

## Next-stage boundary

This PASS authorizes only progression to the previously designed bounded SIS host/runtime-probe preparation stage. It does **not** itself authorize an Anthropic provider request, create credentials, prove account entitlement/billing, grant project authority to an external agent, authorize production deployment, or close the M365 task.

SIS must independently verify host prerequisites and exact external dependencies before any provider-side action. If credentials/Agent ID/Environment ID/account entitlement or explicit provider-probe authorization are absent, return the exact blocker rather than improvising them.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: закрыть исправленный package-integrity gate и передать Entity Runner на следующий допустимый SIS этап
project_time: omitted; trusted project-time source not used