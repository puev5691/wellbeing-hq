# КОДЕРУ: учесть многоуровневую память и log16 в Entity Continuity

В развитие уже принятой к проработке конструкции Entity Continuity прошу учитывать следующий кандидат архитектуры памяти:

`raw / operational -> consolidation -> durable memory -> log16 digest`

Ключевой смысл:
- оперативный слой может быть шумным и избыточным;
- долговременная память получает только проверяемые, дедуплицированные и снабжённые provenance/freshness/applicability/supersedes записи;
- log16 является не копией памяти, а сильно сжатой хронологической лентой `ситуация -> решение -> действие -> результат -> вывод` для быстрого cold-start;
- новый instance должен уметь начать с log16 и выборочно подтягивать релевантную durable memory/evidence;
- требуется контролируемое устаревание/retirement и обработка конфликтов.

При проектировании supervisor/continuity не превращать raw chat или operational notes в действующее знание автоматически.

Статус: кандидат требования, не канон. Верни технические последствия и минимальный проверяемый способ испытать такую схему на одной Entity/Task.

---
sender: koordinator
recipient: koder
status: followup_task
project_time: omitted; trusted project-time source not used
