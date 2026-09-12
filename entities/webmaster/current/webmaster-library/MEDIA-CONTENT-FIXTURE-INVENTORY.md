# WEB: inventory живых content-class fixtures

status: working-research
purpose: подготовить реальные тестовые объекты для будущей media/content routing matrix
production_changed: false
repository_settings_changed: false

## 1. Зачем

Будущую медиамаршрутизацию лучше проверять на существующих материалах с реальными статусами, а не на абстрактных примерах.

Этот inventory не повышает статусы исходных объектов и не разрешает их публикацию.

## 2. Publicism / literary publication

### Fixture PUBL-001

Repository:
`puev5691/wellbeing-hq`

Artifact:
`entities/redaktor/outbox/RED__publication-snachala-ona-byla-vydumana__KOO.md`

Blob:
`01a6aebe57bfb23932ef335d26d18b728bfb7a2d`

Declared RED class:
- публицистика / авторский литературный материал;
- история проекта;
- материал будущей книги/серии.

Current state:
- review candidate;
- not published;
- KOO received/reviewed, acceptance not granted;
- KAN public-boundary review in progress;
- WEB representation not started.

Use:
Primary fixture for long-form publicism + teaser derivative + canonical/full-text distinction.

## 3. Status / project update

### Fixture STATUS-001

Repository:
`puev5691/wellbeing-log16`

Path:
`docs/public/status/current-stage.md`

Blob:
`95f41c8d24b84f1e9f2ea2fbec95e6c9db58d4b1`

Literal status:
`draft`

Content:
- current milestone `v0.3.0-lab`;
- what is confirmed;
- what is not ready;
- correct expectation for users.

Use:
Fixture for durable status/update page.

Important:
This is not yet a verified generic `news item`. It is a status page draft.

## 4. Technical explanation / setup guidance

### Fixture TECH-001

Repository:
`puev5691/wellbeing-log16`

Path:
`docs/public/faq/local-ai-requirements.md`

Blob:
`c2a05a9c1c12f389780d28c1a943cb2ff16679dc`

Literal status:
`draft`

Content:
- Linux-like environment;
- bash/git/Python;
- Ollama;
- qwen3:8b;
- log16 runtime;
- diagnostic commands.

Use:
Fixture for technical FAQ/setup material.

### Fixture TECH-002

Path:
`docs/public/faq/windows-support.md`

Blob:
`e506a821d96ce59ce9dbb04596771c36c3ad68fe`

Literal status:
`draft`

Use:
Fixture for platform-specific technical guidance with explicit uncertainty/limitations.

## 5. Onboarding / educational path

### Fixture EDU-001

Repository:
`puev5691/wellbeing-log16`

Path:
`docs/public/participation/how-to-start.md`

Blob:
`7c1f88623fbb916e6f8310e70350a88e5ed9e6c5`

Literal status:
`draft`

Content structure:
- reader;
- GitHub user;
- local AI tester;
- developer;
- infrastructure contributor.

Use:
Fixture for onboarding/learning-path material.

## 6. Reusable practical answer cards

### Fixture CARD-001

Repository:
`puev5691/wellbeing-log16`

Path:
`docs/public/knowledge-base/answers/index.md`

Blob:
`321c33d3374e0d1f897b46277b25f5e8e6bd4149`

Literal status:
`working`

Index includes reusable cards for:
- project explanation;
- system explanation;
- current stage;
- local AI requirements;
- Windows support;
- participation;
- limitations.

Use:
Fixture family for short reusable cards / tips / FAQ-derived derivatives.

Note:
Not every answer card is a `лайфхак`; the reusable-card format is the relevant routing mechanism.

## 7. Community / participation

### Fixture COMM-001

Repository:
`puev5691/wellbeing-log16`

Path:
`docs/public/faq/how-to-help.md`

Blob:
`77e9ccb9d0ab82a465136785725d759d8529b029`

Literal status:
`draft`

Use:
Fixture for volunteer/contributor call and participation explanation.

### Fixture COMM-002

Path:
`docs/public/tasks/open-task-classes.md`

Blob:
`ff334bad8a6495b19011b6157a91b613330a8de6`

Literal status:
`skeleton`

Use:
Fixture for public task taxonomy / contributor entry.

## 8. Research / evidence material

### Fixture RESEARCH-001

Repository:
`puev5691/wellbeing-hq`

Path:
`entities/volonter/current/coop-meeting/analysis/VOL_cooperation-research-brief_KOO.md`

Blob:
`51c48ef66026ab42684cd2f8f070127fc713d803`

Document status:
`handoff_candidate / awaiting_KOO_receipt`

Content:
- research contour `КООПЕРАЦИЯ`;
- source classes;
- research literature;
- normalized cards;
- derived studies;
- practical cases;
- evidence map / speech-source linkage.

Use:
Fixture for research-to-public-knowledge transformation.

Important:
Raw research brief is **not** automatically a public publication. It is useful precisely as a source that may yield later public syntheses/cards.

## 9. Publication-readiness checklist

### Fixture PROCESS-001

Repository:
`puev5691/wellbeing-log16`

Path:
`docs/productization/log16-publication-readiness-checklist-v01.md`

Blob:
`125da05ec224c43c65f475a019a53d5a3c46b95a`

Literal status:
`working`

Use:
Process fixture for checking documentation/public knowledge/participation/publication readiness.

Important:
This checklist belongs to log16 productization and cannot be promoted to universal project editorial policy without RED/KOO review.

## 10. Missing live fixture: NEWS

During this scan WEB did **not** verify a dedicated object with an explicit semantic class like:

`news_item` / `news_post` / `project_news`.

Commits, status pages, release events and milestones must not be automatically treated as news simply because they are recent.

Therefore:

`NEWS fixture status: MISSING / NEEDS DESIGN OR FIRST REAL OBJECT`

Questions for future RED/KOO media-routing result:
- what exactly qualifies as news;
- what requires a full source article vs short event card;
- can release/milestone events generate news automatically;
- what facts can be rendered without separate editorial rewrite;
- retention/archive behavior of news feed.

## 11. Candidate routing dimensions suggested by these fixtures

Future matrix should distinguish at least:

| Layer | Typical primary object | Likely derivatives | Current fixture |
|---|---|---|---|
| publicism | full article | teaser, quote card, channel announcement | PUBL-001 |
| status/update | durable status page | short update card, feed event | STATUS-001 |
| technical | FAQ/guide | checklist, short answer, search snippet | TECH-001/002 |
| education/onboarding | learning path | step card, task entry | EDU-001 |
| reusable cards | answer card | bot/search/FAQ derivative | CARD-001 |
| community | participation/task page | call-to-action post | COMM-001/002 |
| research | source/evidence brief | reviewed synthesis, source card | RESEARCH-001 |
| news | dedicated news object | feed/Telegram/social derivative | missing |


These are working routing dimensions, not editorial policy.

## 12. Media-system implication

One material may participate in several layers, but one layer should not be inferred solely from platform.

Example:
`Telegram post` may be news, teaser, community call, technical alert or publication announcement.

Therefore future metadata likely needs both:
- `content_layer`;
- `distribution_target`.

Platform cannot substitute for content semantics.

## 13. Short experience note

Идея → заменить абстрактные content-class examples реальными project artifacts.

Проба → inspected RED literary candidate, log16 public docs/cards/status/onboarding, cooperation research brief and publication-readiness checklist.

Результат → fixtures exist for publicism, status, technical, education, reusable cards, community and research.

Negative result → no dedicated verified NEWS object found.

Value → future routing matrix can be tested against actual statuses and provenance instead of generic placeholders.

---
created_by: WEB
document_type: media-content-fixture-inventory
project_time: not_recorded_no_trusted_source