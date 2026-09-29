# Upgrade contract: installed dialogue MVP r0.1 → discussion admission r0.2

Status: reviewable procedure only. Not executed by KOD.

## Preconditions for a future SIS task

- exact host is `ruvds-xnqc6`;
- service `wellbeing-telegram-single-entity-pilot.service` is inactive and disabled before mutation;
- immutable r0.2 package identity and checksums pass independent readback;
- current r0.1 unit and runtime config bytes are preserved before replacement;
- a NEW exact SIS task authorizes only the named install/verify mutations;
- no service start, credential read, Telegram call or OpenAI call is implied.

Any mismatch stops the upgrade.

## Exact target delta

| Object | r0.1 | r0.2 | Action |
|---|---|---|---|
| code root | `/opt/wellbeing/telegram-single-entity-mvp-r01` | `/opt/wellbeing/telegram-single-entity-mvp-r02` | create versioned root; do not overwrite r0.1 |
| runtime schema | `TELEGRAM_ENTITY_DIALOGUE_MVP_R01` | `TELEGRAM_ENTITY_DIALOGUE_MVP_R02` | replace config only after preserved pre-state |
| admitted chat type | `private` | `supergroup` | exact replacement |
| admitted chat | tester ID reused as chat ID | `-1002429106148` | add frozen `discussion_chat_id` |
| bot identity | absent | ID `8866633840`, username `WBNP_Media_Bot` | add frozen fields |
| activation | any admitted private text | reply-to-bot, exact mention, or exact `/ask` command | add explicit trigger gate |
| service code path | r0.1 root | r0.2 root | replace only `WorkingDirectory` and `ExecStart` paths |
| service name | unchanged | unchanged | no new service |
| state DB | existing path | unchanged | preserve; no delete/reset |
| tester allowlist | existing protected file | unchanged | preserve; contains user IDs, not chat ID |
| credential slots | existing systemd sources | unchanged | preserve; values must not be read or printed |

No migration of the SQLite schema is required: tables and state encoding remain compatible. r0.2 changes the conversation-key domain label, so new discussion turns do not collide with old private-chat transcript keys.

## Runtime config delta

Apply these semantic changes to the independently read-back current config:

```diff
-  "allowed_chat_types": ["private"],
+  "activation_command": "ask",
+  "allowed_chat_types": ["supergroup"],
+  "bot_user_id": 8866633840,
+  "bot_username": "WBNP_Media_Bot",
+  "discussion_chat_id": -1002429106148,
-  "entity_bootstrap_path": "/opt/wellbeing/telegram-single-entity-mvp-r01/entity_bootstrap.txt",
+  "entity_bootstrap_path": "/opt/wellbeing/telegram-single-entity-mvp-r02/entity_bootstrap.txt",
-  "schema": "TELEGRAM_ENTITY_DIALOGUE_MVP_R01",
+  "schema": "TELEGRAM_ENTITY_DIALOGUE_MVP_R02",
```

All other keys and bounds remain unchanged. Unknown keys, another chat/bot identity, another command or a missing field fail config validation.

## Unit delta

```diff
-Description=Wellbeing Telegram single-Entity closed pilot r0.1
+Description=Wellbeing Telegram single-Entity discussion pilot r0.2
-WorkingDirectory=/opt/wellbeing/telegram-single-entity-mvp-r01
-ExecStart=/usr/bin/python3 -I -B /opt/wellbeing/telegram-single-entity-mvp-r01/dialogue_mvp.py poll --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json
+WorkingDirectory=/opt/wellbeing/telegram-single-entity-mvp-r02
+ExecStart=/usr/bin/python3 -I -B /opt/wellbeing/telegram-single-entity-mvp-r02/dialogue_mvp.py poll --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json
```

`LoadCredential`, principal, hardening, state directory, network families, restart policy and service name remain unchanged.

## Future install/verify-only sequence

The exact SIS implementation may use equivalent fail-closed operations, but it must prove the same states:

1. Read service active/enabled state and stop on any unexpected activity.
2. Read and preserve exact current unit/config bytes plus their SHA-256 identities without reading credential values.
3. Create `/opt/wellbeing/telegram-single-entity-mvp-r02` with the existing owner/group/mode contract.
4. Install only `dialogue_mvp.py` and `entity_bootstrap.txt` from the verified package.
5. Materialize the exact r0.2 runtime config while preserving the tester allowlist, state DB and credential slots.
6. Install the reviewed r0.2 unit bytes.
7. Run package checksum verification, 24 offline tests, `py_compile`, `systemd-analyze verify`, and unprivileged `check-config`.
8. Run `systemctl daemon-reload` only if exact task authority permits this named unit mutation.
9. Verify service remains inactive and disabled.
10. Publish a sanitized result with pre/post identities. Do not start the service.

## Rollback contract

Rollback is a separate named action within the future exact SIS authority. It restores the preserved r0.1 unit/config bytes, runs `daemon-reload`, verifies the r0.1 config against the preserved r0.1 code root, and confirms the service remains inactive/disabled.

Rollback must not:

- delete either versioned code root;
- delete/reset the SQLite state;
- read, rewrite or expose credential values;
- change the tester allowlist;
- start or enable the service.

If exact predecessor bytes were not preserved or do not match their recorded identities, rollback is `BLOCKED_PRESTATE_MISMATCH`, not guessed reconstruction.

---
КТО: KOD / КОДЕР v0.5
ДЛЯ ЧЕГО: exact install/verify/rollback delta for SIS review
СТАТУС: DOCUMENTED_NOT_EXECUTED
