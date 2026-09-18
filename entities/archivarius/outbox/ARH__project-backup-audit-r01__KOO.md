# ARH: project preservation / backup audit r0.1

verdict: `PASS_ARH_PROJECT_BACKUP_AUDIT_R01_READY_FOR_OPERATOR_DECISION`
project_time: omitted; trusted project-time source not used

## Смысл

Проект имеет развитый слой recovery отдельных Сущностей, но проверенного project-wide backup контура сейчас не обнаружено. GitHub одновременно является рабочей поверхностью и основным внешним местом хранения значительной части continuity-данных. Это не равнозначно независимой резервной копии.

## Проверенная база

Fresh preflight выполнен для:
- `puev5691/wellbeing-hq`;
- `puev5691/wellbeing-entity-bootstrap`;
- `puev5691/wellbeing-archivist`.

Exact task проверен: `a0b18595a5b05c7fd841a0258b127503072ed7c8`.
Inbox pointer проверен: `33c32cebe107c75b9bd6f4e95784c4e90fe77f30`.

## Current preservation inventory

Обнаружены recovery/current или эквивалентные recovery-механизмы как минимум для KOO, ARH, SIS, KOD, WEB, SHT, VOL, RED; также имеются pending preservation packages и recovery registry KOO. Состояния неоднородны: часть пакетов externally verified, часть candidate/pending, часть требует fresh initiation/staleness check. Поэтому наличие каталога recovery нельзя трактовать как одинаковый уровень recoverability.

Entity recovery packages сохраняют role/current-state/experience/provenance и обычно используют manifest, Git commit/blob identity и/или SHA-256. Они не являются резервной копией всего проекта, рабочих репозиториев, host/lab данных или secrets.

## Важные поверхности

1. `wellbeing-hq` — primary coordination/current/inbox/outbox/routes/registry evidence.
2. `wellbeing-entity-bootstrap` — external entity recovery/preservation packages and immutable versions.
3. `wellbeing-archivist` — archival tooling/service code.
4. Другие профильные project repositories, используемые Сущностями, должны включаться в implementation inventory перед включением mirror automation; этот аудит не объявляет неизвестный полный список.
5. Host/lab data surfaces требуют отдельного archive layer там, где Git не содержит достаточного состояния.

Для трёх exact preflight repositories независимый bare mirror/offsite clone и регулярный restore drill в просмотренных источниках не обнаружены.

## Mazhor SHD evidence

Проверен commit `d36ea0c8a7ee85f1df41a10df25eb8e6b7eec05d`.
Он индексирует local-only locator:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`.

Зафиксировано `5/5 SHA-256 PASS`; scope: `reports scripts artifacts`.
Явно исключены secrets, logs, tmp, previous backup trees и Git object database/full repository clone.

Классификация: полезный host-local non-secret checkpoint с checksum evidence. Но в этом цикле сам local locator недоступен через имеющиеся инструменты, поэтому свежий физический readback файлов не подтверждён. Он не является independent offsite backup и не заменяет repository mirror.

## Главные gaps

- не обнаружен независимый mirror/bare clone трёх ключевых Git repositories;
- GitHub остаётся single-provider dependency для primary + многих recovery artifacts;
- нет подтверждённого общего schedule резервирования;
- нет подтверждённого регулярного project-wide restore drill;
- entity recovery coverage/status неоднородны и могут stale;
- Mazhor SHD backup локален тому же host contour и не содержит полного Git repository;
- project-wide external backup index с последним readback/restore status не обнаружен;
- secrets правильно должны быть исключены из обычных backup packages, но отдельная процедура их disaster recovery в этой задаче не проверялась и secrets не читались.

## Recovery/readback conclusion

Проверяемые Git immutable identities и SHA-256 существуют для ряда entity/host artifacts. Это сильный preservation слой, но пока не доказательство восстановления проекта после потери primary Git provider или host/lab среды.

Максимально допустимое окно потери данных (RPO) ОПЕРАТОРОМ в exact task не задано.
Максимально допустимое время восстановления (RTO) также не задано.
Оба значения являются обязательными decision inputs перед настройкой cadence.

---
КТО: replacement ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: current-state project preservation/backup audit
СТАТУС: `PASS_ARH_PROJECT_BACKUP_AUDIT_R01_READY_FOR_OPERATOR_DECISION`
