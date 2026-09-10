# ВЕБМАСТЕР: отчёт аварийной cold-start инициации

## Итог

**Статус: `initiation_verified`.**

Новый экземпляр ВЕБМАСТЕРА инициирован по пяти действующим approved Project Sources и внешнему аварийному recovery-пакету WEB. Внешний locator доступен, фактический состав совпадает с manifest, версия зафиксирована по commit/tree/blob identifiers, SHA-256 трёх содержательных recovery-файлов пересчитан и совпал с опубликованным `sha256sums.txt`.

Прежний WEB-чат **не использовался как current state** и не применялся для восстановления старых задач, конфигураций или production-состояния.

## 1. Проверенный locator

    store: github
    repository: puev5691/wellbeing-entity-bootstrap
    path: entities/web/recovery/current
    ref: main
    manifest: WEB__recovery-manifest__WEB.md
    checksums: sha256sums.txt

Поскольку `main` изменяемый, фактически прочитанная версия была закреплена по commit:

    1e2c8092b17adb11a02fb91c908ce60e0464a6dd

## 2. Commit, tree и blob identifiers

Commit:

    1e2c8092b17adb11a02fb91c908ce60e0464a6dd

Корневое tree commit:

    ef66a25dfc758c49b1e00b954d3744a13a468db2

Tree `entities/web`:

    3e8a8c2f782eb6c0be9890019846360d3cb4e120

Tree `entities/web/recovery`:

    bf13212f385a51adb14c7d9feb3bf03b0ff84411

Tree `entities/web/recovery/current`:

    85248e4f964258cd2332e8451462d61b91054e30

Blob identifiers:

- `WEB__initiation-current__WEB.md` — `1f81c77b50fcf40a8f5a6ca5c8c2b5b927ff1a38`
- `WEB__snapshot__WEB.md` — `14fd417f8c3ee9ee4b4682a0d57e5705cc393796`
- `WEB__recovery-manifest__WEB.md` — `edb15bcb5b92463007217e192c0106ed65fbda5b`
- `sha256sums.txt` — `73c8105f136e83ea55ef646a58acc51af5830863`

## 3. Фактический состав recovery-каталога

Проверено ровно четыре файла:

1. `WEB__initiation-current__WEB.md`
2. `WEB__recovery-manifest__WEB.md`
3. `WEB__snapshot__WEB.md`
4. `sha256sums.txt`

Состав совпадает с `WEB__recovery-manifest__WEB.md`.

## 4. Проверка SHA-256

Для трёх содержательных recovery-файлов опубликованные и независимо пересчитанные значения совпали:

| Файл | SHA-256 из `sha256sums.txt` | Пересчитанный SHA-256 | Результат |
|---|---|---|---|
| `WEB__initiation-current__WEB.md` | `91234401564b5bc2f1294688dcea139b6830ecc6d97c6df141714ae7b080a7e4` | `91234401564b5bc2f1294688dcea139b6830ecc6d97c6df141714ae7b080a7e4` | совпадает |
| `WEB__snapshot__WEB.md` | `649e8f32aa284082804aa006b1b1688ec3aff02c721c13b42974f468643279c4` | `649e8f32aa284082804aa006b1b1688ec3aff02c721c13b42974f468643279c4` | совпадает |
| `WEB__recovery-manifest__WEB.md` | `677c039e075d3cafbfadc1ae8f7c42757028aa0b6c78e76879951b8825a9f99a` | `677c039e075d3cafbfadc1ae8f7c42757028aa0b6c78e76879951b8825a9f99a` | совпадает |

Итог проверки целостности: **успешно**.

## 5. Восстановленная роль WEB и границы

ВЕБМАСТЕР отвечает за:

- сайт;
- HTML/CSS/JS;
- навигацию;
- публикационные страницы;
- Проводник как web-интерфейс.

Границы роли:

- не утверждать DNS, HTTPS, безопасность VDS и policy без профильной проверки;
- не объявлять публикацию состоявшейся без фактической проверки;
- не считать старые nginx/proxy/tunnel-конфигурации действующими без новой проверки;
- не менять production без отдельной задачи и подтверждения ОПЕРАТОРА;
- не восстанавливать состояние по памяти других чатов.

## 6. Что подтверждено минимальным snapshot

После успешной внешней проверки recovery-пакета как minimal current принимаются:

- существование и профиль роли ВЕБМАСТЕРА;
- перечисленные границы роли;
- аварийный характер bootstrap: пакет не является сохранённой памятью старого WEB;
- единственная активная задача на старте — завершить cold-start, затем провести read-only аудит внешнего веб-контура;
- необходимость заново отделить current от legacy и unknown;
- запрет менять production в рамках cold-start.

Исторические сведения внутри snapshot о прежней recovery-кампании рассматриваются как provenance аварийного пакета, а не как доказательство текущего состояния веб-контура.

## 7. Что остаётся unknown / legacy

Без отдельной внешней проверки **не считается current**:

- фактическая доступность сайта;
- текущий URL и структура страниц;
- document root;
- опубликованные материалы;
- меню и навигация;
- фактическое состояние Проводника;
- production-версии HTML/CSS/JS;
- nginx, reverse proxy и tunnel-конфигурации;
- DNS;
- HTTPS;
- VDS и его безопасность;
- локальные каталоги;
- старые backup;
- старые задачи и хвосты WEB;
- старые решения прежнего WEB-чата.

Все такие сведения остаются `unknown` либо `legacy` до нового проверяемого аудита.

## 8. Использование прежнего чата

Прежний WEB-чат не использовался как источник истины для этой инициации.

Не переносились автоматически:

- его память;
- его незавершённые задачи;
- его выводы о production;
- его конфигурации;
- его представление о состоянии сайта, Проводника, DNS, HTTPS, VDS и публикаций.

Текущая основа ограничена approved Project Sources и верифицированным внешним аварийным recovery-пакетом.

## 9. Один безопасный следующий шаг

**Не выполнять в рамках cold-start.**

Следующий профильный шаг:

> read-only аудит внешнего веб-контура проекта: фактический сайт, доступные репозитории, страницы и навигация, Проводник, публикационный слой, current/legacy/unknown. Production не менять.

Статус `upgraded` не присваивается. Его закрывает КООРДИНАТОР.

---

from_entity: WEB
to_entity: OPR
next_route: OPR -> KOO
document_type: cold-start-initiation-report
project_scope: ШТАБ БЛАГОПОЛУЧИЯ
initiation_status: initiation_verified
recovery_standard: v1.2
verified_commit: 1e2c8092b17adb11a02fb91c908ce60e0464a6dd
verified_current_tree: 85248e4f964258cd2332e8451462d61b91054e30
production_changed: false
old_chat_used_as_current_state: false
project_time: generated_without_trusted_project_time
