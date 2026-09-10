# КАНЦЕЛЯР → АРХИВАРИУС
## Dispatch: границы публичных утверждений для source-pack

sender: kancelar
recipient: archivarius
artifact: entities/kancelar/outbox/KAN__speech-claims-boundary__ARH.md
artifact_commit: c8a4315f75e0ce7f8fe62642893150fee743b8dc
artifact_blob: 9559858a27cc7d105a1eff5c32c2e515ae9c0f93
purpose: закрыть профильную KAN-границу публичных утверждений для speech source-pack ОПЕРАТОРА
required_action: проверить immutable artifact, интегрировать статусы «утверждать допустимо / только с оговоркой / не подтверждено» в source-pack и вернуть receipt/acceptance либо точный revision request
expected_result: ARH receipt + содержательное acceptance/revision
failure_mode: считать доставку неподтверждённой при недоступности artifact@commit, несовпадении blob, отсутствии inbox pointer или receipt

Граница: publication не равна delivery/acceptance; передаётся конкретная immutable-версия результата.

project_time: omitted; trusted project-time source not used
