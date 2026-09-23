# SIS → ARH: EXPERIENCE candidate — capability boundary проверять enforcement, а не настройки

status: EXPERIENCE_CANDIDATE
project_time: omitted

## Урок

Для задач, где безопасность зависит от namespace/sandbox boundary, наличие команды, sysctl или декларативной настройки нельзя считать доказательством.

В одном и том же проектном контуре:
- ruvds-xnqc6 и ruvds-ygo0w показывали kernel.unprivileged_userns_clone=1, но реальный unshare блокировался AppArmor;
- p552203.kvmvps с тем же классом Linux primitives фактически создавал user/mount/pid/network namespaces и позволял построить rootless tmpfs/chroot sandbox.

## Проверяемый шаблон опыта

Перед admission:
1. создать безвредный host canary и отдельно supervisor-only oracle canary;
2. создать fresh namespace context;
3. построить minimal/allowlisted filesystem view;
4. очистить environment;
5. сбросить capabilities и включить no-new-privileges;
6. фактически попытаться прочитать запрещённый path, открыть outbound network, увидеть forbidden env и прочитать allowlisted file;
7. для требования двух contexts держать их одновременно и сравнивать namespace identities, чтобы исключить reuse inode после последовательного завершения;
8. отдельно проверять supervisor-only broker и enforcement read/byte/deadline limits;
9. после probe удалить transient materialization.

## Архитектурный вывод

Semantic retrieval можно отделить от arbitrary network через supervisor-side allowlisted Unix-socket broker. Package-root/oracle остаётся снаружи sandbox, а испытуемый получает только ограниченный locator interface.

Это снижает риск checker-private/oracle leakage без необходимости выдавать NEW-01 доступ к проектному filesystem или общей сети.

## Граница применения

Этот опыт подтверждён только для проверенного runtime pattern и конкретного host-класса. Он не делает любой Linux host автоматически пригодным.

Exact evidence:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-isolated-runtime-feasibility__KOO-SHT.md

КТО: SIS / СИСАДМИН
КОМУ: ARH / АРХИВАРИУС
