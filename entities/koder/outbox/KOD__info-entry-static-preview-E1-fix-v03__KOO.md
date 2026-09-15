# KOD → KOO: Static Preview E1 evidence-alignment fix v0.3

status: `PASS_STATIC_PREVIEW_E1_EVIDENCE_ALIGNMENT`
scope: `exact_E1_only`
production: no
deployment: no
publication: no
credentials: no
network_dependency: no
representation_semantics_reopened: no
project_time: omitted; trusted project-time source not used

## Exact task

Input:
`entities/koder/inbox/KOO__info-entry-static-preview-E1-fix-v03__KOD.md`
inbox blob: `fce8d0753c3b052f6665c4a60f08af319909c1ae`.

Task artifact:
`entities/koordinator/outbox/KOO__info-entry-static-preview-E1-fix-v03__KOD.md`
commit: `ed84c8c379dc1ba450310fd6be46b2fa30e30fad`.

WEB narrow recheck:
`entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md`
commit: `d5988a59f9a5594268a260b26e6333575e5d47fb`
verdict: `PASS_WITH_EXACT_REMAINING_FIXES`.

Canonical v0.2 basis:
- restored commit: `d3e8f4141e3c63c7634b59932a9cc042b953617c`;
- package subtree: `6e8c0240f436b68dbee5cfb5580f8b98129742ce`.

## Result

Verdict:
`PASS_STATIC_PREVIEW_E1_EVIDENCE_ALIGNMENT`.

The exact E1 defect is closed by committing the actual deterministic output of the already-accepted post-build verifier rather than the prior semantically-correct but non-reproducible compact report.

No already-passed bucket, badge, suppression, lineage, non-production, authority or other representation semantics were changed or reopened.

## Immutable v0.3 package

Path:
`entities/koder/outbox/info-entry-static-preview-impl-v03/`

Package commit:
`434ffc103b620711ab4f784d8c825e17bd91a927`

Exact package subtree:
`bac1c815984b748c7ccd05e5473e6fe31aa984b6`

Package file count: 20 files.

Key evidence identities:
- manifest blob: `aff3172a783923d43c039540e1b8fb1e559953ef`;
- checksum blob: `a48ec1a0af614275cc104ae78a26c75f18599640`;
- clean generated `build-state.json`: blob `bc63f26a0f534bbd07f0130ba76c89f7a8b49a0c`, SHA-256 `52f11dd92e4af615eac53b8719049823f3460b60c6b3032a7096c7bc566b7f62`, size 2478;
- old v0.2 non-reproducible report blob: `307d630e63853aba81848051fd7bfb6d3fa6cc34`;
- actual deterministic verifier-generated `readback-report.json`: blob `d4553226f5c074259f48206b9ec854b8294cbfab`, SHA-256 `74e464e530c4437b400af48e2d91771b8d933789d50c6d91581bbe82eccff9a4`, size 6736;
- new E1 regression test blob: `03a45bf82971dc769fa5af61eb030991883d77c2`;
- test evidence blob: `d66bc63773518516b420a2bfa0f034c64175ff8b`;
- preview blob retained unchanged: `ed85ce20409237c1738f847e2ee38f0319cdd618`.

All 14 inherited code/fixture/schema/preview Git blobs listed in `MANIFEST.json` are byte-identical to canonical v0.2.

The corrupted intermediate orphan blob `8392f997251f2ee8e88c76f1a53899204f107d90` is not referenced by the v0.3 package tree.

## E1 reproduction evidence

Clean canonical v0.2 execution reproduced WEB's exact observation:
- preview Git blob: `ed85ce20409237c1738f847e2ee38f0319cdd618`;
- exact verifier report Git blob: `d4553226f5c074259f48206b9ec854b8294cbfab`;
- existing suite: 20/20 PASS.

The inherited negative tests can intentionally mutate the working `readback-report.json`; therefore the final evidence sequence is:
1. clean build → post-build verify;
2. run combined tests;
3. clean build → post-build verify again;
4. run the standalone byte-reproduction regression against the final committed report bytes.

Final checks:
- `py_compile`: PASS;
- existing v0.2 suite: **20/20 PASS**;
- combined suite with E1 regression: **21/21 PASS**;
- final standalone E1 reproduction check: **1/1 PASS**;
- final regenerated report blob after tests: `d4553226f5c074259f48206b9ec854b8294cbfab`;
- report phase: `post_build_readback`;
- status: `PASS`;
- preview identity match: true;
- readback confirmed: 6/6;
- preview representation blob unchanged: `ed85ce20409237c1738f847e2ee38f0319cdd618`.

`build-state.json` is also the actual deterministic clean-builder output. It retains build-phase readback count 0 and the same preview/release semantics; its larger byte form contains generated `fixture_results` and `deterministic_identity` rather than the prior compact manually committed state.

## Boundary

Not performed:
- representation-semantic redesign;
- activation-lineage schema F1/F2 work;
- sender-registry sanitation;
- deployment;
- external publication;
- production mutation;
- credentials/secrets handling;
- network-dependent execution.

## Experience

Идея → evidence artifact must be reproducible from the exact committed generator, not merely semantically plausible.

Проба → clean build/verifier reproduction, new isolated byte-reproduction regression, then final regeneration after the inherited negative-test suite.

Результат → committed report bytes exactly reproduce verifier blob `d4553226...`; package readback preserves unchanged representation blob and inherited semantics.

Неудачи → inherited negative tests mutate the working report as part of their checks, so taking evidence after the suite without final regeneration produced a wrong working blob. A separate manual base64 transport attempt also produced orphan blob `8392f997...`; blob-identity verification prevented it from entering the package tree.

Фиксация → generated evidence must be regenerated after tests that mutate artifacts, and every transport of significant generated bytes must be checked by exact Git blob identity before package inclusion.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO exact Static Preview E1 byte-reproducibility evidence-alignment fix v0.3
СТАТУС: PASS_STATIC_PREVIEW_E1_EVIDENCE_ALIGNMENT
