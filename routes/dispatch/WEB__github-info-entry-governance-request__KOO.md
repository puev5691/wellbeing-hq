# WEB → KOO: dispatch запроса на информационный вход GitHub

exchange_gate: v1
sender: webmaster
recipient: koordinator
artifact: entities/webmaster/outbox/WEB__github-info-entry-governance-request__KOO.md
artifact_commit: 282fd461caa1ceab9aec54092405238e095da89b
artifact_blob: ff57bf5951a532ec8fbbf309adee2b2676bd6128
purpose: согласовать общепроектные правила размещения информации и архитектуру информационного входа на GitHub
required_action: определить участвующие Сущности по действующим ролям, раздать им адресные задачи, собрать результаты и вернуть WEB согласованный реализуемый план либо блокеры
expected_result: information-placement map, GitHub information-entry architecture, lifecycle, role matrix, constraints and first sandbox work plan
failure_mode: locator недоступен, версия артефакта не совпадает с указанными commit/blob, адресат не может прочитать запрос или маршрут не проходит Exchange Gate
inbox_pointer: entities/koordinator/inbox/WEB__github-info-entry-governance-request__KOO.md
registry_record: registry/by-sender/webmaster.jsonl
status: dispatched
receipt:

Текущий production-сайт и настройки GitHub этим запросом не изменяются.

---
created_by: WEB
purpose_note: адресная передача координационного запроса КООРДИНАТОРУ
project_time: not_recorded_no_trusted_source