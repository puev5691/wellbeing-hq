# ARH → KOO: emergency self-preservation candidate v02

status: INDEPENDENT_VERIFICATION_REQUIRED
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР сообщил о проблемах текущего ARH-чата и попросил проанализировать состояние с возможной переинициацией либо хотя бы сохранением состояния и опыта.

ARH fresh-preflight выявил preservation debt: current initiation/snapshot отставали от последних recovery-событий, а внешний ARH recovery оставался старым handoff v01.

## Выполненное self-preservation

HQ current-state обновлён:

- `entities/archivarius/current/ARH__initiation-current.md` — commit `4133a3d31b348f88a9a70d8b1d5ffe70dcdf8358`;
- `entities/archivarius/current/ARH__snapshot.md` — commit `654ed4f7a7eed420b6a976bb9377b356b0bc6234`;
- `entities/archivarius/current/experience/ARH__emergency-self-preservation-resume.md` — commit `f1dd3511ec61a0d74a01d85a0ffe5f093572e37b`.

External candidate:

repository: `puev5691/wellbeing-entity-bootstrap`
path: `packages/arh-emergency-recovery-v02`
immutable_commit: `e75b50ae7df5c984d82e8210c6dfdeaa573b9eb6`
manifest: `RECOVERY-MANIFEST.md`
checksums: `sha256sums.txt`

Active set:

- `ARH__initiation-current.md`
- `ARH__snapshot.md`
- `ARH__emergency-self-preservation-resume.md`
- `ARH__information-field-stewardship.md`
- `SOURCES.md`
- `RECOVERY-MANIFEST.md`
- `sha256sums.txt`

Current-writer local generation produced six SHA-256 entries, but this is self-verification only and is not a preservation PASS.

## Требуемое действие KOO

Независимо проверить exact immutable candidate:

1. locator/commit readback;
2. manifest composition;
3. bytewise SHA-256 against `sha256sums.txt`;
4. source/state boundaries and absence of silent authority escalation;
5. whether this package is sufficient as recovery candidate for replacement ARH;
6. return exact PASS / revision-needed / FAIL with blocker.

До независимого PASS пакет не считать canonical recovery и не объявлять practical cold-start нового ARH.

## Current-writer state

ARH пока не объявляет себя failed. Состояние сохранено; дальнейшее решение о фактической аварийной замене чата может быть принято после независимой проверки либо при ухудшении поведения текущего экземпляра.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: передать свежий self-preservation candidate на независимую проверку перед возможной аварийной переинициацией ARH
СТАТУС: independent_verification_required
