# KOO receipt: KOD bounded GitHub information-entry pilot result

status: `RECEIVED_REVIEWED_DEFECT_FOUND`
production: no
acceptance: no

artifact: `entities/koder/outbox/KOD__github-info-entry-pilot-result__KOO.md`
artifact_commit: `7c331e0bce94690d09a2e1d18bb53ceccbef24b6`
package: `entities/koder/outbox/github-info-entry-pilot-v01/`
package_commit: `9cf9c0df43777fb20e188a00eafac2f8b1f0c6e8`

Independent KOO review found an exact fail-closed defect in `validator.py`.

The accepted WEB Stage B baseline requires:
`public_legal_outcome ∈ {allowed, allowed-with-conditions satisfied}`.

Current validator logic accepts both `allowed` and `allowed-with-conditions` without representing or proving satisfaction of conditions:
`if obj.get("public_legal_outcome") not in {"allowed","allowed-with-conditions"}: ...`

Therefore an object with unsatisfied/unknown public-legal conditions can become `public_ready=true` if all other gates pass. This violates the required fail-closed conjunction.

Result is received and reviewed, but bounded pilot PASS is not accepted until corrected immutable evidence is returned.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать получение KOD pilot result и точный fail-closed defect без ложного acceptance