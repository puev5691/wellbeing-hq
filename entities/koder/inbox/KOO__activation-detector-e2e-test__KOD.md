# KOO → KOD
## E2E-тест activation detector

Цель: проверить новый GitHub event detector на реальном изменении адресного inbox.

Изменение, которое должно запустить workflow:
`entities/koder/inbox/KOO__activation-detector-e2e-test__KOD.md`

Проверяемая цепочка на этом этапе:
`push to entities/*/inbox/** → GitHub Actions workflow entity-activation-detector → run evidence`.

Никакое пробуждение существующего ChatGPT Entity-чата этим тестом не заявляется.

Требуемый результат KOD:
1. проверить, что workflow реально стартовал на этом commit;
2. вернуть run id/status и evidence artifact либо точный failure;
3. если detector PASS, подготовить следующий adapter-step для activation_requested без расширения authority.

failure_mode: workflow не стартует, path-filter не срабатывает, permissions/Actions policy блокирует run или evidence отсутствует.

from_entity: KOO
to_entity: KOD
document_type: activation-detector-e2e-test
status: dispatched-test
project_time: omitted
