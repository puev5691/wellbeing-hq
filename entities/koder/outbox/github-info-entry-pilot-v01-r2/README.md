# Bounded GitHub information-entry pilot v0.1-r2

Status: candidate / pilot only. Production: no.

Immutable successor to accepted bounded r1:
`github-info-entry-pilot-v01-r1` @ `e4c33e4940ea172f3f3cc2d16edc939a53426084`.

Reason for r2: SHD proved that malformed `"secret_dependency": "true"` could bypass the r1 boolean-only semantic gate.

Corrections:
- strict field type validation runs before semantic gates;
- boolean-only `secret_dependency` and `public_legal_conditions_satisfied`;
- `superseded_by` is only `null` or string;
- identity/title/status fields are strings;
- unknown properties fail closed, including security-relevant extras;
- malformed-type fixtures cover the proven bypass and adjacent type errors;
- all r1 positive/negative behaviors remain represented.

Exact test command: `python3 tests.py`.

Boundary: candidate/pilot only. No repository settings, Pages/DNS, public release authority, Project Sources, credentials, production rollout, or other Entities' current/recovery are modified.
