# KOO → ARH: Booster experience-layer reconciliation r0.1

status: READY_FOR_EXPERIENCE_RECONCILIATION
project_time: omitted

## Зачем

ОПЕРАТОР указал на системную проблему: технические результаты сохраняются лучше, чем накопленный опыт. Fresh inventory показывает, что experience layer уже существует:
- entities/archivarius/current/experience/ARH_experience-extraction.md
- entities/archivarius/current/experience/ARH_experience-cards.jsonl
- lineage/anti-regression artifacts;
а также существуют KOO/RED/VOL experience materials.

Новый контур опыта создавать нельзя до reconciliation существующего.

## Задача ARH

Resume-First. Выполни bounded reconciliation действующего experience layer применительно к текущей Booster lineage.

Проверь:
1. какие уроки Booster уже представлены в действующих experience artifacts;
2. какие подтверждённые уроки отсутствуют;
3. какие из них являются reusable operational lessons, а какие лишь историей для литературного журнала;
4. как добавить недостающие lessons без дублирования, переписывания history и превращения inference в fact.

Минимально рассмотреть подтверждённые уроки:
- technical PASS != demonstrated utility;
- evaluator/checker должен соответствовать опубликованной specification;
- unknown measurement/cost нельзя заменять нулём;
- failure metadata нужно сохранять до normalization, если post-normalization failure иначе уничтожает causal observability;
- consumed authority не reset/replay;
- post-hoc checker correction не переписывает original result;
- маленькая задача может быть плохим utility benchmark из-за overhead, но это наблюдение N=1/N=2, не универсальный закон.

Token-budget cause r0.1 сохранять UNCONFIRMED.

Не изменять approved Project Sources и не вводить новую норму самостоятельно.

Если существующий experience-layer contract позволяет bounded ingest без нового approval, подготовь exact candidate/update и маршрутизируй по его действующей процедуре. Если требуется decision gate, верни KOO один exact gate.

Сохрани provenance к техническим evidence и редакционному journal episode, но не смешивай литературный текст с operational lesson cards.

---
КТО: KOO / КООРДИНАТОР
КОМУ: ARH / АРХИВАРИУС
СТАТУС: READY_FOR_EXPERIENCE_RECONCILIATION
