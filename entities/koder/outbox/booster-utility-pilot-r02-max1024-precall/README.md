# Utility pilot r0.2 MAX1024: non-live preparation

Подготовлен отдельный exact candidate для AUTHORIZE_BOOSTER_UTILITY_PILOT_R02_ONE_SHOT_MAX1024 по прямому распоряжению ОПЕРАТОРА. Provider calls=0, credential value reads=0, LIVE execution=0, host mutation=0. Кандидат ещё не установлен и не является live admission.

Единственное изменение experimental request: max_output_tokens 64 → 1024. Purpose сохранён дословно, даже несмотря на r01 в task_id. Frozen D0_RUNS_MAX3_R01, payload, source hash, baseline binding, writer/task refs, model gpt-5.6-luna, privacy, tools=[], timeout30, max_response_bytes16384 сохранены. Reasoning effort не отправляется. Admission отличается от r01 только authority_id, max_output_tokens и request_sha256. Остальные identities производные.

## Состав и воспроизведение

request.json; admission.candidate.json; native-body.json; identities.json; comparison.json — детерминированные результаты `python3 -B prepare_candidate.py` (prepare only, без execute/ledger/resolver).
`python3 -B run_tests.py` — guarded offline 7-test verification, только synthetic transport и isolated temporary test ledger. Реальная r02 authority лишь подготавливается; fake execution использует OFFLINE_TEST и TEST_ONLY_UTILITY_BRIDGE_R01, не настоящий r01/r02 admission. TEST-RESULTS фиксирует real_provider_calls=0 и forbidden_attempts=0.
`sha256sum -c SHA256SUMS.txt` — проверка состава.

basis/request-r01.json и admission-r01.json — семантически точные пересериализованные read-only копии исторической конфигурации. Оригиналы не изменялись. Их original file SHA256 соответственно 13ec391f25ab8a5e524e933c61f72dcc30248066daa1babecc22ba8923d8382a и 801059e8e0313dcf2b379d9550b7b5a780cfff26699c41a6e43766704e447568.
Basis task.json и baseline-measurements.json — exact bytes из puev5691/wellbeing-hq@d074ffd92a2794af954e27a8a809a3c6335ce14a:entities/koder/outbox/booster-utility-pilot-r01-baseline. Baseline solution/tests/rubric не перезапускались и не переписывались. Baseline 8/8, elapsed40.071600699, active unknown сохраняются как historical evidence.

## Installed dependency

PASS_SIS_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_HOST_READINESS:
6edc7449706a3884a92aa3e6522ae05fdce32f5f:entities/sisadmin/outbox/SIS__booster-failure-diagnostic-metadata-r01-host-readiness__KOO.md
blob e6d07c015e34dcab23e9f904569eeb70f70b0122.
Installed source: 84988d0e7f881e4c5c01006bd287f7d7469a006c:entities/koder/outbox/booster-failure-diagnostic-metadata-r01.
Все 33 source blobs проверены перед подготовкой. Все deps скопированы byte-identical. Только bridge.py candidate имеет 3 изменения строк: authority literal и два occurrence exact64→1024. Failure metadata, normalizer, live worker/ledger неизменны. Вложенные utility_adapter manifest/test files — provenance прежнего adapter, не новый test report.

Fresh read-only host hashes и canonical utility ledger rows записаны в basis/host-readonly.json. R01 reservation consumed; новый r02 reservation отсутствует. Проверка ограничена действующим canonical STATE=/var/lib/wellbeing/booster-utility-pilot-r01. LIVE_GATE absent. Это evidence момента preflight, не вечная гарантия; SIS обязан повторить сверку перед любым будущим admission. Дублировать/обнулять/переносить canonical ledgers для обхода нельзя.

## Identity and freshness contract

Domain wb.booster.utility_bridge.v1 сохранён. Hashes вычисляются прежними canonical algorithms. native_body_sha256 — hash UTF-8 compact sorted native JSON без LF; files на диске имеют LF, их file hashes отдельно в MANIFEST.

admission.candidate.json сохраняет logical verification now_tick=1, valid_until_tick=2. Эти ticks не являются текущим временем или долговременной live authority. Candidate не содержит LIVE_GATE или host installation. SIS должен независимо проверить exact refs, authority и отсутствие consumption; перед реальной отправкой требуется fresh admission по существующему lifecycle. Если меняется validity/admission metadata, меняются authority/plan/attempt hashes и требуется новый exact readback; опубликованные expected identities нельзя выдавать за прежние после такого изменения.

Текущий установленный bridge/host_caller всё ещё привязан к r01/64. Для будущего r02 исполнения требуется отдельно проверенная установка только подготовленного candidate и соответствующая exact caller/config binding с новой authority, сохранением canonical ledger и installed failure metadata. Не следует запускать старый caller с новым request: это identity/bound mismatch. Здесь host caller/systemd/config не менялись. SIS non-live verify обязателен до установки/вызова.

## Boundaries / remaining limitations

Metadata включена в future path после shape v2 strict readback до normalizer, как в установленном successor. Reasoning-only synthetic тест сохраняет metadata и не создаёт review. Project/production acceptance NOT_GRANTED; automatic application=false. Изменение bound не доказывает token-budget causality и не гарантирует candidate: byte limit16384 и timeout30 намеренно сохранены и также могут остановить следующий эксперимент. Никаких retries/fallback/tools, второй experimental parameter или новых усилий reasoning не добавлено.

После этого readiness остановиться и передать exact package КОО и СИС. Это не результат второго эксперимента и не утверждение о live readiness на хосте.
