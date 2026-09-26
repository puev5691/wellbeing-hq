# КОДЕР → КООРДИНАТОР: fixed-IP router implementation package r0.1

terminal: PASS_KOD_FIXED_IP_ROUTER_IMPLEMENTATION_PACKAGE_R01_READY_FOR_SIS_REVIEW
scope: IMPLEMENTATION_READY_PACKAGE_ONLY_NO_DEPLOYMENT
project_time: omitted

## Человеческий результат

Подготовлен и опубликован проверяемый пакет маршрутизатора для административной HTTPS-проверки по фиксированным IP. Код сохраняет TLS SNI, HTTP Host и проверку сертификата для `chatgpt.com`, последовательно пробует второй допущенный IP на том же узле, затем переходит по порядку burzh → mazhor → erefia. HTTP 403/429/5xx остаются ответами приложения и не запускают сетевое переключение. Это кандидат для независимой проверки СИСАДМИНОМ; ни на один проектный узел ничего не установлено.

## Resume-First и authority

Fresh HQ preflight main `67d291cf927d07ea6be6ae8f5df363c8ced7faa9`, tree `7c2ef74bc92ccd2c88639ad7021d508df3923dcb`, recursive tree truncated=false. Current KOD v0.5 writer `entities/koder/current/KOD__replacement-current-writer-v05.md`, blob `cf1c84f9df7c90509703e4885844d0cf871ff412`; v0.4 handoff freeze remains. Writer Gate `PASS_KOD_REPLACEMENT_WRITER_GATE_V05`. No newer KOD writer, recovery/handoff supersession, exact task successor or competing fixed-IP implementation-package result found. Six attached approved Project Sources loaded under source-loading policy.

Exact task `puev5691/wellbeing-hq@1f784036f56942026454bda58dcac4705be48a63:entities/koordinator/outbox/KOO__fixed-ip-router-implementation-package-r01__KOD.md`, blob `262ed1e37d505a2ad34fd2ae132891e59a746119`. Direct OPERATOR authority “Разрешаю подготовить implementation package fixed-IP router без установки на серверы” preserved in `@a0ecf4fda0bd4223d1ffdfb8c62fdb9b0a0bdf21:entities/sisadmin/outbox/SIS__fixed-ip-router-implementation-package-authority-handoff-r01__KOO.md`, blob `7e3a14eff25356a0af190a840e14c15cb7afd162`. Design `@2d61ac65616b7b30e3a11b6c682ec027094e11dd:entities/sisadmin/outbox/SIS__fixed-ip-administration-routing-design-r01__KOO.md`, blob `399afd89134f877e61d68d0bb2047efd168067dc`. Measurement `@4f07ba64212a78d7e18d44089292b5838475649e:entities/sisadmin/outbox/SIS__three-node-chatgpt-https-latency-by-ip-r01__KOO.md`, blob `a9285466f6541d347309902d21537d2e3c77a0f4`. Exact task/design/measurement/authority blobs independently read and matched.

## Immutable package

Locator: `puev5691/wellbeing-hq@c27c6882743047b576281b918c2ba1fa2741f0f8:entities/koder/outbox/fixed-ip-router-r01`.

Package Git tree: `fc1bb2751cc5d662037a037fdecf3ece69f07adb`; publication commit: `c27c6882743047b576281b918c2ba1fa2741f0f8`. Root `MANIFEST.md` blob `83a45b65dfe81a2e8f666105dc40bfffaff31840`; `SHA256SUMS.txt` blob `2538b84c80f4b27163ea73622d660a56388ee937`. SHA-256 actual bytes of all 11 other members recorded there; `sha256sum -c SHA256SUMS.txt` passed 11/11. Git immutable readback of all 12 exact file bytes and blobs passed 12/12, recursive tree not truncated. The checksum file excludes itself to avoid a self-reference cycle.

| Member | Git blob |
| --- | --- |
| `router.py` | `1848351323ec489a17e9cd8e5e15c99b83f2f913` |
| `node_probe.py` | `359715ca411abb5f7a965da87200d5f926c80142` |
| `offline_cli.py` | `0ad60ef2c2e1ca88232fa190234cf315d6cab611` |
| `profile.schema.json` | `06622ffe707030fd958fe05dd88a46894436be6f` |
| `profile.current.json` | `4890b739876681b9eaf3859f7a211c7269d8f5b5` |
| `fixtures/profile.synthetic-admitted.json` | `361fc246562e8e613213528f0dde8657fff04a51` |
| `fixtures/admission.synthetic.json` | `cc29ce85d39869df0d39299ba1bba1cdd25e604c` |
| `fixtures/observations.synthetic.json` | `76f01e3c914e481416d3ecbe62761ed18a21f3c5` |
| `test_router.py` | `381d27da11ffb1a3e5d223d2a74c613982f90c59` |
| `README.md` | `aae86bad29770aee2f1364a2008f27d1d512c9a4` |

## Проверка

`python -m unittest -v test_router.py`: 17 тестов, 17 PASS, 0 FAIL/ERROR. Только synthetic/mocked: healthy IP; первый IP отказал/второй успешен; оба IP узла отказали; основной узел недоступен; переход на второй и третий узлы; остановка на неверном сертификате; HTTP 403/429/500/503 как application response; stale/unadmitted successor; exhaustion; ручной выбор начального узла; missing observation; identity/digest mismatch; отсутствие DNS при передаче hostname; SNI/Host/certificate-параметры mock-probe; закрытый audit. Два offline CLI прогона прошли: обычный план выбрал `burzh/172.64.155.209` после synthetic отказа первого IP, сохранил HTTP 403; `--manual-node mazhor` выбрал `mazhor/104.18.32.47`. Ни один probe не выполнялся по сети.

## Ограничения и следующий gate

Текущий `profile.current.json` имеет `DOCUMENTED_CURRENT_MEASURED_SET`; код не допускает его как operational `ADMITTED`. Synthetic admission fixture не является полномочием. Planner получает наблюдения извне и сам не проверяет доверенную подпись/источник текущего допуска, не подтверждает фактическую личность трёх узлов и не организует защищённый удалённый запуск. Node-local HTTPS probe включён как кандидат, но не выполнялся live. IP могут устареть; изменение списка требует отдельного successor profile и admission. Предполагаемые rollback/pre-state описаны в README, фактический pre-state узлов не собирался.

СИСАДМИН должен независимо проверить exact пакет, модель допуска/currentness, node adapter/control path, TLS/аудит и rollback boundary. Любой host test, deployment или automatic failover требует отдельного решения ОПЕРАТОРА. CHECKPOINT_DURABLE не установлен, resume authority не предоставлен, memory-layering attempt 3 NOT_AUTHORIZED. Provider/API calls 0; host mutations 0; credentials 0; DNS changes 0; shard WRITE 0; automation/source/canon mutation 0; historical PROMPT replay 0.

Journal candidate для существующего редакционного отбора: «КОДЕР подготовил воспроизводимый маршрутизатор для фиксированных IP, не превращая измеренный адрес в вечную истину. Синтетические проверки показали переход между адресами и узлами при сохранении имени HTTPS; действующее подключение к серверам и принятие профиля остаются отдельными решениями». KOO может объединить этот сигнал с другими для RED journal-sweep; автоматической записи в журнал нет.

Next gate: independent SIS package review, не deployment.
---
КТО: KOD / КОДЕР
КОМУ: KOO / КООРДИНАТОР
