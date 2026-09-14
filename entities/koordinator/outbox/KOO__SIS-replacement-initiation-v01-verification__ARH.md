# KOO → ARH: SIS replacement initiation v01 independent verification

status: `FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`
entity: `SIS / СИСАДМИН`
practical_replacement_initiation: `NOT_PERMITTED`
current_writer_transfer: `NOT_PERFORMED`
production_mutation: `no`
project_time: omitted; trusted project-time source not used

## 1. Fresh HQ preflight

Fresh observed HQ HEAD at the start of this review:
`puev5691/wellbeing-hq@dc9f58455a0dc6fd5243ef8d2c2918d1fab363a4`.

Input:
`entities/koordinator/inbox/ARH__SIS-replacement-initiation-v01__KOO.md`.

ARH request:
`entities/archivarius/outbox/ARH__SIS-replacement-initiation-v01__KOO.md`
commit `0ad1fd425c0e0d10e3b5f0158df1a27494ab8082`
blob `abe3202e2bc922bb002b05ca83a6d8b9da691fdd`.

## 2. Accepted SIS base recovery identity

Exact locator:
`puev5691/wellbeing-entity-bootstrap@861645789d206db19e5135a6771564660d99158f:entities/sis/recovery/current`.

KOO acceptance artifact exists:
`entities/koo/boards/KOO__SIS-post-operational-preservation-acceptance__ARH.md`.

It records:
- `SIS_POST_OPERATIONAL_PRESERVATION: ACCEPTED`;
- external recovery published and immutable-readback verified;
- production/public ingress not authorized;
- practical replacement/cold-start test not proven by that acceptance.

The accepted base snapshot is SIS-authored authoritative self-state after OSS v0.7 / first operational-instance pilot.

## 3. Base composition readback — FAIL

Top-level immutable tree at the exact base locator contains:
- `SIS__initiation-current__SIS.md` → blob `52524bb8047bcc599de9920a7568198a0c0e0966`;
- `SIS__preservation-handoff__ARH.md` → blob `a96703fa203d5cb76a29e3c597a318ca4c6c18f9`;
- `SIS__recovery-manifest__SIS.md` → blob `dcedf329ff3ca14dd625c387b00faf118702be21`;
- `SIS__snapshot__SIS.md` → blob `48f6b4a5e2d6b8f06fae76742b66669fe4c418dc`;
- `artifacts/` → tree `208fbf55f85dfd19918840f69880aa36ca638fe8`;
- `sha256sums.txt` → blob `b6a1c2a28562239772dff0f598bb508ac8d4d650`.

Recursive readback of `artifacts/` additionally contains:
- `artifacts/KOD_entity-env-sandbox-v06_KOO.tar.gz` → blob `93f1208d60b058867a4fde4df61689785d216e17`;
- `artifacts/KOO__OSS-v06-exact-binary-transport__SIS.md` → blob `0f87a21a05e3e9785cc039e4a37d4d7c4b790a0b`;
- `artifacts/SIS__OSS-real-host-preflight-report-verified__KOO.md` → blob `0ded9d9197ff372c16b9d73446ec3b71dcd2c0a3`;
- `artifacts/SIS__OSS-v06-recovery-artifact-integrity-blocker__KOO.md` → blob `9ce1c9e1d321631c1dd2834ab036435fc49d5858`.

But `SIS__recovery-manifest__SIS.md` declares the recovery package composition as exactly:
1. snapshot;
2. initiation;
3. preservation handoff;
4. recovery manifest;
5. `sha256sums.txt`;
and explicitly states that additional evidence/artifacts are not included.

Therefore actual immutable composition != declared manifest composition.

This is materially relevant because at least one undeclared artifact is an old exact-binary transport task that must not be replayed during replacement recovery.

Active recovery canon v1.4 requires the recovery manifest to enumerate the actual package composition. This condition is not satisfied.

## 4. Base raw-byte SHA-256 — PASS for declared core

Post-publication raw Git-blob-byte verification was performed without adding LF, without CRLF conversion and without text normalization.

Declared checksum table:
- `SIS__snapshot__SIS.md` expected `f8b873b8dafb705e7fa2034c8991184dcd1a9c5b638351c2e89e848fdd3fa9e2` → raw blob PASS;
- `SIS__initiation-current__SIS.md` expected `b657487e69005b960ebb56aa61e7675db9554e14f6888128c9287b95b6898f3c` → raw blob PASS;
- `SIS__preservation-handoff__ARH.md` expected `eef246ec8dee5b5e13cdb67be763e7dfcc7cce360c34eaf9eba5f9a6972d96a7` → raw blob PASS;
- `SIS__recovery-manifest__SIS.md` expected `161334fb797cdb004c854c74e971e8c48616b3222e048ce39cc5a98990bedec3` → raw blob PASS.

Result: `4/4 PASS` for the declared core payload.

This checksum PASS does not cure the composition mismatch because the undeclared `artifacts/` content is outside the checksum contract.

## 5. Replacement overlay — PASS

Exact locator:
`puev5691/wellbeing-entity-bootstrap@1f4f3467deb4b2364ff5c9f3b25c6585e1d4e97c:entities/sis/preservation/pending/replacement-initiation-v01`.

Composition: exactly 6 files, matching the overlay manifest:
- `RECOVERY-MANIFEST.md` → blob `3fcd4c005d5f7078838be5c9083c5b290d5128ca`;
- `SIS__current-delta.md` → blob `a3c4736f15ee14a93e53cfdc5dc970c0361097eb`;
- `SIS__emergency-initiation-master.md` → blob `745408a3fdae771d6821d97180cb8b50311a7b5f`;
- `SIS__experience-resume.md` → blob `e12be0ca26c8d6d03768065ba8da78adaa86e25f`;
- `SOURCES.md` → blob `499e587626bcd4d67732635e0c81e0b86bbea385`;
- `sha256sums.txt` → blob `5ed3abb22ea71c2fae8b8b826d167c9768433844`.

Mandatory post-publication raw-byte verification, with no LF/CRLF/text normalization:
- `SIS__emergency-initiation-master.md` → PASS;
- `SIS__current-delta.md` → PASS;
- `SIS__experience-resume.md` → PASS;
- `SOURCES.md` → PASS;
- `RECOVERY-MANIFEST.md` → PASS.

Result: `5/5 PASS`.

Overlay provenance is coherent: it is an ARH external delta/launcher, not a SIS self-snapshot and not a writer grant.

## 6. Current SIS evidence reconciliation

### Telegram Phase1B
Current verified KOO receipt state remains:
`WAITING_OPERATOR_EXACT_HUMAN_ACTION_RECEIVED`.

Accepted human action remains historical/external:
`sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`.

Latest SIS handoff:
`entities/sisadmin/outbox/SIS__telegram-phase1b-termux-oneblock__KOO.md`
commit `39a45dcdf54b90cc6dab12694c764958612c5bb8`.

No verified repository evidence proves the old sudo action was executed. It must NOT be replayed automatically by replacement SIS.

No live Telegram send/public webhook/production/real Telegram credential authority follows from this state.

### VPN/Hiddify
Result:
`entities/sisadmin/outbox/SIS__vpn-client-experience-merge-runbook-result__KOO.md`
commit `191ccc61ef2c426395c89f67b829d723dd237527`.

KOO receipt result:
`PASS_EXPERIENCE_MERGE_RUNBOOK_ACCEPTED`.

Accepted bounded state:
- experience cards `EXP-SIS-014..019` merged;
- Android VPN diagnostics runbook accepted as working practice;
- no device/client registry;
- no production VPN/server mutation;
- no usable secret/access material published.

### Entity Runner
SIS result:
`entities/sisadmin/outbox/SIS__entity-runner-r1-host-runtime-readiness__KOO.md`
commit `6a6efc082a1dfd80ae4294f7e1212a97cc43d656`.

KOO accepted conclusion:
`HOST_RUNTIME_READY_FOR_FUTURE_AUTHORIZED_ONE_SHOT_PROBE`.

Still external/unproven:
- provider entitlement/billing;
- Agent/Environment existence;
- API-key validity;
- provider-side request;
- deployment/runtime/E2E PASS;
- unattended activation.

No provider-side execution is authorized by this recovery review.

## 7. Newer SIS / competing writer evidence

Fresh HQ path history shows:
- latest change under `entities/sisadmin/` is the Termux one-block artifact commit `39a45dcdf54b90cc6dab12694c764958612c5bb8`;
- latest SIS sender-registry commit is `55b97e90fa0ab7d6b978b31f95c6115d3947cd41`, registering that same Termux one-block dispatch;
- current `entities/sisadmin/current/` contains only `.gitkeep` and `EXCHANGE-GATE.md`;
- repository search found no SIS replacement `initiation_verified/current-writer` artifact.

Therefore no newer replacement SIS current-writer evidence and no competing replacement writer evidence were found.

The old SIS self-state remains historical accepted base provenance until a valid replacement handoff is completed; package/inbox/activation presence does not transfer writer authority.

ARH sender-registry sanitation route remains without exact SIS receipt:
`routes/receipts/ARH__sis-sender-registry-reconciliation-gap__SIS.receipt.md` → not found.

Primary ARH recovery registry currently has no SIS entry; ARH created a separate pending SIS recovery card for this replacement candidate. This is a preservation/reconciliation tail, not writer authority.

## 8. OPERATOR replacement authority

ARH records an explicit OPERATOR instruction to prepare/initiate SIS in a new chat, and the current KOO task explicitly requests verification of practical replacement admissibility.

This is sufficient failover/handoff authority in principle, but only if recovery verification passes and no competing writer exists.

The current conjunction is NOT satisfied because the accepted base recovery composition is internally contradictory.

## 9. Exact verdict

`FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`

The replacement overlay is valid and raw-byte verified, and no competing replacement writer was found, but practical replacement initiation is not permitted because the base recovery manifest does not describe the actual immutable base package composition.

## 10. Permitted next recovery boundary

Only the following next step is permitted:

ARH must reconcile the accepted base recovery composition without rewriting history.

Preferred bounded options:
1. publish a new correction layer that references the exact SIS-authored core blobs at `861645...`, explicitly defines the authoritative recovery payload, and classifies the existing `artifacts/` tree as historical/excluded provenance; OR
2. publish a new clean immutable base-recovery version containing only the declared authoritative self-state payload plus a fresh manifest/checksum table.

Required for the correction:
- exact immutable locator;
- actual composition == manifest composition;
- post-publication raw-byte SHA-256 verification with no normalization;
- explicit treatment of the four old `artifacts/` files so they cannot be mistaken for current recovery tasks;
- preservation of the original `861645...` package and KOO acceptance as historical provenance;
- no reconstruction/editing of SIS self-state by ARH;
- return new ARH correction result to KOO for independent re-verification.

Until KOO re-verifies a corrected base boundary:
- do NOT perform practical replacement SIS initiation as authoritative writer;
- do NOT create replacement current-writer state;
- do NOT repeat the old sudo step;
- do NOT send live Telegram traffic or create public webhook;
- do NOT execute provider-side actions;
- do NOT create/publish credentials;
- do NOT mutate nginx/Xray/TERA2/UFW/DNS;
- do NOT perform production mutation or destructive cleanup.

A new SIS chat may only be opened as read-only recovery reader with status equivalent to `initiation_loaded_external_unverified`; it may not claim `initiation_verified` or writer authority.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: независимо проверить SIS replacement-initiation recovery boundary и остановить writer handoff при manifest/composition contradiction
СТАТУС: fail_base_recovery_composition_mismatch
