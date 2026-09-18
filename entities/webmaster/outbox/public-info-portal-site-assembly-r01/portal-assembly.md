# Public information portal site assembly r0.1

status: NON_PRODUCTION_READ_ONLY_ASSEMBLY
public_ready: false
deployment: none
pages_dns_https: unchanged
credentials: none
state_database: none

> **NON-PRODUCTION PREVIEW — STATUS IS NOT AUTHORITY**

## 1. Назначение

Этот пакет собирает будущую структуру публичного информационного портала из фактических GitHub-источников.

Портал является representation layer над GitHub-полем. Он не хранит отдельное «состояние проекта» и не имеет права повышать статус источника.

## 2. Главная

### БЛАГОПОЛУЧИЕ

Candidate public explanation существует в:
`wellbeing-log16/docs/public/project/what-is-wellbeing.md`.

Literal status: **draft**.

В r0.1 этот текст может показываться только как candidate preview с явным draft badge.

Проверенное текущее состояние самого portal lane задаётся KOO:
`OPERATOR_DIRECTION_RECORDED`.

Public-ready claim отсутствует.

## 3. Текущие разработки

### Public information portal

State: **current verified metadata / preview only**.

KOO восстановил GitHub information-field/site lane как независимую public-information ветку. SHD admission gate для r2 закрыт PASS, поэтому site assembly разрешён как bounded non-production work.

### Entity AI resource boosters

State: **current verified metadata / preview only**.

Priority:
`OPERATOR_PRIORITY_CONFIRMED`.

Current gate:
`TECHNICAL_PREP_VERIFIED_WAITING_LIVE_GATES`.

Портал не должен превращать это в утверждение, что live provider path уже работает.

### Telegram facilitator

State: **current verified metadata / preview only**.

Product direction:
`OPERATOR_APPROVED_PRODUCT_DIRECTION`.

Текущий bounded domain-layer развивается независимо от live transport.

Host/runtime gate Phase 1B:
`BLOCKED_PRIVILEGE_REQUIRED`.

Портал показывает blocker class, но не публикует приватные runtime paths/config details.

## 4. Завершённые проверенные рубежи

- Information Entry Stage B:
  `ACCEPTED_AS_BOUNDED_NONPRODUCTION_BASELINE`.
- WEB static preview representation contract:
  `ACCEPTED_BOUNDED_REPRESENTATION_ONLY`.
- Static Preview v0.3 E1 closure:
  `ACCEPTED_PASS_STATIC_PREVIEW_V03_E1_NARROW_RECHECK`.
- SHD cross-layer re-verification r2:
  `PASS_SHD_GITHUB_INFO_ENTRY_R2_CROSS_LAYER_REVERIFY_R01`.

Все эти рубежи являются bounded project achievements. Ни один из них сам по себе не равен public release.

## 5. Активные blockers / verification gates

### AI boosters live execution

Current state:
`TECHNICAL_PREP_VERIFIED_WAITING_LIVE_GATES`.

Remaining gate classes:
- provider/account/project selection;
- billing/account readiness;
- model entitlement;
- private project-scoped credential;
- live executor attachment and independent verification;
- durable live-worker limits/ledger;
- exact operator authority for one bounded call.

### Telegram Phase 1B host runtime

Current state:
`BLOCKED_PRIVILEGE_REQUIRED`.

Reason class:
accepted runtime namespace requires separately authorized privilege/provisioning.

### Portal release

Current state:
**NOT PUBLIC READY**.

Reasons:
- candidate content remains draft/working/skeleton;
- no release authorization;
- no Pages/DNS/HTTPS deployment;
- HQ operational data is metadata-only;
- public/legal/editorial gates are not inferred from repository visibility.

## 6. Участие / кооперация

### Участие

Candidate sources:
- `docs/public/participation/how-to-start.md` — draft;
- `docs/public/tasks/open-task-classes.md` — skeleton.

The future `/participate/` route may preview these with visible status labels.

### Кооперация

No public-safe cooperation projection is admitted in r0.1.

Future route:
`/cooperation/`

Current rendering:
**PUBLIC PROJECTION NOT YET VERIFIED**.

This is an empty/blocked state, not an absence claim about the cooperation project itself.

## 7. Knowledge / FAQ

Candidate source:
`wellbeing-log16/docs/public/`.

Routes:
- `/knowledge/`;
- `/knowledge/answers/`;
- `/faq/`.

Literal states are working/draft and must remain visible.

The log16 `current-stage.md` page is marked **STALE_RISK** because its draft state has not been reconciled to current HQ state.

## 8. Публикации

Future route:
`/publications/`.

r0.1 admits only the working publication-boundary document as a preview boundary.

No approved publication feed is admitted.

Rendering:
**NO APPROVED PUBLICATION INDEX SELECTED IN R0.1**.

## 9. State vocabulary

### current

Verified current project metadata. Does not mean public-ready.

### candidate

Draft/working/skeleton material visible only in non-production preview.

### historical

Preserved prior accepted evidence that is not current.

### superseded

Historical object with a newer accepted state. It must not appear in current navigation.

### withdrawn

Explicit bucket exists. No verified withdrawn public-safe object is admitted in r0.1, so it renders empty.

### blocked / unknown

Fail closed. Show reason/next gate, suppress content when needed.

## 10. Deterministic source-to-route mapping

Exact mapping lives in:
`route-map.json`.

Rules:
- one normalized route maps to a stable ordered list of source ids;
- each source id resolves through `content-eligibility-ledger.json`;
- route rendering never changes semantic/release state;
- HQ sources use metadata projection only;
- log16 candidate sources keep literal status badges;
- empty blocked routes remain explicit;
- source changes require new source commit/blob identities in a future assembly revision.

## 11. No independent database

There is no portal state DB.

The machine-readable ledger is a build/review artifact generated from pinned GitHub source identities. It is not authoritative project state.

Future implementation must rebuild from source objects rather than update the ledger as an independent truth store.

---
created_by: WEB
purpose: non-production read-only public information portal assembly
project_time: omitted; trusted project-time source not used
