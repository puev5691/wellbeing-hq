# SHT → KOO: STP-C B1 factual independence map r0.1

terminal: BLOCKED_SHT_STP_C_B1_INDEPENDENCE_MAP_R01_MISSING_EVIDENCE
scope: DOCUMENT_ONLY_FACTUAL_INDEPENDENCE_MAP
composition_selected: no
quorum_selected: no
participants_appointed: no
project_time: omitted

## Человеческий итог

B1 построена настолько, насколько позволяют факты. Ролевые границы проекта доказаны существенно лучше, чем фактическая operational independence будущих quorum seats.

Approved roles подтверждают, что OPERATOR, KOO, KAN, SHT и SIS имеют разные функции и что capability не создаёт authority. STP-C candidate дополнительно запрещает концентрацию requester/mutation/verifier/publisher/signer powers. Но эти документы не доказывают, что соответствующие seats исполняются разными principals, имеют раздельную credential custody, находятся в разных runtime/admin/control/failure domains или не могут быть технически отключены/подменены одним общим администратором.

Поэтому данных недостаточно для осмысленного выбора C1/C2/C3/C4 именно по критерию независимости. Разные названия ролей, чаты и файлы не повышены до operational independence.

## Exact basis

OPERATOR order:
entities/koordinator/outbox/KOO__STP-C-order-independence-map-before-composition__OPERATOR.md@4eff701b0c4bc47db2a80ffbaf99dae17cb09814.

Task:
entities/koordinator/outbox/KOO__STP-C-B1-independence-map-r01__SHT.md@148d744301f0f3f69604008113d0776ca2da3630.

KAN review:
entities/kancelar/outbox/KAN__STP-C-governance-model-r01-independent-review__KOO.md@1f8f6d17a9b28710ff2fc9445635991a539e1121
blob 986cbdc37aeacbd1c4061f24803580e111e8c105.

STP-C candidate:
entities/shtabist/outbox/SHT__STP-C-multiparty-governance-model-design-r01__KOO.md@622addc16bd8efa8736f3332dd31cee0e7b5dcb1
blob 4191acf5ced6066397c5c734f9246b2098bcb46e.

KOO convergence/B1 boundary:
entities/koordinator/current/KOO__STP-C-r01-review-convergence-and-boundaries-r01.md@f852f02a2ac08e173ef1cec3afc73fe8a3402b81
blob 604d217562709759337e42f6eb1f0f3a2a9ed150.

Approved roles:
entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md
blob 1772339cb74dae8550bfbd2e33401c34a929e911.

Approved Project Core:
entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md
blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33.

Current SHT writer:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da.

## 1. Independence matrix

Status vocabulary:
VERIFIED_INDEPENDENT / VERIFIED_SHARED_DOMAIN / PARTIALLY_INDEPENDENT / UNKNOWN / NOT_APPLICABLE.

Important: role separation is not treated as runtime/control independence.

| Seat / role class | Possible principal/entity class | Who may authorize | Credential custody | Runtime/execution boundary | Admin/control domain | Failure domain | Proven technical controller/substituter | Conflicts of interest | Independence status |
|---|---|---|---|---|---|---|---|---|---|
| OPERATOR / human non-delegable governance | human OPERATOR | OPERATOR retains reserved decisions under approved roles; exact future seat appointment still requires explicit decision | UNKNOWN for future STP-C signing/authentication credentials | Human vs AI-Entity conceptual boundary is established; concrete device/account/runtime boundary for future seat is UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | If OPERATOR is also sole credential custodian/root administrator, governance and authentication/control may collapse; not established | PARTIALLY_INDEPENDENT |
| KOO / governance-coordination | KOO Entity instance | Existing role/process + exact/standing authority; future STP-C seat still needs OPERATOR appointment | UNKNOWN | Entity/chat instance concept established; concrete runtime isolation from KAN/SHT/SIS UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Routing/reconciliation plus approval seat may concentrate agenda/evidence selection and approval | UNKNOWN |
| KAN / normative-formal review | KAN Entity instance | Existing review role; future seat requires OPERATOR decision | UNKNOWN | Concrete runtime isolation UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | If KAN both defines normative acceptance and approves same profile, review/approval separation narrows | UNKNOWN |
| SHT / organizational-process | SHT Entity instance | Existing process-review role; future seat requires OPERATOR decision | UNKNOWN | Current SHT instance has separate Writer Gate evidence, but this does not prove runtime/admin independence from other seats | UNKNOWN | UNKNOWN | UNKNOWN | SHT designed STP-C candidate; using same role as decisive approver of its own design creates self-review concern unless independent evidence/review intervenes | UNKNOWN |
| SIS / infrastructure-security | SIS Entity instance | Existing infrastructure role; future seat requires OPERATOR decision | UNKNOWN | Concrete runtime isolation UNKNOWN | Infrastructure role can administer hosts/services when separately authorized, but exact control over future STP-C participants is UNKNOWN | UNKNOWN | No evidence that SIS currently controls candidate seat runtimes; host/admin capability must not be inferred as trust authority | If SIS operates future host/backend and is approval seat, infrastructure control + approval may concentrate | UNKNOWN |
| Independent technical verifier | future verifier principal, not yet appointed | UNKNOWN; future OPERATOR/profile decision required | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Cannot verify evidence it solely created; cannot silently be mutation service or approval seat | UNKNOWN |
| Future signer/attestor | future signing/attestation principal | UNKNOWN; future root/profile decision required | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Signing capability must not become governance decision authority; signer deciding and self-attesting same truth is prohibited by candidate | UNKNOWN |
| Publisher | future/current publication capability; exact principal for STP-C not appointed | separate publication authority as applicable; no STP-C seat authority established | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Publication capability cannot become approval/currentness authority | NOT_APPLICABLE for quorum independence until proposed as a seat; control conflict remains UNKNOWN |
| Store mutation service | future mutation-service principal | only separately admitted mutation authority; no approval authority from service role | UNKNOWN | UNKNOWN | backend/host/operator not selected | UNKNOWN | UNKNOWN | Must not be sole approver; mutation + approval would concentrate privilege creation/execution | NOT_APPLICABLE for quorum independence until proposed as a seat; control conflict remains UNKNOWN |

## 2. Evidence supporting non-UNKNOWN statements

### OPERATOR — PARTIALLY_INDEPENDENT

Evidence:
approved roles v2.4, blob 1772339c..., states:
- OPERATOR = decision, launch and responsibility;
- AI Entity = specialized tool mode;
- Entities do not replace OPERATOR;
- capability does not create authority.

This proves a governance/principal-class distinction between human OPERATOR and AI Entity roles.

It does NOT prove separate credential custody, account administration, device/runtime, authentication root or failure domain. Hence not VERIFIED_INDEPENDENT.

### SHT current-instance boundary

Evidence:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md@44a8181...
proves this exact SHT instance passed its own initiation/Writer Gate and is current SHT writer.

It does NOT compare SHT runtime/admin/failure domain with KOO/KAN/SIS. Therefore it cannot support cross-seat independence.

### Role separation generally

Evidence:
approved roles v2.4, blob 1772339c..., assigns different functional scopes:
- KOO: priorities/dependencies/reconciliation/routing;
- KAN: normative/formal boundaries;
- SHT: organizational/process lifecycle;
- SIS: infrastructure;
and explicitly says capability does not create authority.

This is VERIFIED role separation, but B1 asks operational independence. Therefore matrix statuses remain UNKNOWN unless control-domain evidence exists.

### Publisher/mutation-service NOT_APPLICABLE as seats

Evidence:
STP-C candidate @622addc... separates publisher, verifier, signer and mutation service and states publication/mutation capability does not create approval authority.
They are analyzed as conflict/control classes, not proposed participant seats in C1-C4. Hence quorum-seat independence is NOT_APPLICABLE at this stage, while their possible shared-control relationship remains UNKNOWN.

## 3. Conflict-of-interest map

Confirmed candidate constraints from STP-C @622addc...:
- requester cannot be sole/decisive approver of own elevation;
- mutation service cannot be sole approver;
- signer/attestor cannot alone decide governance truth then self-attest it;
- verifier cannot verify evidence it solely created;
- publisher cannot convert publication into approval;
- host/admin capability does not grant trust approval;
- routing does not grant signing authority;
- review role does not grant operational/signing authority;
- one runtime/credential identity must not silently occupy multiple seats.

Specific B1 conflict risks:

1. KOO seat + evidence-routing/reconciliation:
risk of agenda/evidence-selection concentration. Whether it is materially independent from other seats is UNKNOWN.

2. SHT seat + author of STP-C organizational design:
self-review/design conflict exists if SHT becomes decisive approver without independent review boundary. KAN review reduces document-review conflict but does not prove runtime independence.

3. SIS seat + future backend/host administration:
potential operational-control + approval concentration if SIS later controls the runtime/backend of other seats. Not established; must be measured, not assumed.

4. verifier + mutation service:
forbidden/unsafe concentration for same evidence path.

5. signer/attestor + governance approver:
possible only under future explicit model; candidate prefers separation unless separately justified.

6. OPERATOR + root/key custody:
could collapse human governance and authentication root if same human/device/account controls all credentials. Current custody is UNKNOWN.

## 4. Shared-control / failure-domain map

### VERIFIED_SHARED_DOMAIN

None can currently be proven from the exact loaded evidence.

This is important: absence of proof of independence is not proof of shared domain either.

### PARTIALLY_INDEPENDENT

OPERATOR vs AI Entity classes:
governance/principal-class separation is proven by approved roles, but technical control/failure-domain separation is not.

### UNKNOWN pairs material to C1-C4

- KOO ↔ KAN;
- KOO ↔ SHT;
- KOO ↔ SIS;
- KAN ↔ SHT;
- KAN ↔ SIS;
- SHT ↔ SIS;
- any of the above ↔ future independent verifier;
- any approval seat ↔ future signer/attestor;
- approval seats ↔ publisher;
- approval seats ↔ future mutation service;
- OPERATOR ↔ authentication/signing infrastructure.

For all these, current evidence does not establish:
- distinct credential custodians;
- distinct runtime providers/accounts;
- distinct administrators;
- distinct hosts/process security boundaries;
- distinct failure domains;
- inability of one principal/admin to disable/substitute another.

Different chats/files/current-writer records are not sufficient.

## 5. UNKNOWN blocking C1/C2/C3/C4 selection

### U1 — principal identity model
Are KOO/KAN/SHT/SIS future seats distinct principals for trust purposes, or role modes under a common account/control principal?

### U2 — credential custody
Who would hold/authenticate each seat's credential? Are credentials separable by custodian and recovery path?

### U3 — runtime boundary
Where does each seat execute for approval purposes? Same ChatGPT account/runtime/provider/session control, separate services, human device, offline signer, or something else?

### U4 — administrative control
Who can reset, revoke, replace, reconfigure or impersonate each seat/runtime/credential?

### U5 — failure domain
Which seats fail together under:
- one account suspension;
- one provider outage;
- one device loss;
- one repository/account compromise;
- one host/admin compromise;
- one credential custodian compromise?

### U6 — technical substitution/control
Can one role/admin technically create or replace another role's approval evidence or execution environment?

### U7 — future verifier independence
No principal/runtime/admin/custody is defined for the “independent technical verifier”, so C3/C4 cannot yet claim that independence.

### U8 — signer/attestor separation
No attestor/root/custody is selected. Therefore no candidate composition can yet rely on cryptographic separation as factual independence.

These UNKNOWNs are material, not cosmetic. They prevent evidence-based ranking/selection among C1-C4.

## 6. Minimum next evidence request

Next owner: SIS / СИСАДМИН for a bounded non-mutating technical-control inventory, with KOO retaining governance reconciliation.

Why SIS:
approved roles assign infrastructure/runtime/storage/service boundaries to SIS. The request is not to choose technology or participants, but to document known technical control/failure domains and mark unavailable facts UNKNOWN.

Minimum requested artifact:
STP-C-B1-runtime-control-inventory-r01.

For each existing candidate Entity class KOO/KAN/SHT/SIS and current OPERATOR-facing execution context, record only evidence-backed:
- account/provider/runtime boundary;
- credential/custody owner if actually known;
- administrator/control principal;
- ability to reset/disable/replace/impersonate;
- shared account/provider/host dependencies;
- common failure domains;
- exact evidence locator for every non-UNKNOWN claim.

For future verifier/signer/publisher/mutation service:
do not invent implementation; explicitly mark UNDEFINED/UNKNOWN and list what future design evidence would be required.

No secrets or credential values.

If SIS lacks visibility into ChatGPT/provider account/control facts, it must return UNKNOWN and identify the minimum fact only OPERATOR can supply.

## 7. Is evidence sufficient now for composition choice?

NO.

It is sufficient to understand functional conflicts and to reject the false inference:
different role name/chat/file => independent seat.

It is not sufficient to choose C1/C2/C3/C4 based on actual independence because the decisive runtime/admin/custody/failure-domain evidence is absent.

Therefore exact terminal:
BLOCKED_SHT_STP_C_B1_INDEPENDENCE_MAP_R01_MISSING_EVIDENCE.

This blocker does not reject STP-C. It blocks only the next composition choice until the material independence evidence is obtained or explicitly accepted as UNKNOWN by an authorized OPERATOR decision.

## EXPERIENCE

Идея → measure independence by who can control/fail/impersonate a seat, not by its role label.

Проба → map role authority evidence separately from credential/runtime/admin/failure-domain evidence.

Результат → role separation is documented, but operational independence for C1-C4 is mostly UNKNOWN.

Неудача composition-readiness → insufficient factual control-domain evidence.

Урок → four different AI job titles inside one unknown administrative boundary may still be one failure domain wearing four badges. B1 exists to discover that before quorum arithmetic turns it into “independence”.

## Terminal

BLOCKED_SHT_STP_C_B1_INDEPENDENCE_MAP_R01_MISSING_EVIDENCE

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
