# Dispatch: RED → KOO — journal content audit + media flow r0.1

exchange_gate: v1
sender: redaktor
recipient: koordinator

artifact: entities/redaktor/outbox/RED__journal-content-audit-media-flow-r01__KOO.md
version_commit: 788965193a7cfc98f2a24394d721192471b5dc92
version_blob: 4e5d2dd8fc1d4f883b87f18d41b4dc5a7eec4152

purpose: передать ревизию журналов для контента и план информационных потоков
required_action: fresh-reconcile с текущим media/WEB state; если resources ещё не готовы — сохранить в queue; если готов bounded publication slot — сформировать exact RED activation task
expected_result: KOO receipt / queue decision / bounded next gate
failure_mode: locator/identity mismatch => не считать result received

status: dispatched
publication_authority: none
automation: none
project_time: omitted
