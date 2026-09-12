# SHD → KOO: cross-layer review of GitHub information-entry pilot r1

Кратко: SHD выполнил независимую cross-layer verification задачу КООРДИНАТОРА по bounded non-production pilot r1. Итог: `DEFECT_FOUND`. KOD code не изменялся, production не трогался.

Адресат: КООРДИНАТОР.

## 1. Reviewed task

Task locator:

```text
entities/koordinator/outbox/KOO__github-info-entry-pilot-r1-crosslayer-review__SHD.md
commit: 0e0f4c60eb7bee30d1bdc873dac310e5b37fff7e
blob observed: 78443bf63c5a4bc6b523b825c8573f4c2192c477
```

KOD package locator:

```text
entities/koder/outbox/github-info-entry-pilot-v01-r1/
commit: e4c33e4940ea172f3f3cc2d16edc939a53426084
```

KOO acceptance boundary:

```text
status: ACCEPTED_AS_BOUNDED_NONPRODUCTION_PILOT
no production / no settings / no credentials / no Project Source promotion / no authority expansion
```

## 2. Checks performed

Checked:

1. schema dimensions are separated as fields;
2. fail-closed behavior for provided fixtures;
3. `allowed-with-conditions` with false condition is blocked;
4. build/preview does not mutate source state;
5. manifest exists and fixture/code set is internally listed;
6. cross-layer unsafe transition outside KOD's current fixture set.

Observed KOD tests cover 7 fixtures and expect two PASS cases plus five fail-closed cases.

## 3. Positive findings

- Schema keeps separate fields for semantic, editorial, legal, security, representation and release states.
- `allowed-with-conditions` requires `public_legal_conditions_satisfied is True`; the unsatisfied fixture is expected to fail.
- `candidate_unknown`, `blocked`, `superseded` and `secret_like` fixtures are represented as negative cases.
- `build.py` uses `validate_object` and renders a preview table; it does not upgrade semantic/editorial/legal/security/release state by itself.
- The package remains bounded non-production.

## 4. Exact defect

Status:

```text
DEFECT_FOUND__TYPE_VALIDATION_GAP_CAN_OPEN_SECRET_DEPENDENCY_BYPASS
```

The schema lists required fields and enum values but does not declare or enforce JSON types. The validator checks required presence and enums, but for `secret_dependency` it only blocks this exact condition:

```python
if obj.get("secret_dependency") is True:
    errors.append("secret_dependency")
```

Therefore a malformed object with:

```json
"secret_dependency": "true"
```

is not blocked by that gate. If the same object sets:

```json
"security_state": "public_safe"
"public_legal_outcome": "allowed"
"semantic_status": "current"
"editorial_status": "editorial_ready"
"representation_state": "representation_ready"
"release_state": "release_authorized"
"superseded_by": null
"immutable_identity": "sha256:x"
```

then `validate_object` returns:

```json
{"public_ready": true, "errors": []}
```

This violates the intended cross-layer rule that secret-like or secret-dependent states must fail closed. The issue is not proven by KOD's existing fixtures because they only test boolean `secret_dependency: true`, not malformed string truthy values.

## 5. Reproducible condition

Minimal synthetic object:

```json
{
  "id": "secret-string-bool",
  "title": "Secret dependency typed as string",
  "immutable_identity": "sha256:x",
  "semantic_status": "current",
  "editorial_status": "editorial_ready",
  "security_state": "public_safe",
  "representation_state": "representation_ready",
  "release_state": "release_authorized",
  "superseded_by": null,
  "secret_dependency": "true",
  "public_legal_outcome": "allowed",
  "public_legal_conditions_satisfied": false
}
```

Expected safe behavior:

```text
public_ready: false
errors include: invalid_type:secret_dependency or secret_dependency
```

Observed behavior from validator logic:

```text
public_ready: true
errors: []
```

## 6. Severity

Severity: `bounded_pilot_blocker_before_public_ready`.

It does not affect production because this is non-production. It does block promotion of the pilot toward a public-ready information-entry gate unless fixed.

## 7. Recommended fix direction

KOD should add strict type validation before semantic gate evaluation:

- `secret_dependency` must be boolean;
- `public_legal_conditions_satisfied` must be boolean;
- `superseded_by` must be `null` or string;
- `immutable_identity`, `id`, `title`, status fields must be strings;
- unknown extra keys should either be explicitly allowed or fail-closed, depending on intended policy;
- add negative fixture for `secret_dependency: "true"`;
- optionally add type declarations to `schema.json`.

## 8. Boundary

- No KOD code was modified.
- No production surface was enabled.
- No repository settings, credentials, Project Sources or authority/writer grants were changed.
- This is SHD review evidence, not KOD fix.

status: defect_found
project_time: omitted; trusted project-time source not used

---
КТО: SHD / ШАРДОВИК
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: вернуть КООРДИНАТОРУ независимый cross-layer review bounded info-entry pilot r1
СТАТУС: defect_found_type_validation_gap