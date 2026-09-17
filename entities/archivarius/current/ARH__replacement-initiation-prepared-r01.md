# ARH replacement initiation preparation — current state r0.1

status: `PREPARED_PENDING_KOO_VERIFICATION`
entity: `ARH / АРХИВАРИУС`
replacement_initiation: `not_started`
current_writer_change: `no`
current_arh_freeze: `not_performed`
canon_change: `no`
project_time: omitted; trusted project-time source not used

## Prepared basis

Fresh self-preservation candidate:
`puev5691/wellbeing-entity-bootstrap@5172d37f9a3560cd177b4fa39e2ead24bc5b458d:entities/arh/preservation/pending/pre-replacement-self-preservation-r02`

tree:
`acf8c2b583ef7d06319a68be21351adec5148544`

snapshot boundary:
`puev5691/wellbeing-hq@c83bf0e5cb5a38b4ce2d460d3d8d57ab4ff6b727`

self-check:
- composition `7_of_7_PASS`;
- published Git blob identities match precomputed final-byte identities;
- protected payload SHA-256 expected `6_of_6_PASS`;
- active approved Project Sources rehashed `5_of_5_PASS`.

KOO verification request:
`entities/archivarius/outbox/ARH__replacement-initiation-preparation-r02__KOO.md`
commit `11de303382ec9dabe406d66ec4e7197b0406acf1`.

KOO dispatch:
`routes/dispatch/ARH__replacement-initiation-preparation-r02__KOO.md`
commit `cbfd28e7473fea8376f7f92c2da7f12702c7222b`.

KOO inbox locator:
`entities/koordinator/inbox/ARH__replacement-initiation-preparation-r02__KOO.md`
commit `1899bfb80925ea94ffaaf139952ec72e24695ab2`.

Operator runbook:
`entities/archivarius/outbox/ARH__replacement-initiation-runbook-r01__OPERATOR.md`
commit `6e43042e986298104f86bc84710004c993163ec7`.

## Current boundary

Current ARH is NOT retired or frozen by this preparation and continues as the existing instance until an explicit later OPERATOR replacement decision.

Actual replacement may start only after:
1. exact KOO PASS for the freshest verified candidate;
2. fresh pre-handoff HQ reconciliation;
3. if needed, refresh of self-preservation because meaningful ARH self-state changed;
4. explicit OPERATOR replacement authority;
5. old-writer freeze/retirement;
6. cold-start verification and separate Writer Gate.

Pending tasks such as `KOO__RED-emergency-preservation-checkpoint-r01__ARH.md` remain pending/revalidation-only and are not executed by this preparation.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: current marker that replacement initiation is prepared but not started
СТАТУС: `PREPARED_PENDING_KOO_VERIFICATION`
