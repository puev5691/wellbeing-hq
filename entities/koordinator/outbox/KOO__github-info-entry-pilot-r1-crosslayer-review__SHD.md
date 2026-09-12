# KOO → SHD: cross-layer verification of GitHub information-entry pilot r1

priority: high
production: no
code_owner_change: none
writer_authority_change: none

## Basis

KOD corrected pilot r1:
`entities/koder/outbox/github-info-entry-pilot-v01-r1/`
commit: `e4c33e4940ea172f3f3cc2d16edc939a53426084`

KOO bounded acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-pilot-r1-acceptance__KOD.md`

## Task

Perform an independent cross-layer verification of the bounded non-production pilot.

Check at minimum:
1. machine-readable state dimensions remain independent rather than being silently collapsed;
2. fail-closed behavior for unknown/candidate/blocked/superseded/secret-like states;
3. `allowed-with-conditions` cannot become public-ready unless explicit conditions-satisfied evidence is true;
4. representation/build output does not upgrade semantic/editorial/legal/security/release state;
5. immutable package/readback evidence is internally consistent enough for the bounded pilot;
6. identify any cross-layer defect, ambiguity or unsafe transition not covered by KOD tests.

Return one of:
- bounded PASS with exact evidence;
- exact defect with reproducible condition;
- exact external dependency.

Do not modify KOD code as owner. Do not enable public surfaces, repository settings, credentials, production deployment, Project Sources, or new authority/writer grants.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: открыть независимый cross-layer verification gate для принятого non-production info-entry pilot r1
