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
