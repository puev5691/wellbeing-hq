# R04 effect-sensitive dependency chain

Authoritative task evidence
-> TaskExecutionBindingResolver
-> TASK_EXECUTION_BINDING
-> RUNTIME_EVIDENCE_RESOLUTION
-> Effective Context / ExecutionContract
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> invocation task binding + exact evidence versions
-> EffectBoundaryVerifier.

Task file presence, prompt receipt, queue/inbox, memory, current-writer and actor eligibility are not task authority.

C1 policy dependency, C2 canonical intent/admission checks and evidence-derived actor/Recovery binding remain present.
