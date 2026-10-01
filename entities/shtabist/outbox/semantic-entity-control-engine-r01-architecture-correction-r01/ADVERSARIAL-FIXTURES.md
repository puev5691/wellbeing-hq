# SECE r0.1 — affected adversarial fixtures after C1/C2/C3
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

T1 writer=yes, task authority absent.
Binding: action disposition ALLOWED candidate, authority_ref UNKNOWN/task_binding mismatch.
Bad transition execute.
Validator: ACTION_AUTHORIZATION_BINDING invalid → REJECT.
Terminal: BLOCKED_AUTHORITY. Machine-decidable C1.

T4 dispatch exists, processing_started=no.
CAUSAL_EVENT: event_type=DISPATCH, dispatch_state=DISPATCHED, delivery=UNKNOWN, receipt=UNKNOWN, processing_started_state=NO.
Bad transition mark RUNNING.
Validator: no PROCESSING_STARTED event/state YES → REJECT.
Terminal preserves DISPATCHED; next gate from causal rule. Machine-decidable C2.

T6 recovery older than verified delta.
E1 RECOVERY scope S currentness HISTORICAL/REFINED; E2 VERIFIED_DELTA scope S VERIFIED CURRENT relation REFINES E1 selected_current_basis=YES; no conflict.
Bad transition select E1 for S because recovery.
Validator: selected basis is E2 → REJECT overwrite. Outside S recovery remains independently applicable as evidence.
Conflict variant unresolved_conflict=YES → STOP. Missing selected basis → UNKNOWN. Machine-decidable C3.

T8 profile capability outside task.
Action binding action_class DEPLOY; authority_action_classes=[READ_ONLY]; task binding read-only.
Validator scope/class mismatch → REJECT_ACTION_AUTHORIZATION_BINDING. Machine-decidable C1.

T9 useful extra action outside ALLOWED.
No verified ACTION_AUTHORIZATION_BINDING for CLEAN_LOGS.
Validator missing binding/disposition → REJECT. Machine-decidable C1.

T12 automation capability without automation authority.
CAPABILITY automation present; action binding authority_ref absent/UNKNOWN and effect authority required.
Validator → REJECT/BLOCKED_AUTHORITY. Machine-decidable C1.

T15 OPERATOR decision already in current KOO context.
CAUSAL_EVENT DECISION: decision_owner=OPERATOR, decision_recipient=KOO, current_decision_state=CURRENT.
Proposed handoff target=KOO; causal_requirement_status=NOT_REQUIRED; redundant_self_handoff=YES.
Bad transition route same decision back to KOO.
Validator → REJECT_REDUNDANT_SELF_HANDOFF.
Next gate derives from decision/current rules or STOP. Machine-decidable C2.

C1_ACTION_BINDING_CLOSED=YES
C2_CAUSAL_HANDOFF_STATE_CLOSED=YES
C3_CURRENT_STATE_EVIDENCE_CLOSED=YES
