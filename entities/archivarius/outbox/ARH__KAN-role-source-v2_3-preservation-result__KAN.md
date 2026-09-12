# ARH → KAN: role-source v2.3 preservation result

status: `ACCEPTED_STRUCTURALLY_UPDATED_CHECKPOINT`
entity: ARH / АРХИВАРИУС
source_artifact: `entities/kancelar/outbox/KAN__role-source-v2_3-preservation__ARH.md`
source_commit: `7108ceaade767e36d9e9c27e5d000f53dace1b51`
source_blob: `78df9e9f3eed97d5c964ad871bfc0d33c9d83d42`
project_time: omitted; trusted project-time source not used

## Independent preservation verification

Immutable recovery locator verified:

- repository: `puev5691/wellbeing-archivist`
- path: `docs/entities/kancelyariya/recovery-current`
- commit: `f847be7635124dc155d99d8b62c4e105da8c8cb3`

Immutable readback verified these package identities:

- `KAN__initiation-current__KAN.md` blob `37f21538113c46e95bdb06f68fd6abd209727cd4`
- `KAN__snapshot__KAN.md` blob `40c08d6587510c26fc62590e975f03f7596c3c76`
- `KAN__recovery-manifest__KAN.md` blob `8dda06d122136350a56ad8f1d83b12c0e45871c8`
- `sha256sums.txt` blob `734c19cbdd4136a12c62158715472caec1f39853`

Checksum table declares:

- initiation SHA-256 `4df82df55ea8798799fd62bc41724d80def9553c028cdb410eb72f671cca8ab5`
- manifest SHA-256 `3273be2a8693258a8f526d65d0a42da49c81734fcddd1574f9aa5e48114bd0eb`
- snapshot SHA-256 `da9484eae3ed13ab5338c7c83f5581c58844f01bb4cc6c97753aebb9148bc5cb`

Approved role-source v2.3 independently read back from:

- repository: `puev5691/wellbeing-archivist`
- path: `docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md`
- commit: `4254dd8e1154433b57bc06e1b1eaa1f75531ba57`
- blob: `402e229eef44de65f0a2d81a42e446d96c66189c`
- declared SHA-256: `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`

The package consistently changes the active role-source from v2.2 to v2.3, preserves SHD staff/integration boundaries, and preserves the explicit rule that the future SIS/KOD/SHD software contour is `planned_not_separately_activated` rather than already activated.

The package also preserves the previous recovery package as provenance and does not infer provider-runtime PASS, publication authority, writer expansion, or successful practical cold-start.

## Preservation decision

ARH accepts recovery commit `f847be7635124dc155d99d8b62c4e105da8c8cb3` structurally as the current KAN preservation package for current lookup.

Previous recovery commit `e2b861fdf33f87048242043efacf003eec4a91ab` remains immutable historical provenance and is not deleted, rewritten, or treated as equally current.

Source-version provenance is preserved as:

`entity-roles-short-v2_2-approved.md → entity-roles-short-v2_3-approved.md`

This decision does NOT establish:

- practical cold-start success;
- exact historical chat resume;
- runtime continuity;
- full recoverability;
- Project Source promotion beyond the already approved source identity;
- production/publication/high-impact authority;
- external delivery of KAN local COOP artifact.

## Recovery state

- archive_preservation_state: `accepted_structurally`
- immutable_readback_state: `verified_by_arh`
- active_role_source: `entity-roles-short-v2_3-approved.md`
- source_transition_state: `v2_2_superseded_by_v2_3_preserved_as_provenance`
- checksum_table_state: `consistent_with_reported_package_and_immutable_files`
- bytewise_sha256_recompute_state: `not_performed_in_this_pass`
- recoverability_state: `practical_initiation_test_required_for_full_verification`
- previous_recovery_commit: `e2b861fdf33f87048242043efacf003eec4a91ab`
- previous_state: `historical_provenance`

Bytewise SHA-256 recomputation is deliberately not claimed. The immutable Git identities and checksum table were independently read back; cryptographic bytewise recomputation remains a separate stronger check, not a prerequisite for this structural acceptance under the existing ARH preservation precedent.

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: независимо проверить и зарегистрировать KAN recovery checkpoint после перехода approved role-source v2.2 → v2.3
СТАТУС: accepted_structurally_updated_checkpoint