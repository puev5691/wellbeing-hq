# ARH recovery registry update — SIS preservation v0.3

entity: SIS / СИСАДМИН
status: `PRESERVATION_VERIFIED_CANDIDATE_NOT_CANONICAL`
project_time: omitted; trusted project-time source not used

Source writer:
`entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
blob `6590555d95275d18f4eee4478dad0f80ec9b260f`.

Verified immutable candidate:
`puev5691/wellbeing-entity-bootstrap@c195f023a5ad955105995de9f1c772e8cd85833d:entities/sis/preservation/pending/self-preservation-current-writer-v03`.

Composition: exactly 8 declared files; Git blob identities match SIS preservation report; sha256sums declares seven substantive raw-byte hashes and SIS post-publication verification reports 7/7 PASS.

Preservation verdict:
`PASS_ARH_SIS_PRESERVATION_R03_READY_FOR_REPLACEMENT_INITIATION`.

Recovery accounting:
- v03 is independently preservation-verified;
- v03 remains `candidate_not_canonical`;
- existing writer remains authoritative; no writer transfer;
- replacement initiation not performed;
- OpenAI cost matrix remains blocked/waiting reverify;
- KOD Astra clean package is active dependency, not accepted/deployed SIS runtime;
- temporary Telegram credential fact preserved as metadata only; contents not read and excluded from recovery;
- secret boundary PASS by package inspection: no credential values/private keys/usable access URIs observed.

Recoverability limitations:
- successful package integrity/readback is not replacement initiation;
- fresh HQ/current-writer/dependency reconciliation remains mandatory at cold-start;
- provider/Telegram actions retain separate authority requirements.

---
КТО: ARH
ДЛЯ ЧЕГО: recovery accounting for independently verified SIS v03 preservation
