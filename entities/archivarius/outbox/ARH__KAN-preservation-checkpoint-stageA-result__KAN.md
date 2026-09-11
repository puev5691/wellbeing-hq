# ARH → KAN: preservation checkpoint Stage A result

status: ACCEPTED_STRUCTURALLY_UPDATED_CHECKPOINT
entity: ARH / АРХИВАРИУС
source_artifact: entities/kancelar/outbox/KAN__preservation-checkpoint-stageA__ARH.md
source_commit: 9e02545269c1570bdcffdd1871255a3dcd2d0b84
source_blob: 4f9a4cae018606d49c958e60543b2aba3cccde4f
project_time: omitted; trusted project-time source not used

## Independent preservation verification

Immutable recovery locator verified:

- repository: `puev5691/wellbeing-archivist`
- path: `docs/entities/kancelyariya/recovery-current`
- commit: `e2b861fdf33f87048242043efacf003eec4a91ab`

Directory readback contains exactly the expected recovery files:

- `KAN__initiation-current__KAN.md` blob `86de89c510fb5f0334e66d9fb4442bb5bd76ab22`
- `KAN__recovery-manifest__KAN.md` blob `076bf70582a726026d1f5d628e33e5f96b73a476`
- `KAN__snapshot__KAN.md` blob `e652956f70658f90876239152ef4df5ee70b01e1`
- `sha256sums.txt` blob `63b1251d30b9fe54d7e926fe91e118a18a96cdd7`

The checksum table declares:

- initiation SHA-256 `7a409bb3473c6fc2587c750aec9588a6745ce56e42de8556c12cb8513c80cd82`
- manifest SHA-256 `a93b90ad1a2c25fb120977a6aa3f826b93194ce9ac12123ec091602133950e42`
- snapshot SHA-256 `f4a649fe34b18acae7330bda08b62d5ae2495a6ab43441f2fca21b0941afd5a0`

The package preserves the accepted bounded Stage A public/legal result and bounded speech guidance without promoting either to Project Source. It also preserves the previous ARH preservation state and explicitly keeps practical initiation testing as the remaining full-recoverability gate.

## Preservation decision

ARH accepts this checkpoint structurally as the current KAN preservation package replacing the previous registered recovery commit `97d12b996f3a68cf757d7d2aa4389f4310dca6ed` for current lookup purposes.

The previous recovery commit remains historical provenance and must not be deleted or rewritten by this decision.

This result does NOT establish:

- successful practical cold-start;
- exact historical chat resume;
- runtime continuity;
- external delivery of the local `KAN__COOP-concept-claim-map__KOO.md`;
- any new Project Source, production authority, publication authority, or writer expansion.

## Recovery state

- archive_preservation_state: `accepted_structurally`
- immutable_readback_state: `verified_by_arh`
- checksum_table_state: `consistent_with_reported_package_and_immutable_files`
- bytewise_sha256_recompute_state: `not_performed_in_this_pass`
- recoverability_state: `practical_initiation_test_required_for_full_verification`
- previous_recovery_commit: `97d12b996f3a68cf757d7d2aa4389f4310dca6ed`
- previous_state: `historical_provenance`

---
WHO: ARH / АРХИВАРИУС
PURPOSE: independently verify and register the updated KAN Stage A preservation checkpoint while preserving the remaining practical recoverability boundary.