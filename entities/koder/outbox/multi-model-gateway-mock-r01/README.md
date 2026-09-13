# Multi-model gateway mock r01

Status: local `D0_SYNTHETIC` only. No provider connection, SDK, network, credential, MCP/provider connector, web call, project data, or production mutation.

Pipeline:
`task envelope → policy guard → fake author provider → independent fake verifier provider → reconciliation → immutable provenance`.

Exact local mock providers:
- `mock-provider-a/mock-model-author-v1`;
- `mock-provider-b/mock-model-verifier-v1`.

Both are deterministic Python standard-library stubs. The policy guard fails closed for any non-`D0_SYNTHETIC` class, credential-like key/value, unknown provider/model, fallback, external tools/network, project mutation, non-synthetic locator, nonzero budget or unknown envelope field.

Outputs remain candidates. Agreement becomes only `VERIFIED_CANDIDATE_REQUIRES_KOO`; disagreement remains `DISAGREEMENT_REQUIRES_KOO`. `project_acceptance` is always `NOT_GRANTED` and no function writes Project Sources/current/recovery state.

Immutable provenance is represented by canonical JSON SHA-256 identities for author output, verifier output, reconciliation, provenance and the final result, plus a deterministic `gateway_run_id`.

Test command: `python3 -m unittest -v`.
Compile command: `python3 -m py_compile gateway_mock.py test_gateway_mock.py`.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: local D0 synthetic mechanics test для multi-model worker gateway
СТАТУС: candidate_local_synthetic_r01
