# R03 static/tests/check evidence

Corrected runtime blob:
482b0986be21db1e3afcb7f3e450d9afa9b09291
SHA-256:
01fcf86cd87087dd752bfac2170c8842b85bd477f6c6d726b48c63d37c799347

Corrected tests blob:
36f558a18221a850431623b812e9a2aab2d26b4b
SHA-256:
a72f2a2b622535339f97c8bbcdbb47837ee059b2747bc5ac711e0e147faf410f

Static readback checks PASS:
- ActorExecutionBindingResolver present;
- RuntimeInputAdapter transports actor claim without creating binding;
- trust_policy_dependency present in resolution/contract/intent/admission/invocation;
- policy exact version/currentness/conflict checked at invocation;
- actor support evidence versions carried end-to-end;
- missing/conflicting actor support becomes UNKNOWN/CONFLICT;
- actor evidence version drift checked at invocation;
- C2 EffectBoundaryVerifier retained;
- old reviewed baseline core not modified;
- runtime regression test methods: 27.

Regression tests include:
- policy stale/conflict cannot bind;
- policy version/conflict change after admission => NOT_EXECUTED;
- actor missing/conflicting support => ineligible;
- actor evidence-version / Recovery changes after admission => NOT_EXECUTED;
- preserved C2 frontier, intent, admission, adapter-authority and prior-effect checks;
- non-live adapter still performs no effect;
- mock observation still cannot fabricate outcome.

Exact package-local Python execution in current KOD container:
NOT_EXECUTED.

Observed environment:
raw.githubusercontent.com / GitHub DNS resolution unavailable.
No SIS/external host was invoked to bypass the boundary.

Therefore this result claims static correction/readback readiness, not independent combined execution PASS.
