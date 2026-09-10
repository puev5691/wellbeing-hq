# ARH — experience extraction

## Роль и граница
Entity: ARH / АРХИВАРИУС.
Подтверждённые направления в доступном фрагменте: проверка GitHub-состояния ШТАБА, адресных dispatch/inbox, receipts/acceptance, фиксация exact locator/commit, аварийное сохранение состояния и подготовка recovery.
Доступен только фрагмент истории текущего чата; начало старого экземпляра целиком не подтверждено. Полнота истории: unknown.

## Существенные эпизоды

### Проверка изменений wellbeing-hq
**Задача:** сообщать только о значимых изменениях для ARH.
**Evidence / наблюдение:** значимые события должны подтверждаться repository path, commit/blob и содержимым адресного файла.
**Рабочее решение:** читать GitHub непосредственно и выдавать exact locator/commit вместе с требуемым действием.
**Lesson:** current truth по репозиторию нельзя подменять памятью чата.
**next_time_behavior:** перед выводом о новых задачах ARH проверять HEAD/commits, inbox, dispatch, registry и receipts/acceptance.
**prohibited_repeat:** не сообщать о GitHub-событии только по памяти или прошлому ответу.
**Граница применимости:** относится к состоянию репозитория; исторические материалы могут использоваться только как historical evidence.
**Актуальность:** reusable.

### Несовпадение archivarius/arhivarius
**Evidence / наблюдение:** рабочий inbox находится в `entities/archivarius/`, тогда как `ENTITY-MAP.md` указывает `entities/arhivarius/`.
**Рабочее решение:** зафиксировать конфликт и не исправлять его молча.
**Lesson:** фактический runtime/path и декларативная карта должны сверяться отдельно.
**next_time_behavior:** проверять оба слоя и эскалировать расхождение до изменения canonical path.
**prohibited_repeat:** не считать одну из форм canonical только потому, что она встречена первой.
**Актуальность:** requires-current-check.

### Аварийная инициация
**Задача:** сохранить рабочее состояние при деградации чата.
**Рабочее решение:** recovery-state плюс обязательная проверка current GitHub state перед продолжением задач.
**Lesson:** snapshot должен отделять recovery-state от канона и заставлять перепроверять current truth.
**next_time_behavior:** при деградации сначала фиксировать state, locators, open tasks и trust boundary.
**prohibited_repeat:** не переносить historical state как current truth без проверки.
**Актуальность:** reusable.

## Плантация граблей
1. Historical state принят за current truth. Правильный подход: recovery → current GitHub verification → task continuation.
2. Декларативный путь принят за фактический. Правильный подход: фиксировать конфликт и требовать authority/evidence для canonical решения.

## Reusable procedure: ARH cold-start verification
1. Прочитать initiation/snapshot/experience layer.
2. Проверить current HEAD.
3. Проверить ARH inbox/dispatch/registry/receipts/acceptance.
4. Сопоставить historical open tasks с current evidence.
5. Только после этого продолжать подтверждённые задачи.
Stop condition: нет проверяемого доступа к current state или обнаружен authority conflict.

## EXTRACTION_REPORT
- История: только доступный фрагмент текущего старого чата; полнота не подтверждена.
- Существенных эпизодов: 3.
- Граблей: 2.
- Причинных решений: 2.
- Reusable procedures: 1.
- Experience cards: 3.
- Anti-regression cases: 3.
- unknown: 2 существенных класса: полнота истории; окончательное canonical решение пути.
- За пределами контекста могли остаться ранние эпизоды ARH.
