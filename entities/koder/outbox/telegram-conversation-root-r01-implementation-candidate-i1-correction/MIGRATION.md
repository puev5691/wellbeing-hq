# Conversation-root r0.1 migration candidate

status: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

Additive nullable columns only:
- inbound_reply_to_message_id INTEGER
- inbound_reply_to_message_thread_id INTEGER
- stable_conversation_root_id TEXT
- root_derivation_class TEXT
- root_evidence_update_id INTEGER
- root_conversation_key TEXT

No table replacement. No destructive rewrite. No historical root backfill. No old conversation_key rewrite. No transcript rewrite.

Legacy rows keep all new fields NULL. Current observability-schema migration first run and second-run idempotency are covered by offline tests. The existing r0.2 legacy migration fixture also remains PASS.

Only newly claimed turns receive root-r0.1 decisions. The legacy tuple key remains in updates.conversation_key as immutable routing evidence; new operational history uses root_conversation_key.

Live DB/schema mutation is not authorized by this package.
