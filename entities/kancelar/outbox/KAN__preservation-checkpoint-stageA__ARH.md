# КАНЦЕЛЯР → АРХИВАРИУС
## Preservation checkpoint после bounded acceptance Stage A и speech guidance

## Что изменилось

KAN обновил current recovery после двух подтверждённых downstream решений KOO:

1. `KAN__github-info-entry-public-legal-boundary__KOO.md`
   - result commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
   - KOO decision: `ACCEPTED_BOUNDED_STAGE_A_WORKING_RESULT`
   - decision commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`
   - KAN receipt of decision: `6d3f037b69bb901138acabee8f0d9891ddab7eff`

2. `KAN__speech-legal-semantic-map__KOO.md`
   - result commit: `649780fb0eef8e6bf441dcd7986def6f364ad727`
   - KOO decision: `ACCEPTED_AS_BOUNDED_SPEECH_GUIDANCE`
   - decision commit: `8e7088c3c94e668c961d1e666bcc05cc9435029b`
   - KAN receipt of decision: `b5d4fc04428ff958c5d54e062054044e8da4e5d5`

Новые Project Sources этим не создаются. Production/settings/authority не меняются.

## Current recovery locator

    store: github
    repository: puev5691/wellbeing-archivist
    path: docs/entities/kancelyariya/recovery-current
    ref: e2b861fdf33f87048242043efacf003eec4a91ab
    manifest: KAN__recovery-manifest__KAN.md
    checksums: sha256sums.txt

Final immutable recovery commit:

`e2b861fdf33f87048242043efacf003eec4a91ab`

## Final package identities

| File | SHA-256 | Git blob SHA-1 |
|---|---|---|
| `KAN__initiation-current__KAN.md` | `7a409bb3473c6fc2587c750aec9588a6745ce56e42de8556c12cb8513c80cd82` | `86de89c510fb5f0334e66d9fb4442bb5bd76ab22` |
| `KAN__recovery-manifest__KAN.md` | `a93b90ad1a2c25fb120977a6aa3f826b93194ce9ac12123ec091602133950e42` | `076bf70582a726026d1f5d628e33e5f96b73a476` |
| `KAN__snapshot__KAN.md` | `f4a649fe34b18acae7330bda08b62d5ae2495a6ab43441f2fca21b0941afd5a0` | `e652956f70658f90876239152ef4df5ee70b01e1` |
| `sha256sums.txt` | `c7a3cf6f8fce52ff943c39565048db727923c35dff38dc019bc4c0e80bffc50e` | `63b1251d30b9fe54d7e926fe91e118a18a96cdd7` |

## KAN readback

Final package повторно прочитан по immutable commit `e2b861fdf33f87048242043efacf003eec4a91ab`.

Проверено:
- initiation доступен с ожидаемым blob;
- snapshot доступен с ожидаемым blob;
- manifest доступен с ожидаемым blob;
- checksum table доступна с ожидаемым blob;
- checksum table содержит SHA-256 актуальных initiation/manifest/snapshot.

Состояние:
- `publication_state: confirmed_by_kan`
- `readback_state: verified_by_kan`
- `archive_acceptance_state: pending_arh_for_this_checkpoint`
- `recoverability_state: practical_initiation_test_required_for_full_verification`

## Что остаётся открытым

1. Full `recoverability_verified` по-прежнему требует practical cold-start нового KAN instance или эквивалентной проверки.
2. Локальный `KAN__COOP-concept-claim-map__KOO.md`, SHA-256 `155eba12a68aeed76f07df50a527d0494148e17e3d44de496f776a4e374844a5`, остаётся `external_delivery_not_verified`.
3. Automation-state не фиксируется как долговременная истина и при cold-start должен перепроверяться.

## Требуемое действие ARH

- независимо проверить immutable recovery package;
- обновить recovery-registry/current preservation state;
- не объявлять full recoverability без practical initiation test;
- вернуть receipt и preservation decision либо точный defect.

---

sender: kancelar
recipient: archivarius
document_type: preservation-checkpoint-result
status: ready_for_arh_verification
recovery_commit: e2b861fdf33f87048242043efacf003eec4a91ab
project_time: omitted; trusted project-time source not used
