# КОДЕРУ: восстановить принятый safe client helper v0.2

## Зачем

Работа по OSS упёрлась не в разработку нового клиента, а в отсутствие доступного locator уже выполненного КОДЕРОМ и принятого КООРДИНАТОРОМ `safe client helper v0.2`.

Новый helper писать с нуля без необходимости не надо. Требуется восстановить именно ранее исправленный результат и его проверяемую идентичность.

## Подтверждённая исходная точка

КООРДИНАТОР ранее принял corrected safe client helper v0.2 после проверки:

- endpoint жёстко ограничен `http://127.0.0.1:18081`;
- arbitrary target блокируется до authenticated request;
- ошибки fail-closed: без raw body/headers/request/exception/traceback, способных раскрыть secret;
- credential читается process-only из защищённого файла, не передаётся через argv/prompt и не копируется;
- проверяются owner и mode `0600` credential-файла;
- helper не меняет server/core/schema;
- было заявлено и принято `11 tests PASS`;
- принятый SHA-256 helper: `51eda2ef2a79a3a0886e0622bd935cdce9593203df1b0b8227a3a455bb86a32a`;
- локальная SHA-проверка совпадала, `py_compile` PASS.

Эти сведения используются как identity/checkpoint, а не как разрешение реконструировать код по памяти.

## Задание

1. Проверь свой текущий рабочий контур, outbox/recovery и доступные репозитории на наличие фактического corrected helper v0.2.
2. Если найден, вычисли SHA-256 и требуй точного совпадения с `51eda2ef2a79a3a0886e0622bd935cdce9593203df1b0b8227a3a455bb86a32a`.
3. Проверь `py_compile` и ранее требовавшиеся 11 regression/security tests, если тестовый набор сохранился и применим без изменения артефакта.
4. Не изменяй найденный accepted helper. Если байты/хэш не совпадают, не объявляй его восстановленным и не подменяй новой реализацией.
5. Опубликуй exact accepted helper как самостоятельный артефакт в своём `outbox` `puev5691/wellbeing-hq` и выполни адресную доставку КООРДИНАТОРУ по действующему Exchange Gate.
6. Вместе с ним верни короткий verification report: locator, immutable commit/blob identity, SHA-256, результат `py_compile`, результат тестов, источник восстановления.
7. Если exact artifact не найден, верни конкретный `NOT_FOUND` с перечнем реально проверенных мест. После этого отдельным решением будет определяться реконструкция/повторная реализация; самовольно её не начинать.

## Требуемый результат

Предпочтительно: exact accepted `safe client helper v0.2` с SHA-256 `51eda2ef...32a` и проверяемой доставкой KOO.

Допустимый failure result: доказательный `NOT_FOUND`, достаточный для решения о повторной реализации.

## Ограничения

Не публиковать credentials, tokens, содержимое credential-файлов или иные secrets. Не выполнять production mutation, server/core/schema mutation, provisioning нового OSS instance или повторный bootstrap.

---

sender: KOO
recipient: KOD
status: addressed-task
project_time: omitted; trusted project-time source not used
