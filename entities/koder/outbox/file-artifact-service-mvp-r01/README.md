# File/Artifact Service MVP r0.1

Локальный детерминированный сервис для повторяющейся механики package/seal/hash/manifest/readback.

Граница:
- explicit JSON request schema;
- каждый input имеет source_id, source_path, target_path, ожидаемые SHA-256 и size;
- source mismatch блокируется;
- файлы копируются в детерминированном порядке;
- MANIFEST.json содержит inventory SHA-256/size/source_id;
- optional deterministic tar.gz использует mtime=0, uid/gid=0 и стабильный порядок;
- readback.json перечитывает итоговые байты;
- diff.json сравнивает новый manifest с prior immutable manifest;
- result.json компактен и не содержит тела файлов/локальных путей;
- GitAdapter существует только как disabled interface и всегда блокирует publish;
- authority/project-state semantics отсутствуют.

MVP execution path не использует сеть и не публикует GitHub. Публикация самого проверенного пакета выполняется внешним проектным контуром, а не сервисом.

Тесты: 12/12 PASS, network_calls=0, git_publications=0, credentials=0.