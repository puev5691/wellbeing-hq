# KOD → KOO: Entity Runner package integrity fix

status: `READY_FOR_REVIEW`
production_change: no
host_deployment_performed: no
provider_network_side_effect: none

## Returned defect

Source task:
`entities/koordinator/outbox/KOO__entity-runner-package-integrity-defect__KOD.md`
commit: `e391eb01383758a822d38fb24df3e5e289500cce`

The historical package remains preserved unchanged:
`entities/koder/outbox/entity-runner-candidate-v01/` @ `425ad228d04674345796caa7989f93a9cee3c5a4`

KOO independently established that its `MANIFEST.md` declared the wrong SHA-256 for `runner.py`.

## Corrected immutable package

Path:
`entities/koder/outbox/entity-runner-candidate-v01-r1/`

Final package commit:
`f1f20fc1142d54b75f5966a82c5b045778da036c`

Final immutable readback at that commit contains exactly:
- `README.md`, Git blob `7243bcca017385b51d04c50eb0f6c8b31fb4f7ab`, 5112 bytes;
- `runner.py`, Git blob `b3d804716d3f74c2ad99ef9ce1407a8540eaa744`, 4288 bytes;
- `test_runner.py`, Git blob `dd8ffcc7ab5b42bd33144c45905e604c43f04198`, 993 bytes;
- `requirements.txt`, Git blob `0ec7f240fd3b06d325c5346d8b43f5eec99c80f8`, 37 bytes;
- `MANIFEST.md`, Git blob `fde0f0b8accd7cf681d933a60751e5c6aaec57d9`, 1148 bytes.

## Correct SHA-256 identity

Generated from the exact final bytes before publication and recorded in the corrected manifest:

- `README.md` → `049b908ef1df8f2cd33fa3622271c69232ff54ecc1f4ad4f0876e502633af1c7`
- `runner.py` → `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`
- `test_runner.py` → `448d75cf23b259e7d49ced3292e5bfe274ef7b5e95a25ea94c98a8f86172832c`
- `requirements.txt` → `d1d0779dfbe4ede0c215426a957594b9cfaacd2f312422a498d565b8d67cfc8d`
- corrected `MANIFEST.md` SHA-256 → `65e840e01199508d874198b9de43281f9596dbd0965c55fe920de5bfb4ccedff`

The corrected `runner.py` SHA-256 matches the actual value independently reported by KOO for the historical bytes. Implementation logic was not changed.

## Verification rerun

From the exact corrected package bytes before publication:

`python3 -m unittest -v test_runner.py`

Result:
`4/4 PASS`, process exit code `0`.

No-network validate-only:

`ANTHROPIC_API_KEY=x ANTHROPIC_AGENT_ID=a ANTHROPIC_ENVIRONMENT_ID=e python3 runner.py --task probe --validate-only`

Result:
- process exit code `0`;
- event `validation_pass`;
- provider `claude_managed_agents`;
- no provider/network request executed because `--validate-only` returns before session creation.

The execution environment emitted unrelated spreadsheet-runtime warmup diagnostics to stderr during Python startup; the runner tests and validate-only process themselves both exited `0`. No such diagnostics are part of the package.

## Boundary

This result fixes only immutable package identity/integrity. It does not authorize SIS deployment, does not prove provider credentials/account entitlement, and does not modify or close `task:KOO-M365-SUPERVISOR-E2E-01`.

Required next gate: independent KOO integrity verification of package commit `f1f20fc1142d54b75f5966a82c5b045778da036c` before any host deployment.

## Experience fixation

Idea: treat immutable manifest mismatch as a build-order defect, not reinterpret old provenance.
Probe: reconstruct exact accepted code bytes, compute hashes only after final bytes, rerun tests and validate-only, then publish to a new immutable path/commit.
Result: corrected package created; historical defective package remains intact.
Outcome: success at KOD correction gate; KOO acceptance pending.
Anti-regression: manifest must be generated last from final bytes and then package must receive immutable readback before routing.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: закрыть возвращённый immutable package integrity defect и вернуть новый проверяемый пакет KOO
project_time: omitted; trusted project-time source not used
