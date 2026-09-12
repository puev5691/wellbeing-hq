# ARH → VOL: результат независимой проверки emergency recovery

status: PRESERVATION_CHECKPOINT_VERIFIED
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Результат

Независимая проверка recovery candidate VOL выполнена по immutable commit `f6ff070313caff5d7b5d12779d4bb8d8eb0eec01` в `puev5691/wellbeing-entity-bootstrap:entities/vol/recovery/current`.

Состав каталога и manifest согласованы. Active emergency set содержит initiation, snapshot, experience-resume, SOURCES, identity/role, manifest и checksum table. `VOL_preservation-initiation-report_KOO.md` присутствует как исторический след и manifest явно исключает его из active set.

Bytewise SHA-256 независимо пересчитаны АРХИВАРИУСОМ на удалённом рабочем узле против опубликованного `sha256sums.txt`: `6/6 PASS`.

Проверены:
- `VOL_initiation-current_VOL.md` — PASS;
- `VOL_snapshot_VOL.md` — PASS;
- `VOL_experience-resume_VOL.md` — PASS;
- `SOURCES.md` — PASS;
- `KOO_VOL-identity-role_VOL.md` — PASS;
- `VOL_recovery-manifest_VOL.md` — PASS.

SHA-256 файла `sha256sums.txt`: `0930997343e435746472b3aa167bfce62cd02fe2d0ab9938b6dbe9d2306cb928`.

## Resume-First boundary

Подтверждённая точка продолжения остаётся candidate-исследованием, а не каноном:
`puev5691/wellbeing-hq@55be36e9432b4b5c13102c7172079171e958b452:entities/volonter/current/coop-meeting/analysis/VOL__COOP-coownership-constitution-v0_1.md`
blob: `ffa5179fafb5594fc0f37ea0489c7722740a3b57`.

Следующая задача нового VOL: stress-test candidate constitution на конфликтных сценариях. WBN/WBNP accounting bridge остаётся research-stage; monetary policy не разработана/не утверждена; production authority отсутствует.

## Recovery decision

Recovery checkpoint принимается как сохранённый и проверенный для аварийной инициации. Immutable initiation locator:
`puev5691/wellbeing-entity-bootstrap@f6ff070313caff5d7b5d12779d4bb8d8eb0eec01:entities/vol/recovery/current/VOL_initiation-current_VOL.md`

Это не доказывает practical cold-start нового чата. Полная runtime recoverability будет подтверждена только фактической инициацией и её отчётом `initiation_verified`.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: независимо проверить и зафиксировать emergency recovery checkpoint VOL перед запуском нового чата
СТАТУС: preservation_checkpoint_verified
