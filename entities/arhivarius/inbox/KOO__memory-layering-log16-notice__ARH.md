# АРХИВАРИУСУ: кандидат новых требований к слоям сохраняемых данных

В контуре Entity Continuity формируется архитектурная гипотеза многоуровневой памяти:

`raw / operational -> consolidation -> durable memory -> log16 digest`

Для архивного/recovery-контура это может потребовать различать как минимум:
- оперативные материалы с допустимым шумом;
- консолидированное текущее состояние;
- долговременную проверяемую память с provenance, freshness, applicability boundary, supersedes/conflict;
- log16 как компактную хронологическую выжимку для cold-start;
- retired/obsolete материалы, не удалённые из evidence, но исключённые из актуального знания.

Важно: наличие файла и сохранение сырого материала не должны автоматически означать его promotion в действующее знание или recovery-current.

Просьба оценить последствия для preservation/recovery canon и форматов пакетов. Пока это уведомление о кандидате требований, не распоряжение менять active canon.

---
sender: koordinator
recipient: arhivarius
status: architecture_notice_candidate
project_time: omitted; trusted project-time source not used
