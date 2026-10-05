# Unresolved Effect Handling
status: DESIGN_ONLY

UNRESOLVED freezes overlapping operation key/target scope.
No blind retry, no overlapping replay, no automatic cleanup.

Required reconciliation:
preserve PRE_EFFECT_INTENT, admission, invocation evidence, transport/session evidence and all observable target state;
request exact target inventory/stat/hash/ownership evidence using separately authorized read-only reconciliation;
classify only after evidence establishes success/failure/not-executed, otherwise remain UNRESOLVED.

Cleanup is prohibited while it could destroy evidence needed to resolve whether mutation occurred.
Independent unrelated sandbox scope may proceed only if dependency/ownership isolation is proven and separately authorized.
