# G4 Sandbox Authority Model
status: DESIGN_CANDIDATE_NOT_AUTHORITY

Separate evidence required:
TASK_AUTHORITY: exact sandbox execution task.
TASK_CURRENTNESS: CURRENT, NOT_SUPERSEDED, conflict NONE.
ACTOR/WRITER: writer requirement explicitly REQUIRED or NOT_REQUIRED_FOR_TASK; current-writer evidence only when required.
ADAPTER_EFFECT_AUTHORITY: exact adapter class + effect class + target + attempt + operation limits.
SANDBOX_TARGET_AUTHORITY: exact ownership/permission to mutate disposable target.
CANDIDATE_BINDING: commit bb5b66644cd9e6421613e2c3f22d3299549ed374, tree 1158f63954c78bb6023e7a05e2e702c110a5203c, package path, relevant blobs.
PRODUCTION_AUTHORITY: ABSENT.

No field creates another authority class.

Task grounding requires exact task ref, authority basis, VERIFIED, CURRENT, supersession NONE/NOT_SUPERSEDED, immutable evidence identities/versions, provenance and conflict NONE. Else NO_EFFECT.

Writer/Recovery:
future G4 must declare whether effect is authoritative project-state mutation. For this proposed disposable external sandbox file class, preferred candidate writer_requirement=NOT_REQUIRED_FOR_TASK because it must not mutate authoritative project current-state; nevertheless actor instance, Recovery/freeze/handoff/replacement state must be exact and clear. This is design preference, not authority. If future governing rule says writer REQUIRED, G4 must require exact current writer.
