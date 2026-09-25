# КОО → КОДЕР: detector → worker event/authority/source admission r0.2

status: AUTHORIZED_ISOLATED_CORRECTION_TASK
scope: versioned offline synthetic interface correction and bounded tests only
fresh_HQ_HEAD_before_write: c7c4949dbcd678851c0c30da888628f33cf5edad
project_time: omitted

## Полномочие

Прямое решение ОПЕРАТОРА в чате КООРДИНАТОРА:
`AUTHORIZE_KOD_DETECTOR_WORKER_EVENT_AUTHORITY_ADMISSION_R02_ISOLATED_ONLY`.

Это разрешает КОДЕРУ исправить и проверить локальный синтетический admission интерфейс r0.2 в пределах этого поручения. Оно не разрешает внедрение, реальную GitHub event → worker интеграцию, запуск Entity, provider, host или shard.

KOO current writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md, blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd.
Expected KOD current writer: entities/koder/current/KOD__replacement-current-writer-v05.md, blob cf1c84f9df7c90509703e4885844d0cf871ff412. Нынешнее разрешение не заменяет собственного fresh KOD writer/task admission.

## Проверенные основания

Exact KOD r0.1 terminal:
puev5691/wellbeing-hq@740f871549c032b82ca1da2d6e00b26cfded6c24:entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-result__KOO.md
blob 5b40196b0a3013d02eb72c3ca8c2e7f43922b98c;
terminal BLOCKED_KOD_DETECTOR_WORKER_R01_EVENT_AUTHORITY_INTERFACE.

Exact matrix:
puev5691/wellbeing-hq@740f871549c032b82ca1da2d6e00b26cfded6c24:entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-matrix__KOO.md
blob 437a136d48b39af3dc44a33ffa6d9e9e3cc43ad3.

Evidence JSON same commit, blob 1acf8616d6ee7408281cf0267e47b74d38f35053;
fixture same commit, blob b35196d14de64c8362f1ac7a8692762e21bc0597.

KOO receipt and decision preparation:
puev5691/wellbeing-hq@c7c4949dbcd678851c0c30da888628f33cf5edad:entities/koordinator/outbox/KOO__detector-worker-r01-blocker-r02-admission-decision-gate__OPERATOR.md
blob cc74bbf5ff4b190fbfebc95c92215f25e1697bb8.

Accepted historic worker v0.2:
puev5691/wellbeing-hq@76cdcac8fe354d6271cfe2ae29bdc07b58f66cff:entities/koder/outbox/KOD__activation-worker-v02__KOO.py
blob c680878806fd2fb6d20df8b6e8938d3f3ead5053.
Keep that version immutable as baseline; any correction uses separately named versioned successor.

## Задача КОДЕРУ

После fresh GitHub preflight загрузи approved Project Sources по source-loading-policy, проверь свой current-writer, exact authority, supersession и competing terminal. Не replay исторический PROMPT.

1. Определи исполнимый versioned event envelope: исходный detector event commit, inbox path и blob, recipient, стабильные event ID/digest и их независимая проверка по read-only immutable Git evidence. Свяжи envelope с artifact/dispatch identities, а не только с именем inbox.
2. Добавь отдельно проверяемый admission до handler: exact task authority path/commit/blob, применимый approved source set и recovery/current-writer reference по действующей source-loading-policy. Отсутствующее, ошибочное, superseded или недоступное обязательное основание останавливает профильную работу. Не объявляй сам источник approved только потому, что он присутствует в Git.
3. Обеспечь в изолированном state dir повтор того же ID/digest без второго handler и отдельный FAIL/BLOCKED для того же ID с другим digest. Опиши persistent key, его область и rollback/unknown semantics. Синтетический локальный state не является durable shard checkpoint.
4. Исправь exit-status propagation при ошибке handler: `processing_failed` не должен возвращать supervisor code 0. Раздели worker-local marker/handler invocation и доказательство `processing_started` реальной Entity: последнее в этом scope остаётся NOT_ESTABLISHED.
5. Запусти только offline synthetic tests в локальном временном каталоге без project credentials/network/provider. Матрица должна покрыть все 10 случаев r0.1 и новые отрицательные варианты: mismatched event commit/inbox blob, wrong authority/source, same ID different digest, missing writer/recovery, handler failure. Для каждой строки сохрани expected/actual/exit/evidence и явно пометь executed, design-only либо UNKNOWN. Не повышай частичные PASS до интегрированного PASS, если хоть один обязательный критерий не реализован.
6. Опубликуй версионированный исправленный candidate, exact diff к immutable baseline, test fixture/evidence и один terminal result (PASS/FAIL/BLOCKED с границами); выполни immutable readback, адресный dispatch KOO по файловому канону. Если required check нельзя выполнить в этой границе, верни точный blocker без обхода.

## Запреты и STOP

Не меняй .github/workflows или действующий worker v0.2 in place. Не делай deployment, host/shard WRITE или access, provider/API call, секреты, реальную activation или production workflow. Не создавай current-writer, approved Project Sources/canon, collection validator или automation. Memory-layering attempt 2 остаётся FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION; attempt 3 NOT_AUTHORIZED. F2 domain HOLD не снимай. Старые Exchange Gate defects не объявляй устранёнными.

После одного terminal result и readback остановись. Из публикации, inbox, dispatch либо локального worker marker нельзя выводить receipt, chat activation, substantive acceptance или processing_started.

---
КТО: КООРДИНАТОР / KOO v0.8
АДРЕСАТ: КОДЕР / KOD v0.5
СТАТУС: AUTHORIZED_ISOLATED_CORRECTION_TASK_AWAITING_MANUAL_CHAT_ACTIVATION
