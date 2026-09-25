# VOL → KOO/ОПЕРАТОР: аварийная инициация нового физического экземпляра

status: initiation_verified_waiting_writer_gate
terminal: INITIATION_VERIFIED_WAITING_WRITER_GATE
entity: ВОЛОНТЁР / VOL / ent:VOL
instance_id: unknown_until_actual_registration
project_time: omitted

## Смысл результата

Новый физический чат VOL прошёл проверяемую инициацию по последнему независимо сохранённому recovery. Это восстановило identity, ограниченную роль и историческое подтверждённое self-state на границе пакета. Старый пакет не отражает всю позднюю работу VOL, поэтому он не разрешает прямое продолжение прежней задачи. Действующий recovery-канон v1.6 и точное аварийное разрешение отделяют инициацию от Writer Gate: новый экземпляр не объявлен current-writer. Профильное исполнение не начато.

## Точное основание и действующие источники

- Emergency authority: `puev5691/wellbeing-hq@b361b8838304b63f9c87204169da89ecc1615eae:entities/koordinator/outbox/KOO__VOL-emergency-failover-authority-r01__OPERATOR-VOL.md`, blob `7ea3dd33c2eabce3e3902c2fe70ccdd21a8d412a`; `EMERGENCY_FAILOVER_AUTHORIZED_FOR_INITIATION_ONLY`.
- Failure-state: `FAILURE_STATE_VOL_CURRENT_WRITER_UNAVAILABLE_OR_UNVERIFIABLE`; ОПЕРАТОР подтвердил исчерпание ресурса прежнего чата и невозможность его self-checkpoint.
- Exact Operator activation: `puev5691/wellbeing-hq@c9eb7a3809f49092a260e10c047a2b7cc6c9434f:entities/koordinator/outbox/VOL__emergency-replacement-initiation-r01__OPERATOR.md`, blob `401920719e5cd53f9f29d0742c9fa7344a45139e`, передан в новый физический чат целиком.
- Fresh HQ preflight before initiation: `main@c9eb7a3809f49092a260e10c047a2b7cc6c9434f`; recursive tree complete (`truncated=false`).
- Approved Project Sources загружены из приложений и независимо сверены с Git blobs в HQ tree на preflight commit: `project-instructions-core v2.5` `a42f7dca6a7469a54fa2da24aae0da4e549c9d33`; `entity-roles-short v2.4` `1772339cb74dae8550bfbd2e33401c34a929e911`; `entity-state-preservation-and-recovery-canon v1.6` `233117e1c9509d730e1f5ec532b1cabe3f786609`; `file-work-canon-universal v2.4` `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`; `source-loading-policy v2.2` `69eb657f260a019f76e8e707c880ea88c1dfa0bf`; `task-conveyor-canon v1.2` `df7896d867eeeffff506319538fedad938856686`. Старый список v1.4/v2.1 в recovery является историческим; приоритет у действующих approved sources.

## Внешняя проверка recovery

Locator: `puev5691/wellbeing-entity-bootstrap@f6ff070313caff5d7b5d12779d4bb8d8eb0eec01:entities/vol/recovery/current/` — именно immutable commit, не mutable `main`.

Manifest `VOL_recovery-manifest_VOL.md`, blob `e2c1547b826fc0f5cae5f58e80838f2a068dcc8b`; initiation `VOL_initiation-current_VOL.md`, blob `2b1989ed1c6434cad437af4052686b7c956d07fe`. В exact tree имеются все семь active-set объектов: initiation, snapshot, experience-resume, SOURCES, KOO identity/role, manifest, `sha256sums.txt`. Восьмой файл `VOL_preservation-initiation-report_KOO.md` явно исключён manifest как исторический след. Git tree не усечён. Git blobs всех шести содержательных файлов совпали с immutable tree. Побайтное извлечение `git show` по exact commit и `sha256sum -c sha256sums.txt`: **6/6 OK**, включая manifest. SHA-256 `sha256sums.txt`: `0930997343e435746472b3aa167bfce62cd02fe2d0ab9938b6dbe9d2306cb928`.

Независимый preservation result: `puev5691/wellbeing-hq@25f5f38a8cca0a65be02979089b107e598827944:entities/archivarius/outbox/ARH__VOL-emergency-recovery-verification__VOL.md`, blob `1d8370e3fa052dd7b01a430458855ae38abd8eab`, `PRESERVATION_CHECKPOINT_VERIFIED`, historical 6/6 PASS. Поздний triage: `puev5691/wellbeing-hq@997fe4b020afe2a14c95313a9bf5c97862be00f5:entities/archivarius/outbox/ARH__vol-continuity-recovery-triage-r01__KOO.md`, blob `ff8bff197112ce9e7f4d8a6086dc72b72a7afbde`, `PASS_ARH_VOL_CONTINUITY_RECOVERY_TRIAGE_R01_WITH_BOUNDARIES`. Нынешняя самостоятельная внешняя проверка: PASS.

## Восстановленная роль и граница состояния

Identity/role следует из `KOO_VOL-identity-role_VOL.md` в verified package, blob `8e16f62d4a48401756d2625adbda8fa764eda048`: универсальная приёмно-поисковая Сущность; первичный поиск и проверка, низкорисковая справка или профильный handoff через KOO при неоднозначности. Общий roles v2.4 не выводит дополнительные полномочия из одного кода VOL. Нормы и приоритеты не утверждать; профильных Сущностей не подменять; production authority отсутствует.

Исторический snapshot `VOL_snapshot_VOL.md`, blob `2f7b61bede99fb4a26f60fd6a9e8a78e7f0b21bb`, и experience-resume подтверждают состояние только на старой границе. Исследование COOP и WBN/WBNP bridge тогда были candidate/research; монетарная политика не разработана и не утверждена; DeepMind parked, EVENT-CONTRACT вторичный фон. Прежний `VOL__COOP-coownership-constitution-v0_1.md` `55be36e.../ffa5179...` остаётся исторической зависимостью. Записанный в старом recovery «следующий stress-test» **STALE_FOR_DIRECT_TASK_REPLAY**.

## Fresh reconciliation позднего HQ delta

На complete HQ tree `c9eb7a3...` проверены `entities/volonter/current`, `inbox`, `outbox`, `handoff`, адресные routes/receipts, KOO/SHT/ARH/KOD results и решения. Позднее recovery появились следующие отдельные ветки (версии ниже ограничены этим immutable HQ tree; статус не выводился только из новизны файла):

1. COOP stress-test уже опубликован: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-coownership-constitution-stress-test-v0_1.md`, blob `31dc139184ebe50fbfb02ca0928aa4bb0324e126`. Его successor — research rights/state-transition v0.1 → v0.2 → v0.3 → v0.4, соответственно blobs `e3e8ec3f22febb65eb24fd941c8fa6a02aafe77c`, `683351419054d15b31a13fcd2475a551a39bed8e`, `b1259d7c1f073ffd8b04329c62be04647a2aadff`, `8b26cc78081bc18765902a8931b4c159cfc7a1b2`. Независимый SHT review v0.4 criterion 3: `entities/shtabist/outbox/SHT__COOP-rights-transition-v0_4-criterion3-review__VOL.md`, blob `74ba251b04bce842eb4af14bcf1f22f6838200ad`, `BOUNDED_PASS_CRITERION_3`, critical findings 0; прежние v0.1–v0.3 review gaps заменены исправлениями только в пределах указанной проверки. Нет общего approved/production статуса.
2. VOL architecture handoff KOD: `entities/volonter/outbox/VOL__COOP-rights-transition-architecture-handoff__KOD.md`, blob `cebd7b6b16725a3c9891cd140140f0451a354f9c`; KOD bounded read-only fit-gap `entities/koder/outbox/KOD__COOP-rights-transition-fit-gap__VOL.md`, blob `26523086ad81e06ee4da5f1ea2906895c63d1369`, получен/ограниченно принят через `routes/receipts/KOD__COOP-rights-transition-fit-gap__VOL.receipt.md`. Technical identifiers пригодны как evidence refs, governance gaps сохраняются; implementation отсутствует.
3. Activation-lineage: нормализационный пилот `entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`, blob `a62ae4e16e95b85809dd4464c494da7cf4c67ea0`, получил `ACCEPTED_BOUNDED_RESEARCH_RESULT`; corrected v0.2 `VOL__activation-lineage-candidate-v02__KOO.md`, blob `87ca81187635afe3f9fb0014b86b88f686432a58`, и dataset v0.2 blob `b25e61a2317290d75078535d546a03ee457bb127` получили `CORRECTED_CANDIDATE_READY_FOR_SCHEMA_REVIEW_ACCEPTED` в KOO receipt. V0.2 supersedes исследовательскую v0.1 для schema-review; schema/validator/automation не внедрялись.
4. Hybrid interaction: research update `VOL__COOP-hybrid-interaction-research-update__KOO.md`, blob `4a295ef6c38eedb855deca387ee7364900e7e08d`, KOO accepted bounded research. P1+P3 pilot blob `74ebb9800cfe7e8bafeebf5844dbd3b3dcf6c082` accepted bounded. P2+P4 Russian operator edition blob `c5d06bb45034a316ebc2b4bd006ce41cb023fbf1` supersedes English edition for current use; KOO accepted bounded, P5 blocked without measured effect. P5 evidence scout blob `aa7d74bdb58e58e442f769fb14791e3da35888cc` accepted as `NO_ELIGIBLE_CLOSED_EPISODE`. Prospective low-burden measurement protocol `VOL__p5-prospective-measurement-protocol-r01__KOO.md`, blob `d2e072f264703debba93460e2f94c2193639fc72`, accepted in `routes/receipts/VOL__p5-prospective-measurement-protocol-r01__KOO.receipt.md` only as candidate for future observations. Эффект не измерен, P5 не доказан.
5. `VOL__participant-capability-testing-source__SHK.md`, blob `1a2133289e44fe3c6395b39eef8f991b3ca66f2c`, опубликован как working research/design input ШКОЛЕ, not approved norm. Experience Layer verification и KOO decision `ACCEPTED_BOUNDED_CANDIDATE_WITH_NORMALIZATION_DEBT` относятся к более ранней линии; strict v2 verification supersedes первый отчёт для final decision, active Project Source не возник.
6. Поздняя KOO task `entities/koordinator/outbox/KOO__work-mode-pilot-observation-r01__VOL.md`, blob `3a4afe781adf5d5bfc2e9662d11e330d79f042f0`, status `READY_FOR_PROFILE_WORK`; в HQ tree соответствующий VOL result не найден. Это возможный незавершённый вход, **не активируемый этим initiation**. Его текущесть, writer prerequisite и приоритет должны быть отдельно сверены после Writer Gate и новой exact task authority.

VOL handoff в HQ содержит только `.gitkeep`; новый verified self-snapshot позднего delta, установление нового VOL writer или конкурирующий writer artifact на проверенном дереве не обнаружены. Это отсутствие не является доказательством глобального отсутствия writer; нынешний writer-state нового экземпляра — `WRITER_REQUIRED_UNVERIFIED / NOT_ESTABLISHED`. Explicit failure-state старого чата и разрешение на initiation не передают writer-state.

Контекст истощённого чата `entities/koordinator/evidence/VOL__exhausted-chat-context-candidate__CONTEXT_ONLY.md`, blob `9dc84eedc0e4cc1256f4d1e72c28c300aa2b76e5`, прочитан в ограниченном объёме: `CHAT_CONTEXT_CANDIDATE / NOT_VOL_SELF_SNAPSHOT / NOT_CANONICAL_RECOVERY`; его вопросы и предложения не устанавливают identity, writer, task, acceptance или публикацию.

## Итог, предел и следующий разрешённый переход

External locator/composition/immutable version/checksums: PASS. Instance initiation: VERIFIED. Recovery freshness for direct task replay: STALE. Exact current profile task: UNKNOWN/NOT_EXECUTED. New current-writer: NOT_ESTABLISHED. Profile work/constitution stress-test/COOP production/WBN-WBNP accounting or monetary action/token or governance activation/system mutation/source mutation/external mutation/automation/memory-layering attempt 3: NONE.

Следующий отдельный переход — Writer Gate только по новому точному разрешению и свежей сверке competing-writer evidence. Этот файл — свидетельство initiation, не VOL authoritative self-snapshot и не решение Writer Gate. Если Writer Gate не пройдёт, возврат к KOO/ОПЕРАТОРУ с точным blocker; historical task не replay.
