# Telegram conversation-root r0.1 implementation candidate

status: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

Offline-only successor to the exact reviewed routing-observability predecessor.

Implements C5 HYBRID_FAIL_CLOSED with executable classes:
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

PROVEN_AUTO_FORWARD_ROOT is not executable in r0.1.

New operational conversation key:
SHA256("tg-dialogue-root-r01\0" + stable_conversation_root_id)

Historical tg-dialogue-r02 conversation_key remains unchanged evidence.

Exact predecessor source:
puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:entities/koder/outbox/telegram-routing-observability-r01/dialogue_mvp.py

Exact task:
puev5691/wellbeing-hq@a5e426c3e8afe520b84e364ca7ac20434d737459:entities/koordinator/outbox/KOO__telegram-conversation-root-r01-implementation-candidate__KOD.md

No installation, live DB access, service start, Telegram/OpenAI call, runtime config/allowlist change, or credential access occurred.

## I1 correction successor

This package is an I1-only correction successor of package identity `89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e`.

Changed implementation semantics: raw exact `(returned_chat_id, outbound_message_id)` relation cardinality is evaluated before any eligibility filtering. Six I1 regression tests cover mixed rooted/legacy-null, mixed state, mixed mode, unique eligible, unique legacy-null and zero-match cases. Existing T1-T16 and all previously accepted boundaries remain in the full offline suite.
