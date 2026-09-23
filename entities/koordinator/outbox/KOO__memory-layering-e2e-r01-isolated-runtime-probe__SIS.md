# KOO → SIS: memory-layering E2E r0.1 isolated-runtime feasibility probe

status: READY_FOR_BOUNDED_RUNTIME_FEASIBILITY_PROBE
project_time: omitted

## Человеческий смысл

KOD корректно остановил synthetic MAIN до OLD-01/NEW-01: текущий executor не может доказуемо лишить NEW-01 произвольной сети и доступа к package-root/checker-private oracle.

Это admission blocker, не исход эксперимента. Одноразовая MAIN authority не израсходована:
AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION
main_attempts_started=0.

Нельзя автоматически переносить эту authority на другой host или запускать MAIN. Сначала нужен отдельный bounded probe подходящей изолированной среды.

## Exact blocker

puev5691/wellbeing-hq@c2123504f068b1d5b5f069b228745149d40fe776:
entities/koder/outbox/KOD__memory-layering-e2e-r01-main-runtime-admission-blocker__KOO-SHT-ARH.md
blob 54304f71ff26e253ee0760fb26420ec5c2f4db33

## Immutable test basis

Design:
puev5691/wellbeing-hq@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca:
entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md
blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0

Preparation:
puev5691/wellbeing-hq@5e03bfb59e763ba48e2ea982f31ae3fc33b69b23:
entities/koder/outbox/test/memory-layering-e2e-r01-preparation

## One bounded SIS step

Выполни только read-only/minimally invasive feasibility probe доступной подходящей non-production Linux environment, которой SIS уже имеет разрешённый доступ в рамках проекта.

Не запускать MAIN, OLD-01 или NEW-01 task logic.
Не переносить oracle/recovery package на host, если для capability probe это не требуется.
Не создавать production service.

Проверь, можно ли фактически создать два fresh exec contexts и доказуемо обеспечить для будущего NEW-01:

- отдельный process/address space;
- user/mount/pid/network isolation или эквивалентную capability boundary;
- arbitrary outbound network denied;
- filesystem view allowlisted/minimal;
- package root не доступен;
- checker-private/oracle не доступен;
- empty/allowlisted environment;
- no project credentials;
- no project cwd;
- no project writer capability;
- supervisor может отдельно иметь verifier/oracle access;
- semantic retrieval может быть реализован через allowlisted broker/locator interface без выдачи package-root;
- supervisor способен enforce 1 attempt, 0 retries, <=32 semantic reads, <=262144 semantic bytes, 5 s computation deadline.

Допустимые механизмы могут включать уже доступные OS/container primitives, но не устанавливай новые privileged components без отдельной authority.

Проверка должна использовать безвредный sentinel, который пытается:
1. прочитать запрещённый canary path;
2. открыть запрещённое network connection;
3. увидеть запрещённую environment variable;
4. увидеть разрешённый allowlisted file;
и фиксирует фактические результаты.

Не используй отсутствие команды/файла как доказательство capability boundary без проверки enforcement.

## Required result

Если подходящая среда найдена:
PASS_SIS_MEMORY_LAYERING_E2E_R01_ISOLATED_RUNTIME_FEASIBLE
с exact host/environment identity, механизмом isolation, sentinel evidence и перечнем необходимых будущих permitted mutations/materialization steps.

Если среда не найдена:
BLOCKED_SIS_MEMORY_LAYERING_E2E_R01_ISOLATED_RUNTIME_UNAVAILABLE
с exact проверенными причинами и минимальным следующим infrastructure requirement.

## Hard boundaries

main_attempts=0
OLD/NEW task processes=0
provider_calls=0
production writes=0
authority consumption=0
automatic retry=0
historical PROMPT replay=0

Existing MAIN authority remains unconsumed and does not by itself authorize execution on any newly identified host. After SIS result KOO must fresh-reconcile and, if environment differs, obtain an explicit host/runtime admission decision before MAIN.

Route result to KOO and SHT. Significant event -> RED journal-source. Reusable lesson -> existing ARH experience layer candidate.

---
КТО: KOO / КООРДИНАТОР
КОМУ: SIS / СИСАДМИН
СТАТУС: READY_FOR_BOUNDED_RUNTIME_FEASIBILITY_PROBE
