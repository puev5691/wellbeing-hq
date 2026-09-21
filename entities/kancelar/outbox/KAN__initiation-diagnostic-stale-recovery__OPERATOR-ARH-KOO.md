# KAN → OPERATOR + ARH + KOO: initiation diagnostic

status: `initiation_failed`
processing_started: `no`
profile_execution: `blocked`
writer_state: `not_established_for_this_instance`
diagnostic_authority: explicit OPERATOR instruction to begin KAN initiation
project_time: omitted; trusted project-time source not used

## Что произошло

По явному указанию ОПЕРАТОРА текущий экземпляр KAN переведён в `Initiation-required`.

Скрытая continuity прежнего экземпляра не предполагалась.

Проверены действующие Project Sources и внешний recovery-контур KAN.

## Текущий approved source basis

Проверены локальные approved bytes:

- `project-instructions-core-v2_5-approved.md`
  SHA-256 `f2ad19e243e55c552b10372c4bd7ddda7f18018579527f94d69e14858303b49c`
- `entity-roles-short-v2_4-approved.md`
  SHA-256 `d7feae524f6d1a34b0fd2a63475435e41ebe48097a191d87ca0ceeb797421530`
- `file-work-canon-universal-v2_4-approved.md`
  SHA-256 `c7e09bb358afd9ff131158044ce3722375ab30580e240909e85afdf38ca1e08b`
- `source-loading-policy-v2_2-approved.md`
  SHA-256 `2a410e929c8cf4daa21f9229ad300e92abbaf4ab40b4fbf3a03950cc663e719e`
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`
  SHA-256 `82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5`
- `task-conveyor-canon-v1_2-approved.md`
  SHA-256 `913e88c1e4d17a07122ad9cdf680abae28fc2def0ea0740df9ce925fec22d0e7`

Fresh HQ evidence additionally confirms Project Core v2.5 rollout as active.

## Внешний recovery locator

Externally verified immutable checkpoint:

`puev5691/wellbeing-archivist@f847be7635124dc155d99d8b62c4e105da8c8cb3:docs/entities/kancelyariya/recovery-current`

Verified package composition:
- `KAN__initiation-current__KAN.md`
  blob `37f21538113c46e95bdb06f68fd6abd209727cd4`
- `KAN__snapshot__KAN.md`
  blob `40c08d6587510c26fc62590e975f03f7596c3c76`
- `KAN__recovery-manifest__KAN.md`
  blob `8dda06d122136350a56ad8f1d83b12c0e45871c8`
- `sha256sums.txt`
  blob `734c19cbdd4136a12c62158715472caec1f39853`

The checksum table was read from the same immutable checkpoint and declares:
- initiation SHA-256 `4df82df55ea8798799fd62bc41724d80def9553c028cdb410eb72f671cca8ab5`;
- manifest SHA-256 `3273be2a8693258a8f526d65d0a42da49c81734fcddd1574f9aa5e48114bd0eb`;
- snapshot SHA-256 `da9484eae3ed13ab5338c7c83f5581c58844f01bb4cc6c97753aebb9148bc5cb`.

External version identity and composition are verified by immutable Git commit + blob identities.

## Почему initiation не может быть подтверждена

The externally verified recovery package is materially stale.

It restores this old baseline:
- core v2.1;
- roles v2.3;
- file-work v2.3;
- recovery v1.4;
- source-loading v2;
- no active task-conveyor baseline in the package.

Current approved baseline is:
- core v2.5;
- roles v2.4;
- file-work v2.4;
- recovery v1.6;
- source-loading v2.2;
- task-conveyor v1.2.

Fresh HQ also contains KAN work and addressed inputs substantially newer than the preserved checkpoint, including source-rebuild/human-interface/journal-feed work and a fresh SHT working-circles result addressed to KAN.

Under recovery v1.6, fresher HQ evidence may prove that recovery is stale, but it may not be merged by plausibility into a synthetic authoritative self-snapshot.

Therefore the package is externally authentic but **insufficient for safe restoration of current authoritative KAN state**.

Exact outcome:

`initiation_failed`

This is not a failure to read the package. It is a failure of current recoverability because the last externally verified recovery is stale.

## Writer boundary

Fresh inspection of:

`entities/kancelar/current/`

does not expose a separate explicit KAN current-writer artifact.

Historical recovery text claims writer-state only for its old checkpoint. That historical claim is not treated as current writer authority for this new/reinitiated instance.

No current-writer was invented.

This instance may perform only bounded recovery diagnostic/correction work under the explicit OPERATOR initiation instruction until the recovery/writer problem is resolved.

## Minimal next step

One fact is now required from OPERATOR:

### Variant A — old authoritative KAN writer is still accessible

The old writer must create or confirm a fresh self-snapshot/recovery package based on current approved sources and current verified KAN state. ARH then performs preservation/readback. After that this instance repeats initiation against the new exact recovery identity.

### Variant B — old authoritative KAN writer is unavailable

OPERATOR must explicitly authorize emergency replacement/failover of KAN. Only then may the replacement procedure use the last externally verified recovery as recovery basis, reconcile fresher evidence within the approved failover procedure, and pass a separate Writer Gate.

Until A or B is established:
- no authoritative KAN current-state mutation;
- no historical task replay;
- fresh addressed KAN artifacts remain evidence, not automatic execution authority.

## Terminal

`BLOCKED_KAN_INITIATION_STALE_RECOVERY_REQUIRES_WRITER_OR_FAILOVER_DECISION`

---

sender: replacement/reinitiating KAN instance
recipients: OPERATOR, ARH, KOO
document_type: initiation-diagnostic
project_time: omitted; trusted project-time source not used
