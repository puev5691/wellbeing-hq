# ОПЕРАТОР — очередь чтения и решений

status: ACTIVE_READING_QUEUE
purpose: единая русскоязычная точка входа для материалов, требующих чтения/решения ОПЕРАТОРА
project_time: omitted; trusted project-time source not used

## Уже обработано ОПЕРАТОРОМ

### «Сначала она была выдумана» v0.3

Состояние:
`WAITING_OPERATOR_EDIT_RETURN`

ОПЕРАТОР забрал текст на собственное редактирование. RED не должен править его параллельно.

### Public cooperation speech v0.2

Состояние:
`ACCEPTED_FOR_DISCUSSION__NO_PUBLICATION_INFERRED`

ОПЕРАТОР одобрил и принял материал как основу для обсуждения. Это не является внешним publication release. Возможные результаты обсуждения будут отдельными будущими задачами.

---

## Ожидает нового русскоязычного материала

### 1. Telegram Phase 1B

Предыдущее решение:
`RETURN_FOR_RUSSIAN_OPERATOR_VERSION`

Текущий технический исходник:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__telegram-phase1b-privilege-path-dependency__OPERATOR.md

RED получил задачу подготовить русскоязычную human-readable версию:
`entities/redaktor/inbox/KOO__operator-briefs-ru__RED.md`

До получения этой версии privileged execution path не считается разрешённым.

### 2. Multi-model D0 pilot

Предыдущее решение:
`CONTINUE_TOPIC__RETURN_FOR_RUSSIAN_OPERATOR_DESCRIPTION`

Текущий technical decision:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__first-real-multimodel-d0-pilot__OPERATOR.md

Provider evidence:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/kancelar/outbox/KAN__multi-model-first-provider-evidence-matrix__KOO.md

Local gateway proof:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md

RED получил задачу подготовить понятное русскоязычное описание:
`entities/redaktor/inbox/KOO__operator-briefs-ru__RED.md`

До чтения этой версии provider pilot не авторизован.

---

## Операторская языковая граница

Для материалов, которые ОПЕРАТОР должен читать и по которым должен принимать решение:
- основной текст — русский;
- латиница только для технически неизбежных имён: переменных, команд, файлов, путей, машинных кодов, моделей/провайдеров, commit/blob, API/URI/locator;
- английские технические термины по смыслу переводятся или поясняются при первом употреблении;
- human-readable смысл идёт раньше служебных метаданных.

Рабочая директива KOO:
`entities/koordinator/current/KOO__operator-facing-language-rule-v01.md`

---

КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: показывать ОПЕРАТОРУ только актуальные хвосты чтения и не заставлять его разбирать англоязычные технические материалы
СТАТУС: active_operator_reading_queue
