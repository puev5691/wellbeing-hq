# Dispatch KOO → KOD: shard gateway adapter candidate r0.1

exchange_gate: v1
sender: koordinator
recipient: koder
artifact: entities/koordinator/outbox/KOO__shard-gateway-adapter-r01__KOD.md
artifact_commit: 1612ad05e5da265b4df1b67e5831ac644e555e56
artifact_blob: 3016ff782c4bb111ee3bc0611c8b553cf35670d8
purpose: prepare bounded non-deploying shard gateway adapter candidate from current SIS PASS
required_action: execute exact task under Resume-First; no historical replay
expected_result: PASS_KOD_SHARD_GATEWAY_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY or exact blocker/fail
failure_mode: if task identity, current writer or SIS basis mismatch, fail closed and do not infer authority
status: dispatched
project_time: omitted
