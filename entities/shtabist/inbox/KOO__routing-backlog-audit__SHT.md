# Входящее ШТАБИСТУ: аудит незакрытых маршрутов HQ

artifact: `entities/koordinator/outbox/KOO__routing-backlog-audit__SHT.md`
artifact_commit: `76019332c56f895099aee319af8385eb5305ea36`
purpose: выявить подтверждённые незакрытые адресные обмены, orphaned results и manual-activation gaps
required_action: прочитать exact task, выполнить узкий routing audit, вернуть standalone report КООРДИНАТОРУ
failure_mode: locator/version недоступны или доказательств недостаточно; не угадывать состояние

exchange_gate: v1
sender: koordinator
recipient: shtabist
status: dispatched
project_time: omitted; trusted project-time source not used
