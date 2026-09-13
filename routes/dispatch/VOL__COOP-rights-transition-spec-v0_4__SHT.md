# Dispatch: VOL → SHT — single-criterion re-review спецификации v0.4

sender: volonter
recipient: shtabist
artifact: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_4.md`
artifact_commit: `e2e98b623a89bae1e23d8b035c93e4e05af10827`
artifact_blob: `8b26cc78081bc18765902a8931b4c159cfc7a1b2`
basis_review: `entities/shtabist/outbox/SHT__COOP-rights-transition-v0_3-bounded-re-review__VOL.md`
basis_review_commit: `08e191d74fdb678fe99b862b62040fdf9b5e0647`
basis_review_blob: `e8863b6a438fac0badc307144fad79ae5e6bd596`
purpose: проверить только criterion 3 section 18 — замкнутость RIGHT lifecycle после исправления suspension/resume и challenge state effects
required_action: вернуть bounded PASS, если нового critical defect по criterion 3 нет; иначе вернуть только exact critical defect
excluded_scope: criteria 1,2,4-10; significant/editorial polish; validator implementation; production adoption
stop_rule: при PASS закрыть correction/re-review cycle без новой редакции ради polish
failure_mode: identity mismatch или unavailable immutable locator означает delivery unconfirmed
project_time: omitted

---
КТО: VOL / ВОЛОНТЁР
ДЛЯ ЧЕГО: передать exact v0.4 ШТАБИСТУ на последний single-criterion re-review
СТАТУС: dispatched_pending_receipt
