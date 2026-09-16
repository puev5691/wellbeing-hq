# Transport contract

Current task execution mode: injected non-network transport only.

The package contains a future-live transport, but it is default-deny:
- exact endpoint and request blueprint must validate;
- an explicit future switch value is required;
- live path requires the real network executor and environment secret reader together;
- the API key is read only from `OPENAI_API_KEY` at runtime and is never added to provenance;
- no automatic retries or fallback are performed by this transport;
- auth errors, rate limit, provider 5xx, timeout/network and malformed provider data fail closed.

This task executes only `MockTransport` and `InjectedHTTPExecutor`; `UrllibExecutor` performs zero requests in the test suite.