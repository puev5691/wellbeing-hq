# R03 correction map

Regression:
R05 proved all required R02 runtime gates except NEXT_GATE_RESOLVER_GROUNDING_FIXED. The failing direct C7 test constructed a legacy incomplete NEXT_GATE_RULE while the newer D1 typed rule contract requires conflict_status and supersession_state.

Selected interpretation: A.

Correction:
- sece_simulator.py: UNCHANGED.
- d1d2_tests.py: UNCHANGED.
- correction_tests.py: direct C7 grounded rule updated to complete normalized typed shape.
- added direct negative checks for conflicted rule and incomplete rule.
- superseded direct rule explicitly carries supersession_state=SUPERSEDED.

Preserved:
- D1 conflict/supersession enforcement;
- malformed/incomplete rule cannot route;
- D2 correction;
- all reviewed inputs and core implementation bytes;
- NOT_ACTIVATED and no-side-effect boundaries.