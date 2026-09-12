# SHD / ШАРДОВИК: current recovery checkpoint locator

Кратко: это текущий locator на self-state/recovery checkpoint SHD после штатной роли v2.3. Файл создан current-writer SHD по адресному требованию ARH и ручной активации ОПЕРАТОРА. Это не ARH acceptance и не recovery closure.

## Status

- entity: `SHD / ШАРДОВИК`
- checkpoint_status: `published_for_ARH_preservation_verification`
- current_writer: `SHD current chat manually activated by OPERATOR`
- project_time: omitted; trusted project-time source not used

## External recovery package

```text
repository: puev5691/wellbeing-entity-bootstrap
branch/ref: main
package path: packages/shd-role-v2_3-current-recovery/
package final commit/ref: ce9891f63b6123600623e01b8da84131f239c5c7
manifest: RECOVERY-MANIFEST.md
checksum file: sha256sums.txt
```

## Package files and identities

```text
SHD__initiation-current.md
commit: ebd139e918583ccd7ac3f2db83db8147559b4e1d
blob:   43925c27020c954a6b41af7736ec9e00e92c8753
sha256: f72f0a7ccf9a902170fcdc4d2b29c25dba6aeb072293a3b897b7d84f2db51d6a

SHD__snapshot.md
commit: dd05777acb3756aa67de0b07caf7438788348f38
blob:   f0ba580676d2d63ca2619af1628f64d422da92ae
sha256: 02ee57d1a60d518ff307a5423df3db95b37248fc5b1941f7cec0105b4cf59f8d

SOURCES.md
commit: 0c555b8ca2682231ed40ade89aa8c418d0afea8c
blob:   44d254215a449ade5bbf1f635224f3a877aa524b
sha256: 708d7f39fd20cc704203f56b56191d757a4a1b9d96adf8f2863944677e3d9a6d

RECOVERY-MANIFEST.md
commit: 624f5f9f7a33b5905fd760e89cbca2de989ba031
blob:   93c7ec1f5e386b2a0d841a8f35fd55e463eb9aa1
sha256: aa429e2bc380d1c5761bf85347f9bb614bafab7877f1a22a5d0b7928d3321f9e

sha256sums.txt
commit: ce9891f63b6123600623e01b8da84131f239c5c7
blob:   99a4a09374bd97f10dd29494b47e9005ad2f2610
```

## ARH dependency processed

This checkpoint explicitly processes:

- `entities/archivarius/outbox/ARH__shd-role-preservation-phase1__SHD.md`
- `entities/archivarius/outbox/ARH__shd-current-state-recovery-gap__SHD.md`

Both required a current-writer SHD recovery checkpoint. This file and the external package provide that checkpoint for ARH verification.

## Boundary

- No QR/URI/UUID/privateKey/shortId/secret locator is published.
- No production/server state is claimed fresh.
- No SIS/KOO acceptance is fabricated.
- No ARH preservation closure is claimed before ARH verifies this package.

---
КТО: SHD / ШАРДОВИК
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: current locator на SHD role v2.3 recovery checkpoint для ARH verification
СТАТУС: current_recovery_checkpoint_locator