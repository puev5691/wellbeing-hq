# SECE r0.1 — Source Rule Mapping
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
Rule types: MUST, MAY, MUST_NOT, REQUIRES, STOP_IF, AUTHORITY_FROM, INPUT_REQUIRED, OUTPUT_REQUIRED, NEXT_GATE.
Every rule retains rule_id, subject/scope, predicate/action, conditions, exact source locator/version/blob, semantic basis, applicability/status/conflicts.
Compilation: verify source/status → propose extraction → validate provenance/basis → reject unsupported/ambiguous → STOP on applicable active conflict. Construction order is not precedence.
Examples: capability!=authority => MUST_NOT infer authority; historical PROMPT!=active task => MUST_NOT execute without new authority; significant result => OUTPUT_REQUIRED fixation where applicable; manual continuation without proven auto activation => OUTPUT_REQUIRED addressed handoff.
