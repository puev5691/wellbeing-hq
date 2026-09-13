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

---

## Готово к чтению ОПЕРАТОРОМ

### 1. Telegram, фаза 1B — русская операторская версия

Прочитать:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/redaktor/outbox/RED__telegram-phase1b-operator-brief-ru__KOO.md

Exact version:
commit `f1006919533f0dde2832c4b3aa65903307342f86`
blob `23d9d5c076abcfe76444383c020e6037aa06e19c`.

Состояние после чтения должно перейти только по явному решению ОПЕРАТОРА.

Требуется решить, каким разрешённым способом SIS получает privileged execution path на `ruvds-xnqc6` для bounded non-production provisioning/readback.

До такого решения никаких серверных изменений, production, live Telegram send, public webhook или публикации секретов не разрешено.

### 2. Многомодельный шлюз — русская операторская версия

Прочитать:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/redaktor/outbox/RED__multimodel-operator-brief-ru__KOO.md

Exact version:
commit `6f5f00aa4f55444157cd292bf0456706196a20cd`
blob `2b6db6de7e259d55bff8ffe4fbaf1c293982a423`.

После чтения можно отдельно решить:
- разрешать ли первый реальный `D0_SYNTHETIC` pilot;
- если разрешать, какой direct provider выбрать первым: Anthropic или Google;
- либо пока оставить внешний pilot на HOLD.

Pro уже подтверждён как купленный и активированный, но это не заменяет отдельное решение по provider/API/data path.

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
ДЛЯ ЧЕГО: показывать ОПЕРАТОРУ актуальные русскоязычные материалы и требуемые решения без поиска по дереву GitHub
СТАТУС: active_operator_reading_queue
