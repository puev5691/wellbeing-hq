# Provenance contract

Each successful candidate records:
- provider, model, adapter/transport version and exact endpoint;
- request hash and response hash;
- response ID and response status;
- normalized usage, preserving optional cached/reasoning details only when present;
- policy decision, D0 identity and synthetic input hash;
- credential source name only, never credential value;
- external-network-used, tools/search/files/computer/code/fallback/project-mutation/production flags;
- `project_acceptance=NOT_GRANTED`;
- provenance hash and final deterministic result identity.

Provider output is evidence/candidate data only. It cannot self-declare project acceptance, current state, canon state or authority.
