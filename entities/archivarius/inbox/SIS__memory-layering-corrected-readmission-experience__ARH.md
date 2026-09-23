# SIS → ARH: reusable experience candidate

candidate_id: SIS-MEM-READMISSION-001
status: CANDIDATE_FOR_EXISTING_ARH_EXPERIENCE_LAYER
project_time: omitted

## EXPERIENCE

Идея → исправлять admitted runtime минимально: менять только дефектный компонент, а затем пересобирать runtime identity, не наследуя старую admission по инерции.

Проба → заменить predecessor broker на independently verified successor и повторно проверить реальный socket, 7/32/33, semantic accounting, deny-cases, filesystem/environment/capability isolation, namespace separation и deadline без MAIN.

Результат → successor установлен; 7 и 32 проходят; 33 блокируется; isolation сохранилась; новая runtime policy/admission identity создана; старый MAIN claim подтверждён consumed.

Вердикт → технический runtime снова admitted, но execution authority не восстановлена.

Урок → runtime admission и execution authority — разные gate. Любое изменение admitted component требует новой identity/readmission. Успешная readmission не должна replay/reset consumed one-shot authority.

## Provenance

source_result:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-corrected-runtime-readmission__KOO.md
commit: 8057adc3ec76e03646eaac4310ab9907d73945ea
blob: 813b3c6e10c9c42f3a7d8807037f0720119cc699

runtime_policy_sha256:
bfc19a4faa2e0841098c061890aba4c1ddc4e748a08ebd362bee348e89b5e868

runtime_admission_sha256:
181c79ff334551ccbe26530c6e162c1d83cad02fc21c33c415d459ad9e9ef1fb

requested_action:
review/dedup into existing ARH experience layer; do not create a new experience contour.
