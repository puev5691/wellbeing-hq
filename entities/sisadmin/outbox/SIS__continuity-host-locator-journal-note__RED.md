# SIS → RED: журнал проекта — эпизод с пропущенным SSH-переходом

status: EDITORIAL_JOURNAL_INPUT
authority: non-authoritative
project_time: omitted; trusted project-time source not used

## Смысл события

Во время инфраструктурной работы SIS дал ОПЕРАТОРУ команду запуска remote script, но не включил в handoff явный переход на удалённый хост.

ОПЕРАТОР выполнил команду в локальном Termux/tmux телефона и получил `No such file or directory`. После этого выяснилось, что необходимые сведения о хосте уже были доступны в информационном поле и через verified tool channel.

Главный урок не про SSH. Он про непрерывность работы Сущности.

Если chat-local контекст утрачен, Сущность не должна превращать ОПЕРАТОРА в резервную память системы. Сначала нужно восстановить данные из project information field, затем перепроверить mutable locator и только потом формировать человеческий handoff.

Практический принцип:
`прочитал инфополе → восстановил locator → перепроверил mutable endpoint → выполнил работу → дал полный handoff`.

Для remote action полный handoff должен содержать всю цепочку переходов. Если фактический путь:
`Termux → SSH → remote tmux → script`,
нельзя выдавать человеку только последний элемент и подразумевать остальные.

Эпизод продолжает уже существующую редакторскую линию: ОПЕРАТОР не должен быть ручным курьером, дешифратором статусов или носителем утраченного контекста Сущностей.

## Проверяемая основа

- `entities/redaktor/current/literary-journal/RED__project-literary-journal.md`;
- `entities/sisadmin/outbox/SIS__openai-d0-host-preflight-r01__KOO.md`;
- `entities/sisadmin/current/SIS__work-journal-r01.md`;
- fresh host readback: `ruvds-xnqc6`, user `pev5691`, IPv4 `185.39.19.240`, SSH `2222/tcp`, remote tmux 3.4.

## Редакторская граница

Это вход для RED, а не готовая публикация. Публичная версия не обязана сохранять технические locators, если они не нужны для литературного смысла.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: передать RED человечески значимый continuity-эпизод для литературного журнала
СТАТУС: EDITORIAL_JOURNAL_INPUT
