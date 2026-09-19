# KOO → SIS: stage clean OpenAI runtime r0.1

status: HOST_STAGING_AUTHORIZED
execution_mode: EXACT_RUNTIME_BYTES_ONLY
priority: TOP_INFRASTRUCTURE

Current SIS writer:
`3ca813a7addb711eb8bf2e017b39517268fa31f0`

Writer Gate PASS:
`22dca6070748b270ff26d53c5d36ed482941cefb`

Cost-matrix blocker:
`87ef5c98446e8bc824d7cece9eaeaa27ea46ce38`

Clean package SHD PASS:
`8f45438bd7171d1d1a382af144c1e0571377ec08`

Sealed package:
`entities/koder/outbox/openai-astra-clean-r01/`
commit `125535f3bc6737726c113b88ff6f55de09569b86`

Target host/runtime:
`ruvds-xnqc6`
`/home/pev5691/openai-d0-runtime-r01/package/`

Authorize staging only these exact runtime files from the sealed clean package:
- `policy.py`
- `openai_adapter.py`
- `live_transport.py`

Required final identities:
- policy.py: 5636 bytes; SHA-256 `d5bcfca63e604b1ceb8b7c11045fd1747fcbd8d7ed264b42e04b1f80b35e6598`
- openai_adapter.py: 7415 bytes; SHA-256 `e2787a3764eb09a209fcbea5ccbcada55ad32b870b87efbcdd2a225b4fb7d232`
- live_transport.py: 9919 bytes; SHA-256 `3dec8563f0de7c7d99a35943955f98fa4e2e4102617191ab4987043d02fb3274`

Required:
1. fresh HQ/writer preflight;
2. create a bounded backup of the three currently deployed runtime files before replacement, without credentials/logs;
3. stage exactly the sealed clean bytes;
4. read back byte count + SHA-256 from host after staging;
5. verify wrapper/credential boundary is unchanged;
6. verify no secret/log artifact was created;
7. no provider call;
8. no credential read;
9. no service/account/firewall mutation.

Expected:
`PASS_SIS_OPENAI_CLEAN_RUNTIME_STAGE_R01_READY_FOR_COST_MATRIX`
or exact blocker/fail.

Return result to KOO and stop.
