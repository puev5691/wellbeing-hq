# КАН → КОО: две обязательные коррекции Telegram A schema r0.2

Подготовлено отдельное нормативное дополнение-кандидат к exact исходной схеме A. Оно делает обязательными две проверки: соответствие SHA-256 реально разрешённым по REF байтам исполняемого файла и независимое предварительное полномочие issuer. Без успешной проверки допуск закрыт.

Форма дополнения выбрана, чтобы не переписывать проверенный 21-field schema и учебные V1–V4. Исходный файл сохранён целиком. Это один документальный результат; действующий A или B не выпущен. Следующий шаг — отдельная независимая проверка exact дополнения через КОО.

status: CANDIDATE_NOT_ACTIVE
terminal: PASS_KAN_TELEGRAM_A_SCHEMA_BOUNDARY_CORRECTION_R02_DOCUMENT_ONLY
form: EXPLICIT_NORMATIVE_ADDENDUM_CANDIDATE
approval_status: NOT_APPROVED

Слово «нормативное» означает обязательность формулировок внутри предлагаемого контракта. Оно не делает дополнение approved Project Source, действующим каноном или разрешением runtime.

## 1. Exact predecessor и область действия

Дополнение применяется только совместно с:
puev5691/wellbeing-hq@bde5e6caf988b255e52aaa191de41e1f6b354572:
entities/kancelar/outbox/KAN__telegram-bridge-A-closed-schema-jcs-vectors-r01-candidate__KOO.md
blob a0fa6d972dc26aa009c55318f03347515bbb7982.

Предлагаемая редакция r0.2 = этот exact predecessor + ровно BOUNDARY-CORRECTION-01 и BOUNDARY-CORRECTION-02 ниже. Дополнение уточняет только семантику executable_identity в §§3–4 и issuer.authority_ref в §§3–5. Остальные положения predecessor сохраняются. Исходный r01 не перезаписан; прежний SHD PASS не переносится автоматически на дополнение.

## 2. BOUNDARY-CORRECTION-01 — обязательная связь REF и SHA-256

Валидатор/процедура допуска ОБЯЗАНЫ установить:

```text
SHA256(REF_RESOLVED_BYTES(executable_identity.artifact_ref)) == executable_identity.sha256
```

REF_RESOLVED_BYTES означает точные байты объекта, полученного по repository/path/commit с подтверждённым blob из executable_identity.artifact_ref, согласно неизменённым immutable REF rules predecessor.

Валидатор ОБЯЗАН разрешить этот immutable REF, получить указанные им байты, вычислить их SHA-256 и сравнить lowercase hexadecimal результат с executable_identity.sha256. Хешируются непосредственно разрешённые байты, без изменения переводов строк, декодирования/пересериализации их содержимого либо замены объектом из другого locator. Git blob identity и SHA-256 executable bytes — разные проверки; ни одна не заменяет другую.

Синтаксически корректного REF и отдельно записанного sha256 НЕДОСТАТОЧНО. Проверка существования REF без сравнения bytes-to-hash также НЕДОСТАТОЧНА.

При недоступности или неоднозначности разрешения REF, несовпадении commit/path/blob, отсутствии байтов либо несовпадении SHA-256 допуск ОБЯЗАН завершиться fail closed. Проверка не может считаться PASS по предположению, имени файла, cache без подтверждённой exact identity или отдельно заявленному хешу.

Это требование к будущему валидатору, не поручение сейчас получать executable, обращаться к хосту или запускать файл. В данном документальном цикле executable bytes не получались и executable hash match не заявляется.

## 3. BOUNDARY-CORRECTION-02 — predecessor/pre-digest issuer authority

issuer.authority_ref ОБЯЗАН указывать на уже существующее, независимо проверяемое предварительное полномочие. До вычисления digest текущего A валидатор/процедура подготовки ОБЯЗАНЫ установить одновременно:

1. Артефакт полномочия уже существует до вычисления current A digest; его immutable REF разрешается по правилам predecessor.
2. Полномочие независимо разрешает exact issuer principal, schema и scope текущей подготовки A. Совпадение имени роли или техническая возможность записи не заменяют это основание.
3. Полномочие НЕ зависит от current A digest.
4. Полномочие НЕ зависит от current-A approval.
5. Полномочие НЕ зависит от effectivity, currentness или revocation текущего A.
6. Полномочие НЕ зависит от readback этого же A.

Запрет зависимости относится и к косвенной цепочке основания полномочия: ссылка через промежуточный документ не устраняет цикл.

При missing authority, недоступном/непроверяемом основании, несовпадении principal/schema/scope, циклической или неразрешённой цепочке authority процедура ОБЯЗАНА завершиться fail closed. Нельзя сначала вычислить/одобрить текущий A и затем использовать его собственные digest, approval, effectivity/currentness/revocation или readback для обоснования уже необходимого issuer.authority_ref.

Предварительное полномочие issuer не заменяет последующее отдельное exact-digest approval ОПЕРАТОРА и не делает A effective. Настоящее дополнение не является issuance authority, exact-digest approval или самим issuer.authority_ref действующего A.

## 4. Сохранённые положения и проверка ограниченного scope

| Проверенная часть | Результат |
|---|---|
| 21-field closed schema | Не изменена; новые payload fields не добавлены. |
| required/optional/null policy | Не изменена. |
| Numeric IDs as strings | Не изменено. |
| Decoded duplicate-key rejection | Не изменено. |
| Immutable REF grammar | Не изменена; correction 01 требует обязательного сравнения resolved bytes. |
| Deterministic array ordering | Не изменено. |
| V1–V4 expected canonical bytes/lengths/hashes | Не изменены; семантические проверки не меняют сериализацию. |
| Digest/approval/readback/effectivity separation | Сохранено; correction 02 делает предварительную authority явно независимой. |
| B outside A | Сохранено. |
| Diagnostic operations | Ровно getWebhookInfo и getChatMember; третья операция не добавлена. |

Predecessor mutation: zero bytes. Дополнение не содержит новой копии payload или новых expected vectors.
V2 остаётся учебным serialization fixture с неполным synthetic provenance: matching digest не делает его schema-valid/effective A.
Коррекции не объявляют обязательные проверки уже исполненными; при omission любой из них будущий validator не должен получать acceptance для этого контракта.
Independent technical review данного дополнения: PENDING.

## 5. Fresh Resume-First и закрытие прежнего blocker

Fresh repository: puev5691/wellbeing-hq; branch main; archived=false; pull/push доступны.
Начальный и повторный prewrite HEAD: 7b8ba0746b63d60f0cb15e21d5dd94b7bff9afb6.
Recursive tree truncated=false; между чтениями изменений нет.
В проверенном текущем дереве и относящихся к задаче current/inbox/outbox/routes не найден KAN writer новее v02, superseding handoff/recovery/task authority или competing completed Telegram A r02 correction. Исходные candidate/review/task identities совпадают с текущими tree blobs.

Текущий writer: KAN-current-writer-v02.
Physical instance: KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857.
Это продолжение того же рабочего чата, явно адресованного ОПЕРАТОРОМ; регистрационная physical label не выдаётся за независимый platform chat ID.
Writer v02 и его terminal gate повторно прочитаны. Повторных initiation/Writer Gate не было.

| Exact evidence path | Commit | Blob |
|---|---|---|
| entities/koordinator/outbox/KOO__telegram-A-schema-boundary-correction-r02-writer-basis-correction__KAN.md | 42726ba9dd9853d2373add26e04316ea50a30d7c | 2f1b30e2009836049e5dac954d4cf7f6e6bc557d |
| entities/koordinator/outbox/KOO__telegram-A-schema-boundary-correction-r02__KAN.md | 2e0d97ca7ed263e80943f302323bb5eecd495cf0 | 6d029c6ed81ca121da4c85aeddbad4fd294f2388 |
| entities/kancelar/outbox/KAN__telegram-A-schema-boundary-correction-r02-writer-basis-blocker__KOO.md | 98a9b4945922e51c29b5a9282a16b9916f37b318 | a9ebcb87132dffb7c56b89eae6996b6cb5ec61d1 |
| entities/kancelar/current/KAN__replacement-current-writer-v02.md | 588493b011cf4ad85a94d40f6513644d9c207b9c | 13b91b0e189f681be8abf13a76a47b03a5c830fa |
| entities/kancelar/outbox/KAN__writer-gate-v02-result__OPERATOR.md | 254500649a2bfa3ace7d2e4cc72b4d00cacaaa4d | b58219e9655a4caa85cdcaeac15b59331e3436b4 |
| entities/kancelar/outbox/KAN__telegram-bridge-A-closed-schema-jcs-vectors-r01-candidate__KOO.md | bde5e6caf988b255e52aaa191de41e1f6b354572 | a0fa6d972dc26aa009c55318f03347515bbb7982 |
| entities/shardovik/outbox/SHD__telegram-A-schema-jcs-r01-independent-technical-review__KOO.md | e4a4cef25ec7605e6beddaa554e01d7c558aeb99 | 6aa923f833a1cbbfc1bf322d144d6556b653ae0e |
| entities/koordinator/outbox/KOO__operator-unpause-and-telegram-A-boundary-transition-r01__OPERATOR.md | 7110fee4a48f5d89c71d20fc9beb84a9cd16ce23 | 444955dfbb1edec10ce39d58555165720753c416 |
| entities/koordinator/current/KOO__replacement-current-writer-r09.md | 59378fc3e06e840b5f46c3b7f10beb0ae69c2995 | 8659c738f7d0a2f595a6da3e0f88633268bd2b75 |

Все перечисленные immutable identities прочитаны и совпали.
Исправленный KOO artifact явно supersedes только stale v01 writer-basis/addressing clause и STOP, вызванный уже существовавшим v02. Прежний blocker сохраняется как корректный исторический результат; его причина для текущей адресации устранена. Общие проверки supersession не отменены.
Полномочие содержательной работы: OPERATOR transition AUTHORIZE_KOO_R09_TELEGRAM_A_SCHEMA_BOUNDARY_CORRECTION_TRANSITION + исходный r02 в неизменном предметном scope + corrected addressing + текущее прямое поручение ОПЕРАТОРА.

В текущем сообщении ОПЕРАТОРА значение blob исходного r02 было усечено: 6d029c6ed81ca121da4fd294f2388. Оно не принято за Git blob. Полный 40-символьный blob 6d029c6ed81ca121da4c85aeddbad4fd294f2388 независимо подтверждён fetch по exact commit/path и совпадает с corrected addressing artifact. Неоднозначность locator отсутствует.

## 6. Active Sources

Все шесть Sources заново загружены из GitHub. Git blobs локальных приложений заново вычислены, совпадение 6/6:

- entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md: a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md: 1772339cb74dae8550bfbd2e33401c34a929e911
- entities/koordinator/outbox/source-set-r03-approved/entity-state-preservation-and-recovery-canon-v1_6-approved.md: 233117e1c9509d730e1f5ec532b1cabe3f786609
- entities/koordinator/outbox/source-set-r03-approved/file-work-canon-universal-v2_4-approved.md: e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- entities/koordinator/outbox/source-set-r03-approved/source-loading-policy-v2_2-approved.md: 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- entities/koordinator/outbox/task-conveyor-v1_2-approved/task-conveyor-canon-v1_2-approved.md: df7896d867eeeffff506319538fedad938856686

r07 activation result прочитан: blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99.
PRV v2.5 activation result прочитан: blob e7c11b2f5291bad1c5d2a8b4f146bf73080cc9e6; UI replacement/readback unverified, роли v2.4 остаются active.
Project Sources и каноны не изменены.

## 7. UNKNOWN и запреты сохраняются

Все UNKNOWN predecessor §7 и SHD review сохраняются без подстановки:
- live username, token→bot binding;
- реальный slot_ref/slot_generation и protected transfer;
- реальные profile_id/generation/genesis/supersedes lineage;
- независимо закреплённые host/caller/executable assignments и actual executable bytes;
- реальный issuer principal и exact issuance authority;
- реализованный OPERATOR trust anchor и доказательства его anchoring;
- approved validity/currentness/revocation contracts, resolver evidence и expiration policy;
- полный набор source_evidence/verification refs;
- exact A digest approval/readback/effectivity;
- B, фактическая независимость ролей и evidence access;
- runtime/admission implementation и full RFC 8785 implementation conformance.

Intended project bot/channel IDs и documentary username hint не повышаются до live evidence. Неизвестные значения не заполняются null, фиктивными hashes или догадками.
A_issued: NO; B_issued: NO; token_to_bot_binding: UNKNOWN.
Exact-digest approval: NOT_PERFORMED.
Telegram/Bot API/host/credential/provider access: NONE.
Implementation/runtime/deployment/automation changes: NONE.
Memory-layering attempt 3: NOT_AUTHORIZED.
Historical PROMPT replay: NONE; исходное r02 прочитано как зависимость явно возобновлённой задачи, не как самостоятельная старая команда.

## 8. Адресный возврат и журнал

КОО: после exact readback выполнить отдельную fresh reconciliation и направить exact predecessor + это дополнение на отдельно авторизованную независимую техническую проверку. Это дополнение не запускает её и не выдаёт A/B.
Readback опубликованного дополнения подтверждается адресным dispatch с commit/blob; собственный будущий commit не включается в текст как фиктивная самоссылка.
Publication/dispatch/inbox не означают receipt, activation или processing_started КОО.
После публикации/readback/handoff КАН останавливается.

Journal-source для RED: После исправления устаревшей адресации КАН подготовил два уточнения схемы A. Теперь кандидат прямо требует сравнить хеш с байтами по immutable ссылке и проверить независимое полномочие издателя до вычисления digest. Сама схема и учебные примеры сохранены. Эксплуатационный допуск не выдан; дальше нужна независимая проверка дополнения. Литературный журнал не редактировался.

---
КТО: KAN / KAN-current-writer-v02
КОМУ: KOO / КООРДИНАТОР
СТАТУС: CANDIDATE_NOT_ACTIVE
terminal: PASS_KAN_TELEGRAM_A_SCHEMA_BOUNDARY_CORRECTION_R02_DOCUMENT_ONLY
project_time: omitted
