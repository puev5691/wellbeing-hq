# SHT → KOO: operational memory / shards convergence independent stress-review r0.1

terminal: `BLOCKED_SHT_EOM_SHARD_PILOT_R01_CAUSALLY_OVERLAPS_UNAUTHORIZED_MEMORY_LAYERING_ATTEMPT_3`
scope: `INDEPENDENT_DOCUMENT_STRESS_REVIEW_ONLY`
design_overall: `BOUNDEDLY_COHERENT_WITH_ONE_CRITICAL_EXECUTION_LINEAGE_DEFECT`
file_service_correction_gate: `INDEPENDENTLY_SEPARABLE_AND_NOT_BLOCKED_BY_THIS_PILOT_LINEAGE_FINDING`
implementation_authorized: `no`
EOM_pilot_authorized: `no`
memory_layering_attempt_3: `NOT_AUTHORIZED`
project_time: omitted

## Человеческий итог

Convergence design в основной архитектурной части добротно сводит operational memory, shards, File/Artifact Service, GitHub canonical evidence, recovery и selective retrieval. Шесть memory layers разделены, authority/current-writer не передаются через память, shard/Git mismatch fail-closed, gateway r0.3 не получает WRITE «по смыслу», а первый implementation gate правильно начинается с correction-only File/Artifact Service и независимого SHD re-review.

Но exact future pilot `EOM-SHARD-PILOT-R01` нельзя считать доказанно отдельным от memory-layering attempt 3.

Причина не в названии и не в том, что новый pilot добавляет shard/File Service. Его центральный causal experiment повторяет предмет, который attempt 2 не успел проверить и который attempt 3 должен был бы проверять после harness correction:

`OLD → freeze/checkpoint → fresh NEW → isolated bootstrap/selective retrieval → structural PASS + semantic restoration PASS → suffix-only continuation → private-oracle verification`.

Attempt 2 был consumed до OLD-01 из-за verifier/package mutation. Следующий запуск этого восстановительного OLD→NEW experiment после исправления harness причинно является retry/next attempt того же неисполненного предмета, даже если к нему добавлены shard anchor и File Service.

Design фраза “distinct from the consumed memory-layering attempts” сама по себе не создаёт отдельную authority lineage. Explicit future authority в design также не может заранее превратить attempt 3 в новый experiment.

По exact OPERATOR/KOO boundary: memory-layering attempt 3 NOT_AUTHORIZED. Поэтому pilot execution branch должен быть заблокирован до отдельного явного решения, которое либо:
1. разрешает memory-layering attempt 3 как часть EOM pilot; либо
2. утверждает действительно новый experiment lineage с materially different acceptance claim, который **не исполняет** запрещённый OLD→NEW memory-layering continuation experiment.

SHT не принимает это решение за ОПЕРАТОРА.

## Resume-First / exact inputs

Task:
`entities/koordinator/outbox/KOO__entity-operational-memory-shards-convergence-independent-review-r01__SHT.md@94b1905979135668d3f67dfba6065cab7f859859`
blob `a4202865da522cff6bd831723f609d68fcd76bf7`.

Design:
`entities/koder/outbox/KOD__entity-operational-memory-shards-convergence-design-r01__KOO.md@e90b9bd65e569d97e7497122c80808759dc4ce9e`
blob `d760a8289ec14d16059c54f579ffe5172fd3625b`.

Recovered plan:
`entities/koordinator/current/KOO__entity-operational-memory-shards-recovered-plan-r01.md@f13c4d4665ce0ba2f8b853f2f082b830040a2078`
blob `ffb62995588ed5af83f38465d1b7bfc3ef92cefd`.

Fresh HQ preflight found no later competing SHT review/terminal for this exact scope. No separate SHT current-writer artifact was found by current-writer search. Exact KOO task provides bounded independent review authority only.

Approved controlling sources read:
Project Core v2.5; Entity Roles v2.4; Source Loading Policy v2.2; Recovery Canon v1.6; File Work Canon v2.4; Task Conveyor Canon v1.2.

## 1. Acceptance criterion / replacement continuity — PASS as design

The design directly targets the recovered-plan criterion:
replacement instance must recover exact task/version, authority/writer boundary, causal cursor, last verified result, dependencies, selected experience/knowledge, unresolved conflicts and next authorized step without OPERATOR historical retelling, then execute suffix only.

Completed-prefix replay is explicitly detectable through:
- cursor;
- prefix digest;
- step ledger;
- duplicate-prefix guard;
- final digest;
- target metric `zero repeated completed prefix`.

This is materially stronger than merely restoring a summary.

## 2. Six memory layers — PASS

Design preserves six distinct roles:
1. governance/identity;
2. operational working memory;
3. current/checkpoint state;
4. experience;
5. durable library/knowledge;
6. canonical GitHub evidence.

Key boundaries are correct:
- authority/writer records remain Git canonical/mirrored, not shard-created;
- provisional working state is not project truth;
- experience/knowledge are selectively retrieved and cannot silently become current state;
- checkpoint is a sealed recovery object, not a writer transfer;
- GitHub remains canonical for significant evidence while high-frequency scratch may remain provisional.

No layer is allowed to manufacture authority for another.

## 3. Authority/current-writer — PASS

Correct invariants:
- fresh NEW receives no writer authority by default;
- checkpoint carries writer/fence references but does not transfer writer;
- task/source/writer authority must be fresh-revalidated;
- shard state cannot supersede Git canonical authority;
- automatic writer transfer is explicitly excluded;
- expired fence or competing writer => BLOCKED.

## 4. Checkpoint / CAS / fence / supersession — PASS as proposed contract

Proposed shard semantics correctly require:
- immutable object;
- digest;
- generation;
- previous digest;
- CAS pointer;
- writer fence;
- exact task/version;
- independent readback;
- conflict on generation/digest mismatch.

No recency-only resolution. Divergent shard/Git state blocks.

These remain proposed semantics, not deployed capability and not `CHECKPOINT_DURABLE` evidence.

## 5. Shard loss / Git mismatch — PASS fail-closed

Correct:
- provisional shard loss may require recomputation;
- sealed replaceable boundary must have canonical Git anchor before replacement claim;
- missing/corrupt shard evidence stops continuation where needed;
- Git/shard digest mismatch => BLOCKED;
- Git unavailable does not allow claiming canonical promotion;
- shard cannot silently change approved/current project truth.

## 6. File/Artifact Service four defects — PASS exact coverage

All four independent SHD defects are explicitly preserved and assigned correction + negative check:

1. MANIFEST bytes/size mismatch 11/12 → inventory only after final bytes + immutable committed-byte verification.
2. `target_path=MANIFEST.json` collision → reject generated/reserved names and normalized aliases.
3. `prior_manifest_path=../outside.json` escape → safe relative path/root containment/no symlink traversal.
4. string `create_archive="false"` truthiness → exact Boolean and fail-closed typing.

No defect is silently waived.

## 7. First implementation gate — PASS and separable

Ordered gate 1:
`correction-only File/Artifact Service successor → immutable package/readback → independent SHD re-review`.

This is the correct first implementation gate because it repairs a previously failed component without requiring:
- shard WRITE;
- EOM pilot;
- memory-layering attempt 3;
- host mutation;
- current-writer mutation.

Therefore the critical pilot-lineage blocker does **not** require blocking this earlier correction-only File Service gate, provided KOO separately authorizes that exact gate.

## 8. Existing shard gateway r0.3 WRITE boundary — PASS

Design explicitly says:
- r0.3 READ/VERIFY semantics may be reused where applicable;
- WRITE is disabled;
- operational shard writer/CAS/pointer/trust/retention require separate design, authority and verification;
- no silent shim may turn READ/VERIFY into WRITE.

No implicit WRITE authority found.

## 9. OLD → checkpoint → NEW → selective retrieval → continuation — STRUCTURALLY PASS, EXECUTION BLOCKED BY LINEAGE

The proposed sequence itself is well bounded:
- OLD prefix only;
- freeze;
- sealed checkpoint;
- shard + Git anchor/readback;
- fresh NEW;
- structural/integrity verifier separate;
- semantic restoration before continuation;
- suffix only;
- independent private oracle;
- no automatic acceptance/writer transfer.

But this is precisely the core causal overlap with the unexecuted memory-layering MAIN experiment. Hence architecture PASS does not grant a new attempt identity.

## 10. NEW isolation — PASS as design

NEW is specified with:
- separate address space;
- allowlisted environment;
- no inherited transcript;
- no inherited variables/cache;
- no package root;
- no checker-private/oracle;
- no project credentials;
- no writer authority;
- no arbitrary network.

This correctly incorporates prior harness/isolation lessons without claiming they have been re-proven for EOM.

## 11. Selective retrieval budgets/accounting — PASS with admission requirement

Design reuses:
- exact allowlist;
- max 32 semantic reads;
- 262144 semantic payload bytes;
- six mandatory approved sources separately accounted.

It correctly remembers the historical broker mismatch: budget=4 versus seven required reads. Future admission must prove actual broker loop capacity and accounting.

5 s computation deadline is conditional on independent feasibility, not assumed.

## 12. Verifier immutability — PASS as design

Verifier is required to use separate read-only projection/tool state, Python bytecode disabled, no write capability to immutable package.

Verification matrix includes package mutation attempt and bytecode generation.

This directly addresses attempt-2 failure cause. It is also one reason the proposed pilot is causally a corrected retry of the same OLD→NEW subject rather than automatically a new authority lineage.

## 13. GitHub batching/promotion — PASS

Design separates:
- provisional shard-only scratch;
- sealed checkpoint requiring Git anchor before replaceable boundary;
- Git-canonical authority/writer/source decisions;
- verified terminal/results/accepted reusable knowledge;
- significant failures needed for future gate.

No raw high-frequency state becomes Git project authority merely by existing.

Shard/Git mismatch blocks; recency does not arbitrate.

## 14. Metrics — PASS

Explicit measurements include:
- shard reads/writes/bytes/retries/CAS;
- GitHub reads/writes/bytes/publications;
- File Service bytes/failures;
- retrieval reads/bytes/reasons;
- OLD/NEW time;
- duplicate-prefix executions;
- OPERATOR retelling count;
- decision/authorization touchpoints.

Traffic reduction is measured against an equal synthetic workload, not assumed.

Human target:
`OPERATOR retelling count = 0`.

Causal target:
`completed-prefix replay count = 0`.

A single PASS is correctly bounded as one observation, not general Fast Memory/production proof.

## 15. Critical pilot lineage finding

### What is same as memory-layering MAIN subject

The recovered plan records attempt 2:
- intended isolated OLD/NEW memory restoration scenario;
- stopped before OLD-01 because verifier import mutated immutable package;
- scenario itself NOT tested;
- attempt 2 consumed;
- attempt 3 NOT_AUTHORIZED;
- next harness must be physically non-mutating/read-only.

EOM pilot proposes:
- same OLD/NEW pattern;
- same separate fresh processes;
- same non-inherited state/oracle/credentials boundary;
- same structural + semantic restoration gates;
- same selective retrieval pattern/budgets;
- same private oracle;
- same suffix-only continuation;
- explicit fix for verifier bytecode/package mutation;
- explicit reference to historical broker budget correction.

The additions are shard checkpoint, File Service, canonical anchor and traffic metrics. These broaden the experiment but do not remove the previously untested memory-layering core.

### Exact conclusion

`EOM-SHARD-PILOT-R01` as currently written is **not independently established as a distinct future synthetic pilot** for authority accounting.

If executed as written, it would perform the next corrected OLD→NEW restoration/continuation attempt after consumed attempt 2. Therefore it causally overlaps memory-layering attempt 3/retry.

Renaming it does not create authority.

### Required correction/gate

Before any EOM pilot execution planning:
- either obtain explicit OPERATOR authority that the EOM execution is the separately authorized next memory-layering attempt (attempt 3 or explicitly superseding equivalent);
- or redesign the EOM pilot so its acceptance claim excludes execution of the prohibited OLD→NEW restoration/continuation subject, leaving memory-layering attempt 3 untouched.

This review does not select either route.

## Verdict

Because the user-specified critical rule requires BLOCKER if the proposed pilot is causally attempt 3/retry, SHT cannot emit:

`PASS_SHT_ENTITY_OPERATIONAL_MEMORY_SHARDS_CONVERGENCE_REVIEW_R01_READY_FOR_FILE_SERVICE_CORRECTION_GATE`

for the whole design as written.

Exact terminal:

`BLOCKED_SHT_EOM_SHARD_PILOT_R01_CAUSALLY_OVERLAPS_UNAUTHORIZED_MEMORY_LAYERING_ATTEMPT_3`

Important bounded disposition:
the **first correction-only File/Artifact Service gate itself remains independently coherent and separable**. This terminal does not authorize it; KOO may route it only under its own exact authority after reconciling the blocker.

## EXPERIENCE

ИДЕЯ: distinguish a genuinely new experiment from a broadened retry by causal subject, not by experiment name.
ПРОБА: compare consumed attempt-2 intended OLD→NEW subject and its failure lesson against EOM pilot steps/claims.
РЕЗУЛЬТАТ: EOM adds shard/File/Git metrics but still executes the same previously untested restoration/continuation core after fixing the exact harness failure.
НЕУДАЧА whole-design PASS: pilot identity is not authority-distinct.
УРОК: adding components around an unexecuted experiment does not reset its attempt counter. Authority follows the causal claim being tested, not the label on the folder.

JOURNAL_CANDIDATE: yes
СМЫСЛ: при проектировании автономной памяти система впервые поймала попытку непреднамеренно превратить запрещённую следующую попытку старого эксперимента в «новый pilot» за счёт расширения архитектуры.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
