# SECE r0.1 D1+D2 C7 grounding regression correction successor R03
Status: OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

Predecessor: b32c3bdefa01c036e78a9e4d60fc2a78fd86418c / tree 7807b3f5d43fe62b344f8ab6f6947aea98e33af7.

Selected contract interpretation: A.
The D1 typed NEXT_GATE_RULE shape requires conflict_status and supersession_state before resolver consumption. Missing fields are malformed, not neutral. The resolver is intentionally unchanged.

R03 changes only the direct C7 correction test and package evidence/metadata:
- the grounded direct unit uses the complete normalized typed rule shape;
- conflicted and superseded rules remain non-routable;
- a rule missing conflict_status remains non-routable;
- D1 end-to-end and D2 implementation bytes are preserved unchanged from predecessor.

Candidate is not activated. No external execution/review is authorized by this package.