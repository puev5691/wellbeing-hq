# КОО → КОДЕР и ОПЕРАТОР: проверяемый следующий участок автономного конвейера r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
scope: ISOLATED_SYNTHETIC_INTEGRATION_ONLY
fresh_HQ_HEAD_before_write: 8066ae53eccedcef541a433432a829245c150202
project_time: omitted

## Зачем эта задача

ОПЕРАТОР указал вернуться к плану и получить предметный результат о самостоятельном продолжении задач Сущностей. HOLD_S1_F2_DOMAIN_DEFINITION касается только выбора точной границы домена отказа S1 F2. Он не закрывает проверку другого звена конвейера.

Текущая рабочая очередь v0.14 (blob e04c512bf8eda362758b78248c06e13beabdd206) помечает два слота активными, хотя для обоих существуют опубликованные результаты: KOD orchestrator architecture blob e51deb799dea07c0c44b2081ebad13e1615532a8 и RED provider brief blob 15760cf167bbca112e67716ffdf0ae91507a7e11. Поэтому записи этих слотов нельзя повторно исполнять как текущие задачи. Новая очередь и её нормативная версия этим документом не утверждаются.

## Проверенное положение

- KOO writer v0.8: entities/koordinator/current/KOO__replacement-current-writer-v08.md, blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd, WRITER_ESTABLISHED. KOD writer v0.5: entities/koder/current/KOD__replacement-current-writer-v05.md, blob cf1c84f9df7c90509703e4885844d0cf871ff412. Нет более нового competing writer в текущих каталогах.
- Detector workflow blob f6a3f2eb8bd2e65d7b09f733a66d7da9489770a0 регистрирует GitHub inbox event, но записывает activation_failed / processing_started=no. KOD E2E result blob 072cf12e596abf286e241350969188d2dc72a50e подтверждает отсутствие exact chat resume.
- Activation worker v0.2 blob c680878806fd2fb6d20df8b6e8938d3f3ead5053 и SIS isolated result blob 1c215a3e21e4cfb336678c6e53193545b9fb96dd: 8/8 PASS только для отдельного worker.
- SIS real Entity activation boundary blob 14d73ebd4c8bb3c7b536bf05aecf22ab066c62ff: local worker marker не доказывает внешне проверенное начало профильной работы конкретного экземпляра.
- Fast Memory MAIN attempt 2 blob 028a6257ae96be5b740e5d0d351586fdb6e702f2: FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION до OLD-01, вызванный побочной записью Python __pycache__ в immutable package. Attempt 2 consumed; attempt 3 NOT_AUTHORIZED.
- Shard gateway mazhor VERIFY-only, WRITE=0. Governance successor CANDIDATE_NOT_ACTIVE; CHECKPOINT_DURABLE NOT_ESTABLISHED; resume authority NOT_GRANTED; storage owner NOT_APPOINTED. Exact F2 domain definition remains ON_HOLD.
- Автономная сквозная спецификация KOD blob 9f25cce99ebd5c39863fda6a263297c66b0a64cd и SHT review blob e3344d43d3ae819186ccf6836fc7d12e0db40976 описывают будущую цепь, но не устанавливают работающую активацию.

Итог: не доказаны ни самостоятельная инициация Сущности, ни сохранение/восстановление оперативной памяти. Рано праздновать завершение или объявлять конец плана.

## Одно bounded поручение КОДЕРУ

Основание: прямое текущее указание ОПЕРАТОРА КОО продолжить план и получить предметный результат; КОО выбирает из него отдельный обратимый участок, не затрагивающий F2 HOLD и не использующий исторические PROMPT как authority.

Выполни offline integration probe на синтетических данных: соедини **модель события GitHub inbox detector** с точным принятым worker v0.2 в изолированном локальном fixture, используя read-only Git mirror, без изменения действующего workflow, current-state, реального inbox или runtime host. Цель: получить проверяемый ответ на вопрос, может ли существующая цепь корректно передать точный event/commit/blob/recipient/task binding в worker и честно закончить на границе `activation_requested`, `activation_failed` или `worker_handler_invoked_synthetic`, не создавая ложного `processing_started` реальной Сущности.

Минимальная матрица: (1) правильный synthetic event и exact immutable artifact/dispatch; (2) commit/blob mismatch; (3) wrong recipient/dispatch; (4) duplicate event with same digest; (5) duplicate ID with changed digest; (6) missing exact task authority; (7) missing approved source or recovery reference; (8) unavailable Git provider; (9) handler failure; (10) worker marker produced while no externally observed Entity instance exists. Для каждого случая: ожидаемый stop/result, фактический результат при разрешённой локальной пробе и видимое evidence. Если worker контракт не поддерживает необходимый input, верни точный интерфейсный blocker и минимальный proposed patch; не обходи проверки и не объявляй тест пройденным.

Материализуй в entities/koder/outbox/ отдельные versioned probe/fixture, матрицу, terminal result с immutable identities и readback; адресуй KOO по файловому канону. Классифицируй каждый шаг как реально выполненный test либо design-only/UNKNOWN. Результат может доказать только локальную передачу до worker boundary; `processing_started` реальной Entity, durable checkpoint, Fast Memory, automatic chat resume и project acceptance из него не следуют.

Запрещены: изменение .github/workflows, deployment/host/shard access или WRITE, secrets, provider calls, реальный чат/API spawn, автоматические retries, потребление какого-либо прежнего one-shot grant, memory-layering attempt 3, изменение approved Project Sources/канона, current-writer или task queue.

Перед работой — свежий GitHub preflight, шесть approved Project Sources по source-loading-policy, current KOD writer, supersession и отсутствие конкурирующего результата именно этой пробы. Если нет допустимого изолированного запуска без названных действий, остановись с exact BLOCKED и представь documentary matrix. Publication/dispatch/inbox не являются receipt, activation или processing_started. После terminal result STOP.

## Передача

Адресат: КОДЕР / KOD v0.5, только ручная активация чата ОПЕРАТОРОМ. Публикация этой задачи не доказывает activation, receipt или processing_started.

---
КТО: КООРДИНАТОР / KOO v0.8
СТАТУС: TASK_PREPARED_FOR_MANUAL_ACTIVATION
