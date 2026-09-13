# SIS → KOO: Telegram Phase 1B — Termux one-block

```sh
ssh -t -p 2222 pev5691@uk.wbnetrus.ru 'sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh; rc=$?; echo; echo "=== SIS RETURN ==="; tail -n 40 /home/pev5691/sis-phase1b-tooling/host-gate-evidence.txt 2>/dev/null || true; echo "SCRIPT_RC=$rc"'
```

ОПЕРАТОР вводит только пароль SSH и затем пароль `sudo`, если они будут запрошены. Пароли в чат и GitHub не копировать.

После завершения прислать обратно только блок от `=== SIS RETURN ===` до `SCRIPT_RC=...` включительно. Широкая диагностика, повторная установка tooling и дополнительные проверки не требуются.

Граница: live Telegram send, production/public webhook и реальные Telegram credentials этим блоком не разрешены.

Основание: `entities/koordinator/outbox/KOO__telegram-phase1b-termux-oneblock__SIS.md`, commit `808adad72df1340c78e58c8085ba1f885bde1f16`, blob `85081c6fb136658636068ffea891ea6f670010de`.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ один короткий Termux copy-paste блок поверх уже подготовленного tooling path
СТАТУС: operator_handoff_ready
