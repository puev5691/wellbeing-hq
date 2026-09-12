# MANIFEST

status: corrected_candidate
production: no
provider: claude_managed_agents
runtime: python-3.12.3
third_party_dependencies: none
supersedes_for_integrity_only: `entities/koder/outbox/entity-runner-candidate-v01/` @ `425ad228d04674345796caa7989f93a9cee3c5a4`
historical_defect: previous manifest declared wrong SHA-256 for `runner.py`

## Files

- `README.md` sha256 `049b908ef1df8f2cd33fa3622271c69232ff54ecc1f4ad4f0876e502633af1c7`
- `runner.py` sha256 `b3175b720e731d9b08ee864979c4fb6a6413a8c6eaf02cc501c1824a24e832a3`
- `test_runner.py` sha256 `448d75cf23b259e7d49ced3292e5bfe274ef7b5e95a25ea94c98a8f86172832c`
- `requirements.txt` sha256 `d1d0779dfbe4ede0c215426a957594b9cfaacd2f312422a498d565b8d67cfc8d`

## Verification

- all declared SHA-256 values generated from exact final package bytes
- unit tests: 4/4 PASS
- validate-only: PASS, exit code 0
- provider/network side effects: none
- credentials handled: none
- implementation logic changed: no

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: corrected immutable package identity after KOO integrity return-for-fix
project_time: omitted; trusted project-time source not used
