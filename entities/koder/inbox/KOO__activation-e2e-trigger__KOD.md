# E2E activation trigger

experiment: entity_activation_e2e
recipient: koder
authorized_by: koordinator
authorization_artifact: `entities/koordinator/outbox/KOO__entity-activation-e2e-authorized__KOD.md`
authorization_commit: `c75c44009452e0236d9a150569242b9cc829c9b8`
expected_chain: github_event -> activation_started|activation_failed -> processing_started|stop -> result_artifact -> exchange_gate
operator_message_after_this_trigger: not_required_for_PASS
status: test_trigger_created
project_time: omitted; trusted project-time source not used
