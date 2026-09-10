# Адресная доставка: КООРДИНАТОР → КОДЕР

source_artifact: `entities/koordinator/outbox/KOO__activation-worker-v01-review__KOD.md`
source_commit: `db0be19032edd81e6b427836c3f8bc24d8665c54`
recipient: koder
required_action: исправить единственный blocking defect immutable identity/provenance validation, выпустить v0.2 и вернуть КООРДИНАТОРУ через Exchange Gate.

Ключевая проверка для v0.2: fake commit/blob или несоответствующий immutable dispatch не должны доходить до `processing_started`.

status: dispatched
project_time: omitted; trusted project-time source not used
