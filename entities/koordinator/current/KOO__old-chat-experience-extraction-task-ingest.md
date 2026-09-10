# Фиксация данных файла старого чата

## Сохранённый источник

- файл: `KOO__OLD-CHAT-experience-extraction-task.md`
- локальный SHA-256: `7e41ac69a67d09df6307faa5a6d2404b79709bf4019e146e311867d74d150666`
- строк: 222
- назначение: универсальное задание старому экземпляру Сущности на извлечение профессионального опыта из истории конкретного чата
- это не recovery snapshot, не current-state и не пересказ чата
- статус, указанный в источнике: `working_protocol_v0_1`
- изменение Project Sources источником не разрешено
- runtime/recovery mutation источником не разрешены

## Основной принцип

Извлекать только то, что следующий экземпляр должен знать и делать иначе благодаря опыту старого экземпляра, чтобы не повторять уже пройденные ошибки и быстрее получать проверяемый результат.

## Разрешённая доказательная база

Только история конкретного чата, реально присутствующие в нём файлы и проверяемые артефакты этого чата. Историческое состояние нельзя выдавать за current truth. Неизвестное должно оставаться `unknown`.

## Требуемые классы результата

1. существенные рабочие эпизоды;
2. каталог существенных ошибок и ловушек;
3. причинные решения;
4. reusable procedures;
5. историческое незавершённое состояние с разделением `open | parked | blocked | unknown | superseded`;
6. машинопригодные experience cards;
7. anti-regression cases;
8. итоговый EXTRACTION_REPORT с честной границей видимого контекста.

## Требуемые выходные файлы

- `ENTITY_experience-extraction.md`
- `ENTITY_experience-cards.jsonl`
- `ENTITY_anti-regression-cases.md`

## Критерий качества

Следующий экземпляр должен раньше распознавать знакомый класс проблемы, не повторять известную ошибку, применять подтверждённый порядок без подсказки, различать historical evidence и current truth, останавливаться на `unknown`, требовать evidence там, где старый экземпляр ошибался, и получать более качественный первый результат с меньшим вмешательством ОПЕРАТОРА.

## Связь с текущей архитектурой

Источник напрямую полезен для развиваемого контура `Entity Continuity / Task Persistence / Experience Continuity`: он определяет правила извлечения слоя опыта из старого instance, но сам по себе не повышается до active Project Source и не подменяет recovery/current-state.

---
document_type: ingest-note
source_file: KOO__OLD-CHAT-experience-extraction-task.md
source_sha256: 7e41ac69a67d09df6307faa5a6d2404b79709bf4019e146e311867d74d150666
source_status: working_protocol_v0_1
active_sources_changed: no
project_time: omitted; trusted project-time source not used
