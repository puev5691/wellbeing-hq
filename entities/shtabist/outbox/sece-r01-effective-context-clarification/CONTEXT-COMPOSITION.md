# SECE r0.1 Context Composition
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

Composition is conjunctive/compositional where compatible.

For each semantic line preserve:
atom_id; exact scope; semantic type; provenance; applicability; epistemic state; lifecycle state; authority/effect implications; dependencies.

Composition procedure:
1 collect applicable L1-L5 atoms/bindings;
2 normalize scope identities;
3 retain compatible lines in parallel;
4 detect typed collisions only where scopes/conditions overlap;
5 create bounded context corrections;
6 derive effective action/proposal/evidence spaces;
7 emit EFFECTIVE_CONTEXT.

Example:
MAY inspect + MUST_NOT mutate + UNKNOWN current consumer
=> inspect remains potentially allowed subject to its own gates;
mutate is forbidden;
consumer remains UNKNOWN;
evidence requirement remains active.
No winner is selected.

Profile, experience and capability may widen/narrow proposal/action candidates but cannot create authority.
Only valid authority bindings can make authority-sensitive actions executable candidates.

Context composition is NOT an effect decision and is NOT L7 MULTI_OUTCOME_AGGREGATION.
