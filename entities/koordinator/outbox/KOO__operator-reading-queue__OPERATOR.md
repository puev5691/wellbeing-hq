# ОПЕРАТОР — очередь чтения и решений

status: ACTIVE_READING_QUEUE
purpose: единая русскоязычная точка входа для материалов, требующих чтения/решения ОПЕРАТОРА
project_time: omitted; trusted project-time source not used

## Уже обработано ОПЕРАТОРОМ

### «Сначала она была выдумана» v0.3

Состояние: `WAITING_OPERATOR_EDIT_RETURN`.

ОПЕРАТОР забрал текст на собственное редактирование. RED не должен править его параллельно.

### Речь для выступления v0.2

Состояние: `ACCEPTED_FOR_DISCUSSION__NO_PUBLICATION_INFERRED`.

ОПЕРАТОР одобрил и принял материал как основу для обсуждения. Внешняя публикация из этого автоматически не следует.

### Telegram, фаза 1B

Решение ОПЕРАТОРА получено: SIS разрешено использовать любой допустимый технический способ для настройки и дальнейшего применения требуемых инструментов; ОПЕРАТОР готов выполнить exact human actions, если они понадобятся.

Текущий маршрут:
`entities/sisadmin/inbox/KOO__telegram-phase1b-authorized-tooling-path__SIS.md`

Состояние: `WAITING_SIS_PROFILE_RESULT`.

### Первый внешний многомодельный provider

Решение ОПЕРАТОРА получено: первым работаем с Anthropic. Google остаётся допустимым резервным/сравнительным route.

Текущий класс пилота: только `D0_SYNTHETIC`.

Состояние: `ANTHROPIC_SELECTED__PREPARING_D0_READINESS`.

---

## Готово к чтению ОПЕРАТОРОМ

### Anthropic — цена, доступ и технические возможности

Русский текущий brief KOO:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__anthropic-access-price-capabilities-ru__OPERATOR.md

Он содержит текущие официально проверенные цены Sonnet 5 / Opus 5 / Fable 5.1, способы доступа, основные API/tool возможности и рекомендуемую схему первого `D0_SYNTHETIC` вызова.

Параллельно KAN получил отдельную задачу на независимую official-source revalidation перед первым платным live request:
`entities/kancelar/inbox/KOO__anthropic-live-d0-access-cost-capabilities__KAN.md`.

После KAN-result KOO выдаст точный следующий технический шаг для direct Anthropic adapter/live D0 pilot.

---

## Операторская языковая граница

Для материалов, которые ОПЕРАТОР должен читать и по которым должен принимать решение:
- основной текст — русский;
- латиница только для технически неизбежных имён: переменных, команд, файлов, путей, машинных кодов, моделей/провайдеров, commit/blob, API/URI/locator;
- английские технические термины переводятся или поясняются при первом употреблении;
- человеческий смысл идёт раньше служебных метаданных.

Рабочая директива KOO:
`entities/koordinator/current/KOO__operator-facing-language-rule-v01.md`

---

КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: показывать ОПЕРАТОРУ только актуальные хвосты чтения и решений после снятия Telegram/Anthropic WAITING_OPERATOR blockers
СТАТУС: active_operator_reading_queue
