# WEB: Telegram media-gateway Phase 0 test contract

status: working-test-contract
scope: credential-free non-production implementation fixture
production_changed: false
repository_settings_changed: false

## Purpose

Give KOD/SHD/SIS an exact testable contract for Media Gateway Phase 0 before any real Telegram bot token, channel, group or webhook exists.

This file is not implementation code and does not authorize production.

## 1. Required component behavior

Phase 0 implementation must support:

1. publication input validation;
2. idempotency by `publication_id + target_channel`;
3. renderer/derivative payload;
4. fake Telegram adapter;
5. simulated Bot API send result;
6. simulated linked-discussion auto-forward;
7. comment ingestion;
8. reaction-count ingestion;
9. member-count snapshots;
10. delivery state persistence;
11. restart/reload test;
12. safe public receipt export without audience identity.

## 2. Synthetic publication input

Use only synthetic test content:

```json
{
  "publication_id": "tg-sandbox-fixture-001",
  "environment": "sandbox",
  "synthetic": true,
  "content_layer": "system-test",
  "source_identity": {
    "scheme": "synthetic",
    "id": "tg-phase0-fixture-001"
  },
  "canonical": {
    "url": "https://example.invalid/wellbeing/tg-phase0-fixture-001",
    "readback_state": "synthetic_pass"
  },
  "release": {
    "state": "synthetic_authorized_for_test_only"
  },
  "target": {
    "platform": "telegram",
    "channel_key": "sandbox-channel"
  },
  "derivative": {
    "type": "telegram-test-message",
    "text": "SANDBOX TEST: wellbeing media-gateway fixture. No public project content."
  }
}
```

`example.invalid` is intentionally non-public/non-routable and must never be treated as a real canonical URL.

## 3. Fake send result

Fake Telegram adapter returns:

```json
{
  "ok": true,
  "result": {
    "message_id": 1001,
    "chat": {
      "id": -1001000000001,
      "type": "channel",
      "title": "WB Sandbox Channel"
    },
    "date": 1,
    "text": "SANDBOX TEST: wellbeing media-gateway fixture. No public project content."
  }
}
```

Expected gateway state:

`prepared → dispatching → delivered_unverified`

After simulated webhook echo/readback:

`delivered_unverified → delivered_verified`

## 4. Simulated automatic forward to linked discussion

Input update fixture:

```json
{
  "update_id": 5001,
  "message": {
    "message_id": 2001,
    "chat": {
      "id": -1002000000002,
      "type": "supergroup",
      "title": "WB Sandbox Discussion"
    },
    "date": 2,
    "is_automatic_forward": true,
    "forward_origin": {
      "type": "channel",
      "date": 1,
      "chat": {
        "id": -1001000000001,
        "type": "channel",
        "title": "WB Sandbox Channel"
      },
      "message_id": 1001
    }
  }
}
```

Expected mapping:

`publication_id = tg-sandbox-fixture-001`
`channel_message_id = 1001`
`discussion_chat_id = -1002000000002`
`discussion_root_message_id = 2001`

## 5. Simulated comment

Input:

```json
{
  "update_id": 5002,
  "message": {
    "message_id": 2002,
    "message_thread_id": 2001,
    "chat": {
      "id": -1002000000002,
      "type": "supergroup"
    },
    "from": {
      "id": 424242,
      "is_bot": false,
      "first_name": "Test User"
    },
    "date": 3,
    "reply_to_message": {
      "message_id": 2001,
      "chat": {
        "id": -1002000000002,
        "type": "supergroup"
      }
    },
    "text": "Тестовый комментарий."
  }
}
```

Private runtime may store the test identity.

Safe exported receipt must NOT contain:
- user id `424242`;
- first name;
- raw comment text unless explicitly requested for a private test artifact.

Expected aggregate:

`comments_count = 1`

## 6. Simulated reaction count

Input:

```json
{
  "update_id": 5003,
  "message_reaction_count": {
    "chat": {
      "id": -1001000000001,
      "type": "channel"
    },
    "message_id": 1001,
    "date": 4,
    "reactions": [
      {
        "type": {"type": "emoji", "emoji": "👍"},
        "total_count": 2
      },
      {
        "type": {"type": "emoji", "emoji": "❤"},
        "total_count": 1
      }
    ]
  }
}
```

Expected aggregate:

`👍 = 2`
`❤ = 1`
`reaction_total = 3`

## 7. Member snapshots

Fake adapter responses:

`channel_member_count = 10`
`discussion_member_count = 5`

Expected:
- one timestamped/synthetic snapshot per chat;
- no inference of subscriber growth from a single snapshot.

## 8. Duplicate publication event

Replay the exact same publication input.

Expected:
- no second Telegram send;
- original `channel_message_id=1001` remains authoritative;
- idempotency result explicitly reports duplicate/no-op;
- no duplicated discussion mapping.

## 9. Duplicate webhook update

Replay `update_id=5002`.

Expected:
- comments count remains 1;
- duplicate update is ignored or marked already processed.

## 10. Correction fixture

Input correction:

```json
{
  "publication_id": "tg-sandbox-fixture-001",
  "action": "correct",
  "revision": 2,
  "derivative": {
    "text": "SANDBOX TEST v2: corrected test message. No public project content."
  }
}
```

Expected:
- fake adapter receives edit request for message `1001`;
- previous payload hash/version preserved;
- state records correction;
- new send is NOT created.

## 11. Restart recovery

Test:

1. persist state after comment/reaction ingestion;
2. stop service;
3. restart using same DB;
4. query publication.

Expected state after restart:
- message id 1001;
- discussion root 2001;
- comments count 1;
- reactions total 3;
- corrected revision if correction test already applied;
- no duplicate publication.

## 12. Safe receipt output

Expected public-safe result shape:

```json
{
  "publication_id": "tg-sandbox-fixture-001",
  "environment": "sandbox",
  "delivery_state": "delivered_verified",
  "channel_message_id": 1001,
  "discussion_root_message_id": 2001,
  "comments_count": 1,
  "reaction_total": 3,
  "channel_member_count": 10,
  "discussion_member_count": 5,
  "synthetic": true,
  "personal_data_exported": false,
  "production_publication": false
}
```

## 13. Required negative tests

- malformed publication id;
- missing target;
- missing derivative;
- duplicate publication event;
- duplicate update id;
- auto-forward references unknown channel message id;
- comment thread references unknown discussion root;
- reaction update references unknown publication;
- DB write failure;
- adapter send failure;
- adapter edit failure;
- restart during `dispatching`;
- attempt to export raw user identity.

All failures must produce explicit state/error, not silent loss.

## 14. PASS criteria

Phase 0 PASS only if:

- all positive fixtures pass;
- all negative fixtures fail safely;
- exported result contains no test user identity;
- no Telegram credentials are required;
- no network call to Telegram is required;
- process restart preserves state;
- duplicate events are idempotent;
- exact test artifacts/results are file-backed and reproducible.

## 15. Handoff

After KOO assigns implementation:

- KOD owns code correctness/tests;
- SHD may independently reproduce fixtures and integration evidence;
- SIS prepares Phase 1 runtime separately;
- WEB verifies contract conformance and publication/message mapping.

---
created_by: WEB
document_type: telegram-media-gateway-phase0-test-contract
purpose: provide credential-free exact fixtures and acceptance criteria before Telegram sandbox integration
project_time: not_recorded_no_trusted_source