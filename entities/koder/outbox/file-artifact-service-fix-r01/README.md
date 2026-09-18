# File/Artifact Service fix r0.1

Correction-only candidate for File/Artifact Service MVP r0.1.

Исправлены ровно четыре boundary defects:
- top-level immutable package MANIFEST seals exact final Git object bytes for all non-self package files;
- MANIFEST.json зарезервирован и не может быть input target;
- prior_manifest_path допускает только null или безопасный относительный путь внутри source_root, включая fail-closed symlink containment;
- create_archive принимает только exact boolean, prior_manifest_path только exact null|string.

Сохранено без расширения полномочий:
- deterministic package/archive/readback/diff;
- zero-network default;
- Git adapter disabled;
- credentials absent;
- authority/project-state semantics = none.

Сам service execution path не публикует GitHub.