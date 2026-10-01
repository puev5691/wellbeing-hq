# SECE r0.1 — Source Rule Mapping C1/C2/C3 correction
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
predecessor_blob: 1fd08c68c3b907d9962cf828a72897730a3fa3e4

Existing rule representation unchanged. Add deterministic binding output:

COMPILED_RULE_BINDING:
compiled_rule_id
rule_type
source_locator
source_version_blob
semantic_basis
source_active_status
rule_scope
required_authority_class
required_task_binding
writer_requirement
effect_authority_requirement
conflict_status

ACTION_AUTHORIZATION_BINDING must reference one verified COMPILED_RULE_BINDING plus exact authority/current task conditions.

No join-by-convention across unrelated arrays is allowed.

Causal rules compile separately:
DISPATCH MUST_NOT imply DELIVERY/RECEIPT/PROCESSING_STARTED.
RECEIPT MUST_NOT imply ACCEPTANCE.
ACTIVATION_ATTEMPT MUST_NOT imply PROCESSING_STARTED.
REDUNDANT_SELF_HANDOFF STOP_IF current decision already resides with proposed target and no new causal gate requires handoff.

Current-state rules:
RECOVERY MUST_NOT automatically outrank VERIFIED_DELTA.
CURRENT_BASIS REQUIRES exact scope + verified evidence relation.
STOP_IF applicable unresolved evidence conflict.
UNKNOWN if required current basis absent.
