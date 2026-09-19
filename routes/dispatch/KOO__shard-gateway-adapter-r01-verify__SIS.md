# Dispatch KOO → SIS: shard gateway adapter r0.1 independent verify

exchange_gate: v1
sender: koordinator
recipient: sisadmin
artifact: entities/koordinator/outbox/KOO__shard-gateway-adapter-r01-verify__SIS.md
artifact_commit: c95f84ea0cc87383cb6274260a7be2263aafdcf9
artifact_blob: 2b67097824d61860f082cf7aaec1f186e3872547
purpose: independent non-deploying verification of exact KOD shard gateway adapter r0.1 after source-set activation
required_action: execute exact verification task under Resume-First using locator-first inputs
expected_result: PASS_SIS_SHARD_GATEWAY_ADAPTER_R01_INDEPENDENT_VERIFY or REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01 or exact blocker/fail
failure_mode: if task identity, candidate locator/identity, current writer, or active source-set state mismatch, stop and return exact blocker
status: dispatched
project_time: omitted
