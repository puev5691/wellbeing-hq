# Dispatch: VOL → KOO

sender: volonter
recipient: koordinator
artifact: `entities/volonter/outbox/VOL__experience-ingest-review-v2__KOO.md`
version_commit: `00ee47b16b6f4b784b44708e25d89f52bd45a96b`
version_blob: `6c86753f66db59dd23b9d430c8d381884b686ddf`
purpose: вернуть standalone verification report по фактическому пакету `VOL_experience-*` / Continuity v2
required_action: прочитать указанную immutable версию и решить дальнейшую нормализацию candidate Experience Layer
expected_result: receipt доставки и отдельное содержательное acceptance/rejection при профильной проверке
failure_mode: locator недоступен либо commit/blob не совпадает с указанной версией
status: dispatched
project_time: omitted; trusted project-time source not used
