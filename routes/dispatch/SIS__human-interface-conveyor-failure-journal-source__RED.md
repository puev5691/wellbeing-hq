# Dispatch: SIS → RED — human-interface conveyor failure journal-source

exchange_gate: v1
sender: sisadmin
recipient: redaktor
artifact: entities/sisadmin/outbox/SIS__human-interface-conveyor-failure-journal-source__RED.md
artifact_commit: 47663c535879920dec45af053469801835f9e89c
artifact_blob: 0a425545d4c5cfeccc307a981a6d4a7989fc783c
purpose: deliver human-readable journal-source about process/interface failure and recovered next-step handoff
required_action: editorial filter only; include/merge/defer/reject according to RED journal practice
failure_mode: if artifact locator or immutable identity mismatches, stop with exact blocker
inbox_pointer: entities/redaktor/inbox/SIS__human-interface-conveyor-failure-journal-source__RED.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
receipt:
project_time: omitted
