# SIS work journal r0.1

status: NON_AUTHORITATIVE_CONTINUITY_JOURNAL
owner: SIS / СИСАДМИН
project_time: omitted; trusted project-time source not used

## Назначение

Сохранять рабочие уроки, проверенные operational locators и continuity notes, чтобы SIS не просил ОПЕРАТОРА заново восстанавливать уже доступные данные.

Журнал не заменяет current-state или task authority. Mutable facts перед действием перепроверяются.

## Эпизод: пропущенный SSH hop

SIS подготовил remote script на `ruvds-xnqc6`, но human-facing handoff дал команду запуска remote path без явного SSH-перехода. ОПЕРАТОР выполнил её в локальном Termux/tmux и получил `No such file or directory`.

Ошибка была не в хосте, а в continuity/handoff: SIS должен был сначала восстановить locator из project information field и verified tool channel, а не просить человека повторять известные данные.

Fresh verified facts:
- host: `ruvds-xnqc6`;
- principal: `pev5691`;
- IPv4: `185.39.19.240`;
- SSH: `2222/tcp`;
- remote tmux: `3.4`;
- runtime: `/home/pev5691/openai-d0-runtime-r01`.

GitHub continuity evidence:
`entities/sisadmin/outbox/SIS__openai-d0-host-preflight-r01__KOO.md`.

Operational rule:
`SEARCH INFORMATION FIELD → VERIFY MUTABLE LOCATOR → BUILD COMPLETE OPERATOR COMMAND → ONLY THEN ASK FOR HUMAN-ONLY INPUT`.

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: continuity journal after avoidable host-locator/handoff regression
СТАТУС: NON_AUTHORITATIVE_CONTINUITY_JOURNAL


## Эпизод: human-facing ответ началcя с machine summary вместо человеческого смысла

Симптом:
после технической проверки SIS выдал ОПЕРАТОРУ machine verdict, перечни PASS/FAIL, hashes, commits и technical boundaries раньше нормального объяснения того, что произошло и зачем это важно.

Это нарушает действующую approved-норму project core v2.5.

Fresh verified normative basis:
- `entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md`;
- status: approved;
- раздел `Человекочитаемый интерфейс проекта`;
- human-facing слой является обязательным первичным интерфейсом;
- сначала: `что произошло → почему это важно / что это означает → что теперь возможно, разрешено или требуется`;
- machine statuses, paths, commits, blobs, hashes и locators не являются основным человеческим текстом;
- human-facing terminal result не должен начинаться с технической служебной сводки, если она не является непосредственным предметом решения ОПЕРАТОРА.

Дополнительная current working directive:
`entities/koordinator/current/KOO__operator-facing-language-rule-v01.md`
требует русский основной текст, human-readable summary before service metadata и пояснение необходимых English technical terms.

Operational rule:
`HUMAN MEANING FIRST → CAUSAL CONTEXT → NEXT PRACTICAL CONSEQUENCE → ONLY THEN NECESSARY MACHINE EVIDENCE → ACTIVATION HANDOFF`.

Самоконтроль перед каждым terminal reply:
1. Можно ли понять результат, не читая machine verdict?
2. Объяснено ли, что изменилось по сути?
3. Объяснено ли, почему это важно для общей цепочки?
4. Понятно ли, что теперь можно/нужно делать?
5. Убраны ли ненужные hashes/statuses из основной прозы?
6. Если нужен другой чат, есть ли готовый АДРЕСАТ/PROMPT/ДЕЙСТВИЕ ОПЕРАТОРА?

