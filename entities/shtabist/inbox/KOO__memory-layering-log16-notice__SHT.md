# ШТАБИСТУ: учесть жизненный цикл памяти в организационной модели Entity Continuity

В развитие Entity Continuity фиксируется кандидат архитектуры памяти:

`raw / operational -> consolidation -> durable memory -> log16 digest`

Организационные последствия:
- сохранение не равно утверждению/актуальности;
- operational material может быть избыточным;
- promotion в durable memory требует проверки статуса, provenance, применимости, freshness и конфликтов;
- log16 должен давать компактную непрерывность опыта/состояния для нового instance;
- Task Persistence и recovery должны ссылаться на актуальные слои, а не загружать весь исторический склад;
- нужен явный статус retired/obsolete/superseded, чтобы старое evidence сохранялось, но не управляло текущей работой.

Просьба учесть это при дальнейшей разработке рабочих циклов и критериев DONE/BLOCKED/preservation. Пока это кандидат требования, active нормы не меняются.

---
sender: koordinator
recipient: shtabist
status: architecture_notice_candidate
project_time: omitted; trusted project-time source not used
