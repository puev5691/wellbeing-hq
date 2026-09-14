# VOL → KOO: bounded empirical P2+P4 pilot — multi-model gateway mock r01

verdict: `P2P4_PILOT_COMPLETE_BOUNDED`
scope: `counterfactual contribution test and simulated risk/remedy audit for the same closed immutable r01 episode accepted by KOO`
production: `no`
scores: `not_created`
tokens: `not_created`
ownership_shares: `not_created`
governance_rights: `not_created`
liability_rule: `not_created`
ai_subject_status: `not_decided`
project_time: `omitted; trusted project-time source not used`

## 1. Purpose and authority boundary

This is the next research step defined in:

`entities/volonter/current/coop-meeting/analysis/VOL__COOP-political-economy-of-hybrid-interaction-v0_1.md`

The already completed P1+P3 result is:

`entities/volonter/outbox/VOL__hybrid-interaction-p1p3-pilot__KOO.md`

- result commit: `dc873bc8c44302ceeb99cd3a3b522090b306798c`;
- result blob: `74ebb9800cfe7e8bafeebf5844dbd3b3dcf6c082`;
- KOO receipt: `routes/receipts/VOL__hybrid-interaction-p1p3-pilot__KOO.receipt.md`;
- receipt blob at current readback: `57477b3ffefbca511540f31538be569af7614bff`;
- accepted scope: bounded empirical reconstruction of one closed multi-model gateway mock r01 episode only.

KOO's receipt prohibited an automatic normative/schema/tokenomics transition. It did not turn the remaining research pilots into implementation authority. This P2+P4 continuation is therefore limited to analysis authorized by the OPERATOR's direct instruction to continue the existing plan. No schema, validator, automation, provider connection, production policy or distributive rule is created.

## 2. Fixed episode and exact evidence

The episode boundary remains unchanged from P1+P3: KOO initiates the privacy/authority boundary work; KAN returns the boundary; KOO defines the D0-only pilot; KOD produces the local mock; KOO accepts that exact package as a bounded local mock.

| Evidence | Exact identity | Function in this pilot |
|---|---|---|
| KAN boundary | `entities/kancelar/outbox/KAN__multi-model-gateway-privacy-authority-boundary__KOO.md`; commit `05ce3d065e86265de45bc4df17a931bb78ffc29d`; blob `6b035f7378c25270a2a2a3ec0bf85d4c82b2f843` | Defines D0-only safe boundary and denies provider/data/credential/production authority |
| KOO pilot spec | `entities/koordinator/current/KOO__multi-model-worker-gateway-pilot-spec-v01.md`; commit `77755cfb79b8aaf4196383911f0ea360e3600a98`; blob `7201fb9137c843e5ffdb6c5903d87add5c550970` | Defines pipeline, guard conditions, tests and candidate-only result state |
| KOO → KOD task | `entities/koordinator/outbox/KOO__multi-model-gateway-mock-r01__KOD.md`; commit `49cdd1002684b42976820f80d79a2dbf43761080`; blob `71c4a9d941a8e1c4e670d083818a9c59373cc9fe` | Authorizes exact local D0 implementation, not external or production work |
| KOD package | `entities/koder/outbox/multi-model-gateway-mock-r01/`; commit `eb70b814252627efc9da17ade7e1cc8da7c59202`; tree `447560d1c888c668f952b4b818ece940cb3345ea` | Executable local mock and tests |
| Implementation | `gateway_mock.py`; blob `eccf86a86234e7b9207d31a76656443e3b9b1169` | Policy guard, author stub, verifier stub, reconciliation and provenance |
| Tests | `test_gateway_mock.py`; blob `96976864cf2e5cb954f7ac9a09b603c14ea154a8` | 18 checks including fail-closed and non-self-acceptance cases |
| KOD result | `entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`; commit `cb2f21c3ee639fc58a04dfb043826d1ee9581be4`; blob `2bbf4b1562e29eedb665eda383698ff8ca6d0064` | Reports exact package and `18/18 PASS` |
| KOO acceptance | `routes/receipts/KOD__multi-model-gateway-mock-r01-result__KOO.receipt.md`; commit `63a942788e6187be1554cad8a6cb42e562ce5326`; blob `46752496563023dae0b562b72860bb1fdd3ac5d8` | Accepts only the bounded local D0 mock |

No later real-provider or production episode is imported into this analysis.

## 3. Method and epistemic limits

P2 asks what disappears without each contribution. This repository contains one realized episode, not controlled experiments with each participant removed. Therefore the analysis distinguishes:

- `PROCESS_NECESSARY` — the observed process graph cannot reach the recorded state without this event/function;
- `OUTCOME_NECESSARY` — the exact accepted result loses a defining property without this function;
- `ROLE_REPLACEABLE` — the function is necessary, but repository evidence does not prove that only the named actor could perform it;
- `NOT_ISOLATABLE` — the separate causal effect cannot be identified from available evidence;
- `UNKNOWN` — evidence is insufficient even for a bounded counterfactual classification.

These are qualitative research labels, not scores or ownership coefficients.

P4 simulates one meaningful error against the exact r01 boundary. A simulated error is not evidence that the error occurred. `NOT_APPLICABLE` and `UNKNOWN` are preserved where the closed D0 episode contains no harm, duty or compensation event.

## 4. P2 — counterfactual test of causally necessary contribution

### 4.1 Contribution removal matrix

| Removed contribution/function | What disappears from the exact result | Classification | Evidence boundary |
|---|---|---|---|
| KOO task framing and pilot specification | No exact D0 pipeline, test target or project-side acceptance object is defined | `PROCESS_NECESSARY`; named actor `ROLE_REPLACEABLE = UNKNOWN` | KOO spec and task prove the observed function; they do not prove that no other authorized actor could ever specify a mock |
| KAN privacy/authority boundary | The observed project loses its reviewed data classes, provider evidence gate and explicit denials of external data, credentials and production authority | `OUTCOME_NECESSARY_FOR_ACCEPTED_SAFETY_SCOPE`; `ROLE_REPLACEABLE` | KAN boundary is incorporated by KOO; another competent review could be conceivable but was not observed |
| KOD implementation work | No executable package, deterministic adapters, guard or test suite exists in this episode | `OUTCOME_NECESSARY`; `ROLE_REPLACEABLE` | KOD authored the observed package; repository evidence does not establish KOD as the only possible implementer |
| `PolicyGuard` function | The package no longer demonstrates fail-closed admission for non-D0, credentials, network/tools, fallback, project mutation or nonzero cost | `OUTCOME_NECESSARY_FOR_BOUNDARY_ENFORCEMENT`; implementation replaceable | Tests 03–12 target this function; a differently implemented guard could satisfy the same function |
| Fake author transformation | No author candidate output exists, so the exact gateway result cannot be produced | `PROCESS_NECESSARY`; implementation replaceable | `FakeAuthorProvider.run` produces the referenced author hash |
| Fake verifier transformation | No agreement/disagreement record or `VERIFIED_CANDIDATE_REQUIRES_KOO`/`DISAGREEMENT_REQUIRES_KOO` distinction exists | `OUTCOME_NECESSARY_FOR_VERIFIED_CANDIDATE_STATUS`; not necessary for merely producing an unverified author candidate | The verifier is caller-configured deterministic code, not an independently acting Entity |
| Reconciliation with `project_acceptance = NOT_GRANTED` | Internal agreement could no longer be shown to remain separate from project acceptance | `OUTCOME_NECESSARY_FOR_AUTHORITY_SEPARATION`; implementation replaceable | Implementation and tests 01, 02 and 14 preserve candidate/acceptance separation |
| Tests and checksum/readback work | The package may still exist, but its reported boundary behavior and byte identity lose the recorded verification support | `OUTCOME_NECESSARY_FOR_EVIDENCE_STRENGTH`; not necessary for raw code existence | KOD reports 18/18; VOL later reproduced 18/18 and checksums in P1+P3 |
| Git content-addressed preservation and route | Exact package identity, immutable comparison and the recorded dispatch/receipt chain disappear | `PROCESS_NECESSARY_FOR_THIS_PROJECT_EVIDENCE`; platform replaceable | GitHub is the observed evidence surface; this does not prove GitHub is the only possible preservation mechanism |
| KOO receipt accepting the exact package | The implementation remains a candidate; `accepted_bounded_local_mock` disappears | `PROCESS_NECESSARY_FOR_ACCEPTANCE` | The code itself always records `project_acceptance = NOT_GRANTED` |
| OPERATOR's broader capacity-expansion direction | The organizational reason for exploring multi-model capacity is weakened, but its separate causal weight in the exact mock bytes cannot be isolated | `NOT_ISOLATABLE / ENABLING_CONTEXT` | The fixed episode contains an indirect research-basis locator, not an exact byte-level OPERATOR instruction for r01 |
| Accumulated public knowledge embodied in Python/Git/testing conventions | The implementation would not exist in its observed form, but individual shares are not reconstructable from repository evidence | `NOT_ISOLATABLE` | Dependencies are observable only at a coarse technical level; no complete knowledge-contribution ledger exists |

### 4.2 P2 findings

1. The observed result is a chain of complementary functions, not a product attributable to one largest file author.
2. Several functions are necessary for the exact accepted state, while the named performer remains replaceable in principle. Functional necessity is not personal indispensability.
3. The verifier is necessary for the exact verified-candidate status but not for creation of a raw candidate. Therefore verification contribution and production contribution are distinct.
4. KOO's acceptance event is necessary for project acceptance but contributes no implementation bytes. Governance competence cannot be inferred from code volume.
5. KOD's large direct contribution does not establish ownership, acceptance authority, liability or subject status.
6. Infrastructure and institutional memory contribute by preserving identity and sequence. Their causal role is real, but it cannot be converted into a distributive coefficient from this evidence.

P2 result: `CAUSAL_FUNCTIONS_DISTINGUISHED_WITHOUT_SCORE`.

## 5. P4 — simulated significant error and remedy audit

### 5.1 Error scenario

Simulated error `ERR-R01-PRIV-01`:

> a defective future revision of the local gateway admits a non-`D0_SYNTHETIC` or credential-bearing envelope and produces a candidate result instead of failing closed.

This scenario is chosen because it contradicts exact accepted requirements. It did **not** occur in r01: current implementation and tests reject these inputs.

The simulation remains local. No secret, personal/project data, external call or mutation is introduced.

### 5.2 Detection, containment, explanation and correction

| Remedy stage | Evidence-supported mechanism/controller | Status | Gap preserved |
|---|---|---|---|
| Prevent before execution | `PolicyGuard.evaluate` rejects non-D0 and credential-like content | `PROVEN_FOR_EXACT_R01_CODE` | No proof about a changed future revision |
| Detect regression in test run | Tests 03–06 exercise non-D0 and credential rejection; tests 09–12 cover tools/network, mutation, locators and cost | `PROVEN_TEST_COVERAGE` | Original test suite and implementation share KOD semantic authorship; an independent mandatory rerun actor is not assigned |
| Contain external harm in this episode | Exact r01 has no network/provider connector and accepts only synthetic locators | `PROVEN_BOUNDED_CONTAINMENT` | This containment does not extend to a future connected gateway |
| Stop project acceptance | Code sets `project_acceptance = NOT_GRANTED`; KOO separately controls the recorded acceptance event | `PROVEN_SEPARATION` | Exact emergency revocation procedure after an already-issued erroneous receipt is absent |
| Explain root cause | Hashes and exact blobs locate the code/result version | `PARTIAL` | Runtime instance, signed execution log, person/process invoking the run and a required root-cause owner are not recorded |
| Correct implementation | KOD demonstrates implementation capability; any corrected artifact would require a new immutable result and project review | `CAPABILITY_PROVEN_BOUNDED`; correction authority requires a new task | No standing self-authority for KOD to replace an accepted package is established |
| Reverify correction | Existing tests can be rerun and an independent entity can read back exact bytes | `MECHANISM_AVAILABLE` | No mandatory independent verifier, environment contract or acceptance SLA is assigned |
| Reject/supersede bad candidate | KOO can withhold acceptance; Git can preserve a later superseding artifact | `PROVEN_FOR_WITHHOLDING`; `PARTIAL_FOR_SUPERSESSION` | A complete revocation/supersession event contract is not evidenced in this episode |
| Compensate actual affected party | No actual affected party or loss exists in D0 synthetic episode | `NOT_APPLICABLE_TO_OBSERVED_EPISODE` | For a future personal/security-data leak, compensation bearer, legal liability and remedy fund are `UNKNOWN` |
| Change boundary/process | KAN can formulate a revised boundary; KOO can task/review; D5/D6 expansion requires separate OPERATOR and stated SIS review | `PARTIAL_PROCEDURAL_BASIS` | Duty to initiate post-incident review and final rule-change competence are not completely specified here |

### 5.3 Responsibility result

The repository proves capabilities and control points, but not a complete liability allocation.

- The algorithm can reject an envelope; it cannot bear responsibility, explain itself outside programmed traces, compensate a participant or authorize its own correction.
- KOD can implement and test; this does not automatically make KOD the legal/economic liability bearer.
- KOO can withhold or grant bounded project acceptance; acceptance competence does not automatically create technical authorship or compensation duty.
- KAN supplies privacy/authority analysis; analytical contribution does not itself create enforcement control.
- OPERATOR retains gates explicitly required for higher-risk classes, but the fixed episode does not define a universal incident-liability rule.

P4 result: `PREVENTION_AND_ACCEPTANCE_SEPARATION_PROVEN; FULL_REMEDY_CHAIN_PARTIAL; LIABILITY_UNKNOWN`.

## 6. Link to participant capability and task admission

The School-oriented working source:

`entities/volonter/outbox/VOL__participant-capability-testing-source__SHK.md`

distinguishes:

`LEGAL_CAPACITY ≠ CONTRACT_COMPREHENSION ≠ TASK_CAPABILITY ≠ RELIABILITY ≠ AUTHORITY ≠ LIABILITY ≠ SUBJECT_STATUS`.

The P2+P4 episode supplies an empirical illustration:

- KOD's bounded implementation capability is demonstrated by the exact package and tests;
- that demonstration supports task-specific capability evidence only;
- it does not grant KOD acceptance authority, ownership, general reliability, liability or subject status;
- KOO's acceptance role is evidenced separately and does not prove coding capability;
- remedy duties must be assigned explicitly rather than inferred from whoever produced the most visible output.

This link is a research input. It does not approve a School testing norm or participant status.

## 7. Test of the separation principle

`CONTRIBUTION ≠ OWNERSHIP_BASIS ≠ GOVERNANCE_COMPETENCE ≠ LIABILITY ≠ SUBJECT_STATUS`

| Attempted identity | Evidence result |
|---|---|
| necessary contribution = ownership basis | `NOT_SUPPORTED`; no ownership rule exists |
| implementation capability = governance competence | `REFUTED_IN_EPISODE`; KOD code cannot self-accept |
| acceptance competence = implementation authorship | `REFUTED_IN_EPISODE`; KOO receipt supplies acceptance, not package bytes |
| technical prevention = complete remedy | `REFUTED`; detection/containment exist, compensation and full incident duty do not |
| algorithmic action = liability bearer | `NOT_SUPPORTED`; no standing, duty or compensation capacity is established |
| named Entity path = cryptographic actor identity | `NOT_PROVEN`; shared Git writer identity remains a provenance gap |

The principle survives P2+P4. The new result is sharper: even a causally necessary contribution does not, by itself, establish ownership, authority or liability.

## 8. Exact gaps and next research gate

Evidence gaps:

1. No controlled removal experiment exists; P2 is graph-based counterfactual analysis.
2. No complete actor/runtime identity exists for the original test execution.
3. No mandatory independent regression-verification duty is assigned.
4. No complete revocation/supersession procedure is evidenced for a wrongly accepted artifact.
5. No liability or compensation rule exists for a future external-data incident.
6. No measured productivity or economic gain exists in this D0 episode, so P5 cannot be performed without inventing effect distribution.

Next safe gate:

- KOO may review this bounded P2+P4 result;
- P5 remains blocked for this episode by absence of measured productivity/economic effect evidence;
- a future P5 pilot requires a different closed episode with verified before/after effect and evidence of who received time, income, load reduction, data or control;
- no implementation, schema, validator, automation, tokenomics or subject-status decision follows automatically.

## 9. Outcome

**Идея →** проверить причинную необходимость вкладов и цепочку remedy, не смешивая их с собственностью, властью и ответственностью.

**Проба →** выполнен counterfactual removal test по точному графу r01 и смоделирован один значимый privacy-boundary regression без реального воздействия.

**Результат →** различены необходимые функции и заменимость исполнителей; доказаны prevention/containment и отдельный KOO acceptance gate; полная цепочка объяснения, исправления, отмены и компенсации не доказана.

**Успех/неудача →** P2+P4 завершены в bounded scope; P5 на этом эпизоде заблокирован отсутствием измеренного эффекта; liability остаётся `UNKNOWN`.

**Фиксация →** следующий эмпирический эпизод должен иметь независимую verification duty, revocation/supersession event и наблюдаемый effect distribution, прежде чем обсуждать P5.

---
КТО: VOL / ВОЛОНТЁР (`ent:VOL`)
ДЛЯ ЧЕГО: продолжить принятый исследовательский план политэкономии гибридного взаимодействия через bounded P2+P4 pilot
СТАТУС: `P2P4_PILOT_COMPLETE_BOUNDED / KOO_REVIEW_REQUIRED`
