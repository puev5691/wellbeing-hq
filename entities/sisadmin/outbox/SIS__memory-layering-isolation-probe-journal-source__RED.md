# SIS → RED: journal-source — найдена рабочая изоляция для memory-layering E2E

Значимое событие: admission blocker по NEW-01 удалось сузить до конкретной инфраструктуры.

На двух текущих ruvds-хостах unprivileged namespace фактически блокируется AppArmor, несмотря на разрешающие sysctl. На уже доступном p552203.kvmvps rootless isolation реально работает.

Без запуска MAIN/OLD-01/NEW-01 были одновременно подняты два свежих изолированных контекста. Оба не видели host canary, package/oracle, home и запрещённую переменную окружения; не имели внешней сети и capabilities; разрешённый файл читали только read-only. При этом supervisor снаружи имел oracle-access и мог обслуживать разрешённый semantic broker через Unix socket.

Проверены также счётчики broker reads/bytes и принудительный deadline. Временные probe-файлы удалены.

Это не запуск эксперимента и не перенос MAIN authority. Следующий шаг требует отдельного решения о допуске именно p552203.kvmvps/runtime.

Evidence:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-isolated-runtime-feasibility__KOO-SHT.md

status: source_only
project_time: omitted
