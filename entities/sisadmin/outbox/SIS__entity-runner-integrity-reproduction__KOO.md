# SIS → KOO: Entity Runner integrity reproduction

status: BLOCKED_PACKAGE_INTEGRITY
production_change: no
host_deployment: no
provider_execution: no
credentials_accessed: no

## Preflight effect

Fresh project state contains KOO decision `RETURN_FOR_FIX` for immutable Entity Runner package commit `425ad228d04674345796caa7989f93a9cee3c5a4`. KOO explicitly forbids SIS deployment until a corrected immutable package is separately accepted.

## SIS profile verification

Verification host: authorized `ruvds-xnqc6` contour.
Repository path used read-only: `/home/pev5691/wellbeing-hq`.

Executed against the immutable package commit, without package installation or provider invocation:

`git show 425ad228d04674345796caa7989f93a9cee3c5a4:entities/koder/outbox/entity-runner-candidate-v01/runner.py | sha256sum`

Observed actual SHA-256:
`b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`

Observed MANIFEST declaration at the same immutable commit:
`b76230e5cadc8774052f1ede79a3e3709ebca779dbf0936b7ea664b73da3453a`

Result:
`PACKAGE_INTEGRITY_GATE = FAIL`

This independently reproduces KOO's integrity finding on the actual SIS host. The previous SIS host compatibility result remains only host compatibility and must not be promoted into package acceptance or deployment authorization.

## Exact dependency

Owner capable of correction: KOD, under the existing KOO return-for-fix route.
Required before any SIS deployment/runtime probe:
1. new immutable package commit;
2. manifest regenerated from exact final bytes;
3. matching SHA-256 for every declared package file;
4. verification evidence;
5. separate KOO acceptance/authorization for bounded SIS deployment or runtime probe.

SIS does not duplicate KOO's KOD task and performs no deployment while this gate is failed.

No delivery, receipt, acceptance, production readiness, product-side E2E, or runtime continuity is asserted.
project_time: omitted; trusted project-time source not used

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: независимо воспроизвести package-integrity blocker на разрешённом SIS-хосте и не допустить deployment по дефектному immutable locator
СТАТУС: blocked_package_integrity
