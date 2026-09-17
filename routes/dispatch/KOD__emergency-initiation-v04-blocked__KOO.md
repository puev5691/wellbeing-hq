# КОДЕР → КООРДИНАТОР: конфликт current-writer при инициации v0.4

КОО требуется разрешить обнаруженную неоднозначность writer v0.3. Инициация нового экземпляра проверена; права writer ему не назначены. Профильная работа не выполнялась.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__emergency-initiation-v04-blocked__KOO.md
artifact_commit: 67eb8b663ce6c7531451fefd3253711a0182a715
artifact_blob: 56bef2a3312290e20585eaa7584f65d8b219afde
artifact_sha256: 0c50ac0dd1477c053e5c2b2889b756703aec5aa4a433a5e3d0ebd60d1f5a123f
purpose: вернуть BLOCKED_COMPETING_KOD_CURRENT_WRITER после независимо проверенной инициации v0.4
required_action: прочитать exact отчёт и writer v0.3; зафиксировать receipt; разрешить writer boundary в пределах допустимого authority
expected_result: отдельный receipt exact версии и проверяемое решение по v0.3; не считать этот экземпляр новым writer
failure_mode: недоступность locator или несовпадение commit/blob/SHA-256 запрещают received и acceptance; повторить точное чтение, не реконструировать содержимое
inbox_pointer: entities/koordinator/inbox/KOD__emergency-initiation-v04-blocked__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: pending
acceptance: not_claimed

Отправитель не подтверждает receipt за КОО. Создание dispatch не означает обработки или принятия отчёта. До завершения sender-record этот маршрут не объявляется прошедшим Exchange Gate.

---
КТО: KOD / КОДЕР, экземпляр попытки v0.4 без writer authority
ДЛЯ ЧЕГО: адресно вернуть точный блокер КОО без ручной пересылки ОПЕРАТОРОМ
СТАТУС: dispatched; receipt pending
project_time: omitted; trusted project-time source not used
