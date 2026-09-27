# КАН → КОО: независимая проверка STP-C r0.1

Модель пригодна как документальный кандидат для последующего выбора параметров ОПЕРАТОРОМ. Она отделяет коллективное решение от аутентификации, публикации и активации, сохраняет остановку при конфликте и неизвестной актуальности. Критического дефекта, требующего отклонить exact candidate на этой стадии, не обнаружено.

PASS относится только к модели и указанным ниже границам. Он не подтверждает независимость реальных участников, криптографическую защиту, работоспособность verifier или готовность активировать профиль. Кандидат не изменён. Следующий шаг — reconciliation КОО и подготовка конкретного bounded решения, а не ещё один идентичный общий review.

terminal: PASS_KAN_STP_C_GOVERNANCE_MODEL_R01_WITH_BOUNDARIES
scope: INDEPENDENT_DOCUMENT_ONLY_NORMATIVE_GOVERNANCE_REVIEW
reviewed_candidate_status: CANDIDATE_NOT_ACTIVE
critical_defects: NONE_FOUND_IN_REVIEWED_DOCUMENT_SCOPE
operational_admission: NOT_GRANTED
fast_gate_activation: NOT_PERFORMED
project_time: omitted

## 1. Exact admission и provenance

Repository: puev5691/wellbeing-hq; fresh main HEAD b565c7c0f6f40a1dc83704f510cc6d43cd7daa35; recursive tree truncated=false.

Exact task:
b565c7c0f6f40a1dc83704f510cc6d43cd7daa35:
entities/koordinator/outbox/KOO__STP-C-governance-model-independent-review-r01__KAN.md
blob deca04112ec6ba3b660987e256f5dc1908c0afbd.

Exact OPERATOR authority:
695aaf9b6b87c312311227ad510db6e237aeed13:
entities/koordinator/outbox/KOO__authorize-KAN-STP-C-governance-model-independent-review-r01__OPERATOR.md
blob 1e4b3d6786e1c4511c91648889c703a7554ac122.
Прямое поручение ОПЕРАТОРА в текущем чате подтверждает тот же scope.

Exact candidate:
622addc16bd8efa8736f3332dd31cee0e7b5dcb1:
entities/shtabist/outbox/SHT__STP-C-multiparty-governance-model-design-r01__KOO.md
blob 4191acf5ced6066397c5c734f9246b2098bcb46e.
Immutable read выполнен; current tree содержит тот же blob. Superseding candidate и уже выполненный KAN STP-C review result в проверенном дереве не найдены.

KAN current-writer повторно прочитан на fresh HEAD:
entities/kancelar/current/KAN__replacement-current-writer-v02.md;
establishment commit 588493b011cf4ad85a94d40f6513644d9c207b9c;
blob 13b91b0e189f681be8abf13a76a47b03a5c830fa.
writer_identity: KAN-current-writer-v02.
physical_instance: KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857.
Это проектная метка, не новая платформенная аттестация chat ID.
Writer Gate result повторно прочитан:
entities/kancelar/outbox/KAN__writer-gate-v02-result__OPERATOR.md;
establishment commit 254500649a2bfa3ace7d2e4cc72b4d00cacaaa4d;
blob b58219e9655a4caa85cdcaeac15b59331e3436b4;
PASS_KAN_PHYSICAL_V02_WRITER_GATE.
Newer writer/handoff и отмена exact задачи не обнаружены. Recovery не воспроизводился, потерянное self-state не реконструировалось.

На fresh HEAD прочитано также решение о выборе семейства:
entities/koordinator/outbox/KOO__select-STP-C-multiparty-approval-profile-r01__OPERATOR.md;
blob 5c2b16545d088365962b2a44846a76190c8980da.
Оно выбирает только STP-C family, не actual participants/root/quorum.

### Дублирующая постановка

В дереве есть совместимая более ранняя формулировка:
entities/koordinator/outbox/KOO__STP-C-multiparty-governance-independent-review-r01__KAN.md;
blob 0f28bdcb141f107c70548d4045d624bba1191237;
и authority record blob 07210def26578386ebab817901512c94e8eeebe4.
Они прочитаны как evidence, не исполнены отдельным циклом. Candidate тот же; нового несовместимого объёма нет. Текущее прямое поручение ОПЕРАТОРА однозначно выбирает task b565c7… и дополнительно требует complexity review. Этот один result отвечает текущей задаче; КОО рекомендуется связать дублирующую постановку с ним, не запрашивая второй общий review. Формальное закрытие чужой очереди КАН не выполняет.

## 2. Матрица независимого review

| Критерий | Exact sections / вывод | Граница PASS |
|---|---|---|
| 1. Составы участников | §2 C1–C4 названы role compositions, §9 NOT SELECTED; dual-role требует explicit OPERATOR approval и conflict analysis. PASS | KOO/KAN/SHT/SIS-class — примеры, не назначения. Одобрение совмещения не доказывает независимость и не даёт двойной счёт одному контролирующему principal |
| 2. Кворумы | §3 Q1–Q4 candidate; Q2 2 APPROVE + current REJECT по default блокируется; §§5,10,11 запрещают silence-as-consent и implicit casting vote. PASS | Исключение «если ОПЕРАТОР позднее утвердит другое правило» не является текущим разрешением игнорировать REJECT. Любой иной conflict contract — отдельно рассматриваемое изменение политики |
| 3. Реальная независимость | §2 запрещает скрытое занятие нескольких seats одним runtime/credential identity; §3 требует independence proof; §9 conflict/threat/failure analysis. PASS как требование модели | Разные имена, чаты, ключи одного администратора сами по себе не доказательство разных независимых seats. Фактическая независимость NOT_ESTABLISHED |
| 4. Emergency revoke | §3 Q4 и §6 R2 разрешают только отдельно одобренный REVOKE/FREEZE exact profile/revision/scope. Запрещены successor approval, widening, appointments, quorum change и writer authority. PASS | Общий запрет grant/widen authority (§10.7) охватывает task/trust authority. Revoker не может снять freeze собственным «отзывом отзыва» и тем самым подменить admission; повторный допуск проходит обычный applicable gate |
| 5. Approval evidence | §4 связывает profile_id/revision/digest/scope и participant identity/role/revision/currentness; §5 и §6 R1 запрещают перенос approvals. PASS | Evidence-set encoding/hash coverage, подпись и authoritative completeness ещё не implementation spec. Изменение policy revision либо роли требует revalidation, не повторного использования старого PASS по имени |
| 6. Currentness/revocation | §§5,6 R3–R5,11: unknown/stale/revoked/superseded блокируют допуск; timeout не согласие. PASS | Unavailable seat с проверенными identity/currentness не равен UNKNOWN currentness. Q2 может терпеть отсутствие голоса, но не неизвестность обязательного revocation/conflict evidence |
| 7. Signer/attestor | §§2,7,8: signer аутентифицирует exact evidence, не решает governance truth. PASS | Подпись без applicable authority/ref/currentness не голос и не trust grant. Механический signer не становится дополнительным независимым seat |
| 8. Separation | §7 отделяет mutation service, read-only verifier и publisher; publication не approval/activation. PASS | Функциональная схема не доказательство изоляции deployment/credentials/admin domains. Store access не даёт verifier или publisher decision authority |
| 9. Authentication root | §§8,9 root-technology agnostic; примеры не default. PASS | Git path, commit, key или выбранное имя не active root. Нужен отдельный approved binding и проверка lifecycle; технология здесь не выбрана |
| 10. Activation | §4 QUORUM_SATISFIED_CANDIDATE не activation; §§7,10,12 сохраняют отдельное final admission authority. PASS | В scope текущего task это отдельное явное OPERATOR authority. Одобрение семейства STP-C, review PASS или заполненный approval-set его не заменяют |
| 11. Complexity | Раздел 4 этого result отделяет редкие изменения от routine checks и указывает наблюдаемый дубль постановок. PASS | Предложение оптимизации не активирует Fast Gate и не изменяет канон |

## 3. Существенные границы перед конкретным выбором и реализацией

Это не новые назначения/политика и не скрытая правка candidate. Они обозначают недоказанные условия его собственных требований.

B1 — карта независимости. Для будущего exact состава нужны связи seat → principal → credential custody → runtime → admin/control/failure domain, возможность одного контролёра подменить несколько решений, конфликт интересов requester/reviewer. Общий домен не засчитывается как несколько независимых seats без доказанной допустимой изоляции по выбранной модели угроз; разные labels не устраняют общий контроль. Q1 «нужно скомпрометировать оба seats» верно лишь при этих предпосылках, а не при общей компрометации root/verifier/admin.

B2 — полнота decision set. §4 перечисляет excluded/rejected/stale IDs, но не задаёт технологию обнаружения всех актуальных решений. При реализации verifier должен доказуемо не пропускать current REJECT, не исключать его как «неудобный голос» и различать авторизованный supersession решения от его удаления publisher. В одном scope два несовместимых текущих решения — conflict до явного resolution. Это evidence requirement до допуска, не причина выбирать транспорт сейчас.

B3 — currentness на границе использования. Свежесть включает profile, participant roles, quorum policy, revocation/root bindings и отдельное admission authority. Положительный результат вчерашней проверки не покрывает отзыв между check и effect. Future interface обязан связать проверенную revision с exact действием и запретить использование после invalidation/expiry/unknown; механизм, clock/freshness bounds и atomicity ещё UNKNOWN.

B4 — emergency containment. Уменьшенный revoke quorum, если когда-либо выбран, не заменяет обычный admission quorum. Нельзя использовать emergency path для key rebind, participant rotation, policy rewrite, task issuance или successor activation. Возможность отказа в обслуживании при компрометации revoker — отдельный явно принимаемый риск.

B5 — evidence format. Candidate содержит концептуальные поля, а не closed wire schema. До технической реализации потребуются точные hash/signature scopes, защита от replay, role-policy binding, canonicalization и зависимости evidence_set_digest без циклической самоссылки. Текущий review не делает выбор технологии и не выдаёт формат за реализованный.

B6 — человеческий admission. КОО должен представлять конкретный exact scope/вариант и последствия, а не просить одним общим «одобряю» одновременно назначить участников, создать root, разрешить host WRITE и activation. Уже разрешённый review завершается сейчас; новая цепочка approval не возникает из самого PASS.

## 4. Проверочная сложность: Heavy Gates / будущий Fast Gate

Следующая классификация — аналитическое предложение внутри разрешённого review. Ни standing authority, ни новый канон, ни Fast Gate не создаются.

| Триггер/объект проверки | Редкий state-changing Heavy Gate | Что позже можно проверять быстро |
|---|---|---|
| Создание/изменение состава, ролей, совмещений, quorum/conflict policy | Анализ независимости, threat/conflict model, точный OPERATOR выбор и immutable policy revision | Совпадение ранее рассмотренных policy/role refs, отсутствие invalidation |
| Root/custody/attestor/admin domain, rotation/compromise/recovery | Проверка новой границы доверия и binding; independent technical review по изменённому риску | Exact binding, validity/revocation, отсутствие неизвестной или сменившейся identity |
| Новый profile revision/digest/scope или high-impact classification | Новый approval set в applicable quorum; conflict resolution; отдельное OPERATOR admission authority | Проверка exact admitted revision/digest/scope и текущего статуса, без нового голосования за неизменные bytes |
| Реализация verifier/mutation boundary или изменение enforcement | Отдельно разрешённая implementation verification, negative cases, TOCTOU/replay/outage/compromise проверки | Проверка применимости exact verified version/config evidence; change invalidates cached applicability |
| Emergency revoke/freeze | Заранее отдельно определённое revoke-only authority и eligibility. Сам срочный revoke не должен ждать повторения общего design-review | Проверка exact scope, допустимых revokers и сохранение outcome; post-event audit отдельно. Не разрешение invoke сейчас |
| Обычное действие в неизменном ранее admitted scope | Нет причин повторять весь design review и выбирать участников заново | Аутентификация request; task/writer/action authority; profile/policy revision; freshness/revocation/conflicts; replay/dedupe/fence где применимо; bounded result evidence |

Для возможного Fast Gate можно повторно использовать проверку неизменных bytes и структуры evidence по digest. Нельзя таким образом навсегда кэшировать currentness, revocation, authority или отсутствие конфликта. Они должны иметь approved freshness/validation contract и проверяемый источник. Stale/unknown/cache miss не превращаются в allow; при изменении scope/policy/roles/domain — возврат на applicable Heavy Gate, при обычном временном outage — stop/wait, а не обязательный новый полный design-review.

Не предполагается, что каждый routine request требует нового голосования, полного GitHub scan и повторного SHT→KAN→SIS→ARH круга. Вместе с тем экономия шагов допустима только после отдельного утверждения и технического доказательства future fast-path; сейчас он не разрешён и его latency/реализация UNKNOWN.

### Что действительно дублируется

Наблюдаемый дубль: две KOO постановки одного независимого review одного exact candidate, перечисленные в §1. Текущая добавляет complexity review; достаточно этого единственного расширенного результата и явной привязки обеих постановок КОО.

Не обнаружено evidence, что все будущие reviews уже запущены или что работающий конвейер фактически повторяет их на каждом запросе. Поэтому следующие пункты — критерии предотвращения избыточности, не обвинение в наблюдённом runtime дефекте:
- повторная общая проверка тех же bytes без нового scope/evidence не создаёт новой причинной функции;
- авторская SHT проверка и данный независимый KAN review не дубли: различаются авторство и функция;
- review семантики KAN и будущая проверка технического enforcement SIS не дубли;
- quorum, аутентификация, OPERATOR admission и проверка currentness не взаимозаменяемы;
- publisher readback, recipient receipt и содержательное acceptance — разные факты; их можно связывать одним exact evidence, но нельзя объявлять один другим;
- ARH нужен для applicable preservation/recovery требований, а не как универсальный дополнительный approval seat по умолчанию.

## 5. Approved Sources и ограничения проверки

На fresh HEAD повторно загружены все шесть approved Sources. Blobs совпали с заново вычисленными blobs приложенных файлов:
- core v2.5: a42f7dca6a7469a54fa2da24aae0da4e549c9d33;
- roles v2.4: 1772339cb74dae8550bfbd2e33401c34a929e911;
- recovery v1.6: 233117e1c9509d730e1f5ec532b1cabe3f786609;
- file-work v2.4: e9c29d62057f34e4f771d6057a36d9b7f72e74c2;
- source-loading v2.2: 69eb657f260a019f76e8e707c880ea88c1dfa0bf;
- task-conveyor v1.2: df7896d867eeeffff506319538fedad938856686.
Effectivity evidence: source-set r07 blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99; staged PRV activation result blob e7c11b2f5291bad1c5d2a8b4f146bf73080cc9e6 не устанавливает active replacement roles v2.4.

Review основан на exact candidate и authority, без внешних предположений о выбранной криптографии или текущем runtime. Документальный PASS не независимое доказательство capability реальных участников.

Никто не назначен. Active quorum, technology/root, keys/credentials, attestor, backend/host/operator не выбраны. Profile и Project Sources не активированы. Live WRITE/CAS/deployment, EOM pilot, memory-layering attempt 3 не выполнялись. CHECKPOINT_DURABLE не установлен. Candidate bytes не изменены.

## 6. Возврат и следующий gate

КОО: fresh-reconcile этот exact review, связать дублирующую постановку с одним результатом и подготовить bounded decision для ОПЕРАТОРА по C/Q и B1–B6 только в пределах существующего authority. Если данных для осмысленного выбора недостаточно, назвать один конкретный missing input, не назначать ещё один идентичный общий review. Final profile-admission authority остаётся отдельным.

После immutable publication/readback result — адресные inbox/dispatch и sender-registry. Они не доказывают receipt КОО, activation, processing_started или acceptance. КАН останавливается.

Короткий journal-source для RED: независимая проверка STP-C сохранила принцип коллективного решения и отделила его от подписи и запуска. Главный вывод — повторять дорогую проверку устройства доверия нужно при его изменении, а перед обычным действием всё равно необходимо подтверждать актуальность полномочий. Fast Gate предложен как направление будущей оптимизации, но не включён. Журнал не редактировался.

---
КТО: KAN / KAN-current-writer-v02
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_KAN_STP_C_GOVERNANCE_MODEL_R01_WITH_BOUNDARIES
