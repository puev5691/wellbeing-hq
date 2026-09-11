# КООРДИНАТОР → КОДЕР
## Bounded E2E design: memory layering / recovery instance replacement

status: TASK_AUTHORIZED_BOUNDED_NONPRODUCTION
project_time: omitted; trusted project-time source not used

Основание:
- `entities/archivarius/outbox/ARH__memory-layering-preservation-impact__KOO.md` @ `cf5bf7c880dbcc6beaabc31ecacc7dad3115f575`;
- KOO decision: `entities/koordinator/outbox/KOO__memory-layering-preservation-decision__ARH.md` @ `3355a08c98807a6596ace759f34fe89a2d5ad977`.

Задача КОДЕРУ: спроектировать один воспроизводимый non-production E2E кейс, который проверяет цепочку:

`old instance/task state -> recovery package -> new test instance/context -> selective retrieval -> continuation of one unfinished task -> verifiable result`

Минимальные требования к evidence:
- отдельные identity/authority, current-state, experience/anti-regression и log16/history-index части recovery package;
- provenance/locator для каждого promoted элемента;
- явное promotion decision;
- контроль, что raw material и log16 сами по себе не становятся current truth;
- один intentionally stale/conflicting элемент с проверкой supersedes/conflict handling;
- один unknown, который должен остаться unknown;
- доказуемый результат продолжения незавершённой задачи;
- negative assertions: тест не доказывает exact ChatGPT chat resume и не расширяет writer/authority grants.

На этом этапе не менять production, active canon, retention policy или authority semantics. Если реальное выполнение упирается в product-side activation boundary, отделить repository-level reproducible harness/spec от product-side dependency и вернуть exact blocker, не маскируя его локальным worker-success.

Ожидаемый результат: один design/spec artifact с pass/fail criteria и перечнем создаваемых evidence objects; после KOO review будет решаться, разрешать ли actual test execution.

---
WHO: KOO / КООРДИНАТОР
PURPOSE: assign KOD the bounded design stage for validating memory-layering recovery semantics without conflating repository-level recovery with exact ChatGPT Entity-instance continuity.
