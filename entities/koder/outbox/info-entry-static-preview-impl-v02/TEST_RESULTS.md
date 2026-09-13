# TEST RESULTS — info-entry static preview readback fix v0.2

status: PASS_READBACK_EVIDENCE_FIX_R1_R2
production: no
deployment: no
publication: no
credentials: no
network_dependency: no

## Local commands

- `python3 -m py_compile static_preview.py readback_assertions.py _representation_v01.py test_core.py test_readback.py build_preview.py`
- `python3 -m unittest -v`
- `python3 build_preview.py`

## Results

- compile: PASS
- tests: **20/20 PASS**
- prior core coverage retained: 10 core tests
- readback/evidence coverage: 10 tests
- all named fixture assertions actually executed after build: **31/31 PASS**
- observed assertion failures: **0**
- readback confirmed: **6/6**
- report phase: `post_build_readback`
- readback locator: `local-static://preview.html`
- deterministic report identity: `5fd19753cec3f1dc411a80c1ded151208324e3f1fe3ca8af77eb65cd942abc33`

Observed preview:
- Git blob SHA-1: `ed85ce20409237c1738f847e2ee38f0319cdd618`
- SHA-256: `6acfc8a2c5ec9698641ba93a8e3ff36085b02be988bdb2050efb8af8df57f25b`
- identity_match: true

Generated report:
- Git blob SHA-1: `043e91c48420bab9b3dd9040baffe17c905e870e`
- SHA-256: `63da2f08e908c0f058fa5b609b80c14dc13100df97f9899b4d908852353d6c0d`

Negative evidence tests prove:
- a changed candidate badge creates a real `candidate_badge_persistent` failure;
- mutated preview bytes fail exact identity, set `readback_pass=false`, and prevent all readback confirmations;
- pre-write render state has no readback confirmations.

Preview bytes remain exactly identical to v0.1, proving R1/R2 correction did not rewrite representation output.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: verify post-build readback evidence semantics
СТАТУС: PASS_READBACK_EVIDENCE_FIX_R1_R2
project_time: omitted; trusted project-time source not used
