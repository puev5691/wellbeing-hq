# КООРДИНАТОР — текущая рабочая очередь v0.7

Статус: актуальная сверенная рабочая очередь.  
Это рабочий документ КООРДИНАТОРА, не канон проекта.  
Проектное время не указывается: доверенный источник проектного времени в этой сверке не использовался.

## Коротко для ОПЕРАТОРА

Сейчас твоя ручная работа состоит из четырёх запусков:

1. **КОДЕР** — не обычный wake, а инициация нового экземпляра по exact task из inbox.
2. **АРХИВАРИУС** — bounded recovery-operational review кандидата общей wake/initiation/resume процедуры r0.3.
3. **ШАРДОВИК** — read-only исследование exact механизма main/root genesis TERA2.
4. **ВЕБМАСТЕР** — узкая независимая перепроверка закрытия Static Preview E1 v0.3.

СИСАДМИНА, КАНЦЕЛЯРИЮ и ШТАБИСТА сейчас не будить.

## Что изменилось после v0.6

- SIS восстановил управляемый доступ к эРэФии через Remote Desktop Commander; KOO bounded PASS принят.
- SHD провёл локальный inventory и обнаружил реальный fork Буржуиния ↔ эРэФия после блока `2984033`; автоматическое соединение/сброс остановлено.
- ОПЕРАТОР уже изменил направление эксперимента: старый shard-only WBN контур не является будущей основой; следующий эксперимент должен начинаться с main/root genesis.
- KOD закрыл Static Preview E1 v0.3; KOO результат принял.
- KAN завершил authority/terminology review кандидата wake/initiation/resume; A1-A6 встроены KOO в candidate r0.3.
- ARH сообщил routing-gap; exact recovery-operational review task теперь материализован.
- Новый/другой KOD chat не имеет доказанной continuity прежнего verified instance, поэтому для него материализована replacement initiation v0.2 без writer transfer.

## Активные независимые полосы

### A. KOD / КОДЕР — ИНИЦИАЦИЯ

Exact input:
`entities/koder/inbox/KOO__replacement-initiation-v02__KOD.md`

Task commit:
`d1c490a47595ff4c39b8fcb8f0811d9137a922a8`

Состояние: `INITIATION_REQUIRED / manual chat start required`.

Задача: восстановить новый экземпляр по canonical recovery, reconcile более свежий KOD evidence, вернуть initiation report. Writer transfer не выполнять. Следующие KOD профильные lanes пока не запускать.

### B. ARH / АРХИВАРИУС — recovery-operational review

Exact input:
`entities/archivarius/inbox/KOO__entity-wake-initiation-resume-recovery-review__ARH.md`

Task commit:
`d0554bf2ee7ed45c21d47b64f13d63eeb896ebeb`

Candidate r0.3:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r03.md`
commit `fa92a24e89ef289689f28f2ebff034cf8279db34`.

Activation evidence: `processing_started: no`; manual wake required.

Отдельный ARH sanitation-gap по `recovery-pending` lifecycle destination пока припаркован и не исполняется параллельно.

### C. SHD / ШАРДОВИК — main/root genesis research

Exact input:
`entities/shardovik/inbox/KOO__tera2-main-genesis-root-research-r01__SHD.md`

Task commit:
`31a283417df2d499882456771cf0f70b0427bb71`.

Activation evidence: `processing_started: no`; manual wake required.

Задача только read-only: установить точный upstream TERA2 механизм main/root genesis и подготовить воспроизводимый план. Старые WBN services/DATA/DB не менять.

### D. WEB / ВЕБМАСТЕР — Static Preview E1 recheck

Exact input:
`entities/webmaster/inbox/KOO__info-entry-static-preview-v03-narrow-recheck__WEB.md`

Task commit:
`2e2a747596169d1e7467ef6e85e54fa87be519f2`.

Activation evidence: `processing_started: no`; manual wake required.

Задача только narrow E1 recheck immutable v0.3 package. Никакого нового дизайна или deployment.

## Сейчас не будить

### SIS / СИСАДМИН

ЭрэФия доступна через Commander. Его текущий инфраструктурный lane закрыт PASS. Telegram Phase1B не возобновляется автоматически и остаётся отдельной более низкой задачей до нового KOO решения.

### KAN / КАНЦЕЛЯРИЯ

Authority/terminology review завершён: `PASS_WITH_EXACT_AUTHORITY_FIXES`. Замечания уже встроены KOO в r0.3.

### SHT / ШТАБИСТ

Process review завершён ранее. Следующий вызов возможен только если после ARH/KOO integration потребуется повторный bounded process recheck.

### VOL / ВОЛОНТЁР

P5 evidence scout закрыт: пригодного измеренного эпизода пока нет.

## После возврата результатов

- KOD initiation report → KOO fresh preflight → отдельное решение по writer boundary → только потом следующий KOD lane.
- ARH review → KOO integration final candidate → ОПЕРАТОР approval/reject v1.5.
- SHD research → KOO review → отдельный future launch/design gate; никакого автоматического genesis launch.
- WEB recheck → KOO closes/reopens Static Preview E1 dependency.

## Операторский интерфейс

ОПЕРАТОР не читает inbox и не пересказывает задачу. Для каждого чата используется готовый короткий промпт из:
`entities/koordinator/current/KOO__operator-wake-card-v02-ru.md`.

Если Сущность просит содержание уже адресованного input, она сначала обязана сама сделать Resume-First и прочитать свой inbox.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: перестроить работу ОПЕРАТОРА после закрытия SIS/KAN/KOD-E1 и смены WBN экспериментального направления
СТАТУС: актуальная_сверенная_очередь_v0_7
