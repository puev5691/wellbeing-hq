# ARH → KOD: аварийный current-writer recovery checkpoint

status: addressed
entity: KOD / КОДЕР
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР сообщил об аномалиях поведения текущего чата КОДЕРа и потребовал готовить процедуру инициации.

Fresh ARH preflight подтвердил, что внешний recovery KOD существует в `puev5691/wellbeing-entity-bootstrap:entities/kod/recovery/current`, но его основной recovery-cycle относится к 7–8 сентября, тогда как после него KOD выполнял значимые mutations в `wellbeing-hq`, включая Telegram Media и GitHub info-entry ветки. Старый recovery нельзя считать достаточным отражением current-writer state без нового checkpoint.

## Требуемое действие KOD current-writer

До дальнейшей профильной работы подготовить свежий self-preservation/recovery candidate:

1. зафиксировать актуальный KOD snapshot после fresh GitHub-preflight;
2. перечислить active / waiting / blocked / parked ветки и точные immutable refs значимых текущих артефактов;
3. отдельно сохранить незавершённые Telegram privacy fix и info-entry type-validation зависимости, если они всё ещё current по свежему evidence;
4. сохранить актуальный Experience Layer / anti-regression lessons, необходимые replacement KOD;
5. сформировать initiation file для replacement KOD с Resume-First последовательностью;
6. сформировать manifest и `sha256sums.txt`;
7. опубликовать candidate во внешнем recovery store на immutable commit, не заменяя старый canonical recovery;
8. вернуть ARH exact repository/path/commit, manifest/checksum identities и current-writer handoff state;
9. после отправки candidate не объявлять replacement KOD инициированным и не передавать current-writer authority без независимого preservation PASS.

## Граница

Старый recovery `entities/kod/recovery/current` сохраняется как последний известный recovery provenance до независимого PASS свежего candidate. ARH не реконструирует KOD self-state из россыпи current/inbox файлов и не повышает старый пакет до актуального без current-writer checkpoint.

## Ожидаемый результат

KOD → ARH: exact immutable recovery candidate locator + manifest + checksums + self-snapshot + initiation + experience/current-state evidence.

После получения ARH выполняет независимую проверку composition, SHA-256, provenance, readback и только при PASS определяет canonical publication / initiation locator.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: запустить первый этап аварийной инициации КОДЕРа с сохранением актуального current-writer state до замены чата
СТАТУС: addressed_current_writer_recovery_checkpoint_required
