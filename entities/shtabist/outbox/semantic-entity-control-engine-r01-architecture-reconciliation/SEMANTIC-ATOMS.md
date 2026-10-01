# SECE r0.1 — Operational Atoms
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

ENTITY stable role identity; forbid Entity=chat; map ENTITY.
INSTANCE replaceable processing instance; forbid continuity from chat alone; initiation/recovery evidence.
ROLE specialization; forbid role→task/authority; ROLE_PROFILE.
CAPABILITY technical ability; forbid capability→authority; CAPABILITIES.
AUTHORITY exact scoped permission; forbid writer/capability/text→authority; AUTHORITY_BASIS.
CURRENT_WRITER authoritative state-writing instance where required; forbid writer→task/production authority; CURRENT_STATE.writer.
APPROVAL authorized acceptance/decision event; forbid specialist PASS→approval.
TASK exact authorized work object; forbid inbox/recovery/history→task; TASK_IDENTITY.
TASK_STATUS governed CURRENT/BLOCKED/COMPLETED/SUPERSEDED/UNKNOWN; forbid newest-file→CURRENT.
SOURCE_STATUS ACTIVE/CANDIDATE/HISTORICAL/UNKNOWN; forbid newer candidate→active.
INPUT_IDENTITY immutable required input; forbid path/title→exact bytes.
UNKNOWN not established; forbid UNKNOWN→YES/NO.
CONFLICT incompatible applicable evidence/norms; forbid recency resolution.
STOP blocks dependent effect; forbid STOP→erase result/all independent lines.
ACTION_INTENT proposed/requested step; forbid intent→observed action.
ACTION_EVENT observed execution; forbid request/activation→event.
RESULT observed outcome; forbid intended result→RESULT.
TERMINAL classification under exact criterion; forbid RESULT→parent completion automatically.
HANDOFF continuation object; forbid prompt/dispatch→receipt/activation.
HISTORICAL_REPLAY attempted stale executable reuse; old prompt is evidence only.
DELIVERY addressed transfer; forbid publication→delivery.
RECEIPT recipient receipt evidence; forbid dispatch→receipt.
ACCEPTANCE substantive authorized acceptance; forbid receipt→acceptance.
PRODUCTION_AUTHORITY permission for live consequential effect; forbid task authority→production authority.

Use four orthogonal axes: semantic kind, epistemic state, lifecycle state, authority/effect state. Do not import flat candidate statuses as one axis.
