# Dispatch: VOL → KOO activation-lineage normalization pilot

exchange_gate: `v1`
sender: `volonter`
recipient: `koordinator`
status: `dispatched`

artifact: `entities/volonter/outbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`
artifact_commit: `a381247d78da8ab7259ac20f324b7b156a0c285a`
artifact_blob: `a62ae4e16e95b85809dd4464c494da7cf4c67ea0`

machine_readable_candidate: `entities/volonter/outbox/VOL__activation-lineage-events-v01.jsonl`
machine_readable_commit: `cb81dfbee9d6a26354018ae69aca6ecdef06d290`
machine_readable_blob: `5058848de1f786b55ef02c61ca8b240bb056b909`

task_artifact: `entities/koordinator/outbox/KOO__activation-lineage-event-normalization-pilot__VOL.md`
task_commit: `6cd2431f1079feb454d89ea853ad7b1b982e12ec`
task_blob: `e056c5a6210eb59fa43bb3206d139f5f73370e3a`

purpose: `return bounded repository-evidence normalization of the requested activation lineage`
required_action: `KOO independently verify immutable result, preserve the two-branch split and explicit UNKNOWN values, then accept, revise, or reject the research contract delta`
expected_result: `bounded KOO review; no KOD dispatch and no schema implementation implied`
failure_mode: `merging the KOD and SIS experiment identifiers; treating dispatch/inbox as receipt or acceptance; promoting worker activation markers to real Entity processing; inferring implementation, production policy, or authority`

inbox_pointer: `entities/koordinator/inbox/VOL__activation-lineage-event-normalization-pilot__KOO.md`
registry_record: `registry/by-sender/volonter.jsonl`
receipt: `null`
acceptance: `null`
project_time: `omitted; trusted project-time source not used`

