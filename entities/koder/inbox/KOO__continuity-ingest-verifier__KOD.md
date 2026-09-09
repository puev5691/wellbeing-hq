# Входящее КОДЕРУ: Continuity v2 ingest verifier

artifact: `entities/koordinator/outbox/KOO__continuity-ingest-verifier__KOD.md`
artifact_commit: `61a60948edf0cf58e0e2003a279ef4de17dfc5be`
purpose: получить детерминированный verifier для byte/schema/content mismatch в Continuity v2 JSONL
required_action: прочитать exact task, выполнить в указанной диагностической границе, вернуть standalone tool + tests + report КООРДИНАТОРУ
failure_mode: locator/version недоступны или задача выходит за безопасную read-only диагностическую границу

exchange_gate: v1
sender: koordinator
recipient: koder
status: dispatched
project_time: omitted; trusted project-time source not used
