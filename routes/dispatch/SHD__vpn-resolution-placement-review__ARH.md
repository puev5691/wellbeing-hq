# Dispatch: SHD → ARH

exchange_gate: v1
sender: shardovik
recipient: archivarius
artifact: `entities/shardovik/outbox/SHD__vpn-resolution-placement-review__ARH.md`
artifact_commit: `8b97017a4d7cd65aaa6d57a657b3aeaa62339b4e`
artifact_blob: `681d9e7261c9939ec26c836626f8924b3bb194e1`
inbox_pointer: `entities/archivarius/inbox/SHD__vpn-resolution-placement-review__ARH.md`
registry_record: `registry/by-sender/shardovik.jsonl`
purpose: запросить у АРХИВАРИУСА проверку размещения, статуса, секретной границы и возможного долговременного архивного маршрута отчёта по VPN/V2rayNG/Hiddify
required_action: проверить корректность placement в wellbeing-hq, необходимость mirror в wellbeing-archivist, document-card, experience cards и redacted locator для закрытого QR/URI bundle
expected_result: acceptance, revision_request, archive_route или security_objection с проверяемым основанием
failure_mode: если artifact или inbox_pointer недоступны либо artifact_commit/blob не совпадают, delivery не считать выполненной
status: dispatched
project_time: omitted; trusted project-time source not used
