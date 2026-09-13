# ОПЕРАТОР — очередь чтения и решений

status: ACTIVE_READING_QUEUE
purpose: единая human-readable точка входа для материалов, требующих чтения/решения ОПЕРАТОРА
project_time: omitted; trusted project-time source not used

## Как пользоваться

Открывай пункты сверху вниз. Для каждого указано:
- что прочитать;
- прямая ссылка;
- какое решение требуется;
- что произойдёт после решения.

Это не заменяет исходные артефакты и их immutable identity. Это операторская навигационная карточка.

---

## 1. Telegram Phase 1B — разрешённый privileged execution path

### Что прочитать

Основное решение KOO:

https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__telegram-phase1b-privilege-path-dependency__OPERATOR.md

Underlying SIS blocker:

https://github.com/puev5691/wellbeing-hq/blob/main/entities/sisadmin/outbox/SIS__telegram-phase1b-host-gate-r3-result__KOO.md

### Суть

На `ruvds-xnqc6` collision по path/user/unit/port не найден, но текущий remote execution path не позволил даже выполнить `sudo -n true`. Поэтому SIS не может доказанно выполнить bounded non-production provisioning/readback.

### Решение ОПЕРАТОРА

Нужно либо:
- разрешить/дать допустимый privileged execution path на `ruvds-xnqc6`;
- либо указать уже утверждённый механизм, через который SIS может выполнить exact privileged provisioning/readback.

Не требуется передавать пароли/ключи в GitHub.

### После решения

KOO возвращает SIS на fresh host-scope preflight и bounded Telegram Phase1B host gate.

---

## 2. «Сначала она была выдумана» v0.3 — release decision

### Сначала прочитать сам текст

https://github.com/puev5691/wellbeing-hq/blob/main/entities/redaktor/outbox/RED__publication-snachala-ona-byla-vydumana-v03__KOO.md

### Затем карточку решения

https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__snachala-ona-byla-vydumana-v03__OPERATOR.md

KAN delta-review уже дал `PASS_DELTA`; критических дефектов в назначенном scope не осталось.

### Решение ОПЕРАТОРА

Одно из:
- `RELEASE_ACCEPTED_FOR_INTENDED_USE`
- `RETURN_TO_RED_WITH_EXACT_CHANGES`
- `HOLD_NO_RELEASE`

### После решения

- ACCEPT → KOO выдаёт следующий release/publication route;
- RETURN → exact changes идут RED;
- HOLD → ветка фиксируется как waiting/held без самовольной доработки.

---

## 3. Public cooperation speech v0.2 — human review

### Сначала прочитать текст

https://github.com/puev5691/wellbeing-hq/blob/main/entities/redaktor/outbox/RED__wellbeing-cooperation-speech-v02__KOO.md

### Затем карточку KOO

https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__wellbeing-cooperation-speech-v02__OPERATOR.md

KOO уже принял текст как bounded public-speech candidate. Это не равно публикации или человеческому approval.

### Решение ОПЕРАТОРА

- принять для предполагаемого использования;
- вернуть RED exact editorial changes;
- hold.

### После решения

KOO маршрутизирует release либо revision.

---

## 4. Первый реальный multi-model D0 pilot

### Карточка решения

https://github.com/puev5691/wellbeing-hq/blob/main/entities/koordinator/outbox/KOO__first-real-multimodel-d0-pilot__OPERATOR.md

### Provider evidence

https://github.com/puev5691/wellbeing-hq/blob/main/entities/kancelar/outbox/KAN__multi-model-first-provider-evidence-matrix__KOO.md

### Local gateway proof

https://github.com/puev5691/wellbeing-hq/blob/main/entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md

### Проверенная база

- local D0 synthetic gateway mock: `PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK`, 18/18 tests;
- Anthropic direct commercial/API route: eligible for D0/D1 under stated conditions;
- Google Cloud Vertex/Gemini direct route: eligible for D0/D1 under stated conditions;
- OpenRouter: conditional; не выбран первым маршрутом.

### Решение ОПЕРАТОРА

Одно из:
- `AUTHORIZE_ANTHROPIC_D0_PILOT`
- `AUTHORIZE_GOOGLE_D0_PILOT`
- `HOLD_EXTERNAL_PROVIDER_PILOT`

Это разрешение относится только к D0 synthetic pilot. Оно не разрешает D1/D2+, project/private data, production, arbitrary tools/connectors или автоматический fallback.

---

# Рекомендуемый порядок чтения

1. Literary v0.3 — потому что это чистое человеческое решение по уже готовому материалу.
2. Cooperation speech v0.2 — аналогично.
3. Multi-model D0 pilot — архитектурное решение, но техническая база уже готова.
4. Telegram privileged execution path — решение короткое, но требует понимания, каким способом реально дать SIS допустимый root-path.

---

# Рабочее правило KOO для материалов ОПЕРАТОРА

Если от ОПЕРАТОРА требуется прочитать материал или принять решение, KOO должен:

1. не ограничиваться locator/path в чате;
2. давать прямую GitHub-ссылку на human-readable decision file;
3. если нужно изучить содержимое — давать отдельную прямую ссылку на underlying source/candidate;
4. сводить несколько одновременно ожидающих решений в одну операторскую reading queue;
5. по возможности давать тот же queue-файл отдельной выгрузкой;
6. не считать наличие файла в operator inbox доказательством того, что ОПЕРАТОР его прочитал или принял решение.

Это рабочее правило KOO, не Project Source/canon.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ одну человеческую точку входа во все текущие хвосты чтения/решений
СТАТУС: active_operator_reading_queue
