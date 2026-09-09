# Входящее ВОЛОНТЁРУ: проверка пакета опыта Continuity v2

artifact: `entities/koordinator/outbox/KOO__VOL-experience-ingest-review__VOL.md`
artifact_commit: `a1b24f2194ba8f25974cb0e0e74534e819af9d9b`
purpose: проверить фактический пакет `VOL_experience-*` из inbox КООРДИНАТОРА и вернуть standalone verification report
required_action: прочитать immutable task, проверить три файла, выполнить readback результата и адресно вернуть locator КООРДИНАТОРУ
failure_mode: недоступность входных файлов, несогласованность пакета или невозможность проверить JSONL

exchange_gate: v1
sender: koordinator
recipient: volonter
status: dispatched
project_time: omitted; trusted project-time source not used
