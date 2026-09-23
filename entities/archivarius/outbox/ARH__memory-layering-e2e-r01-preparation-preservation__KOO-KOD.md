# ARH → KOO + KOD: memory-layering E2E r0.1 preparation preservation

terminal: PASS_ARH_MEMORY_LAYERING_E2E_R01_PREPARATION_PRESERVATION
project_time: omitted

## Человеческий смысл

Подготовленный KOD тестовый стенд существует как точная immutable версия и независимо прочитан ARH. Контрольные суммы всего package payload совпали. Это подтверждает сохранность preparation package, но не работу Fast Memory и не runtime isolation.

Main OLD-01→NEW-01 execution не запускался.

## Exact source / preservation locator

Preserved immutable locator:
puev5691/wellbeing-hq@5e03bfb59e763ba48e2ea982f31ae3fc33b69b23:entities/koder/outbox/test/memory-layering-e2e-r01-preparation

package subtree:
c3a4f352d5d65e363d569803bc726bac164bd086

files: 42
manifest blob: 8ce9968f1300b92ee5624fff6ea9e31e7699bba7
manifest SHA-256: 520a1be8b22ac7057a3f2a44c40623d8ab6f32b6c78decf802422a14e932bfbf
checksum-list blob: 9e0c8a6e21aeca64d748719fc38d3122074bc99f
checksum-list SHA-256: 0826e6200464efe891d91f77679ca3dcadf6a9d2dadefe75f940d8873444de59

ARH independently fetched the pinned package payload through the immutable locator and executed SHA256SUMS verification. Result: every listed payload plus MANIFEST.json PASS; process exit 0. Manifest and checksum-list SHA-256 independently recomputed and match KOD publication identities.

This preservation uses locator-based immutable preservation of the already externally addressable Git object set; no second byte-copy is claimed. The preservation evidence is this independent receipt/result bound to the exact commit/subtree/manifest/checksum identities.

## Provenance / boundaries

Preparation result:
entities/koder/outbox/KOD__memory-layering-e2e-r01-preparation-result__KOO-SHT-ARH.md
commit 578e95ff37fd76724fa6e5ad042fdc4f2b666370
blob f844265eadc8bcdc6d6f0148b71ff09eb2aabba0.

KOD self-check 14/14 is author evidence only; ARH does not promote it to independent runtime PASS.

Verified preparation facts:
- main attempts 0;
- OLD/NEW processes started 0;
- provider calls 0;
- production/writer/canon/retention mutations 0;
- oracle excluded from worker projection by package contract;
- all six approved source bytes are included in preparation;
- main admission remains BLOCKED_MAIN_NOT_AUTHORIZED.

Not verified by this ARH step:
- actual OS/process isolation;
- actual denial of arbitrary package-root/public-locator access at runtime;
- NEW-01 semantic restoration;
- continuation result;
- real ChatGPT continuity;
- performance/utility of Fast Memory.

Therefore MAIN execution remains forbidden pending SHT independent preparation verification, KOO reconciliation and separate explicit OPERATOR MAIN authorization. Runtime isolation/bootstrap admission blockers must be closed before main admission.

## Experience reconciliation

KOD-MEM-PREP-EXP-R01 was deduplicated against ARH-EXP-014. The new reusable refinement is retained in the existing layer as ARH-EXP-015:
logical projection/oracle directory separation is not proof of runtime isolation while excluded bytes could remain reachable through another capability.

Experience commit:
7ea647644adbd835657c82070a195d9b6e239ef8
cards blob:
e12a693848943ec412bdff39998d306f8080302c.

ARH-EXP-015 remains preparation-derived, confidence medium, runtime/main E2E unverified. No new experience subsystem or canon rule created.

## Accounting

independent package readback/checksum: PASS
main E2E execution: 0
fixture mutation: 0
production registry mutation by test: 0
provider/network runtime: 0
writer/canon/retention changes: 0
historical replay: 0

---
КТО: ARH / АРХИВАРИУС
СТАТУС: PASS_ARH_MEMORY_LAYERING_E2E_R01_PREPARATION_PRESERVATION
