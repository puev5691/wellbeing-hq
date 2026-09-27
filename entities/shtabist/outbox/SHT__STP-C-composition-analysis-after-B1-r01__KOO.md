# SHT → KOO: STP-C composition analysis after B1 r0.1

terminal: PASS_SHT_STP_C_COMPOSITION_ANALYSIS_AFTER_B1_R01_READY_FOR_OPERATOR_DECISION
scope: DOCUMENT_ONLY_COMPOSITION_ANALYSIS_AFTER_B1
composition_selected: no
participants_appointed: no
quorum_selected: no
project_time: omitted

## Человеческий итог

После B1 четыре текущие Entity-роли KOO/KAN/SHT/SIS нельзя считать четырьмя технически независимыми seats. SIS + OPERATOR facts закрыли прежний UNKNOWN: они находятся в одном ChatGPT/OpenAI account, имеют одного administrative/access/recovery principal — ОПЕРАТОРА — и не имеют отдельно администрируемых provider/workspace/account/device/runtime boundaries.

Это не обнуляет role diversity. KOO, KAN, SHT и SIS всё ещё дают разные функции, критерии и способы критики. Но их совместное голосование защищает прежде всего от односторонней ошибки рассуждения/процесса, а не от compromise/disablement общего technical control domain.

После B1 надо считать отдельно role diversity, decision diversity, authentication independence, runtime/admin independence и failure-domain independence. Первые два свойства реально присутствуют у внутренних Entity-ролевых комбинаций. Последние три для KOO/KAN/SHT/SIS не являются независимыми: shared technical domain доказан.

Evidence достаточно для следующего bounded решения ОПЕРАТОРА о composition, если decision table сохраняет эту границу.

## Exact basis

Authority: entities/koordinator/outbox/KOO__authorize-SHT-STP-C-composition-analysis-after-B1-r01__OPERATOR.md@58e51b84ce79772ad25a12b208fc9ba0b8c51c6e, blob 29012df121b897bc3904977766ecdc257265d757.
Task: entities/koordinator/outbox/KOO__STP-C-composition-analysis-after-B1-r01__SHT.md@b90d3aab82d9540a5272b7594f1592182c61708f, blob b2e96a8ef91ee41c17f26c7314c7fac688e86c3d.
B1: entities/shtabist/outbox/SHT__STP-C-B1-independence-map-r01__KOO.md@c3024a4b45575c47e0dc381c6470f09b8d6fe1e9, blob 4d3faf5937a847fbc7c2b7c740d0ae6c45938b33.
SIS closure: entities/sisadmin/outbox/SIS__STP-C-B1-runtime-control-inventory-r01-operator-facts-resolved__KOO.md@52507d0643d031d996e2af464071a22598eccf4b, blob 5905899bf9247bee1d5faabd696b6d06b5795139.
STP-C model: entities/shtabist/outbox/SHT__STP-C-multiparty-governance-model-design-r01__KOO.md@622addc16bd8efa8736f3332dd31cee0e7b5dcb1, blob 4191acf5ced6066397c5c734f9246b2098bcb46e.
KAN review: entities/kancelar/outbox/KAN__STP-C-governance-model-r01-independent-review__KOO.md@1f8f6d17a9b28710ff2fc9445635991a539e1121, blob 986cbdc37aeacbd1c4061f24803580e111e8c105.
Current SHT writer: entities/shtabist/current/SHT__current-instance-current-writer-r01.md@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641, blob a019c21cffeb99bb7c387b8fa95a4629137dc6da.

## Established B1 fact

VERIFIED_SHARED_DOMAIN: KOO + KAN + SHT + SIS.

Shared: one ChatGPT/OpenAI account; OPERATOR administrative/control principal; OPERATOR-only access/recovery control; no separately administered provider/workspace/account/device/runtime boundary.

Therefore separate chats, roles and current-writers do not create technical independence.

## Five-axis interpretation

| Axis | Current internal combinations |
|---|---|
| Role diversity | YES — distinct approved project functions |
| Decision diversity | YES, bounded — distinct review responsibilities/perspectives |
| Authentication independence | NO evidence of separate administration; must not be claimed |
| Runtime/admin independence | NO — shared technical control domain |
| Failure-domain independence | NO — shared account/control failure domain |

## C1 — GOV / NORM / INFRA

Real benefit: strong internal role/decision diversity across governance, normative/process and infrastructure/security failure classes.

Not provided: authentication, runtime/admin or failure-domain independence.

Primary status: MEANINGFUL_AS_GOVERNANCE_DIVERSITY.
Also: MISLEADING_IF_COUNTED_AS_TECHNICALLY_INDEPENDENT.

External principal: not required if objective is governance diversity only. Required if STP-C must resist compromise/disablement of the shared ChatGPT/OpenAI control domain.

Failure modes: shared account loss/compromise affects all seats; shared administrator/recovery path correlates replacement/control; numeric internal quorum can create false threshold-security impression.

Evidence for OPERATOR choice: sufficient for governance-only C1. For technical independence, future evidence of at least one separately administered external principal is required.

## C2 — HUMAN / NORM / INFRA

Real benefit: human-reserved governance judgment plus two specialist internal reviews; meaningful human-machine decision diversity.

Limitation: OPERATOR is also administrative/access/recovery controller of the account hosting NORM/INFRA. Human governance distinction therefore does not create a separate technical failure domain against compromise/control of OPERATOR/shared account.

Primary status: MEANINGFUL_AS_GOVERNANCE_DIVERSITY.
Also: MISLEADING_IF_COUNTED_AS_THREE_TECHNICALLY_INDEPENDENT_SEATS.

External principal: not required for human-reserved governance + internal review. Required if protection from OPERATOR/shared-account compromise is an objective.

Failure modes: OPERATOR governance and account control concentrate; shared account/provider outage removes both Entity seats; one compromised control path can affect human governance evidence and Entity control.

Evidence: sufficient to choose C2 as governance structure with known limitation. External-principal evidence only if technical threshold independence is required.

## C3 — GOV / NORM / VERIFIER

Real benefit now: GOV/NORM role diversity. Potential benefit: a separately controlled verifier could add a genuinely different technical failure domain.

Current limitation: verifier is UNKNOWN/UNDEFINED, so the defining “independent verifier” property does not yet exist as evidence.

Primary status: CONDITIONALLY_MEANINGFUL_IF_EXTERNAL_INDEPENDENT_PRINCIPAL_ADDED.

Minimum external verifier evidence:
- distinct principal identity;
- separately administered account/runtime;
- separate access/recovery control;
- separate administrative control;
- documented failure-domain separation for claimed threats;
- inability of requester/mutation/shared internal domain to silently alter verifier runtime/evidence;
- independent evidence read path.

Failure modes without that evidence: verifier independent only in name; common admin can disable/replace all seats; same-domain evidence production/verification can collapse separation.

Evidence: sufficient for OPERATOR to select C3 as a conditional target composition, but no technical-independence claim/admission until verifier evidence exists.

## C4 — GOV / NORM / INFRA / VERIFIER

Real benefit: widest role/decision diversity plus a place for external verification.

Limitation: GOV/NORM/INFRA remain one shared technical domain. Only a genuinely external verifier can add another failure domain.

Primary status: CONDITIONALLY_MEANINGFUL_IF_EXTERNAL_INDEPENDENT_PRINCIPAL_ADDED.

Internal-only C4 remains governance-diverse but is MISLEADING_IF_COUNTED_AS_FOUR_TECHNICALLY_INDEPENDENT_SEATS.

Minimum external verifier evidence: same as C3.

Additional future condition: if technical independence is the reason for the verifier, later quorum design must not allow correlated internal seats to bypass that verifier. This is a later quorum question, not selected here.

Failure modes: 3 internal correlated votes can create false confidence; unconstrained later numeric quorum could nullify verifier benefit; external verifier outage can cause deliberate fail-closed deadlock.

Evidence: sufficient to select C4 conditionally; verifier independence and later non-bypass quorum remain future gates.

## Comparative table

| Composition | Real benefit after B1 | Current technical independence | Status | External principal requirement |
|---|---|---|---|---|
| C1 GOV/NORM/INFRA | broad internal governance/review diversity | NO | MEANINGFUL_AS_GOVERNANCE_DIVERSITY | only if technical threshold independence required |
| C2 HUMAN/NORM/INFRA | human-reserved governance + specialist review | NO against shared OPERATOR/account control | MEANINGFUL_AS_GOVERNANCE_DIVERSITY | only if shared-control compromise must be covered |
| C3 GOV/NORM/VERIFIER | governance diversity + potential external verification | NOT YET; verifier undefined | CONDITIONALLY_MEANINGFUL_IF_EXTERNAL_INDEPENDENT_PRINCIPAL_ADDED | YES for technical-independence benefit |
| C4 GOV/NORM/INFRA/VERIFIER | widest role diversity + potential external failure-domain check | internal three NO; verifier undefined | CONDITIONALLY_MEANINGFUL_IF_EXTERNAL_INDEPENDENT_PRINCIPAL_ADDED | YES for technical-independence benefit |

Global rule: every option is MISLEADING_IF_COUNTED_AS_TECHNICALLY_INDEPENDENT solely from current internal Entity seat count.

## Benefits removed by B1

No longer available assumptions:
- N internal seats => N independent authentication principals;
- N chats => N runtime boundaries;
- N current-writers => N administrative boundaries;
- internal numeric quorum => resilience to shared account compromise;
- internal redundancy => resilience to shared account/provider outage.

Still real:
- functional specialization;
- review/decision diversity;
- conflict-of-interest visibility;
- procedural checks.

## Minimum external-independence requirement

If STP-C objective includes technical threshold independence, minimum additional class is ONE_EXTERNAL_INDEPENDENT_PRINCIPAL_CLASS with evidence-backed:
1. distinct principal identity;
2. separately administered account/runtime;
3. separate access/recovery control;
4. separate administrative control;
5. documented failure-domain separation for claimed threats;
6. independent authentication/currentness evidence;
7. inability of internal shared domain to silently impersonate/replace its approval;
8. independent read/verification path.

No provider/root/signer technology is selected here.

## Is evidence sufficient for next bounded OPERATOR decision?

YES.

The key B1 uncertainty is resolved: KOO/KAN/SHT/SIS are one shared technical domain.

Remaining undefined external verifier is not a blocker to choosing an intended composition model, provided the decision states whether it seeks:
A. governance/decision diversity only; or
B. governance diversity + future external technical independence.

A B-type choice is conditional and cannot claim/admit technical independence until external-principal evidence exists.

## Narrow OPERATOR decision table

| Choice | What is chosen | Real gain | Not gained now | Condition before technical-independence claim |
|---|---|---|---|---|
| C1 | GOV + NORM + INFRA internal roles | broad internal review diversity | independent technical quorum | add external separately controlled principal if required |
| C2 | HUMAN + NORM + INFRA | human-reserved governance + specialist review | protection from OPERATOR/shared-account compromise | external principal outside shared control if that threat must be covered |
| C3 | GOV + NORM + VERIFIER | governance diversity + designated independent-verification role | verifier independence now | verifier must satisfy external-independence evidence |
| C4 | GOV + NORM + INFRA + VERIFIER | widest role diversity + designated external verification role | four-way technical independence | external verifier evidence + later quorum must not bypass it |

Decision question:
Which participant-role composition should be carried forward as the STP-C candidate model, with the exact B1 shared-domain limitations and any external-independence condition preserved?

No quorum decision is part of this gate.

## Boundary preservation

Not performed: composition selection; participant appointment; quorum; emergency revoke; root/signing technology; credentials; attestor/backend/host/operator; Fast Gate/profile activation; live WRITE/CAS; deployment; CHECKPOINT_DURABLE; Project Source activation; EOM pilot; memory-layering attempt 3.

## EXPERIENCE

Идея → after B1, evaluate composition by separating governance diversity from technical threshold independence.

Проба → compare C1-C4 across five independence axes while collapsing KOO/KAN/SHT/SIS into their proven shared failure domain.

Результат → C1/C2 retain real governance value; C3/C4 can add technical protection only if future verifier is genuinely external/separately controlled.

Успех → evidence is sufficient for a narrow OPERATOR composition choice without pretending the shared domain disappeared.

Урок → quorum arithmetic becomes honest only after correlated seats are collapsed into real failure domains. Three internal votes can be three useful opinions and still be one technical point of failure.

## Terminal

PASS_SHT_STP_C_COMPOSITION_ANALYSIS_AFTER_B1_R01_READY_FOR_OPERATOR_DECISION

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
