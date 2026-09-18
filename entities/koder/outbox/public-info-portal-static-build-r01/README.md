# Public information portal deterministic static build r0.1

Локальная непроизводственная статическая сборка из pinned WEB assembly r0.1 и presentation r0.2.

- внешний выпуск: не выполнялся;
- Pages/DNS/HTTPS: не изменялись;
- credentials: не используются;
- state database: отсутствует;
- public_ready: false.

Builder проверяет exact Git blob identity четырёх управляющих входов и каждого разрешённого curated-content body. HQ operational bodies не входят в inputs: для HQ используются только metadata из принятого eligibility ledger.

Сборка создаёт только HTML/CSS/JSON. Все страницы несут заметный NON-PRODUCTION PREVIEW banner. Русские человекочитаемые названия и empty-state формулировки применяются из presentation r0.2, exact machine provenance остаётся во вторичном раскрываемом блоке.

Запуск:

`python3 -I -B builder.py --inputs inputs --out site`

Проверка:

`python3 -I -B test_builder.py`

Пакет предназначен для независимой проверки. Внешняя публикация не разрешена.
