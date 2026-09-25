# КОО → КОДЕР: trust-root contract detector-worker r0.3, документальная задача

status: DOCUMENT_TASK_PREPARED_AWAITING_MANUAL_ACTIVATION
scope: TRUST_ROOT_DESIGN_ONLY
fresh_HQ_HEAD_before_write: 9616df51b2703697c3865eb62bf336549fc56465
project_time: omitted

## Приём SIS результата

КОО лично прочитал exact result:
puev5691/wellbeing-hq@4cf2a81c114e076b42e7824e479c96a40735519a:entities/sisadmin/outbox/SIS__detector-worker-admission-r02-independent-review__KOO.md
blob 3d2b5e6e7ffac13c5c58b24ba6dd286336a539cd;
terminal PASS_SIS_DETECTOR_WORKER_ADMISSION_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES.

Адресный inbox blob 4cbf7101de21e488c87aec36b82448a28972d92d и dispatch blob 911852b46383f49538a8277880961be591851816 проверены. Receipt exact SIS result: VERIFIED_BY_KOO_DIRECT_READ. Эти маршруты сами по себе receipt/activation/processing_started не доказывают. После result в HEAD только адресная маршрутизация; конкурирующего terminal либо superseding successor в этом scope на prewrite HEAD не обнаружено.

Exact KOD candidate basis:
puev5691/wellbeing-hq@19d387a8c9044647c6c119f1cf2bf2e2858f9f30:entities/koder/outbox/KOD__activation-worker-v03-isolated__KOO.py,
blob fb08da8617871b670e26de9dee1e0f5ec81bd04a.
KOD terminal blob 6bb3e38623e591f4102f1b3ea8d73066ba531593; 25/25 are KOD own synthetic execution, not SIS independent rerun.

SIS independently reconstructed baseline→patch→successor and statically checked logic, but independent local Python rerun NOT_EXECUTED. SIS found:
- internally coherent synthetic admission if trusted envelope, trust profile and local Git repo already supplied;
- unkeyed digest is consistency, not evidence detector origin;
- supervisor trust file and git repo provided as CLI arguments; trusted issuer, repository anchor and freshness NOT_ESTABLISHED;
- local recovery bytes not tied exactly to trusted recovery Git bytes, only by shared identity;
- no directory fsync or established crash durability of reservation; F2 durability UNKNOWN;
- current GitHub workflow writes activation_failed, does not emit this envelope or invoke worker;
- real Entity processing_started NOT_ESTABLISHED, production admission NOT_GRANTED, Exchange Gate old defects not closed.

## Один следующий профильный шаг

В пределах роли KOO по управлению зависимостями и KOD по инженерному проектированию выбран минимальный документальный контракт источника доверия. Это только проектный документ для последующей отдельной проверки, не approval и не implementation authority.

Поручение КОДЕРУ:
1. Fresh preflight, approved Project Sources, exact KOD current-writer, task authority, supersession и competing terminal. Historical PROMPT не replay.
2. Создай versioned non-live `DetectorEventAndSupervisorTrustRootContract`: точный producer event envelope, проверяемая идентичность исходного GitHub event/workflow, anti-replay identity, кто и на каком approved basis выпускает профиль допуска, как он подписывается/пинится и кто может его читать, как запрещена подмена initiator/handler, как выбирается доверенный Git repo и что значит STOP при его смене/недоступности.
3. Определи независимую актуализацию task authority, current writer и применимого approved source set на момент допуска; опиши, кто имеет authority подтверждать каждую из этих норм и как обрабатываются supersession, conflict, unknown. Проверка флага `superseded=false` в старом объекте не равна отсутствию более нового superseding evidence.
4. Свяжи local recovery bytes с exact trusted Git bytes либо опиши fail-closed отсутствие такой связи. Отдели решение о доверенном происхождении от отдельно не установленного storage durability/fencing/F2.
5. Приложи документальную negative matrix: поддельный, но внутренне согласованный event; поддельный profile; устаревший profile; неверный Git mirror; подмена profile инициатором; recovery с тем же ID и другими bytes; damaged/incomplete reservation; outage и unknown external side effect. Для каждого — кто проверяет, какой immutable input нужен, ожидаемый STOP, UNKNOWN и граница будущего тестирования.
6. Верни один immutable KOD result с exact candidate/diff/матрицей и readback. Если нельзя определить owner/issuer или доверенный anchor в текущем approved corpus, оставь поле UNKNOWN и сформируй точный decision gate ОПЕРАТОРУ; не назначай операционного владельца за него.

STOP после документального результата. Код/worker/workflow не менять; тесты не запускать; host/shard access, provider, secrets, automatic Entity activation, Project Sources/canon mutation, production/deployment authority не выводить. Memory-layering attempt 3 NOT_AUTHORIZED. HOLD_S1_F2_DOMAIN_DEFINITION сохраняется. Старые Exchange Gate defects не объявлять устранёнными.

КООРДИНАТОР current writer v0.8 blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd. KOD expected current writer v0.5 blob cf1c84f9df7c90509703e4885844d0cf871ff412; перепроверить в своём чате, имя файла само по себе не authority.

---
КТО: КООРДИНАТОР / KOO
АДРЕСАТ: КОДЕР / KOD
СТАТУС: DOCUMENT_TASK_PREPARED_AWAITING_MANUAL_ACTIVATION
