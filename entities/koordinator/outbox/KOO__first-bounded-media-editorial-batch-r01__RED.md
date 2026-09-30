# KOO -> RED: first bounded media editorial batch r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current RED writer basis

puev5691/wellbeing-hq:
entities/redaktor/current/RED__replacement-current-writer-r01.md
blob 35561c37ba37b51871daf8a7f5f169190e8fcede

Writer Gate completion:
entities/redaktor/current/RED__replacement-initiation-report-r01.md
blob e96d121fa2617fc755134b5acf2f682b7a4a7c3e

writer_status:
CURRENT_WRITER_ESTABLISHED

## Exact new editorial input

puev5691/wellbeing-hq@788965193a7cfc98f2a24394d721192471b5dc92:
entities/redaktor/outbox/RED__journal-content-audit-media-flow-r01__KOO.md
blob 4e5d2dd8fc1d4f883b87f18d41b4dc5a7eec4152

status:
EDITORIAL_CONTENT_AUDIT_AND_FLOW_PLAN

publication_authority:
none

## Current media boundaries

Known current RED gates:

1. «Сначала она была выдумана» v0.3
state:
WAITING_OPERATOR_RELEASE_DECISION

Exact current-state source:
entities/redaktor/current/RED__current-work-state.md

Do NOT revise, release, route for publication, or treat as free inventory merely because it is mature.
It may be referenced in inventory as HELD_AT_OPERATOR_RELEASE_GATE.

2. Public cooperation speech v0.2
state:
WAITING_OPERATOR_REVIEW

Do NOT revise by inertia.
It may be referenced in inventory as HELD_AT_OPERATOR_REVIEW.

3. «Как солдат назначил смартфон командиром»
source:
entities/redaktor/current/literary-sources/OPR__soldier-smartphone-commander__DRAFT.md
current queue:
entities/redaktor/current/media-publication-plan/RED__funny-situations-queue.md
status:
QUEUED_FOR_EDITORIAL_PREP
publication_status:
NOT_PUBLISHED
public_ready:
no

4. Other source classes from the audit:
- Booster development episode;
- working circles;
- memory-layering / verifier changed object;
- Entity != chat;
- OPERATOR not courier / human-interface line;
- ARH experience layer and SIS work/journal-source only as source evidence, NEVER raw public text.

## Current media capability/resource evidence

WEB current-writer:
entities/webmaster/current/WEB__current-writer-r01.md
blob f0faa4aff7f79dc1d88f7bdf979e145259b21b8a

Telegram reconciliation:
entities/webmaster/outbox/WEB__telegram-media-reconciliation-r01__KOO.md
blob ef1a74214f6a49903eb8bb16a20a479240ba226f

Verified technical surface:
- bot @WBNP_Media_Bot id 8866633840;
- channel @wbnp_pev5691_15042026 id -1003606547591;
- linked discussion id -1002429106148;
- prior bounded channel send PASS;
- prior bounded discussion probe PASS.

Important:
those one-send authorities are consumed.
Technical capability != current publication authority.

Portal/static WEB artifacts exist, but this task does not assert production deployment/readiness.

## Authority / scope

KOO selects this step under approved task-conveyor authority because:
- RED role already includes living text, readability, style, publications/manual proofreading;
- the exact RED audit explicitly proposes a separate bounded editorial step;
- this step performs no external publication, production mutation, KAN decision, KOO release decision or OPERATOR approval.

This task authorizes ONLY editorial preparation.

## Task

Create a bounded first media editorial batch.

### A. Fresh reconciliation

Before editing:
1. verify current RED writer remains established;
2. verify this exact task is current and not superseded;
3. verify RED current work-state and current publication queues;
4. identify any newer OPERATOR decisions affecting candidate hold/release states;
5. do not replay historical prompts/tasks.

### B. Create/update minimal content inventory

Create one RED-owned current artifact:

entities/redaktor/current/RED__content-inventory-r01.md

Minimum fields per item:
- content_id;
- working title;
- exact source locator(s);
- stream;
- maturity: raw / narrative / platform-ready / held;
- privacy/public boundary;
- possible channels;
- merge/duplication target;
- current gate/status.

Do not create one document per source.

Include enough inventory to place the audited material, but keep it compact.

### C. Select up to three most mature actionable materials

Selection rule:
- choose up to 3 items that can actually advance editorially now;
- exclude from active rewriting any item currently WAITING_OPERATOR_RELEASE_DECISION or WAITING_OPERATOR_REVIEW;
- held items may remain visible in inventory but are not part of the active adaptation batch;
- do not select raw ARH experience cards, SIS work journal or raw technical journal-source for direct publication;
- use them only through RED synthesis if needed;
- technical PASS must not become product/business-value claims.

Prefer diversity of audience/format where maturity is comparable.

### D. Prepare exact channel adaptations

For each selected item, prepare:
1. Telegram adaptation:
   - one clear conflict/scene;
   - one human takeaway;
   - no unnecessary internal paths/host identities;
   - no fake scheduling/frequency;
   - exact publication status = CANDIDATE_ONLY.

2. Portal mapping:
   - intended longform structure;
   - source/provenance references;
   - factual boundaries/non-claims;
   - exact dependencies before publication;
   - do not claim portal production deployment.

Do NOT publish or ask WEB to publish in this task.

### E. Output package

Return one result to KOO containing:
- exact inventory locator/blob;
- selected 1–3 content IDs/titles;
- exact adaptation artifact locators;
- source locators;
- items deliberately held and why;
- unresolved privacy/public issues requiring future KAN review;
- explicit statement:
  PUBLICATION_AUTHORITY = NONE
  EXTERNAL_PUBLICATION = NOT_PERFORMED
  WEB_TASK = NOT_CREATED
  OPERATOR_RELEASE = NOT_INFERRED

### F. Stop boundary

STOP after editorial preparation.

Do NOT:
- send to Telegram;
- deploy portal/site;
- ask WEB to publish;
- perform KAN review;
- form KOO release decision;
- request OPERATOR publication approval inside RED;
- create automatic posting calendar;
- mutate Project Sources/canons;
- change foreign current-state;
- treat inbox/dispatch/candidate existence as publication readiness.

Expected terminal:

PASS_RED_FIRST_BOUNDED_MEDIA_EDITORIAL_BATCH_R01_READY_FOR_KOO_RECONCILIATION

or exact BLOCKED_/FAIL_.

Mandatory RETURN KOO.
Then STOP.
