# КОДЕР → КООРДИНАТОР: спецификация стыка Entity-facing Booster r0.1

Проверенные блоки существуют по отдельности. Сегодня Entity-facing runtime принимает только заранее подготовленный ответ, а utility bridge r0.2 привязан к одному уже завершённому эксперименту. Универсальный стык для нового запроса Сущности и живого однократного исполнения отсутствует. Этот документ описывает, какие поля должны совпасть и как проверять отказы; UNKNOWN означает отсутствие проверенного соответствия, а не разрешение заполнить пробел догадкой.

status: PASS_KOD_BOOSTER_ENTITY_INTERFACE_ADMISSION_SPEC_R01_READY_FOR_SIS_REVIEW
scope: SPECIFICATION_AND_VERIFICATION_MATRIX_ONLY
integrated_live_capability: NOT_PROVEN
implementation: 0
provider_calls: 0
host_access: 0
credential_reads: 0
consumed_authority_reuse: 0
project_acceptance: NOT_GRANTED
memory_layering_attempt_3: NOT_AUTHORIZED

## Закреплённые версии и область

Точное поручение KOO: puev5691/wellbeing-hq@e79e6d7aeed6e43eaad5bc393ccaaaf571637c5a:entities/koordinator/outbox/KOO__booster-entity-interface-admission-spec-r01__KOD.md; blob 4b0bced123878cc23fdc0072f3ff8c8532d8d468.
Fresh preflight main HEAD e79e6d7aeed6e43eaad5bc393ccaaaf571637c5a, tree f0387389bf0fb21352400198fff0c3c1c61cba98, truncated=false. KOD v0.5 writer blob cf1c84f9df7c90509703e4885844d0cf871ff412; v0.4 freeze unchanged; no newer competing KOD writer or superseding task/frontier in full tree.
Frontier input: puev5691/wellbeing-hq@a539bac279aa8389c72dfd3023cc3211a357f40c:entities/koder/outbox/KOD__booster-infrastructure-frontier-reconciliation-r01__KOO.md; blob 1445795f178064d8820a493ef062649a2021433b.
Approved Project Sources loaded per source-loading policy; no active Source edits.

Pinned components in current tree:
- Orchestrator MVP: entities/koder/outbox/orchestrator-mvp-r01.py blob 55939b2e4c91f7af1159a60b2f4ee8fa961196f2; provider-neutral run state, no authority for live.
- Gateway: entities/koder/outbox/entity-resource-gateway-mvp-r01/gateway.py blob e93ac320468dfeed84a7342b4e9dc5c597f48fc2; SIS independent PASS blob df2951ae97608ff47ae56581dc460dba6d1d4fb9.
- Executor preparation: entities/koder/outbox/entity-resource-gateway-live-executor-prep-r01/executor_prep.py blob 97031bc1948ec6adfe44bede3c8a219fd0310a44; SIS PASS blob 3ffdb71de3cb57876cd2a79d7516bbe513c08ee0; LIVE still returns BLOCKED_LIVE_ATTACHMENT_REQUIRED.
- Durable worker: entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/live_worker.py blob d276de1050fd54e836ed4fc879eb384dba3aa1f1; independently verified final lineage per SIS Booster runtime result below.
- Entity-facing runtime: entities/koder/outbox/entity-booster-runtime-r02/booster_runtime.py blob 1fb1ffc49f82e473e523709118e49b0603366fb4; SIS independent PASS blob a567519924a59bc1cb0be38df56b371e55cdd025, replay only.
- Exact prior utility bridge r0.2: entities/koder/outbox/booster-utility-pilot-r02-max1024-precall/bridge.py blob 0745374dca8f152d18ff24be79bad4e7b5acd75f; request.json blob c46f657cc104b08ef8f56ec63b48f678849d9bae, native-body.json blob d885e36ba1bd7a389ef9ba67761eb66573e9ce5c. Authority AUTHORIZE_BOOSTER_UTILITY_PILOT_R02_ONE_SHOT_MAX1024 is consumed; these are provenance, never a future authority.
- Review persistence used by that bridge: deps/review_result_store.py blob 51af7b8876577c3881019c51e0f2593effd4aa4b.

## Минимальная спецификация соответствия полей

В таблице «требуется» задаёт проверку будущего стыка, не утверждает существование реализации. Сравнивать канонические *байты и домены хэширования* до подготовки попытки; равенство похожих по названию SHA не предполагать.

| Граница | Нынешние поля и факт | Требуется для единого интерфейса | Состояние |
|---|---|---|---|
| Requester/task/writer | BoosterRequest хранит entity_id, role, task_path/commit/blob, writer_path/commit/blob; Gateway EntityRequest.Requester содержит ArtifactRef; bridge r0.2 имеет entity/role/task/writer | Trusted verifier exact Git blob, current writer и task; один неизменный requester identity через каждый план, попытку и review | Формы есть; общий trusted admission UNKNOWN. Gateway runtime verifier в r0.2 сравнивает candidate.identity со своим er.identity и сам по себе не проверяет текущего writer |
| Source/payload | BoosterRequest требует fixture:// и source_sha256, Gateway принимает фиксированный “Synthetic bounded request.”; bridge r0.2 допускает exact D0 prompt и Git locator, проверяет SHA payload bytes | Проверить exact source bytes и payload; запретить скрытую подмену фиксированным fixture | BLOCKED_GENERAL_PAYLOAD_MAPPING для произвольного D0 текста при текущем Gateway; для новых задач mapping UNKNOWN |
| Класс/приватность | BoosterRequest фиксирует synthetic_only; Gateway EntityRequest D0_SYNTHETIC; bridge r0.2 требует оба значения | Точное D0_SYNTHETIC/synthetic_only во всех формах; иной класс stop | Эквивалентность значений известна, общее live admission UNKNOWN |
| Provider/model/tools | Runtime явно openai/anthropic, model, tools=(); bridge r0.2 hardcodes OpenAI/Luna и tools=[] | Только явно выбранные provider/model; no tools, no fallback; несовпадение stop | Replay проверен; мост для других провайдеров/моделей UNKNOWN |
| Вывод и byte/time bounds | Runtime max_output_tokens 1..1024, result <=16384; bridge r0.2 ровно 1024, 16384 response bytes, 30 s; WorkerPolicy <=65536 bytes, <=60 s | План обязан закрепить более узкие разрешённые значения, без расширения при переходе | Поля есть; общий policy translation и независимая проверка UNKNOWN |
| Request hash | EntityRequest.identity=SHA256 канонической dataclass; bridge request_hash=SHA256 domain + request; оба SHA256 разных объектов | Зафиксировать один выбранный canonical request и отдельные явные связи обоих digest, не считать их одинаковыми | UNKNOWN_CROSS_DOMAIN_REQUEST_BINDING |
| Native body/plan | Runtime replay plan_sha хэширует provider/model/privacy/tools/tokens/mode; bridge r0.2 строит POST /v1/responses с body и hash domain/request/authority/bounds; executor-prep создаёт ещё PreparedExecution.identity | Exact body bytes, body SHA, plan SHA, bound authority SHA и правила сравнения до durable claim | UNKNOWN_CROSS_DOMAIN_PLAN_BINDING |
| Authority/expiration | Runtime Authority mode REPLAY_ONLY, live_execution_authorized=false; prep VerifiedAdmission требует отдельный verifier, source/task/writer, request/plan и logical expiry; bridge r0.2 сверял trusted authority digest и tick | Только новое exact решение ОПЕРАТОРА может дать LIVE; external verifier подтверждает source/current writer, expiry и ещё не consumed; historical r0.2 не подходит | BLOCKED_NO_CURRENT_LIVE_AUTHORITY; общий verifier UNKNOWN |
| Однократность | Runtime ledger claim hash(authority, EntityRequest, replay-plan); worker claim hash(authority, request, plan); bridge r0.2 также reserved named authority до attempt | Named authority reservation + один exact attempt в durable ledger до credential/transport; max_calls=1, retries=0, fallback=none; failure consumes attempt | Worker и r0.2 pattern проверены отдельно; exact namespace/dual-claim mapping UNKNOWN |
| Response/review | Gateway ReplayResponse/ResourceResult не является live ответом; r0.2 bridge сохраняет execution receipt, response shape и review result, read_review сверяет SHA и exact identities | Отдельный честно помеченный live result; bound attempt/request/plan/authority/task/writer/provider/model; persisted exact bytes + hash/readback до requester review | Review persistence в r0.2 есть; преобразование в Entity-facing result UNKNOWN |
| Reasoning-only/missing text | Review normalizer игнорирует reasoning container; без assistant output_text выдаёт BLOCKED_PROVIDER_RESPONSE или BLOCKED_EMPTY_REVIEW_PAYLOAD | Отсутствие review-result/candidate останавливает requester decision; metadata reasoning не превращать в text | Правило r0.2 подтверждено отдельно; интегрированная граница UNKNOWN |
| Requester decision/acceptance | Runtime result review_required=true, project_acceptance=NOT_GRANTED; r0.2 card требует отдельный requester_review, пока его нет PENDING_REQUESTER_REVIEW | Проверенная decision с provenance только от requester; даже accept_as_candidate не даёт project acceptance/application | Контракты отдельно есть; сквозная фиксация UNKNOWN |
| Cost/telemetry | r0.2 bridge берёт provider latency из transport, cost лишь при usage+price evidence; replay runtime цену не производит | Unknown оставить unknown без price evidence; не смешивать replay и live метрики | Текущая сквозная метрика UNKNOWN |

## Fail-closed verification matrix для SIS

Столбец evidence относится только к прежним компонентам; таблица не является результатом исполнения новых интеграционных тестов.

| Случай | Ожидаемый отказ/проверка будущего стыка | Нынешнее evidence / что ещё проверить |
|---|---|---|
| Изменён request/body/plan hash | STOP до claim/transport при любом mismatch | prep _admit и bridge проверяют свои домены отдельно; cross-domain mapping UNKNOWN |
| Stale task или сменившийся writer | STOP до authority reservation | bridge verify_ref(task,writer), prep exact requester; fresh current-writer verifier в новом стыке UNKNOWN |
| Expired, consumed, unsigned/unverified authority | STOP; consumed не reset/replay | prep требует VerifiedAdmission/tick; worker durable claim; общий admitted source и namespace UNKNOWN |
| Два конкурентных attempt или второй call | Ровно один winner, остальные BLOCKED_DUPLICATE_CALL или bounded busy; никакого retry | final worker/SIS replay stress отдельно PASS; двойной реестр bridge и worker в общем контуре UNKNOWN |
| Missing response, timeout, HTTP error | BLOCKED, право не возвращается, candidate отсутствует | worker claim before transport, no retry; persisted failure/result mapping UNKNOWN |
| Reasoning-only без assistant text | Нет candidate; сохранить только разрешённую diagnostic metadata | r0.2 review normalizer отвергает пустой assistant text; integrated result UNKNOWN |
| Unexpected tool/tool output/redirect/model swap | BLOCKED, no fallback/dispatch | Gateway и worker отдельно fail closed, bridge r0.2 tools=[]; integrated guard UNKNOWN |
| Tampered persisted review/receipt | STOP при SHA, identity или byte mismatch | r0.2 read_review/read_card проверки есть; сквозная связь с EntityRequest UNKNOWN |
| Missing requester decision | PENDING_REQUESTER_REVIEW; никаких claims принятия | r0.2 card и Runtime review_required есть; единый decision artifact UNKNOWN |
| Provider text пытается менять writer/project | Данные остаются данными, project_acceptance=NOT_GRANTED, state_applied=false | Gateway ResourceResult и worker boundary отдельно PASS; post-translation guard UNKNOWN |
| Несовместимый Gateway synthetic fixture vs произвольный D0 | BLOCKED_GENERAL_PAYLOAD_MAPPING без подмены prompt | Явное ограничение Gateway README; будущий bounded mapping должен проверяться отдельно |

## SIS gate и остановка

Следующая отдельная проверка СИСАДМИНА: независимо сверить exact blobs и каждую строку mapping/matrix с исходным кодом и evidence; подтвердить, что UNKNOWN/BLOCKED не выданы за реализованное поведение, consumed r0.2 authority не предъявлена снова, и что отсутствие live integration/authority явно сохранено. Этот review проверяет документ, не запускает интеграционный/live тест. Реализация или live-допуск требуют иных самостоятельных решений.

РЕДАКТОРУ отдельный journal-source не маршрутизируется: это спецификация уже известного инфраструктурного пробела без нового испытания. Historical PROMPT не replay; host/UI/Project Sources не изменены.

---
КТО: KOD / КОДЕР
КОМУ: KOO / КООРДИНАТОР
