# KOO → OPERATOR: KOD emergency initiation v0.3 root-cause diagnosis

status: `BLOCKED_OPERATOR_SOURCE_CONFLICT_DECISION`
production: `no`
project_time: omitted; trusted project-time source not used

## Проверено

Транспортный архив `KOD_source_gate_pack_v01.tar.gz` технически исправен:
- SHA-256 архива: `72f005ff6e95a37ea72ff5ddedac8c3b39fa04cea7a92989afe340a999331b8a`;
- архив распаковывается;
- содержит пять ожидаемых approved source-файлов;
- `sha256sum -c SHA256SUMS.txt` даёт 5/5 OK.

Следовательно, повторное незавершение initiation не объясняется повреждением архива.

## Обнаруженный нормативный конфликт

Файл:
`entity-state-preservation-and-recovery-canon-v1_4-approved.md`

имеет противоречивые внутренние признаки статуса:
- заголовок первой строки: `v1.4 candidate`;
- служебная карточка в конце: `status: approved_for_active_use`;
- `Approval status: approved_by_operator`;
- имя файла: `...v1_4-approved.md`.

При этом действующая `source-loading-policy-v2-approved.md` запрещает использовать документы со статусом `candidate` как действующую норму без явного решения ОПЕРАТОРА.

KOO не устраняет этот конфликт собственной трактовкой.

## Второй дефект retry-инструкции

`PROMPT__KOD__emergency-initiation-v03-retry-source-gate.md` говорит новому чату `Continue the same emergency initiation v0.3`.

Это некорректно для нового экземпляра после предыдущего `initiation_failed`: initiation относится к конкретному instance. Новый чат должен выполнять новую initiation attempt по тому же recovery/failover authority, а не продолжать внутреннее состояние предыдущего экземпляра.

## Минимальное решение ОПЕРАТОРА

Нужно выбрать одно из двух:

A. Явно подтвердить, что для exact immutable файла `entity-state-preservation-and-recovery-canon-v1_4-approved.md` служебная карточка `approved_for_active_use / approved_by_operator` имеет приоритет над ошибочным словом `candidate` в заголовке; затем использовать файл без изменения байтов.

B. Утвердить исправленную immutable редакцию, в которой только заголовок приведён в соответствие с уже установленным approved-статусом, после чего обновить canonical source identity/checksum.

До такого решения новый initiation prompt не должен обходить конфликт.

После решения нужно подготовить fresh-initiation retry, а не continuation retry.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: установить точную причину повторного незавершения аварийной инициации KOD
СТАТУС: `BLOCKED_OPERATOR_SOURCE_CONFLICT_DECISION`
