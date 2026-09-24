# KOO → KOD: bounded activation-lineage schema F1/F2 correction r0.1

status: READY_FOR_BOUNDED_NON_LIVE_F1F2_CORRECTION
project_time: omitted
recipient: KOD / КОДЕР
scope: EXACT_TWO_STRUCTURAL_SCHEMA_FIXES_ONLY

## Человеческий смысл

После завершённой проверки Static Preview возвращаемся к отдельно ожидавшей задаче схемы событий. В candidate найдены два случая, когда формально допустимая запись может обойти смысловые ограничения. Исправь ровно F1 и F2 в новой immutable версии candidate и покажи точный diff и регрессионную проверку. Не меняй действующие Project Sources или automation.

## Authority and fresh basis

ОПЕРАТОР в текущем чате КОО потребовал продолжить работу после локальной остановки Booster. КОО в пределах роли выбирает один уже записанный serialized профильный шаг N2 из KOO__orchestrator-worklist-v01.jsonl, который зависит от O1 Static Preview E1 и fresh preflight. O1 KOD result и WEB v0.3 independent recheck завершены и приняты в bounded scope; эта очередь является историческим plan evidence, свежие terminal results имеют приоритет.

Fresh HQ prewrite HEAD: 2a6aa69a5a1a933e55c25bec67b62e916853b686
Recursive tree: truncated=false.
Current KOO writer: entities/koordinator/current/KOO__replacement-current-writer-v08.md; blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd.
Current KOD writer: entities/koder/current/KOD__replacement-current-writer-v05.md; blob cf1c84f9df7c90509703e4885844d0cf871ff412.
No newer competing KOD writer or existing F1/F2 correction result found.

Closed predecessor:
routes/receipts/WEB__info-entry-static-preview-v03-narrow-recheck__KOO.receipt.md
blob 5c62cd12d99b84c354d89d39f4123dfe613aeca8
verdict ACCEPTED_PASS_STATIC_PREVIEW_V03_E1_NARROW_RECHECK.

Exact SHT organizational review:
entities/shtabist/outbox/SHT__activation-lineage-schema-org-review-v01__KOO.md
blob d42d375a954db94d99a83a66d23965dc19fd934f
verdict PASS_WITH_EXACT_SCHEMA_ORG_FIXES.

Exact base candidate:
puev5691/wellbeing-hq@6890803d88b0d582b7baa51a275a488f3de9e6f6:entities/koder/outbox/activation-lineage-schema-v01-candidate/
schema.json blob 8bf9e8d4900b4994bdb4a1dd7d78c1c4fa90470f
CROSS_RECORD_INVARIANTS.md blob f33d512f584a046ffb5092940ec93c1eb6ce32f1
FIELD-MAP.md blob 8f52b57a862e6bef821850dfa2da5b2aa2805213
TEST-VECTORS.md blob 548a64291e9adaa919b726a2169824caf3d52008

## Exactly one correction increment

F1: for branch_status != TRANSPORT, require non-empty string experiment_id and task_id in the conditional properties, beyond mere required presence. TRANSPORT continues to prohibit those fields. Demonstrate null and empty strings rejected for semantic records, valid IDs accepted.

F2: when acceptance_status=PROVEN, require event_claim_verified=true in the same record. Demonstrate false rejected and true accepted with existing bounded acceptance_scope. Preserve UNKNOWN/NOT_APPLICABLE and transport/receipt boundaries.

Publish successor candidate under a new path, do not overwrite base. Provide exact diff and machine-readable positive/negative fixtures; check unchanged behavior of existing 24-record set and relevant exclusions. If any other change is needed, stop with exact blocker instead of expanding scope. The structural schema still does not prove cross-record truth or immutable acceptance evidence.

After publication independently read back successor schema and test artifacts. Address one result to KOO with exact path/commit/blob, changed fields, test outcomes and PASS_KOD_ACTIVATION_LINEAGE_SCHEMA_F1F2_CORRECTION_R01_READY_FOR_SHT_REVIEW or exact BLOCKED_*/FAIL_*.

## Hard boundaries

live_provider_or_Telegram_calls: 0
host_or_production_mutation: none
credential_access: none
scheduler_or_automation_change: none
runtime_collection_validator: NOT_AUTHORIZED
Project_Source_or_canon_promotion: NOT_AUTHORIZED
historical_PROMPT_replay: none
memory_layering_terminal: FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION
memory_layering_attempt_3: NOT_AUTHORIZED

STOP after bounded candidate correction and immutable readback. SHT re-review is separate.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
