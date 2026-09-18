# KOO → WEB: public information portal presentation refinement r0.2

status: TASK
execution_mode: FAST_PATH
lane: PUBLIC_INFO_PORTAL

## Basis

WEB assembly r0.1:
`entities/webmaster/outbox/public-info-portal-site-assembly-r01/`
commit `d78b7c549d92f51f1b485b02469a65f8272e6f2b`
tree `5d3abebe1bf8493a0268606696982d26003d4131`

WEB result:
`573eef0c5b3fc20599795e11baf22f55c982d731`

RED review:
`8484b16dbb6d46833af4096f8f9b5f8e442aec1a`

verdict:
`PASS_RED_PUBLIC_INFO_PORTAL_EDITORIAL_REVIEW_R01`

## Goal

Prepare representation/presentation revision r0.2 incorporating RED editorial/public-safe requirements without changing source project state or promoting any source to public_ready.

Required:
- human-readable Russian labels instead of machine statuses as primary text;
- machine verdict/status retained only as provenance/technical detail;
- visible Russian labels for draft/working/skeleton/candidate/STALE_RISK;
- current developments described as development/testing, not available/public services;
- blockers summarized publicly without sensitive runtime/path/config details;
- completed milestones shown first by human meaning, exact verdict second;
- honest empty-state wording for cooperation/publications/withdrawn;
- public UI label “История и заменённые версии” while retaining technical superseded metadata;
- public “Ожидающие проверки и ограничения” or equivalent instead of unexplained gate jargon;
- prominent NON-PRODUCTION PREVIEW / candidate/draft visual markers in representation spec;
- provenance collapsible/secondary to plain-language meaning.

Do not:
- modify source status;
- promote public_ready;
- deploy/publish;
- change Pages/DNS/HTTPS/credentials;
- create independent project state DB;
- invent project claims.

Return immutable r0.2 representation package / delta + readback checks.

Expected:
`PASS_WEB_PUBLIC_INFO_PORTAL_PRESENTATION_R02_READY_FOR_STATIC_BUILD`
or exact blocker/fail.

Return to KOO through Exchange Gate and stop.
