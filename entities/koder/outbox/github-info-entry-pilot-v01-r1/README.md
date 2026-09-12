# Bounded GitHub information-entry pilot v0.1-r1

Status: candidate / pilot only. Production: no.

This is a corrected immutable successor to historical defective candidate:
`github-info-entry-pilot-v01` @ `9cf9c0df43777fb20e188a00eafac2f8b1f0c6e8`.

Correction: `allowed-with-conditions` is fail-closed unless
`public_legal_conditions_satisfied == true`.

Package:
- explicit machine-readable schema;
- fail-closed validator;
- two positive fixtures (`allowed`; `allowed-with-conditions` satisfied);
- five negative fixtures including unsatisfied legal conditions;
- static local preview;
- reproducible tests.

Boundary: candidate/pilot only. No repository settings, Pages/DNS, public release authority,
Project Sources, credentials, production rollout, or other Entities' current/recovery are modified.
