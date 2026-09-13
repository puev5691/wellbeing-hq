# ОПЕРАТОРУ: полная процедура аварийной переинициации SHD / ШАРДОВИКА

status: OPERATOR_RUNBOOK_READY
entity: SHD / ШАРДОВИК
production_mutation: no
current_writer_transfer: not_yet_performed
practical_reinitiation: not_yet_performed
project_time: omitted; trusted project-time source not used

## 0. Что уже сделано АРХИВАРИУСОМ

1. Выполнен fresh GitHub-preflight по SHD.
2. Установлено, что последний independently verified SHD recovery `ce9891f...` существенно старше текущей MAZHOR/lab-01 работы.
3. Старый recovery НЕ переписан и остаётся базовой independently verified self-recovery основой.
4. MAZHOR `p552203.kvmvps` проверен через Remote Desktop Commander: device online, ping PASS, user `shd`, lab workspace существует, Desktop Commander agent работает.
5. Создан local non-secret backup:
   `/data/wellbeing-lab/backups/shd-pre-reinit-v01`
   checksum verification: `5/5 PASS`.
6. В backup не включались contents `secrets`, `logs`, `tmp` и Git object database.
7. Создан local failover marker:
   `/data/wellbeing-lab/reports/SHD_FAILOVER_MARKER.md`
   SHA-256 `5ad32dd091e3dbbac1b102fc2fcbd465d5844613e7bdf1491bd8bfbb3011cfb7`.
8. Создан emergency external recovery overlay v02:
   `puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02`
9. Пакет проверен fresh clone непосредственно на MAZHOR: composition 7 files PASS, protected payload `6/6 SHA-256 PASS`.
10. KOO адресована независимая проверка; practical writer handoff ещё не объявлен.

## 1. Что нельзя делать со старым SHD-чатом

С этого момента старый SHD-чат НЕ использовать для:
- новых profile current-state mutations;
- WBN/TERA2 запуска;
- PWH/hashchain продолжения;
- firewall/service изменений;
- destructive cleanup;
- secret/credential операций;
- принятия новых задач от KOO как current-writer.

Старый чат остаётся только историческим evidence. Не просить его "доделать один последний шаг". Именно такие последние шаги имеют дурную привычку становиться ещё семью шагами.

## 2. Контрольный шлюз №1: независимая проверка KOO

KOO inbox:
`entities/koordinator/inbox/ARH__SHD-emergency-failover-v02__KOO.md`

ARH artifact:
`entities/archivarius/outbox/ARH__SHD-emergency-failover-v02__KOO.md`
commit `81ffc6c5e44ff4a9ea92ffb0889111ca237bf59a`
blob `649a620cfa1c74906ecd3157550fa36ac51c2c36`.

Dispatch:
`routes/dispatch/ARH__SHD-emergency-failover-v02__KOO.md`
commit `ad10b740e6beba980ebfb5015cca33acbaed36c9`.

KOO GitHub Work сейчас выключен, поэтому автоматический запуск не предполагается.

ОПЕРАТОР должен открыть действующий чат KOO и отправить:

> Продолжай Resume-First. Сначала fresh GitHub-preflight `puev5691/wellbeing-hq`. Приоритетно обработай `entities/koordinator/inbox/ARH__SHD-emergency-failover-v02__KOO.md`. Независимо проверь last verified SHD recovery `ce9891f63b6123600623e01b8da84131f239c5c7` и emergency failover candidate `ea6a84bc4eb668414cb18758b23d45823c5b5e39`. Проверь composition, checksums, provenance, KOO control state, OPERATOR failover authority и competing/current-writer boundary. Верни exact PASS/FAIL и допустимый следующий шаг. Не объявляй practical replacement initiation только по package/inbox presence, не повышай PWH/process candidates до canon, не разрешай WBN/TERA2 launch или production mutation из этого recovery task.

Ждать от KOO не общую фразу "всё нормально", а exact result artifact с PASS/FAIL и immutable identity.

## 3. Когда можно создавать новый SHD-чат

Предпочтительный режим: после independent KOO PASS.

Если новый чат открыть до KOO PASS, он должен работать только как `initiation_loaded_external_unverified` и выполнять read-only recovery checks. Никакой authoritative profile mutation до закрытия writer boundary.

## 4. Первый промпт в новом SHD-чате после KOO PASS

Передать дословно:

> Проведи аварийную инициацию replacement SHD / ШАРДОВИКА по recovery-канону.
>
> Основной emergency launcher:
> `puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02/SHD__emergency-initiation-master.md`
>
> Last independently verified base recovery:
> `puev5691/wellbeing-entity-bootstrap@ce9891f63b6123600623e01b8da84131f239c5c7:packages/shd-role-v2_3-current-recovery/`
>
> Выполни launcher полностью и строго по порядку. Сначала загрузи active approved Project Sources. Затем независимо проверь base recovery, emergency overlay composition/checksums и fresh `puev5691/wellbeing-hq` state. Проверь MAZHOR `p552203.kvmvps` только одним спокойным read-only pass, локальный backup `/data/wellbeing-lab/backups/shd-pre-reinit-v01`, failover marker и competing/current-writer evidence.
>
> Не продолжай WBN/TERA2, COOP, PWH/hashchain или любые старые профильные хвосты автоматически. Не меняй firewall/services, production, secrets/credentials и не выполняй destructive cleanup.
>
> До writer handoff работай read-only. В первом отчёте верни: `initiation_status`, base recovery locator/checksum result, overlay locator/checksum result, fresh HQ HEAD, MAZHOR readback, backup verification, KOO failover verification identity, competing_writer_state, current_writer_state, exact current task state и forbidden/unresolved boundaries.
>
> Допустимый статус только один из: `initiation_verified | initiation_loaded_external_unverified | initiation_failed`.
>
> Если KOO PASS + OPERATOR failover decision + отсутствие competing writer evidence подтверждены, зафиксируй practical initiation/current-writer handoff отдельным exact SHD current artifact и только после его immutable readback переходи к Resume-First. Если exact профильной задачи после fresh reconciliation нет — остановись в `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`, не придумывай её.

## 5. Контрольный шлюз №2: первый отчёт replacement SHD

Новый SHD должен доказать, а не заявить:
- approved source load;
- base recovery identity;
- base checksum verification;
- overlay exact commit `ea6a84bc...`;
- overlay `6/6 PASS`;
- fresh HQ HEAD;
- KOO PASS identity;
- MAZHOR online/read-only state;
- local backup presence/checksum table;
- old writer frozen/unreliable historical state;
- отсутствие competing writer evidence;
- writer handoff basis.

Если хотя бы один критичный элемент не подтверждён, статус не должен быть `initiation_verified`.

## 6. Контрольный шлюз №3: фиксация current-writer

После успешной инициации replacement SHD создаёт собственный current artifact. Это должен сделать сам SHD, не ARH.

Минимум зафиксировать:
- status `initiation_verified`;
- exact base recovery;
- exact emergency overlay;
- KOO verification artifact;
- OPERATOR failover basis;
- competing writer state;
- current_writer_state;
- fresh HQ boundary;
- MAZHOR recovery state;
- current task state.

После записи — mandatory readback exact commit/blob.

Только после этого старый чат окончательно считается historical writer instance для operational purposes.

## 7. Возобновление профильной работы

Первый профильный шаг выбирается только после нового fresh preflight.

До нового exact KOO/OPERATOR задания нельзя автоматически считать активными:
- PWH/hashchain research candidate;
- COOP/WBN fit-gap;
- старые WBN/TERA2 node tails;
- прежние network/VPN хвосты;
- любое действие, которое старый чат "собирался сделать".

Если fresh KOO evidence не содержит exact SHD task, состояние: `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`.

## 8. Что сохранено на MAZHOR

Local backup:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`

Files:
- `README.md`
- `host-state.txt`
- `lab-tree.txt`
- `repo-state.txt`
- `lab-workfiles.tar.gz`
- `sha256sums.txt`

Checksum result: `5/5 PASS`.

Secret/log/tmp contents исключены.

Failover marker:
`/data/wellbeing-lab/reports/SHD_FAILOVER_MARKER.md`

## 9. Stop conditions

Инициацию остановить, если:
- base recovery checksum mismatch;
- overlay checksum mismatch;
- KOO verification FAIL или отсутствует при попытке authoritative handoff;
- competing SHD writer evidence найдено;
- MAZHOR host identity не совпадает;
- backup/failover state противоречит package;
- active Project Sources конфликтуют;
- требуется production/destructive/secret action для завершения initiation.

При stop condition новый SHD возвращает exact blocker. Не "чинит по месту" recovery process.

## 10. Признак успешного окончания всей процедуры

Процедура завершена только когда одновременно существуют:
1. independent KOO PASS;
2. replacement SHD first report;
3. SHD-owned `initiation_verified/current-writer` artifact;
4. immutable readback этого artifact;
5. fresh Resume-First reconciliation;
6. old chat больше не выполняет authoritative work;
7. MAZHOR backup сохранён;
8. следующий профильный task либо exact-addressed, либо состояние явно `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: операторский runbook максимально контролируемой замены деградировавшего SHD-чата
СТАТУС: operator_runbook_ready
