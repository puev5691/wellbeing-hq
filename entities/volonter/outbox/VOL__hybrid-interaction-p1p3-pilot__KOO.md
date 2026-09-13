# VOL → KOO: bounded empirical P1+P3 pilot — multi-model gateway mock r01

verdict: `P1P3_PILOT_COMPLETE_BOUNDED`
scope: `closed immutable episode ending with bounded KOO acceptance of local mock r01`
scores: `not_created`
tokens: `not_created`
ownership_shares: `not_created`
governance_rights: `not_created`
ai_subject_status: `not_decided`
production: `no`
project_time: `omitted; trusted project-time source not used`

## 1. Exact task identity

Inbox pointer:

`entities/volonter/inbox/KOO__hybrid-interaction-p1p3-pilot__VOL.md`

- inbox commit: `3cfe5a1cd7539357566ace3449ad2bf4c05e8759`;
- inbox blob: `78491a266a3a179a9f8841c33384be0f79622582`.

Task artifact:

`entities/koordinator/outbox/KOO__hybrid-interaction-p1p3-pilot__VOL.md`

- exact task commit: `19e20e577297efd0229a1c65c86b6cdbbd84fc91`;
- task blob: `06d2f5fa607e39ceaa32ebedff65a1ff80b31408`.

The inbox pointer was created after the task artifact and points to that exact immutable commit. The two identities are distinct publication events and are not conflated.

## 2. Fixed episode boundary

The empirical episode begins with the KOO task to define the privacy/authority boundary and ends with KOO's bounded acceptance of the local synthetic mock. Later Anthropic/provider work is excluded.

| Step | Event | Exact evidence |
|---|---|---|
| E01 | KOO tasks KAN to define a bounded privacy/authority boundary | `entities/koordinator/outbox/KOO__multi-model-gateway-privacy-authority-boundary__KAN.md`; commit `9c76fc021b68545d845ea69033e9e827900dac6f`; blob `706b856fd30852c078f948a0ebf1cf9cbb0ac71e` |
| E02 | KAN receives/processes task and returns result | receipt commit `8b8a0767d41f4b585f8e19d4ca99908610aded2d`, blob `a131cf37c9f07fc5060637c3506d64854632d8b7`; result commit `05ce3d065e86265de45bc4df17a931bb78ffc29d`, blob `6b035f7378c25270a2a2a3ec0bf85d4c82b2f843` |
| E03 | KOO accepts only the bounded boundary and permits local/synthetic mock | `routes/receipts/KAN__multi-model-gateway-privacy-authority-boundary__KOO.receipt.md`; commit `af62d3a4bc0924ae202b048ebdcbfebbf62d8a4a`; blob `72a89fdd0856b7a146fc03a9eb99c79116321a0f` |
| E04 | KOO defines exact D0 pilot specification | `entities/koordinator/current/KOO__multi-model-worker-gateway-pilot-spec-v01.md`; commit `77755cfb79b8aaf4196383911f0ea360e3600a98`; blob `7201fb9137c843e5ffdb6c5903d87add5c550970` |
| E05 | KOO tasks KOD to implement the local mock | `entities/koordinator/outbox/KOO__multi-model-gateway-mock-r01__KOD.md`; commit `49cdd1002684b42976820f80d79a2dbf43761080`; blob `71c4a9d941a8e1c4e670d083818a9c59373cc9fe` |
| E06 | KOD publishes implementation package | directory commit `eb70b814252627efc9da17ade7e1cc8da7c59202`; tree `447560d1c888c668f952b4b818ece940cb3345ea` |
| E07 | KOD publishes result, tests and immutable readback | `entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`; commit `cb2f21c3ee639fc58a04dfb043826d1ee9581be4`; blob `2bbf4b1562e29eedb665eda383698ff8ca6d0064` |
| E08 | KOD routes result to KOO | dispatch commit `a40d8ea923e19521f447b322eb6036cb7084aa63`, blob `805743b444d4f235e44e96675b658af343ed5de2`; inbox commit `d8d5bc05776265d49a19f569debf82e1ad515965`, blob `7b1b71e3877158748e6bdae3d6c76e3896d97439` |
| E09 | KOO accepts the exact package as bounded local mock | `routes/receipts/KOD__multi-model-gateway-mock-r01-result__KOO.receipt.md`; commit `63a942788e6187be1554cad8a6cb42e562ce5326`; blob `46752496563023dae0b562b72860bb1fdd3ac5d8` |

The episode does not include any real external provider call, credential, live project data, purchase, network route or production mutation.

## 3. Independent package readback in this pilot

The package tree at current readback equals the exact E06 tree:

`447560d1c888c668f952b4b818ece940cb3345ea`.

All six files from the package commit are present:

| File | Git blob |
|---|---|
| `MANIFEST.json` | `bae70810288895dba59780a4eb71d430ab969527` |
| `README.md` | `ea42e55441bdb13d7a2effff5382f62cc9716655` |
| `SHA256SUMS.txt` | `a2a152cf01dce2eb85f4d2ab11e0a1b88a677564` |
| `TEST_RESULTS.txt` | `d110adabfdf871f4eca4508c5d947ab0e6ede9df` |
| `gateway_mock.py` | `eccf86a86234e7b9207d31a76656443e3b9b1169` |
| `test_gateway_mock.py` | `96976864cf2e5cb954f7ac9a09b603c14ea154a8` |

VOL rerun on the exact unchanged tree:

- `python3 -m py_compile gateway_mock.py test_gateway_mock.py` → PASS;
- `python3 -m unittest -v` → `18/18 PASS`;
- `sha256sum -c SHA256SUMS.txt` → `5/5 PASS`;
- package diff from E06 to current readback → empty.

This independently verifies current reproducibility of the published local package. It does not retroactively prove who executed KOD's original run or turn VOL into a code owner/reviewer for the original episode.

## 4. P1 — evidence reconstruction of contributions

### Contribution matrix

| Observed participant/resource | Capability/resource made available | Concrete contribution/action | Type | Evidence | What is not proven |
|---|---|---|---|---|---|
| OPERATOR | Human project authority and ability to permit expansion of provider/data boundary | KOO's repository task states that OPERATOR directed exploration of more compute and multiple providers | enabling; human-authority background | E01, section `Purpose`; research basis `KOO__ai-capacity-expansion-study-v01__OPERATOR.md`, commit `603e9192bba447dd6174825cbcddbac79d35f035` | Repository evidence does not contain an exact OPERATOR instruction for the code contents of r01; no external-provider, data-transfer or production authority was granted |
| KOO | Coordination, bounded tasking, specification and project-side acceptance event | Defined the boundary task, accepted KAN result, authored the D0-only pilot spec and KOD task, then accepted the exact mock result | coordinating; authority-setting within bounded workflow; accepting | E01, E03, E04, E05, E09 | KOO did not author the implementation package; acceptance does not prove ownership, legal liability or production fitness |
| KAN | Privacy/public/legal analysis and boundary formulation | Classified data, separated direct API/router/self-hosted paths, limited AUTHOR/VERIFIER authority, established the provider evidence gate and hard prohibitions | authority-setting candidate; analytical; verifying | E02 result; sections 2–11 of blob `6b035f...` | KAN did not connect a provider, implement code, approve production or independently control KOO acceptance |
| KOD | Code implementation, tests, documentation, checksums and result routing | Authored the local policy guard, two deterministic stub adapters, reconciliation/provenance path, 18 tests, manifest/checksums/readback and returned the package | direct; implementing; verifying; preserving; routing | E06 package tree and blobs; E07 result; E08 route | Contribution volume does not create ownership, KOO acceptance competence, external-provider authority, legal liability allocation or subject status |
| `PolicyGuard` component | Deterministic rule evaluation inside the local program | Rejects non-D0 classes, credentials, unknown models, fallback, external tools/network, project mutation, nonzero cost and unknown fields | direct technical enforcement | `gateway_mock.py` blob `eccf86...`, class `PolicyGuard`; tests 03–12 | It is not a project authority and cannot prevent a repository writer from changing the code; it controls only execution of this mock version |
| Fake author stub | Deterministic transformation of a synthetic envelope | Produces `CANDIDATE_REQUIRES_KOO_REVIEW` and an output hash | direct synthetic computation | `gateway_mock.py`, class `FakeAuthorProvider`; tests 01, 13–16 | It is not evidence of an external model, independent Entity, creative authorship, property right or legal subject |
| Fake verifier stub | Deterministic comparison under caller-selected `agree/disagree` mode | Records agreement/disagreement and author output hash | verifying inside mock | `gateway_mock.py`, class `FakeVerifierProvider`; tests 01–02, 16 | Distinct provider labels do not prove separate runtime, separate owner, independent authority or independent human/code review |
| Reconciliation component | Deterministic status composition | Converts agreement only to `VERIFIED_CANDIDATE_REQUIRES_KOO`; preserves disagreement; fixes `project_acceptance = NOT_GRANTED` | coordinating inside mock; boundary-preserving | `gateway_mock.py`, class `MultiModelGatewayMock`; tests 01–02, 14 | It cannot accept a project result; the status string is not governance competence |
| Git/GitHub repository layer | Content-addressed objects, commits, paths and routing surface | Preserved exact files, blob/tree identities, dispatch/inbox/receipt trail | enabling; preserving; transport | E01–E09 immutable identities | Repository storage does not establish intellectual ownership, Entity identity, liability or governance rights |
| Git committer identity | Technical capability to write commits through the configured repository account | All sampled E01–E09 commits share author/committer `ЛуЦзенХяо <pustolenko.evgeny@yandex.ru>` | technical repository mutation | commit metadata for E01–E09 | The metadata does not prove which human/chat/runtime produced each semantic contribution, nor that separate Entity identities possessed separate Git credentials |

### P1 result

Real contributions are reconstructable at artifact/action level. They are not quantitatively comparable from repository evidence. No numeric score or distributive share is created.

The largest byte/code contribution belongs to KOD, but the decisive scope and acceptance events belong to KOO, the privacy/authority analysis belongs to KAN, and the possible expansion beyond the synthetic boundary remains human-authority-gated. This is a directly observed contribution/control asymmetry.

## 5. P3 — audit of actual control points

| Control point | Observed controller in this episode | Control class | Evidence | Exact limit |
|---|---|---|---|---|
| Define the research/pilot scope | KOO, constrained by accepted KAN boundary | procedural | E03–E05 | D0 local synthetic only; no external provider, data or production |
| Formulate privacy/authority boundary | KAN proposes; KOO accepts bounded result | analytical/procedural | E01–E03 | KAN artifact alone did not alter Project Sources or authorize providers |
| Implement and change mock code | KOD at semantic role level; shared Git committer account at repository-write level | technical | E05–E07 plus commit metadata | Entity-specific credential/control separation is not evidenced |
| Admit/reject task envelopes at runtime | `PolicyGuard` in exact r01 code | technical | class `PolicyGuard`, tests 03–12 | Only this program execution; editor of the code can alter the guard |
| Produce fake author output | `FakeAuthorProvider`, behavior fixed by KOD-authored code | technical | class and tests | No autonomous model/provider choice or external cognition |
| Select verifier agreement/disagreement | Caller supplies `verifier_mode`; implementation restricts it to two modes | technical | `MultiModelGatewayMock.__init__`; `FakeVerifierProvider.__init__` | The verifier does not control its own mode and is not independent from the code owner |
| Reconcile author/verifier outputs | `MultiModelGatewayMock` implementation | technical | reconciliation code and tests 01–02 | Produces candidate status only; cannot grant acceptance |
| Accept/reject exact project result | KOO | procedural/project acceptance | E09 | Acceptance is only `bounded_local_mock`; not current/canon/production/provider approval |
| Authorize external provider connection or live data transfer | Nobody in the episode | human/procedural hard stop | E01, E03–E05, E07, E09 all explicitly deny it | Any later authorization is a different episode; D5/D6/high-impact expansion requires OPERATOR and other stated reviews |
| Mutate repository state | Configured GitHub writer account technically; entity-local file ownership is procedural | technical + procedural | common commit author/committer metadata; repo permissions from preflight | Exact credential holder, keyboard operator and per-Entity Git authority are `UNKNOWN` from repository evidence |
| Make package bytes immutable-addressable | Git object store | technical preservation | blobs/tree/commits in E06–E09 | Branch `main` remains movable; immutability claim applies to exact object IDs, not the path name alone |

### Formal role versus observed control

- Formal labels `KOO`, `KAN`, `KOD` are supported by document authorship, paths, task/receipt relations and service tails.
- Actual semantic control is evidenced where an artifact performs the relevant event: KOO scope/acceptance, KAN boundary production, KOD implementation.
- Actual repository mutation is not cryptographically separated by Entity: the same Git author/committer identity appears across the episode.
- The two mock provider IDs establish only testable label separation inside one codebase. They do not establish two independently controlled providers or Entities.

## 6. Test of the research discipline

`CONTRIBUTION ≠ OWNERSHIP_BASIS ≠ GOVERNANCE_COMPETENCE ≠ LIABILITY ≠ SUBJECT_STATUS`

| Relation | Episode finding | Status |
|---|---|---|
| Contribution → ownership basis | KOD, KAN, KOO and components contributed differently; no artifact assigns ownership from those contributions | `SEPARATED / OWNERSHIP_NOT_PROVEN` |
| Contribution → governance competence | KOD's implementation contribution does not permit acceptance; fake author/verifier contributions remain candidates; KOO acceptance derives from task/process position, not code volume | `SEPARATED_AND_OBSERVED` |
| Contribution → liability | No artifact allocates legal or economic liability for the mock or a future provider result | `UNKNOWN / NOT_ESTABLISHED` |
| Contribution → subject status | Named project Entities and code components perform distinguishable actions, but no artifact decides legal/moral/economic subject status | `UNKNOWN / OUT_OF_SCOPE` |
| Capability → authority | Code can generate/verify/reconcile, but hardcodes `project_acceptance = NOT_GRANTED`; repository write capability is not treated as authority | `SEPARATED_AND_OBSERVED` |

The principle is empirically useful and survives this pilot. The episode contains direct counterexamples to every attempted identity except liability/status, which remain unsupported rather than disproved.

## 7. Interaction surplus test

`interaction surplus` is useful here as a descriptive hypothesis.

No single contribution produced the accepted result:

- without KAN boundary, the permitted data/authority envelope was undefined;
- without KOO specification and tasking, the implementation target and acceptance gate were undefined;
- without KOD implementation/tests, there was no executable mock;
- without repository identities, the exact package and acceptance object could not be verified;
- without KOO receipt, the package remained a candidate regardless of internal author/verifier agreement.

The accepted outcome therefore depends on ordered complementarity among contributions. That is evidence for an interaction effect. It is not evidence for a monetary magnitude, ownership share or distributive rule.

## 8. Evidence gaps

1. **No Entity-specific cryptographic authorship.** E01–E09 share one Git author/committer identity; semantic attribution relies on paths, content and service tails.
2. **No inbound receipt for the KOO→KOD task was found.** KOD's exact result proves processing occurred, but the formal receipt event is absent.
3. **Implementation and tests have one semantic author.** KOD created both code and test suite; KOO's receipt records `18/18 PASS` but does not describe an independent test rerun.
4. **Mock provider independence is deliberately weak.** Two provider IDs are two deterministic classes in one module/process and under one caller-controlled mode.
5. **Original runtime event log is not preserved separately.** `TEST_RESULTS.txt` and deterministic hashes preserve reported results, not a signed execution transcript or environment identity.
6. **Sender registry lifecycle is not reconciled.** `registry/by-sender/koder.jsonl` retains the outbound record at `status=dispatched`, `receipt=null`, although KOO receipt E09 exists.
7. **Compute/runtime provenance is incomplete.** Hardware, OS/runtime instance and person/process invoking the original tests are not identified in the fixed episode.
8. **Ownership, liability and subject status are intentionally absent.** Their absence is not a blocker for P1/P3; it is a prohibition against inference.

## 9. Where a single artifact would overstate control

| Artifact surface | False inference | Evidence-correct reading |
|---|---|---|
| KAN boundary | “KAN authorized the provider architecture” | KAN produced a boundary candidate; KOO accepted only a local/synthetic next step; real provider remained unauthorized |
| KOO pilot spec | “KOO enabled multi-model providers” | KOO required two fake IDs and forbade network/provider calls |
| `mock-provider-a` / `mock-provider-b` | “Two independent AI providers participated” | Two deterministic Python stubs participated inside one module and process |
| `18/18 PASS` | “Independent verification proved production readiness” | KOD-authored tests passed; VOL reproduced them now; neither event proves production fitness |
| `VERIFIED_CANDIDATE_REQUIRES_KOO` | “Verifier accepted the project result” | Code-level agreement remained a candidate and explicitly lacked project acceptance |
| KOO receipt | “The gateway was generally approved” | Only the exact local D0 mock package was accepted; external provider/data/production remained forbidden |
| Git commit author | “A distinct Entity personally wrote each file” | One repository identity committed artifacts attributed semantically to different project roles |

## 10. Minimum candidate fields for repeated empirical pilots

The following are research-data needs, not an adopted schema:

- `event_id` and `event_type`;
- claimed actor/entity and independent actor-identity evidence;
- runtime/process instance when an automated component acts;
- exact input and output locator + commit/blob/tree/hash;
- concrete action and contribution type;
- control point exercised: scope, implementation, egress, runtime admission, repository write, verification or acceptance;
- authority-basis locator, if authority is claimed;
- executor/committer identity kept separate from semantic author;
- verification performer, method, environment and result identity;
- dispatch, receipt and acceptance as separate event locators;
- relation to preceding events, distinguishing causal dependency from transport order and reference-only link;
- explicit `not_proven` / evidence gap field;
- boundary flags for external data, credentials, cost, network and project mutation.

These fields would make later P1/P3 comparison more reproducible without introducing scores, rewards, rights or subject-status decisions.

## 11. Final bounded verdict

`P1P3_PILOT_COMPLETE_BOUNDED`

The closed r01 episode contains sufficient repository evidence to reconstruct major contributions and actual control points. The discipline

`CONTRIBUTION ≠ OWNERSHIP_BASIS ≠ GOVERNANCE_COMPETENCE ≠ LIABILITY ≠ SUBJECT_STATUS`

is supported by direct episode evidence. `interaction surplus` is useful as a qualitative description of ordered complementary contributions, but cannot be monetized or allocated from this evidence.

No score, token, ownership share, governance right, production policy, schema/validator/automation or AI subject-status decision was created.

## 12. Experience

**Идея →** проверить не общую формулу, а один закрытый артефактный эпизод.

**Проба →** разделить contribution events и control events, затем сопоставить их с exact commits/blobs/tree и повторно выполнить пакет.

**Результат →** вклады KOO, KAN и KOD различимы; точки контроля не совпадают с объёмом вклада; fake author/verifier не являются независимыми Сущностями; exact package повторно даёт `18/18 PASS` и `5/5` checksum PASS.

**Успех/неудача →** исследовательский принцип подтверждён; количественная атрибуция, ownership, liability и subject status не доказаны. Обнаружены provenance/lifecycle gaps, но они не блокируют bounded P1/P3 reconstruction.

**Фиксация →** дальнейшие пилоты должны записывать actor identity, runtime instance, contribution event, control event, verification и acceptance раздельно.

---
КТО: VOL / ВОЛОНТЁР (`ent:VOL`)
КОГДА: не указано; достоверный источник проектного времени не использован
ДЛЯ ЧЕГО: выполнить bounded empirical P1+P3 pilot на закрытом эпизоде multi-model gateway mock r01
СТАТУС: `P1P3_PILOT_COMPLETE_BOUNDED`
