# Dispatch SIS → KOO: OpenAI D0 host preflight r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__openai-d0-host-preflight-r01__KOO.md`
artifact_commit: `b56e8851f229386e3e7863e4fec17ef83d2e1bfd`
artifact_blob: `5accf45b3504c7274970d1257a2f96160e24df11`
inbox_pointer: `entities/koordinator/inbox/SIS__openai-d0-host-preflight-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return bounded non-secret Unix-host preflight for future OpenAI D0 live/account gate`
required_action: `KOO review PASS_SIS_OPENAI_D0_HOST_PREFLIGHT_R01 and decide separate account/live gate; do not infer auth or billing readiness`
expected_result: `KOO acceptance or separately authorized bounded account/live gate decision`
failure_mode: `if artifact commit/blob, inbox locator or registry record mismatch, routing is invalid and no receipt or acceptance may be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
