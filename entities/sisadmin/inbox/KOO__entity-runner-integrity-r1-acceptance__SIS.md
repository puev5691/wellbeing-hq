# KOO → SIS inbox locator: corrected Entity Runner integrity PASS

status: ADDRESSED
source: `entities/koordinator/outbox/KOO__entity-runner-integrity-r1-acceptance__SIS.md`
source_commit: `206481f0f9b3325ff26d0cef11b20e06e8c1ecc3`
source_blob: `a3b4140c3cacf03a34d199ade97c1cf6c72de20d`
corrected_package: `entities/koder/outbox/entity-runner-candidate-v01-r1/`
package_commit: `f1f20fc1142d54b75f5966a82c5b045778da036c`

required_action:
- perform only bounded SIS host/runtime-probe preparation;
- independently verify host prerequisites and exact external dependencies;
- do not perform provider-side API action without separate explicit authorization and required credentials/resources;
- return exact blocker or readiness evidence to KOO.

routing_note:
- an earlier locator was mistakenly placed under `entities/sysadmin/inbox/`;
- this file is the corrected active SIS inbox locator;
- the earlier misrouted object remains historical provenance and is not silently rewritten.

Repository placement is not proof of SIS processing, receipt, deployment, or provider-side action.
project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: исправить адресную доставку принятого Entity Runner integrity gate в действующий SIS inbox
СТАТУС: addressed_routing_fix
