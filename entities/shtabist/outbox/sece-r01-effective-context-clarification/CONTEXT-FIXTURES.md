# SECE r0.1 Context Fixtures CXT1-CXT10
status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE

CXT1 Context(n): MAY inspect; MUST_NOT mutate; consumer UNKNOWN. Trigger: composition. Scope gateway. Invalidated none. Preserved all three. Context(n+1): inspect potential, mutate forbidden, consumer UNKNOWN, evidence requirement active.

CXT2 Context(n): experience recommends mutate; active rule forbids mutate. Trigger: experience selection. Scope action/mutate. Invalidate proposed executable-mutate binding. Preserve experience as advisory and unrelated context. Context(n+1): mutate forbidden; experience retained non-authority.

CXT3 Context(n): recovery evidence R for scopes S and U. Trigger: verified delta D refines S. Affected S. Invalidate R-derived current bindings only in S. Preserve R for U and as history. Context(n+1): D selected current basis S; R preserved U/history.

CXT4 Context(n): task T current with T-derived bindings; unrelated scope U. Trigger: verified terminal supersedes T. Affected T. Invalidate/recompute all T-dependent bindings. Preserve U. Context(n+1): T terminal/superseded; no stale T executable binding.

CXT5 Context(n): action A lacks authority; other actions B unaffected. Trigger: verified authority grant for A/scope S. Affected A/S authority-dependent bindings. Recompute A only. Preserve B. Context(n+1): A authority binding current subject to other gates.

CXT6 Context(n): scopes S1 and S2 valid. Trigger: active source conflict in S1. Affected S1. Invalidate dependent S1 bindings; preserve S2. Context(n+1): S1 conflict/STOP dependent effects; S2 unchanged.

CXT7 Context(n): required evidence E UNKNOWN with dependent bindings blocked. Trigger: verified event resolves E. Affected E scopes/dependencies. Remove resolved UNKNOWN; recompute dependent bindings; preserve independent bindings. Context(n+1): uncertainty removed only exact scope.

CXT8 Context(n): verified GitHub state G. Trigger: human input claims contrary H without authority/evidence status. Affected claim comparison scope. Do not invalidate G. Preserve G current; record H as human claim + conflict/unverified input. Context(n+1): verified state unchanged.

CXT9 Context(n): decision/authority absent or pending in scope S. Trigger: authorized OPERATOR decision event. Affected exact decision/authority scope S. Invalidate dependent pending bindings; recompute from verified decision. Preserve unrelated scopes. Context(n+1): bounded decision/authority binding updated, no wider authority.

CXT10 Context(n): role/profile/independent experience + current next gate G1. Trigger: verified result changes next-gate conditions. Affected result/next-gate bindings only. Preserve role/profile/independent experience. Context(n+1): G2 derived under active rules; preserved context intact.

Each fixture follows Context(n) -> event -> affected scopes -> invalidated bindings -> preserved bindings -> Context(n+1).
