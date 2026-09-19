# Dispatch KOO → KOO: source rebuild r0.3 bounded correction

exchange_gate: v1
sender: koordinator
recipient: koordinator
artifact: entities/koordinator/outbox/KOO__source-rebuild-r03-correction__KOO.md
artifact_commit: b7831b95ffcdffe71c090c4b8fd77d620d004d46
artifact_blob: 98bdd0c56cf017f238aabf76be91070b757e3e6a
purpose: execute bounded candidate integration for SHT D1-D3 in existing source-rebuild lineage
required_action: on next Resume-First cycle, execute exact correction task only; do not approve/activate sources or close OPERATOR gates
expected_result: new r0.3 candidate package identity and routing to next required review
failure_mode: if r0.2 package identity, SHT result identity, current writer, or open gate status differs, stop and fresh-reconcile before editing
status: dispatched
project_time: omitted
