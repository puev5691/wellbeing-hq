# KOO → KAN: Telegram privacy gate decision

status: ACCEPTED_BOUNDED_WITH_PRE_LIVE_FIXES
phase1b_live_send: NOT_AUTHORIZED

## Accepted profile boundary

KAN result:
`PASS_BOUNDED_WITH_PRE_LIVE_PRIVACY_FIXES`.

For the current bounded sandbox, KOO selects:
`privacy_mode = aggregate_only`.

Allowed retained audience-derived state:
- comments_count;
- reaction_total;
- member_count;
- technical publication/delivery identifiers required by the gateway.

Forbidden retained/exported state:
- user ids;
- usernames/names;
- raw comment bodies;
- per-user history;
- identity hashes preserving linkability;
- identifiable audience profiles.

Raw comment text may exist only transiently in memory and must not enter persistent logs, retry/dead-letter storage, GitHub evidence, LLM processing or embeddings.

Aggregate sandbox DB retention:
delete live Telegram-derived aggregate state within 30 days after KOO closes Phase 1B unless a newer explicit decision supersedes this rule.

## Pre-live blockers

1. KOD must replace stale `fail_closed_pending_KAN` receipt semantics with actual privacy mode + policy marker.
2. SIS must prove request-body/application logging is fail-closed for raw Telegram updates.
3. SIS/KOD must identify the sandbox DB path and executable cleanup action.

No credential, webhook, channel-admin or live-send authority is granted here.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать принятый privacy-mode и точные условия до Phase 1B
СТАТУС: accepted_bounded_with_pre_live_fixes
