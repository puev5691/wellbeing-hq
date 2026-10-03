# Correction map
D1:
- typed next_gate_rules enter Effective Context with identity/provenance/currentness/conflict/supersession fields;
- context identity binds them;
- L6 projects only exact in-context rules;
- resolver requires verified event/result, current evidence, ACTIVE/CURRENT non-conflicted/non-superseded exact rule;
- dedicated tests cover grounded, missing, inactive, superseded, ambiguous and post-build metadata injection.

D2:
- SemanticStateMutationLayer converts field_code/from_state/to_state into facts/evidence/events before validators;
- transformation metadata is removed before core validation;
- StaticValidator and Simulator contain no transformation_type shortcut;
- anti-cheat includes mutation layer, CollisionDetector, StaticValidator and Simulator;
- M12 three-blocker meaning is retained with typed blocker-state facts.

SHD execution blocker: UNCHANGED_EXTERNAL_BLOCKER.