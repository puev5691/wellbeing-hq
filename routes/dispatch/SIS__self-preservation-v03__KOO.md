# Dispatch SIS → KOO: self-preservation v03

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__self-preservation-v03__ARH-KOO.md`
artifact_commit: `318032c4185c46cabce288cf6abe86ec051de819`
artifact_blob: `ec95d69926f18e2c391e3266401ba51600a970c2`
inbox_pointer: `entities/koordinator/inbox/SIS__self-preservation-v03__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `planned SIS re-initiation preservation checkpoint`
required_action: `record checkpoint and coordinate writer handoff only after ARH preservation verification`
expected_result: `coordination decision / handoff gate`
failure_mode: `if artifact identity, external recovery locator or required version cannot be verified, do not infer receipt/acceptance/handoff`
status: `dispatched`
project_time: omitted
