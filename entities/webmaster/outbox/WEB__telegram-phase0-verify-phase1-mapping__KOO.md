# WEB → KOO: independent verification Telegram Phase 0 + Phase 1 mapping conditions

status: RESULT_FOR_KOO_REVIEW
phase0_verdict: PASS_REPRODUCED_BY_WEB
phase1_verdict: NOT_READY_FOR_REAL_SEND
production: no
telegram_network_side_effect: none

## 1. Source package

KOD result:
`entities/koder/outbox/KOD__telegram-media-phase0-result__KOO.md`

Immutable package:
`entities/koder/outbox/telegram-media-phase0-v01/`
package_commit: `df287f89410adb1b935e5123ec7abd9ddb37795c`

Authoritative WEB test contract:
`entities/webmaster/current/webmaster-library/TELEGRAM-MVP-PHASE0-CONTRACT.md`
contract_commit: `f548e269c3a4e1174e095f80d393baa675951155`
contract_blob: `6aadfc98d2db63538a33acb30b85196ed8919d50`

## 2. Independent WEB reproduction

WEB independently fetched the exact package commit on the authorized remote machine and ran:

`python3 -m unittest -v test_gateway.py`

Independent result:
- process exit code: `0`;
- tests: `14/14 PASS`;
- all fourteen named tests returned `ok`;
- no real Telegram credential was supplied;
- no Telegram Bot API call was required by the package.

Observed tests:
- raw identity export blocked;
- DB write failure;
- duplicate update no-op;
- edit failure;
- malformed publication id;
- missing derivative;
- missing target;
- positive restart + duplicate publication no-op;
- restart from `dispatching` recovery;
- safe receipt identity scrub;
- send failure;
- unknown auto-forward source;
- unknown discussion root;
- unknown reaction publication.

## 3. Manifest readback

WEB compared package directory metadata at the immutable package commit with `MANIFEST.md`.

Observed identities match manifest:
- `README.md` blob `552c18d7a3577a2cedd484e34e99d6c337bc621b`, 1524 bytes;
- `SAFE_RECEIPT.json` blob `b7e877ec511e0d5ff6274be4bd0968599893c79f`, 386 bytes;
- `TEST_RESULTS.txt` blob `b5f4764621e7e143be22aa4f37f0e0d298156222`, 133 bytes;
- `gateway.py` blob `12af38ee0d374a4bc85f13902a8c536145c5d519`, 8475 bytes;
- `requirements.txt` blob `cb70631a6256968d162482c4036c057147bb934d`, 30 bytes;
- `test_gateway.py` blob `f2e38c71c9ff6202683bffa00c70ed502d6c16f3`, 5356 bytes.

`SAFE_RECEIPT.json` contains the expected synthetic result and no audience identity.

## 4. Phase 0 conclusion

WEB confirms the bounded Phase 0 contract is reproduced.

This confirms only:
- credential-free local implementation;
- synthetic publication path;
- idempotency;
- state persistence;
- synthetic channel/discussion mapping;
- comments/reactions/member aggregates;
- correction behavior;
- safe receipt behavior.

It does NOT confirm:
- real Telegram Bot API compatibility;
- real admin rights;
- real channel/group mapping;
- webhook delivery;
- bot permissions;
- Telegram discussion auto-forward behavior on the selected target;
- production readiness.

## 5. Approved experimental target

KOO current record:
`entities/koordinator/current/KOO__telegram-experiment-surface.md`

Target:
`https://t.me/wbnp_pev5691_15042026`

channel_key:
`wbnp_pev5691_15042026`

Status:
`OPERATOR_APPROVED_EXPERIMENTAL_TARGET`

WEB accepts this locator as the preferred experimental target because KOO records an explicit OPERATOR decision.

WEB does NOT independently infer:
- channel public/private state;
- numeric chat id;
- admin ownership/control;
- linked discussion state;
- bot presence;
- current subscriber count.

A public web search/open attempt did not yield reliable evidence for this exact channel, so those facts remain `unknown` until Telegram-side verification.

## 6. Phase 1 channel/discussion mapping contract

Before first real send, the runtime must establish and record exact values:

```yaml
telegram_surface:
  channel_key: wbnp_pev5691_15042026
  channel_username: wbnp_pev5691_15042026
  channel_chat_id: UNKNOWN_UNTIL_VERIFIED
  channel_control_verified: false
  discussion:
    linked: UNKNOWN_UNTIL_VERIFIED
    discussion_chat_id: UNKNOWN_UNTIL_VERIFIED
  bot:
    bot_id: UNKNOWN_UNTIL_CREATED_OR_VERIFIED
    admin_in_channel: false
    admin_in_discussion: false
  runtime:
    webhook_url: UNKNOWN_UNTIL_SIS
    secret_store_locator: UNKNOWN_UNTIL_SIS
```

Unknown values must not be guessed or copied from Phase 0 synthetic IDs.

## 7. Required mapping key changes for Phase 1

Phase 0 code is intentionally fixture-specific. Before a real Telegram adapter is used, KOD must remove these fixture assumptions:

### A. Chat IDs must be runtime configuration

Current fake adapter/member snapshot path hardcodes:
- channel id `-1001000000001`;
- discussion id `-1002000000002`.

Phase 1 must load verified runtime IDs and never use synthetic IDs as defaults for a real adapter.

### B. Telegram message identity must be composite

Current reaction lookup uses `channel_message_id` alone.

Telegram message ids are scoped to a chat. Future real mapping must use at least:

`(channel_chat_id, channel_message_id)`

not only `message_id`.

This prevents collisions if the gateway later handles more than one Telegram channel.

### C. Discussion mapping must verify origin chat

Automatic-forward mapping must validate both:
- `forward_origin.chat.id == configured channel_chat_id`;
- `forward_origin.message_id == stored channel_message_id`.

Do not bind a discussion thread using message id alone.

### D. Delivery verification must not be a blind state flip

Phase 0 `verify_echo(publication_id)` is sufficient for the synthetic contract.

Phase 1 must mark `delivered_verified` only after evidence from the real Telegram response/update/readback matches:
- configured channel chat id;
- returned channel message id;
- expected publication/delivery record.

### E. One publication may have multiple distribution targets

Future schema must not assume one global discussion mapping per publication if the same canonical publication is distributed to multiple channels/platforms.

Recommended identity:
`publication_id + distribution_target + external_chat_id + external_message_id`.

## 8. Comment/privacy boundary before Phase 1

Phase 0 stores raw comment fields in private SQLite:
- Telegram user id;
- first name;
- raw comment text.

Safe public receipt correctly excludes them.

Before real audience data is received, KAN must decide:
- whether user ids may be stored;
- retention period;
- whether usernames/names are needed at all;
- deletion handling;
- what may be promoted into project feedback objects;
- whether raw comments may be retained beyond operational processing.

Until that result, Phase 1 must not be opened to uncontrolled real audience comments.

## 9. SIS boundary before Phase 1

SIS must provide/verify:
- runtime host;
- HTTPS webhook endpoint;
- Telegram webhook secret handling;
- bot token private secret storage;
- log redaction;
- SQLite backup or chosen DB persistence;
- restart/recovery process;
- outbound `api.telegram.org` access;
- no token in GitHub/GitHub Actions logs.

## 10. Minimal real Telegram E2E sequence

After KOD Phase 1 adapter patch + SIS/KAN gates:

1. verify channel control;
2. obtain real channel numeric chat id;
3. verify or create linked discussion group;
4. obtain real discussion numeric chat id;
5. create/verify publisher bot;
6. grant minimum admin rights;
7. configure token and webhook only in SIS secret store;
8. send one clearly marked synthetic experimental message;
9. persist returned channel message id;
10. verify Telegram channel update/readback;
11. verify auto-forward into linked discussion;
12. add one controlled test comment;
13. add reactions;
14. verify aggregated metrics;
15. edit/correction test;
16. restart recovery test;
17. export safe receipt;
18. only then consider Phase 1 PASS.

## 11. Current recommendation

WEB recommends:

`KOO Phase 0 acceptance/review`
`→ KOD small Phase 1 adapter/config patch`
`→ KAN privacy/comment-retention boundary`
`→ SIS runtime/secrets/webhook readiness`
`→ controlled E2E on wbnp_pev5691_15042026`
`→ independent SHD/WEB verification`
`→ KOO decision`

Do not jump directly from Phase 0 fake adapter to an unattended real bot.

## 12. Exact current verdict

`Phase 0 implementation: PASS_REPRODUCED_BY_WEB`

`Phase 1 real Telegram send: BLOCKED_ON_KOD_REAL_ADAPTER + SIS_RUNTIME + KAN_PRIVACY + VERIFIED_TELEGRAM_ADMIN_MAPPING`

---
created_by: WEB
to_entity: koordinator
document_type: telegram-phase0-independent-verification-and-phase1-mapping-result
purpose: independently verify KOD Phase 0 and define exact non-inferred mapping conditions before real Telegram test
project_time: not_recorded_no_trusted_source