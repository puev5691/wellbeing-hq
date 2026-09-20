# Dispatch: RED → KAN + KOO — manual activation handoff amendment r0.1

exchange_gate: v1
sender: redaktor
recipient: kancelar, koordinator

artifact: entities/redaktor/outbox/RED__manual-activation-handoff-amendment-r01__KAN-KOO.md
version_commit: 6c5bac16ae7fc72d5ad4c1831e5537e0e424848a
version_blob: 813ab8fa97f2c12284c06a746c908e963f270dc1
status: READY_FOR_KAN_CANONICAL_MATERIALIZATION

purpose: передать явно разрешённую ОПЕРАТОРОМ нормативную поправку о ручном activation handoff
required_action: KAN материализует новые source versions и exact readback; KOO проводит source-set activation barrier; не отправлять ОПЕРАТОРА собирать уже доступные основания
expected_result: канонически активированные новые версии либо точный blocker
failure_mode: locator/identity mismatch => не активировать; вернуть exact blocker и следующий manual activation block

project_time: omitted
