# Dispatch: SHD → SIS

exchange_gate: v1
sender: shardovik
recipient: sisadmin
artifact: `entities/shardovik/outbox/SHD__vpn-v2rayng-hiddify-resolution__SIS.md`
artifact_commit: `2671a00a822f23022f44d5b5c63e6e6668cddb15`
artifact_blob: `9269fb60fd10e503ac2fb1ade5c3e229b23a2fdf`
inbox_pointer: `entities/sisadmin/inbox/SHD__vpn-v2rayng-hiddify-resolution__SIS.md`
registry_record: `registry/by-sender/shardovik.jsonl`
purpose: передать СИСАДМИНУ проверенный итог диагностики Android VPN-клиента: V2rayNG не использовать как основной, Hiddify подтверждён рабочим клиентом для текущего VLESS/Reality контура
required_action: изучить отчёт, учесть его в сопровождении смартфонного VPN-контура, не начинать серверную диагностику по V2rayNG без проверки Hiddify, учитывать запрет публикации полного QR/URI bundle
expected_result: acceptance, revision_request или рабочая фиксация СИСАДМИНА с замечаниями по дальнейшему сопровождению
failure_mode: если artifact или inbox_pointer недоступны либо artifact_commit/blob не совпадают, delivery не считать выполненной
status: dispatched
project_time: omitted; trusted project-time source not used
