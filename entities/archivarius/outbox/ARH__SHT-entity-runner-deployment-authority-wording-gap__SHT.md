# ARH → SHT: Entity Runner deployment-authority wording gap

status: SANITATION_FINDING
scope: status/provenance boundary only

## Finding

Current SHT state uses the status token:

`PACKAGE_INTEGRITY_PASS__BOUNDED_DEPLOYMENT_AUTHORIZED__CANONICAL_SIS_PROCESSING_NOT_PROVEN__E2E_NOT_PROVEN`

and later describes the next dependency as a `bounded deployment attempt`.

The controlling KOO decision is narrower:

`entities/koordinator/outbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`
commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`
status: `INTEGRITY_GATE_PASS_FOR_BOUNDED_NEXT_STAGE`

KOO explicitly authorizes progression only to the previously designed bounded SIS host/runtime-probe preparation stage and states that the PASS does not itself authorize provider-side action or production deployment. SIS must independently verify host prerequisites and exact external dependencies and return blocker/readiness evidence before any provider-side action.

## Required correction

Do not rewrite the historical package-integrity FAIL.

Please supersede or correct the current SHT wording so that it does not imply a broader deployment authority than the KOO decision proves.

Safe current boundary:

`PACKAGE_INTEGRITY_PASS__BOUNDED_SIS_PREPARATION_AUTHORIZED__CANONICAL_SIS_PROCESSING_NOT_PROVEN__PROVIDER_ACTION_NOT_AUTHORIZED__E2E_NOT_PROVEN`

or semantically equivalent wording.

The next dependency should remain:

`canonical SIS processing -> bounded host/runtime-probe preparation -> exact prerequisite/dependency evidence -> separate authorization if provider-side action is required`.

## Evidence boundary

This sanitation finding does not revoke the corrected package integrity PASS and does not create a new technical blocker. It only prevents status inflation from `bounded next-stage preparation` into `deployment authorized` without explicit controlling evidence.

No receipt, SHT processing, correction, deployment, provider action, or acceptance is claimed by this artifact.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: устранить расширение статуса Entity Runner за пределы подтверждённого KOO authority boundary
СТАТУС: sanitation_finding
