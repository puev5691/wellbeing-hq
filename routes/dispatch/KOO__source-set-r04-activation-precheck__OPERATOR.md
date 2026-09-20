# Dispatch KOO → OPERATOR: source-set r0.4 activation barrier precheck

exchange_gate: v1
sender: koordinator
recipient: operator
artifact: entities/koordinator/outbox/KOO__source-set-r04-activation-precheck__OPERATOR.md
artifact_commit: 964796fc0840876161a1aa0408198273fbff2c52
artifact_blob: b5ebbbdf6554cdc7801ae7d0df8b597ef3eb2681
purpose: report exact source-set activation barrier blocker and request one checksum-metadata resolution
required_action: OPERATOR selects actual Git blob SHA identities or requires KAN checksum-manifest correction
expected_result: explicit OPERATOR decision text
failure_mode: no partial source activation; core v2.2 and conveyor v1 remain active until complete barrier PASS
status: dispatched
project_time: omitted
