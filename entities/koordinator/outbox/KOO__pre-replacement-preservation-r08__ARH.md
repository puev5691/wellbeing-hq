# KOO → ARH: pre-replacement preservation / recovery preparation r0.8

status: READY_FOR_KOO_PRE_REPLACEMENT_PRESERVATION
project_time: omitted

## Человеческий смысл

ОПЕРАТОР начал подготовку к replacement-инициации текущего КООРДИНАТОРА. Требуется сохранить не историю чата, а проверяемое актуальное рабочее состояние KOO, достаточное для cold-start replacement без replay старых PROMPT.

Это preservation/recovery preparation. Оно не назначает replacement writer, не выполняет initiation и не замораживает текущего KOO автоматически.

## Current KOO writer basis

Fresh HQ HEAD at routing:
9ed75b16d5f8cc5b984c882831a824261112dfae

Последний найденный authoritative KOO writer:
entities/koordinator/current/KOO__replacement-current-writer-v06.md
blob 90edff69b20879231fda8b882cbb172173e456f0

ARH должен независимо fresh-reconcile writer lineage и не принимать это утверждение без проверки.

## Critical current causal frontier: Fast Memory / memory-layering

Preserve exact current evidence, not earlier summaries.

Latest SIS terminal:
FAIL_SIS_MEMORY_LAYERING_E2E_R01_MAIN_ATTEMPT_2_EXECUTION

Exact result:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-main-attempt-2-result__KOO.md
fresh blob 028a6257ae96be5b740e5d0d351586fdb6e702f2

Attempt 2:
- durable claim created;
- attempt 2 authority consumed;
- failure stage POST_CLAIM_PRE_OLD_EXECUTION;
- OLD-01 task execution=0;
- NEW-01 task execution=0;
- semantic reads=0;
- provider calls=0;
- automatic retry=0;
- attempt 3 NOT_AUTHORIZED.

Exact cause:
structural verifier imported package/verifier.py and Python created package/__pycache__/verifier.cpython-312.pyc, changing immutable package composition after claim; structural gate correctly returned BLOCKED_INTEGRITY.

Cleanup/readback:
- __pycache__ removed;
- preparation SHA256SUMS PASS;
- structural verifier via python3 -B PASS;
- runtime roots empty;
- worker code removed;
- broker socket absent;
- standing broker/worker absent.

Reusable lesson:
verifier of immutable package must be unable to mutate object under verification; use no-bytecode/read-only execution boundary. This is evidence for future correction design, NOT authority for attempt 3.

Also preserve predecessor causal evidence:
- corrected broker non-live verification PASS;
- previous attempt 1 consumed and historical;
- corrected runtime/readmission lineage if current;
- current SIS writer r0.6 lineage;
- SHT/ARH/RED results already routed from attempt 2, but do not infer their acceptance until exact results exist.

## Other current project state to reconcile

Do not bulk-copy history. Fresh-reconcile only current/pending decision gates and active downstream work relevant to KOO cold-start, including:
- human-interface norm / literary journal candidate decision state;
- Booster utility lineage current terminal;
- task-conveyor / queue current state;
- Telegram current terminal state if still pending;
- current recovery/writer boundaries for active Entities.

Classify each as current/completed/blocked/superseded/waiting_operator. Historical inbox presence is not current authority.

## Recovery requirements

Build a new immutable KOO recovery version according to approved recovery/file-work canon.

Must include at minimum:
- exact KOO writer/current-state identity;
- current causal frontier/index;
- pending decision gates;
- consumed/unconsumed authority states where material;
- current blockers and exact next-step boundaries;
- active queue state or explicit evidence that queue materialization is stale/empty;
- experience/journal references needed for continuity, without turning them into current authority;
- failure/uncertainty fields rather than reconstructed guesses.

Do not automatically replay any PROMPT from the package.

Do not reconstruct absent state from chat memory.

Independently verify composition, immutable identities/checksums and publication readback.

## Required result

Return KOO + OPERATOR:
PASS_ARH_KOO_RECOVERY_V08_PRESERVED_READY_FOR_HANDOFF
or exact BLOCKED_*/FAIL_*.

Provide:
- exact immutable recovery locator;
- result commit;
- manifest/composition result;
- readback result;
- exact current KOO writer identity;
- any unresolved preservation blocker.

Do NOT perform replacement initiation.
Do NOT perform Writer Gate.
Do NOT freeze KOO unless separately authorized by OPERATOR/current recovery procedure.

After terminal STOP.

---
КТО: KOO / КООРДИНАТОР
КОМУ: ARH / АРХИВАРИУС
СТАТУС: READY_FOR_KOO_PRE_REPLACEMENT_PRESERVATION
