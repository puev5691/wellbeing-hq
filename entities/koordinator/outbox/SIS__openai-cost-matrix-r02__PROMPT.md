# PROMPT SIS — OpenAI cost matrix r0.2

Ты СИСАДМИН проекта «БЛАГОПОЛУЧИЕ».

Продолжай текущую задачу по Resume-First.

Сначала сделай свежий GitHub-preflight `puev5691/wellbeing-hq` и проверь своего current-writer.

Текущий exact task:
`a011be06d1bbb23b53dc74cd0ee3fb1c53291d34`

Clean runtime staging PASS:
`a242e8bdf0455acf1ebe95d1e352b56370d53691`

KOO current-writer:
`525e5b131472e61b1f55db5ef7307217aea4c4fc`

KOO Writer Gate PASS:
`06dd7873b532c1fe86f4b382d40c26908a5a11b2`

Current queue:
`entities/koordinator/current/KOO__active-queue-r37.md`

Выполни существующий OpenAI four-model cost matrix r0.2 без расширения authority и без создания нового контракта.

Перед provider execution проверь, что exact staged runtime identities всё ещё совпадают с PASS `a242e8...`.

Далее исполни только четыре уже разрешённые попытки:
1. `gpt-5.6-luna`
2. `gpt-5.6-terra`
3. `gpt-5.6-sol`
4. `gpt-6-astra`

Ограничения исходной задачи сохраняются:
- максимум 4 provider attempts;
- retries 0;
- fallback none;
- один одинаковый компактный prompt/output cap;
- никакого tools/web/files/computer-use в provider prompt;
- никаких project secrets/private content;
- сохранить проверенную interactive credential/no-persistence boundary.

Зафиксируй safe metadata по каждой модели в соответствии с exact task.

Результат адресно верни KOO и KOD через действующий файловый обмен. Не считай publication доставкой. Receipt не считай acceptance.

Если preflight или runtime identity не проходит, остановись с точным blocker без provider call.

После terminal result остановись.
