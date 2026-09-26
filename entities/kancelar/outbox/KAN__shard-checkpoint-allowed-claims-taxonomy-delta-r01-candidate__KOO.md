# Оперативные checkpoint на шардах — кандидат правил r0.1

Этот документ предлагает, что именно должна означать сохранённая точка продолжения задачи и кто вправе использовать её. Быстрый ответ сервера ещё не доказывает сохранность; сохранность ещё не даёт права продолжать работу; право продолжать одну задачу не назначает нового current-writer.

КАН подготовил только модель для решения и независимой проверки. Никакой checkpoint этим документом не признан durable или authoritative. Владелец оперативного контура не назначен. Следующий предмет решения — оставить checkpoint вспомогательным evidence либо отдельно разрешить его ограниченное использование для продолжения задачи после доказательства необходимых условий.

**Статус: CANDIDATE_NOT_ACTIVE.** Все новые требования ниже — предложения, а не действующая норма или свидетельство работоспособности.

Обозначения:
- **[A]** — уже действующая граница из approved Sources; ссылки A1–A6 приведены в конце.
- **[P]** — предлагаемое правило/определение для будущего контракта; не применяется как новое полномочие сейчас.
- **[U]** — нерешённый выбор или недоказанная техническая характеристика. UNKNOWN не заменяется предположением.
- **[E]** — прочитанное проектное evidence/направление; не новый approved Source.

Оперативный checkpoint здесь — связанный с exact задачей набор данных о завершённых шагах, незавершённых эффектах и допустимой точке продолжения. Это не «external coordination checkpoint» recovery-канона: последний является организационным trigger сохранения, а не хранилищем состояния [A1]. Слова «checkpoint» и «сохранено» сами по себе не обозначают одинаковые объекты.

## 1. Status classes for raw event, transient checkpoint, verified durable checkpoint, recovery-eligible checkpoint, promoted long-lived evidence

[P] Классы описывают доказанное свойство объекта, а не положение в единой автоматической лестнице. Отдельно учитываются целостность/доступность, статус полномочий, пригодность для recovery и содержательное acceptance.

| Класс | Предлагаемый смысл и минимальное основание | Чего не означает |
|---|---|---|
| RAW_EVENT | Наблюдение с источником и exact event/task identity; достоверность содержания может быть UNKNOWN | Не current-state, не PROMPT к исполнению |
| TRANSIENT_CHECKPOINT | Сериализованный набор данных с digest и ссылками на основания; сохранность/полнота ещё не доказаны | Ответ put, локальный файл или cache hit не создаёт CHECKPOINT_DURABLE |
| VERIFIED_DURABLE_CHECKPOINT / CHECKPOINT_DURABLE | Выполнена вся конъюнкция §3 для exact immutable объекта и утверждённого класса отказов/retention | Не operational authority, не recovery verified, не acceptance, не processing |
| RECOVERY_ELIGIBLE_CHECKPOINT | Durable объект включён в approved recovery-контур: авторство, manifest/dependencies, Sources, locator, версии, доступ и профильная проверка состава подтверждены | Eligible не означает успешную практическую инициацию; practical recoverability учитывается отдельно |
| PROMOTED_LONG_LIVED_EVIDENCE | Отобранный объект опубликован во внешнем долговременном контуре и прочитан обратно по exact identity | Candidate остаётся candidate; publication не утверждает норму/результат и не доказывает receipt |

[P] Поле operational_authority имеет отдельные значения NONAUTHORITATIVE, BOUNDED_RESUME_AUTHORIZED, REVOKED, UNKNOWN. Значение BOUNDED_RESUME_AUTHORIZED возможно лишь после решения варианта B в §7 и fresh проверки exact task/writer/scope; это не шестой автоматический шаг после durable.

[P] Дополнительные флаги UNVERIFIED, STALE, EXPIRED, UNAVAILABLE, CORRUPT, BLOCKED_CONFLICT, PUBLISHED_UNVERIFIED, PROMOTION_PENDING не стирают историю. Исторический факт подтверждения сохранности остаётся evidence, но при истечении срока, отзыве authority или расхождении объект перестаёт быть пригодным для текущего resume.

[A1,A2] Новый экземпляр проходит initiation и отдельную проверку writer authority; чтение любого checkpoint не переносит скрытую память и не назначает writer. [U] Сейчас положительных runtime claims об этих новых классах нет.

### 1.1. Закрытая таблица допустимых claims

[P] Таблица задаёт ровно шесть именованных claims и связывает их с существующими §§1–7; это не новая последовательность переходов и не дополнительное полномочие. Каждое утверждение относится к exact объекту/версии, applicable scope и доступным evidence refs. При отсутствии обязательного evidence положительный claim не допускается; UNKNOWN сохраняется. Функции и допуски акторов остаются по §2, разрешение конфликтов — по §5; остальные классы и флаги §1 не отменяются.

| Claim | Минимальное exact evidence и связь с существующей моделью | Разрешённый смысл и запрещённые выводы |
|---|---|---|
| CHECKPOINT_WRITTEN | Exact immutable object identity, bytes/checkpoint digest и evidence принятого defined write path результата PUT_IMMUTABLE: operation-qualified key {namespace, task_revision_ref, operation, request_id}, exact_operation_payload_digest и соответствующий persisted outcome RECORDED по §3. Evidence относится к одной exact операции; очередь, намерение записи и UNKNOWN outcome недостаточны. | Принят exact immutable object/request outcome; это written/transient evidence. Не доказывает durability, COMMIT_CURRENT_CAS / current-pointer commit, independent readback, resume authority, currentness, recovery eligibility или substantive acceptance. |
| CHECKPOINT_DURABLE | Только полная существующая конъюнкция D1 ∧ D2 ∧ D3 ∧ D4 ∧ D5 ∧ D6 ∧ D7 ∧ D8 ∧ D9 и exact tuple/evidence §3. Эта строка ссылается на §3 целиком, не сокращает его требования и не вводит альтернативное определение. | Только version-specific сохранность exact bytes в условиях §3. Сама по себе не устанавливает resume authority, approval, current-writer, RECOVERY_READY или acceptance. |
| CHECKPOINT_STALE | Exact checkpoint identity и проверенное основание неприменимости в названном current-use scope: valid superseding lineage; подтверждённая expiry/retention boundary по §4; revoked/ended authority; changed task revision либо нарушенное dependency/currentness condition по §5. Основание имеет собственные exact refs; chronology/timestamp alone недостаточны. | Текущий resume по этому объекту блокируется в указанном scope. Историческое evidence сохраняет свой доказанный смысл; stale не означает уничтожение bytes или автоматическую недостоверность всей истории. |
| CHECKPOINT_CONFLICT | Минимум два exact несовместимых evidence в одном applicable object/authority scope либо exact противоречие checkpoint authoritative dependency; указаны identities обеих сторон, dependency/authority refs, scope и предмет несовместимости по §5. | Fail closed: блокируется resume/использование, требующее разрешения конфликта; обе ветви и provenance сохраняются в разрешённом контуре. Winner не выбирается по timestamp, generation alone или правдоподобию; claim не является resolution. |
| CHECKPOINT_PROMOTED | Exact classification/review authority; permitted promotion class §6; разрешённая либо redacted payload identity с собственным digest; immutable publication locator/version; exact publication readback; provenance link от исходного checkpoint/object к опубликованному artifact. Содержание и disclosure этой связи подчинены privacy/redaction gate §6. | Подтверждена публикационная часть promotion exact payload. Не означает approval, recipient receipt, acceptance, currentness, resume authority или RECOVERY_READY; требуемые §6 dispatch/receipt остаются отдельными фактами и этой строкой не отменяются. |
| RECOVERY_READY | Exact applicable recoverable state/package identity; manifest и dependency refs; действующие Project Sources refs; current-writer/self-state provenance; exact versions/locators; required preservation и readback по A1 и применимому recovery scope; отсутствие unresolved recovery-blocking conflict. Для operational checkpoint сохраняются все условия RECOVERY_ELIGIBLE_CHECKPOINT из §1, включая durable основание. | Только документально подтверждённая готовность указанного состояния/пакета к предусмотренной recovery-процедуре в exact scope. Не выводится лишь из CHECKPOINT_DURABLE или CHECKPOINT_PROMOTED; не доказывает practical cold-start, успешную initiation или Writer Gate и не назначает writer/resume authority. Эти переходы требуют отдельных evidence. |

[P] Таблица остаётся CANDIDATE_NOT_ACTIVE. Она не устанавливает перечисленные claims для deployed checkpoint и не заполняет ни один существующий UNKNOWN.

## 2. Distinct proposed powers and actors for write, durable ack, readback, classification, promotion, preservation and substantive acceptance

[A1,A2] Автор authoritative self-state — соответствующий current-writer. ARH отвечает за preservation/recovery-процесс, но не сочиняет чужой self-snapshot. KAN определяет понятия и границы; техническая возможность записи не даёт полномочия.

[P] Ниже — функции будущего контракта, не назначения Сущностей на новые должности.

| Действие | Предлагаемый допуск и доказательство | Где остаётся решение |
|---|---|---|
| Сформировать self-state | Действующий профильный writer, exact task/authority и ссылки на фактические результаты | Уже заданная авторская граница [A1]; checkpoint scope ещё [U] |
| Записать объект | Аутентифицированный исполнитель по узкому delegation от допустимого автора; exact namespace/task, запрет произвольного current-state | Storage principal, его ACL и operational owner [U] |
| Выдать storage durable ack | Назначенный storage сервис аттестует конкретный commit объекта, применённый профиль durability и срок хранения | Ack issuer, trust boundary и область ответственности [U] |
| Независимо прочитать/проверить | Авторизованный читатель проверяет bytes по durable ref без памяти writer/put-response/cache; фиксирует verifier identity | Verifier и требуемая организационная независимость [U] |
| Читать для задачи | Минимальный task-scoped доступ после privacy/authority проверки | Read authority не следует из write access или доступности URL [P] |
| Классифицировать | Уполномоченный профильный участник определяет тип/значимость/чувствительность, с проверяемым rationale | Classification owner [U]; не обязательно storage owner |
| Отобрать и опубликовать в GitHub | Classifier предлагает, уполномоченный reviewer разрешает exact bytes/класс, publisher механически исполняет | Reviewer/publisher/delegation [U]; approval source/решения не выводится из публикации |
| Подтвердить preservation/recovery | ARH в существующей роли проверяет состав/provenance/readback; технический контур даёт evidence | Новый operational storage owner не назначается ARH автоматически [A1,A2] |
| Содержательно принять результат | Адресат/профильный reviewer или ОПЕРАТОР по существующему contract | Storage ack, receipt, hash и ARH preservation не дают substantive acceptance [A3,A4] |
| Удалить/редактировать/истечь | Только по утверждённому retention/privacy contract и с provenance | Кто может authorise delete/hold/release — [U] |

[P] Один исполнитель может совмещать функции только если это явно допустимо выбранным trust profile; независимость readback должна быть реальной относительно write-path. Подпись автора доказывает происхождение, а не корректность self-state или физическую сохранность. Наличие ключа не означает действующее полномочие. Отзыв/ротация credentials не должны уничтожать возможность проверить старую provenance.

## 3. Precise meaning and required evidence of CHECKPOINT_DURABLE

[P] Claim допустим только для tuple:
`namespace, entity, task_id, task_revision, writer_identity, writer_epoch, generation, checkpoint_id, digest, durable_ref, durability_profile_ref, retention_policy_ref`.
Это version-specific утверждение о сохранности exact bytes в утверждённых условиях, не обещание вечной доступности.

[P] Перед любым положительным claim требуются одновременно:

| № | Обязательное будущее evidence |
|---|---|
| D1 | Approved exact storage/durability contract: назначенный operational owner, trust boundary, failure domains, допускаемые отказы, commit/replication rule, срок хранения и доступ читателей. Незаданные параметры блокируют claim |
| D2 | Подтверждённая identity caller и действующее write authority exact task/namespace; для self-state — current-writer и его неизменный authority ref; worker ограничен delegation |
| D3 | Неизменяемый объект: определённые schema/encoding/hash scope, размер, digest (предложение SHA-256); task revision, causal parent, cursor, input/result refs и необходимые зависимости. Hash покрывает содержимое и контекст, а не только произвольное поле body |
| D4 | Storage commit evidence по выбранному профилю: подтверждены persistent storage/replicas и конкретные failure domains. HTTP 200, запись в буфер/очередь, timestamp, одинаковые копии на одном диске или только подпись writer недостаточны |
| D5 | Независимый post-commit readback через durable ref авторизованным verifier с совпадением exact bytes/digest/metadata; readback result сохранён отдельно от процесса, создавшего объект. Не чтение отправленного буфера или той же временной cache |
| D6 | CAS, generation, dedupe и fencing удовлетворяют правилу ниже; получено evidence единственного принятого successor и отказа stale writer/неверному parent |
| D7 | Readback retention/access proof: объект и обязательные зависимости доступны установленный срок; их сроки не короче заявленного recoverable interval; проверены backup/restore условия выбранного профиля |
| D8 | Отдельно разрешённые implementation verification и независимая проверка exact deployed version/config: crash/restart, partial write/ack loss, corruption, concurrent CAS, stale fencing, partition, retry/readback и expiry negative cases. Test PASS с иной конфигурацией не достаточен |
| D9 | Для данного объекта проверены ack/readback provenance, отсутствие несоответствия или отзыва, актуальность durability contract. Полный набор immutable evidence refs доступен проверяющему |

[P] Короткая формула: `CHECKPOINT_DURABLE = D1 ∧ D2 ∧ D3 ∧ D4 ∧ D5 ∧ D6 ∧ D7 ∧ D8 ∧ D9`. UNKNOWN в любом обязательном условии не даёт PASS. Предложенный gate не требует возвращения Memory-layering attempt 3: будущая техническая проверка должна иметь самостоятельное exact разрешение и не объявлена задачей этой публикации.

[P] Ack содержит tuple, transaction/commit token, writer/fence identity, committed digest, approved durability/retention refs, evidence о размещении, committed/not_committed/unknown outcome. Отдельный readback record содержит reader, requested/observed ref+digest, outcome, evidence locator. Использовать CHECKPOINT_DURABLE можно только после ack **и** readback, а не по одному полю `independently_readable:true`.

[P] CAS (условная замена) сравнивает атомарно полный expected tuple текущего pointer: task revision, writer epoch, generation, previous digest; успешная транзакция создаёт один successor и журнал результата dedupe. Хранилище неизменяемого объекта и движение current pointer должны иметь определённую atomic boundary. Partial object без pointer commit — orphan, не новый current. Конкретный backend/algorithm здесь не выбран [U].

[P] Generation монотонна в своём namespace/epoch, не равна времени; перезапуск процесса и восстановление backup не обнуляют историю. Сравнение generations разных epochs/задач без authority lineage запрещено. Для защиты от ABA в CAS входят epoch и digest, не только счётчик.

[P] Dedupe key имеет operation-qualified форму {namespace, task_revision_ref, operation, request_id}. PUT_IMMUTABLE использует request_id immutable object и связывает exact object bytes/checkpoint digest с RECORDED / NOT_RECORDED / UNKNOWN. COMMIT_CURRENT_CAS использует отдельный cas_request_id, не входящий в digest immutable object, и связывает exact expected/successor tuples, operation payload digest и transaction identity с POINTER_COMMITTED / POINTER_NOT_COMMITTED / UNKNOWN. Совпадение буквального ID в разных operation domains не объединяет их outcomes. Повтор идентичного payload возвращает сохранённый outcome только той же операции; иной payload в том же operation-qualified key — HARD_DEDUPE_CONFLICT. ResolveRequest(namespace, task_revision_ref, operation, request_id, exact_operation_payload_digest), persisted result, StorageAck и readback относятся к одной exact операции/транзакции. PUT ack/object readback не доказывает CAS; CAS ack/pointer readback не заменяет stored-object readback. После потери ack обе операции сверяются раздельно: object-only orphan; обе подтверждены exact object/pointer readback; ни одна — только при authoritative durable negative proof; иначе UNKNOWN_OUTCOME/STOP. Отсутствие записи без такого negative proof не равно NOT_COMMITTED. Слепой повтор и создание нового request ID для обхода неизвестного исхода запрещены. Фактические principals, журнал операций, atomic boundary и retention остаются UNKNOWN.

[P] Fencing — проверяемое хранилищем отсечение прежнего исполнителя. Новый epoch разрешается только после допустимого writer handoff/failover; storage отклоняет записи со старыми tokens. Lease expiry не назначает writer. Lease/fence/CAS сами не дают authority [A1,A2]. Выдающий epoch орган, его durable counter и trust boundary — [U]. При недоказанном fencing новая authoritative запись блокируется. Fencing записи не предотвращает внешние side effects старого worker: их проверяют отдельно перед повтором.

[U] Текущая KOD/SHT evidence характеризует shard gateway как VERIFY-only, WRITE не доказан. D1–D9 для нового operational checkpoint не установлены. `CHECKPOINT_DURABLE: NOT_ESTABLISHED`. Никакие shard/host проверки в этой задаче не проводятся.

## 4. Retention, expiry, backup/preservation, corruption and restoration behavior, including split-brain/unreachable shard

[P] Срок хранения задаётся по классу данных и зависимости, а не единой произвольной цифрой. До решения §7 численные TTL, RPO (допустимая потеря состояния), RTO (время восстановления), число failure domains, replicas/quorum и backup interval — [U]. Неизвестный срок не считается ни нулевым, ни бессрочным.

| Объект | Предлагаемая нижняя граница/условие очистки |
|---|---|
| Raw/transient данные | Только срок, необходимый для диагностики/незавершённой задачи, по privacy policy; до записи известен допустимый срок |
| Durable checkpoint и необходимые refs | До завершения разрешённого resume/recovery window, проверенного successor и разрешения retention/hold; нельзя удалить единственную нужную dependency |
| Dedupe/fence/transaction outcome | Не короче разрешённого окна повторов и восстановления; после компактизации сохранён достаточный tombstone/epoch evidence, чтобы старый запрос не выполнился заново |
| Pending GitHub promotion | До verified promotion или явного решения о прекращении/другом разрешённом сохранении; GitHub failure не разрешает тихое истечение единственной копии |
| Recovery package | По действующему preservation process и approved retention; не очищается только по operational TTL |
| Published private/redacted lineage | По отдельному разрешённому контуру и срокам; public copy не оправдывает хранение секретного оригинала |

[P] TTL требует проверенного механизма измерения времени/истечения и bounds clock uncertainty; project timestamp не придумывается. Если время/lease не проверяются, срок нельзя продлевать догадкой, read/resume — WAIT_RETENTION_VERIFICATION. Unknown не превращается в автоматическое разрешение удаления.

[P] Backup должен сохранять bytes, manifest, dependency graph, ACL/key availability и transaction/fencing lineage. Восстановление в изолированное место сначала проверяет digest и причины отката; прежний epoch нельзя оживить как новый current. Backup, live replica и independent readback — разные свидетельства; восстановимость проверяется отдельно [A1].

| Failure | Предлагаемая реакция |
|---|---|
| Crash до ack | Не считать новый cursor committed; проверить outcome; использовать только доступное разрешённое последнее verified состояние |
| Ack потерян/timeout | OUTCOME_UNKNOWN; query/readback по прежнему request_id; без слепого повторения effects |
| Shard unavailable | UNAVAILABLE; продолжение, требующее checkpoint, остановлено. Проверить last externally verified recovery; отметить stale boundary, ничего не реконструировать |
| Split-brain/разные heads | BLOCKED_CONFLICT; сохранить обе версии и provenance; не выбирать по timestamp/большему числу replicas вне утверждённого consistency contract |
| Digest mismatch/corruption | CORRUPT; quarantine в разрешённых пределах; не отдавать bytes как trusted; восстановить проверенную копию и повторно проверить всю lineage |
| Старый writer ещё жив | Не переносить writer authority по availability; fence/authority reconciliation, отдельная оценка незавершённых effects |
| GitHub недоступен | PROMOTION_PENDING; не заявлять публикацию. В варианте A resume authority не появляется; в B продолжение возможно только в заранее разрешённом outage scope/window и при отсутствии обязательной GitHub dependency |
| Retention deadline близко, promotion не готов | Эскалация владельцу/КОО; требуется разрешённое продление, альтернативное сохранение или явное прекращение, не тихая потеря |
| Expired/отозванный checkpoint найден в backup | Историческое evidence, не автоматическое разрешение текущего resume |

[A1] Новый экземпляр проходит recovery по действующему канону. [P] Даже при варианте B перед продолжением повторно сверяются task revision, Sources, writer, dependencies и cursor/effect ledger. Если внешний effect мог произойти, но его результат неизвестен, checkpoint не даёт права повторить его; нужен independent reconciliation. `resume from cursor` не обещает exactly-once для внешнего мира.

## 5. Conflict and supersession matrix by object class

[A1–A6] Правила, решения, результаты, роли и storage records имеют разную область полномочий. Нельзя построить универсальный порядок «самый новый источник всегда прав». Ни GitHub commit time, ни shard generation не создают semantic authority.

| Конфликт | Уже действующая граница / предлагаемое разрешение |
|---|---|
| Checkpoint против approved Sources | [A3,A5] Candidate/checkpoint не отменяет норму. STOP; применяется действующая норма в её scope, конфликт требует явного решения; нет silent override |
| Checkpoint против explicit OPERATOR decision | [A2,A3] Проверить exact содержание, scope, статус и supersession решения. [P] Новый checkpoint должен ссылаться на него; противоречащий checkpoint не используется. Решение о цели не равно разрешению host/write/доступа |
| Два approved Sources либо неоднозначное решение ОПЕРАТОРА | [A3] Остановить профильное действие и запросить точное разрешение, не придумывать приоритет |
| Checkpoint против authoritative current-writer | [A1] Storage не назначает writer. [P] Exact writer epoch/authority проверяются; competing writer — STOP, разрешение через существующий handoff/failover gate |
| Shard против immutable GitHub decision/accepted result | [P] Сверить object identity, task revision и authority цепочку. Checkpoint не может объявить accepted результат отсутствующим или отменить решение. Недоказанный successor — BLOCKED_CONFLICT |
| Shard против GitHub current-state того же task | [P] A: checkpoint только evidence. B: утверждённая delegation и causal successor позволяют bounded progress после известного GitHub base; публикационный lag помечается. Разветвление, неизвестные changes, иная revision — STOP; «shard свежее» недостаточно |
| Checkpoint против ARH preserved recovery | [A1] ARH preservation не переписывает self-state; last verified recovery сохраняется. [P] Более поздний checkpoint не обязательно конфликт: если доказаны lineage и разрешённые изменения, это отдельный successor. Противоречие без такой цепи блокирует восстановление |
| Raw/log/digest против checkpoint | [P] Raw может выявить ошибку, но не повышается до current автоматически; фиксируется competing evidence и профильная сверка |
| Одинаковая generation, разные digests / два parents | [P] Конфликт целостности/branch; freeze applicable namespace, provenance обеих ветвей, явное resolution record; не merge self-state по правдоподобию |
| GitHub publication success, shard promotion pointer не обновлён | [P] Читать exact published commit/blob и прежний request outcome. Подтвердить связь, а не заново публиковать или считать promotion complete без readback |

**Граница старого shard-направления.** [E] Два прочитанных KOO direction-файла сохраняют GitHub как canonical immutable evidence; операционные shards не получают writer/acceptance/project-state authority. Это профильное направление для file/Git механики, а не новый универсальный recovery-канон. [A1] Recovery v1.6 прямо допускает иные внешние контуры; [A4] информационное поле включает другие разрешённые источники. Это разрешение класса возможностей не утверждает конкретный shard-контур.

[P] Вариант B §7 требует явного решения, которое укажет исключение/изменение старого направления **только** для bounded task-progress checkpoint. GitHub decisions, Sources, writer establishment и accepted results не заменяются. При невозможности согласовать scope требуется explicit normative amendment/activation, а не декларация КАН о «конфликта больше нет». Вариант A нового authority domain не создаёт.

## 6. Candidate GitHub promotion classes, mandatory/optional selections, reviewer, privacy/redaction, secret exclusion, promotion and readback failure semantics

[P] «Обязательно» ниже — предложение политики отбора после её утверждения, а не требование новой нормы сегодня. [A3,A6] Уже действуют самостоятельный значимый артефакт, проверяемая версия, privacy и различение publication/receipt/acceptance.

| Класс | Предлагаемый отбор | Проверяющий и статус |
|---|---|---|
| Значимый terminal/result, blocker, принятие/отклонение | MANDATORY для воспроизводимости следующего решения; сохранять exact outcome и существенные ограничения | Профильный author/reviewer в existing authority; failed результат не скрывается |
| Решение ОПЕРАТОРА, approved Source/current-writer transition | MANDATORY точное решение и provenance | Уполномоченный decision owner; publisher не выдаёт candidate за approved |
| Recovery snapshot/package | MANDATORY по event triggers канона; exact состав/checksums/dependencies | Self-author current-writer + ARH preservation boundary [A1] |
| Основание выбора cursor и необратимый внешний effect | MANDATORY минимальное проверяемое evidence, если без него нельзя безопасно продолжить/разобрать отказ | Exact scope classification/reviewer [U], нельзя заменить нужный факт бессодержательной сводкой |
| Компактный индекс checkpoint generations | CONDITIONAL: достаточно для task/recovery lineage и поиска exact данных в разрешённом контуре | Указатель не заменяет недоступные или истёкшие существенные bytes |
| Reusable lesson / journal-source | OPTIONAL по практической/редакционной ценности, batching | ARH/RED по существующим ролям; не автоматическая публикация |
| Высокочастотные progress/raw events/retries | EXCLUDE_BY_DEFAULT из публичного GitHub; агрегат при достаточности и privacy | Не «весь raw обязателен» и не «весь raw можно уничтожить»; dependency/retention правило первично |
| Непроверенная гипотеза/черновик | Не project truth. OPTIONAL как явно маркированный candidate, если нужен review | Не запрещает публикацию данного non-live кандидата |
| Секреты, credentials, приватные данные без public authority | NEVER_PUBLIC; не помещать в raw payload/reusable memory | Закрытый разрешённый контур/безопасный redacted derivative; публичный digest тоже проверяется на раскрытие |

[P] Promotion sequence: exact input → classification → privacy/redaction review → permitted payload + ожидаемый digest → immutable publication → exact readback → provenance link → адресный dispatch/receipt по действующему contract. Content acceptance отдельно. Reviewer identity, решение и checks относятся к конкретным bytes; последующая правка инвалидирует прежнюю проверку для новых bytes.

[P] Редактирование чувствительных данных создаёт **производный** объект с собственным digest и описанием удалённых классов; не выдаётся за точный исходный checkpoint. Приватная связь с оригиналом хранится лишь если разрешена. Не публиковать низкоэнтропийные secret hashes, URL с токенами, private locators, скрытые приложения/логи. Если sanitization уничтожает необходимое recovery evidence, public derivative не считается достаточным recovery.

[P] Частота promotion — событийная (terminal/решение/значимый этап/изменение authority/перед риском), с будущим bounded backlog/outage window, определяемым §7. Численная частота и объём ещё [U]. Privacy review или отсутствие approval нельзя обходить «обязательностью публикации»: WAIT_PRIVACY_REVIEW/разрешённое закрытое сохранение.

[P] Publication failure → PROMOTION_PENDING/FAILED; readback failure → PUBLISHED_UNVERIFIED; receipt отсутствует → DISPATCHED, не RECEIVED. При частично опубликованном пакете нет complete package claim. Уже опубликованные bytes не переписываются незаметно; исправление — successor и явная invalidation/supersession. При утечке — ограниченное incident response по существующим полномочиям, а не утверждение, что удаление из HEAD устранило всю историю.

## 7. One exact bounded OPERATOR decision gate

**GATE_SHARD_CHECKPOINT_STATUS_AND_ACCOUNTABILITY_R01** — одно нормативное решение после reconciliation КОО и необходимых независимых reviews. КАН не выбирает вариант и не назначает владельца.

| Вариант | Что решает ОПЕРАТОР | Следствие |
|---|---|---|
| A — только неавторитетное evidence | Checkpoint остаётся оперативным cache/evidence даже после durable verification | Для resume требуются отдельно authoritative state/recovery основания; shard не определяет current cursor сам |
| B — ограниченное состояние продолжения | Разрешить проверенному checkpoint operational authority исключительно для exact task-progress/cursor в перечисленном scope | Необходимо явно изменить/ограничить прежнее shard-направление, назначить полномочия и доказать весь contract до использования; approval Sources/решений/writer не переносится на shard |
| C — отложить/отклонить новую политику | Не принимать A/B до дополнительных сведений | Сохраняются текущие границы; operational write/resume не разрешаются |

[P] Решение A или B должно заполнить **одну карточку**, не набор скрытых автоматических решений:
- выбранный вариант, exact candidate identity/version и scope: entities/tasks/classes/exclusions;
- operational owner и named write/ack/readback/classification/promotion principals, reviewer/разделение функций; existing ARH role сохраняется;
- approved durability/failure profile, namespaces, epoch/fence authority, transaction boundary и evidence acceptor;
- retention для payload/dependencies/dedupe/fencing, expiry/time basis, backup/restore, RPO/RTO и outage/backlog пределы; отсутствие чисел — pending, не implicit default;
- применимая conflict matrix, exact relation к старому GitHub canonical direction, разрешённые successors и орган решения конфликтов;
- privacy/read scope, public promotion classes, redaction/delete/hold authority;
- способ нормативного adoption/effectivity и ссылки на необходимые amendments; implementation/live authority: **NOT_GRANTED_BY_THIS_DECISION**.

[P] Незаполненная карточка может выразить предпочтение, но не завершает adoption gate. Единственное решение «выбираю B» без scope/actors/retention/conflicts недостаточно для operational authority.

[A2,A3] Нормативное принятие и фактический rollout — разные gates. После возможного adoption ещё нужны отдельно разрешённые implementation/test/deployment действия и их независимое evidence (§3). Ни этот design, ни будущий approval сам по себе не разрешает provider call, shard write, автоматический spawn, host access или изменение automation. Future review ARH/SHT/SIS/KOD определяет КОО после fresh reconciliation; этим документом такие задачи не запускаются.

## Основания и exact lineage

Все locators ниже относятся к puev5691/wellbeing-hq; read_ref для Sources и directions: 5d32517d525516c358b6dbd198a99e9deb0bd234.

- A3: entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md; blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33.
- A2: entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md; blob 1772339cb74dae8550bfbd2e33401c34a929e911.
- A1: entities/koordinator/outbox/source-set-r03-approved/entity-state-preservation-and-recovery-canon-v1_6-approved.md; blob 233117e1c9509d730e1f5ec532b1cabe3f786609.
- A6: entities/koordinator/outbox/source-set-r03-approved/file-work-canon-universal-v2_4-approved.md; blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2.
- A5: entities/koordinator/outbox/source-set-r03-approved/source-loading-policy-v2_2-approved.md; blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf.
- A4: entities/koordinator/outbox/task-conveyor-v1_2-approved/task-conveyor-canon-v1_2-approved.md; blob df7896d867eeeffff506319538fedad938856686.

Применяемые разделы: A1 — авторство self-snapshot, внешнее сохранение, initiation/Writer Gate, роли, practical recoverability; A2 — полномочие не capability, KAN/ARH/KOO boundaries; A3 — authority, достоверность, human-first и delivery; A4 — exact authorized task, historical PROMPT и activation; A5 — candidate/approved status и минимальная загрузка; A6 — file-first, версии, delivery, privacy, запрет имитации выполнения.

- task: entities/koordinator/outbox/KOO__shard-checkpoint-governance-r01-design-task__KAN.md@5d32517d525516c358b6dbd198a99e9deb0bd234; blob cf679833141d960e172b2aebe7ef42336ab53319.
- review: entities/shtabist/outbox/SHT__autonomous-entity-conveyor-r01-independent-review__KOO.md@7b875234b84049294166b082c48519151e46affe; blob e3344d43d3ae819186ccf6836fc7d12e0db40976.
- spec: entities/koder/outbox/KOD__autonomous-entity-conveyor-cross-component-spec-r01__KOO.md@eb1f0f6cefaad9aa6858cf36caa3d8bf7a01d652; blob 9f25cce99ebd5c39863fda6a263297c66b0a64cd.
- E1: entities/koordinator/outbox/KOO__file-artifact-git-shards-r01__PROJECT.md; blob a32d248e6296ab3a0ba07ca07e6d163bf6d3c0ee.
- E2: entities/koordinator/outbox/KOO__git-operational-shards-priority-r01__OPERATOR.md; blob 5b19033eff68f5409992631e38adc9bbd759fa2e.

Открытые [U]: выбор A/B/C; operational owner и actor grants; storage trust/failure/transaction boundary; replication/CAS/fence реализация; retention/time/backup/restore параметры; exact normative effectivity; privacy scope и promotion reviewer. Указанные UNKNOWN — конкретные inputs gate, а не замена готового предложения.

---
КТО: KAN / KAN-current-writer-v02
physical_instance: KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857
task: DESIGN_SHARD_CHECKPOINT_GOVERNANCE_R01
status: CANDIDATE_NOT_ACTIVE
owner_assignment: NOT_MADE
operational_checkpoint_authority: NOT_GRANTED
CHECKPOINT_DURABLE: NOT_ESTABLISHED
Memory-layering_attempt_3: NOT_AUTHORIZED
implementation_shard_write_host_access_secrets_provider_calls_automation_change: NOT_PERFORMED
Project_Sources_or_canon_mutation: NONE
project_time: omitted
