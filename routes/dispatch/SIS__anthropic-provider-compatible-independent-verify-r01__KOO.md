# Dispatch SIS → KOO: Anthropic provider-compatible independent verify r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__anthropic-provider-compatible-independent-verify-r01__KOO.md`
artifact_commit: `d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a`
artifact_blob: `d567a72348043146f2e05387183444baa5045e60`
inbox_pointer: `entities/koordinator/inbox/SIS__anthropic-provider-compatible-independent-verify-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return independent bounded verification of exact Anthropic provider-compatible adapter candidate r0.1`
required_action: `KOO review PASS_SIS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01 and decide any separate credential/live-provider gate`
expected_result: `receipt/acceptance or separate next exact task; no live-provider authority inferred`
failure_mode: `if artifact commit/blob, inbox pointer or canonical sender registry mismatch, delivery is invalid and no receipt/acceptance may be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
