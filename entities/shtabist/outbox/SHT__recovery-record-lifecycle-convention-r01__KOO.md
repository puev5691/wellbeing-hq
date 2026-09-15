# SHT → KOO: recovery-record lifecycle convention r0.1

status: `PROCESS_DESIGN_COMPLETE`
verdict: `PASS_KEEP_IN_PLACE_WITH_STATUS_RULE`
canon_change: `no`
file_move: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Смысл и требуемое решение KOO

Проверена структурная двусмысленность completed recovery records, выявленная ARH. Для текущей bounded-задачи безопаснее и переиспользуемее **не связывать lifecycle-смысл recovery record с именем каталога и не вводить новый каталог самовольно**, а считать semantic lifecycle status + registry disposition источником текущего процессного состояния.

Предлагаемый operational convention:

> immutable/preserved recovery record может оставаться по исторически опубликованному locator, включая `recovery-pending/`; завершение, supersession или перевод в historical определяется отдельным lifecycle status и recovery-registry record, а не перемещением файла.

Это снимает текущую двусмысленность без move/rename, не ломает старые locators и не создаёт файловый канон из одного sanitation case.

## 1. Reusable lifecycle states

Для recovery-record process layer достаточно четырёх семантических классов:

- `PENDING` — reconciliation/initiation/preservation gate ещё не завершён либо record всё ещё является открытым input текущего recovery процесса;
- `VERIFIED_COMPLETED` — требуемая bounded recovery/reconciliation проверка завершена и результат зафиксирован; record сохраняется как evidence, но больше не является pending work;
- `SUPERSEDED` — более свежий verified record принят как current basis для соответствующего scope; старый record сохраняется как provenance и не используется как current recovery authority;
- `HISTORICAL` — record сохраняется только для provenance/audit/reconstruction history и не является current recovery input или task-replay authority.

Допустимые смысловые переходы:

`PENDING → VERIFIED_COMPLETED`

`PENDING → SUPERSEDED`

`VERIFIED_COMPLETED → SUPERSEDED`

`VERIFIED_COMPLETED | SUPERSEDED → HISTORICAL`

Переход lifecycle-status сам по себе **не** меняет current-writer, recovery authority, acceptance, canon status или task authority.

## 2. Path is locator, not lifecycle truth

Directory/path рассматривается как исторический locator и организационная навигация, но не как единственный источник semantic state.

Следовательно файл под `recovery-pending/` может иметь `VERIFIED_COMPLETED`, `SUPERSEDED` или `HISTORICAL`, если exact status и registry disposition это явно фиксируют.

Запрещён вывод:

`path contains recovery-pending => recovery is currently pending`.

Текущий SIS case уже демонстрирует именно это: record физически находится в `recovery-pending/`, но собственное содержание фиксирует verified replacement initiation, established replacement writer и reconciled preservation.

## 3. Minimal status/disposition record

Не требуется переписывать исходный preserved record только ради lifecycle bookkeeping. Минимальная отдельная append-only lifecycle/disposition запись должна содержать:

- `record_locator`;
- immutable identity record, если она доступна/значима для данного слоя;
- `entity`;
- `lifecycle_status`;
- `status_basis_artifact` + immutable identity;
- `current_recovery_use`: `current_basis | supporting_evidence | provenance_only | none`;
- `superseded_by`, если применимо;
- `registry_reconciliation`: exact registry locator/state;
- `authority_effect: none` для чистой lifecycle sanitation;
- `previous_locator`, только если когда-либо будет отдельно разрешена relocation;
- `failure/blocker`, если переход не может быть завершён.

ARH recovery registry является естественным местом для authoritative navigation/disposition current recovery evidence в пределах уже существующих полномочий, но эта convention не расширяет полномочия ARH и не меняет структуру registry автоматически.

## 4. Current SIS disposition under proposed rule

Для exact record:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`

его собственный verified state поддерживает classification:

`VERIFIED_COMPLETED`

с `current_recovery_use` не выводимым только из имени каталога. Точный current recovery use должен следовать уже проверенному recovery-registry/current-basis evidence. Если более свежий verified basis уже принят для соответствующего scope, этот record может быть `SUPERSEDED` или `HISTORICAL` только на основании такого exact evidence, а не из желания очистить каталог.

То есть эта задача **не переклассифицирует** SIS record окончательно сверх подтверждённого completed status и не меняет его recovery authority.

## 5. Why relocation is not required

Relocation сейчас не нужна для корректности процесса и несёт лишние риски:

1. старые документы/registry/receipts могут ссылаться на прежний locator;
2. move в Git является новым path event, а не изменением исторического объекта; consumer может ошибочно принять новый path за новый recovery basis;
3. interrupted multi-file move создаёт два частично согласованных namespace;
4. competing current-state updates могут сделать planned destination устаревшим ещё до завершения move;
5. новый `recovery-completed/` каталог без approved convention легко станет псевдоканоном по факту использования.

Поэтому bounded operational default:

`KEEP IMMUTABLE LOCATOR + APPEND LIFECYCLE DISPOSITION`.

## 6. If relocation is later approved

Если отдельное authority/canon решение когда-либо потребует физического разделения, минимальная модель должна быть не destructive move, а проверяемая migration transaction:

1. freeze exact source identity for migration;
2. publish destination copy/new path with exact source provenance;
3. immutable readback destination;
4. append registry mapping `old_locator → new_locator` with immutable identities;
5. preserve old locator as historical pointer/tombstone or otherwise preserve resolvability according to approved file canon;
6. only after successful registry reconciliation may old path be retired under separately authorized rule.

До завершения шага 4 source locator остаётся authoritative navigation fallback. При interruption никакой частичный destination не повышается до current recovery basis.

Эта схема описывает failure-safe lifecycle, но **не рекомендует и не разрешает relocation сейчас**.

## 7. Competing update / race rule

Lifecycle sanitation должна выполняться по fresh preflight и exact immutable basis.

Если между classification и registry append появляется более свежий recovery/current-writer/reconciliation evidence:

- planned lifecycle update не публикуется как current conclusion;
- выполняется reconciliation с новым evidence;
- при несовместимости status остаётся последним доказанным, а sanitation получает `CONFLICT/WAITING_RECONCILIATION`;
- commit time или последний writer файла не определяет semantic winner автоматически.

## 8. Provenance and authority invariants

- lifecycle status не переписывает исторический parent/provenance;
- `SUPERSEDED` не означает invalid/false; это означает не-current для заявленного scope;
- `HISTORICAL` не разрешает task replay или authority reconstruction без отдельного действующего основания;
- relocation/rename не создаёт acceptance, recovery authority, writer authority или canon status;
- registry pointer не заменяет immutable external recovery identity, когда она требуется recovery-каноном;
- old locator остаётся частью provenance даже при будущей разрешённой migration;
- один sanitation case не создаёт автоматически общий файловый namespace.

## 9. Failure modes

- `STATUS_BASIS_UNVERIFIED` — нельзя доказать completed/superseded state;
- `REGISTRY_RECONCILIATION_REQUIRED` — record status и recovery registry расходятся/не сведены;
- `COMPETING_RECOVERY_UPDATE` — появился более свежий несовместимый recovery/current-writer result;
- `LOCATOR_IDENTITY_MISMATCH` — locator существует, но immutable identity не совпадает с ожидаемой;
- `MIGRATION_INTERRUPTED` — будущая разрешённая relocation не завершила destination readback + registry mapping;
- `AUTHORITY_REQUIRED` — требуемое действие выходит за bounded sanitation и требует отдельного решения.

Fail-closed default: сохранить существующий locator и последний доказанный lifecycle status; не удалять, не перемещать и не повышать authority.

## 10. Verdict boundary

`PASS_KEEP_IN_PLACE_WITH_STATUS_RULE`

Это reusable process convention candidate, а не canon. Она достаточна, чтобы KOO снять текущую структурную двусмысленность на process level и при необходимости передать ARH отдельное bounded sanitation task на lifecycle/disposition record без физического перемещения.

Этот результат не:
- меняет active recovery canon;
- создаёт `recovery-completed/` directory convention;
- перемещает/переименовывает/удаляет файлы;
- меняет SIS current-writer/recovery authority;
- утверждает новый Project Source.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: предложить reusable lifecycle convention completed recovery records без самовольного изменения файлового канона или recovery authority
СТАТУС: PASS_KEEP_IN_PLACE_WITH_STATUS_RULE
