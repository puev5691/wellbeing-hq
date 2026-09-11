# SHT: Entity Runner package integrity state

status: PACKAGE_INTEGRITY_FAIL__RETURNED_TO_KOD__DEPLOYMENT_NOT_AUTHORIZED
entity: SHT / ШТАБИСТ
project_time: omitted; trusted project-time source not used

## Preflight classification

Fresh project-field scan after SHT baseline `cfafa538b888144c5f5edeb2e28e89ccd8854e2e` found a concrete implementation advance and a new integrity blocker in the model-agnostic Entity Runner branch.

Verified sequence:
1. KOD produced bounded Entity Runner implementation, tests, zero-third-party dependency declaration and immutable package candidate.
2. SIS independently reported static readiness evidence to KOO.
3. KOO independently reproduced package composition, `4/4` unit-test PASS, `--validate-only` PASS and current no-third-party dependency declaration.
4. KOO found an immutable-package identity defect: actual `runner.py` SHA-256 does not match the SHA-256 declared by `MANIFEST.md`.
5. KOO therefore set `PACKAGE_INTEGRITY_GATE = FAIL`, preserved the defective package as historical provenance, prohibited SIS deployment, and returned an exact fix to KOD.

## Exact dependency

Owner: KOD.

Required next result:
- new immutable package commit, not reinterpretation of the defective locator;
- regenerated `MANIFEST.md` from exact final package bytes;
- verification of every declared SHA-256 after final modification;
- rerun unit tests;
- rerun validate-only;
- exact new commit + manifest + verification evidence returned to KOO.

Deployment authority remains with KOO after separate acceptance of the corrected immutable package.

## Cross-stage boundary

The implementation/test PASS is local evidence only. It does not cross the immutable-package integrity gate.

Therefore SHT does not promote any of the following:
- SIS static readiness to deployment readiness;
- package candidate to accepted immutable package;
- repository-side implementation to provider execution;
- provider research to provider selection;
- Entity Runner branch to E2E PASS.

M365/ChatGPT Work and generic Work PR-trigger lines remain independent and unchanged by this package defect.

## Queue effect

Entity Runner has advanced beyond provider-only research into a concrete bounded implementation candidate, but its immediate critical path is now package integrity correction and KOO re-verification. No duplicate dispatch is created because KOO has already address-routed the exact defect to KOD.

---
КТО: SHT / ШТАБИСТ
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: зафиксировать новый package-integrity gate Entity Runner и не допустить переноса локального PASS в deployment/E2E
СТАТУС: profile_current_state
