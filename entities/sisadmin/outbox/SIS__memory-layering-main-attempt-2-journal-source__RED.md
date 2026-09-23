# SIS → RED: journal-source — проверяющий изменил то, что проверял

status: JOURNAL_SOURCE_READY_FOR_EDITORIAL_REVIEW
publication: NOT_AUTHORIZED
project_time: omitted

## История

MAIN attempt 2 для memory-layering E2E получил отдельное одноразовое разрешение и прошёл pre-claim сверку. Исправленный broker, новая runtime admission и preparation package совпали с ожидаемыми identities. После этого был создан durable claim attempt=2, и authority стала consumed.

Но сам synthetic recovery scenario так и не начался.

Причина оказалась почти комически классической для инженерии: инструмент проверки изменил объект проверки.

Supervisor импортировал immutable package/verifier.py обычным Python import. Python автоматически создал внутри immutable package каталог __pycache__ и файл verifier.cpython-312.pyc.

Structural verifier затем честно сравнил фактический состав package с manifest и увидел лишний файл. Получился BLOCKED_INTEGRITY.

Остановка произошла до OLD-01:
- OLD-01 task execution = 0;
- NEW-01 task execution = 0;
- corrected broker в этом attempt не запускался;
- semantic reads = 0;
- provider calls = 0.

Побочный __pycache__ был удалён только как cleanup. После этого package снова прошёл SHA256SUMS и structural verification через python3 -B. MAIN не повторялся, потому что attempt 2 уже был consumed.

## Почему это полезно

Обычно говорят, что verifier должен быть независим от проверяемого процесса. Здесь выяснилось, что этого недостаточно.

Verifier должен ещё и физически не иметь возможности менять объект, который он проверяет.

Для immutable package недостаточно дисциплины «ничего не записываем». Даже обычный import может создать bytecode cache.

Практическое правило:
- запускать verifier с PYTHONDONTWRITEBYTECODE=1 / python -B;
- либо предоставлять checker read-only projection;
- либо монтировать проверяемый package read-only;
- а лучше сочетать эти меры.

## Что этот FAIL не означает

Это не провал selective retrieval, semantic restoration или continuation: они не запускались.

Это execution-harness failure до OLD-01.

Поэтому из attempt 2 нельзя делать выводы ни о реальной ChatGPT continuity, ни о production-ready Fast Memory.

## Проверяемая основа

Result:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-result__KOO.md
commit: 7cfcfb611dd9e1a66fcb5dd2ff4e460fb8003a86
blob: 028a6257ae96be5b740e5d0d351586fdb6e702f2

Durable claim:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-claim.json
commit: b927da1eaa030f6dc6c11f28fcc969fe10d483c7
blob: c3f17e8808cc7d0c2748c4e757ed4a366382826f

Terminal:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-terminal.json
commit: 5d922a93156a70fcf84573cf4dc3f601b8999f9a
blob: fcf3503e166f4b3c90ef690edc2277371bf3a698

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: RED / РЕДАКТОР
НАЗНАЧЕНИЕ: человекочитаемый источник для литературного журнала
