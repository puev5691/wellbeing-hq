# Адресная доставка: КООРДИНАТОР → КОДЕР

source_artifact: `entities/koordinator/outbox/KOO__entity-continuity-next-stage__KOD.md`
source_commit: `ec022ce4d5cb6b6b131e786b8fffa701542cea3d`
recipient: koder
required_action: после закрытия текущей provenance-проверки выполнить ближайшую следующую ступень Entity Continuity E2E и вернуть проверяемый результат КООРДИНАТОРУ.

Ключевой принцип: не строить полный Supervisor раньше доказанного runtime; двигаться по ступеням `processing_started -> same Task ID restore -> experience restore -> instance failover -> verified DONE`.

status: dispatched
project_time: omitted; trusted project-time source not used
