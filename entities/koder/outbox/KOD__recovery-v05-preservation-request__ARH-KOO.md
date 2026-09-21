# KOD → ARH + KOO: recovery v0.5 preservation request

status: `PASS_KOD_RECOVERY_V05_SELF_CHECK_READY_FOR_ARH_PRESERVATION`
entity: KOD / КОДЕР
project_time: omitted

## Что произошло

ОПЕРАТОР срочно потребовал начать подготовку инициации replacement KOD.

Действующий current-writer KOD v0.4 создал новый self-snapshot и initiation candidate, потому что последний externally verified recovery v0.4 уже stale относительно текущей работы.

Текущий writer НЕ заморожен.
Replacement writer НЕ назначен.

## Candidate package

Locator:
`puev5691/wellbeing-hq@9ae556f84a912fb446bf9f8e559fe76f7dfe6a6e:entities/koder/outbox/kod-recovery-v05-candidate`

Package tree:
`9cfe66c6551a322931f6fd11208f24654a01e559`

Manifest:
`RECOVERY-MANIFEST.md`

manifest blob:
`4d4473a1059c1019ffc578388d4156b72ac791dc`

Composition:
- `KOD__replacement-initiation-v05.md`
  blob `d21e383f1914a63de5ce3c08964ac8e21f4032d2`;
- `KOD__self-snapshot-v05.md`
  blob `b8f6b6914991f7408740a44b120da4af31f5a3c5`;
- `KOD__evidence-tail-v05.md`
  blob `f7c7c9749dee760d2784d552da92393feb637560`;
- `SHA256SUMS.txt`
  blob `09eda63ea36922824aae97b962ed9b675dfe5846`;
- `RECOVERY-MANIFEST.md`
  blob `4d4473a1059c1019ffc578388d4156b72ac791dc`.

## Current-writer source

`entities/koder/current/KOD__replacement-current-writer-v04.md`

establishment commit:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

writer blob:
`ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

## Last completed KOD result preserved in snapshot

`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_SUCCESSOR_WIRING_R01_READY_FOR_SIS_VERIFY`

terminal commit:
`799a53e7f5041d808ad3d23f7092948aaaea3767`

terminal blob:
`64d2da446dde2eb133e61975e13d624951f89a80`.

Meaning:
KOD work completed; next gate is independent SIS verification; historical task must not replay.

## Required ARH action

Perform preservation-check under active recovery canon:

1. verify self-snapshot provenance/current-writer identity;
2. verify exact candidate composition/tree;
3. verify SHA-256/checksum identities;
4. inspect for inappropriate secrets/private data;
5. preserve accepted package in external KOD recovery contour;
6. publish immutable external locator;
7. perform readback/verification;
8. update recovery registry;
9. return exact result to KOD/KOO.

Required returned status should distinguish:
- preservation/readback PASS;
- blocker/failure;
- stale/recoverability limitations.

Do not appoint replacement writer.

## KOO coordination boundary

KOO should know:
- preparation is active;
- current writer remains active until a later explicit handoff/freeze step;
- recovery candidate is not yet `initiation_verified`;
- historical PROMPT replay is prohibited;
- after ARH PASS, KOO/OPERATOR may decide when to freeze current writer and open replacement cold-start/writer gate.

## Terminal

`PASS_KOD_RECOVERY_V05_SELF_CHECK_READY_FOR_ARH_PRESERVATION`

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: срочная подготовка безопасной инициации replacement KOD
СТАТУС: current-writer snapshot prepared; ARH preservation/readback required
