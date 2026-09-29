# Telegram single-provider Entity dialogue MVP r0.1

Status: implementation candidate for independent review. It has not been deployed and has made no Telegram or OpenAI call.

## Purpose and exact flow

`Telegram getUpdates long polling → closed tester admission → replay claim → per-chat/thread history → bounded Entity bootstrap + OpenAI Responses API → Telegram sendMessage → committed turn`

The candidate serves one provider (`OpenAI`) and one Entity bootstrap. It is intentionally smaller than the Semantic Engine. It supports private text chats admitted by both exact `user_id` and exact `chat_id`.

## Reused project evidence

- Telegram facilitator core independent PASS: commit `947ea4b76d367774fbc2ae37b61d49e0e89d55bc`. Its authority and privacy boundaries are preserved; this MVP does not treat generated text as project authority.
- Normalized-event bridge independent PASS: commit `c0ed7057da344bf6b10b0718960c36962b8d9536`. That bridge is aggregate-only and is not used as raw dialogue ingress.
- Phase1B threading fix: commit `62f82c3322f28adc55b47b1a7064fccb23e4c351`, `gateway.py` blob `c870616f119fa3198a50db31898ad9ba4ad4bafc`. This package reuses its exact-thread routing and replay principles without modifying or importing the publication gateway.
- Phase1B runtime boundary: commit `b939a238f757be0bcfaf1bb4164b0362eafc088f`, `runtime_app.py` blob `f2987f880a25b5e295fd94eadb6447fd2438054d`. This package reuses its systemd credential and privacy-safe logging patterns.
- Bounded OpenAI D0 live evidence: commit `80a87f5920bb26c06c31006b3ccb7a9eabd62bfa`. It proved one exact historical call only. It is not standing provider authority.
- Fresh SIS host/runtime preflight: commit `f8fbde559a7964ac774ce28b5200dce9b66a2fda`, terminal `READY_FOR_BOUNDED_LIVE_PILOT_PROVISIONING`. This package adopts its recommended polling route, service identity, principal and exact paths.
- SHT portable bootstrap candidate: commit `1574c8dd0f688a693a4d870ae65aa6ac9fa262bd`. It remains `CANDIDATE_NOT_ACTIVE`; this package does not silently activate it.

The provider request follows the official Responses API contract: `instructions`, message-array `input`, `max_output_tokens`, `store=false`, and `tools=[]`. The adapter accepts only completed assistant `output_text`. A reasoning-only response triggers the visible fallback.

Multi-turn state is the bounded visible user/assistant transcript managed locally. Provider-side conversation storage and hidden reasoning items are not reused across calls.

Official references used for this candidate:

- <https://developers.openai.com/api/reference/cli/resources/responses/methods/create>
- <https://developers.openai.com/api/docs/guides/conversation-state>
- <https://core.telegram.org/bots/api>

## Files

- `dialogue_mvp.py`: polling runtime, closed config, SQLite ledger/history, provider and Telegram adapters.
- `test_dialogue_mvp.py`: offline fake-transport tests.
- `config.example.json`: non-secret closed-pilot configuration.
- `testers.allow.example`: synthetic root-controlled tester identifier fixture.
- `entity_bootstrap.txt`: bounded initial Entity instructions.
- `wellbeing-telegram-single-entity-pilot.service`: systemd candidate.
- `MANIFEST.json`, `SHA256SUMS`, `SELFTEST.json`: immutable package evidence.

## Admission and state

Admission requires all of the following:

1. `message` update with bounded non-empty text;
2. chat type `private`;
3. exact numeric `user_id` in root-controlled `testers.allow`;
4. exact numeric `chat_id` in the same allowlist;
5. `user_id == chat_id`.

Conversation identity is a SHA-256 projection of `chat_id`, `message_thread_id` and `direct_messages_topic.topic_id`. SQLite stores the bounded user/assistant text required for multi-turn context and the opaque conversation key. It does not store the raw Telegram update, username, display name, provider response body or secret values.

The poll cursor is committed after each handled Telegram update. The transcript is pruned to the configured message-count bound per conversation, and terminal replay records are pruned to their configured count bound. Unresolved records are never removed automatically. This is count-bounded retention; no wall-clock retention claim is made.

`update_id` is reserved with the exact canonical update digest before either external call. An identical committed replay is acknowledged without a second provider/send effect. The same `update_id` with different bytes is a conflict. An in-progress or uncertain replay stops with `manual_reconciliation_required`.

Telegram `sendMessage` has no transaction shared with the local SQLite ledger. A crash after the external send and before local commit therefore becomes `OUTCOME_UNKNOWN`; the runtime will not resend blindly. This is a deliberate fail-closed MVP limit, not an exactly-once claim.

## Offline verification

From the package directory:

```sh
python3 -I -B test_dialogue_mvp.py
python3 -m py_compile dialogue_mvp.py test_dialogue_mvp.py
```

The tests use injected provider and Telegram fakes. They cover one-turn and multi-turn dialogue, chat/thread isolation, exact replay, collision, allowlist and non-message rejection, input bounds, fallback, unknown send outcome, durable poll cursor, exact polling request shape, absence of raw content/identity in logs, exact OpenAI request shape, and reasoning-only rejection.

## Future deployment procedure

These commands are a reviewable runbook for a separately authorized SIS deployment. Before use, SIS must substitute an independently approved live config containing the exact tester IDs and preserve any predecessor bytes/state.

### Pre-state and install

```sh
sudo systemctl status wellbeing-telegram-single-entity-pilot.service --no-pager || true
sudo install -d -o root -g wellbeing-tg-dialog -m 0750 /opt/wellbeing/telegram-single-entity-mvp-r01
sudo install -d -o root -g wellbeing-tg-dialog -m 0750 /etc/wellbeing/telegram-single-entity-pilot
sudo install -d -o root -g root -m 0700 /etc/wellbeing/telegram-single-entity-pilot/secrets
sudo install -d -o wellbeing-tg-dialog -g wellbeing-tg-dialog -m 0750 /var/lib/wellbeing/telegram-single-entity-pilot
sudo install -o root -g wellbeing-tg-dialog -m 0755 dialogue_mvp.py /opt/wellbeing/telegram-single-entity-mvp-r01/dialogue_mvp.py
sudo install -o root -g wellbeing-tg-dialog -m 0644 entity_bootstrap.txt /opt/wellbeing/telegram-single-entity-mvp-r01/entity_bootstrap.txt
sudo install -o root -g wellbeing-tg-dialog -m 0640 LIVE.runtime.json /etc/wellbeing/telegram-single-entity-pilot/runtime.json
sudo install -o root -g wellbeing-tg-dialog -m 0640 LIVE.testers.allow /etc/wellbeing/telegram-single-entity-pilot/testers.allow
sudo install -o root -g root -m 0644 wellbeing-telegram-single-entity-pilot.service /etc/systemd/system/wellbeing-telegram-single-entity-pilot.service
sudo systemd-analyze verify /etc/systemd/system/wellbeing-telegram-single-entity-pilot.service
sudo -u wellbeing-tg-dialog /usr/bin/python3 -I -B /opt/wellbeing/telegram-single-entity-mvp-r01/dialogue_mvp.py check-config --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json
sudo systemctl daemon-reload
```

The service account, two systemd credential sources and state-directory ownership must exist before the config check/start. Credential values must never be put in `runtime.json`, `testers.allow`, shell history, Git or logs.

### Run and verify

```sh
sudo systemctl enable --now wellbeing-telegram-single-entity-pilot.service
sudo systemctl is-active wellbeing-telegram-single-entity-pilot.service
sudo systemctl status wellbeing-telegram-single-entity-pilot.service --no-pager
sudo journalctl -u wellbeing-telegram-single-entity-pilot.service --no-pager -n 50
```

The polling service opens no inbound listener. Before live start, the current webhook state must be checked and, if present, removed under separate Telegram API authority because `getUpdates` and an active webhook cannot be used together.

### Stop

```sh
sudo systemctl stop wellbeing-telegram-single-entity-pilot.service
sudo systemctl is-active wellbeing-telegram-single-entity-pilot.service || true
```

### Rollback

```sh
sudo systemctl disable --now wellbeing-telegram-single-entity-pilot.service
sudo systemctl is-enabled wellbeing-telegram-single-entity-pilot.service || true
sudo systemctl is-active wellbeing-telegram-single-entity-pilot.service || true
sudo systemctl status wellbeing-telegram-phase1b-sandbox.service --no-pager || true
```

The new pilot is a separate contour, so rollback stops and disables it while preserving package, config, secrets and SQLite state for inspection. Removing any of those objects requires a separate exact cleanup task. The old Phase1B service is not changed by this package.

## Remaining live dependencies and next gate

The candidate cannot enter a live pilot until one exact task establishes all of these:

1. independent SIS review of exact package bytes, service boundary and test reproduction;
2. exact provisioning task binding the package to SIS-preflighted host `ruvds-xnqc6`, service principal `wellbeing-tg-dialog`, Python 3.12.3 and exact paths above;
3. protected credential slots bound to the verified `@WBNP_Media_Bot` token and approved OpenAI account/key without revealing values;
4. exact closed tester `user_id` and `chat_id` allowlist accepted by OPERATOR;
5. read-only webhook-state check and, if required, separately authorized webhook removal before polling;
6. explicit authority to install/verify the service without starting it;
7. separate explicit bounded live authority to start polling, call OpenAI and send Telegram replies, with call/turn/tester/time/cost stop limits;
8. OPERATOR acceptance of count-bounded transcript/replay retention and a procedure for `OUTCOME_UNKNOWN` reconciliation;
9. informed tester acceptance that their admitted dialogue text is sent to OpenAI and retained locally within the stated bounds;
10. live success criteria: admitted tester receives same-dialogue replies for at least two turns, replay causes no duplicate effect, rejected tester causes no provider call, and fallback is observed under a controlled provider failure.

The exact next causal gate is `SIS_INDEPENDENT_REVIEW_AND_LIVE_DEPENDENCY_ADMISSION_R01`. No deployment or live call is implied by this package.
