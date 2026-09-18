# Portal presentation boundary fix r0.1

Исправление ограничено presentation semantics поверх принятой deterministic static build r0.1.

Изменено:
- primary labels detail-страниц задаются явной русской human-readable таблицей;
- internal source id сохраняется только внутри раскрываемого provenance;
- candidate/preview_candidate получает видимый badge «Кандидат»;
- добавлены негативные/coverage tests.

Не изменено:
- pinned WEB/RED inputs;
- source status/public_ready;
- static-only/no-DB boundary;
- source identity fail-closed;
- empty states;
- preview banner;
- deployment boundary.

Это NON-PRODUCTION PREVIEW. Внешняя публикация не разрешена.
