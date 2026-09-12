# MANIFEST

status: candidate
production: no
network_to_telegram: forbidden
real_credentials: forbidden
runtime: python3-stdlib-sqlite

## Immutable package identity

Package base commit before manifest: `cffb5b60ac30ec1bc4955568635f9e96c509941c`.
The table below was generated after the final bytes of all payload/test/result files were published and read back from GitHub.

| file | Git blob SHA-1 | bytes |
|---|---|---:|
| README.md | `552c18d7a3577a2cedd484e34e99d6c337bc621b` | 1524 |
| SAFE_RECEIPT.json | `b7e877ec511e0d5ff6274be4bd0968599893c79f` | 386 |
| TEST_RESULTS.txt | `b5f4764621e7e143be22aa4f37f0e0d298156222` | 133 |
| gateway.py | `12af38ee0d374a4bc85f13902a8c536145c5d519` | 8475 |
| requirements.txt | `cb70631a6256968d162482c4036c057147bb934d` | 30 |
| test_gateway.py | `f2e38c71c9ff6202683bffa00c70ed502d6c16f3` | 5356 |

## Verification

- test command: `python3 -m unittest -v test_gateway.py`
- local result: `14/14 PASS`
- process exit code: `0`
- Telegram/Bot API network calls: `0`
- credentials handled: `0`
- third-party dependencies: `none`
- safe receipt contains no audience identity
- duplicate publication: no-op
- duplicate webhook update: no-op
- restart during `dispatching`: recovered to `prepared`
- correction edits message `1001` without duplicate send

Git blob SHA-1 values above are immutable Git object identities for the exact published bytes. They are used here as the post-publication checksum table for this non-recovery package.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать состав и exact-byte identity Telegram media Phase 0 package после финальной публикации файлов
project_time: omitted; trusted project-time source not used
