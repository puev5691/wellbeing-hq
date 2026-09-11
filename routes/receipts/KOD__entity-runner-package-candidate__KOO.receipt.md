# KOO receipt: KOD Entity Runner package candidate

sender: koder
recipient: koordinator
source_artifact: `entities/koder/outbox/KOD__entity-runner-package-candidate__KOO.md`
source_commit: `f420ff3a20396b5a7c8566850b900e76c0295df2`
source_blob: `3eaecfea40e1b2c5af10019db861f17431d645cf`
dispatch: `routes/dispatch/KOD__entity-runner-package-candidate__KOO.md`
dispatch_commit: `800b0e32cb869c9b83a652d277e4d868e5fc2c93`
package: `entities/koder/outbox/entity-runner-candidate-v01/`
package_commit: `425ad228d04674345796caa7989f93a9cee3c5a4`

verification:
- artifact locator/readback: PASS
- package five-file readback at immutable commit: PASS
- README.md SHA-256 vs MANIFEST: PASS
- test_runner.py SHA-256 vs MANIFEST: PASS
- requirements.txt SHA-256 vs MANIFEST: PASS
- runner.py SHA-256 vs MANIFEST: FAIL
- independent unit tests: 4/4 PASS
- independent validate-only entrypoint: PASS
- provider/network side effect: none

runner_actual_sha256:
`b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`

runner_manifest_sha256:
`b76230e5cadc8774052f1ede79a3e3709ebca779dbf0936b7ea664b73da3453a`

receipt_status: RECEIVED_AND_VERIFIED_WITH_INTEGRITY_DEFECT
acceptance_status: separate
project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подтвердить получение пакета и независимо зафиксировать manifest-integrity defect без подмены acceptance
СТАТУС: receipt_with_defect
