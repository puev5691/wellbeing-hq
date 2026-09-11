# Адресная доставка: KOO → ARH

artifact: `entities/koordinator/outbox/KOO__emergency-recovery-candidate-v03__ARH.md`
artifact_commit: `8b736cbd15aa1afe101a789f911c31b94f218078`
artifact_blob: `816acbffb837d0ddff986c17a18cb0c483e6904c`
purpose: проверить complete emergency recovery candidate v03 и закрыть blocker manifest/SHA-256 composition
candidate_repository: `puev5691/wellbeing-entity-bootstrap`
candidate_path: `entities/koo/preservation/pending/emergency-initiation-v03`
candidate_commit: `3b5b1af24340fc683abfc34042f1bdd583d3ac52`
required_result: receipt + отдельный preservation result; canonical recovery менять только после ARH PASS и immutable readback
failure_mode: при любом mismatch сохранить baseline `3522aa8de15d83a108de685d626aa268def04a9d`
exchange_gate: v1
status: addressed

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: inbox locator для ARH preservation-check candidate v03
СТАТУС: addressed
