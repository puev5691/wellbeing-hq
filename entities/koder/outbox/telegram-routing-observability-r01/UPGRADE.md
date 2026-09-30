# Future SIS install-readiness contract: discussion runtime r0.2 → routing observability r0.1

Status: `DOCUMENTED_NOT_EXECUTED`.

This document is not deployment authority. The KOD task authorized only an offline candidate.

## Preconditions for a separate SIS task

- independently verify the immutable package and all checksums;
- independently reproduce the offline suite;
- verify the exact installed predecessor code/config/database identities;
- verify the service is inactive and disabled;
- preserve exact pre-state and a rollback source;
- authorize only named install/migration/readback operations;
- do not read credential values, start the service, or call Telegram/OpenAI.

Any mismatch is a stop.

## Intended delta

Only `dialogue_mvp.py` changes at runtime. Configuration schema, provider/model, allowlist, credential slots, admission identities, polling and systemd unit remain unchanged.

The first writable startup on the reviewed candidate performs the additive SQLite migration in `Store._migrate_routing_schema`. It adds missing nullable columns from `ROUTING-OBSERVABILITY-SCHEMA.json`. Re-running the migration is a no-op. It does not rewrite legacy rows or messages.

The future SIS verification must prove on a preserved disposable database copy before any installed-state migration:

1. exact r0.2 schema and history remain readable;
2. all nine columns are added once;
3. a second run makes no schema/data change;
4. legacy values are not guessed or backfilled;
5. current conversation keys and transcript rows are unchanged;
6. malformed/unexpected database state fails closed;
7. the diagnostic command opens the database read-only and needs no credentials;
8. service remains inactive and disabled.

## Diagnostic command after reviewed migration

```sh
python3 -I -B /opt/wellbeing/telegram-single-entity-mvp-r02/dialogue_mvp.py \
  diagnose-routing \
  --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json \
  --update-id UPDATE_ID
```

The existing code-root name may be retained only if SIS proves exact versioned-byte placement and rollback. A new versioned root is preferable but is not selected by this package.

## Rollback

Rollback requires the separately preserved predecessor bytes and database pre-state. Because SQLite `ALTER TABLE ADD COLUMN` is additive, restoring only the predecessor code while leaving added nullable columns is expected to be compatible, but SIS must prove that against an exact disposable copy before relying on it. If exact pre-state or proof is unavailable, rollback is `BLOCKED_PRESTATE_MISMATCH`, not inferred.

Rollback must not delete the state database, transcript, allowlist, credentials, or either code version.

## Explicitly outside this gate

- service start/enable;
- live `getUpdates` or `sendMessage`;
- OpenAI request;
- credential readout;
- Telegram rights/webhook changes;
- allowlist/admission/provider/model/conversation-key changes;
- replay of r0.1/r0.2/r0.3 live authorities.

---
КТО: KOD / КОДЕР v0.5
СТАТУС: INSTALL_READINESS_CONTRACT_ONLY; CANDIDATE_NOT_INSTALLED
