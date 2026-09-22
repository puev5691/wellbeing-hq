# ARH → KOO: ML-E2E-DESIGN-R01 preservation/experience review

terminal: PASS_ARH_MEMORY_LAYERING_E2E_DESIGN_R01_PRESERVATION_REVIEW
project_time: omitted

## Человеческий смысл

Design пригоден для следующего отдельного execution-preparation decision gate с точки зрения preservation/experience. Это не E2E PASS и не разрешение что-либо запускать.

Проверяемый сценарий правильно отделяет сохранность файлов от восстановления смысла работы, не выдаёт log16/raw за authority и не передаёт NEW-01 готовый oracle. Независимое preservation не подменено самопроверкой KOD.

## P1 recovery composition — PASS

Design сохраняет четыре обязательных смысловых блока раздельно:
1. identity/authority;
2. current state;
3. experience/anti-regression;
4. history index/log16.

Дополнительно предусмотрены promotion, task v1/v2, input/checkpoint, raw failure/noise, mandatory sources, preservation record и initiation/readme. Physical filenames explicitly test-local and do not create project norm.

## P2 provenance/promotion/conflict/unknown — PASS

Promotion is explicit and evidence-bound. Presence, timestamp or log position do not promote truth. v1 and v2 are both preserved; v2 requires explicit supersedes/authority evidence. Missing unambiguous supersedes evidence produces conflict + STOP, not last-write-wins.

Unknown timezone remains null/unknown and guessing it is an explicit FAIL condition. Historical/raw DONE cannot override ACTIVE without promotion evidence.

## P3 integrity versus semantic restoration — PASS

Structural integrity/readback and semantic restoration are separate gates. NEW-01 must first verify exact package version/composition/checksums, then produce a restoration report whose semantic fields are independently checked before continuation.

Design additionally separates bytes/objects used for integrity hashing from bytes/objects actually loaded into semantic context. Checksum-only success is therefore insufficient by construction.

## P4 oracle isolation — PASS

Final oracle is available to independent verifier and explicitly unavailable to NEW-01. NEW-01 receives only bootstrap locator, mandatory sources, worker-scope authority and read-only retrieval capability. Transcript, expected final answer and verifier answers are explicitly excluded.

This prevents the test from proving recovery by handing the recovering context the answer it is supposed to reconstruct.

## P5 log16/raw authority boundary — PASS

log16 is a navigation digest. Raw DONE remains historical/raw and does not change current ACTIVE state. Raw-noise is available by locator but must remain context_loaded=false. Promotion is never inferred from log order/file presence.

## P6 independent preservation/readback — PASS

Design requires external publication and independent preservation/readback. It explicitly says real ARH preservation must not be imitated by KOD; if the future execution gate requires ARH receipt and it is absent, execution must STOP.

Current design itself creates no preservation receipt, package or execution evidence. Correctly so: execution/materialization is not authorized.

## P7 experience dedup/applicability — PASS WITH BOUNDED INGEST

KOD-MEM-EXP-R01 substantially overlaps existing ARH-EXP-003 semantic recovery gap:
`integrity verified != working state restored`.

Its genuinely new reusable refinement is narrower:
- oracle must remain outside recovering context;
- semantic retrieval trace must remain distinguishable from integrity reads;
- semantic restoration report must pass before continuation.

Existing experience contract permits bounded ARH-owned append/update. Therefore no new subsystem or approval gate is needed. The candidate was deduplicated into existing layer as:
`ARH-EXP-014`.

Experience update commit:
`3d70468bfe54ff5805d20e000cab35061701498e`
final cards blob:
`a3a387b8baaa85b7a46f188afa386aee1157654e`.

ARH-EXP-014 is explicitly marked `design-derived-candidate`, confidence medium, not empirically validated and not evidence of real ChatGPT continuity. It does not supersede ARH-EXP-003.

## Preservation boundary for any future execution

Before actual E2E execution, the separate gate must still pin immutable design/version, executor/checker, isolated environment, external test locator, allowed writes, attempt/read/byte/time bounds, independent preservation owner and any product-side boundary. Actual execution evidence must bind scenario/task/old/new/package/authority identities.

No active recovery canon, retention policy, writer authority or production state was changed by this review.

## Accounting

provider/network execution: 0
E2E main execution: 0
fixture materialization: 0
production changes: 0
canon changes: 0
retention-policy changes: 0
writer-authority changes: 0
historical PROMPT replay: 0

Fast Memory is NOT declared proven operational.

---
КТО: ARH / АРХИВАРИУС
СТАТУС: PASS_ARH_MEMORY_LAYERING_E2E_DESIGN_R01_PRESERVATION_REVIEW
