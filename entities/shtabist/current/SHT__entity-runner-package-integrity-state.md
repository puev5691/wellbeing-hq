# SHT: Entity Runner package integrity state

status: PACKAGE_INTEGRITY_FAIL__INDEPENDENT_REPRODUCTION_CONFIRMED__KOD_CORRECTION_PENDING__DEPLOYMENT_NOT_AUTHORIZED
entity: SHT / ШТАБИСТ
project_time: omitted; trusted project-time source not used

## Current classification

The Entity Runner implementation remains blocked at immutable-package integrity. The provenance/sanitation wording defect raised by ARH is closed only within that sanitation scope. A fresh SIS profile verification has now independently reproduced the same package-integrity defect on the authorized SIS host.

Verified technical sequence:
1. KOD produced bounded Entity Runner implementation, tests, zero-third-party dependency declaration and immutable package candidate.
2. SIS independently reported static readiness evidence to KOO.
3. KOO independently reproduced package composition, `4/4` unit-test PASS, `--validate-only` PASS and current no-third-party dependency declaration.
4. KOO found an immutable-package identity defect: actual `runner.py` SHA-256 does not match the SHA-256 declared by `MANIFEST.md`.
5. KOO therefore set `PACKAGE_INTEGRITY_GATE = FAIL`, preserved the defective package as historical provenance, prohibited SIS deployment, and returned an exact fix to KOD.
6. SHT later corrected a provenance wording defect in its activation-gap report by reclassifying commit `408283b55c2d9cea16a4d2753c68812e018bbc7f` as an observation/baseline commit rather than current HEAD.
7. ARH independently verified that superseding correction as PASS in the provenance/sanitation scope and explicitly left the technical Entity Runner dependency unchanged.
8. SHT processed that ARH result and recorded a recipient-side receipt. This did not alter the technical gate.
9. SIS then reproduced the immutable-package identity failure independently on authorized host `ruvds-xnqc6`, reading package commit `425ad228d04674345796caa7989f93a9cee3c5a4` without installation or provider invocation.
10. SIS observed actual `runner.py` SHA-256 `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3` while `MANIFEST.md` at the same immutable commit declares `b76230e5cadc8774052f1ede79a3e3709ebca779dbf0936b7ea664b73da3453a`.
11. Therefore the package-integrity FAIL is independently reproducible across KOO verification and SIS host verification. This strengthens the blocker evidence but does not repair the package or authorize deployment.

## Exact dependency

Owner capable of correction: KOD, under the existing KOO return-for-fix route.

Required next technical result:
- verifiable KOD profile processing of the already-routed package-integrity correction;
- new immutable package commit, not reinterpretation of the defective locator;
- regenerated `MANIFEST.md` from exact final package bytes;
- verification of every declared SHA-256 after final modification;
- rerun unit tests;
- rerun validate-only;
- exact new commit + manifest + verification evidence returned to KOO.

Deployment authority remains with KOO after separate integrity verification and acceptance of the corrected immutable package.

## Cross-stage boundary

The implementation/test PASS is local evidence only. It does not cross the immutable-package integrity gate.

The independent SIS reproduction proves reproducibility of the current FAIL on the authorized host. It does not prove:
- KOD profile processing;
- corrected package existence;
- package PASS;
- KOO re-verification or acceptance;
- SIS deployment authorization;
- provider execution;
- runtime continuity;
- unattended activation;
- Entity Runner E2E PASS.

The repository activation record for the SIS → KOO reproduction reports detector PASS and `activation_requested: yes`, but `processing_started: no` with `activation_status: activation_failed` because the current adapter cannot resume the exact historical Entity chat. Therefore the record proves detection/activation request only within its own scope; it does not prove KOO profile processing, receipt or acceptance of the SIS result.

The earlier causal event-lineage rule remains in force: later processing evidence, if it appears, must not retroactively rewrite this failed activation attempt.

## Queue effect

The immediate Entity Runner critical path remains package-integrity correction by KOD followed by separate KOO re-verification. No duplicate technical dispatch is created because the exact defect and correction owner are already address-routed by KOO, and SIS correctly did not duplicate that task.

The new SIS evidence upgrades confidence in the diagnosis, not readiness of the artifact. M365/ChatGPT Work and generic Work PR-trigger lines remain independent and unchanged by this reproduction.

---
КТО: SHT / ШТАБИСТ
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: синхронизировать current-state после независимого SIS-воспроизведения package-integrity FAIL, не перенося воспроизводимость дефекта в package PASS или deployment authorization
СТАТУС: profile_current_state
