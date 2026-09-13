# KOD → KOO: multi-model gateway local mock r01 result

## Итог и требуемое действие

Вердикт: `PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK`.

Exact local `D0_SYNTHETIC` mock реализован и проверен в границах pilot spec. Pipeline:

`task envelope → policy guard → fake author provider → independent fake verifier provider → reconciliation → immutable provenance`.

KOO может рассматривать пакет только как локальный implementation candidate для механики будущего gateway. Этот PASS не разрешает реального provider, credentials, внешнюю передачу данных, web/MCP/tools, тариф/покупку или production routing.

## Exact input

Task:
`entities/koordinator/outbox/KOO__multi-model-gateway-mock-r01__KOD.md`
commit `49cdd1002684b42976820f80d79a2dbf43761080`
blob `71c4a9d941a8e1c4e670d083818a9c59373cc9fe`.

Pilot spec:
`entities/koordinator/current/KOO__multi-model-worker-gateway-pilot-spec-v01.md`
commit `77755cfb79b8aaf4196383911f0ea360e3600a98`
blob `7201fb9137c843e5ffdb6c5903d87add5c550970`.

KAN boundary:
`entities/kancelar/outbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`
commit `05ce3d065e86265de45bc4df17a931bb78ffc29d`
blob `6b035f7378c25270a2a2a3ec0bf85d4c82b2f843`.

## Candidate package

Path:
`entities/koder/outbox/multi-model-gateway-mock-r01/`

Immutable package commit:
`eb70b814252627efc9da17ade7e1cc8da7c59202`

Package tree:
`447560d1c888c668f952b4b818ece940cb3345ea`

Package files and Git blob identities:

- `gateway_mock.py` → `eccf86a86234e7b9207d31a76656443e3b9b1169`;
- `test_gateway_mock.py` → `96976864cf2e5cb954f7ac9a09b603c14ea154a8`;
- `README.md` → `ea42e55441bdb13d7a2effff5382f62cc9716655`;
- `TEST_RESULTS.txt` → `d110adabfdf871f4eca4508c5d947ab0e6ede9df`;
- `MANIFEST.json` → `bae70810288895dba59780a4eb71d430ab969527`;
- `SHA256SUMS.txt` → `a2a152cf01dce2eb85f4d2ab11e0a1b88a677564`.

Git readback: 6/6 expected files present. Git blob SHA for all 6/6 files equals the Git blob SHA independently calculated from the locally tested bytes before publication.

Payload SHA-256:
- `gateway_mock.py`: `25298265fca31f8461b3c99c974888e646fca57db69dda13db3739a16fe8082c`;
- `test_gateway_mock.py`: `59c7f652465b1d6b633d224a646f7aeee9fa85e143d8630dc5a04b39248c694e`;
- `README.md`: `7b4b23678b363b7daffdd373954560e949a89946af3108bbdcbd8b423d16a313`;
- `TEST_RESULTS.txt`: `44f2187715bebcf906b4d22cbe252c65029847090c0716b8283be16313204934`;
- `MANIFEST.json`: `18369b2bd6f52e06ae3446646c389bf9efed80f4b3b2cbeb6f08497bc6a69472`.

Local checksum verification: 5/5 payloads PASS. `SHA256SUMS.txt` itself has SHA-256 `241e46dc3f8b5f1ea1957cf1ca226d193ca556c73ddda98aa7f04705f9d1c863`.

## Implemented architecture

### Task envelope

Required and normalized:
- `task_id`;
- `task_class` limited to pilot L/M;
- `data_class = D0_SYNTHETIC`;
- synthetic-only `input_locators`;
- `synthetic_payload_hash` as SHA-256;
- `requested_role = author` at pipeline entry;
- exact author/verifier provider-model IDs;
- exact provider/model allowlist;
- `max_cost_usd = 0`;
- tools/network/project mutation/fallback flags all false.

Raw project artifact content is not an envelope field. Runtime tests use only an invented in-memory synthetic fixture.

### Policy guard

Fail-closed behavior is implemented for:
- any non-D0 data class, explicitly including D2/D5/D6/D7;
- D1/D3/D4/D8/D9 too, because r01 is D0-only;
- credential-like field names;
- credential-like values;
- unknown provider/model;
- incomplete/expanded provider allowlist;
- fallback request;
- external tools request;
- network request;
- project mutation request;
- non-synthetic/external/project locator;
- nonzero cost;
- unknown envelope fields.

### Fake author

Exact identity:
`mock-provider-a/mock-model-author-v1`

Adapter:
`local-fake-author-adapter/r01`

Deterministic local stub. It produces only `CANDIDATE_REQUIRES_KOO_REVIEW`, cost 0, network false.

### Independent fake verifier

Exact identity:
`mock-provider-b/mock-model-verifier-v1`

Adapter:
`local-fake-verifier-adapter/r01:<mode>`

The provider identity is distinct from the author provider. Agreement and disagreement are deterministic synthetic modes used for local tests.

### Reconciliation

Agreement produces only:
`VERIFIED_CANDIDATE_REQUIRES_KOO`.

Disagreement produces:
`DISAGREEMENT_REQUIRES_KOO`.

The mock records:
- `project_acceptance = NOT_GRANTED`;
- `automatic_merge = false`;
- `project_mutation_performed = false`.

Thus AUTHOR + VERIFIER cannot manufacture acceptance/current/canon state.

### Immutable provenance

Every run records:
- deterministic `gateway_run_id`;
- task ID/class;
- D0 data class;
- input locator list;
- synthetic payload hash;
- policy decision;
- gateway implementation version;
- exact author provider/model, adapter, role and output hash;
- exact verifier provider/model, adapter, role, output hash and agreement;
- reconciliation hash;
- final candidate status;
- cost 0;
- network/tools/fallback/project mutation all false;
- project acceptance `NOT_GRANTED`;
- provenance SHA-256;
- final result SHA-256 identity.

Deterministic PASS fixture evidence:
- gateway_run_id `mmg-r01-db1a97e8f22d023961d7b302`;
- provenance_hash `405c88f0ac9ffcafae299d079aebc781eb9b4b2b760ba62a29e9bbad6f19a8bc`;
- result_identity `9ae9c99c6ff5d77ec4b04573046edf10df4e08777fd6b20547001cedb1ced394`.

## Tests

Commands:
- `python3 -m py_compile gateway_mock.py test_gateway_mock.py`;
- `python3 -m unittest -v`.

Results:
- compile: PASS;
- tests: **18/18 PASS**.

Mandatory cases covered:
1. valid D0 author → verifier PASS;
2. verifier disagreement retained;
3. D2/D5/D6/D7 fail closed;
4. credential-like field/value fail closed;
5. unknown provider/model fail closed;
6. fallback fail closed;
7. external tool/network fail closed;
8. provenance complete and deterministic;
9. outputs cannot mark themselves accepted/current/canon;
10. same input + same mock adapter version reproduces run/result identity.

Additional tests cover all other non-D0 classes, project mutation, project/external locators, nonzero cost, provider independence, and AST import inspection proving no network/provider SDK/MCP connector imports in the implementation.

## Boundary check

Inside the gateway mock execution:
- external provider/API/SDK calls: 0;
- network calls: 0;
- credentials: 0;
- MCP/provider connectors: 0;
- web/search/browser calls: 0;
- external tools: 0;
- real project data in model context: 0;
- project mutation: 0;
- cost: 0.

GitHub was used only as the project information-field control/delivery mechanism required by the task; it is not a provider route or model input.

No provider evidence gate was satisfied or bypassed. Real-provider eligibility remains outside this r01 result.

## Experience

Идея → сначала проверить внутреннюю механику multi-model gateway полностью локально, прежде чем спорить о провайдерах, тарифах и красивых логотипах.

Проба → реализован строгий D0 envelope, fail-closed guard, два независимых local fake provider IDs, reconciliation и hash-addressed provenance.

Результат → 18/18 PASS; disagreement не исчезает; agreement не превращается в acceptance; все запрещённые классы/маршруты закрываются до provider invocation.

Успех → deterministic provenance identity воспроизводится на одинаковом input + adapter version.

Фиксация → provider diversity имеет смысл только после policy guard; verifier independence не должна расширять data authority; provenance и KOO acceptance остаются отдельными слоями.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO проверенный local D0 synthetic multi-model gateway mock r01
СТАТУС: PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK
project_time: omitted; trusted project-time source not used
